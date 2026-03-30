/**
 * Converts the playground's mutable DAG representation to the immutable
 * @typed-ffmpeg/core DAG, so it can be compiled to an FFmpeg CLI command.
 */

import {
  AudioStream as CoreAudioStream,
  AVStream as CoreAVStream,
  FilterNode as CoreFilterNode,
  GlobalNode as CoreGlobalNode,
  GlobalStream as CoreGlobalStream,
  InputNode as CoreInputNode,
  OutputStream as CoreOutputStream,
  OutputNode as CoreOutputNode,
  StreamType as CoreStreamType,
  VideoStream as CoreVideoStream,
} from '@typed-ffmpeg/core';

import type { FilterableStream as CoreFilterableStream } from '@typed-ffmpeg/core';

import {
  AudioStream,
  FilterNode,
  GlobalNode,
  InputNode,
  OutputStream,
  OutputNode,
  VideoStream,
  type StreamTypeEnum,
} from '../types/dag';

import type { Node, Stream } from '../types/dag';

// ─── Internal helpers ──────────────────────────────────────────────────────

function toCoreStreamType(value: StreamTypeEnum): CoreStreamType {
  if (value === 'audio') return CoreStreamType.Audio;
  return CoreStreamType.Video; // 'video' or 'av' default to Video
}

/**
 * Given a playground stream and the already-converted core source node,
 * create the appropriate @typed-ffmpeg/core stream instance.
 *
 * When the source is an InputNode and the stream is AVStream, the returned
 * type is inferred from `targetTyping` (the filter's expected input type).
 */
function toCoreStream(
  stream: Stream,
  coreNode: CoreInputNode | CoreFilterNode | CoreOutputNode,
  targetTyping?: StreamTypeEnum,
): CoreFilterableStream {
  if (stream instanceof VideoStream) {
    return new CoreVideoStream(
      coreNode as CoreFilterNode,
      stream.index !== undefined ? stream.index : null,
    );
  }
  if (stream instanceof AudioStream) {
    return new CoreAudioStream(
      coreNode as CoreFilterNode,
      stream.index !== undefined ? stream.index : null,
    );
  }
  // AVStream comes from InputNode outputs.
  // Determine the concrete stream type from the target filter's input typing.
  if (targetTyping === 'audio') {
    return new CoreAudioStream(coreNode as CoreInputNode);
  }
  if (targetTyping === 'video') {
    return new CoreVideoStream(coreNode as CoreInputNode);
  }
  return new CoreAVStream(coreNode as CoreInputNode);
}

// ─── Main converter ────────────────────────────────────────────────────────

/**
 * Walk the playground's mutable GlobalNode and produce an equivalent
 * @typed-ffmpeg/core GlobalStream that can be passed to `compile()`.
 *
 * Null (disconnected) inputs are skipped; the resulting core nodes only
 * contain the streams that are actually connected in the UI.
 */
export function convertToCoreDAG(globalNode: GlobalNode): CoreGlobalStream {
  // Memoize converted nodes to handle shared references correctly.
  const memo = new Map<Node, CoreInputNode | CoreFilterNode | CoreOutputNode | CoreGlobalNode>();

  function convertNode(node: Node): CoreInputNode | CoreFilterNode | CoreOutputNode | CoreGlobalNode {
    const cached = memo.get(node);
    if (cached) return cached;

    let coreNode: CoreInputNode | CoreFilterNode | CoreOutputNode | CoreGlobalNode;

    if (node instanceof InputNode) {
      coreNode = new CoreInputNode(node.filename, node.kwargs);

    } else if (node instanceof FilterNode) {
      const coreInputs: CoreFilterableStream[] = [];
      const coreInputTypings: CoreStreamType[] = [];

      for (let i = 0; i < node.inputs.length; i++) {
        const stream = node.inputs[i];
        if (stream === null) continue;

        const typing = node.input_typings[i]?.value ?? 'video';
        const srcCoreNode = convertNode(stream.node) as CoreInputNode | CoreFilterNode;
        coreInputs.push(toCoreStream(stream, srcCoreNode, typing));
        coreInputTypings.push(toCoreStreamType(typing));
      }

      const coreOutputTypings = node.output_typings.map((t) =>
        toCoreStreamType(t.value),
      );

      coreNode = new CoreFilterNode(
        node.name,
        coreInputs,
        node.kwargs,
        coreInputTypings,
        coreOutputTypings,
      );

    } else if (node instanceof OutputNode) {
      const coreInputs = node.inputs
        .filter((s): s is NonNullable<typeof s> => s !== null)
        .map((stream) => {
          const srcCoreNode = convertNode(stream.node) as CoreInputNode | CoreFilterNode;
          return toCoreStream(stream, srcCoreNode);
        });

      coreNode = new CoreOutputNode(coreInputs, node.filename, node.kwargs);

    } else if (node instanceof GlobalNode) {
      const coreInputs: CoreOutputStream[] = [];

      for (const stream of node.inputs) {
        if (stream === null) continue;
        if (!(stream instanceof OutputStream)) continue;
        const srcCoreNode = convertNode(stream.node) as CoreOutputNode;
        coreInputs.push(new CoreOutputStream(srcCoreNode));
      }

      coreNode = new CoreGlobalNode(coreInputs, node.kwargs);

    } else {
      throw new Error(`Unknown node type: ${node.constructor.name}`);
    }

    memo.set(node, coreNode);
    return coreNode;
  }

  const coreGlobal = convertNode(globalNode) as CoreGlobalNode;
  return new CoreGlobalStream(coreGlobal);
}
