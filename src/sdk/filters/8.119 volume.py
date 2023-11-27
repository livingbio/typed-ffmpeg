from typing import Literal, Union

from ..enums import Precision, ReplayGain
from ..node import FilterNode
from ..stream import Stream


class VolumeExpr:
    def __init__(
        self,
        n: int = None,
        nb_channels: int = None,
        nb_consumed_samples: int = None,
        nb_samples: int = None,
        pos: int = None,
        pts: float = None,
        sample_rate: int = None,
        startpts: float = None,
        startt: float = None,
        t: float = None,
        tb: float = None,
        volume: float = None,
    ):
        self.n = n
        self.nb_channels = nb_channels
        self.nb_consumed_samples = nb_consumed_samples
        self.nb_samples = nb_samples
        self.pos = pos
        self.pts = pts
        self.sample_rate = sample_rate
        self.startpts = startpts
        self.startt = startt
        self.t = t
        self.tb = tb
        self.volume = volume


def volume(
    stream: Stream,
    volume: Union[float, VolumeExpr] = 1.0,
    precision: Union[str, Precision] = "float",
    replaygain: Union[str, ReplayGain] = "drop",
    replaygain_preamp: float = 0.0,
    replaygain_noclip: bool = True,
    eval: Literal["once", "frame"] = "once",
) -> Stream:
    """
    Adjust the input audio volume.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    volume : float or VolumeExpr, optional
        Set audio volume expression.
        Output values are clipped to the maximum value.
        The output audio volume is given by the relation:
            output_volume = volume * input_volume
        The default value is 1.0.
    precision : str or Precision, optional
        This parameter represents the mathematical precision.
        It determines which input sample formats will be allowed, which affects the
        precision of the volume scaling.
        - 'fixed': 8-bit fixed-point; this limits input sample format to U8, S16, and S32.
        - 'float': 32-bit floating-point; this limits input sample format to FLT. (default)
        - 'double': 64-bit floating-point; this limits input sample format to DBL.
    replaygain : str or ReplayGain, optional
        Choose the behaviour on encountering ReplayGain side data in input frames.
        - 'drop': Remove ReplayGain side data, ignoring its contents (the default).
        - 'ignore': Ignore ReplayGain side data, but leave it in the frame.
        - 'track': Prefer the track gain, if present.
        - 'album': Prefer the album gain, if present.
    replaygain_preamp : float, optional
        Pre-amplification gain in dB to apply to the selected replaygain gain.
        The default value is 0.0.
    replaygain_noclip : bool, optional
        Prevent clipping by limiting the gain applied.
        The default value is True.
    eval : {'once', 'frame'}, optional
        Set when the volume expression is evaluated.
        - 'once': Only evaluate expression once during the filter initialization, or
            when the 'volume' command is sent.
        - 'frame': Evaluate expression for each incoming frame.
        The default value is 'once'.

    Example usage:
    --------------
    stream.volume(volume=0.5, replaygain='album')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#volume
    """
    if isinstance(volume, VolumeExpr):
        volume_expr = volume
    else:
        volume_expr = VolumeExpr(volume=volume)

    return FilterNode(
        stream,
        volume.__name__,
        kwargs={
            "volume": volume_expr,
            "precision": Precision(precision).value,
            "replaygain": ReplayGain(replaygain).value,
            "replaygain_preamp": replaygain_preamp,
            "replaygain_noclip": 1 if replaygain_noclip else 0,
            "eval": eval,
        },
    ).stream()
