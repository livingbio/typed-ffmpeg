from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def afwtdn(
    stream: Stream,
    sigma: float = 0.0,
    levels: int = 10,
    wavet: str = Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"],
    percent: float = 85,
    profile: bool = False,
    adaptive: bool = False,
    samples: int = 8192,
    softness: int = 1,
) -> Stream:
    """
    Reduce broadband noise from input samples using Wavelets.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    sigma : float, optional
        Set the noise sigma, allowed range is from 0 to 1.
        Default value is 0.
        This option controls strength of denoising applied to input samples.
        Most useful way to set this option is via decibels, eg. -45dB.
    levels : int, optional
        Set the number of wavelet levels of decomposition.
        Allowed range is from 1 to 12.
        Default value is 10.
        Setting this too low make denoising performance very poor.
    wavet : str, optional
        Set wavelet type for decomposition of input frame.
        They are sorted by number of coefficients, from lowest to highest.
        More coefficients means worse filtering speed, but overall better quality.
        Available wavelets are:
            - 'sym2'
            - 'sym4'
            - 'rbior68'
            - 'deb10'
            - 'sym10'
            - 'coif5'
            - 'bl3'
    percent : float, optional
        Set percent of full denoising. Allowed range is from 0 to 100 percent.
        Default value is 85 percent or partial denoising.
    profile : bool, optional
        If enabled, the first input frame will be used as a noise profile.
        If the first frame samples contain non-noise, performance will be very poor.
    adaptive : bool, optional
        If enabled, input frames are analyzed for the presence of noise.
        If noise is detected with high possibility, then input frame profile will be
        used for processing following frames, until a new noise frame is detected.
    samples : int, optional
        Set size of single frame in number of samples. Allowed range is from 512 to 65536.
        Default frame size is 8192 samples.
    softness : int, optional
        Set softness applied inside thresholding function. Allowed range is from 0 to 10.
        Default softness is 1.

    Returns:
    -------
    Stream
        The filtered output stream.

    Example usage:
    --------------
    stream.afwtdn(
        sigma=-45,
        profile=True,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afwtdn
    """
    return FilterNode(
        stream,
        afwtdn.__name__,
        kwargs={
            "sigma": sigma,
            "levels": levels,
            "wavet": wavet,
            "percent": percent,
            "profile": profile,
            "adaptive": adaptive,
            "samples": samples,
            "softness": softness,
        },
    ).stream()
