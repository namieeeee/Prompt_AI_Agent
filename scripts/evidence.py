"""Bounded source evidence, constrained changes, and explicit test commands."""
from __future__ import annotations
import difflib
import hashlib
import json
import os
import shutil
from pathlib import Path, PurePosixPath
import subprocess
import tempfile


class Blocked(Exception):
    """Missing, ambiguous or unsafe evidence/configuration."""


EXCLUDED = {'.git', '.venv', 'node_modules', 'bin', 'obj', 'dist', 'build',
            '__pycache__', '.aws', '.ssh', '.codex', '.pytest_cache', 'logs'}
SECRET_NAMES = ('password', 'credential', 'secret', 'token', 'id_rsa', 'id_ed25519')
TEXT_EXTENSIONS = {'.py', '.ts', '.tsx', '.js', '.jsx', '.cs', '.json', '.yaml',
                   '.yml', '.toml', '.md', '.txt', '.html', '.css', '.sql', '.xml'}


def safe_name(name: str) -> bool:
    """Exclude secrets, runtime data and generated paths before reading bytes."""
    parts = PurePosixPath(name).parts
    return bool(parts) and not any(
        p.lower() in EXCLUDED or p.startswith('.') or
        any(p.lower().startswith(prefix) for prefix in SECRET_NAMES) or
        Path(p).suffix.lower() in {'.pem', '.key', '.mbkey', '.pfx', '.xlsx', '.mbenc'}
        for p in parts
    )


def scoped_path(root: Path, name: str, scopes: list[str]) -> Path:
    """Reject traversal, links, alternate streams and files outside curated scopes."""
    if not isinstance(name, str) or '\\' in name or ':' in name:
        raise Blocked('Paths must be relative POSIX paths without drive/stream names.')
    parts = PurePosixPath(name).parts
    if not parts or '..' in parts or PurePosixPath(name).is_absolute() or not safe_name(name):
        raise Blocked('Unsafe or sensitive source path.')
    if not any(name == scope or name.startswith(scope.rstrip('/') + '/') for scope in scopes):
        raise Blocked('File is outside configured source scopes.')
    path = root
    for part in parts:
        path = path / part
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            raise Blocked('Source links/junctions are unsupported.')
        if path.exists() and path.resolve() != path.absolute():
            raise Blocked('Path resolves through a reparse point.')
    if not path.resolve().is_relative_to(root.resolve()):
        raise Blocked('Source path escapes repository.')
    return path


def digest(data: object) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def collect_source(root: Path, scopes: list[str], budget: int = 1_000_000) -> dict[str, str]:
    """Collect only explicitly scoped text; never truncate to make a run succeed."""
    files: dict[str, str] = {}
    total = 0
    for scope in scopes:
        path = scoped_path(root, scope, scopes)
        candidates = [path] if path.is_file() else []
        if path.is_dir():
            for directory, dirs, names in os.walk(path, followlinks=False):
                dirs[:] = [n for n in dirs if safe_name(n)]
                for name in names:
                    candidate = Path(directory) / name
                    relative = candidate.relative_to(root).as_posix()
                    if safe_name(relative) and candidate.suffix.lower() in TEXT_EXTENSIONS:
                        candidates.append(candidate)
        for candidate in candidates:
            name = candidate.relative_to(root).as_posix()
            checked = scoped_path(root, name, scopes)
            if checked.suffix.lower() not in TEXT_EXTENSIONS:
                raise Blocked('Explicit evidence file is not a supported text format.')
            size = checked.stat().st_size
            if size > budget or total + size > budget:
                raise Blocked('Source evidence exceeds budget; narrow source_scopes.')
            try:
                with checked.open('rb') as stream:
                    raw = stream.read(budget + 1)
                if total + len(raw) > budget:
                    raise Blocked('Source grew beyond evidence budget.')
                content = raw.decode('utf-8')
            except (UnicodeError, OSError):
                raise Blocked('Cannot read scoped UTF-8 source.') from None
            if name not in files:
                total += len(content.encode())
                files[name] = content
    if not files:
        raise Blocked('No scoped source evidence found.')
    return dict(sorted(files.items()))


def run_command(argv: list[str], root: Path, timeout: int = 120, stdin: str | None = None) -> subprocess.CompletedProcess:
    """Run operator-selected argv directly, with an explicit cwd and timeout."""
    if not argv or any(not isinstance(x, str) or not x for x in argv):
        raise Blocked('Invalid command argv.')
    executable = shutil.which(argv[0]) or argv[0]
    if Path(executable).suffix.lower() in {'.bat', '.cmd'}:
        raise Blocked('Configure a native executable or node + CLI JavaScript, not a batch wrapper.')
    try:
        return subprocess.run(argv, cwd=root, input=stdin, capture_output=True,
                              text=True, encoding='utf-8', errors='replace',
                              timeout=timeout, shell=False)
    except (OSError, subprocess.TimeoutExpired):
        raise Blocked('Command unavailable or timed out.') from None


def git_evidence(root: Path, files: dict[str, str], required: bool) -> dict:
    """Require an exact Git root; read baseline bytes only for scoped safe files."""
    if not (root / '.git').exists():
        if required:
            raise Blocked('Target must have its own Git root; parent/home repositories are not accepted.')
        return {'available': False, 'limitation': 'gitless snapshot; no HEAD baseline', 'diff': ''}
    result = run_command(['git', 'rev-parse', '--show-toplevel'], root)
    if result.returncode or Path(result.stdout.strip()).resolve() != root.resolve():
        raise Blocked('Cannot verify exact target Git root.')
    head = run_command(['git', 'rev-parse', '--verify', 'HEAD'], root)
    if head.returncode:
        raise Blocked('Git evidence requires an existing HEAD commit.')
    status = run_command(['git', 'status', '--porcelain', '-z', '--untracked-files=all'], root)
    if status.returncode:
        raise Blocked('Cannot obtain Git status.')
    diffs = []
    for name, current in files.items():
        tracked = run_command(['git', 'ls-tree', '--name-only', 'HEAD', '--', name], root)
        if tracked.returncode:
            raise Blocked('Cannot enumerate Git baseline.')
        old = ''
        if tracked.stdout.strip():
            result = run_command(['git', 'show', f'HEAD:{name}'], root)
            if result.returncode:
                raise Blocked('Cannot read scoped Git baseline.')
            old = result.stdout
        diffs.extend(difflib.unified_diff(old.splitlines(True), current.splitlines(True),
                                        fromfile=f'HEAD/{name}', tofile=name))
    return {'available': True, 'head': head.stdout.strip(),
            'status': status.stdout, 'diff': ''.join(diffs)}


def source_evidence(files: dict[str, str]) -> list[dict]:
    """Supply accurate line numbers and content hashes for verifier citations."""
    result = []
    for name, content in files.items():
        parts = name.lower().split('/')
        category = 'tests' if any(x in {'tests', 'test', '__tests__'} for x in parts) else (
            'migrations' if 'migrations' in parts else 'config' if Path(name).suffix in {'.json', '.yaml', '.yml', '.toml'}
            else 'frontend' if Path(name).suffix in {'.tsx', '.jsx', '.html', '.css'} or 'frontend' in parts
            else 'backend' if Path(name).suffix in {'.py', '.cs'} or 'backend' in parts else 'other')
        result.append({'path': name, 'category': category, 'sha256': digest(content),
                       'lines': [{'number': i, 'text': line} for i, line in enumerate(content.splitlines(), 1)]})
    return result


def apply_proposal(root: Path, baseline: dict[str, str], replacements: list[dict], scopes: list[str]) -> None:
    """Apply complete scoped replacements; preserve unrelated files and refuse races."""
    if collect_source(root, scopes) != baseline:
        raise Blocked('Source changed concurrently; refusing proposal.')
    seen = set()
    validated = []
    for item in replacements:
        if not isinstance(item, dict) or set(item) != {'path', 'content'} or not isinstance(item['content'], str):
            raise Blocked('Invalid replacement shape.')
        name = item['path']
        path = scoped_path(root, name, scopes)
        if name in seen or path.suffix.lower() not in TEXT_EXTENSIONS or path.name in {'AGENTS.md', 'SKILL.md'}:
            raise Blocked('Duplicate, instruction or unsupported replacement.')
        if path.exists() and (not path.is_file() or path.stat().st_nlink > 1):
            raise Blocked('Cannot replace directories or hard-linked files.')
        if not path.parent.is_dir():
            raise Blocked('Create target directories manually before proposing new files.')
        seen.add(name)
        validated.append((path, item['content']))
    for path, content in validated:
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='',
                                             dir=path.parent, delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
