"""
typed-ffmpeg v8: FFmpeg 8.x type-safe Python bindings.

This package provides comprehensive type hints and IDE autocomplete for FFmpeg 8.x.
"""

__version__ = "1.0.0a1"

# Export main API functions and classes
from .dag.io import input, output
from .base import merge_outputs
from ffmpeg_core.ffprobe.probe import probe, probe_obj

# Make commonly used modules easily accessible
from . import filters, streams, codecs, formats

__all__ = [
    "__version__",
    "input",
    "output",
    "merge_outputs",
    "probe",
    "probe_obj",
    "filters",
    "streams",
    "codecs",
    "formats",
    "ffprobe",
]

# Dynamically add OutputArgs methods to FilterableStream
# This must be done after all imports to avoid circular dependencies
from .dag.base_streams import _add_output_args_methods

_add_output_args_methods()
del _add_output_args_methods
