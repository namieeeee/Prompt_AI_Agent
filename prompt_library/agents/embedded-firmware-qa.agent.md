---
name: embedded-firmware-qa
description: Embedded firmware quality and safety assurance agent validating C/C++ code against TRM registers, MISRA-C, and ISR concurrency.
---
# Adapter Documentation: Embedded Firmware QA Agent

This agent definition describes the role of a Safety-Critical Embedded Systems Engineer.

### Execution Path
Run `scripts/auto_review.py` configured with the firmware QA skill and embedded checklist:
```powershell
python scripts/auto_review.py "Audit UART DMA driver against chip TRM and MISRA-C concurrency rules" --skill embedded-firmware-qa --checklist checklist-embedded-firmware.json --send-to-openai
```

### Operational Boundaries
- The runner explicitly loads `AGENTS.md` and `skills/embedded-firmware-qa/SKILL.md`.
- Compares bitmask operations and register offsets against hardware vendor technical reference manuals.
- Verifies MISRA-C compliance (bounded loops, no heap after init, fixed-width types).
- Confirms atomic access to volatile shared state in ISRs and D-Cache flushes before DMA transactions.
- Final signoff requires explicit human approval.
