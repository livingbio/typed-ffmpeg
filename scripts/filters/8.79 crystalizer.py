from typing import Union

from ..node import FilterNode
from ..stream import Stream


def crystalizer(
    stream: Stream,
    intensity: Union[float, int] = 2.0,
    clipping: bool = True,
) -> Stream:
    """
    Simple algorithm for audio noise sharpening.

    This filter linearly increases differences between each audio sample.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        intensity : Union[float, int], optional
            Sets the intensity of effect (default: 2.0). Must be in range between -10.0 to 0
            (unchanged sound) to 10.0 (maximum effect).
            To inverse filtering use negative value.
        clipping : bool, optional
            Enable clipping. By default is enabled.

    Example usage:
    --------------
    stream.crystalizer(
        intensity=1.5,
        clipping=False,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#crystalizer
    """
    return FilterNode(
        stream,
        crystalizer.__name__,
        kwargs={
            "i": intensity,
            "c": int(clipping),
        },
    ).stream()
