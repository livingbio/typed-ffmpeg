from typing import List

from ..node import FilterNode
from ..stream import Stream


def amultiply(stream1: Stream, stream2: Stream, outputs: int = 1) -> List[Stream]:
    """
    Multiply the first audio stream with the second audio stream and store the result in the output audio stream. Multiplication is done by multiplying each sample from the first stream with the sample at the same position from the second stream.

    With this element-wise multiplication, one can create amplitude fades and amplitude modulations.

    Parameters:
    ----------
    stream1 : Stream
        The first audio stream to multiply.
    stream2 : Stream
        The second audio stream to multiply.
    outputs : int, optional
        The number of output audio streams to create. Default is 1.

    Returns:
    -------
    List[Stream]
        The output audio stream(s) with the multiplied audio.

    Example usage:
    --------------
    stream1.amultiply(stream2, outputs=2)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amultiply
    """
    return FilterNode(stream1, amultiply.__name__, outputs=outputs).join(stream2).stream()
