from typing import List

from ..node import FilterNode
from ..stream import Stream


def chorus(
    stream: Stream,
    in_gain: float = 0.4,
    out_gain: float = 0.4,
    delays: List[float],
    decays: List[float],
    speeds: List[float],
    depths: List[float],
) -> Stream:
    """
    Add a chorus effect to the audio.

    Can make a single vocal sound like a chorus, but can also be applied to instrumentation.

    Chorus resembles an echo effect with a short delay, but whereas with echo the delay is constant, with chorus, it is varied using sinusoidal or triangular modulation. The modulation depth defines the range the modulated delay is played before or after the delay. Hence the delayed sound will sound slower or faster, that is the delayed sound tuned around the original one, like in a chorus where some vocals are slightly off key.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    in_gain : float, optional
        Set input gain. Default is 0.4.
    out_gain : float, optional
        Set output gain. Default is 0.4.
    delays : List[float]
        Set delays. A typical delay is around 40ms to 60ms.
    decays : List[float]
        Set decays.
    speeds : List[float]
        Set speeds.
    depths : List[float]
        Set depths.

    Example usage:
    --------------
    stream.chorus(
        in_gain=0.3,
        out_gain=0.5,
        delays=[30, 40, 50],
        decays=[0.3, 0.4, 0.5],
        speeds=[0.4, 0.5, 0.6],
        depths=[0.3, 0.4, 0.5],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#chorus
    """
    return FilterNode(
        stream,
        chorus.__name__,
        kwargs={
            "in_gain": in_gain,
            "out_gain": out_gain,
            "delays": delays,
            "decays": decays,
            "speeds": speeds,
            "depths": depths,
        },
    ).stream()
