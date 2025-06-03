"""
typed-ffmpeg: A strongly-typed FFmpeg binding for Python.

This module provides a high-level, type-safe interface to FFmpeg, enabling
Python developers to process audio and video with compile-time validation.
The library uses Python's type annotations to ensure correct filter graphs
and parameter usage.

Key components:
- Input/output handling via `input` and `output` functions
- Stream manipulation with `VideoStream`, `AudioStream`, and `AVStream` classes
- Filter application through the `filters` module
- Media information analysis using `probe` function
- Codec and encoder detection with `get_codecs`, `get_decoders`, and `get_encoders`

Example:
    ```python
    import ffmpeg

    # Simple video transcoding
    (ffmpeg.input("input.mp4").output("output.mp4").run())
    ```
"""

from . import compile, dag, filters, sources
from .base import afilter, filter_multi_output, input, merge_outputs, output, vfilter
from .dag import Stream
from .exceptions import FFMpegExecuteError, FFMpegTypeError, FFMpegValueError
from .ffprobe.probe import probe, probe_obj
from .info import get_codecs, get_decoders, get_encoders
from .streams import AudioStream, AVStream, VideoStream

__all__ = [
    "sources",
    "filters",
    "input",
    "output",
    "merge_outputs",
    "FFMpegExecuteError",
    "FFMpegTypeError",
    "FFMpegValueError",
    "Stream",
    "probe",
    "probe_obj",
    "compile",
    "AudioStream",
    "VideoStream",
    "AVStream",
    "vfilter",
    "afilter",
    "filter_multi_output",
    "dag",
    "get_codecs",
    "get_decoders",
    "get_encoders",
]
