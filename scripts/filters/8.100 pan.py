from typing import List

from ..node import FilterNode
from ..stream import Stream


def pan(
    stream: Stream,
    layout: str,
    definitions: List[str],
) -> Stream:
    """
    Mix channels with specific gain levels. The filter accepts the output channel layout followed by a set of channels definitions.

    This filter is also designed to efficiently remap the channels of an audio stream.

    The filter accepts parameters of the form: "<layout>|<outdef>|<outdef>|..."

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    layout : str
        Output channel layout or number of channels.
    definitions : List[str]
        Output channel specifications of the form: "<out_name>=<gain>*<in_name>(+-)<gain>*<in_name>..."

    Returns:
    -------
    Stream
        The output filtered stream.

    Example usage:
    --------------
    stream.pan(
        layout='stereo',
        definitions=[
            'FL=0.5*C',
            'FR=0.5*C',
            'L=0.5*L',
            'R=0.5*R',
        ],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#pan
    """
    return FilterNode(
        stream,
        pan.__name__,
        kwargs={
            "layout": layout,
            "definitions": definitions,
        },
    ).stream()
