"""
Defines the basic schema for the FFmpeg command line options.

This module contains base classes used throughout the typed-ffmpeg library to handle
default values, automatic parameter derivation, and stream type definitions.
These components form the foundation of the type annotation system that
enables static type checking in the FFmpeg filter graph.
"""

from .common.schema import StreamType


class Default(str):
    """
    Represents a default value for an FFmpeg option.

    This class is used for annotation purposes only and indicates that a parameter
    should use its default value. When a parameter is marked with Default, it
    will not be explicitly passed to the FFmpeg command line, letting FFmpeg use
    its built-in default value instead.

    Example:
        ```python
        # This will use FFmpeg's default crf value
        video.output("output.mp4", crf=Default("23"))
        ```
    """

    ...


class Auto(Default):
    """
    Represents an automatically derived value for an FFmpeg option.

    This is a special case of Default that indicates the value should be
    calculated automatically based on the context. For example, the number
    of inputs to a filter might be derived from the number of streams passed
    to that filter.

    Auto contains an expression string that defines how the value should be computed.

    Example:
        ```python
        # The number of inputs is automatically derived from the length of streams
        hstack(*streams, inputs=Auto("len(streams)"))
        ```
    """


__all__ = [
    "Auto",
    "Default",
    "StreamType",
]
