import { Serializable } from '../utils/serialize';

// Core types

export type StreamTypeEnum = 'av' | 'video' | 'audio';

export class StreamType extends Serializable {
  constructor(public value: StreamTypeEnum) {
    super();
  }
}

// Base abstract classes
export abstract class Node extends Serializable {
  constructor(
    public kwargs: Record<string, string | number | boolean>,
    public inputs: (Stream | null)[]
  ) {
    super();
  }
}

export abstract class Stream extends Serializable {
  constructor(
    public node: Node,
    public index: number | null
  ) {
    super();
  }
}

// Node types
export class FilterNode extends Node {
  constructor(
    public name: string,
    inputs: (FilterableStream | null)[],
    public input_typings: StreamType[],
    public output_typings: StreamType[],
    kwargs: Record<string, string | number | boolean> = {}
  ) {
    super(kwargs, inputs);
  }
}

export class InputNode extends Node {
  constructor(
    public filename: string,
    inputs: [] = [],
    kwargs: Record<string, string | number | boolean> = {}
  ) {
    super(kwargs, inputs);
  }
}

export class OutputNode extends Node {
  constructor(
    public filename: string,
    inputs: (FilterableStream | null)[],
    kwargs: Record<string, string | number | boolean> = {}
  ) {
    super(kwargs, inputs);
  }
}

export class GlobalNode extends Node {
  constructor(
    inputs: (OutputStream | null)[],
    kwargs: Record<string, string | number | boolean> = {}
  ) {
    super(kwargs, inputs);
  }
}

// Stream types
export class FilterableStream extends Stream {
  constructor(node: FilterNode | InputNode, index: number | null = null) {
    super(node, index);
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

export class OutputStream extends Stream {
  constructor(node: OutputNode, index: number | null = null) {
    super(node, index);
  }
}

export class GlobalStream extends Stream {
  constructor(node: GlobalNode, index: number | null = null) {
    super(node, index);
  }
}
