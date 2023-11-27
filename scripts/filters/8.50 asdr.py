from typing import Union

from ..node import FilterNode
from ..stream import Stream


def asdr(
    input1: Union[Stream, str] = "[in1]",
    input2: Union[Stream, str] = "[in2]",
) -> Stream:
    """
    Measure Audio Signal-to-Distortion Ratio.

    This filter takes two audio streams for input and outputs the first
    audio stream. Results are in dB per channel at the end of either input.

    Parameters:
    ----------
    input1 : Union[Stream, str], optional
        The first input stream. Default is "[in1]".
    input2 : Union[Stream, str], optional
        The second input stream. Default is "[in2]".

    Returns:
    -------
    Stream
        The output audio stream.

    Example usage:
    --------------
    stream.asdr()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asdr
    """
    return FilterNode(
        input1 if isinstance(input1, Stream) else Stream(input1),
        asdr.__name__,
        kwargs={"input2": input2},
    ).stream()
