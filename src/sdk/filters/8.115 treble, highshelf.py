from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def treble_highshelf(
    stream: Stream,
    gain: float = 0,
    frequency: float = 3000,
    width_type: str = Literal["h", "q", "o", "s", "k"],
    width: float = 0.707,
    poles: int = 2,
    mix: float = 1,
    channels: str = None,
    normalize: bool = False,
    transform_type: str = Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"],
    precision: str = Literal["auto", "s16", "s32", "f32", "f64"],
    block_size: int = 256,
) -> Stream:
    """
    Boost or cut treble (upper) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi's tone-controls. This is also known as shelving equalization (EQ).

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        gain : float, optional
            Give the gain at whichever is the lower of ~22 kHz and the
            Nyquist frequency. Its useful range is about -20 (for a large cut)
            to +20 (for a large boost). Beware of clipping when using a positive gain.
            Default is 0.
        frequency : float, optional
            Set the filter's central frequency and so can be used to extend or
            reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        width_type : str, optional
            Set method to specify the bandwidth of the filter.
            - h : Hz
            - q : Q-Factor
            - o : octave
            - s : slope
            - k : kHz
            Default is 'h'.
        width : float, optional
            Determine how steep the filter's shelf transition is.
            Default is 0.707.
        poles : int, optional
            Set the number of poles. Default is 2.
        mix : float, optional
            How much to use the filtered signal in output. Default is 1.
            Range is between 0 and 1.
        channels : str, optional
            Specify which channels to filter. By default, all available channels are filtered.
        normalize : bool, optional
            Normalize biquad coefficients. Default is False. Enabling it will normalize
            the magnitude response at DC to 0dB.
        transform_type : str, optional
            Set the transform type of the IIR filter.
            - di
            - dii
            - tdi
            - tdii
            - latt
            - svf
            - zdf
            Default is 'di'.
        precision : str, optional
            Set the precision of filtering.
            - auto: Pick automatic sample format depending on surround filters.
            - s16: Always use signed 16-bit.
            - s32: Always use signed 32-bit.
            - f32: Always use float 32-bit.
            - f64: Always use float 64-bit.
            Default is 'auto'.
        block_size : int, optional
            Set the block size used for reverse IIR processing. If this value is set
            to a high enough value (higher than impulse response length truncated when
            reaches near zero values), filtering will become linear phase. Otherwise,
            if not big enough, it will just produce nasty artifacts.
            Note that filter delay will be exactly this many samples when set to a
            non-zero value.
            Default is 256.

    Example usage:
    --------------
    stream.treble_highshelf(
        gain=6,
        frequency=4000,
        width_type='o',
        width=2,
        poles=4,
        mix=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf
    """
    return FilterNode(
        stream,
        treble_highshelf.__name__,
        kwargs={
            "gain": gain,
            "frequency": frequency,
            "width_type": width_type,
            "width": width,
            "poles": poles,
            "mix": mix,
            "channels": channels,
            "normalize": normalize,
            "transform_type": transform_type,
            "precision": precision,
            "block_size": block_size,
        },
    ).stream()
