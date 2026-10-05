"""Strict verifier contracts and deterministic acceptance gates."""
import json
import re
from evidence import Blocked

PLACEHOLDER = re.compile(r'\{\{([A-Z_]+)\}\}')


def fill_template(template: str, values: dict) -> str:
    """Substitute only original template tokens, once; data is never a template."""
    missing = set(PLACEHOLDER.findall(template)) - values.keys()
    if missing:
        raise Blocked('Missing template variables: ' + ', '.join(sorted(missing)))
    return PLACEHOLDER.sub(lambda match: str(values[match[1]]), template)


def strict_json(text: str) -> dict:
    """Reject markdown, duplicate keys, non-object roots and nonfinite numbers."""
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise Blocked('Duplicate JSON field.')
            result[key] = value
        return result
    try:
        value = json.loads(text, object_pairs_hook=unique,
                           parse_constant=lambda value: (_ for _ in ()).throw(Blocked('Nonfinite JSON.')))
    except (ValueError, TypeError):
        raise Blocked('Invalid machine-readable JSON.') from None
    if not isinstance(value, dict):
        raise Blocked('Expected JSON object.')
    return value


def parse_verifier_result(text: str, checklist: list[dict], evidence: dict) -> dict:
    """Validate every criterion and citation; model PASS alone is never acceptance."""
    result = strict_json(text)
    if set(result) != {'result', 'reason', 'feedback', 'criteria'} or not isinstance(result['result'], str) or result['result'] not in {'PASS', 'FAIL', 'BLOCKED'}:
        raise Blocked('Invalid verifier contract.')
    if any(not isinstance(result[k], str) for k in ('reason', 'feedback')) or not result['reason'].strip():
        raise Blocked('Verifier reason is mandatory.')
    if not isinstance(result['criteria'], list):
        raise Blocked('Criterion evaluations must be a list.')
    expected = {item['id']: item for item in checklist}
    observed = {}
    files = {item['path']: item for item in evidence['source']}
    for item in result['criteria']:
        if not isinstance(item, dict) or set(item) != {'id', 'status', 'reason', 'citations'}:
            raise Blocked('Invalid criterion shape.')
        if not isinstance(item['id'], str) or not isinstance(item['status'], str) or item['id'] not in expected or item['id'] in observed or item['status'] not in {'PASS', 'FAIL', 'NOT_APPLICABLE', 'INSUFFICIENT_EVIDENCE'}:
            raise Blocked('Unknown/duplicate criterion or invalid status.')
        if not isinstance(item['reason'], str) or not item['reason'].strip() or not isinstance(item['citations'], list):
            raise Blocked('Criterion reason/citations missing.')
        for citation in item['citations']:
            if not isinstance(citation, dict) or set(citation) != {'path', 'line'}:
                raise Blocked('Invalid citation shape.')
            if not isinstance(citation['path'], str) or citation['path'] not in files or type(citation['line']) is not int or not 1 <= citation['line'] <= len(files[citation['path']]['lines']):
                raise Blocked('Citation does not identify supplied source.')
        if item['status'] == 'PASS' and not item['citations']:
            raise Blocked('Criterion PASS requires source evidence.')
        observed[item['id']] = item
    if observed.keys() != expected.keys():
        raise Blocked('Verifier did not evaluate every criterion.')
    if result['result'] == 'PASS':
        if not evidence['tests'] or any(test['returncode'] != 0 for test in evidence['tests']):
            raise Blocked('Tests are missing or failed; PASS rejected.')
        for name, criterion in expected.items():
            if criterion['mandatory'] and observed[name]['status'] != 'PASS':
                raise Blocked('Mandatory criterion is not PASS.')
            if observed[name]['status'] == 'FAIL':
                raise Blocked('Failed criterion cannot produce overall PASS.')
    return result
