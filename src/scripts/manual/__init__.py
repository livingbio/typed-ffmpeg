"""
Manual Filter Definition Package

This package provides functionality for manually defining or augmenting filter
information that cannot be automatically extracted from FFmpeg documentation,
source code, or help output. The main functionality includes:

- Defining custom input/output type formulas for complex filters
- Overriding automatically extracted filter information
- Adding pre-processing steps for filter options
- Providing additional metadata for filters with special behaviors

These manual definitions supplement the automatically extracted information
to handle edge cases and special filters that require custom type annotations
beyond what can be parsed from standard sources.
"""
