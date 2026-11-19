---
name: security-audit
description: Review repository source code for security vulnerabilities, injection flaws, broken authorization, hardcoded secrets, and unsafe exception handling against OWASP Top 10 and CWE standards.
---
# Security Audit & Vulnerability Triage Workflow

Audit source code changes, API routes, and configuration files against enterprise AppSec criteria using host-collected source, diffs, and test outputs.

### Verification Principles
1. **Injection Prevention**: Scrutinize all untrusted input entry points (HTTP requests, CLI args, environment strings, database queries, file uploads). Every query or command must be parameterized or strictly validated.
2. **Authorization & Access Control**: Validate that caller permissions and roles are checked server-side before executing privileged operations. Prevent Broken Object Level Authorization (BOLA/IDOR).
3. **Secret Zero-Tolerance**: Ensure absolute absence of hardcoded tokens, passwords, private keys, or API keys. Secrets must resolve strictly through validated environment variables or external secret managers.
4. **Information Disclosure Defense**: Inspect catch/rescue blocks to confirm that stack traces, database schema details, and infrastructure hostnames are scrubbed before reaching external consumers.

### Evidence Mapping
- Map checklist criteria (`INJECTION_DEFENSE`, `AUTH_ACCESS`, `SECRET_HYGIENE`, `EXCEPTION_SHIELDING`) to concrete file paths and line numbers.
- Any unresolved security defect or ambiguous validation path must result in `FAIL` or `BLOCKED`.
- Return structured verdicts strictly matching [verifier.schema.json](../../config/verifier.schema.json).
