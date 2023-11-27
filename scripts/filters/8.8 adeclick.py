from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def adeclick(
    stream: Stream,
    window: float = 55,
    overlap: float = 75,
    arorder: float = 2,
    threshold: float = 2,
    burst: float = 2,
    method: str = Literal["add", "save"],
) -> Stream:
    """
    Remove impulsive noise from input audio.

    Samples detected as impulsive noise are replaced by interpolated samples using autoregressive modelling.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    window : float, optional
        Set window size, in milliseconds. Allowed range is from 10 to
        100. Default value is 55 milliseconds.
        This sets the size of the window that will be processed at once.
    overlap : float, optional
        Set window overlap, in percentage of window size. Allowed range is from
        50 to 95. Default value is 75 percent.
        Setting this to a very high value increases impulsive noise removal but makes
        the whole process much slower.
    arorder : float, optional
        Set autoregression order, in percentage of window size. Allowed range is from
        0 to 25. Default value is 2 percent. This option also
        controls the quality of interpolated samples using neighbour good samples.
    threshold : float, optional
        Set threshold value. Allowed range is from 1 to 100.
        Default value is 2.
        This controls the strength of impulsive noise which is going to be removed.
        The lower value, the more samples will be detected as impulsive noise.
    burst : float, optional
        Set burst fusion, in percentage of window size. Allowed range is 0 to
        10. Default value is 2.
        If any two samples detected as noise are spaced less than this value then any
        sample between those two samples will be also detected as noise.
    method : str, optional
        Set the overlap method.
        It accepts the following values:
            - 'add' or 'a': Select overlap-add method. Even non-interpolated samples are slightly changed.
            - 'save' or 's': Select overlap-save method. Non-interpolated samples remain unchanged.
        Default value is 'a'.

    Example usage:
    --------------
    stream.adeclick(
        window=50,
        overlap=80,
        arorder=1,
        threshold=5,
        burst=3,
        method='save',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclick
    """
    return FilterNode(
        stream,
        adeclick.__name__,
        kwargs={
            "window": window,
            "overlap": overlap,
            "arorder": arorder,
            "threshold": threshold,
            "burst": burst,
            "method": method,
        },
    ).stream()
