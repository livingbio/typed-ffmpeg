/**
 * Base stream classes for filterable streams.
 *
 * FilterableStream is the base for VideoStream and AudioStream.
 * It provides methods for applying custom filters via a late-bound
 * node factory to avoid circular imports with nodes.ts.
 */

import { StreamType } from "../common/schema.js";
import type { KwargsValue } from "../utils/frozenRecord.js";
import type { RunResult } from "../utils/run.js";
import { Node, Stream } from "./schema.js";

/**
 * A stream that can be used as input to an FFmpeg filter.
 * Base class for VideoStream and AudioStream.
 */
export abstract class FilterableStream extends Stream {
  declare readonly node: Node;

  /** The stream type (video or audio) of this stream. */
  abstract get streamType(): StreamType;
}

/**
 * Late-bound reference to node constructors.
 * Set by nodes.ts after it loads to break the circular dependency.
 */
export const _nodeFactories: {
  createFilterNode?: (
    name: string,
    inputs: readonly FilterableStream[],
    kwargs: Record<string, KwargsValue>,
    inputTypings: readonly StreamType[],
    outputTypings: readonly StreamType[],
  ) => { video(index: number): FilterableStream; audio(index: number): FilterableStream };
  createOutputNode?: (
    inputs: readonly FilterableStream[],
    filename: string,
    kwargs?: Record<string, KwargsValue>,
  ) => Node;
} = {};

/**
 * Late-bound reference to compile functions.
 * Set by compileCli.ts after it loads to break the circular dependency
 * (compileCli.ts → nodes.ts → baseStreams.ts).
 */
export const _compileFactories: {
  compileAsList?: (stream: Stream, autoFix?: boolean) => string[];
  compile?: (stream: Stream, autoFix?: boolean) => string;
  run?: (args: string[], ffmpegBinary?: string) => RunResult;
  runAwaitable?: (args: string[], ffmpegBinary?: string) => Promise<RunResult>;
} = {};

/**
 * Apply a custom filter with multiple outputs.
 */
export function filterMultiOutput(
  self: FilterableStream,
  name: string,
  kwargs: Record<string, KwargsValue> = {},
  options?: {
    additionalInputs?: FilterableStream[];
    inputTypings?: StreamType[];
    outputTypings?: StreamType[];
  },
): { video(index: number): FilterableStream; audio(index: number): FilterableStream } {
  if (!_nodeFactories.createFilterNode) {
    throw new Error("Node factories not initialized. Import nodes.ts first.");
  }
  const additionalInputs = options?.additionalInputs ?? [];
  const allInputs: FilterableStream[] = [self, ...additionalInputs];
  const inputTypings =
    options?.inputTypings ?? allInputs.map((s) => s.streamType);
  const outputTypings = options?.outputTypings ?? [];

  return _nodeFactories.createFilterNode(
    name,
    allInputs,
    kwargs,
    inputTypings,
    outputTypings,
  );
}
