class Error(Exception):
    """
    FFmpeg error
    """

    def __init__(self, retcode: int | None, cmd: str, stdout: bytes, stderr: bytes):

        self.stdout = stdout
        self.stderr = stderr
        self.cmd = cmd
        self.retcode = retcode

        super(Error, self).__init__(f"{cmd} error (see stderr output for detail) {stderr!r}")
