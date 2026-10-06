---
name: coordinate-codex-agents
description: Coordinate independent Codex app agents and tasks across any saved local or remote project. Use when the user asks to create a task in another project, find or inspect an existing task, send a message or question to another Codex agent, bring its response back, open its task, or coordinate a bounded exchange between agents working in different projects. When a project is delegated to an agent, treat that agent as the exclusive interface to its files and implementation work.
---

# Coordinate Codex Agents

Use Codex app task-management tools to coordinate independent tasks across saved projects. Treat “agent,” “chat,” “task,” and “thread” as equivalent when the user is referring to another Codex conversation.

## Exclusive project ownership

Once work in a saved project is assigned to an agent, use that agent as the exclusive interface to the project for the entire bounded exchange.

- Never search for, list, open, read, or inspect that project's files through filesystem or shell tools.
- Never create, edit, move, or delete that project's files directly, including for small fixes, cleanup, verification, or test preparation.
- Ask the selected agent to inspect the project, implement changes, run tests, and return the required evidence or summaries.
- If more detail is needed, message the selected task instead of falling back to direct filesystem access.
- If the selected agent cannot complete the work, report the blocker or ask the user how to proceed. Do not silently take over the project locally.

## Resolve the project

1. Call `codex_app__list_projects`.
2. Match the project name from the request. Prefer an exact label match; use a unique case-insensitive match when unambiguous.
3. Use the returned `projectId`, `hostId`, and path. Never hardcode project, host, or task identifiers.
4. Ask for the project only when it cannot be inferred safely. Report clearly when the requested saved project is unavailable.

## Confirm the communication target

Before the first outbound message in a new collaboration, always ask the user to choose between:

1. Creating a new task in the project.
2. Using a specific existing task.

Do not infer this choice from recency or silently select a task, even when one candidate appears obvious. If the user chooses an existing task, list the relevant candidates and ask which one to use. Do not call `codex_app__create_thread` or `codex_app__send_message_to_thread` until the user confirms the choice. Once the user selects a target, keep using it for the same bounded exchange without asking again.

## Create a new task

Use this workflow after the user selects a new chat, task, or independent agent:

1. Use the requested first message as the `prompt`. Ask for it only when missing.
2. Call `codex_app__create_thread` with a project target, the resolved `projectId`, and `environment: { type: "local" }` unless the user explicitly requests a worktree.
3. Omit `model` and `thinking` unless explicitly requested.
4. Preserve short prompts exactly.
5. After successful creation, report the result and emit `::created-thread{threadId="..."}` on its own line.

## Find an existing task

1. Call `codex_app__list_threads` and identify tasks using the resolved project’s `hostId` and path plus any title, preview, status, or recency clues from the request.
2. Prefer a sufficiently broad recent list and filter it. A query containing only the project label can miss tasks whose titles do not mention the project.
3. Honor an explicit task ID or title. If several candidates remain materially ambiguous, show a short candidate list and ask which one to use.

## Message an existing task

1. Use the existing task selected through the confirmation and discovery workflows above.
2. Call `codex_app__send_message_to_thread` with its `threadId`, `hostId`, and the user’s message as `prompt`.
3. Omit `model` and `thinking` unless explicitly requested.
4. If the user wants the reply, inspect the task with `codex_app__read_thread`. Do not claim a response arrived until it is visible.

## Coordinate agents

For a requested cross-project collaboration:

1. Read only the task context needed for the exchange with `codex_app__read_thread`.
2. Send the relevant question, findings, or constraints to the selected task.
3. Read its response when requested and relay it accurately to the user or another explicitly selected task.
4. Keep the exchange bounded to the requested outcome. Do not start an indefinite agent-to-agent loop or forward messages to additional tasks without authorization.

## Inspect or open a task

- Use `codex_app__read_thread` to inspect status and recent turns without opening it.
- Use `codex_app__navigate_to_codex_page` only when the user asks to open or show the task.

## Boundaries

- Use Codex app task tools for existing independent tasks; do not substitute collaboration subagents.
- Delegated project ownership is exclusive: do not inspect or modify the project through local filesystem or shell tools while coordinating its agent.
- Do not fork or hand off a task unless explicitly requested.
- Creating a task or sending a message changes app state. Always perform the communication-target confirmation before starting a new exchange.
