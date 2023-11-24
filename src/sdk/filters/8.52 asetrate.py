from typing import Union

from ..node import FilterNode
from ..stream import Stream


def asetrate(
    stream: Stream,
    sample_rate: Union[int, float] = 44100,
) -> Stream:
    """
    Set the sample rate without altering the PCM data. This will result in a change of speed and pitch.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        sample_rate : int or float, optional
            Set the output sample rate. Default is 44100 Hz.

    Example usage:
    --------------
    stream.asetrate(sample_rate=48000)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asetrate
    """
    return FilterNode(
        stream,
        asetrate.__name__,
        kwargs={
            "sample_rate": sample_rate,
        },
    ).stream()
