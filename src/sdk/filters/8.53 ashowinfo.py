from typing import List, Optional

from ..node import FilterNode
from ..stream import Stream


def ashowinfo(
    stream: Stream,
    n: bool = True,
    pts: bool = True,
    pts_time: bool = True,
    fmt: bool = True,
    chlayout: bool = True,
    rate: bool = True,
    nb_samples: bool = True,
    checksum: bool = True,
    plane_checksums: Optional[List[int]] = None,
) -> Stream:
    """
    Show a line containing various information for each input audio frame. The input audio is not modified.

    The shown line contains a sequence of key/value pairs of the form key:value.

    The following values are shown in the output:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        n : bool, optional
            The (sequential) number of the input frame, starting from 0. Default is True.
        pts : bool, optional
            The presentation timestamp of the input frame, in time base units; the time base depends on the filter input pad, and is usually 1/sample_rate. Default is True.
        pts_time : bool, optional
            The presentation timestamp of the input frame in seconds. Default is True.
        fmt : bool, optional
            The sample format. Default is True.
        chlayout : bool, optional
            The channel layout. Default is True.
        rate : bool, optional
            The sample rate for the audio frame. Default is True.
        nb_samples : bool, optional
            The number of samples (per channel) in the frame. Default is True.
        checksum : bool, optional
            The Adler-32 checksum (printed in hexadecimal) of the audio data. For planar audio, the data is treated as if all the planes were concatenated. Default is True.
        plane_checksums : List[int], optional
            A list of Adler-32 checksums for each data plane. Default is None.

    Example usage:
    --------------
    stream.ashowinfo(
        n=True,
        pts=True,
        pts_time=True,
        fmt=True,
        chlayout=True,
        rate=True,
        nb_samples=True,
        checksum=True,
        plane_checksums=[128, 256, 512],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#ashowinfo
    """
    return FilterNode(
        stream,
        ashowinfo.__name__,
        kwargs={
            "n": int(n),
            "pts": int(pts),
            "pts_time": int(pts_time),
            "fmt": int(fmt),
            "chlayout": int(chlayout),
            "rate": int(rate),
            "nb_samples": int(nb_samples),
            "checksum": int(checksum),
            "plane_checksums": plane_checksums,
        },
    ).stream()
