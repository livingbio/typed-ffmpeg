def adynamicsmooth(
    stream: Stream,
    sensitivity: float = 2,
    basefreq: float = 22050,
) -> Stream:
    """
    Apply dynamic smoothing to input audio stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    sensitivity : float, optional
        Set an amount of sensitivity to frequency fluctuations.
        Default is 2. Allowed range is from 0 to 1e+06.
    basefreq : float, optional
        Set a base frequency for smoothing.
        Default value is 22050. Allowed range is from 2 to 1e+06.

    Example usage:
    --------------
    stream.adynamicsmooth(
        sensitivity=1.5,
        basefreq=44100
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth
    """
    return FilterNode(
        stream,
        adynamicsmooth.__name__,
        kwargs={
            "sensitivity": sensitivity,
            "basefreq": basefreq,
        },
    ).stream()
