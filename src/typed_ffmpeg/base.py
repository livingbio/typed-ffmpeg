from .nodes.nodes import FilterableStream, InputNode, MergeOutputsNode, OutputNode, OutputStream
from .streams.av import AVStream


def input(filename: str, **kwargs: str | int | None | float) -> AVStream:
    """Input file URL (ffmpeg ``-i`` option)
    Any supplied kwargs are passed to ffmpeg verbatim (e.g. ``t=20``,
    ``f='mp4'``, ``acodec='pcm'``, etc.).
    To tell ffmpeg to read from stdin, use ``pipe:`` as the filename.
    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
    """
    fmt = kwargs.pop("f", None)
    if fmt:
        if "format" in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs["format"] = fmt
    return InputNode(filename=filename, kwargs=tuple(kwargs.items())).stream()


def output(*inputs: FilterableStream, filename: str, **kwargs: str | int | None | float) -> OutputStream:
    return OutputNode(filename=filename, inputs=inputs, kwargs=tuple(kwargs.items())).stream()


def merge_outputs(*inputs: OutputStream) -> OutputStream:
    return MergeOutputsNode(inputs=inputs).stream()


__all__ = ["input", "output", "merge_outputs"]
