"""Offline behavior tests: synthetic repos, real local checks, injected model responses."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import auto_review as runner
from contracts import fill_template, parse_verifier_result, strict_json
from evidence import Blocked, apply_proposal, collect_source, digest, git_evidence, source_evidence


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / 'calc.py').write_text('VALUE = 1\n', encoding='utf-8')
        self.config = {'target_repository': str(self.root), 'source_scopes': ['calc.py'],
            'mode': 'review', 'require_git': False, 'checklist': 'config/checklist.json',
            'checklist_confirmed': True, 'max_attempts': 3, 'generator_argv': ['codex'],
            'model': 'gpt-4o', 'api_key_env': 'OPENAI_API_KEY', 'timeout': 30,
            'tests_authorized': True, 'tests': [{'id': 'unit', 'argv': [sys.executable, '-c',
                "import calc; assert calc.VALUE == 1; print('verified')"], 'timeout': 10}]}
        self.criteria = runner.load_checklist_text(runner.local_file(self.config['checklist']))
        self.evidence = {'source': source_evidence({'calc.py': 'VALUE = 1\n'}),
                         'tests': [{'id': 'unit', 'returncode': 0}]}

    def verdict(self, result='PASS'):
        return {'result': result, 'reason': 'Host evidence assessed.', 'feedback': '' if result == 'PASS' else 'Fix logic.\nKeep scope.',
                'criteria': [{'id': c['id'], 'status': result, 'reason': 'Actual source line.',
                              'citations': [{'path': 'calc.py', 'line': 1}]} for c in self.criteria]}

    def test_single_substitution_preserves_user_tokens(self):
        self.assertEqual(fill_template('{{TASK}} {{FEEDBACK}}', {'TASK': '{{FEEDBACK}}', 'FEEDBACK': 'fix'}), '{{FEEDBACK}} fix')

    def test_missing_template_value_blocks(self):
        with self.assertRaises(Blocked):
            fill_template('{{MISSING}}', {})

    def test_json_rejects_markdown_and_duplicates(self):
        for value in ['```json\n{}\n```', '{"result":"FAIL","result":"PASS"}', 'KET_QUA: PASS', '[]']:
            with self.subTest(value=value), self.assertRaises(Blocked):
                strict_json(value)

    def test_multiline_feedback_preserved(self):
        result = parse_verifier_result(json.dumps(self.verdict('FAIL')), self.criteria, self.evidence)
        self.assertIn('\n', result['feedback'])

    def test_missing_fields_never_pass(self):
        with self.assertRaises(Blocked):
            parse_verifier_result('{"result":"PASS"}', self.criteria, self.evidence)

    def test_bad_citation_never_pass(self):
        value = self.verdict()
        value['criteria'][0]['citations'][0]['line'] = 999
        with self.assertRaises(Blocked):
            parse_verifier_result(json.dumps(value), self.criteria, self.evidence)

    def test_mandatory_not_applicable_never_pass(self):
        value = self.verdict()
        value['criteria'][0]['status'] = 'NOT_APPLICABLE'
        with self.assertRaises(Blocked):
            parse_verifier_result(json.dumps(value), self.criteria, self.evidence)

    def test_missing_and_failed_tests_block_pass(self):
        for tests in [[], [{'returncode': 1}]]:
            with self.subTest(tests=tests), self.assertRaises(Blocked):
                parse_verifier_result(json.dumps(self.verdict()), self.criteria, {'source': self.evidence['source'], 'tests': tests})

    def test_malformed_types_block_without_traceback(self):
        value = self.verdict()
        value['criteria'][0]['id'] = []
        with self.assertRaises(Blocked):
            parse_verifier_result(json.dumps(value), self.criteria, self.evidence)

    def test_pass_is_only_human_candidate(self):
        def verify(payload, config):
            data = json.loads(payload)
            self.assertIn('verified', data['evidence']['tests'][0]['stdout'])
            self.assertEqual(data['evidence']['source'][0]['lines'][0]['number'], 1)
            return json.dumps(self.verdict())
        report = runner.pipeline('Review', self.config, allow_edits=False, verify=verify)
        self.assertEqual(report['status'], 'AWAITING_HUMAN')
        self.assertEqual(len(report['history']), 1)

    def test_review_fail_does_not_generate_or_retry(self):
        report = runner.pipeline('Review', self.config, allow_edits=False,
                                 verify=lambda *args: json.dumps(self.verdict('FAIL')),
                                 generate=lambda *args: self.fail('must not generate'))
        self.assertEqual(report['status'], 'FAIL')
        self.assertEqual(len(report['history']), 1)

    def test_generate_requires_explicit_permission(self):
        self.config['mode'] = 'generate'
        with self.assertRaises(Blocked):
            runner.pipeline('Fix', self.config, allow_edits=False)

    def test_generator_failure_never_calls_verifier(self):
        self.config['mode'] = 'generate'
        def fail(*args):
            raise Blocked('Generator unavailable')
        with self.assertRaises(Blocked):
            runner.pipeline('Fix', self.config, allow_edits=True, generate=fail,
                            verify=lambda *args: self.fail('verifier called after generator error'))

    def test_generator_reads_real_repository_and_host_applies(self):
        self.config['mode'] = 'generate'
        def generate(prompt, config, root):
            self.assertEqual(root, self.root)
            self.assertIn('VALUE = 1', prompt)
            return {'summary': 'Fix formatting', 'files': [{'path': 'calc.py', 'content': 'VALUE = 1  # reviewed\n'}]}
        report = runner.pipeline('Fix', self.config, allow_edits=True, generate=generate,
                                 verify=lambda *args: json.dumps(self.verdict()))
        self.assertEqual(report['status'], 'AWAITING_HUMAN')
        self.assertIn('reviewed', (self.root / 'calc.py').read_text())

    def test_stale_source_after_tests_blocks(self):
        self.config['tests'][0]['argv'] = [sys.executable, '-c', "from pathlib import Path; Path('calc.py').write_text('VALUE = 2')"]
        with self.assertRaises(Blocked):
            runner.pipeline('Review', self.config, allow_edits=False, verify=lambda *args: self.fail('stale verifier called'))

    def test_failed_real_check_cannot_pass(self):
        self.config['tests'][0]['argv'] = [sys.executable, '-c', 'raise SystemExit(1)']
        with self.assertRaises(Blocked):
            runner.pipeline('Review', self.config, allow_edits=False, verify=lambda *args: json.dumps(self.verdict()))

    def test_identical_retry_stops(self):
        self.config['mode'] = 'generate'
        calls = []
        def generate(*args):
            calls.append(1)
            return {'summary': 'No changes', 'files': []}
        report = runner.pipeline('Fix', self.config, allow_edits=True, generate=generate,
                                 verify=lambda *args: json.dumps(self.verdict('FAIL')))
        self.assertEqual(report['status'], 'BLOCKED')
        self.assertEqual(len(calls), 2)

    def test_traversal_rejected(self):
        with self.assertRaises(Blocked):
            apply_proposal(self.root, collect_source(self.root, ['calc.py']),
                           [{'path': '../escape.py', 'content': 'x'}], ['calc.py'])

    def test_concurrent_change_preserved(self):
        baseline = collect_source(self.root, ['calc.py'])
        (self.root / 'calc.py').write_text('user edit')
        with self.assertRaises(Blocked):
            apply_proposal(self.root, baseline, [{'path': 'calc.py', 'content': 'overwrite'}], ['calc.py'])
        self.assertEqual((self.root / 'calc.py').read_text(), 'user edit')

    def test_secret_files_excluded_before_reading(self):
        (self.root / 'secrets.json').write_text('not for evidence')
        (self.root / 'credentials.txt').write_text('not for evidence')
        files = collect_source(self.root, ['calc.py'])
        self.assertEqual(set(files), {'calc.py'})

    def test_secret_pattern_blocks_double_quoted_source(self):
        with self.assertRaises(Blocked):
            runner.checked_data({'source': 'api_key = "synthetic-not-a-real-key"'})

    def test_gitless_explicit_and_parent_repo_not_assumed(self):
        files = collect_source(self.root, ['calc.py'])
        self.assertFalse(git_evidence(self.root, files, False)['available'])
        with self.assertRaises(Blocked):
            git_evidence(self.root, files, True)

    def test_no_implicit_target_and_no_confirmed_checklist(self):
        for key, value in [('target_repository', ''), ('checklist_confirmed', False), ('tests', [])]:
            config = copy.deepcopy(self.config)
            config[key] = value
            with self.subTest(key=key), self.assertRaises(Blocked):
                runner.validate_config(config)

    def test_log_contains_metadata_only(self):
        library = self.root / 'library'
        library.mkdir()
        with patch.object(runner, 'BASE_DIR', library):
            path = runner.save_log({'status': 'FAIL', 'candidate': {'reason': 'must not log'}, 'task': 'must not log', 'history': []})
            text = path.read_text()
            self.assertNotIn('must not log', text)

    def test_codex_receives_stdin_and_explicit_cwd(self):
        from types import SimpleNamespace
        with patch.object(runner, 'run_command', return_value=SimpleNamespace(returncode=0, stdout='{"summary":"ok","files":[]}')) as command:
            runner.run_codex('untrusted task', self.config, self.root)
            args, kwargs = command.call_args
            self.assertEqual(args[1], self.root)
            self.assertNotIn('untrusted task', args[0])
            self.assertEqual(kwargs['stdin'], 'untrusted task')
            self.assertIn('read-only', args[0])


if __name__ == '__main__':
    unittest.main()
