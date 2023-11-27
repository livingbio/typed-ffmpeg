from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def lowpass(
    stream: Stream,
    frequency: int = 500,
    poles: int = 2,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 0.707,
    mix: float = 1.0,
    channels: str = None,
    normalize: bool = False,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = None,
) -> Stream:
    """
    Apply a low-pass filter with 3dB point frequency. The filter can be either single-pole or double-pole (the default). The filter roll off at 6dB per pole per octave (20dB per pole per decade).

    The filter accepts the following options:

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    frequency : int, optional
        Set frequency in Hz. Default is 500.
    poles : int, optional
        Set the number of poles. Default is 2.
    width_type : str, optional
        Set the method to specify the bandwidth of the filter.
          - 'h': Hz
          - 'q': Q-Factor
          - 'o': octave
          - 's': slope
          - 'k': kHz
        Default is 'q'.
    width : float, optional
        Specify the bandwidth of a filter in width_type units. Applies only to the double-pole filter.
        The default is 0.707q and gives a Butterworth response.
    mix : float, optional
        How much to use the filtered signal in the output. Default is 1.
        Range is between 0 and 1.
    channels : str, optional
        Specify which channels to filter. By default, all available channels are filtered.
    normalize : bool, optional
        Normalize biquad coefficients. Default is False.
        Enabling it will normalize the magnitude response at DC to 0dB.
    transform : str, optional
        Set the transform type of the IIR filter.
          - 'di'
          - 'dii'
          - 'tdi'
          - 'tdii'
          - 'latt'
          - 'svf'
          - 'zdf'
        Default is 'di'.
    precision : str, optional
        Set the precision of filtering.
          - 'auto': Automatically pick the sample format depending on surround filters.
          - 's16': Always use signed 16-bit.
          - 's32': Always use signed 32-bit.
          - 'f32': Always use float 32-bit.
          - 'f64': Always use float 64-bit.
        Default is 'auto'.
    block_size : int, optional
        Set the block size used for reverse IIR processing. If this value is set to a high enough value (higher than the impulse response length truncated when it reaches near zero values), filtering will become linear phase. Otherwise, if not big enough, it will just produce nasty artifacts.
        Note that the filter delay will be exactly this many samples when set to a non-zero value.

    Example usage:
    --------------
    stream.lowpass(frequency=1000, poles=1)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#lowpass
    """
    return FilterNode(
        stream,
        lowpass.__name__,
        kwargs={
            "frequency": frequency,
            "poles": poles,
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
