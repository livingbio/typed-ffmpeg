from typing import List, Union

from ..node import FilterNode
from ..stream import Stream


def biquad(
    stream: Stream,
    b0: float,
    b1: float,
    b2: float,
    a0: float,
    a1: float,
    a2: float,
    channels: Union[int, List[int]] = "all",
) -> Stream:
    """
    Apply a biquad IIR filter with the given coefficients.
    Where b0, b1, b2 and a0, a1, a2 are the numerator and denominator coefficients respectively.
    and channels, c specify which channels to filter, by default all available are filtered.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    b0 : float
        Numerator coefficient.
    b1 : float
        Numerator coefficient.
    b2 : float
        Numerator coefficient.
    a0 : float
        Denominator coefficient.
    a1 : float
        Denominator coefficient.
    a2 : float
        Denominator coefficient.
    channels : int or List[int], optional
        Specify which channels to filter, by default all available are filtered.

    Example usage:
    --------------
    stream.biquad(
        b0=1.0,
        b1=0.5,
        b2=0.0,
        a0=1.0,
        a1=0.0,
        a2=0.0,
        channels=[0, 1],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#biquad
    """
    return FilterNode(
        stream,
        biquad.__name__,
        kwargs={
            "b0": b0,
            "b1": b1,
            "b2": b2,
            "a0": a0,
            "a1": a1,
            "a2": a2,
            "channels": channels,
        },
    ).stream()
