import json
import logging
import subprocess
from pathlib import Path
from typing import Any

from .exceptions import FFMpegExecuteError
from .utils.escaping import convert_kwargs_to_cmd_line_args
from .utils.run import command_line

logger = logging.getLogger(__name__)


def probe(
    filename: str | Path,
    cmd: str = "ffprobe",
    timeout: int | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """
    Run ffprobe on the given file and return a JSON representation of the output

    Args:
        filename: The path to the file to probe.
        cmd: The ffprobe command to run. Defaults to "ffprobe".
        timeout: The timeout for the command. Defaults to None.
        **kwargs: The arguments for the ffprobe command.

    Returns:
        The JSON representation of the ffprobe output.
    """
    args = [cmd, "-show_format", "-show_streams", "-of", "json"]
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args += [str(filename)]

    logger.info("Running ffprobe command: %s", command_line(args))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if timeout is not None:
        out, err = p.communicate(timeout=timeout)
    else:
        out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise FFMpegExecuteError(
            retcode=retcode, cmd=command_line(args), stdout=out, stderr=err
        )

    return json.loads(out.decode("utf-8"))
