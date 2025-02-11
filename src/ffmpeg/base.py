"""
This module defined the basic functions for creating the ffmpeg filter graph.
"""

from typing import Any

from .dag.io._input import input
from .dag.io._output import output
from .dag.nodes import (
    FilterableStream,
    FilterNode,
    GlobalNode,
    GlobalStream,
    OutputStream,
)
from .schema import StreamType
from .streams.audio import AudioStream
from .streams.video import VideoStream


def merge_outputs(*streams: OutputStream) -> GlobalStream:
    """
    Merge multiple output streams into one.

    Args:
        *streams: The output streams to merge.

    Returns:
        The merged output stream.
    """
    return GlobalNode(inputs=streams).stream()


def vfilter(
    *streams: FilterableStream,
    name: str,
    input_typings: tuple[StreamType, ...] = (StreamType.video,),
    **kwargs: Any,
) -> VideoStream:
    """
    Apply a custom video filter which has only one output to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
        input_typings: the input typings of the filter
        **kwargs: the arguments for the filter

    Returns:
        the output stream

    Note:
        This function is for custom filter which is not implemented in typed-ffmpeg
    """
    return FilterNode(
        name=name,
        inputs=streams,
        output_typings=(StreamType.video,),
        input_typings=input_typings,
        kwargs=tuple(kwargs.items()),
    ).video(0)


def afilter(
    *streams: FilterableStream,
    name: str,
    input_typings: tuple[StreamType, ...] = (StreamType.audio,),
    **kwargs: Any,
) -> AudioStream:
    """
    Apply a custom audio filter which has only one output to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
        input_typings: the input typings of the filter
        **kwargs: the arguments for the filter

    Returns:
        the output stream

    Note:
        This function is for custom filter which is not implemented in typed-ffmpeg
    """
    return FilterNode(
        name=name,
        inputs=streams,
        output_typings=(StreamType.audio,),
        input_typings=input_typings,
        kwargs=tuple(kwargs.items()),
    ).audio(0)


def filter_multi_output(
    *streams: FilterableStream,
    name: str,
    input_typings: tuple[StreamType, ...] = (),
    output_tyings: tuple[StreamType, ...] = (),
    **kwargs: Any,
) -> FilterNode:
    """
    Apply a custom filter which has multiple outputs to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
        input_typings: the input typings of the filter
        output_tyings: the output typings of the filter
        **kwargs: the arguments for the filter

    Returns:
        the FilterNode

    Note:
        This function is for custom filter which is not implemented in typed-ffmpeg
    """
    return FilterNode(
        name=name,
        kwargs=tuple(kwargs.items()),
        inputs=streams,
        input_typings=input_typings,
        output_typings=output_tyings,
    )


__all__ = [
    "input",
    "output",
    "merge_outputs",
    "vfilter",
    "afilter",
    "filter_multi_output",
]
