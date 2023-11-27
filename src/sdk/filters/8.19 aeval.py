from typing import List, Union

from ..node import FilterNode
from ..stream import Stream


def aeval(
    stream: Stream,
    exprs: Union[str, List[str]],
    channel_layout: Union[str, int] = None,
) -> Stream:
    """
    Modify an audio signal according to the specified expressions.

    This filter accepts one or more expressions (one for each channel), which are evaluated and used to modify a corresponding audio signal.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    exprs : Union[str, List[str]]
        Set the '|'-separated expressions list for each separate channel. If the number of input channels is greater than the number of expressions, the last specified expression is used for the remaining output channels.
    channel_layout : Union[str, int], optional
        Set output channel layout. If not specified, the channel layout is specified by the number of expressions. If set to 'same', it will use by default the same input channel layout.

    Example usage:
    --------------
    stream.aeval(
        exprs='val(0)*0.5|val(1)*0.5',
        channel_layout='same',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aeval
    """
    return FilterNode(
        stream,
        aeval.__name__,
        kwargs={
            "exprs": exprs,
            "channel_layout": channel_layout,
        },
    ).stream()
