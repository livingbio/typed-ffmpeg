from typing import Union

from ..node import FilterNode
from ..stream import Stream


def virtualbass(
    stream: Stream,
    cutoff: int = 250,
    strength: Union[int, float] = 3,
) -> Stream:
    """
    Apply audio Virtual Bass filter.

    This filter accepts stereo input and produce stereo with LFE (2.1) channels output.
    The newly produced LFE channel have enhanced virtual bass originally obtained from both stereo channels.
    This filter outputs front left and front right channels unchanged as available in stereo input.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    cutoff : int, optional
        Set the virtual bass cutoff frequency. Default value is 250 Hz.
        Allowed range is from 100 to 500 Hz.
    strength : int or float, optional
        Set the virtual bass strength. Allowed range is from 0.5 to 3.
        Default value is 3.

    Example usage:
    --------------
    stream.virtualbass(
        cutoff=200,
        strength=2.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#virtualbass
    """
    return FilterNode(
        stream,
        virtualbass.__name__,
        kwargs={
            "cutoff": cutoff,
            "strength": strength,
        },
    ).stream()
