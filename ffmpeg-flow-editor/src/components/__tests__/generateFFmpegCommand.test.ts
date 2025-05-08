import type { Edge, Node } from "reactflow";
import { describe, expect, it } from "vitest";
import { generateFFmpegCommand } from "../../utils/generateFFmpegCommand";

interface FilterData {
  filterType: "input" | "output" | "filter";
  filterName?: string;
  parameters?: Record<string, string>;
}

interface FilterNode extends Node {
  type: "filter";
  data: FilterData;
}

describe("generateFFmpegCommand", () => {
  it("returns empty python string if no input or output nodes", () => {
    const nodes: FilterNode[] = [];
    const edges: Edge[] = [];
    expect(generateFFmpegCommand(nodes, edges)).toEqual({ python: "" });
  });

  it("generates basic input-output chain", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "output1",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).toContain('output0 = ffmpeg.output(input0, filename="output0.mp4")');
  });

  it("generates code with filter nodes", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "filter1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: {
          filterType: "filter",
          filterName: "scale",
          parameters: { width: "1280", height: "720" },
        },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "filter1",
      },
      {
        id: "edge2",
        source: "filter1",
        target: "output1",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).toContain("stream_filter1 = input0.scale(width=1280, height=720)");
    expect(result.python).toContain(
      'output0 = ffmpeg.output(stream_filter1, filename="output0.mp4")',
    );
  });

  it("handles multiple input and output nodes", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "input2",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
      {
        id: "output2",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "output1",
      },
      {
        id: "edge2",
        source: "input2",
        target: "output2",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).toContain('input1 = ffmpeg.input("input1.mp4")');
    expect(result.python).toContain('output0 = ffmpeg.output(input0, filename="output0.mp4")');
    expect(result.python).toContain('output1 = ffmpeg.output(input1, filename="output1.mp4")');
    expect(result.python).toContain("ffmpeg.merge_outputs(output0, output1).compile_line()");
  });

  it("handles complex filter chains", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "filter1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: {
          filterType: "filter",
          filterName: "scale",
          parameters: { width: "1280", height: "720" },
        },
      },
      {
        id: "filter2",
        type: "filter",
        position: { x: 0, y: 0 },
        data: {
          filterType: "filter",
          filterName: "crop",
          parameters: { x: "0", y: "0", width: "640", height: "480" },
        },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "filter1",
      },
      {
        id: "edge2",
        source: "filter1",
        target: "filter2",
      },
      {
        id: "edge3",
        source: "filter2",
        target: "output1",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).toContain("stream_filter1 = input0.scale(width=1280, height=720)");
    expect(result.python).toContain(
      "stream_filter2 = stream_filter1.crop(x=0, y=0, width=640, height=480)",
    );
    expect(result.python).toContain(
      'output0 = ffmpeg.output(stream_filter2, filename="output0.mp4")',
    );
  });

  it("handles numeric and boolean parameters correctly", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "filter1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: {
          filterType: "filter",
          filterName: "filter",
          parameters: {
            number: "42",
            boolean: "true",
            string: "test",
          },
        },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "filter1",
      },
      {
        id: "edge2",
        source: "filter1",
        target: "output1",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).toContain(
      'stream_filter1 = input0.filter(number=42, boolean=true, string="test")',
    );
    expect(result.python).toContain(
      'output0 = ffmpeg.output(stream_filter1, filename="output0.mp4")',
    );
  });

  it("handles disconnected nodes", () => {
    const nodes: FilterNode[] = [
      {
        id: "input1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "input" },
      },
      {
        id: "filter1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: {
          filterType: "filter",
          filterName: "scale",
          parameters: { width: "1280", height: "720" },
        },
      },
      {
        id: "output1",
        type: "filter",
        position: { x: 0, y: 0 },
        data: { filterType: "output" },
      },
    ];
    const edges: Edge[] = [
      {
        id: "edge1",
        source: "input1",
        target: "output1",
      },
    ];

    const result = generateFFmpegCommand(nodes, edges);
    expect(result.python).toContain("import ffmpeg");
    expect(result.python).toContain('input0 = ffmpeg.input("input0.mp4")');
    expect(result.python).not.toContain("scale");
    expect(result.python).toContain('output0 = ffmpeg.output(input0, filename="output0.mp4")');
  });
});
