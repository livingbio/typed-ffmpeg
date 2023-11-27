from ..node import FilterNode
from ..stream import Stream


def volumedetect(stream: Stream) -> Stream:
    """
    Detect the volume of the input video.

    The filter has no parameters. It supports only 16-bit signed integer samples,
    so the input will be converted when needed. Statistics about the volume will
    be printed in the log when the input stream end is reached.

    In particular, it will show the mean volume (root mean square), maximum
    volume (on a per-sample basis), and the beginning of a histogram of the
    registered volume values (from the maximum value to a cumulated 1/1000 of
    the samples).

    All volumes are in decibels relative to the maximum PCM value.

    Parameters:
    ----------
    stream : Stream
        The input stream to analyze.

    Example usage:
    --------------
    stream.volumedetect()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#volumedetect
    """
    return FilterNode(stream, volumedetect.__name__).stream()
