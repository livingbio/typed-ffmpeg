"""
FFmpeg Metadata Extraction Package.

This package extracts structured metadata from FFmpeg sources including:
- C header files (filter/codec/format definitions)
- FFmpeg help output (--help parsing)
- FFmpeg documentation (descriptions and examples)

The extracted metadata is output as standardized JSON schemas that can be
consumed by code generation tools.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
