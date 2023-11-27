from typing import Union

from ..node import FilterNode
from ..stream import Stream


def afade(
    stream: Stream,
    fade_type: str = "in",
    start_sample: int = 0,
    nb_samples: int = 44100,
    start_time: Union[float, str] = 0,
    duration: Union[float, str] = None,
    curve: str = "tri",
    silence: float = 0.0,
    unity: float = 1.0,
) -> Stream:
    """
    Apply fade-in/out effect to input audio.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    fade_type : str, optional
        Specify the effect type, can be either 'in' for fade-in or 'out' for a fade-out effect.
        Default is 'in'.
    start_sample : int, optional
        Specify the number of the start sample for starting to apply the fade effect.
        Default is 0.
    nb_samples : int, optional
        Specify the number of samples for which the fade effect has to last.
        At the end of the fade-in effect, the output audio will have the same volume as the input audio.
        At the end of the fade-out transition, the output audio will be silence.
        Default is 44100.
    start_time : Union[float, str], optional
        Specify the start time of the fade effect.
        Default is 0. The value must be specified as a time duration.
    duration : Union[float, str], optional
        Specify the duration of the fade effect.
        At the end of the fade-in effect, the output audio will have the same volume as the input audio.
        At the end of the fade-out transition, the output audio will be silence.
        By default, the duration is determined by `nb_samples`.
    curve : str, optional
        Set the curve for the fade transition.
        Default is 'tri'. It accepts the following values:
            'tri' - select triangular, linear slope (default)
            'qsin' - select quarter of sine wave
            'hsin' - select half of sine wave
            'esin' - select exponential sine wave
            'log' - select logarithmic
            'ipar' - select inverted parabola
            'qua' - select quadratic
            'cub' - select cubic
            'squ' - select square root
            'cbr' - select cubic root
            'par' - select parabola
            'exp' - select exponential
            'iqsin' - select inverted quarter of sine wave
            'ihsin' - select inverted half of sine wave
            'dese' - select double-exponential seat
            'desi' - select double-exponential sigmoid
            'losi' - select logistic sigmoid
            'sinc' - select sine cardinal function
            'isinc' - select inverted sine cardinal function
            'quat' - select quartic
            'quatr' - select quartic root
            'qsin2' - select squared quarter of sine wave
            'hsin2' - select squared half of sine wave
            'nofade' - no fade applied
    silence : float, optional
        Set the initial gain for fade-in or final gain for fade-out.
        Default value is 0.0.
    unity : float, optional
        Set the initial gain for fade-out or final gain for fade-in.
        Default value is 1.0.

    Example usage:
    --------------
    stream.afade(
        fade_type="out",
        start_time=5.0,
        duration=2.5,
        curve="log",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afade
    """
    return FilterNode(
        stream,
        afade.__name__,
        kwargs={
            "type": fade_type,
            "start_sample": start_sample,
            "nb_samples": nb_samples,
            "start_time": start_time,
            "duration": duration,
            "curve": curve,
            "silence": silence,
            "unity": unity,
        },
    ).stream()
