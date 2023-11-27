from typing import List

from ..node import FilterNode
from ..stream import Stream


def aecho(
    stream: Stream,
    in_gain: float = 0.6,
    out_gain: float = 0.3,
    delays: List[float] = [1000],
    decays: List[float] = [0.5],
) -> Stream:
    """
    Apply echoing to the input audio.

    Echoes are reflected sound and can occur naturally amongst mountains (and sometimes large buildings) when talking or shouting; digital echo effects emulate this behaviour and are often used to help fill out the sound of a single instrument or vocal. The time difference between the original signal and the reflection is the delay, and the loudness of the reflected signal is the decay. Multiple echoes can have different delays and decays.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    in_gain : float, optional
        Set input gain of reflected signal. Default is 0.6.
    out_gain : float, optional
        Set output gain of reflected signal. Default is 0.3.
    delays : List[float], optional
        Set list of time intervals in milliseconds between original signal and reflections separated by '|'. Allowed range for each delay is (0 - 90000.0]. Default is [1000].
    decays : List[float], optional
        Set list of loudness of reflected signals separated by '|'. Allowed range for each decay is (0 - 1.0]. Default is [0.5].

    Example usage:
    --------------
    stream.aecho(
        in_gain=0.8,
        out_gain=0.5,
        delays=[1000, 2000, 3000],
        decays=[0.5, 0.3, 0.1],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aecho
    """
    return FilterNode(
        stream,
        aecho.__name__,
        kwargs={
            "in_gain": in_gain,
            "out_gain": out_gain,
            "delays": "|".join(str(delay) for delay in delays),
            "decays": "|".join(str(decay) for decay in decays),
        },
    ).stream()
