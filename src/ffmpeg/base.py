from .nodes.input_node import InputNode
from .streams.av import AVStream


def input(filename: str, **kwargs: str | int | None | float) -> AVStream:
    """Input file URL (ffmpeg ``-i`` option)
    Any supplied kwargs are passed to ffmpeg verbatim (e.g. ``t=20``,
    ``f='mp4'``, ``acodec='pcm'``, etc.).
    To tell ffmpeg to read from stdin, use ``pipe:`` as the filename.
    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
    """
    kwargs["filename"] = filename
    fmt = kwargs.pop("f", None)
    if fmt:
        if "format" in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs["format"] = fmt
    return InputNode(filename=filename, name=input.__name__, kwargs=kwargs).stream()
