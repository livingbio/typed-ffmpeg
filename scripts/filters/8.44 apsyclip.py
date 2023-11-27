from typing import Union

from ..node import FilterNode
from ..stream import Stream


def apsyclip(
    stream: Stream,
    level_in: float = 1.0,
    level_out: float = 1.0,
    clip: float = 0.0,
    diff: bool = False,
    adaptive: float = 0.5,
    iterations: int = 10,
    level: Union[bool, int] = False,
) -> Stream:
    """
    Apply Psychoacoustic clipper to input audio stream.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set input gain. By default, it is 1.0. Range is between 0.015625 and 64.
        level_out : float, optional
            Set output gain. By default, it is 1.0. Range is between 0.015625 and 64.
        clip : float, optional
            Set the clipping start value. Default value is 0dBFS or 1.
        diff : bool, optional
            Output only difference samples, useful to hear introduced distortions.
            By default, it is disabled.
        adaptive : float, optional
            Set strength of adaptive distortion applied. Default value is 0.5.
            Allowed range is from 0 to 1.
        iterations : int, optional
            Set number of iterations of psychoacoustic clipper.
            Allowed range is from 1 to 20. Default value is 10.
        level : Union[bool, int], optional
            Auto level output signal. Default is disabled.
            This normalizes audio back to 0dBFS if enabled.

    Example usage:
    --------------
    stream.apsyclip(
        level_in=0.5,
        level_out=0.8,
        clip=0.2,
        diff=True,
        adaptive=0.7,
        iterations=5,
        level=True,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#apsyclip
    """
    return FilterNode(
        stream,
        apsyclip.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "clip": clip,
            "diff": diff,
            "adaptive": adaptive,
            "iterations": iterations,
            "level": level,
        },
    ).stream()
