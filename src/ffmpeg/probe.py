import json
import subprocess
from typing import Any

from .utils.escaping import convert_kwargs_to_cmd_line_args


def probe(filename: str, cmd: str = "ffprobe", timeout: int | None = None, **kwargs: Any) -> dict[str, Any]:
    """Run ffprobe on the specified file and return a JSON representation of the output.

    Raises:
        :class:`ffmpeg.Error`: if ffprobe returns a non-zero exit code,
            an :class:`Error` is returned with a generic error message.
            The stderr output can be retrieved by accessing the
            ``stderr`` property of the exception.
    """
    args = [cmd, "-show_format", "-show_streams", "-of", "json"]
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args += [filename]

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if timeout is not None:
        out, err = p.communicate(timeout=timeout)
    else:
        out, err = p.communicate()

    if p.returncode != 0:
        raise subprocess.SubprocessError("ffprobe", out, err)
    return json.loads(out.decode("utf-8"))


__all__ = ["probe"]
