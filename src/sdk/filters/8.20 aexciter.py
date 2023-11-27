from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def aexciter(
    stream: Stream,
    level_in: float = 1.0,
    level_out: float = 1.0,
    amount: float = 1.0,
    drive: float = 8.5,
    blend: float = 0.0,
    freq: Optional[int] = 7500,
    ceil: Optional[int] = None,
    listen: bool = False,
) -> Stream:
    """
    An exciter is used to produce high sound that is not present in the original signal. This is done by creating harmonic distortions of the signal which are restricted in range and added to the original signal. An Exciter raises the upper end of an audio signal without simply raising the higher frequencies like an equalizer would do to create a more "crisp" or "brilliant" sound.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input level prior processing of signal.
            Allowed range is from 0 to 64.
            Default value is 1.
        level_out : float, optional
            Set output level after processing of signal.
            Allowed range is from 0 to 64.
            Default value is 1.
        amount : float, optional
            Set the amount of harmonics added to the original signal.
            Allowed range is from 0 to 64.
            Default value is 1.
        drive : float, optional
            Set the amount of newly created harmonics.
            Allowed range is from 0.1 to 10.
            Default value is 8.5.
        blend : float, optional
            Set the octave of newly created harmonics.
            Allowed range is from -10 to 10.
            Default value is 0.
        freq : int, optional
            Set the lower frequency limit of producing harmonics in Hz.
            Allowed range is from 2000 to 12000 Hz.
            Default is 7500 Hz.
        ceil : int, optional
            Set the upper frequency limit of producing harmonics.
            Allowed range is from 9999 to 20000 Hz.
            If value is lower than 10000 Hz no limit is applied.
        listen : bool, optional
            Mute the original signal and output only added harmonics.
            By default is disabled.

    Example usage:
    --------------
    stream.aexciter(
        level_in=0.8,
        level_out=1.2,
        amount=1.5,
        drive=5.5,
        blend=-4.3,
        freq=5000,
        ceil=15000,
        listen=True,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aexciter
    """
    return FilterNode(
        stream,
        aexciter.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "amount": amount,
            "drive": drive,
            "blend": blend,
            "freq": freq,
            "ceil": ceil,
            "listen": int(listen),
        },
    ).stream()
