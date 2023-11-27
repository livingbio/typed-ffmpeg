from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def aemphasis(
    stream: Stream,
    level_in: float,
    level_out: float,
    mode: str = Literal["production", "reproduction"],
    type: str = Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"],
) -> Stream:
    """
    Audio emphasis filter creates or restores material directly taken from LPs or emphased CDs with different filter curves. E.g. to store music on vinyl the signal has to be altered by a filter first to even out the disadvantages of this recording medium. Once the material is played back the inverse filter has to be applied to restore the distortion of the frequency response.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float
            Set input gain.
        level_out : float
            Set output gain.
        mode : str, optional
            Set filter mode. For restoring material use 'reproduction' mode, otherwise
            use 'production' mode. Default is 'reproduction' mode.
        type : str, optional
            Set filter type. Selects medium. Can be one of the following:
                - 'col': select Columbia.
                - 'emi': select EMI.
                - 'bsi': select BSI (78RPM).
                - 'riaa': select RIAA.
                - 'cd': select Compact Disc (CD).
                - '50fm': select 50µs (FM).
                - '75fm': select 75µs (FM).
                - '50kf': select 50µs (FM-KF).
                - '75kf': select 75µs (FM-KF).

    Example usage:
    --------------
    stream.aemphasis(
        level_in=0.5,
        level_out=1.0,
        mode='production',
        type='riaa',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aemphasis
    """
    return FilterNode(
        stream,
        aemphasis.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "mode": mode,
            "type": type,
        },
    ).stream()
