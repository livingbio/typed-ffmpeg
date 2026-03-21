"""
typed-ffmpeg v6: FFmpeg 6.x type-safe Python bindings.

This package provides comprehensive type hints and IDE autocomplete for FFmpeg 6.x.
"""

__version__ = "6.1.0"

# Export main API functions and classes
from ffmpeg_core.dag.io import input, output, merge_outputs
from ffmpeg_core.ffprobe import probe

# Make commonly used modules easily accessible
from . import filters, streams, codecs, formats

__all__ = [
    "__version__",
    "input",
    "output",
    "merge_outputs",
    "probe",
    "filters",
    "streams",
    "codecs",
    "formats",
]
