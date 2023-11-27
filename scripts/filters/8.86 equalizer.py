from typing import Optional, Union

from ..node import FilterNode
from ..stream import Stream


def equalizer(
    stream: Stream,
    frequency: float,
    width_type: Optional[Union[str, int]] = None,
    width: Optional[float] = None,
    gain: float = 0,
    mix: float = 1,
    channels: Optional[str] = None,
    normalize: bool = False,
    transform: Optional[str] = None,
    precision: Optional[str] = None,
    block_size: Optional[int] = None,
) -> Stream:
    """
    Apply a two-pole peaking equalisation (EQ) filter. With this filter, the signal-level at and around a selected frequency can be increased or decreased, whilst (unlike bandpass and bandreject filters) that at all other frequencies is unchanged.

    In order to produce complex equalisation curves, this filter can be given several times, each with a different central frequency.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        frequency : float
            Set the filter's central frequency in Hz.
        width_type : Optional[Union[str, int]], optional
            Set method to specify band-width of filter. Default is None.
            Valid values are: 'h' (Hz), 'q' (Q-Factor), 'o' (octave), 's' (slope), 'k' (kHz),
            or an integer value representing the corresponding option index.
        width : Optional[float], optional
            Specify the band-width of a filter in width_type units. Default is None.
        gain : float, optional
            Set the required gain or attenuation in dB. Default is 0.
            Beware of clipping when using a positive gain.
        mix : float, optional
            How much to use filtered signal in output. Default is 1.
            Range is between 0 and 1.
        channels : Optional[str], optional
            Specify which channels to filter. Default is None (i.e., all available channels are filtered).
        normalize : bool, optional
            Normalize biquad coefficients. Default is False.
            Enabling it will normalize magnitude response at DC to 0dB.
        transform : Optional[str], optional
            Set transform type of IIR filter. Default is None.
            Valid values are: 'di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf',
            or an integer value representing the corresponding option index.
        precision : Optional[str], optional
            Set precision of filtering. Default is None.
            Valid values are: 'auto', 's16', 's32', 'f32', 'f64',
            or an integer value representing the corresponding option index.
        block_size : Optional[int], optional
            Set block size used for reverse IIR processing. Default is None.
            If this value is set to a high enough value (higher than impulse response length
            truncated when reaches near zero values) filtering will become linear phase.
            If not big enough, it will produce artifacts.
            Note that the filter delay will be exactly this many samples when set to nonzero value.

    Example usage:
    --------------
    stream.equalizer(
        frequency=1000,
        width_type='h',
        width=100,
        gain=-6,
        mix=0.8,
        channels='0',
        normalize=True,
        transform='zdf',
        precision='f32',
        block_size=8192,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#equalizer
    """
    return FilterNode(
        stream,
        equalizer.__name__,
        kwargs={
            "frequency": frequency,
            "width_type": width_type,
            "width": width,
            "gain": gain,
            "mix": mix,
            "channels": channels,
            "normalize": normalize,
            "transform": transform,
            "precision": precision,
            "block_size": block_size,
        },
    ).stream()
