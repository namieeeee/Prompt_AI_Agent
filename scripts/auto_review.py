"""Evidence-based local Generator/Verifier runner. No target is chosen implicitly."""
from __future__ import annotations
import argparse
import difflib
import json
from pathlib import Path
import re
import sys
import uuid

from contracts import fill_template, parse_verifier_result, strict_json
from evidence import Blocked, apply_proposal, collect_source, digest, git_evidence, run_command, source_evidence

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_PATTERN = re.compile(r'sk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|(?:password|api_key|token|secret)\s*[:=]\s*[\"\x27][^\"\x27\n]{8,}[\"\x27]', re.I)


def checked_data(data: object) -> str:
    """Stop instead of sending source/test data containing recognizable secrets."""
    def scan(value):
        if isinstance(value, str) and SECRET_PATTERN.search(value):
            raise Blocked('Potential secret in evidence; curate/redact inputs before sending.')
        if isinstance(value, dict):
            for child in value.values():
                scan(child)
        elif isinstance(value, list):
            for child in value:
                scan(child)
    scan(data)
    text = json.dumps(data, ensure_ascii=False)
    if len(text.encode()) > 2_000_000:
        raise Blocked('Combined evidence budget exceeded.')
    return text


def local_file(name: str) -> Path:
    path = (BASE_DIR / name).resolve()
    if not path.is_relative_to(BASE_DIR) or not path.is_file():
        raise Blocked('Missing or out-of-library resource.')
    return path


def load_config(path: Path) -> dict:
    """Load JSON or YAML configuration; validate before executing any tools."""
    if path.suffix == '.json':
        return strict_json(path.read_text(encoding='utf-8'))
    try:
        import yaml
    except ImportError:
        raise Blocked('Install requirements.txt to read YAML config.') from None
    value = yaml.safe_load(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise Blocked('Config must be a mapping.')
    return value


def validate_config(config: dict) -> Path:
    try:
        if not isinstance(config['target_repository'], str) or not config['target_repository']:
            raise Blocked('Configure target_repository first.')
        root = Path(config['target_repository']).resolve()
        if not root.is_dir() or root == BASE_DIR:
            raise Blocked('Target must be an existing repository separate from prompt_library.')
        scopes = config['source_scopes']
        if not isinstance(scopes, list) or not scopes or any(not isinstance(s, str) or not s for s in scopes):
            raise Blocked('Configure nonempty source_scopes.')
        if type(config['max_attempts']) is not int or not 1 <= config['max_attempts'] <= 3:
            raise Blocked('max_attempts must be 1..3, including the first attempt.')
        if config['mode'] not in {'review', 'generate'}:
            raise Blocked('mode must be review or generate.')
        if config['checklist_confirmed'] is not True:
            raise Blocked('Review the checklist and set checklist_confirmed: true.')
        if type(config['require_git']) is not bool or type(config['tests_authorized']) is not bool:
            raise Blocked('Git/test flags must be booleans.')
        if not isinstance(config['tests'], list) or not config['tests']:
            raise Blocked('Configure at least one test/build command.')
        ids = set()
        for test in config['tests']:
            if set(test) != {'id', 'argv', 'timeout'} or not isinstance(test['id'], str) or not test['id'] or test['id'] in ids:
                raise Blocked('Invalid or duplicate test profile.')
            ids.add(test['id'])
            if not isinstance(test['argv'], list) or not test['argv'] or any(not isinstance(v, str) or not v for v in test['argv']):
                raise Blocked('Test commands must be explicit argv lists.')
            if type(test['timeout']) is not int or not 1 <= test['timeout'] <= 600:
                raise Blocked('Test timeout must be 1..600 seconds.')
        if type(config['timeout']) is not int or not 1 <= config['timeout'] <= 600:
            raise Blocked('Pipeline timeout must be 1..600 seconds.')
        for key in ('model', 'api_key_env', 'checklist'):
            if not isinstance(config[key], str) or not config[key]:
                raise Blocked('Missing model/API variable/checklist setting.')
        if not isinstance(config['generator_argv'], list) or not config['generator_argv']:
            raise Blocked('Configure generator_argv.')
        return root
    except (KeyError, TypeError):
        raise Blocked('Incomplete or invalid configuration.') from None


def load_checklist_text(path: Path) -> list[dict]:
    """Load structured criteria. Legacy XLSX remains available for manual migration."""
    if path.suffix != '.json':
        raise Blocked('Migrate checklist.xlsx to the documented JSON criterion schema.')
    value = strict_json(path.read_text(encoding='utf-8'))
    if set(value) != {'criteria'} or not isinstance(value['criteria'], list) or not value['criteria']:
        raise Blocked('Checklist has no criteria.')
    seen = set()
    for item in value['criteria']:
        if not isinstance(item, dict) or set(item) != {'id', 'description', 'mandatory'}:
            raise Blocked('Invalid checklist criterion.')
        if not isinstance(item['id'], str) or not item['id'].strip() or item['id'] in seen:
            raise Blocked('Empty or duplicate criterion ID.')
        if not isinstance(item['description'], str) or not item['description'].strip() or type(item['mandatory']) is not bool:
            raise Blocked('Criterion description/mandatory semantics missing.')
        seen.add(item['id'])
    return value['criteria']


def load_prompt_template(name: str) -> str:
    text = local_file(name).read_text(encoding='utf-8')
    if text.startswith('---\n'):
        parts = text.split('---', 2)
        if len(parts) != 3:
            raise Blocked('Unclosed prompt front matter.')
        text = parts[2]
    return text.strip()


def run_codex(prompt: str, config: dict, root: Path) -> dict:
    """Ask a read-only Codex process for scoped proposals, never stdout-as-evidence."""
    schema = local_file('config/generator.schema.json')
    argv = config['generator_argv'] + ['exec', '--ignore-user-config', '--ephemeral',
             '--sandbox', 'read-only', '--output-schema', str(schema), '-']
    result = run_command(argv, root, config['timeout'], stdin=prompt)
    if result.returncode:
        raise Blocked('Generator failed; no proposal or verifier acceptance.')
    proposal = strict_json(result.stdout)
    if set(proposal) != {'summary', 'files'} or not isinstance(proposal['summary'], str) or not isinstance(proposal['files'], list):
        raise Blocked('Generator proposal contract invalid.')
    checked_data(proposal)
    return proposal


def run_gpt_verifier(prompt: str, config: dict) -> str:
    """Use a separate system instruction and strict schema; errors are not review results."""
    try:
        from openai import OpenAI
        schema = strict_json(local_file('config/verifier.schema.json').read_text(encoding='utf-8'))
        with OpenAI(timeout=config['timeout'], max_retries=0) as client:
            response = client.chat.completions.create(
                model=config['model'],
                messages=[{'role': 'system', 'content': load_prompt_template('prompts/verifier_gpt.prompt.md')},
                          {'role': 'user', 'content': prompt}],
                response_format={'type': 'json_schema', 'json_schema': {'name': 'review_result', 'strict': True, 'schema': schema}},
            )
        message = response.choices[0].message
        if message.refusal or not message.content:
            raise Blocked('Verifier refused or returned no content.')
        return message.content
    except Blocked:
        raise
    except Exception:
        raise Blocked('Verifier/API unavailable; no acceptance or code retry.') from None


def execute_tests(config: dict, root: Path) -> list[dict]:
    if config['tests_authorized'] is not True:
        raise Blocked('Review commands/code and explicitly authorize configured tests first.')
    results = []
    for test in config['tests']:
        result = run_command(test['argv'], root, test['timeout'])
        evidence = {'id': test['id'], 'argv': test['argv'], 'returncode': result.returncode,
                    'stdout': result.stdout, 'stderr': result.stderr}
        checked_data(evidence)
        results.append(evidence)
    return results


def pipeline(task: str, config: dict, *, allow_edits: bool, generate=run_codex, verify=run_gpt_verifier) -> dict:
    """Gather host evidence, retry actual fixes, and return a human-review candidate."""
    root = validate_config(config)
    checklist = load_checklist_text(local_file(config['checklist']))
    scopes = config['source_scopes']
    if config['mode'] == 'generate' and not allow_edits:
        raise Blocked('Generate mode requires --allow-edits for host-applied replacements.')
    rules = local_file('AGENTS.md').read_text(encoding='utf-8')
    target_rules = []
    instruction = root / 'AGENTS.md'
    if instruction.is_file():
        if instruction.is_symlink() or instruction.stat().st_size > 32_768:
            raise Blocked('Target instructions are linked or exceed budget.')
        target_rules.append({'path': 'AGENTS.md', 'content': instruction.read_text(encoding='utf-8')})
    skill = local_file('skills/nghiem-thu-code/SKILL.md').read_text(encoding='utf-8')
    initial = collect_source(root, scopes)
    baseline_git = git_evidence(root, initial, config['require_git'])
    feedback = None
    previous_signature = None
    history = []
    for attempt in range(1, config['max_attempts'] + 1):
        before = collect_source(root, scopes)
        if config['mode'] == 'generate':
            payload = checked_data({'task': task, 'checklist': checklist, 'source': source_evidence(before),
                                    'source_scopes': scopes, 'target_instructions': target_rules,
                                    'current_git': git_evidence(root, before, config['require_git']), 'previous_feedback': feedback})
            prompt = fill_template(load_prompt_template('prompts/generator_codex.prompt.md'),
                                   {'RULES': rules, 'SKILL': skill, 'DATA_JSON': payload})
            proposal = generate(prompt, config, root)
            apply_proposal(root, before, proposal['files'], scopes)
        current = collect_source(root, scopes)
        initial_diff = ''.join(line for name in sorted(initial.keys() | current.keys())
            for line in difflib.unified_diff(initial.get(name, '').splitlines(True), current.get(name, '').splitlines(True),
                                             fromfile='initial/' + name, tofile=name))
        evidence = {'source': source_evidence(current), 'git': git_evidence(root, current, config['require_git']),
                    'initial_git': baseline_git, 'initial_to_current_diff': initial_diff,
                    'changed_since_start': [name for name in sorted(initial.keys() | current.keys()) if initial.get(name) != current.get(name)],
                    'tests': execute_tests(config, root)}
        if collect_source(root, scopes) != current:
            raise Blocked('Tests/concurrent process changed source; evidence is stale.')
        request = checked_data({'task': task, 'rules': rules, 'target_instructions': target_rules,
                               'skill': skill, 'checklist': checklist, 'evidence': evidence})
        result = parse_verifier_result(verify(request, config), checklist, evidence)
        if collect_source(root, scopes) != current:
            raise Blocked('Source changed while verifier ran.')
        history.append({'attempt': attempt, 'result': result['result'], 'source_sha256': digest(current),
                        'tests': [{'id': t['id'], 'returncode': t['returncode']} for t in evidence['tests']]})
        if result['result'] == 'PASS':
            return {'status': 'AWAITING_HUMAN', 'candidate': result, 'source_sha256': digest(current), 'history': history}
        if result['result'] == 'BLOCKED' or config['mode'] == 'review':
            return {'status': result['result'], 'candidate': result, 'history': history}
        signature = digest({'source': current, 'result': result})
        if signature == previous_signature:
            return {'status': 'BLOCKED', 'history': history, 'reason': 'Identical failure repeated.'}
        previous_signature = signature
        feedback = result
    return {'status': 'FAIL', 'history': history, 'reason': 'Attempt budget exhausted.'}


def save_log(report: dict) -> Path:
    """Persist only metadata, never task, source, prompts, keys or model text."""
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    path = log_dir / f'run_{uuid.uuid4().hex}.json'
    data = {'status': report['status'], 'history': report.get('history', []),
            'source_sha256': report.get('source_sha256')}
    with path.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Evidence-based review; config must name a target explicitly.')
    parser.add_argument('task', nargs='?', default='')
    parser.add_argument('--config', type=Path, default=BASE_DIR / 'config/config.yaml')
    parser.add_argument('--preflight', action='store_true')
    parser.add_argument('--allow-edits', action='store_true')
    parser.add_argument('--send-to-openai', action='store_true', help='Authorize sending curated source/test evidence to OpenAI')
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        root = validate_config(config)
        criteria = load_checklist_text(local_file(config['checklist']))
        files = collect_source(root, config['source_scopes'])
        git_evidence(root, files, config['require_git'])
        if args.preflight:
            print(json.dumps({'status': 'READY', 'source_files': len(files), 'criteria': len(criteria)}, indent=2))
            return 0
        if not args.task.strip() or not args.send_to_openai:
            raise Blocked('Provide a task and --send-to-openai after reviewing source scopes.')
        # The SDK reads only this configured variable, never persists its value.
        import os
        if not os.environ.get(config['api_key_env']):
            raise Blocked('Configured API key environment variable is not set.')
        if config['api_key_env'] != 'OPENAI_API_KEY':
            raise Blocked('Use OPENAI_API_KEY for the current SDK adapter.')
        report = pipeline(args.task, config, allow_edits=args.allow_edits)
        if report['status'] == 'AWAITING_HUMAN':
            print(json.dumps(report['candidate'], ensure_ascii=False, indent=2))
            print('Review actual source/diff and tests. Type APPROVE to accept this exact source snapshot.')
            decision = input('Decision: ').strip()
            if digest(collect_source(root, config['source_scopes'])) != report['source_sha256']:
                raise Blocked('Source changed before human decision.')
            report['status'] = 'ACCEPTED' if decision == 'APPROVE' else 'REJECTED'
        elif 'candidate' in report:
            print(json.dumps(report['candidate'], ensure_ascii=False, indent=2))
        elif 'reason' in report:
            print(report['reason'])
        save_log(report)
        print(report['status'])
        return 0 if report['status'] == 'ACCEPTED' else 1
    except (Blocked, OSError, UnicodeError, ValueError, EOFError, KeyboardInterrupt) as error:
        print('BLOCKED: ' + (str(error) if isinstance(error, Blocked) else 'Input, dependency or filesystem operation failed.'), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
