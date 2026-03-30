import { Serializable } from '../utils/serialize';

// Core types

export type StreamTypeEnum = 'av' | 'video' | 'audio';

export class StreamType extends Serializable {
  static className = 'StreamType';
  constructor(public value: StreamTypeEnum) {
    super();
  }
}

// Base abstract classes
export abstract class Node extends Serializable {
  static className = 'Node';
  constructor(
    public kwargs: Record<string, string | number | boolean>,
    public inputs: (Stream | null)[],
    id?: string
  ) {
    super(id);
  }
}

export abstract class Stream extends Serializable {
  static className = 'Stream';
  constructor(
    public node: Node,
    public index: number | null,
    id?: string
  ) {
    super(id);
  }
}

// Node types
export class FilterNode extends Node {
  static className = 'FilterNode';
  constructor(
    public name: string,
    inputs: (FilterableStream | null)[],
    public input_typings: StreamType[],
    public output_typings: StreamType[],
    kwargs: Record<string, string | number | boolean> = {},
    id?: string
  ) {
    super(kwargs, inputs, id);
  }
}

export class InputNode extends Node {
  static className = 'InputNode';
  constructor(
    public filename: string,
    inputs: [] = [],
    kwargs: Record<string, string | number | boolean> = {},
    id?: string
  ) {
    super(kwargs, inputs, id);
  }
}

export class OutputNode extends Node {
  static className = 'OutputNode';
  constructor(
    public filename: string,
    inputs: (FilterableStream | null)[],
    kwargs: Record<string, string | number | boolean> = {},
    id?: string
  ) {
    super(kwargs, inputs, id);
  }
}

export class GlobalNode extends Node {
  static className = 'GlobalNode';
  constructor(
    inputs: (OutputStream | null)[],
    kwargs: Record<string, string | number | boolean> = {},
    id?: string
  ) {
    super(kwargs, inputs, id);
  }
}

// Stream types
export class FilterableStream extends Stream {
  static className = 'FilterableStream';
  constructor(node: FilterNode | InputNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}

export class VideoStream extends FilterableStream {
  static className = 'VideoStream';
  constructor(node: FilterNode | InputNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}

export class AudioStream extends FilterableStream {
  static className = 'AudioStream';
  constructor(node: FilterNode | InputNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}

export class AVStream extends FilterableStream {
  static className = 'AVStream';
  constructor(node: FilterNode | InputNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}

export class OutputStream extends Stream {
  static className = 'OutputStream';
  constructor(node: OutputNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}

export class GlobalStream extends Stream {
  static className = 'GlobalStream';
  constructor(node: GlobalNode, index: number | null = null, id?: string) {
    super(node, index, id);
  }
}
