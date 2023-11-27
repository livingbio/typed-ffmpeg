from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def areverse(
    stream: Stream,
    duration: Optional[float] = None,
) -> Stream:
    """
    Reverse an audio clip.

    Warning: This filter requires memory to buffer the entire clip, so trimming
    is suggested.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    duration : float, optional
        Specify the duration of the resulting reversed clip.
        Default is None, which means the duration will be the same as the input stream.

    Example usage:
    --------------
    stream.areverse(duration=10)

    Returns:
    -------
    Stream
        The resulting reversed audio stream.
    """
    return FilterNode(stream, areverse.__name__, kwargs={"duration": duration}).stream()
