---
name: flutter-motion-debugging
description: Diagnose Flutter scroll jumps, first-frame offsets, and animation glitches when screenshots hide when content moves. Record an iOS Simulator interaction, inspect timed frames with ffmpeg, and correlate motion with Flutter layout data.
---

# Flutter motion debugging

Use this workflow when the timing or direction of a UI movement matters. Use the existing Flutter MCP skill for app connection, gestures, widget inspection, and runtime errors; this skill adds frame-by-frame visual evidence.

## Capture the exact interaction

1. Reproduce the user's route, viewport state, and gesture. Pick a visible landmark that should stay fixed, such as the top of a card or the first retained row. Capture a still frame before the action.
2. Get the booted simulator ID with `xcrun simctl list devices booted`; match it to the running app. Use a fresh Flutter app URI and check Driver `get_health`. If ongoing animations block Driver commands, disable frame sync for the replay and restore it afterward.
3. Start recording **before** the tap or scroll. Run the command in a shell session that can be stopped with Ctrl-C; keep the video under a temporary path.

```sh
xcrun simctl io "$sim_id" recordVideo --codec=h264 "$video"
```

4. Perform one interaction, wait until its animation settles, then stop the recording. Keep the baseline, recording, and final screenshot tied to the same run. Avoid recording screens with sensitive user data.

## Inspect motion with ffmpeg

Check duration and frame rate, then sample a contact sheet around the action:

```sh
ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate:format=duration -of default=noprint_wrappers=1 "$video"
ffmpeg -v error -i "$video" -ss 0.8 -vf "fps=8,scale=240:-1,tile=5x4" -frames:v 1 "$sheet"
```

Adjust the seek time and sampling rate to include frames before, during, and after the movement. Simulator recordings can have variable frame rate; the `fps` filter resamples and may duplicate frames. A contact sheet can miss a one-frame flash. For a suspected jump, extract a short contiguous interval at source resolution and inspect the same crop in adjacent frames:

```sh
ffmpeg -v error -i "$video" -ss 1.0 -t 0.5 "$frames/frame-%03d.png"
```

Create `$frames` first. Crop or zoom copies for presentation, but compare source-resolution frames for pixel positions. Note the frame where the landmark first moves, whether it returns, and which other edges move with it.

## Correlate and verify

- Read Flutter Driver widget offsets and, when needed, temporary scroll/layout logs: current offset, min/max scroll extent, viewport size, and the relevant item geometry. Video coordinates are physical pixels; Driver offsets are logical pixels, so account for device pixel ratio before comparing numbers.
- Decide whether the viewport moved, an item's measured height changed, a sliver corrected scroll position, or an overlay stayed fixed while content passed beneath it. A finder timeout is a harness result; check runtime errors separately.
- Fix the demonstrated cause. Add a focused widget test that checks the landmark during intermediate animation frames as well as after settling. Replay the original simulator action and inspect the new recording. Remove temporary logging and preserve unrelated workspace changes.

Use installed tools already available in the environment. Follow the project's approval rules before installing a missing recorder or ffmpeg.
