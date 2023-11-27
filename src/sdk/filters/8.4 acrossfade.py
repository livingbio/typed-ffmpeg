from typing import Union

from ..node import FilterNode
from ..stream import Stream


def acrossfade(
    stream1: Stream,
    stream2: Stream,
    nb_samples: int = 44100,
    duration: Union[float, str] = None,
    overlap: bool = True,
    curve1: str = None,
    curve2: str = None,
) -> Stream:
    """
    Apply crossfade from one input audio stream to another input audio stream. The crossfade is applied for the specified duration near the end of the first stream.

    The filter accepts the following options:

        Parameters:
        ----------
        stream1 : Stream
            The first input audio stream.
        stream2 : Stream
            The second input audio stream.
        nb_samples : int, optional
            Specify the number of samples for which the crossfade effect has to last. At the end of the crossfade effect, the first input audio will be completely silent. Default is 44100.
        duration : float or str, optional
            Specify the duration of the crossfade effect. See the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. By default, the duration is determined by nb_samples. If set, this option is used instead of nb_samples.
        overlap : bool, optional
            Should the first stream end overlap with the second stream start. Default is True.
        curve1 : str, optional
            Set the curve for the crossfade transition for the first stream.
        curve2 : str, optional
            Set the curve for the crossfade transition for the second stream. For descriptions of available curve types, see the afade filter description.

    Example usage:
    --------------
    stream1.acrossfade(stream2, nb_samples=22050, duration=1.5)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossfade
    """
    return FilterNode(
        [stream1, stream2],
        acrossfade.__name__,
        kwargs={
            "nb_samples": nb_samples,
            "duration": duration,
            "overlap": overlap,
            "curve1": curve1,
            "curve2": curve2,
        },
    ).stream()
