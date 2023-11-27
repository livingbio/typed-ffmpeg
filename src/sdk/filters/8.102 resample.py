from typing import Union

from ..node import FilterNode
from ..stream import Stream


def resample(
    stream: Stream,
    sample_rate: Union[int, str],
    sample_fmt: str = None,
    channel_layout: Union[str, int] = None,
) -> Stream:
    """
    Convert the audio sample format, sample rate, and channel layout.

    It is not meant to be used directly.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    sample_rate : int or str
        The target sample rate of the output.
        If it is a string, it must be in the format 'rate[.frac]'.
    sample_fmt : str, optional
        The target sample format of the output.
        If not provided, the input sample format will be used.
    channel_layout : int or str, optional
        The target channel layout of the output.
        If not provided, the input channel layout will be used.

    Example usage:
    --------------
    stream.resample(
        sample_rate=44100,
        sample_fmt='fltp',
        channel_layout='stereo',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aresample
    """
    return FilterNode(
        stream,
        resample.__name__,
        kwargs={
            "sample_rate": sample_rate,
            "sample_fmt": sample_fmt,
            "channel_layout": channel_layout,
        },
    ).stream()
