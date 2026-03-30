/**
 * FFmpeg command generation using @typed-ffmpeg/core (no Python/Pyodide).
 */

import { compile } from '@typed-ffmpeg/core';
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

/**
 * Stub: Parsing an FFmpeg CLI command back to a JSON graph is not yet
 * implemented in the TypeScript version.
 */
export async function parseFFmpegCommandToJson(
  _cmd: string,
): Promise<CommandResult> {
  return {
    result: '',
    error: 'Parsing an FFmpeg command to a graph is not yet supported.',
  };
}
