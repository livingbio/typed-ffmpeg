from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def apad(stream: Stream, packet_size: Optional[int] = 4096, pad_len: Optional[int] = None, whole_len: Optional[int] = None, pad_dur: Optional[str] = None, whole_dur: Optional[str] = None) -> Stream:
    """
    Pad the end of an audio stream with silence.

    This can be used together with ffmpeg `-shortest` to extend audio streams to the same length as the video stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    packet_size : int, optional
        Set silence packet size. Default value is 4096.
    pad_len : int, optional
        Set the number of samples of silence to add to the end. After the value is reached, the stream is terminated. This option is mutually exclusive with `whole_len`.
    whole_len : int, optional
        Set the minimum total number of samples in the output audio stream. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with `pad_len`.
    pad_dur : str, optional
        Specify the duration of samples of silence to add. See the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value.
    whole_dur : str, optional
        Specify the minimum total duration in the output audio stream. See the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with `pad_dur`.

    Example usage:
    --------------
    stream.apad(pad_len=1000)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#apad
    """
    return FilterNode(
        stream,
        apad.__name__,
        kwargs={
            "packet_size": packet_size,
            "pad_len": pad_len,
            "whole_len": whole_len,
            "pad_dur": pad_dur,
            "whole_dur": whole_dur,
        },
    ).stream()
