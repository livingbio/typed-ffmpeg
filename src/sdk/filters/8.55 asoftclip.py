from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def asoftclip(
    stream: Stream,
    type: str = Literal[
        "hard",
        "tanh",
        "atan",
        "cubic",
        "exp",
        "alg",
        "quintic",
        "sin",
        "erf",
    ],
    threshold: float = 1,
    output: float = 1,
    param: float = 0,
    oversample: int = 1,
) -> Stream:
    """
    Apply audio soft clipping.

    Soft clipping is a type of distortion effect where the amplitude of a signal is saturated along a smooth curve, rather than the abrupt shape of hard-clipping.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    type : str, optional
        Set type of soft-clipping. Default is 'hard'. It accepts the following values:
            - 'hard'
            - 'tanh'
            - 'atan'
            - 'cubic'
            - 'exp'
            - 'alg'
            - 'quintic'
            - 'sin'
            - 'erf'
    threshold : float, optional
        Set threshold from where to start clipping. Default value is 1.
    output : float, optional
        Set gain applied to output. Default value is 1.
    param : float, optional
        Set additional parameter which controls sigmoid function.
    oversample : int, optional
        Set oversampling factor. Default value is 1.

    Example usage:
    --------------
    stream.asoftclip(
        type='tanh',
        threshold=0.8,
        output=0.5,
        oversample=2,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asoftclip
    """
    return FilterNode(
        stream,
        asoftclip.__name__,
        kwargs={
            "type": type,
            "threshold": threshold,
            "output": output,
            "param": param,
            "oversample": oversample,
        },
    ).stream()
