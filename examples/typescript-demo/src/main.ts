/**
 * typed-ffmpeg TypeScript Demo
 *
 * This demo shows how to use @typed-ffmpeg/v8 to build FFmpeg
 * filter graphs with full type safety and IDE autocomplete.
 *
 * Prerequisites:
 *   npm install
 *   FFmpeg installed on your system (only needed for .run())
 */

import {
  input,
  output,
  compileAsList,
  mergeOutputs,
  InputNode,
  OutputNode,
  FilterNode,
  StreamType,
} from "@typed-ffmpeg/v8";

// ---------------------------------------------------------------------------
// Example 1: Simple transcode (no filters)
// ---------------------------------------------------------------------------
console.log("=== Example 1: Simple transcode ===");

const simpleCmd = output(
  [input("input.mp4")],
  "output.mp4",
  { vcodec: "libx264" },
).overwriteOutput();

console.log("Command:", simpleCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 2: Scale video
// ---------------------------------------------------------------------------
console.log("=== Example 2: Scale video ===");

const inp2 = new InputNode("input.mp4");
const scale = new FilterNode(
  "scale",
  [inp2.video],
  { w: 1280, h: 720 },
  [StreamType.Video],
  [StreamType.Video],
);
const scaleCmd = new OutputNode([scale.video(0)], "scaled.mp4")
  .stream()
  .overwriteOutput();

console.log("Command:", scaleCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 3: Chain multiple filters
// ---------------------------------------------------------------------------
console.log("=== Example 3: Chained video filters ===");

const inp3 = new InputNode("input.mp4");

const hflip = new FilterNode(
  "hflip",
  [inp3.video],
  {},
  [StreamType.Video],
  [StreamType.Video],
);

const scale3 = new FilterNode(
  "scale",
  [hflip.video(0)],
  { w: 640, h: 480 },
  [StreamType.Video],
  [StreamType.Video],
);

const drawbox = new FilterNode(
  "drawbox",
  [scale3.video(0)],
  { x: 10, y: 10, w: 100, h: 100, color: "red", thickness: 3 },
  [StreamType.Video],
  [StreamType.Video],
);

const chainCmd = new OutputNode([drawbox.video(0)], "chained.mp4")
  .stream()
  .overwriteOutput();

console.log("Command:", chainCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 4: Overlay one video on another
// ---------------------------------------------------------------------------
console.log("=== Example 4: Overlay ===");

const main = new InputNode("main.mp4");
const logo = new InputNode("logo.png");

const overlay = new FilterNode(
  "overlay",
  [main.video, logo.video],
  { x: 10, y: 10 },
  [StreamType.Video, StreamType.Video],
  [StreamType.Video],
);

const overlayCmd = new OutputNode([overlay.video(0)], "with_logo.mp4")
  .stream()
  .overwriteOutput();

console.log("Command:", overlayCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 5: Audio processing
// ---------------------------------------------------------------------------
console.log("=== Example 5: Audio processing ===");

const inp5 = new InputNode("input.mp4");

const volume = new FilterNode(
  "volume",
  [inp5.audio],
  { volume: 0.5 },
  [StreamType.Audio],
  [StreamType.Audio],
);

const echo = new FilterNode(
  "aecho",
  [volume.audio(0)],
  { in_gain: 0.8, out_gain: 0.88, delays: 60, decays: 0.4 },
  [StreamType.Audio],
  [StreamType.Audio],
);

const audioCmd = new OutputNode([echo.audio(0)], "audio_out.mp4")
  .stream()
  .overwriteOutput();

console.log("Command:", audioCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 6: Multiple outputs at different resolutions
// ---------------------------------------------------------------------------
console.log("=== Example 6: Multiple outputs ===");

const inp6 = new InputNode("input.mp4");

const hd = new FilterNode(
  "scale",
  [inp6.video],
  { w: 1920, h: 1080 },
  [StreamType.Video],
  [StreamType.Video],
);
const sd = new FilterNode(
  "scale",
  [inp6.video],
  { w: 1280, h: 720 },
  [StreamType.Video],
  [StreamType.Video],
);

const out1 = new OutputNode([hd.video(0)], "1080p.mp4");
const out2 = new OutputNode([sd.video(0)], "720p.mp4");

const multiCmd = mergeOutputs(out1.stream(), out2.stream());
console.log("Command:", multiCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 7: Input options (seeking, duration)
// ---------------------------------------------------------------------------
console.log("=== Example 7: Input options ===");

const trimmed = input("long_video.mp4", { ss: "00:01:00", t: "00:00:30" });
const trimCmd = output([trimmed], "clip.mp4").overwriteOutput();

console.log("Command:", trimCmd.compileLine());
console.log();

// ---------------------------------------------------------------------------
// Example 8: Compile as list for programmatic use
// ---------------------------------------------------------------------------
console.log("=== Example 8: Compile as list ===");

const inp8 = new InputNode("input.mp4");
const scaled8 = new FilterNode(
  "scale",
  [inp8.video],
  { w: 640, h: 480 },
  [StreamType.Video],
  [StreamType.Video],
);
const listCmd = new OutputNode([scaled8.video(0)], "small.mp4")
  .stream()
  .overwriteOutput();

const args = listCmd.compile();
console.log("Argument list:");
args.forEach((arg: string, i: number) => console.log(`  [${i}] ${arg}`));
