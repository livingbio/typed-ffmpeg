from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def adynamicequalizer(
    stream: Stream,
    threshold: float = 0,
    dfrequency: float = 1000,
    dqfactor: float = 1,
    tfrequency: float = 1000,
    tqfactor: float = 1,
    attack: float = 20,
    release: float = 200,
    ratio: float = 1,
    makeup: float = 0,
    range: int = 50,
    mode: Literal["listen", "cutbelow", "cutabove", "boostbelow", "boostabove"] = "cutbelow",
    dftype: Literal["bandpass", "lowpass", "highpass", "peak"] = "bandpass",
    tftype: Literal["bell", "lowshelf", "highshelf"] = "bell",
    auto: Literal["disabled", "off", "on", "adaptive"] = "disabled",
    precision: Literal["auto", "float", "double"] = "auto",
) -> Stream:
    """
    Apply dynamic equalization to input audio stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    threshold : float, optional
        Set the detection threshold used to trigger equalization.
        Threshold detection is using detection filter.
        Default value is 0. Allowed range is from 0 to 100.
    dfrequency : float, optional
        Set the detection frequency in Hz used for detection filter used to trigger equalization.
        Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
    dqfactor : float, optional
        Set the detection resonance factor for detection filter used to trigger equalization.
        Default value is 1. Allowed range is from 0.001 to 1000.
    tfrequency : float, optional
        Set the target frequency of equalization filter.
        Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
    tqfactor : float, optional
        Set the target resonance factor for target equalization filter.
        Default value is 1. Allowed range is from 0.001 to 1000.
    attack : float, optional
        Set the amount of milliseconds the signal from detection has to rise above
        the detection threshold before equalization starts.
        Default is 20. Allowed range is between 1 and 2000.
    release : float, optional
        Set the amount of milliseconds the signal from detection has to fall below the
        detection threshold before equalization ends.
        Default is 200. Allowed range is between 1 and 2000.
    ratio : float, optional
        Set the ratio by which the equalization gain is raised.
        Default is 1. Allowed range is between 0 and 30.
    makeup : float, optional
        Set the makeup offset by which the equalization gain is raised.
        Default is 0. Allowed range is between 0 and 100.
    range : int, optional
        Set the max allowed cut/boost amount. Default is 50.
        Allowed range is from 1 to 200.
    mode : str, optional
        Set the mode of filter operation, can be one of the following:
            - 'listen'
            - 'cutbelow'
            - 'cutabove'
            - 'boostbelow'
            - 'boostabove'
        Default mode is 'cutbelow'.
    dftype : str, optional
        Set the type of detection filter, can be one of the following:
            - 'bandpass'
            - 'lowpass'
            - 'highpass'
            - 'peak'
        Default type is 'bandpass'.
    tftype : str, optional
        Set the type of target filter, can be one of the following:
            - 'bell'
            - 'lowshelf'
            - 'highshelf'
        Default type is 'bell'.
    auto : str, optional
        Automatically gather threshold from detection filter. By default
        is 'disabled'. This option is useful to detect threshold in certain time frame of
        input audio stream, in such case option value is changed at runtime.
        Available values are:
            - 'disabled'
            - 'off'
            - 'on'
            - 'adaptive'
    precision : str, optional
        Set which precision to use when processing samples.
        Available values:
            - 'auto'
            - 'float'
            - 'double'

    Returns:
    -------
    Stream :
        The output filtered stream.

    Example usage:
    --------------
    stream.adynamicequalizer(
        threshold=10,
        dfrequency=500,
        mode='cutabove',
        range=20,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer
    """
    return FilterNode(
        stream,
        adynamicequalizer.__name__,
        kwargs={
            "threshold": threshold,
            "dfrequency": dfrequency,
            "dqfactor": dqfactor,
            "tfrequency": tfrequency,
            "tqfactor": tqfactor,
            "attack": attack,
            "release": release,
            "ratio": ratio,
            "makeup": makeup,
            "range": range,
            "mode": mode,
            "dftype": dftype,
            "tftype": tftype,
            "auto": auto,
            "precision": precision,
        },
    ).stream()
