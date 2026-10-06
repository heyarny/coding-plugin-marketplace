# Coordinate Codex Agents

Coordinate independent Codex app chats across saved local and remote projects.
The skill can find and inspect tasks, create or message a selected task, relay
responses, and open a task when requested.

## Runtime support

This workflow requires host-provided **Codex app task-management tools** for
listing projects and tasks, creating tasks, messaging, reading responses, and
navigation. Tool names can vary by host; match the supplied `codex_app__*`
operations to the corresponding available tool schemas.

The package includes both marketplace manifest formats. Installing it in Claude
Code supplies the instructions; executing the workflow there requires a bridge
that exposes the same Codex app APIs. This package does not supply that bridge.

## Install and use in Codex

From the marketplace repository root:

```sh
codex plugin marketplace add .
codex plugin add coordinate-codex-agents@coding-plugins-marketplace
```

Start a new session, then ask:

- “Use Coordinate Codex Agents to find the chats for my backend project.”
- “Ask an agent in the backend project how the upload endpoint handles retries.”
- “Bring back the response from the chat I selected.”

For a new outbound exchange, choose whether to create a task or use a specific
existing task before communication starts. Once selected, the same target is
used for that bounded exchange. Task creation and messaging change app state
and require the corresponding request and target selection.

## Project ownership and resources

The workflow treats an agent assigned to a project as the exclusive interface
to that project's implementation. It asks that agent to inspect files, make
changes, and run checks instead of accessing the delegated project's files
directly. It coordinates independent Codex app tasks using the app's APIs.

The supplied skill and Codex display metadata are preserved unchanged under
`skills/coordinate-codex-agents/`. No external files, MCP server configuration,
executable hooks, or credentials are bundled.

Author: Arnold Stark. Licensed under [MIT](LICENSE).
