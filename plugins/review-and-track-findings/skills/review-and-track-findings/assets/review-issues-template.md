# Code Review Issues

This living document tracks actionable findings from the current code review through resolution and
verification.

## Review scope

- Reviewed changes: [staged, unstaged, untracked, commit range, or user-specified scope]
- Applicable repository guidance: [paths and relevant scopes]
- Review date: [YYYY-MM-DD]

## Summary

| ID | Priority | Status | Area | Summary |
| --- | --- | --- | --- | --- |
| CR-001 | P1/P2/P3 | Open | [area] | [concise defect] |

## CR-001: [Concise defect title]

- Priority: P1/P2/P3
- Status: Open
- Owner: Unassigned
- Primary location: `[path]`, `[line or symbol]`
- Rule support: [smallest applicable instruction-file citation, or omit when not rule-supported]

### Problem

[Explain the defective behavior and the conditions that trigger it.]

### Impact

[Explain the concrete correctness, security, performance, or maintainability consequence.]

### Evidence and reproduction

1. [Relevant setup or input.]
2. [Execution path.]
3. [Observed incorrect result.]

### Recommended resolution

[Describe the smallest complete repair without over-prescribing incidental implementation details.]

### Value versus complexity

- Value of fixing: [Likely impact, realistic trigger frequency, and uncertainty.]
- Cost of complete fix: [Scope, new contracts or state, regression risk, and testing; note why a
  simpler partial fix falls short when relevant.]
- Recommendation: [Fix now / Accept risk / Defer, with a short reason; this is not a status decision.]

### Acceptance criteria

- [Observable behavior that must hold.]
- [Regression coverage or validation required.]

### Resolution record

- Fix or decision: Pending
- Verification: Pending

<!-- Duplicate the issue section for each finding and keep IDs stable. -->

## Review validation baseline

- Commands run: [commands, or "None"]
- Result: [exact counts/results, or why validation was not run]
