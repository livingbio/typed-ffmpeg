"""
Compile module has been moved to version-specific packages.

This module depends on DAG structures which are version-specific.
Import from ffmpeg.compile instead.
"""
raise ImportError(
    "ffmpeg_core.compile has been moved to version packages. "
    "Use: from ffmpeg.compile import ..."
)
