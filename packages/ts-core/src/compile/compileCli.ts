/**
 * Compiles FFmpeg filter graphs into command-line arguments.
 */

import { StreamType } from "../common/schema.js";
import { FilterableStream } from "../dag/baseStreams.js";
import {
  AudioStream,
  AVStream,
  FilterNode,
  GlobalNode,
  InputNode,
  OutputNode,
  OutputStream,
  SubtitleStream,
  VideoStream,
} from "../dag/nodes.js";
import { Node, Stream } from "../dag/schema.js";
import { FFMpegValueError } from "../exceptions.js";
import { escape } from "../utils/escaping.js";
import { isDefault } from "../utils/types.js";
import { commandLine } from "../utils/run.js";
import { DAGContext } from "./context.js";
import { validate } from "./validate.js";

/**
 * Compile a stream into a command-line string.
 */
export function compile(
  stream: Stream,
  autoFix: boolean = true,
): string {
  return "ffmpeg " + commandLine(compileAsList(stream, autoFix));
}

/**
 * Compile a stream into a list of FFmpeg command-line arguments.
 */
export function compileAsList(
  stream: Stream,
  autoFix: boolean = true,
): string[] {
  stream = validate(stream, autoFix);
  const node = stream.node;
  const context = DAGContext.build(node);

  const commands: string[] = [];

  // Global nodes
  for (const n of context.allNodes) {
    if (n instanceof GlobalNode) {
      commands.push(...getArgsGlobalNode(n, context));
    }
  }

  // Input nodes
  for (const n of context.allNodes) {
    if (n instanceof InputNode) {
      commands.push(...getArgsInputNode(n, context));
    }
  }

  // Filter nodes
  const filterNodes = context.allNodes.filter(
    (n): n is FilterNode => n instanceof FilterNode,
  );
  const sortedFilters = [...filterNodes].sort(
    (a, b) => a.upstreamNodes.size - b.upstreamNodes.size,
  );

  const vfCommands: string[] = [];
  for (const n of sortedFilters) {
    vfCommands.push(getArgsFilterNode(n, context).join(""));
  }

  if (vfCommands.length > 0) {
    commands.push("-filter_complex", vfCommands.join(";"));
  }

  // Output nodes
  for (const n of context.allNodes) {
    if (n instanceof OutputNode) {
      commands.push(...getArgsOutputNode(n, context));
    }
  }

  return commands;
}

/**
 * Generate the FFmpeg label for a stream.
 */
export function getStreamLabel(stream: Stream, context?: DAGContext): string {
  if (!context) context = DAGContext.build(stream.node);

  if (stream.node instanceof InputNode) {
    const label = getNodeLabel(stream.node, context);
    if (stream instanceof AVStream) return label;
    if (stream instanceof VideoStream) {
      return stream.index != null ? `${label}:v:${stream.index}` : `${label}:v`;
    }
    if (stream instanceof AudioStream) {
      return stream.index != null ? `${label}:a:${stream.index}` : `${label}:a`;
    }
    if (stream instanceof SubtitleStream) {
      return stream.index != null ? `${label}:s:${stream.index}` : `${label}:s`;
    }
    throw new FFMpegValueError(`Unknown stream type: ${stream.constructor.name}`);
  }

  if (stream.node instanceof FilterNode) {
    const label = getNodeLabel(stream.node, context);
    if (stream.node.outputTypings.length > 1) {
      return `${label}#${stream.index}`;
    }
    return label;
  }

  if (stream.node instanceof OutputNode) {
    return getNodeLabel(stream.node, context);
  }

  throw new FFMpegValueError(`Unknown node type: ${stream.node.constructor.name}`);
}

/**
 * Generate the filter string for a FilterNode.
 */
export function getArgsFilterNode(node: FilterNode, context: DAGContext): string[] {
  const incomingLabels = node.inputs
    .map((k) => `[${getStreamLabel(k, context)}]`)
    .join("");

  const outputs = context.getOutgoingStreams(node);
  const sortedOutputs = [...outputs].sort(
    (a, b) => (a.index ?? 0) - (b.index ?? 0),
  );
  const outgoingLabels = sortedOutputs
    .map((s) => `[${getStreamLabel(s, context)}]`)
    .join("");

  const commands: string[] = [];
  for (const [key, value] of Object.entries(node.kwargs)) {
    if (isDefault(value)) continue;
    const v = typeof value === "boolean" ? String(Number(value)) : value;
    commands.push(`${key}=${escape(v)}`);
  }

  if (commands.length > 0) {
    return [
      incomingLabels,
      `${node.name}=`,
      escape(commands.join(":"), "\\\\'[],;"),
      outgoingLabels,
    ];
  }
  return [incomingLabels, node.name, outgoingLabels];
}

/**
 * Generate CLI args for an InputNode.
 */
export function getArgsInputNode(node: InputNode, _context: DAGContext): string[] {
  const commands: string[] = [];
  for (const [key, value] of Object.entries(node.kwargs)) {
    if (typeof value === "boolean") {
      commands.push(value ? `-${key}` : `-no${key}`);
    } else {
      commands.push(`-${key}`, String(value));
    }
  }
  commands.push("-i", node.filename);
  return commands;
}

/**
 * Generate CLI args for an OutputNode.
 */
export function getArgsOutputNode(node: OutputNode, context: DAGContext): string[] {
  const commands: string[] = [];

  // Handle stream mapping
  for (const input of node.inputs) {
    if (input.node instanceof InputNode) {
      // Special case: single input, single output, unmapped AVStream
      if (
        input.index == null &&
        input instanceof AVStream &&
        context.allNodes.filter((n) => n instanceof InputNode).length === 1 &&
        context.allNodes.filter((n) => n instanceof OutputNode).length === 1 &&
        node.inputs.length === 1
      ) {
        continue;
      }
      if (input.optional) {
        commands.push("-map", `${getStreamLabel(input, context)}?`);
      } else {
        commands.push("-map", getStreamLabel(input, context));
      }
    } else {
      commands.push("-map", `[${getStreamLabel(input, context)}]`);
    }
  }

  for (const [key, value] of Object.entries(node.kwargs)) {
    if (typeof value === "boolean") {
      commands.push(value ? `-${key}` : `-no${key}`);
    } else {
      commands.push(`-${key}`, String(value));
    }
  }
  commands.push(node.filename);
  return commands;
}

/**
 * Generate CLI args for a GlobalNode.
 */
export function getArgsGlobalNode(node: GlobalNode, _context: DAGContext): string[] {
  const commands: string[] = [];
  for (const [key, value] of Object.entries(node.kwargs)) {
    if (typeof value === "boolean") {
      commands.push(value ? `-${key}` : `-no${key}`);
    } else {
      commands.push(`-${key}`, String(value));
    }
  }
  return commands;
}

/**
 * Get the label for a node.
 */
export function getNodeLabel(node: Node, context: DAGContext): string {
  const id = context.nodeIds.get(node) ?? 0;
  if (node instanceof InputNode) return String(id);
  if (node instanceof FilterNode) return `s${id}`;
  return "out";
}

/**
 * Dispatch to the appropriate getArgs function for a node.
 */
export function getArgs(node: Node, context?: DAGContext): string[] {
  if (!context) context = DAGContext.build(node);
  if (node instanceof FilterNode) return getArgsFilterNode(node, context);
  if (node instanceof InputNode) return getArgsInputNode(node, context);
  if (node instanceof OutputNode) return getArgsOutputNode(node, context);
  if (node instanceof GlobalNode) return getArgsGlobalNode(node, context);
  throw new FFMpegValueError(`Unknown node type: ${node.constructor.name}`);
}
