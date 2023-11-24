from typing import Union

from ..node import FilterNode
from ..stream import Stream


def drmeter(
    stream: Stream,
    length: Union[int, float] = 3,
) -> Stream:
    """
    Measure audio dynamic range.

    DR values of 14 and higher are found in very dynamic material. DR of 8 to 13
    is found in transition material. And anything less than 8 has very poor dynamics
    and is very compressed.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    length : Union[int, float], optional
        Set window length in seconds used to split audio into segments of equal length.
        Default is 3 seconds.

    Example usage:
    --------------
    stream.drmeter(length=5)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#drmeter
    """
    return FilterNode(
        stream,
        drmeter.__name__,
        kwargs={"length": length},
    ).stream()
