from typing import Any

from .nodes.nodes import FilterableStream, FilterNode, InputNode, MergeOutputsNode, OutputNode, OutputStream
from .streams.av import AVStream


def input(filename: str, **kwargs: Any) -> AVStream:
    """
    Input file URL (ffmpeg ``-i`` option)

    Args:
        filename: Input file URL
        **kwargs: ffmpeg options

    Returns:
        Input stream
    """
    fmt = kwargs.pop("f", None)
    if fmt:
        if "format" in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs["format"] = fmt
    return InputNode(filename=filename, kwargs=tuple(kwargs.items())).stream()


def output(*streams: FilterableStream, filename: str, **kwargs: Any) -> OutputStream:
    """
    Output the streams to a file URL

    Args:
        *streams: the streams to output
        filename: the filename to output to
        **kwargs: the arguments for the output

    Returns:
        the output stream
    """
    return OutputNode(filename=filename, inputs=streams, kwargs=tuple(kwargs.items())).stream()


def merge_outputs(*streams: OutputStream) -> OutputStream:
    """
    Merge multiple output streams into one.

    Args:
        *streams: The output streams to merge.

    Returns:
        The merged output stream.
    """
    return MergeOutputsNode(inputs=streams).stream()


def filter(*streams: FilterableStream, name: str, **kwargs: Any) -> AVStream:
    """
    Apply a custom filter which has only one output to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
        **kwargs: the arguments for the filter

    Returns:
        the output stream
    """
    return FilterNode(name=name, inputs=streams, kwargs=tuple(kwargs.items())).stream(0)


def filter_multi_output(*streams: FilterableStream, name: str, **kwargs: Any) -> FilterNode:
    """
    Apply a custom filter which has multiple outputs to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
        **kwargs: the arguments for the filter

    Returns:
        the FilterNode
    """
    return FilterNode(name=name, kwargs=tuple(kwargs.items()), inputs=streams)
