import { Serializable } from "../utils/serialize";
import type { FFmpegFilter } from "./ffmpeg";

// Core types
export class StreamType extends Serializable {
  constructor(public value: string) {
    super();
  }
}

// Base interfaces
export interface Node {
  kwargs: Record<string, string | number | boolean>;
  inputs: Stream[];
}

export interface Stream {
  node: Node;
  index: number | null;
}

// Node types
export class FilterNode extends Serializable implements Node {
  constructor(
    public name: string,
    public inputs: FilterableStream[],
    public input_typings: StreamType[],
    public output_typings: StreamType[],
    public filter: FFmpegFilter,
    public kwargs: Record<string, string | number | boolean> = {},
  ) {
    super();
  }
}

export class InputNode extends Serializable implements Node {
  constructor(
    public filename: string,
    public inputs: [] = [],
    public kwargs: Record<string, string | number | boolean> = {},
  ) {
    super();
  }
}

export class OutputNode extends Serializable implements Node {
  constructor(
    public filename: string,
    public inputs: FilterableStream[],
    public kwargs: Record<string, string | number | boolean> = {},
  ) {
    super();
  }
}

export class GlobalNode extends Serializable implements Node {
  constructor(
    public inputs: OutputStream[],
    public kwargs: Record<string, string | number | boolean> = {},
  ) {
    super();
  }
}

// Stream types
export class FilterableStream extends Serializable implements Stream {
  constructor(
    public node: FilterNode | InputNode,
    public index: number | null = null,
  ) {
    super();
  }
}

export class VideoStream extends FilterableStream {
  constructor(node: FilterNode | InputNode, index: number | null = null) {
    super(node, index);
  }
}

export class AudioStream extends FilterableStream {
  constructor(node: FilterNode | InputNode, index: number | null = null) {
    super(node, index);
  }
}

export class AVStream extends FilterableStream {
  constructor(node: FilterNode | InputNode, index: number | null = null) {
    super(node, index);
  }
}

export class OutputStream extends Serializable implements Stream {
  constructor(
    public node: OutputNode,
    public index: number | null = null,
  ) {
    super();
  }
}

export class GlobalStream extends Serializable implements Stream {
  constructor(
    public node: GlobalNode,
    public index: number | null = null,
  ) {
    super();
  }
}
