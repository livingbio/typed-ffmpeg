from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def aformat(
    stream: Stream,
    sample_fmts: Optional[str] = None,
    sample_rates: Optional[str] = None,
    channel_layouts: Optional[str] = None,
) -> Stream:
    """
    Set output format constraints for the input audio. The framework will negotiate the most appropriate format to minimize conversions.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    sample_fmts : str, optional
        A '|' separated list of requested sample formats.
    sample_rates : str, optional
        A '|' separated list of requested sample rates.
    channel_layouts : str, optional
        A '|' separated list of requested channel layouts.

    Example usage:
    --------------
    stream.aformat(
        sample_fmts="u8|s16",
        channel_layouts="stereo",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aformat
    """
    return FilterNode(
        stream,
        aformat.__name__,
        kwargs={
            "sample_fmts": sample_fmts,
            "sample_rates": sample_rates,
            "channel_layouts": channel_layouts,
        },
    ).stream()
