import { describe, it, expect } from "vitest";
import { StreamType } from "../common/schema.js";
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  GlobalStream,
  VideoStream,
  AudioStream,
  mergeOutputs,
} from "../dag/nodes.js";
import { compileAsList, compile } from "../compile/compileCli.js";

// ─── OutputStream ──────────────────────────────────────────────────────────

describe("OutputStream", () => {
  it("compile() returns the CLI args list", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const args = output.stream().compile();

    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
    expect(args).toContain("output.mp4");
  });

  it("compileLine() returns a ffmpeg command string", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const line = output.stream().compileLine();

    expect(line).toMatch(/^ffmpeg /);
    expect(line).toContain("output.mp4");
  });

  it("overwriteOutput() produces a GlobalStream with -y flag", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const global = output.stream().overwriteOutput();

    expect(global).toBeInstanceOf(GlobalStream);
    expect(compileAsList(global)).toContain("-y");
  });

  it("globalArgs() passes through arbitrary global options", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const global = output.stream().globalArgs({ loglevel: "quiet" });

    const args = compileAsList(global);
    expect(args).toContain("-loglevel");
    expect(args).toContain("quiet");
  });

  it("run() executes the compiled command", () => {
    const input = new InputNode("hello"), output = new OutputNode([input.stream()], "world");
    // Use 'echo' as a stand-in binary: echo -i hello world
    const result = output.stream().run("echo");
    expect(result.stdout.toString()).toContain("hello");
  });

  it("runAsync() resolves the compiled command", async () => {
    const input = new InputNode("hello"), output = new OutputNode([input.stream()], "world");
    const result = await output.stream().runAsync("echo");
    expect(result.stdout.toString()).toContain("hello");
  });

  it("_globalNode() with additional streams and kwargs", () => {
    const input = new InputNode("input.mp4");
    const out1 = new OutputNode([input.stream()], "out1.mp4");
    const out2 = new OutputNode([input.stream()], "out2.mp4");
    const node = out1.stream()._globalNode([out2.stream()], { y: true });

    expect(node).toBeInstanceOf(GlobalNode);
    expect(node.inputs).toHaveLength(2);
    expect(node.kwargs.y).toBe(true);
  });
});

// ─── GlobalNode / GlobalStream ─────────────────────────────────────────────

describe("GlobalNode", () => {
  it("wraps output streams", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const node = new GlobalNode([out.stream()], { y: true });

    expect(node.inputs).toHaveLength(1);
    expect(node.kwargs.y).toBe(true);
  });

  it("stream() returns a GlobalStream", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const node = new GlobalNode([out.stream()]);

    expect(node.stream()).toBeInstanceOf(GlobalStream);
  });
});

describe("GlobalStream", () => {
  it("compile() returns CLI args list", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const global = out.stream().overwriteOutput();

    const args = global.compile();
    expect(args).toContain("-y");
    expect(args).toContain("-i");
    expect(args).toContain("output.mp4");
  });

  it("compileLine() returns a ffmpeg command string", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const line = out.stream().overwriteOutput().compileLine();

    expect(typeof line).toBe("string");
    expect(line).toMatch(/^ffmpeg /);
  });

  it("run() executes the compiled command", () => {
    const input = new InputNode("hello"), output = new OutputNode([input.stream()], "world");
    const result = output.stream().overwriteOutput().run("echo");
    expect(result.stdout.toString()).toContain("hello");
  });

  it("runAsync() resolves the compiled command", async () => {
    const input = new InputNode("hello"), output = new OutputNode([input.stream()], "world");
    const result = await output.stream().overwriteOutput().runAsync("echo");
    expect(result.stdout.toString()).toContain("hello");
  });

  it("overwriteOutput() is idempotent (single -y)", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const args = compileAsList(out.stream().overwriteOutput().overwriteOutput());

    expect(args.filter((a) => a === "-y")).toHaveLength(1);
  });

  it("globalArgs() merges with existing kwargs", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const global = out.stream()
      .globalArgs({ loglevel: "quiet" })
      .globalArgs({ y: true });

    const args = compileAsList(global);
    expect(args).toContain("-loglevel");
    expect(args).toContain("-y");
  });
});

// ─── mergeOutputs ─────────────────────────────────────────────────────────

describe("mergeOutputs", () => {
  it("returns the single stream unchanged", () => {
    const input = new InputNode("input.mp4");
    const out = new OutputNode([input.stream()], "output.mp4");
    const stream = out.stream();

    expect(mergeOutputs(stream)).toBe(stream);
  });

  it("wraps multiple outputs into a GlobalStream", () => {
    const input = new InputNode("input.mp4");
    const out1 = new OutputNode([input.stream()], "out1.mp4");
    const out2 = new OutputNode([input.stream()], "out2.mp4");

    const merged = mergeOutputs(out1.stream(), out2.stream());
    expect(merged).toBeInstanceOf(GlobalStream);

    const args = compileAsList(merged);
    expect(args).toContain("out1.mp4");
    expect(args).toContain("out2.mp4");
  });
});

// ─── VideoStream custom filters ────────────────────────────────────────────

describe("VideoStream.vfilter", () => {
  it("applies a custom video filter and returns VideoStream", () => {
    const input = new InputNode("input.mp4");
    const result = input.video.vfilter("hflip");

    expect(result).toBeInstanceOf(VideoStream);

    const output = new OutputNode([result], "output.mp4");
    const args = compileAsList(output.stream());
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).toContain("hflip");
  });

  it("passes kwargs to the filter", () => {
    const input = new InputNode("input.mp4");
    const result = input.video.vfilter("scale", { w: 1280, h: 720 });

    const output = new OutputNode([result], "output.mp4");
    const args = compileAsList(output.stream());
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).toContain("w=1280");
    expect(fc).toContain("h=720");
  });
});

describe("VideoStream.afilter", () => {
  it("applies a custom audio filter from a video stream and returns AudioStream", () => {
    const input = new InputNode("input.mp4");
    // inputTypings must match the actual stream type (Video) to pass validation
    const result = input.video.afilter("aecho", {}, { inputTypings: [StreamType.Video] });

    expect(result).toBeInstanceOf(AudioStream);
  });
});

describe("VideoStream.filterMultiOutput", () => {
  it("returns a FilterNode with multiple outputs", () => {
    const input = new InputNode("input.mp4");
    const splitNode = input.video.filterMultiOutput("split", { outputs: 2 }, {
      inputTypings: [StreamType.Video],
      outputTypings: [StreamType.Video, StreamType.Video],
    });

    const v0 = splitNode.video(0);
    const v1 = splitNode.video(1);
    expect(v0).toBeInstanceOf(VideoStream);
    expect(v1).toBeInstanceOf(VideoStream);
  });
});

// ─── AudioStream custom filters ────────────────────────────────────────────

describe("AudioStream.afilter", () => {
  it("applies a custom audio filter and returns AudioStream", () => {
    const input = new InputNode("input.mp4");
    const result = input.audio.afilter("volume", { volume: 2 });

    expect(result).toBeInstanceOf(AudioStream);

    const output = new OutputNode([result], "output.mp4");
    const args = compileAsList(output.stream());
    const fc = args[args.indexOf("-filter_complex") + 1] ?? "";
    expect(fc).toContain("volume");
  });
});

describe("AudioStream.vfilter", () => {
  it("applies a custom video filter from an audio stream and returns VideoStream", () => {
    const input = new InputNode("input.mp4");
    // inputTypings must match the actual stream type (Audio) to pass validation
    const result = input.audio.vfilter("hflip", {}, { inputTypings: [StreamType.Audio] });

    expect(result).toBeInstanceOf(VideoStream);
  });
});

describe("AudioStream.filterMultiOutput", () => {
  it("returns a FilterNode with multiple audio outputs", () => {
    const input = new InputNode("input.mp4");
    const splitNode = input.audio.filterMultiOutput("asplit", { outputs: 2 }, {
      inputTypings: [StreamType.Audio],
      outputTypings: [StreamType.Audio, StreamType.Audio],
    });

    expect(splitNode.audio(0)).toBeInstanceOf(AudioStream);
    expect(splitNode.audio(1)).toBeInstanceOf(AudioStream);
  });
});
