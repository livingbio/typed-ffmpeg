from ..node import FilterNode
from ..stream import Stream


def aderivative(stream: Stream) -> Stream:
    """
    Compute the derivative of an audio stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to compute the derivative of.

    Returns:
    -------
    Stream
        The resulting stream after computing the derivative.

    Example usage:
    --------------
    stream.aderivative()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative-1
    """
    return FilterNode(stream, aderivative.__name__).stream()


def aintegral(stream: Stream) -> Stream:
    """
    Compute the integral of an audio stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to compute the integral of.

    Returns:
    -------
    Stream
        The resulting stream after computing the integral.

    Example usage:
    --------------
    stream.aintegral()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aintegral-1
    """
    return FilterNode(stream, aintegral.__name__).stream()
