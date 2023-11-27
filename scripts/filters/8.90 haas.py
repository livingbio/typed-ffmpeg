from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def haas(
    stream: Stream,
    level_in: float = 1,
    level_out: float = 1,
    side_gain: float = 1,
    middle_source: str = Literal["left", "right", "mid", "side"],
    middle_phase: bool = False,
    left_delay: float = 2.05,
    left_balance: float = -1,
    left_gain: float = 1,
    left_phase: bool = False,
    right_delay: float = 2.12,
    right_balance: float = 1,
    right_gain: float = 1,
    right_phase: bool = True,
) -> Stream:
    """
    Apply Haas effect to audio.

    Note that this makes most sense to apply on mono signals.
    With this filter applied to mono signals, it gives some directionality and
    stretches its stereo image.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input level. By default is 1, or 0dB.
        level_out : float, optional
            Set output level. By default is 1, or 0dB.
        side_gain : float, optional
            Set gain applied to side part of the signal. By default is 1.
        middle_source : str, optional
            Set kind of middle source. Can be one of the following:
                - 'left': Pick left channel.
                - 'right': Pick right channel.
                - 'mid': Pick middle part signal of stereo image.
                - 'side': Pick side part signal of stereo image.
            Default is 'left'.
        middle_phase : bool, optional
            Change middle phase. By default is disabled.
        left_delay : float, optional
            Set left channel delay. By default is 2.05 milliseconds.
        left_balance : float, optional
            Set left channel balance. By default is -1.
        left_gain : float, optional
            Set left channel gain. By default is 1.
        left_phase : bool, optional
            Change left phase. By default is disabled.
        right_delay : float, optional
            Set right channel delay. By defaults is 2.12 milliseconds.
        right_balance : float, optional
            Set right channel balance. By default is 1.
        right_gain : float, optional
            Set right channel gain. By default is 1.
        right_phase : bool, optional
            Change right phase. By default is enabled.

    Example usage:
    --------------
    stream.haas(
        middle_source="mid",
        left_delay=2.5,
        right_delay=2.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#haas
    """
    return FilterNode(
        stream,
        haas.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "side_gain": side_gain,
            "middle_source": middle_source,
            "middle_phase": middle_phase,
            "left_delay": left_delay,
            "left_balance": left_balance,
            "left_gain": left_gain,
            "left_phase": left_phase,
            "right_delay": right_delay,
            "right_balance": right_balance,
            "right_gain": right_gain,
            "right_phase": right_phase,
        },
    ).stream()
