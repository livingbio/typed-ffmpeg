from typing import Literal, Union

from ..node import FilterNode
from ..stream import Stream


def acrusher(
    stream: Stream,
    level_in: float = 0.5,
    level_out: float = 0.5,
    bits: int = 8,
    mix: float = 0.5,
    mode: Literal["lin", "log"] = "lin",
    dc: float = 0,
    aa: Union[int, bool] = 0,
    samples: int = 0,
    lfo: bool = False,
    lforange: int = 1,
    lforate: float = 0.5,
) -> Stream:
    """
    Reduce audio bit resolution.

    This filter is a bit crusher with enhanced functionality. A bit crusher
    is used to audibly reduce the number of bits an audio signal is sampled with. This doesn't change the bit depth at all, it just produces the effect. Material reduced in bit depth sounds more harsh and "digital". This filter is able to even round to continuous values instead of discrete bit depths.
    Additionally, it has a D/C offset which results in different crushing of the lower and the upper half of the signal. An Anti-Aliasing setting is able to produce "softer" crushing sounds.

    Another feature of this filter is the logarithmic mode. This setting switches from linear distances between bits to logarithmic ones. The result is a much more "natural" sounding crusher that doesn't gate low signals, for example. The human ear has a logarithmic perception, so this kind of crushing is much more pleasant. Logarithmic crushing is also able to get anti-aliased.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        level_in : float, optional
            Set level in. Default is 0.5.
        level_out : float, optional
            Set level out. Default is 0.5.
        bits : int, optional
            Set bit reduction. Default is 8.
        mix : float, optional
            Set mixing amount. Default is 0.5.
        mode : str, optional
            Can be 'lin' for linear or 'log' for logarithmic. Default is 'lin'.
        dc : float, optional
            Set DC. Default is 0.
        aa : Union[int, bool], optional
            Set anti-aliasing. Default is 0.
        samples : int, optional
            Set sample reduction. Default is 0.
        lfo : bool, optional
            Enable LFO. Default is False.
        lforange : int, optional
            Set LFO range. Default is 1.
        lforate : float, optional
            Set LFO rate. Default is 0.5.

    Example usage:
    --------------
    stream.acrusher(bits=4, mix=0.8, mode="log")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrusher
    """
    return FilterNode(
        stream,
        acrusher.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "bits": bits,
            "mix": mix,
            "mode": mode,
            "dc": dc,
            "aa": aa,
            "samples": samples,
            "lfo": lfo,
            "lforange": lforange,
            "lforate": lforate,
        },
    ).stream()
