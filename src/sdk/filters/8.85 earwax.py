from typing import Union

from ..node import FilterNode
from ..stream import Stream


def earwax(
    stream: Stream,
    amount: Union[float, None] = None,
) -> Stream:
    """
    Make audio easier to listen to on headphones.

    This filter adds 'cues' to 44.1kHz stereo (i.e. audio CD format) audio so that when listened to on headphones the stereo image is moved from inside your head (standard for headphones) to outside and in front of the listener (standard for speakers).

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    amount : float, optional
        Adjust the effect by increasing or decreasing the strength of the psychoacoustic effect.
        Range is between -10 and 10.
        Default is None.

    Example usage:
    --------------
    stream.earwax()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#earwax
    """
    return FilterNode(stream, earwax.__name__, kwargs={"amount": amount}).stream()
