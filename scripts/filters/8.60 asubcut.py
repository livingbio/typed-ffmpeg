from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def asubcut(
    stream: Stream,
    cutoff: Optional[int] = 20,
    order: Optional[int] = 10,
    level: Optional[float] = 1,
) -> Stream:
    """
    Cut subwoofer frequencies.

    This filter allows you to set a custom, steeper roll-off than a highpass filter, and thus is able to more attenuate frequency content in the stop-band.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        cutoff : Optional[int], optional
            Set cutoff frequency in Hertz. Allowed range is 2 to 200.
            Default value is 20.
        order : Optional[int], optional
            Set filter order. Available values are from 3 to 20.
            Default value is 10.
        level : Optional[float], optional
            Set input gain level. Allowed range is from 0 to 1.
            Default value is 1.

    Example usage:
    --------------
    stream.asubcut(
        cutoff=50,
        order=5,
        level=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asubcut
    """
    return FilterNode(
        stream,
        asubcut.__name__,
        kwargs={"cutoff": cutoff, "order": order, "level": level},
    ).stream()
