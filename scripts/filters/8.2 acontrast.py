def acontrast(
    stream: Stream,
    contrast: int = 33,
) -> Stream:
    """
    Simple audio dynamic range compression/expansion filter.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        contrast : int, optional
            Set contrast. Default is 33. Allowed range is between 0 and 100.

    Example usage:
    --------------
    stream.acontrast(
        contrast=50,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acontrast
    """
    return FilterNode(
        stream,
        acontrast.__name__,
        kwargs={"contrast": contrast},
    ).stream()
