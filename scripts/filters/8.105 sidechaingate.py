from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def sidechaingate(
    stream1: Stream,
    stream2: Stream,
    level_in: float = 1.0,
    mode: str = Literal["downward", "upward"],
    threshold: float = 0.125,
    ratio: float = 2,
    attack: float = 20,
    release: float = 250,
    makeup: float = 1,
    knee: float = 2.828427125,
    detection: str = "rms",
    link: str = "average",
    level_sc: float = 1.0,
) -> Stream:
    """
    A sidechain gate acts like a normal (wideband) gate but has the ability to
    filter the detected signal before sending it to the gain reduction stage. Normally, a gate uses the full-range signal to detect a level above the threshold. For example, if you cut all lower frequencies from your sidechain signal, the gate will decrease the volume of your track only if not enough highs appear. With this technique, you are able to reduce the resonance of a natural drum or remove "rumbling" of muted strokes from a heavily distorted guitar. It needs two input streams and returns one output stream. The first input stream will be processed depending on the second stream signal.

    The filter accepts the following options:
        Parameters:
        ----------
        stream1 : Stream
            The first input stream to filter.
        stream2 : Stream
            The second input stream to filter.
        level_in : float, optional
            Set input level before filtering. Default is 1.0. Allowed range is from 0.015625 to 64.
        mode : str, optional
            Set the mode of operation. Can be 'upward' or 'downward'. Default is 'downward'. If set to 'upward' mode, higher parts of the signal will be amplified, expanding dynamic range in the upward direction. Otherwise, in the case of 'downward', lower parts of the signal will be reduced.
        range : float, optional
            Set the level of gain reduction when the signal is below the threshold. Default is 0.06125. Allowed range is from 0 to 1. Setting this to 0 disables reduction, making the filter behave like an expander.
        threshold : float, optional
            If a signal rises above this level, the gain reduction is released. Default is 0.125. Allowed range is from 0 to 1.
        ratio : float, optional
            Set a ratio by which the signal is reduced. Default is 2. Allowed range is from 1 to 9000.
        attack : float, optional
            The amount of milliseconds the signal has to rise above the threshold before gain reduction stops. Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
        release : float, optional
            The amount of milliseconds the signal has to fall below the threshold before the reduction is increased again. Default is 250 milliseconds. Allowed range is from 0.01 to 9000.
        makeup : float, optional
            Set the amount of amplification of the signal after processing. Default is 1. Allowed range is from 1 to 64.
        knee : float, optional
            Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.828427125. Allowed range is from 1 to 8.
        detection : str, optional
            Choose if the exact signal should be taken for detection or an RMS-like one. Default is 'rms'. Can be 'peak' or 'rms'.
        link : str, optional
            Choose if the average level between all channels or the louder channel affects the reduction. Default is 'average'. Can be 'average' or 'maximum'.
        level_sc : float, optional
            Set sidechain gain. Default is 1. Range is from 0.015625 to 64.

    Example usage:
    -------------
    stream1.sidechaingate(stream2, threshold=0.2, attack=50, release=500)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaingate
    """
    return FilterNode(
        [stream1, stream2],
        sidechaingate.__name__,
        kwargs={
            "level_in": level_in,
            "mode": mode,
            "threshold": threshold,
            "ratio": ratio,
            "attack": attack,
            "release": release,
            "makeup": makeup,
            "knee": knee,
            "detection": detection,
            "link": link,
            "level_sc": level_sc,
        },
    ).stream()
