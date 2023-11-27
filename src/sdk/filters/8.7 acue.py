from ..node import FilterNode
from ..stream import Stream
from ..util import Time


def acue(
    stream: Stream,
    time: Time,
) -> Stream:
    """
    Delay audio filtering until a given wallclock timestamp.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    time : Time
        The wallclock timestamp to delay the audio filtering until.

    Example usage:
    --------------
    stream.acue(
        time="00:01:30",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acue
    """
    return FilterNode(stream, acue.__name__, kwargs={"time": time}).stream()
