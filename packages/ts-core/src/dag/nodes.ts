/**
 * DAG node definitions for FFmpeg filter graphs.
 */

import { StreamType } from "../common/schema.js";
import { FFMpegTypeError, FFMpegValueError } from "../exceptions.js";
import type { KwargsValue } from "../utils/frozenRecord.js";
import { FilterableStream, _nodeFactories, _compileFactories, filterMultiOutput } from "./baseStreams.js";
import { Node, Stream } from "./schema.js";
import { run as runSync, runAwaitable } from "../utils/run.js";
import type { RunResult } from "../utils/run.js";


// ─── Concrete Stream Types ─────────────────────────────────────────────────

/** A video stream in the filter graph. */
export class VideoStream extends FilterableStream {
  get streamType(): StreamType {
    return StreamType.Video;
  }

  /** Apply a custom video filter. */
  vfilter(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
    },
  ): VideoStream {
    const node = filterMultiOutput(this, name, kwargs, {
      additionalInputs: options?.additionalInputs,
      inputTypings: options?.inputTypings ?? [StreamType.Video],
      outputTypings: [StreamType.Video],
    });
    return node.video(0) as VideoStream;
  }

  /** Apply a custom audio filter. */
  afilter(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
    },
  ): AudioStream {
    const node = filterMultiOutput(this, name, kwargs, {
      additionalInputs: options?.additionalInputs,
      inputTypings: options?.inputTypings ?? [StreamType.Audio],
      outputTypings: [StreamType.Audio],
    });
    return node.audio(0) as AudioStream;
  }

  /** Apply a filter with multiple outputs. */
  filterMultiOutput(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
      outputTypings?: StreamType[];
    },
  ): FilterNode {
    return filterMultiOutput(this, name, kwargs, options) as FilterNode;
  }
}

/** An audio stream in the filter graph. */
export class AudioStream extends FilterableStream {
  get streamType(): StreamType {
    return StreamType.Audio;
  }

  /** Apply a custom video filter. */
  vfilter(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
    },
  ): VideoStream {
    const node = filterMultiOutput(this, name, kwargs, {
      additionalInputs: options?.additionalInputs,
      inputTypings: options?.inputTypings ?? [StreamType.Video],
      outputTypings: [StreamType.Video],
    });
    return node.video(0) as VideoStream;
  }

  /** Apply a custom audio filter. */
  afilter(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
    },
  ): AudioStream {
    const node = filterMultiOutput(this, name, kwargs, {
      additionalInputs: options?.additionalInputs,
      inputTypings: options?.inputTypings ?? [StreamType.Audio],
      outputTypings: [StreamType.Audio],
    });
    return node.audio(0) as AudioStream;
  }

  /** Apply a filter with multiple outputs. */
  filterMultiOutput(
    name: string,
    kwargs: Record<string, KwargsValue> = {},
    options?: {
      additionalInputs?: FilterableStream[];
      inputTypings?: StreamType[];
      outputTypings?: StreamType[];
    },
  ): FilterNode {
    return filterMultiOutput(this, name, kwargs, options) as FilterNode;
  }
}

/** A subtitle stream in the filter graph. */
export class SubtitleStream extends FilterableStream {
  get streamType(): StreamType {
    return StreamType.Video; // Subtitles use video StreamType in FFmpeg
  }
}

/** A combined audio+video stream (e.g., from an InputNode). */
export class AVStream extends FilterableStream {
  get streamType(): StreamType {
    return StreamType.Video;
  }

  videoStream(index?: number | null, optional: boolean = false): VideoStream {
    return new VideoStream(this.node, index ?? null, optional);
  }

  audioStream(index?: number | null, optional: boolean = false): AudioStream {
    return new AudioStream(this.node, index ?? null, optional);
  }

  subtitleStream(index?: number | null, optional: boolean = false): SubtitleStream {
    return new SubtitleStream(this.node, index ?? null, optional);
  }

  get video(): VideoStream {
    return new VideoStream(this.node);
  }

  get audio(): AudioStream {
    return new AudioStream(this.node);
  }
}

// ─── Concrete Node Types ────────────────────────────────────────────────────

/** A node representing an FFmpeg filter operation. */
export class FilterNode extends Node {
  readonly name: string;
  declare readonly inputs: readonly FilterableStream[];
  readonly inputTypings: readonly StreamType[];
  readonly outputTypings: readonly StreamType[];

  constructor(
    name: string,
    inputs: readonly FilterableStream[] = [],
    kwargs: Record<string, KwargsValue> = {},
    inputTypings: readonly StreamType[] = [],
    outputTypings: readonly StreamType[] = [],
  ) {
    super(kwargs, inputs);
    this.name = name;
    this.inputTypings = Object.freeze([...inputTypings]);
    this.outputTypings = Object.freeze([...outputTypings]);
    this._validateTypings();
  }

  override repr(): string {
    return this.name;
  }

  /** Get a video output stream by index among video outputs. */
  video(index: number): VideoStream {
    const videoOutputs: number[] = [];
    for (let i = 0; i < this.outputTypings.length; i++) {
      if (this.outputTypings[i] === StreamType.Video) videoOutputs.push(i);
    }
    if (index >= videoOutputs.length) {
      throw new FFMpegValueError(
        `Index ${index} out of range for video outputs (${videoOutputs.length})`,
      );
    }
    return new VideoStream(this, videoOutputs[index]);
  }

  /** Get an audio output stream by index among audio outputs. */
  audio(index: number): AudioStream {
    const audioOutputs: number[] = [];
    for (let i = 0; i < this.outputTypings.length; i++) {
      if (this.outputTypings[i] === StreamType.Audio) audioOutputs.push(i);
    }
    if (index >= audioOutputs.length) {
      throw new FFMpegValueError(
        `Index ${index} out of range for audio outputs (${audioOutputs.length})`,
      );
    }
    return new AudioStream(this, audioOutputs[index]);
  }

  private _validateTypings(): void {
    if (this.inputs.length !== this.inputTypings.length) {
      throw new FFMpegValueError(
        `Expected ${this.inputTypings.length} inputs, got ${this.inputs.length}`,
      );
    }
    for (let i = 0; i < this.inputs.length; i++) {
      const stream = this.inputs[i];
      const expected = this.inputTypings[i];
      if (expected === StreamType.Video && !(stream instanceof VideoStream)) {
        throw new FFMpegTypeError(
          `Expected input ${i} to have video component, got ${stream.constructor.name}`,
        );
      }
      if (expected === StreamType.Audio && !(stream instanceof AudioStream)) {
        throw new FFMpegTypeError(
          `Expected input ${i} to have audio component, got ${stream.constructor.name}`,
        );
      }
    }
  }
}

/** A node representing an input file. */
export class InputNode extends Node {
  readonly filename: string;

  constructor(filename: string, kwargs: Record<string, KwargsValue> = {}) {
    super(kwargs, []);
    this.filename = filename;
  }

  override repr(): string {
    return this.filename.replace(/^.*[\\/]/, '') || this.filename;
  }

  get video(): VideoStream {
    return new VideoStream(this);
  }

  get audio(): AudioStream {
    return new AudioStream(this);
  }

  stream(): AVStream {
    return new AVStream(this);
  }
}

/** A node representing an output file. */
export class OutputNode extends Node {
  readonly filename: string;
  declare readonly inputs: readonly FilterableStream[];

  constructor(
    inputs: readonly FilterableStream[],
    filename: string,
    kwargs: Record<string, KwargsValue> = {},
  ) {
    super(kwargs, inputs);
    this.filename = filename;
  }

  override repr(): string {
    return this.filename.replace(/^.*[\\/]/, '') || this.filename;
  }

  stream(): OutputStream {
    return new OutputStream(this);
  }
}

// ─── Output / Global Stream Types ───────────────────────────────────────────

/** A stream representing an output file with execution capabilities. */
export class OutputStream extends Stream {
  declare readonly node: OutputNode;

  constructor(node: OutputNode) {
    super(node);
  }

  _globalNode(
    additionalStreams: OutputStream[] = [],
    kwargs: Record<string, KwargsValue> = {},
  ): GlobalNode {
    return new GlobalNode([this, ...additionalStreams], kwargs);
  }

  globalArgs(kwargs: Record<string, KwargsValue> = {}): GlobalStream {
    return this._globalNode([], kwargs).stream();
  }

  overwriteOutput(): GlobalStream {
    return this.globalArgs({ y: true });
  }

  compile(autoFix: boolean = true): string[] {
    if (!_compileFactories.compileAsList) {
      throw new Error("Compile factories not initialized. Import compileCli.ts first.");
    }
    return _compileFactories.compileAsList(this, autoFix);
  }

  compileLine(autoFix: boolean = true): string {
    if (!_compileFactories.compile) {
      throw new Error("Compile factories not initialized. Import compileCli.ts first.");
    }
    return _compileFactories.compile(this, autoFix);
  }

  run(ffmpegBinary: string = "ffmpeg", autoFix: boolean = true): RunResult {
    return runSync(this.compile(autoFix), ffmpegBinary);
  }

  async runAsync(ffmpegBinary: string = "ffmpeg", autoFix: boolean = true): Promise<RunResult> {
    return runAwaitable(this.compile(autoFix), ffmpegBinary);
  }
}

/** A node representing global FFmpeg options. */
export class GlobalNode extends Node {
  declare readonly inputs: readonly OutputStream[];

  constructor(inputs: readonly OutputStream[], kwargs: Record<string, KwargsValue> = {}) {
    super(kwargs, inputs);
  }

  stream(): GlobalStream {
    return new GlobalStream(this);
  }
}

/** A stream representing global FFmpeg options with execution capabilities. */
export class GlobalStream extends Stream {
  declare readonly node: GlobalNode;

  constructor(node: GlobalNode) {
    super(node);
  }

  _globalNode(
    additionalStreams: OutputStream[] = [],
    kwargs: Record<string, KwargsValue> = {},
  ): GlobalNode {
    const combinedInputs = [...this.node.inputs, ...additionalStreams];
    const combinedKwargs = { ...this.node.kwargs, ...kwargs };
    return new GlobalNode(combinedInputs, combinedKwargs);
  }

  globalArgs(kwargs: Record<string, KwargsValue> = {}): GlobalStream {
    return this._globalNode([], kwargs).stream();
  }

  overwriteOutput(): GlobalStream {
    return this.globalArgs({ y: true });
  }

  compile(autoFix: boolean = true): string[] {
    if (!_compileFactories.compileAsList) {
      throw new Error("Compile factories not initialized. Import compileCli.ts first.");
    }
    return _compileFactories.compileAsList(this, autoFix);
  }

  compileLine(autoFix: boolean = true): string {
    if (!_compileFactories.compile) {
      throw new Error("Compile factories not initialized. Import compileCli.ts first.");
    }
    return _compileFactories.compile(this, autoFix);
  }

  run(ffmpegBinary: string = "ffmpeg", autoFix: boolean = true): RunResult {
    return runSync(this.compile(autoFix), ffmpegBinary);
  }

  async runAsync(ffmpegBinary: string = "ffmpeg", autoFix: boolean = true): Promise<RunResult> {
    return runAwaitable(this.compile(autoFix), ffmpegBinary);
  }
}

/** Merge multiple output streams into a single runnable stream. */
export function mergeOutputs(...streams: OutputStream[]): OutputStream | GlobalStream {
  if (streams.length === 1) return streams[0];
  return streams[0]._globalNode(streams.slice(1)).stream();
}

// ─── Initialize late-bound factories ────────────────────────────────────────

_nodeFactories.createFilterNode = (name, inputs, kwargs, inputTypings, outputTypings) =>
  new FilterNode(name, inputs, kwargs, inputTypings, outputTypings);

_nodeFactories.createOutputNode = (inputs, filename, kwargs) =>
  new OutputNode(inputs, filename, kwargs);
