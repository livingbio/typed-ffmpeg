from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def acompressor(
    stream: Stream,
    level_in: float = 1.0,
    mode: str = Literal["downward", "upward"],
    threshold: float = 0.125,
    ratio: float = 2,
    attack: float = 20,
    release: float = 250,
    makeup: float = 1,
    knee: float = 2.82843,
    link: str = "average",
    detection: str = "rms",
    mix: float = 1,
) -> Stream:
    """
    A compressor is mainly used to reduce the dynamic range of a signal. Especially modern music is mostly compressed at a high ratio to improve the overall loudness. It’s done to get the highest attention of a listener, "fatten" the sound and bring more "power" to the track. If a signal is compressed too much it may sound dull or "dead" afterwards or it may start to "pump" (which could be a powerful effect but can also destroy a track completely). The right compression is the key to reach a professional sound and is the high art of mixing and mastering. Because of its complex settings it may take a long time to get the right feeling for this kind of effect.

    Compression is done by detecting the volume above a chosen level threshold and dividing it by the factor set with ratio. So if you set the threshold to -12dB and your signal reaches -6dB a ratio of 2:1 will result in a signal at -9dB. Because an exact manipulation of the signal would cause distortion of the waveform the reduction can be levelled over the time. This is done by setting "Attack" and "Release". attack determines how long the signal has to rise above the threshold before any reduction will occur and release sets the time the signal has to fall below the threshold to reduce the reduction again. Shorter signals than the chosen attack time will be left untouched. The overall reduction of the signal can be made up afterwards with the makeup setting. So compressing the peaks of a signal about 6dB and raising the makeup to this level results in a signal twice as loud than the source. To gain a softer entry in the compression the knee flattens the hard edge at the threshold in the range of the chosen decibels.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input gain. Default is 1.0. Range is between 0.015625 and 64.
        mode : str, optional
            Set mode of compressor operation. Can be 'upward' or 'downward'.
            Default is 'downward'.
        threshold : float, optional
            If a signal of stream rises above this level, it will affect the gain reduction.
            Default is 0.125. Range is between 0.00097563 and 1.
        ratio : float, optional
            Set a ratio by which the signal is reduced. 1:2 means that if the level
            rose 4dB above the threshold, it will be only 2dB above after the reduction.
            Default is 2. Range is between 1 and 20.
        attack : float, optional
            Amount of milliseconds the signal has to rise above the threshold before gain
            reduction starts. Default is 20. Range is between 0.01 and 2000.
        release : float, optional
            Amount of milliseconds the signal has to fall below the threshold before
            reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
        makeup : float, optional
            Set the amount by how much signal will be amplified after processing.
            Default is 1. Range is from 1 to 64.
        knee : float, optional
            Curve the sharp knee around the threshold to enter gain reduction more softly.
            Default is 2.82843. Range is between 1 and 8.
        link : str, optional
            Choose if the 'average' level between all channels of the input stream
            or the louder ('maximum') channel of the input stream affects the reduction.
            Default is 'average'.
        detection : str, optional
            Should the exact signal be taken in case of 'peak' or an RMS one in case
            of 'rms'. Default is 'rms' which is mostly smoother.
        mix : float, optional
            How much to use compressed signal in output. Default is 1.
            Range is between 0 and 1.

    Example usage:
    --------------
    stream.acompressor(
        threshold=0.2,
        attack=50,
        release=500,
        mix=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acompressor
    """
    return FilterNode(
        stream,
        acompressor.__name__,
        kwargs={
            "level_in": level_in,
            "mode": mode,
            "threshold": threshold,
            "ratio": ratio,
            "attack": attack,
            "release": release,
            "makeup": makeup,
            "knee": knee,
            "link": link,
            "detection": detection,
            "mix": mix,
        },
    ).stream()
