from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def superequalizer(
    stream: Stream,
    b1: Optional[float] = None,
    b2: Optional[float] = None,
    b3: Optional[float] = None,
    b4: Optional[float] = None,
    b5: Optional[float] = None,
    b6: Optional[float] = None,
    b7: Optional[float] = None,
    b8: Optional[float] = None,
    b9: Optional[float] = None,
    b10: Optional[float] = None,
    b11: Optional[float] = None,
    b12: Optional[float] = None,
    b13: Optional[float] = None,
    b14: Optional[float] = None,
    b15: Optional[float] = None,
    b16: Optional[float] = None,
    b17: Optional[float] = None,
    b18: Optional[float] = None,
) -> Stream:
    """
    Apply 18 band equalizer.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    b1 : float, optional
        Set 65Hz band gain.
    b2 : float, optional
        Set 92Hz band gain.
    b3 : float, optional
        Set 131Hz band gain.
    b4 : float, optional
        Set 185Hz band gain.
    b5 : float, optional
        Set 262Hz band gain.
    b6 : float, optional
        Set 370Hz band gain.
    b7 : float, optional
        Set 523Hz band gain.
    b8 : float, optional
        Set 740Hz band gain.
    b9 : float, optional
        Set 1047Hz band gain.
    b10 : float, optional
        Set 1480Hz band gain.
    b11 : float, optional
        Set 2093Hz band gain.
    b12 : float, optional
        Set 2960Hz band gain.
    b13 : float, optional
        Set 4186Hz band gain.
    b14 : float, optional
        Set 5920Hz band gain.
    b15 : float, optional
        Set 8372Hz band gain.
    b16 : float, optional
        Set 11840Hz band gain.
    b17 : float, optional
        Set 16744Hz band gain.
    b18 : float, optional
        Set 20000Hz band gain.

    Example usage:
    --------------
    stream.superequalizer(
        b1=3,
        b2=-2,
        b3=1,
        b4=0,
        b5=2,
        b6=-1,
        b7=4,
        b8=-2,
        b9=3,
        b10=0,
        b11=1,
        b12=-3,
        b13=2,
        b14=-1,
        b15=0,
        b16=2,
        b17=-3,
        b18=4,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#superequalizer
    """
    return FilterNode(
        stream,
        superequalizer.__name__,
        kwargs={
            "b1": b1,
            "b2": b2,
            "b3": b3,
            "b4": b4,
            "b5": b5,
            "b6": b6,
            "b7": b7,
            "b8": b8,
            "b9": b9,
            "b10": b10,
            "b11": b11,
            "b12": b12,
            "b13": b13,
            "b14": b14,
            "b15": b15,
            "b16": b16,
            "b17": b17,
            "b18": b18,
        },
    ).stream()
