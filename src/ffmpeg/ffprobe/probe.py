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

from ..exceptions import FFMpegExecuteError
from ..utils.escaping import convert_kwargs_to_cmd_line_args
from ..utils.run import command_line
from .parse import parse_ffprobe
from .schema import ffprobeType

logger = logging.getLogger(__name__)


def _probe(
    filename: str | Path,
    *,
    show_program_version: bool = False,
    show_library_versions: bool = False,
    show_pixel_formats: bool = False,
    show_packets: bool = False,
    show_frames: bool = False,
    show_programs: bool = False,
    show_streams: bool = True,
    show_chapters: bool = False,
    show_format: bool = True,
    show_error: bool = False,
    cmd: str = "ffprobe",
    timeout: int | None = None,
    format: str = "json",
    **kwargs: Any,
) -> str:
    """
    Analyze a media file using ffprobe and return its metadata as a dictionary.

    This function executes ffprobe to extract detailed information about a media file,
    including format metadata (container format, duration, bitrate) and stream information
    (codecs, resolution, sample rate, etc). The result is returned as a Python dictionary
    parsed from ffprobe's JSON output.

    Args:
        filename: Path to the media file to analyze
        cmd: Path or name of the ffprobe executable
        timeout: Maximum time in seconds to wait for ffprobe to complete (default: None, wait indefinitely)
        show_program_version: Show the program version
        show_library_versions: Show the library versions
        show_pixel_formats: Show the pixel formats
        show_packets: Show the packets. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_frames: Show the frames. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_programs: Show the programs
        show_streams: Show the streams
        show_chapters: Show the chapters
        show_format: Show the format
        show_error: Show the error
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
    args = [
        cmd,
        *(["-show_program_version"] if show_program_version else []),
        *(["-show_library_versions"] if show_library_versions else []),
        *(["-show_pixel_formats"] if show_pixel_formats else []),
        *(["-show_packets"] if show_packets else []),
        *(["-show_frames"] if show_frames else []),
        *(["-show_programs"] if show_programs else []),
        *(["-show_streams"] if show_streams else []),
        *(["-show_chapters"] if show_chapters else []),
        *(["-show_format"] if show_format else []),
        *(["-show_error"] if show_error else []),
        "-of",
        format,
    ]
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

    return out.decode("utf-8")


def probe(
    filename: str | Path,
    *,
    show_program_version: bool = False,
    show_library_versions: bool = False,
    show_pixel_formats: bool = False,
    show_packets: bool = False,
    show_frames: bool = False,
    show_programs: bool = False,
    show_streams: bool = True,
    show_chapters: bool = False,
    show_format: bool = True,
    show_error: bool = False,
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
        cmd: Path or name of the ffprobe executable
        timeout: Maximum time in seconds to wait for ffprobe to complete (default: None, wait indefinitely)
        show_program_version: Show the program version
        show_library_versions: Show the library versions
        show_pixel_formats: Show the pixel formats
        show_packets: Show the packets. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_frames: Show the frames. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_programs: Show the programs
        show_streams: Show the streams
        show_chapters: Show the chapters
        show_format: Show the format
        show_error: Show the error
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
    return json.loads(
        _probe(
            filename,
            show_program_version=show_program_version,
            show_library_versions=show_library_versions,
            show_pixel_formats=show_pixel_formats,
            show_packets=show_packets,
            show_frames=show_frames,
            show_programs=show_programs,
            show_streams=show_streams,
            show_chapters=show_chapters,
            show_format=show_format,
            show_error=show_error,
            cmd=cmd,
            timeout=timeout,
            **kwargs,
        )
    )


def probe_obj(
    filename: str | Path,
    *,
    show_program_version: bool = False,
    show_library_versions: bool = False,
    show_pixel_formats: bool = False,
    show_packets: bool = False,
    show_frames: bool = False,
    show_programs: bool = False,
    show_streams: bool = True,
    show_chapters: bool = False,
    show_format: bool = True,
    show_error: bool = False,
    cmd: str = "ffprobe",
    timeout: int | None = None,
    **kwargs: Any,
) -> ffprobeType | None:
    """
    Analyze a media file using ffprobe and return its metadata as a dataclass.

    This function executes ffprobe to extract detailed information about a media file,
    including format metadata (container format, duration, bitrate) and stream information
    (codecs, resolution, sample rate, etc). The result is returned as a Python dataclass
    parsed from ffprobe's output.

    Args:
        filename: Path to the media file to analyze
        cmd: Path or name of the ffprobe executable
        timeout: Maximum time in seconds to wait for ffprobe to complete (default: None, wait indefinitely)
        show_program_version: Show the program version
        show_library_versions: Show the library versions
        show_pixel_formats: Show the pixel formats
        show_packets: Show the packets. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_frames: Show the frames. Note: When both show_packets and show_frames are True,
            ffprobe will output a combined "packets_and_frames" section instead of separate sections.
        show_programs: Show the programs
        show_streams: Show the streams
        show_chapters: Show the chapters
        show_format: Show the format
        show_error: Show the error
        **kwargs: Additional arguments to pass to ffprobe as command line parameters
            (e.g., loglevel="quiet", skip_frame="nokey")

    Returns:
        A dataclass containing the parsed ffprobe output

    Raises:
        FFMpegExecuteError: If ffprobe returns a non-zero exit code
        subprocess.TimeoutExpired: If the timeout is reached before ffprobe completes

    Example:
        ```python
        info = probe_obj("video.mp4")
        print(f"Duration: {float(info.format.duration):.2f} seconds")
        print(f"Streams: {len(info.streams)}")
        ```
    """

    xml = _probe(
        filename,
        show_program_version=show_program_version,
        show_library_versions=show_library_versions,
        show_pixel_formats=show_pixel_formats,
        show_packets=show_packets,
        show_frames=show_frames,
        show_programs=show_programs,
        show_streams=show_streams,
        show_chapters=show_chapters,
        show_format=show_format,
        show_error=show_error,
        cmd=cmd,
        timeout=timeout,
        format="xml",
        **kwargs,
    )
    return parse_ffprobe(xml)
