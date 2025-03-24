"""
Module for analyzing media files with ffprobe.

This module provides functionality to extract detailed metadata from media files
using FFmpeg's ffprobe utility. It returns a structured representation of the
file's format, streams, and other relevant information.
"""

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
    Analyze a media file using ffprobe and return its metadata as a dictionary.

    This function executes ffprobe to extract detailed information about a media file,
    including format metadata (container format, duration, bitrate) and stream information
    (codecs, resolution, sample rate, etc). The result is returned as a Python dictionary
    parsed from ffprobe's JSON output.

    Args:
        filename: Path to the media file to analyze
        cmd: Path or name of the ffprobe executable (default: "ffprobe")
        timeout: Maximum time in seconds to wait for ffprobe to complete (default: None, wait indefinitely)
        **kwargs: Additional arguments to pass to ffprobe as command line parameters
            (e.g., loglevel="quiet", skip_frame="nokey")

    Returns:
        A dictionary containing the parsed JSON output from ffprobe with format and stream information

    Raises:
        FFMpegExecuteError: If ffprobe returns a non-zero exit code
        subprocess.TimeoutExpired: If the timeout is reached before ffprobe completes

    Example:
        ```python
        info = probe("video.mp4")
        print(f"Duration: {float(info['format']['duration']):.2f} seconds")
        print(f"Streams: {len(info['streams'])}")
        ```
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
