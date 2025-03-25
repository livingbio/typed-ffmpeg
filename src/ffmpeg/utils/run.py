"""
Utilities for executing FFmpeg commands and handling command arguments.

This module provides helper functions for formatting command-line arguments,
filtering default values, and preparing options for command execution.
"""

import shlex
from collections.abc import Mapping

from ..schema import Default
from ..utils.lazy_eval.schema import LazyValue
from .forzendict import FrozenDict


def command_line(args: list[str]) -> str:
    """
    Convert a list of command arguments to a properly escaped command-line string.

    This function takes a list of command arguments and converts it to a single
    string with proper shell escaping applied to each argument. This is useful
    for logging commands or displaying them to users.

    Args:
        args: The command arguments to convert to a string

    Returns:
        A properly escaped command-line string representation of the arguments

    Example:
        ```python
        cmd = ["ffmpeg", "-i", "input file.mp4", "-c:v", "libx264"]
        print(command_line(cmd))  # 'ffmpeg -i "input file.mp4" -c:v libx264'
        ```
    """
    return " ".join(shlex.quote(arg) for arg in args)


# Filter_Node_Option_Type
def ignore_default(
    kwargs: Mapping[str, str | int | float | bool | Default],
) -> FrozenDict[str, str | int | float | bool | LazyValue]:
    """
    Filter out Default values from a dictionary of options.

    This function is used to process FFmpeg filter options and command arguments,
    removing any values that are instances of the Default class. This ensures
    that only explicitly set options are passed to FFmpeg, allowing default values
    to be applied by FFmpeg itself.

    Args:
        kwargs: A mapping containing parameter names and values,
               which may include Default instances

    Returns:
        An immutable FrozenDict containing only non-Default values

    Example:
        ```python
        options = {"width": 1920, "height": 1080, "format": Default("yuv420p")}
        filtered = ignore_default(options)  # {"width": 1920, "height": 1080}
        ```
    """
    return FrozenDict({k: v for k, v in kwargs.items() if not isinstance(v, Default)})
