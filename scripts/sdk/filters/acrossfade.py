from typing import Union

from ..node import FilterNode
from ..stream import Stream


def acrossfade(
    input1: Stream,
    input2: Stream,
    nb_samples: Union[int, str] = 44100,
    duration: Union[int, float, str] = "",
    overlap: bool = True,
    curve1: str = "",
    curve2: str = "",
) -> Stream:
    """
    Apply cross fade from one input audio stream to another input audio stream.

    The cross fade is applied for a specified duration near the end of the first stream.

    Parameters:
    ----------
    input1 : Stream
        The first input audio stream.
    input2 : Stream
        The second input audio stream.
    nb_samples : int, optional
        Specify the number of samples for which the cross fade effect has to last.
        At the end of the cross fade effect, the first input audio will be completely silent.
        Default is 44100.
    duration : int, float, str, optional
        Specify the duration of the cross fade effect. See
        https://ffmpeg.org/ffmpeg-utils.html#time-duration-syntax
        for the accepted syntax.
        By default, the duration is determined by nb_samples.
        If set, this option is used instead of nb_samples.
    overlap : bool, optional
        Should the first stream end overlap with the second stream start. Default is True.
    curve1 : str, optional
        Set the curve for the cross fade transition for the first stream.
    curve2 : str, optional
        Set the curve for the cross fade transition for the second stream.
        For a description of available curve types, see the 'afade' filter description.

    Example usage:
    --------------
    input_stream1 = Stream(...)
    input_stream2 = Stream(...)

    output_stream = acrossfade(input_stream1, input_stream2, nb_samples=48000, curve1='tri')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossfade
    """
    return FilterNode(
        [input1, input2],
        acrossfade.__name__,
        kwargs={
            "nb_samples": nb_samples,
            "duration": duration,
            "overlap": overlap,
            "curve1": curve1,
            "curve2": curve2,
        },
    ).stream()
