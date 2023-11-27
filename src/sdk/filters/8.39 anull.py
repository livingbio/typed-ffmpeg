def anull(stream: Stream) -> Stream:
    """
    Pass the audio source unchanged to the output.

    Parameters:
    ----------
    stream : Stream
        The input stream to pass unchanged to the output.

    Returns:
    -------
    Stream
        The output stream with the audio source unchanged.

    Example usage:
    --------------
    stream.anull()

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anull
    """
    return FilterNode(stream, anull.__name__).stream()
