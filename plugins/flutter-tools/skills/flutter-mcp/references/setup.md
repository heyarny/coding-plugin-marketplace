# Codex MCP configuration, Driver setup, and connection

## Configure the MCP server in Codex

Add the Dart/Flutter MCP server to the Flutter project's local
`.codex/config.toml`. Codex loads project-local configuration for trusted projects.
Merge the server entry into any existing config. Example using FVM:

```toml
[mcp_servers.dart-flutter]
command = "fvm"
args = ["dart", "mcp-server"]

[mcp_servers.dart-flutter.env]
PATH = "/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
```

FVM must be installed and available on the configured PATH. This macOS example
includes the Apple Silicon Homebrew directory; adjust it for the machine's FVM
installation. The `env.PATH` value sets the server process's PATH.

Use the Flutter project configured for FVM, restart the Codex session after
editing the configuration, and use `/mcp` to inspect the server connection and
available tools. Discover the live tool names and schemas before following the
DTD examples below.

See [Codex MCP configuration](https://learn.chatgpt.com/docs/extend/mcp) for
project-local configuration and STDIO server options.

## Reuse before adding

Inspect `pubspec.yaml`, the app entrypoint, test directories, and project launch
instructions. An existing `test_driver/app.dart` may already supply everything.
Adding `flutter_driver` is useful for the exposed live MCP Driver commands; it
does not require replacing a project's `integration_test` suite.

When Driver setup is authorized, add to the existing development dependencies:

```yaml
dev_dependencies:
  flutter_driver:
    sdk: flutter
```

Create a separate entrypoint, adapting `your_app` to the package name:

```dart
import 'package:flutter/foundation.dart';
import 'package:flutter_driver/driver_extension.dart';
import 'package:your_app/main.dart' as app;

Future<void> main() async {
  if (!kDebugMode) {
    throw StateError('The Flutter Driver entrypoint requires debug mode.');
  }
  enableFlutterDriverExtension(enableTextEntryEmulation: false);
  await app.main();
}
```

Adapt the final call if the real app has synchronous startup or a different
bootstrap signature. Initialize Driver before the app creates its Flutter
binding. Keep this entrypoint out of release launches. Native text entry remains
available because emulation starts disabled. These requirements follow the
[Driver extension API](https://api.flutter.dev/flutter/flutter_driver_extension/enableFlutterDriverExtension.html).

```sh
flutter pub get
flutter devices
flutter --print-dtd run --debug -d <observed-device-id> -t test_driver/app.dart
```

Check the installed Flutter help if `--print-dtd` is unavailable. Reuse a running
simulator or the user's selected device. Stop the previous client debug session
when needed to replace its launch. Do not restart a backend as part of Driver
setup. Keep the run process alive for the MCP session.

After adding the entrypoint, analyze it, inspect the dependency diff for unrelated
upgrades, and check the working-tree diff. A live health/tap/scroll check is more
meaningful here than a unit test that merely checks the bootstrap's source text.

## DTD commands

Current `mcp__dart_flutter__dtd` arguments:

```json
{"command":"listDtdUris"}
```

```json
{"command":"connect","uri":"<DTD URI returned by discovery or launch>"}
```

```json
{"command":"listConnectedApps"}
```

Then call `mcp__dart_flutter__flutter_driver_command`:

```json
{"command":"get_health","appUri":"<returned app URI>","timeout":"5000"}
```

Expected successful Driver response: `isError: false` and `status: ok`. Inspect
the nested response as well as the MCP transport result. A successful DTD
connection alone does not establish Driver availability.

If package/analysis tools report no registered project roots, use the current
`mcp__dart_flutter__roots` schema, for example:

```json
{"command":"add","uris":["file:///absolute/workspace/path"]}
```

If Simulator disappears from sandboxed device discovery but is visibly running,
report the environment access failure accurately and use the tool's normal
permission mechanism for simulator access. Do not install another simulator or
alter app behavior to compensate.

## Common failure distinctions

| Symptom | Next step |
| --- | --- |
| DTD disconnected / app URI no longer live | Rediscover DTD and the current app URI |
| `ext.flutter.driver` is missing | Launch the test entrypoint; hot reload cannot switch targets |
| Driver finder times out | Check current route, uniqueness, off-screen/lazy content, and native UI |
| Driver waits indefinitely around animations | Check readiness/frame sync; disable temporarily only if relevant |
| Build is slow with no app URI yet | Wait for build/launch evidence; do not claim MCP is connected |
| Native picker visible but Flutter tree unchanged | Hand off to native UI automation |

For repeatable Flutter test suites, use the SDK's
[integration testing guidance](https://docs.flutter.dev/testing/integration-tests).
