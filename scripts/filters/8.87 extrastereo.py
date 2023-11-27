def extrastereo(
    stream: Stream,
    m: float = 2.5,
    c: bool = True,
) -> Stream:
    """
    Linearly increases the difference between left and right channels which adds some sort of "live" effect to playback.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        m : float, optional
            Sets the difference coefficient (default: 2.5).
            0.0 means mono sound (average of both channels), with 1.0 sound will be unchanged,
            with -1.0 left and right channels will be swapped.
        c : bool, optional
            Enable clipping. By default is enabled.

    Example usage:
    --------------
    stream.extrastereo(
        m=2.0,
        c=False,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#extrastereo
    """
    return FilterNode(
        stream,
        extrastereo.__name__,
        kwargs={
            "m": m,
            "c": c,
        },
    ).stream()
