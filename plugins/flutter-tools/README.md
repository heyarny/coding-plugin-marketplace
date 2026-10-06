# Flutter Tools

Two complementary skills for live Flutter testing and diagnosis:

| Skill | Workflow |
| --- | --- |
| `flutter-mcp` | Connect to a running app, inspect widgets, exercise interactions, and verify visible results |
| `flutter-motion-debugging` | Record a simulator interaction, inspect adjacent frames, and correlate motion with Flutter layout data |

Motion Debugging uses the Flutter MCP workflow. Both are bundled so the companion
skill is available in the same installation, with Codex display metadata and
Flutter MCP reference files. The setup guide includes a project-local Codex
configuration example using FVM.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add flutter-tools@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install flutter-tools@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, ask:

- “Use Flutter MCP from Flutter Tools to inspect and test my running app.”
- “Use Flutter Motion Debugging from Flutter Tools to diagnose this scroll jump.”

In Claude Code:

```text
/flutter-tools:flutter-mcp Inspect and test my running Flutter app.
/flutter-tools:flutter-motion-debugging Diagnose a scroll jump in my iOS Simulator app.
```

Describe the app, route, device, and interaction you want exercised. The workflow
discovers current app and device identities rather than relying on saved ports.

## Dependencies and effects

Flutter MCP needs a Flutter project, a running debug app, and a compatible
host-configured Dart/Flutter MCP server providing connection, inspector,
runtime-error, and Driver tools. Driver interaction requires a test-only Driver
entrypoint when the app has no existing instrumentation. Bundled
[`setup.md`](skills/flutter-mcp/references/setup.md) describes project-local
`.codex/config.toml` configuration with FVM and Driver setup;
[`actions.md`](skills/flutter-mcp/references/actions.md) covers interactions.

Native pickers and permission dialogs require native UI automation, such as CUA.
See [`native-ui.md`](skills/flutter-mcp/references/native-ui.md) for that boundary.
Simulator video capture uses macOS, Xcode Simulator, `xcrun simctl`, `ffmpeg`, and
`ffprobe`. Recordings, contact sheets, and extracted frames use temporary paths.
Use the target project's tools for analysis and regression tests.

Live gestures can change app state. Photo selection or submission can initiate
uploads and must stay within the requested test. Authorized setup and fixes may
change project dependencies, a test entrypoint, application code, or tests.
Temporary frame-sync changes and diagnostics should be restored after the check.

This is a skills-only package. It provides no MCP server configuration,
executable hooks, or credentials; configure the required tools in the host.
`plugin.json` supplies the portable Codex identity, and
`.claude-plugin/plugin.json` supplies the matching Claude Code identity.

Author: Arnold Stark. Licensed under [MIT](LICENSE).
