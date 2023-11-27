from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def alimiter(
    stream: Stream,
    level_in: Optional[float] = None,
    level_out: Optional[float] = None,
    limit: Optional[float] = None,
    attack: Optional[float] = None,
    release: Optional[float] = None,
    asc: Optional[bool] = None,
    asc_level: Optional[float] = None,
    level: Optional[bool] = None,
    latency: Optional[float] = None,
) -> Stream:
    """
    The limiter prevents an input signal from rising over a desired threshold. This limiter uses lookahead technology to prevent your signal from distorting. It means that there is a small delay after the signal is processed. Keep in mind that the delay it produces is the attack time you set.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input gain. Default is 1.
        level_out : float, optional
            Set output gain. Default is 1.
        limit : float, optional
            Don’t let signals above this level pass the limiter. Default is 1.
        attack : float, optional
            The limiter will reach its attenuation level in this amount of time in milliseconds. Default is 5 milliseconds.
        release : float, optional
            Come back from limiting to attenuation 1.0 in this amount of milliseconds. Default is 50 milliseconds.
        asc : bool, optional
            When gain reduction is always needed ASC takes care of releasing to an average reduction level rather than reaching a reduction of 0 in the release time.
        asc_level : float, optional
            Select how much the release time is affected by ASC, 0 means nearly no changes in release time while 1 produces higher release times.
        level : bool, optional
            Auto level output signal. Default is enabled. This normalizes audio back to 0dB if enabled.
        latency : float, optional
            Compensate the delay introduced by using the lookahead buffer set with the attack parameter. Also flush the valid audio data in the lookahead buffer when the stream hits EOF.

    Example usage:
    --------------
    stream.alimiter(
        limit=0.5,
        attack=10,
        release=100,
        level=True,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#alimiter
    """
    return FilterNode(
        stream,
        alimiter.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "limit": limit,
            "attack": attack,
            "release": release,
            "asc": asc,
            "asc_level": asc_level,
            "level": level,
            "latency": latency,
        },
    ).stream()
