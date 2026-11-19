---
name: refactor-clean-code
description: Evidence-based code refactoring and smell elimination. Verifies behavior invariance against regression tests, SOLID conformance, cyclomatic complexity reduction, and interface stability.
---
# Refactoring & Clean Code Verification Workflow

Review source changes proposed for refactoring or clean code improvements against the structured checklist IDs, source code with line numbers, Git baseline diff, and actual test suite execution.

### Verification Principles
1. **Behavior Invariance First**: A refactoring must never alter external functional contracts. Existing unit and integration tests must execute with 100% PASS (`returncode == 0`).
2. **SOLID & Single Responsibility**: Ensure monolithic routines are partitioned into cohesive, single-responsibility units without introducing over-engineering or premature abstraction.
3. **Complexity & Redundancy (DRY)**: Check that duplicated logic is extracted into reusable components and nested conditional branching is flattened using early returns or guard clauses.
4. **Interface Preservation**: Public APIs, signatures, and exported contracts must remain backward-compatible unless explicit deprecation migrations are provided and proven by tests.

### Evidence Mapping
- Map each checklist criterion ID (`BEHAVIOR_INVARIANCE`, `SOLID_COUPLING`, `COMPLEXITY`, `READABILITY`) to exact source citations (`path` and `line`).
- Validate that the test execution evidence proves no behavioral regression.
- Output JSON strictly adhering to [verifier.schema.json](../../config/verifier.schema.json).
- Never grant a PASS based on subjective claims. Missing test results or unmapped refactor lines block acceptance (`BLOCKED`).
