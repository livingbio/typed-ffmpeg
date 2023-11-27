from ..node import FilterNode
from ..stream import Stream


def apsnr(
    stream1: Stream,
    stream2: Stream,
) -> Stream:
    """
    Measure Audio Peak Signal-to-Noise Ratio.

    This filter takes two audio streams for input and outputs the first audio stream. Results are in dB per channel at the end of either input.

    Parameters:
    ----------
    stream1 : Stream
        The first input stream.
    stream2 : Stream
        The second input stream.

    Returns:
    -------
    Stream
        The output stream.

    Example usage:
    --------------
    stream1.apsnr(stream2)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#apsnr
    """
    return FilterNode(stream1, "apsnr", inputs=[stream2]).stream()
