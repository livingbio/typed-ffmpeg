from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def aap(
    stream1: Stream,
    stream2: Stream,
    order: int,
    projection: int,
    mu: float,
    delta: float,
    out_mode: Literal["i", "d", "o", "n", "e"] = "o",
    precision: Literal["auto", "float", "double"] = "auto",
) -> Stream:
    """
    Apply Affine Projection algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to estimate unknown audio based on multiple input audio samples.
    Affine projection algorithm can make trade-offs between computation complexity with convergence speed.

    The filter accepts the following options:
        Parameters:
        ----------
        stream1 : Stream
            The first input audio stream.
        stream2 : Stream
            The second input audio stream.
        order : int
            Set the filter order.
        projection : int
            Set the projection order.
        mu : float
            Set the filter mu.
        delta : float
            Set the coefficient to initialize internal covariance matrix.
        out_mode : str, optional
            Set the filter output samples. It accepts the following values:
                - 'i': Pass the 1st input.
                - 'd': Pass the 2nd input.
                - 'o': Pass difference between desired, 2nd input and error signal estimate.
                - 'n': Pass difference between input, 1st input and error signal estimate.
                - 'e': Pass error signal estimated samples.
            Default value is 'o'.
        precision : str, optional
            Set which precision to use when processing samples. It accepts the following values:
                - 'auto': Auto pick internal sample format depending on other filters.
                - 'float': Always use single-floating point precision sample format.
                - 'double': Always use double-floating point precision sample format.

    Example usage:
    --------------
    stream1.aap(
        stream2,
        order=10,
        projection=5,
        mu=0.1,
        delta=0.01,
        out_mode='e',
        precision='auto',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aap
    """
    return FilterNode(
        [stream1, stream2],
        aap.__name__,
        kwargs={
            "order": order,
            "projection": projection,
            "mu": mu,
            "delta": delta,
            "out_mode": out_mode,
            "precision": precision,
        },
    ).stream()
