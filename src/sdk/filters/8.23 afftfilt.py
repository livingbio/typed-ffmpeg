from typing import List

from ..node import FilterNode
from ..stream import Stream


def afftfilt(
    stream: Stream,
    real: List[str] = ["re"],
    imag: List[str] = ["im"],
    win_size: int = 4096,
    win_func: str = "hann",
    overlap: float = 0.75,
) -> Stream:
    """
    Apply arbitrary expressions to samples in frequency domain.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    real : List[str], optional
        Set frequency domain real expression for each separate channel separated by '|'.
        Default is ['re'].
    imag : List[str], optional
        Set frequency domain imaginary expression for each separate channel separated by '|'.
        Default is ['im'].
    win_size : int, optional
        Set window size. Allowed range is from 16 to 131072.
        Default is 4096.
    win_func : str, optional
        Set window function.
        It accepts the following values:
        'rect', 'bartlett', 'hann, hanning', 'hamming', 'blackman', 'welch', 'flattop',
        'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey',
        'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser'.
        Default is 'hann'.
    overlap : float, optional
        Set window overlap. If set to 1, the recommended overlap for the selected window function will be picked.
        Default is 0.75.

    Example usage:
    --------------
    stream.afftfilt(
        real=["re", "re*b - im*a"],
        imag=["im", "im*a + re*b"],
        win_size=1024,
        win_func="hann",
        overlap=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afftfilt
    """
    return FilterNode(
        stream,
        afftfilt.__name__,
        kwargs={
            "real": "|".join(real),
            "imag": "|".join(imag),
            "win_size": win_size,
            "win_func": win_func,
            "overlap": overlap,
        },
    ).stream()
