from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def atempo(
    stream: Stream,
    tempo: Optional[float] = 1.0,
) -> Stream:
    """
    Adjust audio tempo.

    The filter accepts exactly one parameter, the audio tempo. If not specified then the filter will assume nominal 1.0 tempo. Tempo must be in the [0.5, 100.0] range.

    Note that tempo greater than 2 will skip some samples rather than blend them in.  If for any reason this is a concern it is always possible to daisy-chain several instances of atempo to achieve the desired product tempo.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    tempo : float, optional
        The audio tempo. Default is 1.0. Tempo must be in the [0.5, 100.0] range.

    Returns:
    -------
    Stream:
        The output stream after applying the filter.

    Example usage:
    --------------
    stream.atempo(tempo=1.5)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#atempo
    """
    return FilterNode(stream, atempo.__name__, kwargs={"tempo": tempo}).stream()
