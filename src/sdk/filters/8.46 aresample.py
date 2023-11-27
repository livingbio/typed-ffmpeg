from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def aresample(
    stream: Stream,
    sample_rate: Optional[int] = None,
    resampler_options: Optional[str] = None,
) -> Stream:
    """
    Resample the input audio to the specified parameters, using the libswresample library. If none are specified then the filter will automatically convert between its input and output.

    This filter is also able to stretch/squeeze the audio data to make it match the timestamps or to inject silence / cut out audio to make it match the timestamps, do a combination of both or do neither.

    The filter accepts the syntax [<sample_rate>:]<resampler_options>, where <sample_rate> expresses a sample rate and <resampler_options> is a list of <key>=<value> pairs, separated by ":". See the (ffmpeg-resampler)"Resampler Options" section in the ffmpeg-resampler(1) manual for the complete list of supported options.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    sample_rate : int, optional
        The sample rate to resample the audio to. If not specified, the filter will automatically convert between the input and output sample rates.
    resampler_options : str, optional
        Additional resampler options as a string of "<key>=<value>" pairs separated by ":".

    Example usage:
    --------------
    stream.aresample(sample_rate=44100)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aresample
    """
    args = []
    if sample_rate is not None:
        args.append(str(sample_rate))
    if resampler_options is not None:
        args.append(resampler_options)
    return FilterNode(stream, aresample.__name__, args=args).stream()
