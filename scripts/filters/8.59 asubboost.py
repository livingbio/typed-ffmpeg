from typing import Optional, Tuple

from ..node import FilterNode
from ..stream import Stream


def asubboost(
    stream: Stream,
    dry: Optional[float] = 1.0,
    wet: Optional[float] = 1.0,
    boost: Optional[float] = 2.0,
    decay: Optional[float] = 0.0,
    feedback: Optional[float] = 0.9,
    cutoff: Optional[float] = 100.0,
    slope: Optional[float] = 0.5,
    delay: Optional[float] = 20.0,
    channels: Optional[Tuple[int, ...]] = None,
) -> Stream:
    """
    Boost subwoofer frequencies.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        dry : float, optional
            Set dry gain, how much of the original signal is kept.
            Allowed range is from 0 to 1. Default value is 1.0.
        wet : float, optional
            Set wet gain, how much of the filtered signal is kept.
            Allowed range is from 0 to 1. Default value is 1.0.
        boost : float, optional
            Set max boost factor. Allowed range is from 1 to 12. Default value is 2.
        decay : float, optional
            Set delay line decay gain value. Allowed range is from 0 to 1.
            Default value is 0.0.
        feedback : float, optional
            Set delay line feedback gain value. Allowed range is from 0 to 1.
            Default value is 0.9.
        cutoff : float, optional
            Set cutoff frequency in Hertz. Allowed range is from 50 to 900.
            Default value is 100.
        slope : float, optional
            Set slope amount for the cutoff frequency. Allowed range is from 0.0001 to 1.
            Default value is 0.5.
        delay : float, optional
            Set delay. Allowed range is from 1 to 100.
            Default value is 20.
        channels : tuple of int, optional
            Set the channels to process. Default value is all available.

    Example usage:
    --------------
    stream.asubboost(
        dry=0.5,
        wet=0.7,
        boost=3,
        cutoff=200,
        channels=(0, 1),
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asubboost
    """
    return FilterNode(
        stream,
        asubboost.__name__,
        kwargs={
            "dry": dry,
            "wet": wet,
            "boost": boost,
            "decay": decay,
            "feedback": feedback,
            "cutoff": cutoff,
            "slope": slope,
            "delay": delay,
            "channels": channels,
        },
    ).stream()
