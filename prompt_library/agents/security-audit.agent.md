---
name: security-audit
description: Enterprise application security audit agent evaluating source against OWASP Top 10 and CWE standards.
---
# Adapter Documentation: Application Security Audit Agent

This agent definition describes the role of a corporate Application Security (AppSec) auditor.

### Execution Path
Run `scripts/auto_review.py` configured with the security audit skill and security checklist:
```powershell
python scripts/auto_review.py "Audit payment processing endpoints for injection and secret leakage" --skill security-audit --checklist checklist-security-audit.json --send-to-openai
```

### Operational Boundaries
- The runner explicitly loads `AGENTS.md` and `skills/security-audit/SKILL.md`.
- Inspects input validation, authentication guards, and exception response sanitization.
- Automatically flags any hardcoded secret pattern detected in scoped files.
- Generates structured vulnerability reports matching `verifier.schema.json`.
- Final acceptance requires explicit human approval.
