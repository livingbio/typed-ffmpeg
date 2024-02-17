class Error(Exception):
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

        super(Error, self).__init__(f"{cmd} error (see stderr output for detail) {stderr!r}")
