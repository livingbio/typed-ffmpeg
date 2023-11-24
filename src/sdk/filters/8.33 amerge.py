from typing import Union

from ..node import FilterNode
from ..stream import Stream


def amerge(
    *streams: Union[Stream, int],
    inputs: Union[int, str] = 2,
) -> Stream:
    """
    Merge two or more audio streams into a single multi-channel stream.

    Parameters:
    ----------
    streams : Union[Stream, int]
        The input streams to merge.
    inputs : Union[int, str], optional
        Set the number of inputs. Default is 2.

    Returns:
    -------
    Stream
        The output merged stream.

    Example usage:
    --------------
    stream1 = Stream("audio1.wav")
    stream2 = Stream("audio2.wav")

    amerge(stream1, stream2, inputs=2)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amerge
    """
    return FilterNode(streams, amerge.__name__, kwargs={"inputs": inputs}).stream()
