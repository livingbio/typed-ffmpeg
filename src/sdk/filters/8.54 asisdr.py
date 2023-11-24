from ..node import FilterNode
from ..stream import Stream


def asisdr(stream1: Stream, stream2: Stream) -> Stream:
    """
    Measure Audio Scaled-Invariant Signal-to-Distortion Ratio.

    This filter takes two audio streams for input, and outputs first audio stream.
    Results are in dB per channel at end of either input.

    Parameters:
    ----------
    stream1 : Stream
        The first input stream.
    stream2 : Stream
        The second input stream.

    Returns:
    --------
    Stream
        The processed stream.

    Example usage:
    --------------
    stream1.asisdr(stream2)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asisdr
    """
    return FilterNode(stream1, "asisdr", input2=stream2).stream()
