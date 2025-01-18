class FFMpegError(Exception):
    """
    Base exception for all ffmpeg errors.
    """

    ...


class FFMpegTypeError(FFMpegError, TypeError):
    """
    Base exception for all ffmpeg type errors.
    """


class FFMpegValueError(FFMpegError, ValueError):
    """
    Base exception for all ffmpeg value errors.
    """


class FFMpegExecuteError(FFMpegError):
    """
    FFmpeg error
    """

    def __init__(self, retcode: int | None, cmd: str, stdout: bytes, stderr: bytes):
        """
        Initialize the exception.

        Args:
            retcode: The return code of the command.
            cmd: The command that was run.
            stdout: The stdout of the command.
            stderr: The stderr of the command.
        """

        self.stdout = stdout
        self.stderr = stderr
        self.cmd = cmd
        self.retcode = retcode

        super().__init__(f"{cmd} error (see stderr output for detail) {stderr!r}")
