from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def dcshift(
    stream: Stream,
    shift: float,
    limitergain: Optional[float] = None,
) -> Stream:
    """
    Apply a DC shift to the audio.

    This can be useful to remove a DC offset (caused perhaps by a hardware problem
    in the recording chain) from the audio. The effect of a DC offset is reduced
    headroom and hence volume. The astats filter can be used to determine if
    a signal has a DC offset.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    shift : float
        Set the DC shift, allowed range is [-1, 1]. It indicates the amount to shift
        the audio.
    limitergain : float, optional
        Optional. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is
        used to prevent clipping.

    Example usage:
    --------------
    stream.dcshift(
        shift=0.2,
        limitergain=0.05,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#dcshift
    """
    return FilterNode(
        stream,
        dcshift.__name__,
        kwargs={
            "shift": shift,
            "limitergain": limitergain,
        },
    ).stream()
