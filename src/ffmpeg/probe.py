import json
import subprocess
from typing import Any

from .exeptions import Error
from .utils.escaping import convert_kwargs_to_cmd_line_args


def probe(filename: str, cmd: str = "ffprobe", timeout: int | None = None, **kwargs: Any) -> dict[str, Any]:
    """
    Run ffprobe on the given file and return a JSON representation of the output

    Parameters:
    -----------
    :param str filename: the path to the file to probe
    :param str cmd: the ffprobe command to run
    :param int|None timeout: the timeout for the command
    :param Any kwargs: the arguments for the ffprobe command

    Returns:
    --------
    :return: the JSON representation of the ffprobe output
    """
    args = [cmd, "-show_format", "-show_streams", "-of", "json"]
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args += [filename]

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if timeout is not None:
        out, err = p.communicate(timeout=timeout)
    else:
        out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise Error(retcode=retcode, cmd=args, stdout=out, stderr=err)

    return json.loads(out.decode("utf-8"))
