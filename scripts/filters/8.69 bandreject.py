from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def bandreject(
    stream: Stream,
    frequency: float = 3000,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 0,
    mix: float = 1,
    channels: str = "",
    normalize: bool = False,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 0,
) -> Stream:
    """
    Apply a two-pole Butterworth band-reject filter with central frequency `frequency`, and (3dB-point) band-width `width`. The filter roll off at 6dB per octave (20dB per decade).

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        frequency : float, optional
            Set the filter's central frequency. Default is 3000.
        width_type : str, optional
            Set method to specify band-width of filter.
            - 'h': Hz
            - 'q': Q-Factor
            - 'o': octave
            - 's': slope
            - 'k': kHz
            Default is 'h'.
        width : float, optional
            Specify the band-width of a filter in width_type units.
        mix : float, optional
            How much to use filtered signal in output. Default is 1.
            Range is between 0 and 1.
        channels : str, optional
            Specify which channels to filter, by default all available are filtered.
        normalize : bool, optional
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
    stream.bandreject(
        frequency=5000,
        width=1000,
        mix=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bandreject
    """
    return FilterNode(
        stream,
        bandreject.__name__,
        kwargs={
            "frequency": frequency,
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
