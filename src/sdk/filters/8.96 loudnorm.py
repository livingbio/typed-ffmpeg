from ..node import FilterNode
from ..stream import Stream


def loudnorm(
    stream: Stream,
    I: float = -24.0,
    LRA: float = 7.0,
    TP: float = -2.0,
    measured_I: float = None,
    measured_LRA: float = None,
    measured_TP: float = None,
    measured_thresh: float = None,
    offset: float = 0.0,
    linear: bool = True,
    dual_mono: bool = False,
    print_format: str = "none",
) -> Stream:
    """
    EBU R128 loudness normalization. Includes both dynamic and linear normalization modes. Support for both single pass (livestreams, files) and double pass (files) modes. This algorithm can target IL, LRA, and maximum true peak. In dynamic mode, to accurately detect true peaks, the audio stream will be upsampled to 192 kHz. Use the -ar option or aresample filter to explicitly set an output sample rate.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        I : float, optional
            Set integrated loudness target.
            Range is -70.0 - -5.0. Default value is -24.0.
        LRA : float, optional
            Set loudness range target.
            Range is 1.0 - 50.0. Default value is 7.0.
        TP : float, optional
            Set maximum true peak.
            Range is -9.0 - +0.0. Default value is -2.0.
        measured_I : float, optional
            Measured IL of input file.
            Range is -99.0 - +0.0.
        measured_LRA : float, optional
            Measured LRA of input file.
            Range is  0.0 - 99.0.
        measured_TP : float, optional
            Measured true peak of input file.
            Range is  -99.0 - +99.0.
        measured_thresh : float, optional
            Measured threshold of input file.
            Range is -99.0 - +0.0.
        offset : float, optional
            Set offset gain. Gain is applied before the true-peak limiter.
            Range is  -99.0 - +99.0. Default is +0.0.
        linear : bool, optional
            Normalize by linearly scaling the source audio.
            `measured_I`, `measured_LRA`, `measured_TP`, and `measured_thresh` must all be specified.
            Target LRA shouldn't be lower than source LRA and the change in integrated loudness shouldn't
            result in a true peak which exceeds the target TP. If any of these
            conditions aren't met, normalization mode will revert to 'dynamic'.
            Options are `True` or `False`. Default is `True`.
        dual_mono : bool, optional
            Treat mono input files as "dual-mono". If a mono file is intended for playback
            on a stereo system, its EBU R128 measurement will be perceptually incorrect.
            If set to `True`, this option will compensate for this effect.
            Multi-channel input files are not affected by this option.
            Options are `True` or `False`. Default is `False`.
        print_format : str, optional
            Set print format for stats. Options are 'summary', 'json', or 'none'.
            Default value is 'none'.

    Example usage:
    --------------
    stream.loudnorm(
        I=-23.0,
        LRA=7.0,
        TP=-1.0,
        linear=False,
        print_format='summary',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#loudnorm
    """
    kwargs = {
        "I": I,
        "LRA": LRA,
        "TP": TP,
        "measured_I": measured_I,
        "measured_LRA": measured_LRA,
        "measured_TP": measured_TP,
        "measured_thresh": measured_thresh,
        "offset": offset,
        "linear": linear,
        "dual_mono": dual_mono,
        "print_format": print_format,
    }
    for key, value in kwargs.items():
        if value is None:
            kwargs.pop(key)  # Remove optional arguments that are not provided

    return FilterNode(stream, loudnorm.__name__, kwargs=kwargs).stream()
