from typing import Union

from ..node import FilterNode
from ..stream import Stream


def afreqshift(
    stream: Stream,
    shift: Union[int, float] = 0.0,
    level: Union[int, float] = 1.0,
    order: int = 8,
) -> Stream:
    """
    Apply frequency shift to input audio samples.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        shift : int or float, optional
            Specify frequency shift. Allowed range is -INT_MAX to INT_MAX.
            Default value is 0.0.
        level : int or float, optional
            Set output gain applied to the final output. Allowed range is from 0.0 to 1.0.
            Default value is 1.0.
        order : int, optional
            Set filter order used for filtering. Allowed range is from 1 to 16.
            Default value is 8.

    Example usage:
    --------------
    stream.afreqshift(
        shift=1000,
        level=0.5,
        order=4,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afreqshift
    """
    return FilterNode(
        stream,
        afreqshift.__name__,
        kwargs={
            "shift": shift,
            "level": level,
            "order": order,
        },
    ).stream()
