/**
 * Exception classes for handling FFmpeg-related errors.
 */

/** Base exception for all FFmpeg errors. */
export class FFMpegError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "FFMpegError";
  }
}

/** Exception raised for FFmpeg-related type errors. */
export class FFMpegTypeError extends FFMpegError {
  constructor(message: string) {
    super(message);
    this.name = "FFMpegTypeError";
  }
}

/** Exception raised for FFmpeg-related value errors. */
export class FFMpegValueError extends FFMpegError {
  constructor(message: string) {
    super(message);
    this.name = "FFMpegValueError";
  }
}

/** Exception raised when an FFmpeg command fails during execution. */
export class FFMpegExecuteError extends FFMpegError {
  readonly stdout: Buffer;
  readonly stderr: Buffer;
  readonly cmd: string;
  readonly retcode: number | null;

  constructor(retcode: number | null, cmd: string, stdout: Buffer, stderr: Buffer) {
    super(`${cmd} error (see stderr for detail) ${stderr.toString()}`);
    this.name = "FFMpegExecuteError";
    this.retcode = retcode;
    this.cmd = cmd;
    this.stdout = stdout;
    this.stderr = stderr;
  }
}
