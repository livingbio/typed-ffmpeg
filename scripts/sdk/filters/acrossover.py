from typing import List, Literal, Union

from ..node import FilterNode
from ..stream import Stream


def acrossover(
    stream: Stream,
    split: List[Union[float, Literal["auto"]]],
    *,
    order: Literal[
        "2nd",
        "4th",
        "6th",
        "8th",
        "10th",
        "12th",
        "14th",
        "16th",
        "18th",
        "20th",
    ] = "4th",
    level: float = 1.0,
    gains: List[float] = [1.0],
    precision: Literal["auto", "float", "double"] = "auto",
) -> List[Stream]:
    """
    Split audio stream into several bands.

    This filter splits audio stream into two or more frequency ranges.
    Summing all streams back will give flat output.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    split : List[Union[float, Literal["auto"]]]
        Set split frequencies. Those must be positive and increasing.
    order : str, optional
        Set filter order for each band split. This controls filter roll-off or steepness
        of filter transfer function.
        Default is '4th'.
    level : float, optional
        Set input gain level. Allowed range is from 0 to 1. Default value is 1.
    gains : List[float], optional
        Set output gain for each band. Default value is 1 for all bands.
    precision : str, optional
        Set which precision to use when processing samples.
        Default value is 'auto'.

    Returns:
    -------
    List[Stream]
        List of output streams, each representing a band.

    Example usage:
    --------------
    stream.acrossover(
        split=[500, 2000, 8000],
        order="6th",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossover
    """
    return FilterNode(
        stream,
        acrossover.__name__,
        kwargs={
            "split": split,
            "order": order,
            "level": level,
            "gains": gains,
            "precision": precision,
        },
        is_complex=True,
    ).split_outputs()
