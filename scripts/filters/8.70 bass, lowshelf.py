from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def bass_lowshelf(
    stream: Stream,
    gain: float,
    frequency: float = 100,
    width_type: Literal["h", "q", "o", "s", "k"] = None,
    width: float = None,
    poles: int = 2,
    mix: float = 1,
    channels: str = "all",
    normalize: bool = False,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 0,
) -> Stream:
    """
    Boost or cut the bass (lower) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi's tone-controls. This is also known as shelving equalisation (EQ).

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        gain : float
            Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency : float, optional
            Set the filter's central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz.
        width_type : str, optional
            Set method to specify the band-width of the filter.
            'h' - Hz
            'q' - Q-Factor
            'o' - octave
            's' - slope
            'k' - kHz
        width : float
            Determine how steep is the filter's shelf transition.
        poles : int, optional
            Set the number of poles. Default is 2.
        mix : float, optional
            How much to use the filtered signal in output. Default is 1. Range is between 0 and 1.
        channels : str, optional
            Specify which channels to filter, by default all available are filtered.
        normalize : bool, optional
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize the magnitude response at DC to 0dB.
        transform : str, optional
            Set the transform type of the IIR filter.
            'di'
            'dii'
            'tdi'
            'tdii'
            'latt'
            'svf'
            'zdf'
        precision : str, optional
            Set the precision of filtering.
            'auto' - Pick automatic sample format depending on surround filters
            's16' - Always use signed 16-bit
            's32' - Always use signed 32-bit
            'f32' - Always use float 32-bit
            'f64' - Always use float 64-bit
        block_size : int, optional
            Set block size used for reverse IIR processing. If this value is set to a high enough value (higher than impulse response length truncated when it reaches near zero values), filtering will become linear phase. If not big enough, it will just produce nasty artifacts.
            Note that the filter delay will be exactly this many samples when set to a non-zero value.

    Example usage:
    --------------
    stream.bass_lowshelf(
        gain=-10,
        frequency=80,
        width_type='h',
        width=2,
        poles=2,
        mix=0.8,
        channels='FL',
        normalize=True,
        transform='di',
        precision='auto',
        block_size=0,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bass-002c-lowshelf
    """
    return FilterNode(
        stream,
        bass_lowshelf.__name__,
        kwargs={
            "gain": gain,
            "frequency": frequency,
            "width_type": width_type,
            "width": width,
            "poles": poles,
            "mix": mix,
            "channels": channels,
            "normalize": normalize,
            "transform": transform,
            "precision": precision,
            "block_size": block_size,
        },
    ).stream()
