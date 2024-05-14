import shlex


def parse(cmd: str):
    arguments = shlex.split(cmd)

    assert arguments[0] == "ffmpeg"

    