"""
FFmpeg Help Output Parsing Package.

This package contains modules for parsing the output of FFmpeg's help commands
to extract detailed information about filters and their options. The main functionality includes:

- Running FFmpeg with various help flags to get information about filters
- Parsing the help output to extract structured filter information
- Extracting option details, input/output stream types, and other metadata
- Building comprehensive data structures that represent FFmpeg filter capabilities

These modules provide the most detailed and accurate information about FFmpeg filters
by directly querying the FFmpeg binary, ensuring the generated type annotations
match the exact behavior of the installed FFmpeg version.
"""

from . import cli, schema

__all__ = ["cli", "schema"]
