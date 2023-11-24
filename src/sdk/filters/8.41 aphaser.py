from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def aphaser(
    stream: Stream,
    in_gain: float = 0.4,
    out_gain: float = 0.74,
    delay: float = 3.0,
    decay: float = 0.4,
    speed: float = 0.5,
    type: str = Literal["triangular", "t", "sinusoidal", "s"],
) -> Stream:
    """
    Add a phasing effect to the input audio.

    A phaser filter creates series of peaks and troughs in the frequency spectrum.
    The position of the peaks and troughs are modulated so that they vary over time, creating a sweeping effect.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    in_gain : float, optional
        Set input gain. Default is 0.4.
    out_gain : float, optional
        Set output gain. Default is 0.74.
    delay : float, optional
        Set delay in milliseconds. Default is 3.0.
    decay : float, optional
        Set decay. Default is 0.4.
    speed : float, optional
        Set modulation speed in Hz. Default is 0.5.
    type : str, optional
        Set modulation type. Default is 'triangular'. It accepts the following values:
            - 'triangular' or 't'
            - 'sinusoidal' or 's'

    Returns:
    -------
    Stream
        The resulting filtered stream.

    Example usage:
    --------------
    stream.aphaser(
        in_gain=0.6,
        out_gain=0.8,
        delay=5.0,
        decay=0.3,
        speed=1.0,
        type='sinusoidal',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaser
    """
    return FilterNode(
        stream,
        aphaser.__name__,
        kwargs={
            "in_gain": in_gain,
            "out_gain": out_gain,
            "delay": delay,
            "decay": decay,
            "speed": speed,
            "type": type,
        },
    ).stream()
