from typing import Literal

from ffmpeg.nodes import FilterNode
from ffmpeg.streams import Stream


def acompressor(
    stream: Stream,
    level_in: float = 1.0,
    mode: Literal["upward", "downward"] = "downward",
    threshold: float = 0.125,
    ratio: float = 2,
    attack: float = 20,
    release: float = 250,
    makeup: float = 1,
    knee: float = 2.82843,
    link: Literal["average", "maximum"] = "average",
    detection: Literal["peak", "rms"] = "rms",
    mix: float = 1,
) -> Stream:
    return FilterNode(
        stream,
        "acompressor",
        level_in=level_in,
        mode=mode,
        threshold=threshold,
        ratio=ratio,
        attack=attack,
        release=release,
        makeup=makeup,
        knee=knee,
        link=link,
        detection=detection,
        mix=mix,
    ).stream()
