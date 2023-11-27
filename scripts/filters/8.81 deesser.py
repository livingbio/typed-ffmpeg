from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def deesser(
    stream: Stream,
    i: float = 0,
    m: float = 0.5,
    f: float = 0.5,
    s: str = Literal["i", "o", "e"],
) -> Stream:
    """
    Apply de-essing to the audio samples.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    i : float, optional
        Set intensity for triggering de-essing. Allowed range is from 0 to 1.
        Default is 0.
    m : float, optional
        Set amount of ducking on treble part of sound. Allowed range is from 0 to 1.
        Default is 0.5.
    f : float, optional
        How much of the original frequency content to keep when de-essing.
        Allowed range is from 0 to 1. Default is 0.5.
    s : str, optional
        Set the output mode. It can be 'i' (Pass input unchanged), 'o' (Pass ess filtered out),
        or 'e' (Pass only ess). Default value is 'o'.

    Example usage:
    --------------
    stream.deesser(i=0.2, m=0.8, f=0.3, s='i')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#deesser
    """
    return FilterNode(
        stream,
        deesser.__name__,
        kwargs={
            "i": i,
            "m": m,
            "f": f,
            "s": s,
        },
    ).stream()
