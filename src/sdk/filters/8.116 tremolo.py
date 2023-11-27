from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def tremolo(
    stream: Stream,
    f: Optional[float] = 5.0,
    d: Optional[float] = 0.5,
) -> Stream:
    """
    Sinusoidal amplitude modulation.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        f : float, optional
            Modulation frequency in Hertz. Modulation frequencies in the subharmonic range
            (20 Hz or lower) will result in a tremolo effect.
            This filter may also be used as a ring modulator by specifying
            a modulation frequency higher than 20 Hz.
            Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        d : float, optional
            Depth of modulation as a percentage. Range is 0.0 - 1.0.
            Default value is 0.5.

    Example usage:
    --------------
    stream.tremolo(
        f=2.5,
        d=0.3,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#tremolo
    """
    return FilterNode(
        stream,
        tremolo.__name__,
        kwargs={
            "f": f,
            "d": d,
        },
    ).stream()
