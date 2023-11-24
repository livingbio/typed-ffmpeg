from typing import Union

from ..node import FilterNode
from ..stream import Stream


def vibrato(
    stream: Stream,
    f: float = 5.0,
    d: Union[int, float] = 0.5,
) -> Stream:
    """
    Sinusoidal phase modulation.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        f : float, optional
            Modulation frequency in Hertz.
            Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        d : float, optional
            Depth of modulation as a percentage. Range is 0.0 - 1.0.
            Default value is 0.5.

    Example usage:
    --------------
    stream.vibrato(
        f=2.5,
        d=0.2,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrato
    """
    return FilterNode(
        stream,
        vibrato.__name__,
        kwargs={
            "f": f,
            "d": d,
        },
    ).stream()
