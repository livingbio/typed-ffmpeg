"""Input/output utilities for FFmpeg DAG operations."""

from ._input import input
from ._output import output

# merge_outputs is defined in base.py, not here
__all__ = ["input", "output"]
