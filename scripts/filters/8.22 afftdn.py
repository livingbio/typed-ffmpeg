from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def afftdn(
    stream: Stream,
    noise_reduction: float = 12,
    noise_floor: float = -50,
    noise_type: str = Literal["white", "vinyl", "shellac", "custom"],
    band_noise: str = "",
    residual_floor: float = -38,
    track_noise: bool = False,
    track_residual: bool = False,
    output_mode: str = Literal["input", "output", "noise"],
    adaptivity: float = 0.5,
    floor_offset: float = 1.0,
    noise_link: str = Literal["none", "min", "max", "average"],
    band_multiplier: float = 1.25,
    sample_noise: str = "none",
    gain_smooth: int = 0,
) -> Stream:
    """
    Denoise audio samples with FFT.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    noise_reduction : float, optional
        Set the noise reduction in dB, allowed range is 0.01 to 97.
        Default value is 12 dB.
    noise_floor : float, optional
        Set the noise floor in dB, allowed range is -80 to -20.
        Default value is -50 dB.
    noise_type : str, optional
        Set the noise type.

        It accepts the following values:

        - 'white', 'w': Select white noise.
        - 'vinyl', 'v': Select vinyl noise.
        - 'shellac', 's': Select shellac noise.
        - 'custom', 'c': Select custom noise, defined in 'band_noise' option.

        Default value is white noise.
    band_noise : str, optional
        Set custom band noise profile for every one of 15 bands.
        Bands are separated by ' ' or '|'.
    residual_floor : float, optional
        Set the residual floor in dB, allowed range is -80 to -20.
        Default value is -38 dB.
    track_noise : bool, optional
        Enable noise floor tracking. By default is disabled.
        With this enabled, noise floor is automatically adjusted.
    track_residual : bool, optional
        Enable residual tracking. By default is disabled.
    output_mode : str, optional
        Set the output mode.

        It accepts the following values:

        - 'input', 'i': Pass input unchanged.
        - 'output', 'o': Pass noise filtered out.
        - 'noise', 'n': Pass only noise.

        Default value is 'output'.
    adaptivity : float, optional
        Set the adaptivity factor, used how fast to adapt gains adjustments per
        each frequency bin. Value 0 enables instant adaptation, while higher values
        react much slower.
        Allowed range is from 0 to 1. Default value is 0.5.
    floor_offset : float, optional
        Set the noise floor offset factor. This option is used to adjust offset applied to measured
        noise floor. It is only effective when noise floor tracking is enabled.
        Allowed range is from -2.0 to 2.0. Default value is 1.0.
    noise_link : str, optional
        Set the noise link used for multichannel audio.

        It accepts the following values:

        - 'none': Use unchanged channel's noise floor.
        - 'min': Use measured min noise floor of all channels.
        - 'max': Use measured max noise floor of all channels.
        - 'average': Use measured average noise floor of all channels.

        Default value is 'min'.
    band_multiplier : float, optional
        Set the band multiplier factor, used how much to spread bands across frequency bins.
        Allowed range is from 0.2 to 5. Default value is 1.25.
    sample_noise : str, optional
        Toggle capturing and measurement of noise profile from input audio.

        It accepts the following values:

        - 'start', 'begin': Start sample noise capture.
        - 'stop', 'end': Stop sample noise capture and measure new noise band profile.

        Default value is 'none'.
    gain_smooth : int, optional
        Set gain smooth spatial radius, used to smooth gains applied to each frequency bin.
        Useful to reduce random music noise artifacts.
        Higher values increases smoothing of gains.
        Allowed range is from 0 to 50. Default value is 0.

    Example usage:
    --------------
    stream.afftdn(
        noise_reduction=6,
        noise_floor=-30,
        noise_type="white",
        band_noise="32 29 32 34 34 29 33 33 32 30 27 26 26 25 25",
        track_residual=True,
        output_mode="noise",
        adaptivity=0.8,
        floor_offset=0.5,
        noise_link="average",
        band_multiplier=1.5,
        sample_noise="start",
        gain_smooth=10,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afftdn
    """
    return FilterNode(
        stream,
        afftdn.__name__,
        kwargs={
            "noise_reduction": noise_reduction,
            "noise_floor": noise_floor,
            "noise_type": noise_type,
            "band_noise": band_noise,
            "residual_floor": residual_floor,
            "track_noise": track_noise,
            "track_residual": track_residual,
            "output_mode": output_mode,
            "adaptivity": adaptivity,
            "floor_offset": floor_offset,
            "noise_link": noise_link,
            "band_multiplier": band_multiplier,
            "sample_noise": sample_noise,
            "gain_smooth": gain_smooth,
        },
    ).stream()
