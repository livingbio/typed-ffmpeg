from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def anlmf(
    stream1: Stream,
    stream2: Stream,
    order: int,
    mu: float,
    eps: float,
    leakage: float,
    out_mode: str = Literal["i", "d", "o", "n", "e"],
) -> Stream:
    """
    Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to mimic a desired filter by finding the filter coefficients that relate to producing the least mean square of the error signal (difference between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream).

    Parameters:
    ----------
    stream1 : Stream
        The first input audio stream.
    stream2 : Stream
        The second input audio stream.
    order : int
        Set filter order.
    mu : float
        Set filter mu.
    eps : float
        Set the filter eps.
    leakage : float
        Set the filter leakage.
    out_mode : str, optional
        It accepts the following values:
        - 'i': Pass the 1st input.
        - 'd': Pass the 2nd input.
        - 'o': Pass difference between desired, 2nd input and error signal estimate.
        - 'n': Pass difference between input, 1st input and error signal estimate.
        - 'e': Pass error signal estimated samples.
        Default value is 'o'.

    Returns:
    -------
    Stream
        The filtered audio stream.

    Example usage:
    --------------
    stream1.anlmf(
        stream2,
        order=10,
        mu=0.01,
        eps=0.001,
        leakage=1,
        out_mode='o',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms
    """
    return FilterNode(
        stream1,
        "anlmf",
        inputs=[stream2],
        kwargs={
            "order": order,
            "mu": mu,
            "eps": eps,
            "leakage": leakage,
            "out_mode": out_mode,
        },
    ).stream()
