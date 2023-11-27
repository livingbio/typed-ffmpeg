from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def crossfeed(
    stream: Stream,
    strength: float = 0.2,
    range: float = 0.5,
    slope: float = 0.5,
    level_in: Optional[float] = 0.9,
    level_out: Optional[float] = 1,
    block_size: Optional[int] = None,
) -> Stream:
    """
    Apply headphone crossfeed filter.

    Crossfeed is the process of blending the left and right channels of stereo audio recording.
    It is mainly used to reduce extreme stereo separation of low frequencies.
    The intent is to produce more speaker like sound to the listener.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    strength : float, optional
        Set strength of crossfeed. Default is 0.2. Allowed range is from 0 to 1.
        This sets gain of the low shelf filter for the side part of the stereo image.
        Default is -6dB. Max allowed is -30dB when strength is set to 1.
    range : float, optional
        Set soundstage wideness. Default is 0.5. Allowed range is from 0 to 1.
        This sets the cut-off frequency of the low shelf filter.
        Default is cut off near 1550 Hz. With range set to 1, the cut-off frequency is set to 2100 Hz.
    slope : float, optional
        Set curve slope of the low shelf filter. Default is 0.5.
        Allowed range is from 0.01 to 1.
    level_in : float, optional
        Set input gain. Default is 0.9.
    level_out : float, optional
        Set output gain. Default is 1.
    block_size : int, optional
        Set block size used for reverse IIR processing. If this value is set to a high enough
        value (higher than impulse response length truncated when reaches near zero values),
        the filtering will become linear phase. Otherwise, if not big enough, it will just produce nasty artifacts.
        Note that the filter delay will be exactly this many samples when set to a non-zero value.

    Example usage:
    --------------
    stream.crossfeed(
        strength=0.3,
        range=0.8,
        slope=0.3,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#crossfeed
    """
    return FilterNode(
        stream,
        crossfeed.__name__,
        kwargs={
            "strength": strength,
            "range": range,
            "slope": slope,
            "level_in": level_in,
            "level_out": level_out,
            "block_size": block_size,
        },
    ).stream()
