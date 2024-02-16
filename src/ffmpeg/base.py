from typing import Any

from ffmpeg.schema import StreamType

from .dag.nodes import FilterableStream, FilterNode, InputNode, MergeOutputsNode, OutputNode, OutputStream
from .streams.audio import AudioStream
from .streams.av import AVStream
from .streams.video import VideoStream


def input(filename: str, **kwargs: Any) -> AVStream:
    """
    Input file URL (ffmpeg ``-i`` option)

    Args:
        filename: Input file URL
        **kwargs: ffmpeg's input file options

    Returns:
        Input stream

    Examples:
    ```py
    >>> input('input.mp4')
    <AVStream:input.mp4:0>
    ```
    """
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


def vfilter(
    *streams: FilterableStream, name: str, input_typings: tuple[StreamType, ...] = (StreamType.video,), **kwargs: Any
) -> VideoStream:
    """
    Apply a custom video filter which has only one output to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
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
    *streams: FilterableStream, name: str, input_typings: tuple[StreamType, ...] = (StreamType.audio,), **kwargs: Any
) -> AudioStream:
    """
    Apply a custom audio filter which has only one output to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
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
    **kwargs: Any
) -> FilterNode:
    """
    Apply a custom filter which has multiple outputs to this stream

    Args:
        *streams: the streams to apply the filter to
        name: the name of the filter
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
