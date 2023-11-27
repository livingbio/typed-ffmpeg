from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def flanger(
    stream: Stream,
    delay: float = 0,
    depth: float = 2,
    regen: float = 0,
    width: float = 71,
    speed: float = 0.5,
    shape: str = Literal["triangular", "sinusoidal"],
    phase: float = 25,
    interp: str = Literal["linear", "quadratic"],
) -> Stream:
    """
    Apply a flanging effect to the audio.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    delay : float, optional
        Set base delay in milliseconds. Range from 0 to 30. Default value is 0.
    depth : float, optional
        Set added sweep delay in milliseconds. Range from 0 to 10. Default value is 2.
    regen : float, optional
        Set percentage regeneration (delayed signal feedback). Range from -95 to 95.
        Default value is 0.
    width : float, optional
        Set percentage of delayed signal mixed with original. Range from 0 to 100.
        Default value is 71.
    speed : float, optional
        Set sweeps per second (Hz). Range from 0.1 to 10. Default value is 0.5.
    shape : str, optional
        Set swept wave shape, can be 'triangular' or 'sinusoidal'.
        Default value is 'sinusoidal'.
    phase : float, optional
        Set swept wave percentage-shift for multi-channel. Range from 0 to 100.
        Default value is 25.
    interp : str, optional
        Set delay-line interpolation, 'linear' or 'quadratic'.
        Default is 'linear'.

    Example usage:
    --------------
    stream.flanger(
        delay=10,
        depth=5,
        regen=15,
        width=60,
        speed=1,
        shape='triangular',
        interp='linear',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#flanger
    """
    return FilterNode(
        stream,
        flanger.__name__,
        kwargs={
            "delay": delay,
            "depth": depth,
            "regen": regen,
            "width": width,
            "speed": speed,
            "shape": shape,
            "phase": phase,
            "interp": interp,
        },
    ).stream()
