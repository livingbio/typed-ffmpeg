from typing import List, Union

from ..node import FilterNode
from ..stream import Stream


def join(
    inputs: int = 2,
    channel_layout: str = "stereo",
    map: Union[str, List[str]] = None,
) -> Stream:
    """
    Join multiple input streams into one multi-channel stream.

    Parameters:
    ----------
    inputs : int, optional
        The number of input streams. It defaults to 2.
    channel_layout : str, optional
        The desired output channel layout. It defaults to stereo.
    map : str or List[str], optional
        Map channels from inputs to output. The argument is a '|'-separated list of
        mappings, each in the 'input_idx.in_channel-out_channel' form. input_idx is
        the 0-based index of the input stream. in_channel can be either the name of
        the input channel (e.g. FL for front left) or its index in the specified
        input stream. out_channel is the name of the output channel.

    Example usage:
    --------------
    join(
        inputs=3,
        channel_layout="5.1",
        map=["0.0-FL", "1.0-FR", "2.0-FC", "3.0-SL", "4.0-SR", "5.0-LFE"],
    )

    Returns:
    --------
    Stream

    Ref: https://ffmpeg.org/ffmpeg-filters.html#join
    """
    kwargs = {"inputs": inputs, "channel_layout": channel_layout}
    if map:
        mappings = "|".join(map) if isinstance(map, list) else map
        kwargs["map"] = mappings

    return FilterNode(None, join.__name__, kwargs=kwargs).stream()
