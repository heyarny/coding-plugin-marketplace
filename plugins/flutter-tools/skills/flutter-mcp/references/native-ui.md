# Native selections, photo picker, and camera

## Capability boundary

Flutter MCP can tap the Flutter control that opens a picker and inspect the
Flutter widgets created when it returns. It cannot locate the system picker's
photo cells through Flutter widget finders. Native dialogs and platform-view
contents require a native automation surface; Flutter documents this distinction
for its [testing tools](https://docs.flutter.dev/testing/testing-plugins).

For an iOS simulator with CUA available, get the Simulator app and read its
accessibility tree and screenshot. Use only the currently documented CUA APIs.
If CUA is not available, report that limitation; another installed native test
tool may be appropriate, but do not silently install Patrol, Appium, or helpers.

## Photo-selection workflow

1. Establish the authorized fixture photos and destination. Returning a selected
   photo may immediately start an upload; do not assume there is a later Send
   button or select personal library images as an unrequested test fixture.
2. Use Flutter MCP to open the observed gallery/photo action.
3. Observe the native surface. If an unexpected permission prompt appears, apply
   the session's permission rules; do not pre-grant broad access to bypass it.
4. Use native accessibility identities to choose Photos/Albums and the intended
   fixture. For multi-selection, verify each selected mark and the count before
   the picker’s Add/Done action. Labels and button names vary by OS and locale.
5. Refresh the native state after actions. If grid cells have no useful labels,
   use a current screenshot and the native tool's documented coordinate system.
   Do not reuse Mac-window coordinates as Flutter logical coordinates, or repeat
   a gesture that produces no observed movement.
6. After Add/Done or Cancel dismisses the native UI, return to Flutter MCP. Verify
   preview count/order, correct owner, limit behavior, and any transfer/error
   state relevant to the requested test. Cancel should leave the selection as
   specified by the app; do not infer the outcome merely from picker dismissal.

If the picker is unavailable to native automation, separate the unverified
native path from any test that injects picker results. A fake selection can test
Flutter bookkeeping but cannot prove the actual OS picker works.

## Fixtures and simulator limitations

Prefer deterministic, non-personal PNG/JPEG fixtures already approved for the
test. When fixture seeding is authorized, an installed Simulator CLI may support:

```sh
xcrun simctl addmedia <observed-device-id> /absolute/path/to/fixture.png
```

This adds media to the simulator library; it does not perform the app's selection
flow. Check the installed command help and existing fixtures before adding copies.
Use CUA for native UI interaction when that is the provided control surface.

The current official `image_picker` documentation notes a PHPicker/HEIC limitation
on iOS simulators; use supported fixture formats or a physical device when testing
that path. Camera capture also depends on device/runtime availability, so do not
claim a simulator gallery test covers real camera capture. Check the installed
plugin version and [image_picker documentation](https://pub.dev/packages/image_picker)
when diagnosing those cases.

For a durable automated suite, Flutter `integration_test` covers Flutter state
and gestures. Native selections need an appropriate native test layer. Choose
that infrastructure separately from the live MCP session and within user scope.
