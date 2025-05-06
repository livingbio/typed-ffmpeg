import { FFmpegFilter } from './ffmpeg';

// Core types
export enum StreamType {
  audio = 'audio',
  video = 'video',
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
export interface FilterNode extends Node {
  name: string;
  inputs: FilterableStream[];
  input_typings: StreamType[];
  output_typings: StreamType[];
  filter: FFmpegFilter;
}

export interface InputNode extends Node {
  filename: string;
  inputs: [];
}

export interface OutputNode extends Node {
  filename: string;
  inputs: FilterableStream[];
}

export interface GlobalNode extends Node {
  inputs: OutputStream[];
}

// Stream types
export interface FilterableStream extends Stream {
  node: FilterNode | InputNode;
}

export interface VideoStream extends FilterableStream {
  node: FilterNode | InputNode;
}

export interface AudioStream extends FilterableStream {
  node: FilterNode | InputNode;
}

export interface AVStream extends FilterableStream {
  node: FilterNode | InputNode;
}

export interface OutputStream extends Stream {
  node: OutputNode;
}

export interface GlobalStream extends Stream {
  node: GlobalNode;
}
