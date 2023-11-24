from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def bs2b(
    stream: Stream,
    profile: str = Literal["default", "cmoy", "jmeier"],
    fcut: int = 700,
    feed: int = 50,
) -> Stream:
    """
    Bauer stereo to binaural transformation, which improves headphone listening of stereo audio records.

    To enable compilation of this filter you need to configure FFmpeg with --enable-libbs2b.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    profile : str, optional
        Pre-defined crossfeed level. Can be 'default', 'cmoy', or 'jmeier'.
        Default is 'default'.
    fcut : int, optional
        Cut frequency (in Hz). Default is 700.
    feed : int, optional
        Feed level (in Hz). Default is 50.

    Example usage:
    --------------
    stream.bs2b(
        profile='cmoy',
        fcut=650,
        feed=95,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bs2b
    """
    return FilterNode(
        stream,
        bs2b.__name__,
        kwargs={
            "profile": profile,
            "fcut": fcut,
            "feed": feed,
        },
    ).stream()
