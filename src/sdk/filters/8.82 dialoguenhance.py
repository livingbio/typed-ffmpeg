from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def dialoguenhance(
    stream: Stream,
    original: Optional[float] = 1.0,
    enhance: Optional[float] = 1.0,
    voice: Optional[int] = 2,
) -> Stream:
    """
    Enhance dialogue in stereo audio.

    This filter accepts stereo input and produces surround (3.0) channels output.
    The newly produced front center channel has enhanced speech dialogue originally
    available in both stereo channels. This filter outputs front left and front right
    channels same as available in stereo input.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    original : float, optional
        Set the original center factor to keep in front center channel output.
        Allowed range is from 0 to 1. Default value is 1.
    enhance : float, optional
        Set the dialogue enhance factor to put in front center channel output.
        Allowed range is from 0 to 3. Default value is 1.
    voice : int, optional
        Set the voice detection factor.
        Allowed range is from 2 to 32. Default value is 2.

    Example usage:
    --------------
    stream.dialoguenhance(original=0.5, enhance=2.5, voice=16)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance
    """
    return FilterNode(
        stream,
        dialoguenhance.__name__,
        kwargs={"original": original, "enhance": enhance, "voice": voice},
    ).stream()
