import { describe, it, expect } from "vitest";
import { StreamType } from "../common/schema.js";
import { FilterNode, InputNode, OutputNode, VideoStream, AudioStream } from "../dag/nodes.js";
import { addSplit, removeSplit, fixGraph, validate } from "../compile/validate.js";
import { compileAsList } from "../compile/compileCli.js";

describe("removeSplit", () => {
  it("is a no-op when there are no split nodes", () => {
    const input = new InputNode("input.mp4");
    const scale = new FilterNode(
      "scale",
      [input.video],
      { w: 1280 },
      [StreamType.Video],
      [StreamType.Video],
    );
    const output = new OutputNode([scale.video(0)], "output.mp4");
    const stream = output.stream();

    const [result] = removeSplit(stream);
    const args = compileAsList(result, false);
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).toContain("scale");
  });

  it("removes an explicit split node", () => {
    const input = new InputNode("input.mp4");
    const split = new FilterNode(
      "split",
      [input.video],
      { outputs: 2 },
      [StreamType.Video],
      [StreamType.Video, StreamType.Video],
    );
    const output = new OutputNode([split.video(0)], "output.mp4");
    const [result] = removeSplit(output.stream());

    const args = compileAsList(result, false);
    // split node should be gone
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).not.toContain("split");
  });

  it("removes an asplit node", () => {
    const input = new InputNode("input.mp4");
    const asplit = new FilterNode(
      "asplit",
      [input.audio],
      { outputs: 2 },
      [StreamType.Audio],
      [StreamType.Audio, StreamType.Audio],
    );
    const output = new OutputNode([asplit.audio(0)], "output.mp4");
    const [result] = removeSplit(output.stream());

    const args = compileAsList(result, false);
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).not.toContain("asplit");
  });
});

describe("addSplit", () => {
  it("inserts a split node when a video stream is shared", () => {
    const input = new InputNode("input.mp4");
    const scale = new FilterNode(
      "scale",
      [input.video],
      { w: 1280 },
      [StreamType.Video],
      [StreamType.Video],
    );
    const shared = scale.video(0);

    // Both outputs share the same stream instance
    const out1 = new OutputNode([shared], "out1.mp4");
    const out2 = new OutputNode([shared], "out2.mp4");
    const global = out1.stream()._globalNode([out2.stream()]).stream();

    const args = compileAsList(global);
    const fcIdx = args.indexOf("-filter_complex");
    const fc = args[fcIdx + 1] ?? "";
    expect(fc).toContain("split");
  });

  it("inserts an asplit node when an audio stream is shared", () => {
    const input = new InputNode("input.mp4");
    const volume = new FilterNode(
      "volume",
      [input.audio],
      { volume: 2 },
      [StreamType.Audio],
      [StreamType.Audio],
    );
    const shared = volume.audio(0);

    const out1 = new OutputNode([shared], "out1.mp4");
    const out2 = new OutputNode([shared], "out2.mp4");
    const global = out1.stream()._globalNode([out2.stream()]).stream();

    const args = compileAsList(global);
    const fcIdx = args.indexOf("-filter_complex");
    const fc = args[fcIdx + 1] ?? "";
    expect(fc).toContain("asplit");
  });

  it("does not insert split for input node reused by multiple outputs", () => {
    const input = new InputNode("input.mp4");
    const shared = input.video;

    const out1 = new OutputNode([shared], "out1.mp4");
    const out2 = new OutputNode([shared], "out2.mp4");
    const global = out1.stream()._globalNode([out2.stream()]).stream();

    const args = compileAsList(global);
    const fcIdx = args.indexOf("-filter_complex");
    // InputNode reuse doesn't need split — no filter_complex
    expect(fcIdx).toBe(-1);
  });
});

describe("fixGraph", () => {
  it("round-trips a graph without splits unchanged", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.video], "output.mp4");
    const stream = output.stream();

    const fixed = fixGraph(stream);
    expect(compileAsList(fixed, false)).toContain("output.mp4");
  });

  it("normalizes a graph with an explicit split into one with split inferred", () => {
    const input = new InputNode("input.mp4");
    // The shared stream must come from a FilterNode (not InputNode) for split to be re-added
    const scale = new FilterNode(
      "scale",
      [input.video],
      { w: 1280 },
      [StreamType.Video],
      [StreamType.Video],
    );
    const scaleOut = scale.video(0);
    const split = new FilterNode(
      "split",
      [scaleOut],
      { outputs: 2 },
      [StreamType.Video],
      [StreamType.Video, StreamType.Video],
    );
    const out1 = new OutputNode([split.video(0)], "out1.mp4");
    const out2 = new OutputNode([split.video(1)], "out2.mp4");
    const global = out1.stream()._globalNode([out2.stream()]).stream();

    const fixed = fixGraph(global);
    const args = compileAsList(fixed, false);
    // split is still present (re-added by addSplit for the shared FilterNode output)
    const fcIdx = args.indexOf("-filter_complex");
    const fc = args[fcIdx + 1] ?? "";
    expect(fc).toContain("split");
  });
});

describe("validate", () => {
  it("with autoFix=false returns the stream unchanged", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.video], "output.mp4");
    const stream = output.stream();

    const result = validate(stream, false);
    expect(result).toBe(stream);
  });

  it("with autoFix=true (default) fixes shared streams", () => {
    const input = new InputNode("input.mp4");
    const scale = new FilterNode(
      "scale",
      [input.video],
      {},
      [StreamType.Video],
      [StreamType.Video],
    );
    const shared = scale.video(0);
    const out1 = new OutputNode([shared], "out1.mp4");
    const out2 = new OutputNode([shared], "out2.mp4");
    const global = out1.stream()._globalNode([out2.stream()]).stream();

    const result = validate(global, true);
    const args = compileAsList(result, false);
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).toContain("split");
  });
});
