from ..node import FilterNode
from ..stream import Stream


def afir(
    stream: Stream,
    dry: float = 1.0,
    wet: float = 1.0,
    length: int = 1,
    gtype: str = "deprecated",
    irnorm: float = 1.0,
    irlink: bool = True,
    irgain: float = 1.0,
    irfmt: str = "input",
    maxir: float = 30.0,
    response: str = "deprecated",
    channel: str = "deprecated",
    size: int = "deprecated",
    rate: int = "deprecated",
    minp: int = 8192,
    maxp: int = 8192,
    nbirs: int = 1,
    ir: int = 0,
    precision: str = "auto",
    irload: str = "init",
) -> Stream:
    """
    Apply an arbitrary Finite Impulse Response filter.

    This filter is designed for applying long FIR filters, up to 60 seconds long.

    It can be used as component for digital crossover filters, room equalization, cross talk cancellation, wavefield synthesis, auralization, ambiophonics, ambisonics and spatialization.

    This filter uses the streams higher than first one as FIR coefficients. If the non-first stream holds a single channel, it will be used for all input channels in the first stream, otherwise the number of channels in the non-first stream must be same as the number of channels in the first stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    dry : float, optional
        Set dry gain. This sets input gain.
        Default is 1.0.
    wet : float, optional
        Set wet gain. This sets final output gain.
        Default is 1.0.
    length : int, optional
        Set Impulse Response filter length. Default is 1, which means whole IR is processed.
        Default is 1.
    gtype : str, optional
        This option is deprecated, and does nothing.
        Default is 'deprecated'.
    irnorm : float, optional
        Set norm to be applied to IR coefficients before filtering. Allowed range is from -1 to 2.
        IR coefficients are normalized with calculated vector norm set by this option. For negative values, no norm is calculated, and IR coefficients are not modified at all.
        Default is 1.0.
    irlink : bool, optional
        For multichannel IR if this option is set to True, all IR channels will be normalized with maximal measured gain of all IR channels coefficients as set by irnorm option. When disabled, all IR coefficients in each IR channel will be normalized independently.
        Default is True.
    irgain : float, optional
        Set gain to be applied to IR coefficients before filtering. Allowed range is 0 to 1. This gain is applied after any gain applied with irnorm option.
        Default is 1.0.
    irfmt : str, optional
        Set format of IR stream. Can be 'mono' or 'input'.
        Default is 'input'.
    maxir : float, optional
        Set max allowed Impulse Response filter duration in seconds. Default is 30 seconds. Allowed range is 0.1 to 60 seconds.
        Default is 30.0.
    response : str, optional
        This option is deprecated, and does nothing.
        Default is 'deprecated'.
    channel : str, optional
        This option is deprecated, and does nothing.
        Default is 'deprecated'.
    size : int, optional
        This option is deprecated, and does nothing.
        Default is 'deprecated'.
    rate : int, optional
        This option is deprecated, and does nothing.
        Default is 'deprecated'.
    minp : int, optional
        Set minimal partition size used for convolution. Default is 8192. Allowed range is from 1 to 65536.
        Lower values decreases latency at cost of higher CPU usage.
        Default is 8192.
    maxp : int, optional
        Set maximal partition size used for convolution. Default is 8192. Allowed range is from 8 to 65536. Lower values may increase CPU usage.
        Default is 8192.
    nbirs : int, optional
        Set number of input impulse responses streams which will be switchable at runtime. Allowed range is from 1 to 32. Default is 1.
        Default is 1.
    ir : int, optional
        Set IDIR stream which will be used for convolution, starting from 0, should always be lower than supplied value by nbirs option. Default is 0. This option can be changed at runtime via commands.
        Default is 0.
    precision : str, optional
        Set which precision to use when processing samples.

        'auto': Auto pick internal sample format depending on other filters.
        'float': Always use single-floating point precision sample format.
        'double': Always use double-floating point precision sample format.

        Default is 'auto'.
    irload : str, optional
        Set when to load IR stream. Can be 'init' or 'access'.
        First one loads and prepares all IRs on initialization, second one once on first access of specific IR.
        Default is 'init'.

    Example usage:
    --------------
    stream.afir(
        wet=0.5,
        length=10,
        minp=4096,
        maxp=16384,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afir
    """
    return FilterNode(
        stream,
        afir.__name__,
        kwargs={
            "dry": dry,
            "wet": wet,
            "length": length,
            "gtype": gtype,
            "irnorm": irnorm,
            "irlink": irlink,
            "irgain": irgain,
            "irfmt": irfmt,
            "maxir": maxir,
            "response": response,
            "channel": channel,
            "size": size,
            "rate": rate,
            "minp": minp,
            "maxp": maxp,
            "nbirs": nbirs,
            "ir": ir,
            "precision": precision,
            "irload": irload,
        },
    ).stream()
