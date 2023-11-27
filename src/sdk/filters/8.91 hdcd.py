from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def hdcd(
    stream: Stream,
    disable_autoconvert: Optional[bool] = None,
    process_stereo: Optional[bool] = None,
    cdt_ms: Optional[int] = None,
    force_pe: Optional[bool] = None,
    analyze_mode: Optional[str] = None,
) -> Stream:
    """
    Decodes High Definition Compatible Digital (HDCD) data. A 16-bit PCM stream with embedded HDCD codes is expanded into a 20-bit PCM stream.

    The filter supports the Peak Extend and Low-level Gain Adjustment features of HDCD and detects the Transient Filter flag.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    disable_autoconvert : bool, optional
        Disable any automatic format conversion or resampling in the filter graph.
    process_stereo : bool, optional
        Process the stereo channels together. If target_gain does not match between
        channels, consider it invalid and use the last valid target_gain.
    cdt_ms : int, optional
        Set the code detect timer period in ms.
    force_pe : bool, optional
        Always extend peaks above -3dBFS even if PE isn’t signaled.
    analyze_mode : str, optional
        Replace audio with a solid tone and adjust the amplitude to signal some specific aspect of the decoding process. The output file can be loaded in an audio editor alongside the original to aid analysis.
        'analyze_mode=pe:force_pe=true' can be used to see all samples above the PE level.

        Modes are:
        - '0, off': Disabled
        - '1, lle': Gain adjustment level at each sample
        - '2, pe': Samples where peak extend occurs
        - '3, cdt': Samples where the code detect timer is active
        - '4, tgm': Samples where the target gain does not match between channels

    Example usage:
    --------------
    stream.hdcd(
        disable_autoconvert=True,
        process_stereo=True,
        cdt_ms=100,
        force_pe=True,
        analyze_mode="pe",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hdcd
    """
    return FilterNode(
        stream,
        hdcd.__name__,
        kwargs={
            "disable_autoconvert": disable_autoconvert,
            "process_stereo": process_stereo,
            "cdt_ms": cdt_ms,
            "force_pe": force_pe,
            "analyze_mode": analyze_mode,
        },
    ).stream()
