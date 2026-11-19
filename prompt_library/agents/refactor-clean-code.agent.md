---
name: refactor-clean-code
description: Evidence-based code refactoring and smell elimination agent through the local runner.
---
# Adapter Documentation: Refactor & Clean Code Agent

This agent definition describes the role of an autonomous code refactoring and clean code assurance specialist.

### Execution Path
Run `scripts/auto_review.py` configured with the refactor skill and clean code checklist:
```powershell
python scripts/auto_review.py "Refactor data access layer to eliminate duplication" --skill refactor-clean-code --checklist checklist-clean-code.json --send-to-openai
```

### Operational Boundaries
- The runner explicitly loads `AGENTS.md` and `skills/refactor-clean-code/SKILL.md`.
- Behavior invariance is verified against host-executed test profiles.
- Any change that alters public interfaces or causes test regressions is blocked.
- Final acceptance requires explicit human approval.
