def adecorrelate(
    stream: Stream,
    stages: int = 6,
    seed: int = 0,
) -> Stream:
    """
    Apply decorrelation to input audio stream.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        stages : int, optional
            Set decorrelation stages of filtering. Allowed range is from 1 to 16.
            Default value is 6.
        seed : int, optional
            Set random seed used for setting delay in samples across channels.

    Example usage:
    --------------
    stream.adecorrelate(
        stages=8,
        seed=1234,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adecorrelate
    """
    return FilterNode(
        stream,
        adecorrelate.__name__,
        kwargs={
            "stages": stages,
            "seed": seed,
        },
    ).stream()
