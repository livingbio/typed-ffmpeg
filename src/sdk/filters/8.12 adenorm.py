from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def adenorm(stream: Stream, level: float = -351, type: str = Literal["dc", "ac", "square", "pulse"]) -> Stream:
    """
    Remedy denormals in audio by adding extremely low-level noise.

    This filter shall be placed before any filter that can produce denormals.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level : float, optional
            Set level of added noise in dB. Default is -351. Allowed range is from -451 to -90.
        type : str, optional
            Set type of added noise.
                - 'dc'   : Add DC signal.
                - 'ac'   : Add AC signal.
                - 'square'   : Add square signal.
                - 'pulse'   : Add pulse signal.
            Default is 'dc'.

    Example usage:
    --------------
    stream.adenorm(level=-400, type='ac')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adenorm
    """
    return FilterNode(stream, adenorm.__name__, kwargs={"level": level, "type": type}).stream()
