from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def aspectralstats(
    stream: Stream,
    win_size: int = 2048,
    win_func: str = Literal[
        "rect",
        "bartlett",
        "hann",
        "hamming",
        "blackman",
        "welch",
        "flattop",
        "bharris",
        "bnuttall",
        "bhann",
        "sine",
        "nuttall",
        "lanczos",
        "gauss",
        "tukey",
        "dolph",
        "cauchy",
        "parzen",
        "poisson",
        "bohman",
        "kaiser",
    ],
    overlap: float = 0.5,
    measure: str = "all",
) -> Stream:
    """
    Display frequency domain statistical information about the audio channels.
    Statistics are calculated and stored as metadata for each audio channel and for each audio frame.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    win_size : int, optional
        Set the window length in samples. Default value is 2048.
        Allowed range is from 32 to 65536.
    win_func : str, optional
        Set window function.
        It accepts the following values:
        'rect', 'bartlett', 'hann', 'hamming', 'blackman', 'welch', 'flattop',
        'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss',
        'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser'.
        Default is 'hann'.
    overlap : float, optional
        Set window overlap. Allowed range is from 0 to 1. Default value is 0.5.
    measure : str, optional
        Select the parameters which are measured. The metadata keys can
        be used as flags, default is 'all' which measures everything.
        'none' disables all measurement.

    Returns:
    -------
    Stream
        The filtered stream.

    Example usage:
    --------------
    stream.aspectralstats(win_size=4096, overlap=0.8, measure='mean variance slope')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aspectralstats
    """
    return FilterNode(
        stream,
        aspectralstats.__name__,
        kwargs={
            "win_size": win_size,
            "win_func": win_func,
            "overlap": overlap,
            "measure": measure,
        },
    ).stream()
