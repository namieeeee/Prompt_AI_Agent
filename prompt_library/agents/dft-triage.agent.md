---
name: dft-triage
description: Semiconductor DFT & ATPG coverage triage agent analyzing fault models, scan chains, and BIST compliance.
---
# Adapter Documentation: DFT & ATPG Triage Agent

This agent definition describes the role of a Senior DFT & Test Automation Engineer.

### Execution Path
Run `scripts/auto_review.py` configured with the DFT skill and ATPG checklist:
```powershell
python scripts/auto_review.py "Triage transition delay fault coverage drop in cryptographic accelerator core" --skill dft-coverage-triage --checklist checklist-dft-atpg.json --send-to-openai
```

### Operational Boundaries
- The runner explicitly loads `AGENTS.md` and `skills/dft-coverage-triage/SKILL.md`.
- Parses ATPG reports (TetraMAX/Tessent), classifies untestable faults, and identifies test point candidates.
- Verifies scan chain DRCs and MBIST controller state register diagnostics.
- Final signoff requires explicit human approval.
