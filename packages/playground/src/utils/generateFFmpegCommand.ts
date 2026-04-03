/**
 * FFmpeg command generation using @typed-ffmpeg/core (no Python/Pyodide).
 */

import {
  compile,
  parse as coreParse,
  StreamType as CoreStreamType,
  type FFMpegFilter as CoreFFMpegFilter,
  type FFMpegOption as CoreFFMpegOption,
  type Stream as CoreStream,
} from '@typed-ffmpeg/core';
import {
  FilterNode as CoreFilterNode,
  InputNode as CoreInputNode,
  OutputNode as CoreOutputNode,
  GlobalNode as CoreGlobalNode,
  VideoStream as CoreVideoStream,
  AudioStream as CoreAudioStream,
  AVStream as CoreAVStream,
  OutputStream as CoreOutputStream,
  GlobalStream as CoreGlobalStream,
} from '@typed-ffmpeg/core';
import type { Node as CoreNode } from '@typed-ffmpeg/core';

import { predefinedFilters } from '../types/ffmpeg';
import optionsData from '../config/options.json';

import {
  GlobalStream,
  GlobalNode,
  OutputNode,
  InputNode,
  FilterNode,
  VideoStream,
  AudioStream,
  AVStream,
  OutputStream,
  StreamType,
  type FilterableStream,
} from '../types/dag';
import { dumps } from './serialize';
import { NodeMappingManager } from './nodeMapping';
import { convertToCoreDAG } from './dagConverter';

export interface CommandResult {
  result: string;
  error: string | null;
}

/**
 * Generate the FFmpeg CLI command string from the current node graph.
 */
export async function generateFFmpegCommand(
  manager: NodeMappingManager,
): Promise<CommandResult> {
  try {
    const coreStream = convertToCoreDAG(manager.getGlobalNode());
    const line = compile(coreStream, true);
    return { result: line, error: null };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    return { result: `# Error: ${msg}`, error: msg };
  }
}

/**
 * Stub: Python code generation is no longer supported.
 * Kept for API compatibility; always returns an error.
 */
export async function generateFFmpegPythonCode(
  _manager: NodeMappingManager,
): Promise<CommandResult> {
  return {
    result: '# Python code generation is not available in the TypeScript version.',
    error: null,
  };
}

// ─── Parse helpers ────────────────────────────────────────────────────────────

/** Map of filter name → CoreFFMpegFilter, built once at module load. */
const filterMap: Map<string, CoreFFMpegFilter> = (() => {
  const result = new Map<string, CoreFFMpegFilter>();
  for (const f of predefinedFilters) {
    result.set(f.name, {
      name: f.name,
      description: f.description ?? '',
      isDynamicInput: f.is_dynamic_input,
      isDynamicOutput: f.is_dynamic_output,
      streamTypingsInput: f.stream_typings_input.map(t => ({
        type: (t.type as { value: string }).value === 'audio'
          ? CoreStreamType.Audio
          : CoreStreamType.Video,
      })),
      streamTypingsOutput: f.stream_typings_output.map(t => ({
        type: (t.type as { value: string }).value === 'audio'
          ? CoreStreamType.Audio
          : CoreStreamType.Video,
      })),
      formulaTypingsInput: f.formula_typings_input ?? null,
      formulaTypingsOutput: f.formula_typings_output ?? null,
      pre: [],
      options: f.options.map(o => ({
        name: o.name,
        alias: o.alias,
        description: o.description ?? '',
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        type: (o.type as any).value ?? o.type,
        required: o.required,
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        choices: o.choices as any[],
        default: o.default ?? null,
      })),
      isSupportSliceThreading: null,
      isSupportTimeline: null,
      isSupportFramesync: null,
      isSupportCommand: null,
      isFilterSink: null,
      isFilterSource: null,
    });
  }
  return result;
})();

/** Map of option name → CoreFFMpegOption, built once at module load. */
const optionMap: Map<string, CoreFFMpegOption> = new Map(
  (optionsData as CoreFFMpegOption[]).map(o => [o.name, o]),
);

/**
 * Convert a ts-core Stream DAG to the playground's serialized JSON format.
 * The result is compatible with NodeMappingManager.fromJson().
 */
function coreStreamToPlaygroundJson(coreStream: CoreStream): string {
  const nodeCache = new Map<CoreNode, InputNode | FilterNode | OutputNode | GlobalNode>();

  function convertNode(n: CoreNode): InputNode | FilterNode | OutputNode | GlobalNode {
    const cached = nodeCache.get(n);
    if (cached) return cached;

    let pg: InputNode | FilterNode | OutputNode | GlobalNode;

    if (n instanceof CoreInputNode) {
      pg = new InputNode(n.filename, [], n.kwargs as Record<string, string | number | boolean>);

    } else if (n instanceof CoreFilterNode) {
      const pgInputs = n.inputs.map(s => convertFilterableStream(s));
      const pgInTypings = n.inputTypings.map(
        t => new StreamType(t === CoreStreamType.Audio ? 'audio' : 'video'),
      );
      const pgOutTypings = n.outputTypings.map(
        t => new StreamType(t === CoreStreamType.Audio ? 'audio' : 'video'),
      );
      pg = new FilterNode(
        n.name,
        pgInputs,
        pgInTypings,
        pgOutTypings,
        n.kwargs as Record<string, string | number | boolean>,
      );

    } else if (n instanceof CoreOutputNode) {
      const pgInputs = n.inputs.map(s => convertFilterableStream(s));
      pg = new OutputNode(
        n.filename,
        pgInputs,
        n.kwargs as Record<string, string | number | boolean>,
      );

    } else if (n instanceof CoreGlobalNode) {
      const pgInputs = (n.inputs as CoreOutputStream[]).map(s => {
        const srcNode = convertNode(s.node) as OutputNode;
        return new OutputStream(srcNode, null);
      });
      pg = new GlobalNode(pgInputs, n.kwargs as Record<string, string | number | boolean>);

    } else {
      throw new Error(`Unknown core node type: ${n.constructor.name}`);
    }

    nodeCache.set(n, pg);
    return pg;
  }

  function convertFilterableStream(s: CoreStream): FilterableStream {
    const pgNode = convertNode(s.node) as InputNode | FilterNode;
    const idx = s.index ?? null;
    if (s instanceof CoreVideoStream) return new VideoStream(pgNode, idx);
    if (s instanceof CoreAudioStream) return new AudioStream(pgNode, idx);
    if (s instanceof CoreAVStream) return new AVStream(pgNode, idx);
    return new VideoStream(pgNode, idx); // fallback
  }

  // Wrap in GlobalNode/GlobalStream if needed
  let globalNode: GlobalNode;
  if (coreStream instanceof CoreGlobalStream) {
    globalNode = convertNode(coreStream.node) as GlobalNode;
  } else if (coreStream instanceof CoreOutputStream) {
    const outputNode = convertNode(coreStream.node) as OutputNode;
    globalNode = new GlobalNode([new OutputStream(outputNode, null)], {});
  } else {
    throw new Error(`Cannot convert stream type: ${coreStream.constructor.name}`);
  }

  return dumps(new GlobalStream(globalNode, null, 'final'));
}

/**
 * Parse an FFmpeg CLI command string and return the playground graph as JSON.
 * The JSON is compatible with NodeMappingManager.fromJson().
 */
export async function parseFFmpegCommandToJson(
  cmd: string,
): Promise<CommandResult> {
  try {
    const coreStream = coreParse(cmd, filterMap, optionMap);
    const json = coreStreamToPlaygroundJson(coreStream);
    return { result: json, error: null };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    return { result: '', error: msg };
  }
}
