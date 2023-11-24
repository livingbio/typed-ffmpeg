from typing import Union

from ..node import FilterNode
from ..stream import Stream


def channelmap(
    stream: Stream,
    map: str = None,
    channel_layout: Union[str, int] = None,
) -> Stream:
    """
    Remap input channels to new locations.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    map : str, optional
        Map channels from input to output. The argument is a '|'-separated list of
        mappings, each in the 'in_channel-out_channel' or 'in_channel' form.
        in_channel can be either the name of the input channel (e.g. FL for front left) or
        its index in the input channel layout. out_channel is the name of the output channel
        or its index in the output channel layout. If out_channel is not given then it is implicitly an
        index, starting with zero and increasing by one for each mapping.
    channel_layout : Union[str, int], optional
        The channel layout of the output stream.

    Example usage:
    --------------
    stream.channelmap(map='FL-FR|FR-FL', channel_layout='stereo')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#channelmap
    """
    return FilterNode(
        stream,
        channelmap.__name__,
        kwargs={
            "map": map,
            "channel_layout": channel_layout,
        },
    ).stream()
