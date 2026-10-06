# Flutter MCP actions

These examples are arguments to `mcp__dart_flutter__flutter_driver_command`.
Replace placeholder URIs and example keys/labels with observed values. Recheck
the active tool schema: this server encodes many numeric and boolean fields as
strings, not JSON numbers or booleans.

## Finders and inspection

- `ByValueKey`: `keyValueString` plus `keyValueType: "String"` or `"int"`.
- `BySemanticsLabel`: `label` plus `isRegExp: "true"` or `"false"`.
- `ByText` / `ByTooltipMessage`: `text`; rich text may need a semantics finder.
- `ByType`: `type`, using the observed runtime type. Scope repeated types.
- `Ancestor` / `Descendant`: nested `of` and `matching` finder objects; inspect
  the current schema for `firstMatchOnly` and `matchRoot` rather than guessing.
- `PageBack`: use only when navigating back is intended.

Use `widget_inspector` with `command: "get_widget_tree"` and `summaryOnly: true`
for a compact initial view; the full tree can expose framework widgets omitted
from the summary. `get_diagnostics_tree` takes a finder, `diagnosticsType`
(`widget` or `renderObject`), `subtreeDepth`, and `includeProperties`.

`get_offset` supports `topLeft`, `topRight`, `bottomLeft`, `bottomRight`, and
`center`; it helps check geometry when the finder uniquely identifies a rendered
widget. `get_text` is for supported text widgets, not a universal value reader.

## Tap and select

```json
{
  "appUri":"<app URI>",
  "command":"tap",
  "finderType":"ByValueKey",
  "keyValueString":"<observed control key>",
  "keyValueType":"String",
  "timeout":"5000"
}
```

Use `waitForTappable` when readiness is uncertain. For a dropdown, tap its
control, inspect the opened menu, tap the intended option, and verify the chosen
value after the menu closes. For checkboxes, radios, switches, or multi-select
lists, inspect current state first so a repeated tap does not undo a selection.
Verify the checked/selected state through diagnostics or the visible UI.

## Scroll through a visible anchor

```json
{
  "appUri":"<app URI>",
  "command":"scroll",
  "finderType":"BySemanticsLabel",
  "label":"<unique visible label in the intended scrollable>",
  "isRegExp":"false",
  "dx":"0.0",
  "dy":"300.0",
  "duration":"500000",
  "frequency":"60",
  "timeout":"5000"
}
```

`duration` is in **microseconds**: `500000` means half a second. `timeout` is in
**milliseconds**. Offsets are Flutter logical coordinates; positive `dy` moves
the simulated finger down, negative moves it up. Judge the content direction
from the actual viewport, especially with reversed lists. The gesture starts
at the target's center, so a very large/off-screen widget is a poor anchor.
These semantics come from the
[Driver scroll API](https://api.flutter.dev/flutter/flutter_driver/FlutterDriver/scroll.html).

```json
{
  "appUri":"<app URI>",
  "command":"scrollIntoView",
  "finderType":"ByValueKey",
  "keyValueString":"<observed target key>",
  "keyValueType":"String",
  "alignment":"0.3",
  "timeout":"5000"
}
```

This command does not search unbuilt content. Semantics finders may also omit
off-screen nodes. Expose the target with bounded `scroll` gestures before retrying.
Flutter's Dart API has `scrollUntilVisible`, but the verified MCP command enum
does not expose that command; do not invent an MCP command. Use a bounded
scroll-observe-find loop. See
[scrollIntoView limitations](https://api.flutter.dev/flutter/flutter_driver/FlutterDriver/scrollIntoView.html).

## Text entry and selection

The test entrypoint starts with native keyboard input. For MCP text replacement:

1. Record any existing draft that the task requires preserving.
2. Set `command: "set_text_entry_emulation", enabled: "true"`.
3. Tap the intended editable Flutter widget and verify focus.
4. Use `command: "enter_text", text: "..."`.
5. Verify the field and restore the prior emulation mode afterward.

`enter_text` usually replaces the whole focused field; it is not an append or
text-range-selection API. See the
[enterText contract](https://api.flutter.dev/flutter/flutter_driver/FlutterDriver/enterText.html).
`send_text_input_action` supports actions such as `done`, `next`, `search`, and
`send`. Use only the action the flow calls for: `send` may submit content.

The exposed MCP commands do not provide a general cursor/range-selection command.
Use available native text interaction for selection handles/copy/paste or a
purpose-built integration test when precise editing is the behavior under test.
Native text entry and emulated text entry validate different paths.

## Timing and errors

`waitFor`, `waitForAbsent`, and `waitForTappable` support explicit readiness
checks. For demonstrated perpetual-animation waits, use
`set_frame_sync` with `enabled: "false"` temporarily and restore the prior state.
Do not use fixed sleeps or broad retries to conceal missing targets.

Check `get_runtime_errors` before and after a scenario. Preserve relevant error
evidence before clearing old errors. Distinguish a Driver timeout from a rendering
exception. Screenshots and actual widget state establish the UI outcome.
