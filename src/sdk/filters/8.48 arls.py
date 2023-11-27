from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def arls(
    input_stream: Stream,
    desired_stream: Stream,
    order: int,
    lambda_: float,
    delta: float,
    out_mode: Literal["i", "d", "o", "n", "e"] = "o",
) -> Stream:
    """
    Apply Recursive Least Squares algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to mimic a desired filter by recursively finding the filter coefficients that relate to producing
    the minimal weighted linear least squares cost function of the error signal (difference
    between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream).

    Parameters:
    ----------
    input_stream : Stream
        The first input audio stream.
    desired_stream : Stream
        The second input audio stream (desired filter).
    order : int
        Set the filter order.
    lambda_ : float
        Set the forgetting factor.
    delta : float
        Set the coefficient to initialize internal covariance matrix.
    out_mode : str, optional
        Set the filter output samples. It can be "i" (pass the 1st input), "d" (pass the 2nd input),
        "o" (pass difference between desired, 2nd input and error signal estimate),
        "n" (pass difference between input, 1st input and error signal estimate), "e" (pass error signal
        estimated samples). Default value is "o".

    Example usage:
    --------------
    arls(input_stream, desired_stream, order=4, lambda_=0.5, delta=1.0, out_mode="o")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#arls
    """
    return FilterNode(
        input_stream,
        "arls",
        kwargs={
            "order": order,
            "lambda": lambda_,
            "delta": delta,
            "out_mode": out_mode,
        },
        inputs=[desired_stream],
    ).stream()
