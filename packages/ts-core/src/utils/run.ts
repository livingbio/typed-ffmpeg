/**
 * Utilities for executing FFmpeg commands.
 */

import { execFileSync, spawn, type ChildProcess } from "child_process";

export interface RunResult {
  stdout: Buffer;
  stderr: Buffer;
}

/**
 * Run an FFmpeg command synchronously.
 *
 * @param args - Command-line arguments (without the "ffmpeg" binary name)
 * @param ffmpegBinary - Path to the ffmpeg binary (default: "ffmpeg")
 * @returns stdout and stderr buffers
 * @throws Error if the command fails
 */
export function run(args: string[], ffmpegBinary: string = "ffmpeg"): RunResult {
  try {
    const stdout = execFileSync(ffmpegBinary, args, {
      maxBuffer: 1024 * 1024 * 100,
    });
    return { stdout, stderr: Buffer.alloc(0) };
  } catch (error: unknown) {
    const err = error as { stdout?: Buffer; stderr?: Buffer; status?: number };
    throw new FFMpegExecuteError(
      err.status ?? null,
      `${ffmpegBinary} ${args.join(" ")}`,
      err.stdout ?? Buffer.alloc(0),
      err.stderr ?? Buffer.alloc(0),
    );
  }
}

/**
 * Run an FFmpeg command asynchronously.
 *
 * @param args - Command-line arguments (without the "ffmpeg" binary name)
 * @param ffmpegBinary - Path to the ffmpeg binary (default: "ffmpeg")
 * @returns A ChildProcess handle
 */
export function runAsync(args: string[], ffmpegBinary: string = "ffmpeg"): ChildProcess {
  return spawn(ffmpegBinary, args);
}

/**
 * Run an FFmpeg command and return a promise.
 *
 * @param args - Command-line arguments (without the "ffmpeg" binary name)
 * @param ffmpegBinary - Path to the ffmpeg binary (default: "ffmpeg")
 * @returns A promise that resolves with stdout and stderr
 */
export function runAwaitable(
  args: string[],
  ffmpegBinary: string = "ffmpeg",
): Promise<RunResult> {
  return new Promise((resolve, reject) => {
    const proc = spawn(ffmpegBinary, args);
    const stdoutChunks: Buffer[] = [];
    const stderrChunks: Buffer[] = [];

    proc.stdout?.on("data", (chunk: Buffer) => stdoutChunks.push(chunk));
    proc.stderr?.on("data", (chunk: Buffer) => stderrChunks.push(chunk));

    proc.on("close", (code) => {
      const stdout = Buffer.concat(stdoutChunks);
      const stderr = Buffer.concat(stderrChunks);
      if (code === 0) {
        resolve({ stdout, stderr });
      } else {
        reject(
          new FFMpegExecuteError(
            code,
            `${ffmpegBinary} ${args.join(" ")}`,
            stdout,
            stderr,
          ),
        );
      }
    });

    proc.on("error", (err) => reject(err));
  });
}

import { FFMpegExecuteError } from "../exceptions.js";

/**
 * Join command-line arguments into a shell-safe command string.
 */
export function commandLine(args: string[]): string {
  return args
    .map((arg) => {
      if (/[^a-zA-Z0-9_\-/.=:]/.test(arg)) {
        return `'${arg.replace(/'/g, "'\\''")}'`;
      }
      return arg;
    })
    .join(" ");
}
