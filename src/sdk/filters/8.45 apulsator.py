from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def apulsator(
    stream: Stream,
    level_in: float = 1.0,
    level_out: float = 1.0,
    mode: str = Literal["sine", "triangle", "square", "sawup", "sawdown"],
    amount: float = 1.0,
    offset_l: float = 0.0,
    offset_r: float = 0.5,
    width: float = 1.0,
    timing: str = Literal["bpm", "ms", "hz"],
    bpm: float = 120.0,
    ms: float = 500.0,
    hz: float = 2.0,
) -> Stream:
    """
    Audio pulsator is something between an autopanner and a tremolo. But it can produce funny stereo effects as well. Pulsator changes the volume of the left and right channel based on an LFO (low-frequency oscillator) with different waveforms and shifted phases. This filter has the ability to define an offset between the left and right channel. An offset of 0 means that both LFO shapes match each other. The left and right channel are altered equally - a conventional tremolo. An offset of 50% means that the shape of the right channel is exactly shifted in phase (or moved backwards about half of the frequency) - pulsator acts as an autopanner. At 1, both curves match again. Every setting in between moves the phase shift gapless between all stages and produces some "bypassing" sounds with sine and triangle waveforms. The more you set the offset near 1 (starting from the 0.5) the faster the signal passes from the left to the right speaker.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input gain. By default it is 1.0. Range is [0.015625 - 64].
        level_out : float, optional
            Set output gain. By default it is 1.0. Range is [0.015625 - 64].
        mode : str, optional
            Set waveform shape the LFO will use. Can be one of: 'sine', 'triangle', 'square', 'sawup', 'sawdown'.
            Default is 'sine'.
        amount : float, optional
            Set modulation. Define how much of the original signal is affected by the LFO.
        offset_l : float, optional
            Set left channel offset. Default is 0.0. Allowed range is [0 - 1].
        offset_r : float, optional
            Set right channel offset. Default is 0.5. Allowed range is [0 - 1].
        width : float, optional
            Set pulse width. Default is 1. Allowed range is [0 - 2].
        timing : str, optional
            Set possible timing mode. Can be one of: 'bpm', 'ms', 'hz'. Default is 'hz'.
        bpm : float, optional
            Set bpm. Default is 120. Allowed range is [30 - 300]. Only used if timing is set to 'bpm'.
        ms : float, optional
            Set ms. Default is 500. Allowed range is [10 - 2000]. Only used if timing is set to 'ms'.
        hz : float, optional
            Set frequency in Hz. Default is 2. Allowed range is [0.01 - 100]. Only used if timing is set to 'hz'.

    Example usage:
    --------------
    stream.apulsator(
        level_in=0.8,
        level_out=1.2,
        mode='sine',
        amount=0.5,
        offset_l=0.25,
        offset_r=0.75,
        width=1.5,
        timing='bpm',
        bpm=140.0,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#apulsator
    """
    return FilterNode(
        stream,
        apulsator.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "mode": mode,
            "amount": amount,
            "offset_l": offset_l,
            "offset_r": offset_r,
            "width": width,
            "timing": timing,
            "bpm": bpm,
            "ms": ms,
            "hz": hz,
        },
    ).stream()
