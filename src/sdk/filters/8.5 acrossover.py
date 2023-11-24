from typing import List, Literal, Union

from ..node import FilterNode
from ..stream import Stream


def acrossover(
    stream: Stream,
    split: Union[float, List[float]],
    order: Literal["2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"] = "4th",
    level: float = 1,
    gains: Union[float, List[float]] = 1,
    precision: Literal["auto", "float", "double"] = "auto",
) -> Stream:
    """
    Split audio stream into several bands.

    This filter splits audio stream into two or more frequency ranges. Summing all streams back will give flat output.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        split : float or List[float]
            Set split frequencies. Those must be positive and increasing.
        order : str, optional
            Set filter order for each band split. This controls filter roll-off or steepness
            of filter transfer function. Available values are:
            - '2nd': 12 dB per octave.
            - '4th': 24 dB per octave.
            - '6th': 36 dB per octave.
            - '8th': 48 dB per octave.
            - '10th': 60 dB per octave.
            - '12th': 72 dB per octave.
            - '14th': 84 dB per octave.
            - '16th': 96 dB per octave.
            - '18th': 108 dB per octave.
            - '20th': 120 dB per octave.
            Default is '4th'.
        level : float, optional
            Set input gain level. Allowed range is from 0 to 1. Default value is 1.
        gains : float or List[float], optional
            Set output gain for each band. Default value is 1 for all bands.
        precision : str, optional
            Set which precision to use when processing samples.
            - 'auto': Auto pick internal sample format depending on other filters.
            - 'float': Always use single-floating point precision sample format.
            - 'double': Always use double-floating point precision sample format.
            Default value is 'auto'.

    Example usage:
    --------------
    stream.acrossover(split=[200, 2000], order='6th')

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
    ).stream()
