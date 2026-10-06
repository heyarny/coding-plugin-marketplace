---
name: review-and-track-findings
description: Review staged, unstaged, and untracked code changes and maintain a living issue document in the repository root with stable finding IDs, evidence, priorities, status, acceptance criteria, decisions, fixes, and verification. Use when the user asks for a code review that should be captured in a living document, asks to write review findings into an issue document, refers to a review issue by number such as "nr. 3", wants to explain or fix findings one at a time, or wants to close or remove the document after the findings are resolved.
---

# Review and Track Findings

Maintain one repository-local source of truth from the initial review through discussion, repair,
verification, and closure. Keep the chat response concise; keep durable detail in the document.

## Select the workflow

1. Locate the repository root and applicable project instruction files.
2. Use the user-specified document path. Otherwise use `<repository-root>/code_review_issues.md`.
3. If the document does not exist, perform the review and create it only when actionable findings
   exist.
4. If the document exists, resume it. Never overwrite or recreate stable finding IDs.
5. Treat requests such as "nr. 2" as requests about the corresponding stable ID, such as `CR-002`.
6. Explain or diagnose without editing code unless the user asks to fix or implement.

## Review and create the document

1. Inspect staged, unstaged, and untracked changes unless the user gives a narrower scope. Read
   enough unchanged context and tests to establish actual behavior.
2. When the diff has at least two independent review questions, spawn two or three subagents in
   parallel with `xhigh` reasoning effort. Choose concrete, non-overlapping questions from the
   changed behavior; do not require the user to define their tasks. Set `xhigh` reasoning effort on
   each spawn request and omit the model override so subagents inherit the parent model. Use a
   bounded context fork if the tool requires one for an explicit effort override. Give each
   subagent the review scope and relevant repository rules, and ask for introduced, actionable
   defects with file and line evidence, trigger, and impact. Subagents inspect only: they must not
   edit code or the issue document. Wait for their results, then verify and deduplicate every
   candidate before assigning IDs or writing the document. Review directly when the diff has no
   useful independent tracks. If `xhigh` is unavailable, state the effort actually used.
3. Apply repository rules according to their normal precedence and retain any required rule
   attribution. Follow user-supplied review format and severity guidance.
4. Report only discrete, actionable issues introduced by the reviewed change. Do not manufacture a
   target count, record speculative concerns, or turn general cleanup into findings.
5. Deduplicate findings by defect and remedy. Order them by severity, then by the order in which a
   maintainer should address them.
6. Assign stable sequential IDs (`CR-001`, `CR-002`, ...). Never reuse or renumber an ID later.
7. Use `assets/review-issues-template.md` as the document structure. Make every issue independently
   understandable without relying on the chat transcript.
8. Include exact files, symbols, and smallest useful line locations. Explain the triggering scenario,
   concrete impact, evidence, recommended repair, and verifiable acceptance criteria.
9. For each finding, assess the value of fixing it against the complexity of the smallest complete
   repair using the triage guidance below. Give a recommendation without deciding for the user.
10. Record the commands and results that establish the review baseline. Never claim a check ran when
   it did not.
11. Return the normal review response with a concise value-versus-complexity recommendation for
    open findings. The living document complements any required inline review comments; it does
    not replace them.

If no actionable findings exist, say so and do not create an empty issue document.

## Maintain issue state

Use these states consistently:

- `Open`: actionable and not yet being implemented.
- `In Progress`: implementation or verification is underway.
- `Blocked`: resolution needs missing authority, information, or external state.
- `Deferred`: acknowledged but deliberately postponed; still unresolved.
- `Verified`: the fix or decision is implemented and appropriate verification passed.
- `Accepted`: the user explicitly accepts the behavior or risk without a code change.
- `Not Applicable`: later evidence disproves the finding or removes it from scope.

Update both the summary row and issue section whenever status changes. Preserve the original problem
and evidence as historical context; put later decisions and results in the resolution record. Treat
`Open`, `In Progress`, `Blocked`, and `Deferred` as unresolved.

Append newly discovered actionable findings with the next unused ID. Do not silently expand an
existing issue to cover a different defect.

## Weigh value against complexity

Keep the assessment proportional to the finding; do not invent precise estimates. Compare the
likely impact and realistic trigger frequency with the scope, new contracts or state, regression
risk, and testing needed for the smallest complete fix. Call out uncertainty and any tempting
partial fix that merely moves the problem. Recommend **fix now**, **accept the risk**, or **defer**
with a short reason. Priority describes impact, not implementation cost. A recommendation to accept
does not change the issue to `Accepted`; only the user's explicit decision does.

## Work one issue at a time

For an explanation request:

1. Re-read the issue, current diff, surrounding implementation, and relevant tests.
2. Keep the visible explanation brief and use simple words. Lead with a one-sentence summary of what
   goes wrong and avoid jargon unless a term is necessary and immediately explained.
3. Give one small, concrete example that shows the trigger and observable consequence.
4. Add the smallest useful graph when it materially clarifies a request flow, state change,
   dependency, or cause-and-effect chain. Prefer a compact Mermaid diagram with plain labels; skip
   the graph when prose and the example are clearer on their own.
5. Explain why current safeguards do or do not prevent the issue, what the smallest complete fix
   would change, and whether its value justifies its complexity.
6. Correct the document if current evidence invalidates or narrows the finding.

For a fix request:

1. Confirm the issue still reproduces against the current worktree.
2. Set it to `In Progress` when useful for a long-running change.
3. Implement the smallest complete fix while preserving unrelated user changes.
4. Add focused regression coverage for the failing path and run broader validation proportional to
   risk. Preserve asynchronous or reactive semantics where applicable.
5. Mark it `Verified` only after the implementation and relevant checks succeed. Otherwise leave the
   accurate unresolved state.
6. Fill in `Fix or decision` and `Verification` with concrete behavior, tests, command results, and
   date. Avoid vague entries such as "fixed" or "tests pass".
7. Summarize the outcome in chat with links to the implementation, tests, and living document.

Do not combine fixes for other findings unless the user expands the scope or the same minimal change
necessarily resolves them. If it does, update every affected issue explicitly.

## Close the document

Keep the document until the user explicitly requests deletion. Before deleting it:

1. Search the summary, issue states, and resolution records for unresolved or pending entries.
2. Refuse deletion and list the remaining IDs when any issue is unresolved.
3. Delete it only when every issue is `Verified`, `Accepted`, or `Not Applicable` and no resolution
   field remains pending.
4. State whether version control can recover the file, especially when it was untracked.
