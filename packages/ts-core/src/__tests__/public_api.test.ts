import { describe, it, expect } from "vitest";
import * as api from "../index.js";

describe("public API (index.ts)", () => {
  it("exports StreamType enum", () => {
    expect(api.StreamType).toBeDefined();
    expect(api.StreamType.Video).toBeDefined();
    expect(api.StreamType.Audio).toBeDefined();
  });

  it("exports node classes", () => {
    expect(api.FilterNode).toBeDefined();
    expect(api.InputNode).toBeDefined();
    expect(api.OutputNode).toBeDefined();
    expect(api.GlobalNode).toBeDefined();
  });

  it("exports stream classes", () => {
    expect(api.VideoStream).toBeDefined();
    expect(api.AudioStream).toBeDefined();
    expect(api.SubtitleStream).toBeDefined();
    expect(api.AVStream).toBeDefined();
    expect(api.OutputStream).toBeDefined();
    expect(api.GlobalStream).toBeDefined();
    expect(api.FilterableStream).toBeDefined();
  });

  it("exports compile functions", () => {
    expect(api.compile).toBeDefined();
    expect(api.compileAsList).toBeDefined();
    expect(api.getStreamLabel).toBeDefined();
    expect(api.getArgs).toBeDefined();
  });

  it("exports validate functions", () => {
    expect(api.validate).toBeDefined();
    expect(api.fixGraph).toBeDefined();
    expect(api.removeSplit).toBeDefined();
    expect(api.addSplit).toBeDefined();
  });

  it("exports utility functions", () => {
    expect(api.escape).toBeDefined();
    expect(api.convertKwargsToArgs).toBeDefined();
    expect(api.merge).toBeDefined();
    expect(api.ignoreDefault).toBeDefined();
    expect(api.isDefault).toBeDefined();
    expect(api.isAuto).toBeDefined();
    expect(api.Default).toBeDefined();
    expect(api.Auto).toBeDefined();
    expect(api.commandLine).toBeDefined();
    expect(api.run).toBeDefined();
    expect(api.runAsync).toBeDefined();
    expect(api.runAwaitable).toBeDefined();
  });

  it("exports exception classes", () => {
    expect(api.FFMpegError).toBeDefined();
    expect(api.FFMpegTypeError).toBeDefined();
    expect(api.FFMpegValueError).toBeDefined();
    expect(api.FFMpegExecuteError).toBeDefined();
  });

  it("exports DAG helpers", () => {
    expect(api.filterNodeFactory).toBeDefined();
    expect(api.mergeOutputs).toBeDefined();
    expect(api.isDAG).toBeDefined();
    expect(api.DAGContext).toBeDefined();
  });

  it("exported InputNode is functional", () => {
    const node = new api.InputNode("test.mp4");
    expect(node.video).toBeInstanceOf(api.VideoStream);
    expect(node.audio).toBeInstanceOf(api.AudioStream);
  });
});
