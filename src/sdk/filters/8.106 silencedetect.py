from typing import Union

from ..node import FilterNode
from ..stream import Stream


def silencedetect(
    stream: Stream,
    noise: Union[float, str] = -60,
    duration: str = "2s",
    mono: bool = False,
) -> Stream:
    """
    Detect silence in an audio stream.

    This filter logs a message when it detects that the input audio volume is less or equal to a noise tolerance value for a duration greater or equal to the minimum detected noise duration.

    The printed times and duration are expressed in seconds. The `lavfi.silence_start` or `lavfi.silence_start.X` metadata key is set on the first frame whose timestamp equals or exceeds the detection duration and it contains the timestamp of the first frame of the silence.

    The `lavfi.silence_duration` or `lavfi.silence_duration.X` and `lavfi.silence_end` or `lavfi.silence_end.X` metadata keys are set on the first frame after the silence. If `mono` is enabled, and each channel is evaluated separately, the `.X` suffixed keys are used, and `X` corresponds to the channel number.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    noise : float or str, optional
        Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default is -60dB, or 0.001.
    duration : str, optional
        Set silence duration until notification (default is 2 seconds). See the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax.
    mono : bool, optional
        Process each channel separately, instead of combined. By default, it is disabled.

    Example usage:
    --------------
    stream.silencedetect(
        noise=-40,
        duration="5s",
        mono=True,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#silencedetect
    """
    return FilterNode(
        stream,
        silencedetect.__name__,
        kwargs={
            "noise": noise,
            "duration": duration,
            "mono": mono,
        },
    ).stream()
