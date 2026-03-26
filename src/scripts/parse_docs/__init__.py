"""
FFmpeg Documentation Parsing Package.

This package contains modules for parsing FFmpeg filter documentation
from version-correct Texinfo (.texi) source files included in FFmpeg
source tarballs.

The primary path uses parse_texi to extract filter descriptions and
parameter documentation from doc/filters.texi. A legacy HTML download
path from ffmpeg.org is retained as a fallback.
"""

from . import cli, parse_texi, schema

__all__ = ["cli", "parse_texi", "schema"]
