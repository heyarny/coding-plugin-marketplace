---
name: git-commit
description: Draft concise Conventional Commit messages from the current git index. Use when Codex needs to inspect staged changes only, classify them with the Conventional Commits 1.0.0 format, suggest a brief commit title with optional bullet details for larger changes, or commit the staged change set on the current branch. If the user explicitly includes `draft`, return the proposed message only and do not commit.
---

# Git Commit

## Overview

Inspect only the staged diff and produce a Conventional Commit message for that staged change set. Keep the result specific, concise, and directly grounded in what is actually staged.

Use the Conventional Commits 1.0.0 structure: `<type>[optional scope]: <description>`. Treat `feat` as a new feature, `fix` as a bug fix, and use other standard types when they fit better.

Default behavior is to commit the staged changes on the current branch. If the user explicitly includes `draft`, return the proposed commit message only and do not perform the commit.

## Workflow

1. Check whether anything is staged.
   - Run `git diff --cached --name-only`.
   - If nothing is staged, say so plainly and stop.

2. Inspect staged changes only.
   - Run `git diff --cached --stat` for a high-level summary.
   - Run `git diff --cached --unified=0` when the summary is not enough.
   - Do not inspect unstaged or untracked work to shape the message.

3. Choose the narrowest commit type that matches the staged intent.
   - `feat`: add user-visible behavior or a new capability.
   - `fix`: correct a defect or regression.
   - `refactor`: change internal structure without intended behavior change.
   - `docs`: change documentation only.
   - `test`: add or update tests only.
   - `perf`: improve performance.
   - `build`: change build, packaging, or dependencies.
   - `ci`: change CI or automation workflow.
   - `style`: apply formatting-only changes.
   - `chore`: apply maintenance work that does not fit a stronger type.
   - `revert`: revert an earlier change.

4. Add a scope only when it is obvious from the staged files or subsystem.
   - Prefer no scope over a vague one.
   - Example: `fix(api): handle empty command batches`

5. Write a brief subject.
   - Use imperative mood.
   - Keep it specific to the outcome of the staged change.
   - Keep it short; prefer a single line that stays comfortably under 72 characters.
   - Do not end the description with a period.
   - Avoid filler like "update stuff" or implementation detail dumps.

6. Add an optional body only when it helps.
   - Use a body when the staged change is large, spans multiple concerns inside one coherent feature/fix, or the user asks for detailed commit details.
   - Put exactly one blank line between the subject and the bullet body.
   - Keep the body to at most 5 brief bullet points.
   - Each bullet should describe one concrete changed outcome, not every edited file.
   - Prefer bullets like `- Add credit balance persistence` over vague or process-heavy bullets.
   - Do not include a body for simple changes where the subject is enough.

7. Flag breaking changes when the staged diff clearly changes a public contract.
   - Use `!` after the type or scope when the title itself should carry that signal.
   - Use a `BREAKING CHANGE:` footer when the staged diff clearly requires it, after any bullet body.

8. Handle mixed staged work deliberately.
   - If the staged set contains multiple unrelated concerns, say a split is advisable and briefly group the changes by concern.
   - Provide suggested Conventional Commit messages for each split group.
   - Ask the user to approve either splitting the staged work or making one mixed commit.
   - Do not change the index to split commits until the user approves the split.
   - If the user approves splitting, unstage/restage only the relevant files or hunks for each group and commit each group separately.
   - If the user asks for one mixed commit, use the highest-impact type represented by the staged changes and add a concise body summarizing each concern.
   - Highest-impact type order: `feat`, `fix`, `perf`, `refactor`, `build`, `ci`, `docs`, `test`, `style`, `chore`.

9. Respect `draft` mode when the user explicitly asks for it.
   - Treat `draft` as message-preview mode.
   - In `draft` mode, inspect only staged changes, choose the full message, and return it without committing.
   - Without `draft`, commit the staged changes on the current branch using the proposed message.
   - When committing a message with a body, pass the subject and body separately, for example with repeated `git commit -m` arguments, so the subject remains the first line.
   - Preserve the blank line between the subject and the first body bullet in both draft output and actual commits.
   - Do not push as part of this skill. Pushing is outside this skill unless the user asks separately outside the skill flow.

## Output

- Default output: commit the staged changes using the generated message.
- If the user asks for explanation, include the proposed message first and then a one-sentence rationale.
- If the user explicitly includes `draft`, output only the proposed commit message.
- If mixed staged work should be split, output the split recommendation and ask for approval before committing.
- If the user asks to perform the commit, use only the staged content and the approved message.

## Examples

- `feat(auth): add refresh token rotation`
- `fix(stream): stop duplicate heartbeat events`
- `docs: clarify local development setup`
- `refactor(chat): extract response cost calculation`
- `test(config): cover MCP CORS defaults`

Larger-change example:

```text
feat(credits): add agent run credit accounting

- Add persistent user credit balances and ledgers
- Charge completed model calls from monthly credits before purchases
- Block new agent runs when available credits are below the minimum
- Expose dev endpoints for plan selection and demo purchases
- Document credit reset and out-of-credits behavior
```

Draft-aware examples:

- User asks for `$git-commit draft` after staging docs changes:
  - output only: `docs: reorganize VAC documentation`

- User asks for `$git-commit draft` after staging a larger feature:
  - output only the full proposed commit message, including the subject and up to 5 bullets.

- User asks for `$git-commit` after staging docs changes:
  - execute: commit staged changes on the current branch with `docs: reorganize VAC documentation`

## Notes

- The canonical spec describes Conventional Commits as a lightweight convention on top of commit messages and defines the core format as `<type>[optional scope]: <description>`.
- Common extra types such as `build`, `chore`, `ci`, `docs`, `perf`, `refactor`, `style`, and `test` are widely used alongside the spec.
