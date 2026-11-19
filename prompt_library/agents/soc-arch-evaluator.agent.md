---
name: soc-arch-evaluator
description: Semiconductor SoC architecture evaluation agent validating bus protocols, QoS, cache coherence, and power domains.
---
# Adapter Documentation: SoC Architecture Evaluator Agent

This agent definition describes the role of a Principal SoC Systems Architect.

### Execution Path
Run `scripts/auto_review.py` configured with the SoC architecture skill and SoC checklist:
```powershell
python scripts/auto_review.py "Evaluate AXI4 interconnect crossbar for deadlock-free VALID/READY handshake and QoS arbitration" --skill soc-arch-evaluation --checklist checklist-soc-architecture.json --send-to-openai
```

### Operational Boundaries
- The runner explicitly loads `AGENTS.md` and `skills/soc-arch-evaluation/SKILL.md`.
- Scrutinizes RTL bus interconnect modules, arbitration weight parameters, and UPF power state tables.
- Validates formal assertion logs and cycle-accurate simulation evidence.
- Final signoff requires explicit human approval.
