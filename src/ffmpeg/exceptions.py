class Error(Exception):
    """
    FFmpeg error
    """

    def __init__(self, retcode: int | None, cmd: str, stdout: bytes, stderr: bytes):
        super(Error, self).__init__(f"{cmd} error (see stderr output for detail)")

        self.stdout = stdout
        self.stderr = stderr
        self.cmd = cmd
        self.retcode = retcode
