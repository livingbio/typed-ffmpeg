from typing import List, Tuple, Union

from ..node import FilterNode
from ..stream import Stream


def aiir(
    stream: Stream,
    zeros: Union[List[Union[str, float]], Tuple[Union[str, float]]] = [],
    poles: Union[List[Union[str, float]], Tuple[Union[str, float]]] = [],
    gains: Union[List[float], Tuple[float]] = [],
    dry_gain: float = 1.0,
    wet_gain: float = 1.0,
    format: str = "zp",
    process: str = "d",
    precision: str = "dbl",
    normalize: bool = True,
    mix: float = 1.0,
    response: bool = False,
    channel: int = 0,
    size: str = "",
) -> Stream:
    """
    Apply an arbitrary Infinite Impulse Response filter.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    zeros : Union[List[Union[str, float]], Tuple[Union[str, float]]], optional
        Set B/numerator/zeros/reflection coefficients.
    poles : Union[List[Union[str, float]], Tuple[Union[str, float]]], optional
        Set A/denominator/poles/ladder coefficients.
    gains : Union[List[float], Tuple[float]], optional
        Set channels gains.
    dry_gain : float, optional
        Set input gain.
    wet_gain : float, optional
        Set output gain.
    format : str, optional
        Set coefficients format.
        'll': lattice-ladder function
        'sf': analog transfer function
        'tf': digital transfer function
        'zp': Z-plane zeros/poles, cartesian (default)
        'pr': Z-plane zeros/poles, polar radians
        'pd': Z-plane zeros/poles, polar degrees
        'sp': S-plane zeros/poles
    process : str, optional
        Set type of processing.
        'd': direct processing
        's': serial processing
        'p': parallel processing
    precision : str, optional
        Set filtering precision.
        'dbl': double-precision floating-point (default)
        'flt': single-precision floating-point
        'i32': 32-bit integers
        'i16': 16-bit integers
    normalize : bool, optional
        Normalize filter coefficients, by default is enabled.
        Enabling it will normalize magnitude response at DC to 0dB.
    mix : float, optional
        How much to use filtered signal in output. Default is 1.
        Range is between 0 and 1.
    response : bool, optional
        Show IR frequency response, magnitude(magenta), phase(green) and group delay(yellow) in additional video stream.
        By default it is disabled.
    channel : int, optional
        Set for which IR channel to display frequency response. By default is first channel
        displayed. This option is used only when response is enabled.
    size : str, optional
        Set video stream size. This option is used only when response is enabled.

    Example usage:
    --------------
    stream.aiir(
        zeros=[1, 2i, -3],
        poles=[1, 0.5],
        gains=[1, 0.5],
        dry_gain=0.8,
        wet_gain=1.2,
        format="zp",
        process="d",
        precision="dbl",
        normalize=True,
        mix=1.0,
        response=False,
        channel=0,
        size=""
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aiir
    """
    return FilterNode(
        stream,
        aiir.__name__,
        kwargs={
            "zeros": zeros,
            "poles": poles,
            "gains": gains,
            "dry_gain": dry_gain,
            "wet_gain": wet_gain,
            "format": format,
            "process": process,
            "precision": precision,
            "normalize": normalize,
            "mix": mix,
            "response": response,
            "channel": channel,
            "size": size,
        },
    ).stream()
