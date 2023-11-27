from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def replaygain(stream: Stream, track_gain: Optional[str] = None, track_peak: Optional[str] = None) -> Stream:
    """
    ReplayGain scanner filter. This filter takes an audio stream as an input and outputs it unchanged.
    At end of filtering, it displays track_gain and track_peak.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    track_gain : str, optional
        Exported track gain in dB at the end of the stream.
    track_peak : str, optional
        Exported track peak at the end of the stream.

    Returns:
    -------
    Stream
        The filtered output stream.

    Example usage:
    --------------
    stream.replaygain(track_gain="track_gain.txt", track_peak="track_peak.txt")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#replaygain
    """
    return FilterNode(
        stream,
        replaygain.__name__,
        kwargs={
            "track_gain": track_gain,
            "track_peak": track_peak,
        },
    ).stream()
