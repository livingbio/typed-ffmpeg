from typing import Optional, Union

from ..node import FilterNode
from ..stream import Stream


def aloop(
    stream: Stream,
    loop: int = 0,
    size: int = 0,
    start: int = 0,
    time: Optional[Union[int, float]] = None,
) -> Stream:
    """
    Loop audio samples.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        loop : int, optional
            Set the number of loops. Setting this value to -1 will result in infinite loops.
            Default is 0.
        size : int, optional
            Set maximal number of samples. Default is 0.
        start : int, optional
            Set first sample of loop. Default is 0.
        time : int or float, optional
            Set the time of loop start in seconds.
            Only used if option named 'start' is set to -1.

    Example usage:
    --------------
    stream.aloop(
        loop=-1,
        size=10000,
        start=5000,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aloop
    """
    return FilterNode(
        stream,
        aloop.__name__,
        kwargs={
            "loop": loop,
            "size": size,
            "start": start,
            "time": time,
        },
    ).stream()
