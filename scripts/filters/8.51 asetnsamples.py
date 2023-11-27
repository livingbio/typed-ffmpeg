from typing import Literal, Union

from ..node import FilterNode
from ..stream import Stream


def asetnsamples(
    stream: Stream,
    nb_out_samples: int = 1024,
    pad: Union[int, Literal["true"]] = 1,
) -> Stream:
    """
    Set the number of samples per each output audio frame.

    The last output packet may contain a different number of samples, as the filter will flush all the remaining samples when the input audio signals its end.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    nb_out_samples : int, optional
        Set the number of frames per each output audio frame. The number is intended as the number of samples per each channel. Default value is 1024.
    pad : int or str, optional
        If set to 1 or 'true', the filter will pad the last audio frame with zeroes, so that the last frame will contain the same number of samples as the previous ones. Default value is 1.

    Example usage:
    --------------
    stream.asetnsamples(
        nb_out_samples=1234,
        pad=0,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asetnsamples
    """
    return FilterNode(
        stream,
        asetnsamples.__name__,
        kwargs={"nb_out_samples": nb_out_samples, "pad": pad},
    ).stream()
