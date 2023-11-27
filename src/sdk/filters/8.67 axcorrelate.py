from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def axcorrelate(
    stream1: Stream,
    stream2: Stream,
    size: int = 256,
    algo: str = Literal["slow", "fast", "best"],
) -> Stream:
    """
    Calculate normalized windowed cross-correlation between two input audio streams.

    Resulted samples are always between -1 and 1 inclusive.
    If result is 1 it means two input samples are highly correlated in that selected segment.
    Result 0 means they are not correlated at all.
    If result is -1 it means two input samples are out of phase, which means they cancel each other.

    The filter accepts the following options:

        Parameters:
        ----------
        stream1 : Stream
            The first audio stream to cross-correlate.
        stream2 : Stream
            The second audio stream to cross-correlate.
        size : int, optional
            Set the size of the segment over which cross-correlation is calculated.
            Default is 256. Allowed range is from 2 to 131072.
        algo : str, optional
            Set the algorithm for cross-correlation. Can be 'slow', 'fast', or 'best'.
            Default is 'best'. The fast algorithm assumes mean values over any given segment
            are always zero and thus need much fewer calculations to make.
            This is generally not true, but is valid for typical audio streams.

    Example usage:
    --------------
    stream1.axcorrelate(
        stream2,
        size=512,
        algo='fast',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#axcorrelate
    """
    return FilterNode(
        [stream1, stream2],
        axcorrelate.__name__,
        kwargs={
            "size": size,
            "algo": algo,
        },
    ).stream()
