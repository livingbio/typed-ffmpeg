from typing import Union

from ..node import FilterNode
from ..stream import Stream


def tiltshelf(
    stream: Stream,
    gain: Union[int, float],
    frequency: float = 3000,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 1,
    poles: int = 2,
    mix: float = 1,
    channels: str = "",
    normalize: bool = False,
    transform: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 0,
) -> Stream:
    """
    Boost or cut the lower frequencies and cut or boost higher frequencies
    of the audio using a two-pole shelving filter with a response similar to
    that of a standard hi-fi's tone-controls. This is also known as shelving equalisation (EQ).

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        gain : int or float
            Give the gain at 0 Hz. Its useful range is about -20
            (for a large cut) to +20 (for a large boost).
            Beware of clipping when using a positive gain.
        frequency : float, optional
            Set the filter's central frequency and so can be used
            to extend or reduce the frequency range to be boosted or cut.
            The default value is 3000 Hz.
        width_type : str, optional
            Set method to specify band-width of filter.
            'h': Hz
            'q': Q-Factor
            'o': octave
            's': slope
            'k': kHz
        width : float, optional
            Determine how steep is the filter's shelf transition.
        poles : int, optional
            Set number of poles. Default is 2.
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
            'di': Direct Form I
            'dii': Direct Form II
            'tdi': Trapezoidal Direct Form I
            'tdii': Trapezoidal Direct Form II
            'latt': Lattice
            'svf': State Variable Filter
            'zdf': Zero-Delay Feedback
        precision : str, optional
            Set precision of filtering.
            'auto': Pick automatic sample format depending on surround filters.
            's16': Always use signed 16-bit.
            's32': Always use signed 32-bit.
            'f32': Always use float 32-bit.
            'f64': Always use float 64-bit.
        block_size : int, optional
            Set block size used for reverse IIR processing.
            If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering
            will become linear phase otherwise if not big enough it will just produce nasty artifacts.
            Note that the filter delay will be exactly this many samples when set to non-zero value.

    Example usage:
    --------------
    stream.tiltshelf(
        gain=-10,
        frequency=5000,
        width_type='o',
        width=1,
        poles=2,
        mix=0.5,
        normalize=True,
        transform='tdii',
        precision='auto',
        block_size=0,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#tiltshelf
    """
    return FilterNode(
        stream,
        tiltshelf.__name__,
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
