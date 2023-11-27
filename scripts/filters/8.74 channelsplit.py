from ..node import FilterNode
from ..stream import Stream


def channelsplit(
    stream: Stream,
    channel_layout: str = "stereo",
    channels: str = "all",
) -> Stream:
    """
    Split each channel from an input audio stream into a separate output stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to split.
    channel_layout : str, optional
        The channel layout of the input stream. The default is "stereo".
    channels : str, optional
        A channel layout describing the channels to be extracted as separate output streams
        or "all" to extract each input channel as a separate stream. The default is "all".
        Choosing channels not present in the channel layout in the input will result in an error.

    Example usage:
    --------------
    stream.channelsplit()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#channelsplit
    """
    return FilterNode(
        stream,
        channelsplit.__name__,
        kwargs={
            "channel_layout": channel_layout,
            "channels": channels,
        },
    ).stream()
