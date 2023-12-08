from ..node import FilterNode
from ..stream import Stream


def acopy(stream: Stream) -> Stream:
    """
    Copy the input audio source unchanged to the output. This is mainly useful for testing purposes.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.

    Example usage:
    --------------
    stream.acopy()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acopy
    """
    return FilterNode(stream, acopy.__name__).stream()
