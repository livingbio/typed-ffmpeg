from ..node import FilterNode
from ..stream import Stream


def speechnorm(
    stream: Stream,
    peak: float = 0.95,
    expansion: float = 2.0,
    compression: float = 2.0,
    threshold: float = 0.0,
    raise_: float = 0.001,
    fall: float = 0.001,
    channels: str = "all",
    invert: bool = False,
    link: bool = False,
    rms: float = 0.0,
) -> Stream:
    """
    Speech Normalizer.

    This filter expands or compresses each half-cycle of audio samples (local set of samples all above or all below zero and between two nearest zero crossings) depending on threshold value, so audio reaches target peak value under conditions controlled by below options.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    peak : float, optional
        Set the expansion target peak value. This specifies the highest allowed absolute amplitude level
        for the normalized audio input. Default value is 0.95. Allowed range is from 0.0 to 1.0.
    expansion : float, optional
        Set the maximum expansion factor. Allowed range is from 1.0 to 50.0. Default value is 2.0.
        This option controls maximum half-cycle of samples expansion. The maximum expansion would be such
        that the local peak value reaches the target peak value but never surpasses it and that the ratio
        between the new and previous peak value does not surpass this option value.
    compression : float, optional
        Set the maximum compression factor. Allowed range is from 1.0 to 50.0. Default value is 2.0.
        This option controls maximum local half-cycle of samples compression. This option is used only if
        'threshold' option is set to a value greater than 0.0, then in such cases when local peak is lower
        or the same as the value set by 'threshold' all samples belonging to that peak's half-cycle
        will be compressed by the current compression factor.
    threshold : float, optional
        Set the threshold value. Default value is 0.0. Allowed range is from 0.0 to 1.0.
        This option specifies which half-cycles of samples will be compressed and which will be expanded.
        Any half-cycle samples with their local peak value below or the same as this option value will be
        compressed by the current compression factor, otherwise, if greater than the threshold value they
        will be expanded with the expansion factor so that it could reach peak target value but never surpass it.
    raise_ : float, optional
        Set the expansion raising amount per each half-cycle of samples. Default value is 0.001.
        Allowed range is from 0.0 to 1.0. This controls how fast the expansion factor is raised per
        each new half-cycle until it reaches the 'expansion' value. Setting this options too high may lead to distortions.
    fall : float, optional
        Set the compression raising amount per each half-cycle of samples. Default value is 0.001.
        Allowed range is from 0.0 to 1.0. This controls how fast the compression factor is raised per
        each new half-cycle until it reaches the 'compression' value.
    channels : str, optional
        Specify which channels to filter, by default all available channels are filtered.
    invert : bool, optional
        Enable inverted filtering, by default is disabled. This inverts interpretation of 'threshold' option.
        When enabled any half-cycle of samples with their local peak value below or the same as the 'threshold'
        option will be expanded otherwise it will be compressed.
    link : bool, optional
        Link channels when calculating gain applied to each filtered channel sample, by default is disabled.
        When disabled each filtered channel gain calculation is independent, otherwise when this option is enabled
        the minimum of all possible gains for each filtered channel is used.
    rms : float, optional
        Set the expansion target RMS value. This specifies the highest allowed RMS level for the normalized
        audio input. Default value is 0.0, thus disabled. Allowed range is from 0.0 to 1.0.

    Example usage:
    --------------
    stream.speechnorm(
        peak=0.8,
        expansion=3,
        compression=4,
        threshold=0.2,
        rms=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#speechnorm
    """
    return FilterNode(
        stream,
        speechnorm.__name__,
        kwargs={
            "peak": peak,
            "expansion": expansion,
            "compression": compression,
            "threshold": threshold,
            "raise_": raise_,
            "fall": fall,
            "channels": channels,
            "invert": invert,
            "link": link,
            "rms": rms,
        },
    ).stream()
