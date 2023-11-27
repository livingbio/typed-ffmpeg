from typing import List

from ..node import FilterNode
from ..stream import Stream


def anequalizer(
    stream: Stream,
    params: str,
    curves: bool = False,
    size: str = "",
    mgain: float = 0,
    fscale: str = "logarithmic",
    colors: List[str] = [],
) -> Stream:
    """
    High-order parametric multiband equalizer for each channel.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    params : str
        Equalizer parameters. This option string is in the format:
        "c<chn> f=<cf> w=<w> g=<g> t=<f> | ...".
        Each equalizer band is separated by '|'.
    curves : bool, optional
        With this option activated, the frequency response of the equalizer is displayed
        in the video stream. Default is False.
    size : str, optional
        Set video stream size. Only useful if curves option is activated. Default is empty.
    mgain : float, optional
        Set the maximum gain that will be displayed. Only useful if curves option is activated.
        Setting this to a reasonable value makes it possible to display gain which is derived from
        neighbour bands which are too close to each other and thus produce higher gain
        when both are activated. Default is 0.
    fscale : str, optional
        Set the frequency scale used to draw the frequency response in the video output.
        Can be 'linear' or 'logarithmic'. Default is 'logarithmic'.
    colors : List[str], optional
        Set the color for each channel curve which is going to be displayed in the video stream.
        This is a list of color names separated by space or by '|'.
        Unrecognized or missing colors will be replaced by white color. Default is an empty list.

    Example usage:
    --------------
    stream.anequalizer(
        params="c0 f=1000 w=200 g=3 t=0 | c0 f=5000 w=500 g=6 t=1",
        curves=True,
        size="1920x1080",
        mgain=6,
        fscale="logarithmic",
        colors=["red", "green"]
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anequalizer
    """
    return FilterNode(
        stream,
        anequalizer.__name__,
        kwargs={
            "params": params,
            "curves": curves,
            "size": size,
            "mgain": mgain,
            "fscale": fscale,
            "colors": colors,
        },
    ).stream()
