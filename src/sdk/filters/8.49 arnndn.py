from typing import Union

from ..node import FilterNode
from ..stream import Stream


def arnndn(
    stream: Stream,
    model: str,
    mix: Union[float, int] = 1,
) -> Stream:
    """
    Reduce noise from speech using Recurrent Neural Networks.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    model : str
        Set train model file to load. This option is always required.
    mix : Union[float, int], optional
        Set how much to mix filtered samples into the final output.
        Allowed range is from -1 to 1. Default value is 1.
        Negative values are special, they set how much to keep filtered noise
        in the final filter output. Set this option to -1 to hear actual
        noise removed from the input signal.

    Example usage:
    --------------
    stream.arnndn(
        model="model_file",
        mix=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#arnndn
    """
    return FilterNode(
        stream,
        arnndn.__name__,
        kwargs={
            "model": model,
            "mix": mix,
        },
    ).stream()
