from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def adeclip(
    stream: Stream,
    window: int = 55,
    overlap: int = 75,
    arorder: int = 8,
    threshold: int = 10,
    hsize: int = 1000,
    method: str = Literal["add", "save"],
) -> Stream:
    """
    Remove clipped samples from input audio.

    Samples detected as clipped are replaced by interpolated samples using autoregressive modelling.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    window : int, optional
        Set window size, in milliseconds. Allowed range is from 10 to 100.
        Default value is 55 milliseconds.
        This sets the size of the window which will be processed at once.
    overlap : int, optional
        Set window overlap, in percentage of window size. Allowed range is from 50 to 95.
        Default value is 75 percent.
    arorder : int, optional
        Set autoregression order, in percentage of window size. Allowed range is from 0 to 25.
        Default value is 8 percent. This option also controls the quality of interpolated samples using good samples from the neighbor.
    threshold : int, optional
        Set the threshold value. Allowed range is from 1 to 100.
        Default value is 10. Higher values make clip detection less aggressive.
    hsize : int, optional
        Set the size of the histogram used to detect clips. Allowed range is from 100 to 9999.
        Default value is 1000. Higher values make clip detection less aggressive.
    method : str, optional
        Set the overlap method.
        It accepts the following values:
            - 'add' or 'a': Select overlap-add method. Even not interpolated samples are slightly changed with this method.
            - 'save' or 's': Select overlap-save method. Not interpolated samples remain unchanged.
        Default value is 'a'.

    Example usage:
    --------------
    stream.adeclip(
        window=50,
        overlap=80,
        arorder=10,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclip
    """
    return FilterNode(
        stream,
        adeclip.__name__,
        kwargs={
            "window": window,
            "overlap": overlap,
            "arorder": arorder,
            "threshold": threshold,
            "hsize": hsize,
            "method": method,
        },
    ).stream()
