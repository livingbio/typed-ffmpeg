from typing import Literal, Union

from ..node import FilterNode
from ..stream import Stream


def allpass(
    stream: Stream,
    frequency: float,
    width_type: Literal["h", "q", "o", "s", "k"],
    width: Union[int, float],
    mix: float = 1,
    channels: str = None,
    normalize: bool = False,
    order: Literal[1, 2] = 2,
    transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] = None,
    precision: Literal["auto", "s16", "s32", "f32", "f64"] = "auto",
) -> Stream:
    """
    Apply a two-pole all-pass filter with central frequency (in Hz) frequency, and filter-width width. An all-pass filter changes the audio's frequency to phase relationship without changing its frequency to amplitude relationship.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        frequency : float
            Set frequency in Hz.
        width_type : str
            Set method to specify band-width of filter.
            Options:
            - 'h': Hz
            - 'q': Q-Factor
            - 'o': octave
            - 's': slope
            - 'k': kHz
        width : Union[int, float]
            Specify the band-width of a filter in width_type units.
        mix : float, optional
            How much to use filtered signal in output. Default is 1.
            Range is between 0 and 1.
        channels : str, optional
            Specify which channels to filter, by default, all available are filtered.
        normalize : bool, optional
            Normalize biquad coefficients, by default is disabled.
            Enabling it will normalize magnitude response at DC to 0dB.
        order : str, optional
            Set the filter order, can be 1 or 2. Default is 2.
        transform : str, optional
            Set transform type of IIR filter.
            Options:
            - 'di'
            - 'dii'
            - 'tdi'
            - 'tdii'
            - 'latt'
            - 'svf'
            - 'zdf'
        precision : str, optional
            Set precision of filtering.
            Options:
            - 'auto': Pick automatic sample format depending on surround filters.
            - 's16': Always use signed 16-bit.
            - 's32': Always use signed 32-bit.
            - 'f32': Always use float 32-bit.
            - 'f64': Always use float 64-bit.

    Example usage:
    --------------
    stream.allpass(
        frequency=1000,
        width_type='h',
        width=500,
        mix=0.8,
        channels="0-2",
        normalize=True,
        order=1,
        transform="di",
        precision="s16",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#allpass
    """

    return FilterNode(
        stream,
        allpass.__name__,
        kwargs={
            "frequency": frequency,
            "width_type": width_type,
            "width": width,
            "mix": mix,
            "channels": channels,
            "normalize": normalize,
            "order": order,
            "transform": transform,
            "precision": precision,
        },
    ).stream()
