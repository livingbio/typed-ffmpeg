from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def bandpass(
    stream: Stream,
    frequency: float = 3000,
    csg: int = 0,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 1,
    mix: float = 1,
    channels: int = None,
    normalize: int = 0,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 0,
) -> Stream:
    """
    Apply a two-pole Butterworth band-pass filter with central frequency frequency, and (3dB-point) band-width width. The csg option selects a constant skirt gain (peak gain = Q) instead of the default: constant 0dB peak gain. The filter rolls off at 6dB per octave (20dB per decade).

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    frequency : float, optional
        Set the filter's central frequency. Default is 3000.
    csg : int, optional
        Constant skirt gain if set to 1. Defaults to 0.
    width_type : str, optional
        Set method to specify band-width of the filter.
        - 'h': Hz
        - 'q': Q-Factor
        - 'o': octave
        - 's': slope
        - 'k': kHz
        Default is 'h'.
    width : float, optional
        Specify the band-width of a filter in width_type units.
        Default is 1.
    mix : float, optional
        How much to use filtered signal in output. Default is 1.
        Range is between 0 and 1.
    channels : int, optional
        Specify which channels to filter, by default all available are filtered.
    normalize : int, optional
        Normalize biquad coefficients, by default is disabled.
        Enabling it will normalize magnitude response at DC to 0dB.
    transform : str, optional
        Set transform type of IIR filter.
        - 'di'
        - 'dii'
        - 'tdi'
        - 'tdii'
        - 'latt'
        - 'svf'
        - 'zdf'
    precision : str, optional
        Set precision of filtering.
        - 'auto': Pick automatic sample format depending on surround filters.
        - 's16': Always use signed 16-bit.
        - 's32': Always use signed 32-bit.
        - 'f32': Always use float 32-bit.
        - 'f64': Always use float 64-bit.
    block_size : int, optional
        Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts.
        Note that filter delay will be exactly this many samples when set to non-zero value.

    Example usage:
    --------------
    stream.bandpass(
        frequency=2000,
        width_type='k',
        width=2,
        mix=0.7,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bandpass
    """
    return FilterNode(
        stream,
        bandpass.__name__,
        kwargs={
            "frequency": frequency,
            "csg": csg,
            "width_type": width_type,
            "width": width,
            "mix": mix,
            "channels": channels,
            "normalize": normalize,
            "transform": transform,
            "precision": precision,
            "block_size": block_size,
        },
    ).stream()
