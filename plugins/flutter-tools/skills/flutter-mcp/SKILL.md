---
name: flutter-mcp
description: Inspect and operate running Flutter apps through Dart/Flutter MCP for simulator testing, widget selection, scrolling, text entry, and runtime diagnosis. Set up a test-only Flutter Driver entrypoint when needed, and hand off native photo pickers or permission dialogs to native UI automation. Use for live Flutter UI checks and E2E testing, rather than ordinary Dart edits without runtime interaction.
---

# Flutter MCP

Use Flutter MCP for Flutter widgets and native UI automation for system surfaces.
Select controls through observed widget identities, then verify their visible
state. A command returning success does not prove the requested behavior occurred.

## Choose the control surface

| Task | Preferred approach |
| --- | --- |
| Flutter buttons, dropdowns, checkboxes, tabs, list selections | Driver `tap` with a unique widget finder; inspect the resulting state |
| Flutter scrolling and text entry | Driver `scroll`, `scrollIntoView`, and text commands |
| Widget inspection, runtime errors, reload/restart | Flutter inspector, runtime-error, and lifecycle MCP tools |
| Native photo picker, camera UI, permission dialog, OS keyboard selection | Available native UI automation, such as CUA on Simulator |
| Repeatable automated test suite | Flutter `integration_test`; native coverage requires a suitable native test layer |

Read [setup.md](references/setup.md) for Codex MCP configuration and launch/instrumentation problems,
[actions.md](references/actions.md) for command examples and finders, and
[native-ui.md](references/native-ui.md) before photo picking or other native UI work.

## Connect to the actual running app

1. Read the project's applicable instructions and existing test setup. Reuse its
   Driver entrypoint if present; do not replace normal startup for a UI check.
2. Discover available tool names and schemas. The validated server exposes
   `mcp__dart_flutter__dtd`, `flutter_driver_command`, `widget_inspector`,
   `get_runtime_errors`, `hot_reload`, and `hot_restart`. Names can vary by host.
3. Use DTD `listDtdUris`, select the instance for this workspace, then `connect`.
   Use `listConnectedApps` and the returned app URI for subsequent commands.
   A launch can also print a DTD URI. DTD and app/VM-service URIs are different.
   Never reuse a previous session's port, token, device ID, or app URI blindly.
4. Call Driver `get_health` before attempting Driver interactions. An ordinary
   debug app may support inspection and reload but lack `ext.flutter.driver`.
   Missing Driver requires an instrumented launch, not repeated reconnection.
5. For project-aware operations, register the workspace through `roots` if needed.
   This server's roots, analysis, package-reading, and pub tools use `file:` URIs.
   A separate `launch_app` tool may instead require a plain path; follow its schema.

Read package APIs with `read_package_uris` / `rip_grep_packages` when available.
Use `analyze_files`, LSP, and pub tools for their specific tasks rather than
trying to drive an editor UI. Adding dependencies still follows the user's scope
and the repository's installation rules.

## Operate and verify

- Start from a current widget tree or screenshot. Prefer existing value keys,
  then unique semantics labels, text, or a scoped type finder. Do not invent keys
  or assume a Mac accessibility label is identical to a Flutter text widget.
- Use Flutter MCP for Flutter scrollables. Desktop scroll-wheel events and
  screenshot-coordinate drags were unreliable in the observed Simulator session;
  this alone is not evidence that the app's touch scrolling is broken.
- When a visible `CustomScrollView` is the intended scrollable, target it
  directly with Driver `ByType` (`type: "CustomScrollView"`) rather than a
  descendant that may be a platform view or grid item. First confirm the finder
  with `waitFor`, then use a bounded gesture such as `dx: "0.0"`,
  `dy: "-420.0"`, `duration: "500000"`, and `frequency: "60"` to move toward
  later content; immediately take a screenshot to prove movement. This path was
  verified in the iPhone 17 Pro Playground on 2026-09-13.
- Keep gestures within visible content, away from composer bars and overlays.
  `scroll` injects touch movement. `scrollIntoView` requires a findable target;
  off-screen semantics and lazily built children may be unavailable.
- For an unavailable target, scroll a visible widget in the same scrollable in
  bounded steps and observe progress. If a gesture produces no movement, refresh
  the target and inspect the scrollable/overlay rather than repeating unchanged
  commands. Stop at an observed list end or report an unavailable target.
- Follow a tap or selection with a state check: selected label/value, checked
  appearance, visible route, preview count, or another task-specific assertion.
  Use diagnostics for values and render properties; use screenshots for visual
  layout. Read-only debug measurements supplement, rather than replace, gestures.
- Preserve existing drafts and user selections. Text entry usually replaces the
  focused field's contents. Submission, upload, or deletion must be within the
  user's actual task; selection itself may start an upload.
- A continuously animating UI can prevent frame synchronization from settling.
  If this is the demonstrated blocker, temporarily disable Driver frame sync,
  use explicit readiness checks, and restore the prior setting afterward.

## Diagnose without changing the wrong layer

Separate connection failure, missing Driver instrumentation, finder failure,
gesture failure, native UI, and application exceptions. A finder timeout can
appear in the runtime-error collector as a `FlutterDriverExtension` error; record
it as a harness failure and explain how it was resolved.

Hot reload preserves app state. Hot restart resets Dart state and applies startup
changes, but switching entrypoints requires a new launch. Reconnect when the app
URI changes. Prefer a focused retry after new evidence over repeated restarts.

When checking a suspected regression, keep the backend and fixtures fixed unless
the user explicitly authorizes changing them. Missing templates or wrong styles
in a live app establish symptoms, not which change caused them. Compare the
actual resolved template/data with the test fixture before assigning blame.

## Completion evidence

Report the entrypoint/device used, interactions actually exercised, visible
results, relevant runtime errors, and remaining gaps. Do not claim a photo-picker
test from injected image data, an upload test from a preview alone, or a visual
pass from `get_health`. Preserve staged changes when the user requests it.

The reference workflow was exercised on 2026-09-08: a debug Driver entrypoint,
DTD connection, `get_health`, semantics-based taps, scrolling both directions,
and `scrollIntoView` after exposing its target. Single-image and three-image chat
bubbles and activity rows were visually checked. Native photo selection and
precise text-range selection were not validated by that check.
