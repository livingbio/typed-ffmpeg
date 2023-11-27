from ..node import FilterNode
from ..stream import Stream


def asupercut(
    stream: Stream,
    cutoff: int = 20000,
    order: int = 10,
    level: float = 1,
) -> Stream:
    """
    Cut super frequencies.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        cutoff : int, optional
            Set cutoff frequency in Hertz. Allowed range is from 20000 to 192000.
            Default value is 20000.
        order : int, optional
            Set filter order. Available values are from 3 to 20. Default value is 10.
        level : float, optional
            Set input gain level. Allowed range is from 0 to 1. Default value is 1.

    Example usage:
    --------------
    stream.asupercut(
        cutoff=15000,
        order=6,
        level=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asupercut
    """
    return FilterNode(
        stream,
        asupercut.__name__,
        kwargs={
            "cutoff": cutoff,
            "order": order,
            "level": level,
        },
    ).stream()
