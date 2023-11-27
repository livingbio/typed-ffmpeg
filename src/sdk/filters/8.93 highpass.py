from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def highpass(
    stream: Stream,
    frequency: float = 3000,
    poles: int = 2,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 0.707,
    mix: float = 1,
    channels: str = "",
    normalize: bool = False,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 0,
) -> Stream:
    """
    Apply a high-pass filter with 3dB point frequency. The filter can be either single-pole, or double-pole (the default). The filter rolls off at 6dB per pole per octave (20dB per pole per decade).

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        frequency : float, optional
            Set frequency in Hz. Default is 3000.
        poles : int, optional
            Set number of poles. Default is 2.
        width_type : str, optional
            Set method to specify the bandwidth of the filter.
            Can be 'h' (Hz), 'q' (Q-Factor), 'o' (octave), 's' (slope), or 'k' (kHz).
        width : float, optional
            Specify the bandwidth of a filter in width_type units.
            Applies only to double-pole filter.
            The default is 0.707q and gives a Butterworth response.
        mix : float, optional
            How much to use the filtered signal in the output. Default is 1.
            Range is between 0 and 1.
        channels : str, optional
            Specify which channels to filter, by default all available are filtered.
        normalize : bool, optional
            Normalize biquad coefficients, by default is disabled.
            Enabling it will normalize the magnitude response at DC to 0dB.
        transform : str, optional
            Set the transform type of IIR filter.
            Can be 'di', 'dii', 'tdi', 'tdii', 'latt', 'svf', or 'zdf'.
        precision : str, optional
            Set the precision of filtering.
            Can be 'auto', 's16', 's32', 'f32', or 'f64'.
        block_size : int, optional
            Set the block size used for reverse IIR processing. If this value is set to a high enough
            value (higher than impulse response length truncated when reaches near zero values), filtering
            will become linear phase. Otherwise, if not big enough, it will just produce nasty artifacts.
            Note that filter delay will be exactly this many samples when set to a non-zero value.

    Example usage:
    --------------
    stream.highpass(
        frequency=1000,
        poles=1,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#highpass
    """
    return FilterNode(
        stream,
        highpass.__name__,
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
