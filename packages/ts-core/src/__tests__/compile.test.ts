import { describe, it, expect } from "vitest";
import { StreamType } from "../common/schema.js";
import {
  FilterNode,
  InputNode,
  OutputNode,
  OutputStream,
} from "../dag/nodes.js";
import { compileAsList } from "../compile/compileCli.js";

describe("compileAsList", () => {
  it("compiles a simple input -> output", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const stream = output.stream();

    const args = compileAsList(stream);
    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
    expect(args).toContain("output.mp4");
  });

  it("compiles a simple filter chain", () => {
    const input = new InputNode("input.mp4");
    const scale = new FilterNode(
      "scale",
      [input.video],
      { w: 1280, h: 720 },
      [StreamType.Video],
      [StreamType.Video],
    );
    const output = new OutputNode([scale.video(0)], "output.mp4");
    const stream = output.stream();

    const args = compileAsList(stream);
    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
    expect(args).toContain("-filter_complex");
    expect(args).toContain("output.mp4");

    // Check the filter_complex contains scale
    const fcIdx = args.indexOf("-filter_complex");
    const filterStr = args[fcIdx + 1];
    expect(filterStr).toContain("scale");
    expect(filterStr).toContain("w=1280");
    expect(filterStr).toContain("h=720");
  });

  it("compiles with global options", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const stream = output.stream();
    const global = stream.overwriteOutput();

    const args = compileAsList(global);
    expect(args).toContain("-y");
    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
    expect(args).toContain("output.mp4");
  });

  it("compiles multi-input filter (overlay)", () => {
    const a = new InputNode("a.mp4");
    const b = new InputNode("b.mp4");
    const overlay = new FilterNode(
      "overlay",
      [a.video, b.video],
      { x: 10, y: 20 },
      [StreamType.Video, StreamType.Video],
      [StreamType.Video],
    );
    const output = new OutputNode([overlay.video(0)], "out.mp4");
    const stream = output.stream();

    const args = compileAsList(stream);
    expect(args).toContain("-filter_complex");

    const fcIdx = args.indexOf("-filter_complex");
    const filterStr = args[fcIdx + 1];
    expect(filterStr).toContain("overlay");
    expect(filterStr).toContain("[0:v]");
    expect(filterStr).toContain("[1:v]");
  });

  it("compiles with input options", () => {
    const input = new InputNode("input.mp4", { ss: 10, t: 30 });
    const output = new OutputNode([input.stream()], "output.mp4");
    const stream = output.stream();

    const args = compileAsList(stream);
    expect(args).toContain("-ss");
    expect(args).toContain("10");
    expect(args).toContain("-t");
    expect(args).toContain("30");
  });

  it("compiles with output options", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4", {
      "c:v": "libx264",
      crf: 23,
    });
    const stream = output.stream();

    const args = compileAsList(stream);
    expect(args).toContain("-c:v");
    expect(args).toContain("libx264");
    expect(args).toContain("-crf");
    expect(args).toContain("23");
  });
});
