from decimal import Decimal
from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def atrim(
    stream: Stream,
    start: Optional[Decimal] = None,
    end: Optional[Decimal] = None,
    start_pts: Optional[Decimal] = None,
    end_pts: Optional[Decimal] = None,
    duration: Optional[Decimal] = None,
    start_sample: Optional[Decimal] = None,
    end_sample: Optional[Decimal] = None,
) -> Stream:
    """
    Trim the input so that the output contains one continuous subpart of the input.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    start : float, optional
        Timestamp (in seconds) of the start of the section to keep.
        I.e. the audio sample with the timestamp 'start' will be the first sample in the output.
    end : float, optional
        Specify time of the first audio sample that will be dropped, i.e. the
        audio sample immediately preceding the one with the timestamp 'end' will be
        the last sample in the output.
    start_pts : float, optional
        Same as `start`, except this option sets the start timestamp in samples
        instead of seconds.
    end_pts : float, optional
        Same as `end`, except this option sets the end timestamp in samples instead
        of seconds.
    duration : float, optional
        The maximum duration of the output in seconds.
    start_sample : float, optional
        The number of the first sample that should be output.
    end_sample : float, optional
        The number of the first sample that should be dropped.

    Example usage:
    --------------
    stream.atrim(start=60, end=120)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#atrim
    """
    return FilterNode(
        stream,
        atrim.__name__,
        kwargs={
            "start": start,
            "end": end,
            "start_pts": start_pts,
            "end_pts": end_pts,
            "duration": duration,
            "start_sample": start_sample,
            "end_sample": end_sample,
        },
    ).stream()
