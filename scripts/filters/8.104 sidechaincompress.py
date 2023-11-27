def sidechaincompress(
    main_stream: Stream,
    side_chain_stream: Stream,
    level_in: float = 1.0,
    mode: str = Literal["downward", "upward"],
    threshold: float = 0.125,
    ratio: float = 2,
    attack: float = 20,
    release: float = 250,
    makeup: float = 1,
    knee: float = 2.82843,
    link: str = "average",
    detection: str = "rms",
    level_sc: float = 1.0,
    mix: float = 1,
) -> Stream:
    """
    This filter acts like normal compressor but has the ability to compress
    detected signal using second input signal.
    It needs two input streams and returns one output stream.
    First input stream will be processed depending on second stream signal.
    The filtered signal then can be filtered with other filters in later stages of processing.

    Parameters:
    ----------
    main_stream : Stream
        The main input stream to filter.
    side_chain_stream : Stream
        The sidechain input stream to control the compression.
    level_in : float, optional
        Set input gain. Default is 1. Range is between 0.015625 and 64.
    mode : str, optional
        Set mode of compressor operation. Can be 'upward' or 'downward'.
        Default is 'downward'.
    threshold : float, optional
        If a signal of the second stream raises above this level, it will affect the gain
        reduction of the first stream.
        Default is 0.125. Range is between 0.00097563 and 1.
    ratio : float, optional
        Set a ratio about which the signal is reduced. 1:2 means that if the level
        raised 4dB above the threshold, it will be only 2dB above after the reduction.
        Default is 2. Range is between 1 and 20.
    attack : float, optional
        Amount of milliseconds the signal has to rise above the threshold before gain
        reduction starts. Default is 20. Range is between 0.01 and 2000.
    release : float, optional
        Amount of milliseconds the signal has to fall below the threshold before
        reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
    makeup : float, optional
        Set the amount by how much signal will be amplified after processing.
        Default is 1. Range is from 1 to 64.
    knee : float, optional
        Curve the sharp knee around the threshold to enter gain reduction more softly.
        Default is 2.82843. Range is between 1 and 8.
    link : str, optional
        Choose if the 'average' level between all channels of sidechain stream
        or the louder ('maximum') channel of sidechain stream affects the
        reduction. Default is 'average'.
    detection : str, optional
        Should the exact signal be taken in case of 'peak' or an RMS one in case
        of 'rms'. Default is 'rms' which is mainly smoother.
    level_sc : float, optional
        Set sidechain gain. Default is 1. Range is between 0.015625 and 64.
    mix : float, optional
        How much to use compressed signal in output. Default is 1.
        Range is between 0 and 1.

    Returns:
    -------
    Stream
        The stream with compression applied.

    Example usage:
    --------------
    main_stream.sidechaincompress(
        side_chain_stream,
        threshold=0.2,
        attack=50,
        release=500,
        mix=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress
    """
    return FilterNode(
        [main_stream, side_chain_stream],
        sidechaincompress.__name__,
        kwargs={
            "level_in": level_in,
            "mode": mode,
            "threshold": threshold,
            "ratio": ratio,
            "attack": attack,
            "release": release,
            "makeup": makeup,
            "knee": knee,
            "link": link,
            "detection": detection,
            "level_sc": level_sc,
            "mix": mix,
        },
    ).stream()
