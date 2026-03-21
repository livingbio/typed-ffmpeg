"""
typed-ffmpeg v7: FFmpeg 7.x type-safe Python bindings.

This package provides comprehensive type hints and IDE autocomplete for FFmpeg 7.x.
"""

__version__ = "7.1.0"

# Export main API functions and classes
from .dag.io import input, output
from .base import merge_outputs
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
