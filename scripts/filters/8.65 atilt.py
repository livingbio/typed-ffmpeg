from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def atilt(
    stream: Stream,
    freq: Optional[int] = 10000,
    slope: Optional[float] = 0,
    width: Optional[int] = 1000,
    order: Optional[int] = None,
    level: Optional[float] = 1,
) -> Stream:
    """
    Apply spectral tilt filter to the audio stream.

    This filter applies any spectral roll-off slope over any specified frequency band.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        freq : int, optional
            Set the central frequency of tilt in Hz. Default is 10000 Hz.
        slope : float, optional
            Set the slope direction of tilt. Default is 0. Allowed range is from -1 to 1.
        width : int, optional
            Set the width of tilt. Default is 1000. Allowed range is from 100 to 10000.
        order : int, optional
            Set the order of the tilt filter.
        level : float, optional
            Set the input volume level. Allowed range is from 0 to 4. Default is 1.

    Example usage:
    --------------
    stream.atilt(
        freq=8000,
        slope=-0.5,
        width=2000,
        level=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#atilt
    """
    return FilterNode(
        stream,
        atilt.__name__,
        kwargs={
            "freq": freq,
            "slope": slope,
            "width": width,
            "order": order,
            "level": level,
        },
    ).stream()
