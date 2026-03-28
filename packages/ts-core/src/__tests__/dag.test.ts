import { describe, it, expect } from "vitest";
import { StreamType } from "../common/schema.js";
import {
  FilterNode,
  InputNode,
  OutputNode,
  VideoStream,
  AudioStream,
  AVStream,
} from "../dag/nodes.js";
import { filterNodeFactory } from "../dag/factory.js";
import { FFMpegValueError, FFMpegTypeError } from "../exceptions.js";

describe("InputNode", () => {
  it("creates an input node with filename", () => {
    const node = new InputNode("input.mp4");
    expect(node.filename).toBe("input.mp4");
    expect(node.inputs).toHaveLength(0);
    expect(node.repr()).toBe("input.mp4");
  });

  it("provides video and audio stream accessors", () => {
    const node = new InputNode("input.mp4");
    const video = node.video;
    const audio = node.audio;

    expect(video).toBeInstanceOf(VideoStream);
    expect(audio).toBeInstanceOf(AudioStream);
    expect(video.node).toBe(node);
    expect(audio.node).toBe(node);
  });

  it("provides a combined AV stream", () => {
    const node = new InputNode("input.mp4");
    const av = node.stream();
    expect(av).toBeInstanceOf(AVStream);
    expect(av.node).toBe(node);
  });

  it("creates input with kwargs", () => {
    const node = new InputNode("input.mp4", { ss: 10, t: 30 });
    expect(node.kwargs.ss).toBe(10);
    expect(node.kwargs.t).toBe(30);
  });
});

describe("FilterNode", () => {
  it("creates a simple video filter", () => {
    const input = new InputNode("input.mp4");
    const video = input.video;

    const filter = new FilterNode(
      "scale",
      [video],
      { w: 1280, h: 720 },
      [StreamType.Video],
      [StreamType.Video],
    );

    expect(filter.name).toBe("scale");
    expect(filter.inputs).toHaveLength(1);
    expect(filter.repr()).toBe("scale");
  });

  it("extracts video output streams", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode(
      "scale",
      [input.video],
      {},
      [StreamType.Video],
      [StreamType.Video],
    );

    const output = filter.video(0);
    expect(output).toBeInstanceOf(VideoStream);
    expect(output.node).toBe(filter);
    expect(output.index).toBe(0);
  });

  it("extracts audio output streams", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode(
      "volume",
      [input.audio],
      { volume: 2 },
      [StreamType.Audio],
      [StreamType.Audio],
    );

    const output = filter.audio(0);
    expect(output).toBeInstanceOf(AudioStream);
  });

  it("throws on out-of-range video index", () => {
    const input = new InputNode("input.mp4");
    const filter = new FilterNode(
      "scale",
      [input.video],
      {},
      [StreamType.Video],
      [StreamType.Video],
    );

    expect(() => filter.video(1)).toThrow(FFMpegValueError);
  });

  it("throws on input count mismatch", () => {
    const input = new InputNode("input.mp4");
    expect(
      () =>
        new FilterNode(
          "overlay",
          [input.video],
          {},
          [StreamType.Video, StreamType.Video],
          [StreamType.Video],
        ),
    ).toThrow(FFMpegValueError);
  });

  it("throws on input type mismatch", () => {
    const input = new InputNode("input.mp4");
    expect(
      () =>
        new FilterNode(
          "scale",
          [input.audio],
          {},
          [StreamType.Video],
          [StreamType.Video],
        ),
    ).toThrow(FFMpegTypeError);
  });

  it("supports multi-input filters", () => {
    const a = new InputNode("a.mp4");
    const b = new InputNode("b.mp4");

    const overlay = new FilterNode(
      "overlay",
      [a.video, b.video],
      { x: 10, y: 10 },
      [StreamType.Video, StreamType.Video],
      [StreamType.Video],
    );

    expect(overlay.inputs).toHaveLength(2);
    const output = overlay.video(0);
    expect(output).toBeInstanceOf(VideoStream);
  });

  it("supports multi-output filters (split)", () => {
    const input = new InputNode("input.mp4");
    const split = new FilterNode(
      "split",
      [input.video],
      { outputs: 2 },
      [StreamType.Video],
      [StreamType.Video, StreamType.Video],
    );

    const out0 = split.video(0);
    const out1 = split.video(1);
    expect(out0.index).toBe(0);
    expect(out1.index).toBe(1);
  });
});

describe("OutputNode", () => {
  it("creates an output node", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.video], "output.mp4");

    expect(output.filename).toBe("output.mp4");
    expect(output.inputs).toHaveLength(1);
    expect(output.repr()).toBe("output.mp4");
  });

  it("creates an output stream", () => {
    const input = new InputNode("input.mp4");
    const output = new OutputNode([input.video], "output.mp4");
    const stream = output.stream();

    expect(stream.node).toBe(output);
  });
});

describe("filterNodeFactory", () => {
  it("creates a filter node from a definition", () => {
    const input = new InputNode("input.mp4");
    const node = filterNodeFactory(
      {
        name: "scale",
        typingsInput: ["video"],
        typingsOutput: ["video"],
      },
      [input.video],
      { w: 1280, h: 720 },
    );

    expect(node).toBeInstanceOf(FilterNode);
    expect(node.name).toBe("scale");
    expect(node.kwargs.w).toBe(1280);
    expect(node.kwargs.h).toBe(720);
  });
});

describe("upstream nodes", () => {
  it("collects all upstream nodes", () => {
    const input = new InputNode("input.mp4");
    const scale = new FilterNode(
      "scale",
      [input.video],
      {},
      [StreamType.Video],
      [StreamType.Video],
    );
    const output = new OutputNode([scale.video(0)], "output.mp4");

    const upstream = output.upstreamNodes;
    expect(upstream.size).toBe(3); // output, scale, input
  });
});
