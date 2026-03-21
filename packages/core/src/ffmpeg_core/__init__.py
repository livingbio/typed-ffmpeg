"""
ffmpeg-core: Core runtime for typed-ffmpeg.

This package contains the hand-written runtime code that is shared across
all FFmpeg version bindings. It includes:

- DAG layer: Filter graph representation
- Compile layer: FFmpeg command generation
- IR layer: Intermediate representation for multi-backend support
- Common utilities: Serialization, schemas, etc.
"""

__version__ = "1.0.0"

# Export commonly used classes
from .dag import (
    FilterNode,
    FilterableStream,
    GlobalNode,
    InputNode,
    OutputStream,
    OutputNode,
    Stream,
)
from .exceptions import FFMpegExecuteError, FFMpegTypeError, FFMpegValueError

__all__ = [
    "__version__",
    "FilterNode",
    "FilterableStream",
    "GlobalNode",
    "InputNode",
    "OutputStream",
    "OutputNode",
    "Stream",
    "FFMpegExecuteError",
    "FFMpegTypeError",
    "FFMpegValueError",
]
