import { describe, it, expect } from "vitest";
import { StreamType } from "../common/schema.js";
import {
  FilterNode,
  InputNode,
  OutputNode,
  OutputStream,
} from "../dag/nodes.js";
import { compileAsList, compile, getArgs, getNodeLabel } from "../compile/compileCli.js";
import { DAGContext } from "../compile/context.js";
import { GlobalNode } from "../dag/nodes.js";

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

describe("compile", () => {
  it("returns a ffmpeg command string", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const result = compile(output.stream());

    expect(result).toMatch(/^ffmpeg /);
    expect(result).toContain("input.mp4");
    expect(result).toContain("output.mp4");
  });

  it("includes -y when overwriteOutput is set", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const result = compile(output.stream().overwriteOutput());

    expect(result).toContain("-y");
  });
});

describe("getArgs", () => {
  it("dispatches to getArgsInputNode", () => {
    const node = new InputNode("input.mp4", { ss: 10 });
    const context = DAGContext.build(node);
    const args = getArgs(node, context);

    expect(args).toContain("-ss");
    expect(args).toContain("10");
    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
  });

  it("dispatches to getArgsFilterNode", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode(
      "scale",
      [input.video],
      { w: 1280 },
      [StreamType.Video],
      [StreamType.Video],
    );
    const output = new OutputNode([filter.video(0)], "output.mp4");
    const context = DAGContext.build(output);
    const args = getArgs(filter, context);

    expect(args.join("")).toContain("scale");
  });

  it("dispatches to getArgsOutputNode", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const context = DAGContext.build(output);
    const args = getArgs(output, context);

    expect(args).toContain("output.mp4");
  });

  it("dispatches to getArgsGlobalNode", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const globalNode = new GlobalNode([output.stream()], { y: true });
    const context = DAGContext.build(globalNode);
    const args = getArgs(globalNode, context);

    expect(args).toContain("-y");
  });

  it("builds context automatically when none provided", () => {
    const input = new InputNode("input.mp4");
    const args = getArgs(input);

    expect(args).toContain("-i");
    expect(args).toContain("input.mp4");
  });
});

describe("DAGContext.nodeLabels / getNodeLabel", () => {
  it("nodeLabels maps InputNode to numeric string", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const ctx = DAGContext.build(output);

    expect(ctx.nodeLabels.get(input)).toBe("0");
  });

  it("nodeLabels maps FilterNode to s-prefixed string", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode("scale", [input.video], {}, [StreamType.Video], [StreamType.Video]);
    const output = new OutputNode([filter.video(0)], "output.mp4");
    const ctx = DAGContext.build(output);

    expect(ctx.nodeLabels.get(filter)).toBe("s0");
  });

  it("getNodeLabel returns the label for a node", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const ctx = DAGContext.build(output);

    expect(ctx.getNodeLabel(input)).toBe("0");
  });

  it("getNodeLabel returns 'out' for unknown node", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    // Build context from input only — output is not in its nodes
    const ctx = DAGContext.build(input);

    expect(ctx.getNodeLabel(output)).toBe("out");
  });
});

describe("getNodeLabel", () => {
  it("returns numeric string for InputNode", () => {
    const input = new InputNode("input.mp4");
    const context = DAGContext.build(input);
    expect(getNodeLabel(input, context)).toBe("0");
  });

  it("returns s-prefixed string for FilterNode", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode("scale", [input.video], {}, [StreamType.Video], [StreamType.Video]);
    const output = new OutputNode([filter.video(0)], "output.mp4");
    const context = DAGContext.build(output);
    expect(getNodeLabel(filter, context)).toBe("s0");
  });

  it("returns 'out' for OutputNode", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.stream()], "output.mp4");
    const context = DAGContext.build(output);
    expect(getNodeLabel(output, context)).toBe("out");
  });
});
