import re
from typing import Any, Literal

from .nodes.nodes import FilterableStream, FilterNode
from .schema import Default, StreamType
from .streams.audio import AudioStream
from .streams.video import VideoStream


def aap(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int | str = Default(16),
    projection: int | str = Default(2),
    mu: float | int | str = Default(0.0001),
    delta: float | int | str = Default(0.001),
    out_mode: int | Literal["i", "d", "o", "n", "e"] | Default = Default("OUT_MODE"),
    precision: int | Literal["auto", "float", "double"] | Default = Default(0),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    ### 8.1 aap

    Apply Affine Projection algorithm to the first audio stream using the second
    audio stream.

    This adaptive filter is used to estimate unknown audio based on multiple input
    audio samples. Affine projection algorithm can make trade-offs between
    computation complexity with convergence speed.

    A description of the accepted options follows.

    **order**

        Set the filter order.

    **projection**

        Set the projection order.

    **mu**

        Set the filter mu.

    **delta**

        Set the coefficient to initialize internal covariance matrix.

    **out_mode**

        Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.

    **precision**

        Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



    Parameters:
    ----------

    :param int order: Set the filter order.
    :param int projection: Set the projection order.
    :param float mu: Set the filter mu.
    :param float delta: Set the coefficient to initialize internal covariance matrix.
    :param int out_mode: Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aap

    """
    filter_node = FilterNode(
        name="aap",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input,
            _desired,
        ),
        kwargs=tuple(
            (
                {
                    "order": order,
                    "projection": projection,
                    "mu": mu,
                    "delta": delta,
                    "out_mode": out_mode,
                    "precision": precision,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def acrossfade(
    _crossfade0: "AudioStream",
    _crossfade1: "AudioStream",
    *,
    nb_samples: int | str = Default("44100"),
    duration: str | float | int = Default("0"),
    overlap: bool | int | str = Default("true"),
    curve1: int
    | Literal[
        "nofade",
        "tri",
        "qsin",
        "esin",
        "hsin",
        "log",
        "ipar",
        "qua",
        "cub",
        "squ",
        "cbr",
        "par",
        "exp",
        "iqsin",
        "ihsin",
        "dese",
        "desi",
        "losi",
        "sinc",
        "isinc",
    ]
    | Default = Default("tri"),
    curve2: int
    | Literal[
        "nofade",
        "tri",
        "qsin",
        "esin",
        "hsin",
        "log",
        "ipar",
        "qua",
        "cub",
        "squ",
        "cbr",
        "par",
        "exp",
        "iqsin",
        "ihsin",
        "dese",
        "desi",
        "losi",
        "sinc",
        "isinc",
    ]
    | Default = Default("tri"),
    **kwargs: Any
) -> "AudioStream":
    """

    Cross fade two input audio streams.

    Parameters:
    ----------

    :param int nb_samples: set number of samples for cross fade duration (from 1 to 2.14748e+08) (default 44100)
    :param str duration: set cross fade duration (default 0)
    :param bool overlap: overlap 1st stream end with 2nd stream start (default true)
    :param int curve1: set fade curve type for 1st stream (from -1 to 18) (default tri)
    :param int curve2: set fade curve type for 2nd stream (from -1 to 18) (default tri)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossfade

    """
    filter_node = FilterNode(
        name="acrossfade",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _crossfade0,
            _crossfade1,
        ),
        kwargs=tuple(
            (
                {
                    "nb_samples": nb_samples,
                    "duration": duration,
                    "overlap": overlap,
                    "curve1": curve1,
                    "curve2": curve2,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def afir(
    *streams: "AudioStream",
    dry: float | int | str = Default("1"),
    wet: float | int | str = Default("1"),
    length: float | int | str = Default("1"),
    gtype: int | Literal["none", "peak", "dc", "gn", "ac", "rms"] | Default = Default("peak"),
    irgain: float | int | str = Default("1"),
    irfmt: int | Literal["mono", "input"] | Default = Default("input"),
    maxir: float | int | str = Default("30"),
    response: bool | int | str = Default("false"),
    channel: int | str = Default("0"),
    size: str | float | int = Default('"hd720"'),
    rate: str | float | int = Default('"25"'),
    minp: int | str = Default("8192"),
    maxp: int | str = Default("8192"),
    nbirs: int | str = Default("1"),
    ir: int | str = Default("0"),
    precision: int | Literal["auto", "float", "double"] | Default = Default("auto"),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply Finite Impulse Response filter with supplied coefficients in additional stream(s).

    Parameters:
    ----------

    :param float dry: set dry gain (from 0 to 10) (default 1)
    :param float wet: set wet gain (from 0 to 10) (default 1)
    :param float length: set IR length (from 0 to 1) (default 1)
    :param int gtype: set IR auto gain type (from -1 to 4) (default peak)
    :param float irgain: set IR gain (from 0 to 1) (default 1)
    :param int irfmt: set IR format (from 0 to 1) (default input)
    :param float maxir: set max IR length (from 0.1 to 60) (default 30)
    :param bool response: show IR frequency response (default false)
    :param int channel: set IR channel to display frequency response (from 0 to 1024) (default 0)
    :param str size: set video size (default "hd720")
    :param str rate: set video rate (default "25")
    :param int minp: set min partition size (from 1 to 65536) (default 8192)
    :param int maxp: set max partition size (from 8 to 65536) (default 8192)
    :param int nbirs: set number of input IRs (from 1 to 32) (default 1)
    :param int ir: select IR (from 0 to 31) (default 0)
    :param int precision: set processing precision (from 0 to 2) (default auto)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afir

    """
    filter_node = FilterNode(
        name="afir",
        input_typings=tuple([StreamType.audio] * int(nbirs)),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "dry": dry,
                    "wet": wet,
                    "length": length,
                    "gtype": gtype,
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
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def ainterleave(
    *streams: "AudioStream",
    nb_inputs: int | str = Default("2"),
    duration: int | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    **kwargs: Any
) -> "AudioStream":
    """

    Temporally interleave audio inputs.

    Parameters:
    ----------

    :param int nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    :param int duration: how to determine the end-of-stream (from 0 to 2) (default longest)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave

    """
    filter_node = FilterNode(
        name="ainterleave",
        input_typings=tuple([StreamType.video] * int(nb_inputs)),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "nb_inputs": nb_inputs,
                    "duration": duration,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def alphamerge(
    _main: "VideoStream",
    _alpha: "VideoStream",
    *,
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Copy the luma value of the second input into the alpha channel of the first input.

    Parameters:
    ----------

    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#alphamerge

    """
    filter_node = FilterNode(
        name="alphamerge",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _alpha,
        ),
        kwargs=tuple(
            (
                {
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def amerge(*streams: "AudioStream", inputs: int | str = Default("2"), **kwargs: Any) -> "AudioStream":
    """

    Merge two or more audio streams into a single multi-channel stream.

    Parameters:
    ----------

    :param int inputs: specify the number of inputs (from 1 to 64) (default 2)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amerge

    """
    filter_node = FilterNode(
        name="amerge",
        input_typings=tuple([StreamType.audio] * int(inputs)),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def amix(
    *streams: "AudioStream",
    inputs: int | str = Default("2"),
    duration: int | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    dropout_transition: float | int | str = Default("2"),
    weights: str | float | int = Default('"1 1"'),
    normalize: bool | int | str = Default("true"),
    **kwargs: Any
) -> "AudioStream":
    """

    Audio mixing.

    Parameters:
    ----------

    :param int inputs: Number of inputs. (from 1 to 32767) (default 2)
    :param int duration: How to determine the end-of-stream. (from 0 to 2) (default longest)
    :param float dropout_transition: Transition time, in seconds, for volume renormalization when an input stream ends. (from 0 to INT_MAX) (default 2)
    :param str weights: Set weight for each input. (default "1 1")
    :param bool normalize: Scale inputs (default true)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amix

    """
    filter_node = FilterNode(
        name="amix",
        input_typings=tuple([StreamType.audio] * int(inputs)),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "duration": duration,
                    "dropout_transition": dropout_transition,
                    "weights": weights,
                    "normalize": normalize,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def amultiply(_multiply0: "AudioStream", _multiply1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    Multiply two audio streams.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#amultiply

    """
    filter_node = FilterNode(
        name="amultiply",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _multiply0,
            _multiply1,
        ),
        kwargs=tuple(({} | kwargs).items()),
    )
    return filter_node.audio(0)


def anlmf(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int | str = Default("256"),
    mu: float | int | str = Default("0.75"),
    eps: float | int | str = Default("1"),
    leakage: float | int | str = Default("0"),
    out_mode: int | Literal["i", "d", "o", "n"] | Default = Default("o"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply Normalized Least-Mean-Fourth algorithm to first audio stream.

    Parameters:
    ----------

    :param int order: set the filter order (from 1 to 32767) (default 256)
    :param float mu: set the filter mu (from 0 to 2) (default 0.75)
    :param float eps: set the filter eps (from 0 to 1) (default 1)
    :param float leakage: set the filter leakage (from 0 to 1) (default 0)
    :param int out_mode: set output mode (from 0 to 3) (default o)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

    """
    filter_node = FilterNode(
        name="anlmf",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input,
            _desired,
        ),
        kwargs=tuple(
            (
                {
                    "order": order,
                    "mu": mu,
                    "eps": eps,
                    "leakage": leakage,
                    "out_mode": out_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def anlms(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int | str = Default("256"),
    mu: float | int | str = Default("0.75"),
    eps: float | int | str = Default("1"),
    leakage: float | int | str = Default("0"),
    out_mode: int | Literal["i", "d", "o", "n"] | Default = Default("o"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply Normalized Least-Mean-Squares algorithm to first audio stream.

    Parameters:
    ----------

    :param int order: set the filter order (from 1 to 32767) (default 256)
    :param float mu: set the filter mu (from 0 to 2) (default 0.75)
    :param float eps: set the filter eps (from 0 to 1) (default 1)
    :param float leakage: set the filter leakage (from 0 to 1) (default 0)
    :param int out_mode: set output mode (from 0 to 3) (default o)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

    """
    filter_node = FilterNode(
        name="anlms",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input,
            _desired,
        ),
        kwargs=tuple(
            (
                {
                    "order": order,
                    "mu": mu,
                    "eps": eps,
                    "leakage": leakage,
                    "out_mode": out_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def apsnr(
    _input0: "AudioStream", _input1: "AudioStream", *, enable: str | float | int = Default(None), **kwargs: Any
) -> "AudioStream":
    """

    ### 8.44 apsnr

    Measure Audio Peak Signal-to-Noise Ratio.

    This filter takes two audio streams for input, and outputs first audio stream.
    Results are in dB per channel at end of either input.



    Parameters:
    ----------

    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#apsnr

    """
    filter_node = FilterNode(
        name="apsnr",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input0,
            _input1,
        ),
        kwargs=tuple(
            (
                {
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def arls(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int | str = Default(16),
    _lambda: float | int | str = Default("1.f"),
    delta: float | int | str = Default("2.f"),
    out_mode: int | Literal["i", "d", "o", "n", "e"] | Default = Default("OUT_MODE"),
    precision: int | Literal["auto", "float", "double"] | Default = Default(0),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    ### 8.49 arls

    Apply Recursive Least Squares algorithm to the first audio stream using the
    second audio stream.

    This adaptive filter is used to mimic a desired filter by recursively finding
    the filter coefficients that relate to producing the minimal weighted linear
    least squares cost function of the error signal (difference between the
    desired, 2nd input audio stream and the actual signal, the 1st input audio
    stream).

    A description of the accepted options follows.

    **order**

        Set the filter order.

    **lambda**

        Set the forgetting factor.

    **delta**

        Set the coefficient to initialize internal covariance matrix.

    **out_mode**

        Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.

    **precision**

        Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



    Parameters:
    ----------

    :param int order: Set the filter order.
    :param float _lambda: Set the forgetting factor.
    :param float delta: Set the coefficient to initialize internal covariance matrix.
    :param int out_mode: Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#arls

    """
    filter_node = FilterNode(
        name="arls",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input,
            _desired,
        ),
        kwargs=tuple(
            (
                {
                    "order": order,
                    "lambda": _lambda,
                    "delta": delta,
                    "out_mode": out_mode,
                    "precision": precision,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def asdr(_input0: "AudioStream", _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    Measure Audio Signal-to-Distortion Ratio.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#asdr

    """
    filter_node = FilterNode(
        name="asdr",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input0,
            _input1,
        ),
        kwargs=tuple(({} | kwargs).items()),
    )
    return filter_node.audio(0)


def asisdr(
    _input0: "AudioStream", _input1: "AudioStream", *, enable: str | float | int = Default(None), **kwargs: Any
) -> "AudioStream":
    """

    ### 8.55 asisdr

    Measure Audio Scaled-Invariant Signal-to-Distortion Ratio.

    This filter takes two audio streams for input, and outputs first audio stream.
    Results are in dB per channel at end of either input.



    Parameters:
    ----------

    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asisdr

    """
    filter_node = FilterNode(
        name="asisdr",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _input0,
            _input1,
        ),
        kwargs=tuple(
            (
                {
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def astreamselect(
    *streams: "AudioStream", inputs: int | str = Default("2"), map: str | float | int = Default(None), **kwargs: Any
) -> FilterNode:
    """

    Select audio streams

    Parameters:
    ----------

    :param int inputs: number of input streams (from 2 to INT_MAX) (default 2)
    :param str map: input indexes to remap to outputs

    Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

    """
    filter_node = FilterNode(
        name="astreamselect",
        input_typings=tuple([StreamType.audio] * int(inputs)),
        output_typings=tuple([StreamType.audio] * len(re.findall(r"\d+", str(map)))),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "map": map,
                }
                | kwargs
            ).items()
        ),
    )

    return filter_node


def axcorrelate(
    _axcorrelate0: "AudioStream",
    _axcorrelate1: "AudioStream",
    *,
    size: int | str = Default("256"),
    algo: int | Literal["slow", "fast"] | Default = Default("slow"),
    **kwargs: Any
) -> "AudioStream":
    """

    Cross-correlate two audio streams.

    Parameters:
    ----------

    :param int size: set segment size (from 2 to 131072) (default 256)
    :param int algo: set algorithm (from 0 to 1) (default slow)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#axcorrelate

    """
    filter_node = FilterNode(
        name="axcorrelate",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _axcorrelate0,
            _axcorrelate1,
        ),
        kwargs=tuple(
            (
                {
                    "size": size,
                    "algo": algo,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def blend(
    _top: "VideoStream",
    _bottom: "VideoStream",
    *,
    c0_mode: int
    | Literal[
        "addition",
        "addition128",
        "grainmerge",
        "and",
        "average",
        "burn",
        "darken",
        "difference",
        "difference128",
        "grainextract",
        "divide",
        "dodge",
        "exclusion",
        "extremity",
        "freeze",
        "glow",
        "hardlight",
        "hardmix",
        "heat",
        "lighten",
        "linearlight",
        "multiply",
        "multiply128",
        "negation",
        "normal",
        "or",
        "overlay",
        "phoenix",
        "pinlight",
        "reflect",
        "screen",
        "softlight",
        "subtract",
        "vividlight",
        "xor",
        "softdifference",
        "geometric",
        "harmonic",
        "bleach",
        "stain",
        "interpolate",
        "hardoverlay",
    ]
    | Default = Default("normal"),
    c1_mode: int
    | Literal[
        "addition",
        "addition128",
        "grainmerge",
        "and",
        "average",
        "burn",
        "darken",
        "difference",
        "difference128",
        "grainextract",
        "divide",
        "dodge",
        "exclusion",
        "extremity",
        "freeze",
        "glow",
        "hardlight",
        "hardmix",
        "heat",
        "lighten",
        "linearlight",
        "multiply",
        "multiply128",
        "negation",
        "normal",
        "or",
        "overlay",
        "phoenix",
        "pinlight",
        "reflect",
        "screen",
        "softlight",
        "subtract",
        "vividlight",
        "xor",
        "softdifference",
        "geometric",
        "harmonic",
        "bleach",
        "stain",
        "interpolate",
        "hardoverlay",
    ]
    | Default = Default("normal"),
    c2_mode: int
    | Literal[
        "addition",
        "addition128",
        "grainmerge",
        "and",
        "average",
        "burn",
        "darken",
        "difference",
        "difference128",
        "grainextract",
        "divide",
        "dodge",
        "exclusion",
        "extremity",
        "freeze",
        "glow",
        "hardlight",
        "hardmix",
        "heat",
        "lighten",
        "linearlight",
        "multiply",
        "multiply128",
        "negation",
        "normal",
        "or",
        "overlay",
        "phoenix",
        "pinlight",
        "reflect",
        "screen",
        "softlight",
        "subtract",
        "vividlight",
        "xor",
        "softdifference",
        "geometric",
        "harmonic",
        "bleach",
        "stain",
        "interpolate",
        "hardoverlay",
    ]
    | Default = Default("normal"),
    c3_mode: int
    | Literal[
        "addition",
        "addition128",
        "grainmerge",
        "and",
        "average",
        "burn",
        "darken",
        "difference",
        "difference128",
        "grainextract",
        "divide",
        "dodge",
        "exclusion",
        "extremity",
        "freeze",
        "glow",
        "hardlight",
        "hardmix",
        "heat",
        "lighten",
        "linearlight",
        "multiply",
        "multiply128",
        "negation",
        "normal",
        "or",
        "overlay",
        "phoenix",
        "pinlight",
        "reflect",
        "screen",
        "softlight",
        "subtract",
        "vividlight",
        "xor",
        "softdifference",
        "geometric",
        "harmonic",
        "bleach",
        "stain",
        "interpolate",
        "hardoverlay",
    ]
    | Default = Default("normal"),
    all_mode: int
    | Literal[
        "addition",
        "addition128",
        "grainmerge",
        "and",
        "average",
        "burn",
        "darken",
        "difference",
        "difference128",
        "grainextract",
        "divide",
        "dodge",
        "exclusion",
        "extremity",
        "freeze",
        "glow",
        "hardlight",
        "hardmix",
        "heat",
        "lighten",
        "linearlight",
        "multiply",
        "multiply128",
        "negation",
        "normal",
        "or",
        "overlay",
        "phoenix",
        "pinlight",
        "reflect",
        "screen",
        "softlight",
        "subtract",
        "vividlight",
        "xor",
        "softdifference",
        "geometric",
        "harmonic",
        "bleach",
        "stain",
        "interpolate",
        "hardoverlay",
    ]
    | Default = Default("-1"),
    c0_expr: str | float | int = Default(None),
    c1_expr: str | float | int = Default(None),
    c2_expr: str | float | int = Default(None),
    c3_expr: str | float | int = Default(None),
    all_expr: str | float | int = Default(None),
    c0_opacity: float | int | str = Default("1"),
    c1_opacity: float | int | str = Default("1"),
    c2_opacity: float | int | str = Default("1"),
    c3_opacity: float | int | str = Default("1"),
    all_opacity: float | int | str = Default("1"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Blend two video frames into each other.

    Parameters:
    ----------

    :param int c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
    :param int c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
    :param int c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
    :param int c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
    :param int all_mode: set blend mode for all components (from -1 to 39) (default -1)
    :param str c0_expr: set color component #0 expression
    :param str c1_expr: set color component #1 expression
    :param str c2_expr: set color component #2 expression
    :param str c3_expr: set color component #3 expression
    :param str all_expr: set expression for all color components
    :param float c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
    :param float c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
    :param float c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
    :param float c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
    :param float all_opacity: set opacity for all color components (from 0 to 1) (default 1)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#blend

    """
    filter_node = FilterNode(
        name="blend",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _top,
            _bottom,
        ),
        kwargs=tuple(
            (
                {
                    "c0_mode": c0_mode,
                    "c1_mode": c1_mode,
                    "c2_mode": c2_mode,
                    "c3_mode": c3_mode,
                    "all_mode": all_mode,
                    "c0_expr": c0_expr,
                    "c1_expr": c1_expr,
                    "c2_expr": c2_expr,
                    "c3_expr": c3_expr,
                    "all_expr": all_expr,
                    "c0_opacity": c0_opacity,
                    "c1_opacity": c1_opacity,
                    "c2_opacity": c2_opacity,
                    "c3_opacity": c3_opacity,
                    "all_opacity": all_opacity,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def blend_vulkan(
    _top: "VideoStream",
    _bottom: "VideoStream",
    *,
    c0_mode: int | Literal["normal", "multiply"] | Default = Default(0),
    c1_mode: int | Literal["normal", "multiply"] | Default = Default(0),
    c2_mode: int | Literal["normal", "multiply"] | Default = Default(0),
    c3_mode: int | Literal["normal", "multiply"] | Default = Default(0),
    all_mode: int | Literal["normal", "multiply"] | Default = Default(-1),
    c0_opacity: float | int | str = Default(1.0),
    c1_opacity: float | int | str = Default(1.0),
    c2_opacity: float | int | str = Default(1.0),
    c3_opacity: float | int | str = Default(1.0),
    all_opacity: float | int | str = Default(1.0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 14.2 blend_vulkan

    Blend two Vulkan frames into each other.

    The `blend` filter takes two input streams and outputs one stream, the first
    input is the "top" layer and second input is "bottom" layer. By default, the
    output terminates when the longest input terminates.

    A description of the accepted options follows.

    **c0_mode**

    **c1_mode**

    **c2_mode**

    **c3_mode**

    **all_mode**

        Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’



    Parameters:
    ----------

    :param int c0_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c1_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c2_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c3_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int all_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param float c0_opacity: set color component #0 opacity
    :param float c1_opacity: set color component #1 opacity
    :param float c2_opacity: set color component #2 opacity
    :param float c3_opacity: set color component #3 opacity
    :param float all_opacity: set opacity for all color components

    Ref: https://ffmpeg.org/ffmpeg-filters.html#blend_005fvulkan

    """
    filter_node = FilterNode(
        name="blend_vulkan",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _top,
            _bottom,
        ),
        kwargs=tuple(
            (
                {
                    "c0_mode": c0_mode,
                    "c1_mode": c1_mode,
                    "c2_mode": c2_mode,
                    "c3_mode": c3_mode,
                    "all_mode": all_mode,
                    "c0_opacity": c0_opacity,
                    "c1_opacity": c1_opacity,
                    "c2_opacity": c2_opacity,
                    "c3_opacity": c3_opacity,
                    "all_opacity": all_opacity,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def bm3d(
    *streams: "VideoStream",
    sigma: float | int | str = Default("1"),
    block: int | str = Default("16"),
    bstep: int | str = Default("4"),
    group: int | str = Default("1"),
    range: int | str = Default("9"),
    mstep: int | str = Default("1"),
    thmse: float | int | str = Default("0"),
    hdthr: float | int | str = Default("2.7"),
    estim: int | Literal["basic", "final"] | Default = Default("basic"),
    ref: bool | int | str = Default("false"),
    planes: int | str = Default("7"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Block-Matching 3D denoiser.

    Parameters:
    ----------

    :param float sigma: set denoising strength (from 0 to 99999.9) (default 1)
    :param int block: set size of local patch (from 8 to 64) (default 16)
    :param int bstep: set sliding step for processing blocks (from 1 to 64) (default 4)
    :param int group: set maximal number of similar blocks (from 1 to 256) (default 1)
    :param int range: set block matching range (from 1 to INT_MAX) (default 9)
    :param int mstep: set step for block matching (from 1 to 64) (default 1)
    :param float thmse: set threshold of mean square error for block matching (from 0 to INT_MAX) (default 0)
    :param float hdthr: set hard threshold for 3D transfer domain (from 0 to INT_MAX) (default 2.7)
    :param int estim: set filtering estimation mode (from 0 to 1) (default basic)
    :param bool ref: have reference stream (default false)
    :param int planes: set planes to filter (from 0 to 15) (default 7)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bm3d

    """
    filter_node = FilterNode(
        name="bm3d",
        input_typings=tuple([StreamType.video] + [StreamType.video] if ref else []),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "sigma": sigma,
                    "block": block,
                    "bstep": bstep,
                    "group": group,
                    "range": range,
                    "mstep": mstep,
                    "thmse": thmse,
                    "hdthr": hdthr,
                    "estim": estim,
                    "ref": ref,
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def colormap(
    _default: "VideoStream",
    _source: "VideoStream",
    _target: "VideoStream",
    *,
    patch_size: str | float | int = Default('"64x64"'),
    nb_patches: int | str = Default("0"),
    type: int | Literal["relative", "absolute"] | Default = Default("absolute"),
    kernel: int | Literal["euclidean", "weuclidean"] | Default = Default("euclidean"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply custom Color Maps to video stream.

    Parameters:
    ----------

    :param str patch_size: set patch size (default "64x64")
    :param int nb_patches: set number of patches (from 0 to 64) (default 0)
    :param int type: set the target type used (from 0 to 1) (default absolute)
    :param int kernel: set the kernel used for measuring color difference (from 0 to 1) (default euclidean)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#colormap

    """
    filter_node = FilterNode(
        name="colormap",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _default,
            _source,
            _target,
        ),
        kwargs=tuple(
            (
                {
                    "patch_size": patch_size,
                    "nb_patches": nb_patches,
                    "type": type,
                    "kernel": kernel,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def concat(
    *streams: "FilterableStream",
    n: int | str = Default("2"),
    v: int | str = Default("1"),
    a: int | str = Default("0"),
    unsafe: bool | int | str = Default("false"),
    **kwargs: Any
) -> FilterNode:
    """

    Concatenate audio and video streams.

    Parameters:
    ----------

    :param int n: specify the number of segments (from 1 to INT_MAX) (default 2)
    :param int v: specify the number of video streams (from 0 to INT_MAX) (default 1)
    :param int a: specify the number of audio streams (from 0 to INT_MAX) (default 0)
    :param bool unsafe: enable unsafe mode (default false)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#concat

    """
    filter_node = FilterNode(
        name="concat",
        input_typings=tuple(([StreamType.video] * int(v) + [StreamType.audio] * int(a)) * int(n)),
        output_typings=tuple([StreamType.video] * int(v) + [StreamType.audio] * int(a)),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "n": n,
                    "v": v,
                    "a": a,
                    "unsafe": unsafe,
                }
                | kwargs
            ).items()
        ),
    )

    return filter_node


def convolve(
    _main: "VideoStream",
    _impulse: "VideoStream",
    *,
    planes: int | str = Default("7"),
    impulse: int | Literal["first", "all"] | Default = Default("all"),
    noise: float | int | str = Default("1e-07"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Convolve first video stream with second video stream.

    Parameters:
    ----------

    :param int planes: set planes to convolve (from 0 to 15) (default 7)
    :param int impulse: when to process impulses (from 0 to 1) (default all)
    :param float noise: set noise (from 0 to 1) (default 1e-07)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#convolve

    """
    filter_node = FilterNode(
        name="convolve",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _impulse,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "impulse": impulse,
                    "noise": noise,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def corr(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the correlation between two video streams.

    Parameters:
    ----------

    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#corr

    """
    filter_node = FilterNode(
        name="corr",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def decimate(
    *streams: "VideoStream",
    cycle: int | str = Default("5"),
    dupthresh: float | int | str = Default("1.1"),
    scthresh: float | int | str = Default("15"),
    blockx: int | str = Default("32"),
    blocky: int | str = Default("32"),
    ppsrc: bool | int | str = Default("false"),
    chroma: bool | int | str = Default("true"),
    mixed: bool | int | str = Default("false"),
    **kwargs: Any
) -> "VideoStream":
    """

    Decimate frames (post field matching filter).

    Parameters:
    ----------

    :param int cycle: set the number of frame from which one will be dropped (from 2 to 25) (default 5)
    :param float dupthresh: set duplicate threshold (from 0 to 100) (default 1.1)
    :param float scthresh: set scene change threshold (from 0 to 100) (default 15)
    :param int blockx: set the size of the x-axis blocks used during metric calculations (from 4 to 512) (default 32)
    :param int blocky: set the size of the y-axis blocks used during metric calculations (from 4 to 512) (default 32)
    :param bool ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    :param bool chroma: set whether or not chroma is considered in the metric calculations (default true)
    :param bool mixed: set whether or not the input only partially contains content to be decimated (default false)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#decimate

    """
    filter_node = FilterNode(
        name="decimate",
        input_typings=tuple([StreamType.video] + ([StreamType.video] if ppsrc else [])),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "cycle": cycle,
                    "dupthresh": dupthresh,
                    "scthresh": scthresh,
                    "blockx": blockx,
                    "blocky": blocky,
                    "ppsrc": ppsrc,
                    "chroma": chroma,
                    "mixed": mixed,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def deconvolve(
    _main: "VideoStream",
    _impulse: "VideoStream",
    *,
    planes: int | str = Default("7"),
    impulse: int | Literal["first", "all"] | Default = Default("all"),
    noise: float | int | str = Default("1e-07"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Deconvolve first video stream with second video stream.

    Parameters:
    ----------

    :param int planes: set planes to deconvolve (from 0 to 15) (default 7)
    :param int impulse: when to process impulses (from 0 to 1) (default all)
    :param float noise: set noise (from 0 to 1) (default 1e-07)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#deconvolve

    """
    filter_node = FilterNode(
        name="deconvolve",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _impulse,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "impulse": impulse,
                    "noise": noise,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def displace(
    _source: "VideoStream",
    _xmap: "VideoStream",
    _ymap: "VideoStream",
    *,
    edge: int | Literal["blank", "smear", "wrap", "mirror"] | Default = Default("smear"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Displace pixels.

    Parameters:
    ----------

    :param int edge: set edge mode (from 0 to 3) (default smear)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#displace

    """
    filter_node = FilterNode(
        name="displace",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _xmap,
            _ymap,
        ),
        kwargs=tuple(
            (
                {
                    "edge": edge,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def feedback(
    _default: "VideoStream",
    _feedin: "VideoStream",
    *,
    x: int | str = Default("0"),
    w: int | str = Default("0"),
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    Apply feedback video filter.

    Parameters:
    ----------

    :param int x: set top left crop position (from 0 to INT_MAX) (default 0)
    :param int w: set crop size (from 0 to INT_MAX) (default 0)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#feedback

    """
    filter_node = FilterNode(
        name="feedback",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video, StreamType.video]),
        inputs=(
            _default,
            _feedin,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "w": w,
                }
                | kwargs
            ).items()
        ),
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def fieldmatch(
    *streams: "VideoStream",
    order: int | Literal["auto", "bff", "tff"] | Default = Default("auto"),
    mode: int | Literal["pc", "pc_n", "pc_u", "pc_n_ub", "pcn", "pcn_ub"] | Default = Default("pc_n"),
    ppsrc: bool | int | str = Default("false"),
    field: int | Literal["auto", "bottom", "top"] | Default = Default("auto"),
    mchroma: bool | int | str = Default("true"),
    y0: int | str = Default("0"),
    scthresh: float | int | str = Default("12"),
    combmatch: int | Literal["none", "sc", "full"] | Default = Default("sc"),
    combdbg: int | Literal["none", "pcn", "pcnub"] | Default = Default("none"),
    cthresh: int | str = Default("9"),
    chroma: bool | int | str = Default("false"),
    blockx: int | str = Default("16"),
    blocky: int | str = Default("16"),
    combpel: int | str = Default("80"),
    **kwargs: Any
) -> "VideoStream":
    """

    Field matching for inverse telecine.

    Parameters:
    ----------

    :param int order: specify the assumed field order (from -1 to 1) (default auto)
    :param int mode: set the matching mode or strategy to use (from 0 to 5) (default pc_n)
    :param bool ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    :param int field: set the field to match from (from -1 to 1) (default auto)
    :param bool mchroma: set whether or not chroma is included during the match comparisons (default true)
    :param int y0: define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX) (default 0)
    :param float scthresh: set scene change detection threshold (from 0 to 100) (default 12)
    :param int combmatch: set combmatching mode (from 0 to 2) (default sc)
    :param int combdbg: enable comb debug (from 0 to 2) (default none)
    :param int cthresh: set the area combing threshold used for combed frame detection (from -1 to 255) (default 9)
    :param bool chroma: set whether or not chroma is considered in the combed frame decision (default false)
    :param int blockx: set the x-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    :param int blocky: set the y-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    :param int combpel: set the number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed (from 0 to INT_MAX) (default 80)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldmatch

    """
    filter_node = FilterNode(
        name="fieldmatch",
        input_typings=tuple([StreamType.video] + [StreamType.video] if ppsrc else []),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "order": order,
                    "mode": mode,
                    "ppsrc": ppsrc,
                    "field": field,
                    "mchroma": mchroma,
                    "y0": y0,
                    "scthresh": scthresh,
                    "combmatch": combmatch,
                    "combdbg": combdbg,
                    "cthresh": cthresh,
                    "chroma": chroma,
                    "blockx": blockx,
                    "blocky": blocky,
                    "combpel": combpel,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def framepack(
    _left: "VideoStream",
    _right: "VideoStream",
    *,
    format: int | Literal["sbs", "tab", "frameseq", "lines", "columns"] | Default = Default("sbs"),
    **kwargs: Any
) -> "VideoStream":
    """

    Generate a frame packed stereoscopic video.

    Parameters:
    ----------

    :param int format: Frame pack output format (from 0 to INT_MAX) (default sbs)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#framepack

    """
    filter_node = FilterNode(
        name="framepack",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _left,
            _right,
        ),
        kwargs=tuple(
            (
                {
                    "format": format,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def freezeframes(
    _source: "VideoStream",
    _replace: "VideoStream",
    *,
    first: int | str = Default("0"),
    last: int | str = Default("0"),
    replace: int | str = Default("0"),
    **kwargs: Any
) -> "VideoStream":
    """

    Freeze video frames.

    Parameters:
    ----------

    :param int first: set first frame to freeze (from 0 to I64_MAX) (default 0)
    :param int last: set last frame to freeze (from 0 to I64_MAX) (default 0)
    :param int replace: set frame to replace (from 0 to I64_MAX) (default 0)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#freezeframes

    """
    filter_node = FilterNode(
        name="freezeframes",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _replace,
        ),
        kwargs=tuple(
            (
                {
                    "first": first,
                    "last": last,
                    "replace": replace,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def guided(
    *streams: "VideoStream",
    radius: int | str = Default("3"),
    eps: float | int | str = Default("0.01"),
    mode: int | Literal["basic", "fast"] | Default = Default("basic"),
    sub: int | str = Default("4"),
    guidance: int | Literal["off", "on"] | Default = Default("off"),
    planes: int | str = Default("1"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Guided filter.

    Parameters:
    ----------

    :param int radius: set the box radius (from 1 to 20) (default 3)
    :param float eps: set the regularization parameter (with square) (from 0 to 1) (default 0.01)
    :param int mode: set filtering mode (0: basic mode; 1: fast mode) (from 0 to 1) (default basic)
    :param int sub: subsampling ratio for fast mode (from 2 to 64) (default 4)
    :param int guidance: set guidance mode (0: off mode; 1: on mode) (from 0 to 1) (default off)
    :param int planes: set planes to filter (from 0 to 15) (default 1)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#guided

    """
    filter_node = FilterNode(
        name="guided",
        input_typings=tuple([StreamType.video] + [StreamType.video] if guidance else []),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "radius": radius,
                    "eps": eps,
                    "mode": mode,
                    "sub": sub,
                    "guidance": guidance,
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def haldclut(
    _main: "VideoStream",
    _clut: "VideoStream",
    *,
    clut: int | Literal["first", "all"] | Default = Default("all"),
    interp: int | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"] | Default = Default("tetrahedral"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Adjust colors using a Hald CLUT.

    Parameters:
    ----------

    :param int clut: when to process CLUT (from 0 to 1) (default all)
    :param int interp: select interpolation mode (from 0 to 4) (default tetrahedral)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#haldclut

    """
    filter_node = FilterNode(
        name="haldclut",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _clut,
        ),
        kwargs=tuple(
            (
                {
                    "clut": clut,
                    "interp": interp,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def headphone(
    *streams: "AudioStream",
    map: str | float | int = Default(None),
    gain: float | int | str = Default("0"),
    lfe: float | int | str = Default("0"),
    type: int | Literal["time", "freq"] | Default = Default("freq"),
    size: int | str = Default("1024"),
    hrir: int | Literal["stereo", "multich"] | Default = Default("stereo"),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply headphone binaural spatialization with HRTFs in additional streams.

    Parameters:
    ----------

    :param str map: set channels convolution mappings
    :param float gain: set gain in dB (from -20 to 40) (default 0)
    :param float lfe: set lfe gain in dB (from -20 to 40) (default 0)
    :param int type: set processing (from 0 to 1) (default freq)
    :param int size: set frame size (from 1024 to 96000) (default 1024)
    :param int hrir: set hrir format (from 0 to 1) (default stereo)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#headphone

    """
    filter_node = FilterNode(
        name="headphone",
        input_typings=tuple(
            [StreamType.audio] + [StreamType.audio] * (len(str(map).split("|")) - 1) if int(hrir) == 1 else []
        ),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "map": map,
                    "gain": gain,
                    "lfe": lfe,
                    "type": type,
                    "size": size,
                    "hrir": hrir,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def hstack(
    *streams: "VideoStream",
    inputs: int | str = Default("2"),
    shortest: bool | int | str = Default("false"),
    **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs horizontally.

    Parameters:
    ----------

    :param int inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param bool shortest: force termination when the shortest input terminates (default false)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hstack

    """
    filter_node = FilterNode(
        name="hstack",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def hstack_qsv(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    height: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 15.1 hstack_qsv

    Stack input videos horizontally.

    This is the QSV variant of the hstack filter, each input stream may have
    different height, this filter will scale down/up each input stream while
    keeping the original aspect.

    It accepts the following options:

    **inputs**

        See hstack.

    **shortest**

        See hstack.

    **height**

        Set height of output. If set to 0, this filter will set height of output to height of the first input stream. Default value is 0.



    Parameters:
    ----------

    :param int inputs: See hstack.
    :param bool shortest: See hstack.
    :param int height: Set height of output. If set to 0, this filter will set height of output to height of the first input stream. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hstack_005fqsv

    """
    filter_node = FilterNode(
        name="hstack_qsv",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "height": height,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def hstack_vaapi(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    height: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 13.3 hstack_vaapi

    Stack input videos horizontally.

    This is the VA-API variant of the hstack filter, each input stream may have
    different height, this filter will scale down/up each input stream while
    keeping the original aspect.

    It accepts the following options:

    **inputs**

        See hstack.

    **shortest**

        See hstack.

    **height**

        Set height of output. If set to 0, this filter will set height of output to height of the first input stream. Default value is 0.



    Parameters:
    ----------

    :param int inputs: See hstack.
    :param bool shortest: See hstack.
    :param int height: Set height of output. If set to 0, this filter will set height of output to height of the first input stream. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hstack_005fvaapi

    """
    filter_node = FilterNode(
        name="hstack_vaapi",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "height": height,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def hysteresis(
    _base: "VideoStream",
    _alt: "VideoStream",
    *,
    planes: int | str = Default("15"),
    threshold: int | str = Default("0"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Grow first stream into second stream by connecting components.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param int threshold: set threshold (from 0 to 65535) (default 0)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hysteresis

    """
    filter_node = FilterNode(
        name="hysteresis",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _base,
            _alt,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "threshold": threshold,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def identity(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the Identity between two video streams.

    Parameters:
    ----------

    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#identity

    """
    filter_node = FilterNode(
        name="identity",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def interleave(
    *streams: "VideoStream",
    nb_inputs: int | str = Default("2"),
    duration: int | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    **kwargs: Any
) -> "VideoStream":
    """

    Temporally interleave video inputs.

    Parameters:
    ----------

    :param int nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    :param int duration: how to determine the end-of-stream (from 0 to 2) (default longest)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave

    """
    filter_node = FilterNode(
        name="interleave",
        input_typings=tuple([StreamType.video] * int(nb_inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "nb_inputs": nb_inputs,
                    "duration": duration,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def join(
    *streams: "AudioStream",
    inputs: int | str = Default("2"),
    channel_layout: str | float | int = Default('"stereo"'),
    map: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Join multiple audio streams into multi-channel output.

    Parameters:
    ----------

    :param int inputs: Number of input streams. (from 1 to INT_MAX) (default 2)
    :param str channel_layout: Channel layout of the output stream. (default "stereo")
    :param str map: A comma-separated list of channels maps in the format 'input_stream.input_channel-output_channel.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#join

    """
    filter_node = FilterNode(
        name="join",
        input_typings=tuple([StreamType.audio] * int(inputs)),
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "channel_layout": channel_layout,
                    "map": map,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def ladspa(
    *streams: "AudioStream",
    file: str | float | int = Default(None),
    plugin: str | float | int = Default(None),
    controls: str | float | int = Default(None),
    sample_rate: int | str = Default(44100),
    nb_samples: int | str = Default(1024),
    duration: int | str = Default(-1),
    latency: bool | int | str = Default(0),
    **kwargs: Any
) -> "AudioStream":
    """

    ### 8.96 ladspa

    Load a LADSPA (Linux Audio Developer’s Simple Plugin API) plugin.

    To enable compilation of this filter you need to configure FFmpeg with
    `--enable-ladspa`.

    **file, f**

        Specifies the name of LADSPA plugin library to load. If the environment variable LADSPA_PATH is defined, the LADSPA plugin is searched in each one of the directories specified by the colon separated list in LADSPA_PATH, otherwise in the standard LADSPA paths, which are in this order: HOME/.ladspa/lib/, /usr/local/lib/ladspa/, /usr/lib/ladspa/.

    **plugin, p**

        Specifies the plugin within the library. Some libraries contain only one plugin, but others contain many of them. If this is not set filter will list all available plugins within the specified library.

    **controls, c**

        Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). Controls need to be defined using the following syntax: c0=value0|c1=value1|c2=value2|..., where valuei is the value set on the i-th control. Alternatively they can be also defined using the following syntax: value0|value1|value2|..., where valuei is the value set on the i-th control. If controls is set to help, all available controls and their valid ranges are printed.

    **sample_rate, s**

        Specify the sample rate, default to 44100. Only used if plugin have zero inputs.

    **nb_samples, n**

        Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.

    **duration, d**

        Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.

    **latency, l**

        Enable latency compensation, by default is disabled. Only used if plugin have inputs.



    Parameters:
    ----------

    :param str file: Specifies the name of LADSPA plugin library to load. If the environment variable LADSPA_PATH is defined, the LADSPA plugin is searched in each one of the directories specified by the colon separated list in LADSPA_PATH, otherwise in the standard LADSPA paths, which are in this order: HOME/.ladspa/lib/, /usr/local/lib/ladspa/, /usr/lib/ladspa/.
    :param str plugin: Specifies the plugin within the library. Some libraries contain only one plugin, but others contain many of them. If this is not set filter will list all available plugins within the specified library.
    :param str controls: Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). Controls need to be defined using the following syntax: c0=value0|c1=value1|c2=value2|..., where valuei is the value set on the i-th control. Alternatively they can be also defined using the following syntax: value0|value1|value2|..., where valuei is the value set on the i-th control. If controls is set to help, all available controls and their valid ranges are printed.
    :param int sample_rate: Specify the sample rate, default to 44100. Only used if plugin have zero inputs.
    :param int nb_samples: Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.
    :param int duration: Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.
    :param bool latency: Enable latency compensation, by default is disabled. Only used if plugin have inputs.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#ladspa

    """
    filter_node = FilterNode(
        name="ladspa",
        input_typings=None,
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "file": file,
                    "plugin": plugin,
                    "controls": controls,
                    "sample_rate": sample_rate,
                    "nb_samples": nb_samples,
                    "duration": duration,
                    "latency": latency,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def libplacebo(
    *streams: "VideoStream",
    inputs: int | str = Default(1),
    w: str | float | int = Default("iw"),
    h: str | float | int = Default("ih"),
    fps: str | float | int = Default("none"),
    crop_x: str | float | int = Default("(iw-cw)/2"),
    crop_y: str | float | int = Default("(ih-ch)/2"),
    crop_w: str | float | int = Default("iw"),
    crop_h: str | float | int = Default("ih"),
    pos_x: str | float | int = Default("(ow-pw)/2"),
    pos_y: str | float | int = Default("(oh-ph)/2"),
    pos_w: str | float | int = Default("ow"),
    pos_h: str | float | int = Default("oh"),
    format: str | float | int = Default(None),
    force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
    force_divisible_by: int | str = Default(1),
    normalize_sar: bool | int | str = Default(0),
    pad_crop_ratio: float | int | str = Default(0.0),
    fillcolor: str | float | int = Default("black"),
    corner_rounding: float | int | str = Default(0.0),
    extra_opts: str | float | int = Default(None),
    colorspace: int
    | Literal[
        "auto", "gbr", "bt709", "unknown", "bt470bg", "smpte170m", "smpte240m", "ycgco", "bt2020nc", "bt2020c", "ictcp"
    ]
    | Default = Default(-1),
    range: int
    | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
    | Default = Default(-1),
    color_primaries: int
    | Literal[
        "auto",
        "bt709",
        "unknown",
        "bt470m",
        "bt470bg",
        "smpte170m",
        "smpte240m",
        "film",
        "bt2020",
        "smpte428",
        "smpte431",
        "smpte432",
        "jedec-p22",
        "ebu3213",
    ]
    | Default = Default(-1),
    color_trc: int
    | Literal[
        "auto",
        "bt709",
        "unknown",
        "bt470m",
        "bt470bg",
        "smpte170m",
        "smpte240m",
        "linear",
        "iec61966-2-4",
        "bt1361e",
        "iec61966-2-1",
        "bt2020-10",
        "bt2020-12",
        "smpte2084",
        "arib-std-b67",
    ]
    | Default = Default(-1),
    upscaler: str | float | int = Default("spline36"),
    downscaler: str | float | int = Default("mitchell"),
    frame_mixer: str | float | int = Default("none"),
    lut_entries: int | str = Default(0),
    antiringing: float | int | str = Default(0.0),
    sigmoid: bool | int | str = Default(1),
    apply_filmgrain: bool | int | str = Default(1),
    apply_dolbyvision: bool | int | str = Default(1),
    deband: bool | int | str = Default(0),
    deband_iterations: int | str = Default(1),
    deband_threshold: float | int | str = Default(4.0),
    deband_radius: float | int | str = Default(16.0),
    deband_grain: float | int | str = Default(6.0),
    brightness: float | int | str = Default(0.0),
    contrast: float | int | str = Default(1.0),
    saturation: float | int | str = Default(1.0),
    hue: float | int | str = Default(0.0),
    gamma: float | int | str = Default(1.0),
    peak_detect: bool | int | str = Default(1),
    smoothing_period: float | int | str = Default(100.0),
    minimum_peak: float | int | str = Default(1.0),
    scene_threshold_low: float | int | str = Default(5.5),
    scene_threshold_high: float | int | str = Default(10.0),
    percentile: float | int | str = Default(99.995),
    gamut_mode: int
    | Literal["clip", "perceptual", "relative", "saturation", "absolute", "desaturate", "darken", "warn", "linear"]
    | Default = Default("GAMUT_MAP_PERCEPTUAL"),
    tonemapping: int
    | Literal["auto", "clip", "bt.2390", "bt.2446a", "spline", "reinhard", "mobius", "hable", "gamma", "linear"]
    | Default = Default("TONE_MAP_AUTO"),
    tonemapping_param: float | int | str = Default(0.0),
    inverse_tonemapping: bool | int | str = Default(0),
    tonemapping_lut_size: int | str = Default(256),
    contrast_recovery: float | int | str = Default(0.3),
    contrast_smoothness: float | int | str = Default(3.5),
    desaturation_strength: float | int | str = Default(-1.0),
    desaturation_exponent: float | int | str = Default(-1.0),
    gamut_warning: bool | int | str = Default(0),
    gamut_clipping: bool | int | str = Default(0),
    intent: int
    | Literal["perceptual", "relative", "absolute", "saturation"]
    | Default = Default("PL_INTENT_PERCEPTUAL"),
    tonemapping_mode: int | Literal["auto", "rgb", "max", "hybrid", "luma"] | Default = Default(0),
    tonemapping_crosstalk: float | int | str = Default(0.04),
    overshoot: float | int | str = Default(0.05),
    hybrid_mix: float | int | str = Default(0.2),
    dithering: int
    | Literal["none", "blue", "ordered", "ordered_fixed", "white"]
    | Default = Default("PL_DITHER_BLUE_NOISE"),
    dither_lut_size: int | str = Default(6),
    dither_temporal: bool | int | str = Default(0),
    cones: str | Literal["l", "m", "s"] | Default = Default(0),
    cone_strength: float | int | str = Default(0.0),
    custom_shader_path: str | float | int = Default(None),
    custom_shader_bin: str | float | int = Default(None),
    skip_aa: bool | int | str = Default(0),
    polar_cutoff: float | int | str = Default(0.0),
    disable_linear: bool | int | str = Default(0),
    disable_builtin: bool | int | str = Default(0),
    force_icc_lut: bool | int | str = Default(0),
    force_dither: bool | int | str = Default(0),
    disable_fbos: bool | int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 11.144 libplacebo

    Flexible GPU-accelerated processing filter based on libplacebo
    (<https://code.videolan.org/videolan/libplacebo>).



    Parameters:
    ----------

    :param int inputs: Number of inputs
    :param str w: Output video frame width
    :param str h: Output video frame height
    :param str fps: Output video frame rate
    :param str crop_x: Input video crop x
    :param str crop_y: Input video crop y
    :param str crop_w: Input video crop w
    :param str crop_h: Input video crop h
    :param str pos_x: Output video placement x
    :param str pos_y: Output video placement y
    :param str pos_w: Output video placement w
    :param str pos_h: Output video placement h
    :param str format: Output video format
    :param int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR
    :param int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used
    :param bool normalize_sar: force SAR normalization to 1:1 by adjusting pos_x/y/w/h
    :param float pad_crop_ratio: ratio between padding and cropping when normalizing SAR (0=pad, 1=crop)
    :param str fillcolor: Background fill color
    :param float corner_rounding: Corner rounding radius
    :param str extra_opts: Pass extra libplacebo-specific options using a :-separated list of key=value pairs
    :param int colorspace: select colorspace
    :param int range: select color range
    :param int color_primaries: select color primaries
    :param int color_trc: select color transfer
    :param str upscaler: Upscaler function
    :param str downscaler: Downscaler function
    :param str frame_mixer: Frame mixing function
    :param int lut_entries: Number of scaler LUT entries
    :param float antiringing: Antiringing strength (for non-EWA filters)
    :param bool sigmoid: Enable sigmoid upscaling
    :param bool apply_filmgrain: Apply film grain metadata
    :param bool apply_dolbyvision: Apply Dolby Vision metadata
    :param bool deband: Enable debanding
    :param int deband_iterations: Deband iterations
    :param float deband_threshold: Deband threshold
    :param float deband_radius: Deband radius
    :param float deband_grain: Deband grain
    :param float brightness: Brightness boost
    :param float contrast: Contrast gain
    :param float saturation: Saturation gain
    :param float hue: Hue shift
    :param float gamma: Gamma adjustment
    :param bool peak_detect: Enable dynamic peak detection for HDR tone-mapping
    :param float smoothing_period: Peak detection smoothing period
    :param float minimum_peak: Peak detection minimum peak
    :param float scene_threshold_low: Scene change low threshold
    :param float scene_threshold_high: Scene change high threshold
    :param float percentile: Peak detection percentile
    :param int gamut_mode: Gamut-mapping mode
    :param int tonemapping: Tone-mapping algorithm
    :param float tonemapping_param: Tunable parameter for some tone-mapping functions
    :param bool inverse_tonemapping: Inverse tone mapping (range expansion)
    :param int tonemapping_lut_size: Tone-mapping LUT size
    :param float contrast_recovery: HDR contrast recovery strength
    :param float contrast_smoothness: HDR contrast recovery smoothness
    :param float desaturation_strength: Desaturation strength
    :param float desaturation_exponent: Desaturation exponent
    :param bool gamut_warning: Highlight out-of-gamut colors
    :param bool gamut_clipping: Enable desaturating colorimetric gamut clipping
    :param int intent: Rendering intent
    :param int tonemapping_mode: Tone-mapping mode
    :param float tonemapping_crosstalk: Crosstalk factor for tone-mapping
    :param float overshoot: Tone-mapping overshoot margin
    :param float hybrid_mix: Tone-mapping hybrid LMS mixing coefficient
    :param int dithering: Dither method to use
    :param int dither_lut_size: Dithering LUT size
    :param bool dither_temporal: Enable temporal dithering
    :param str cones: Colorblindness adaptation model
    :param float cone_strength: Colorblindness adaptation strength
    :param str custom_shader_path: Path to custom user shader (mpv .hook format)
    :param str custom_shader_bin: Custom user shader as binary (mpv .hook format)
    :param bool skip_aa: Skip anti-aliasing
    :param float polar_cutoff: Polar LUT cutoff
    :param bool disable_linear: Disable linear scaling
    :param bool disable_builtin: Disable built-in scalers
    :param bool force_icc_lut: Deprecated, does nothing
    :param bool force_dither: Force dithering
    :param bool disable_fbos: Force-disable FBOs

    Ref: https://ffmpeg.org/ffmpeg-filters.html#libplacebo

    """
    filter_node = FilterNode(
        name="libplacebo",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "w": w,
                    "h": h,
                    "fps": fps,
                    "crop_x": crop_x,
                    "crop_y": crop_y,
                    "crop_w": crop_w,
                    "crop_h": crop_h,
                    "pos_x": pos_x,
                    "pos_y": pos_y,
                    "pos_w": pos_w,
                    "pos_h": pos_h,
                    "format": format,
                    "force_original_aspect_ratio": force_original_aspect_ratio,
                    "force_divisible_by": force_divisible_by,
                    "normalize_sar": normalize_sar,
                    "pad_crop_ratio": pad_crop_ratio,
                    "fillcolor": fillcolor,
                    "corner_rounding": corner_rounding,
                    "extra_opts": extra_opts,
                    "colorspace": colorspace,
                    "range": range,
                    "color_primaries": color_primaries,
                    "color_trc": color_trc,
                    "upscaler": upscaler,
                    "downscaler": downscaler,
                    "frame_mixer": frame_mixer,
                    "lut_entries": lut_entries,
                    "antiringing": antiringing,
                    "sigmoid": sigmoid,
                    "apply_filmgrain": apply_filmgrain,
                    "apply_dolbyvision": apply_dolbyvision,
                    "deband": deband,
                    "deband_iterations": deband_iterations,
                    "deband_threshold": deband_threshold,
                    "deband_radius": deband_radius,
                    "deband_grain": deband_grain,
                    "brightness": brightness,
                    "contrast": contrast,
                    "saturation": saturation,
                    "hue": hue,
                    "gamma": gamma,
                    "peak_detect": peak_detect,
                    "smoothing_period": smoothing_period,
                    "minimum_peak": minimum_peak,
                    "scene_threshold_low": scene_threshold_low,
                    "scene_threshold_high": scene_threshold_high,
                    "percentile": percentile,
                    "gamut_mode": gamut_mode,
                    "tonemapping": tonemapping,
                    "tonemapping_param": tonemapping_param,
                    "inverse_tonemapping": inverse_tonemapping,
                    "tonemapping_lut_size": tonemapping_lut_size,
                    "contrast_recovery": contrast_recovery,
                    "contrast_smoothness": contrast_smoothness,
                    "desaturation_strength": desaturation_strength,
                    "desaturation_exponent": desaturation_exponent,
                    "gamut_warning": gamut_warning,
                    "gamut_clipping": gamut_clipping,
                    "intent": intent,
                    "tonemapping_mode": tonemapping_mode,
                    "tonemapping_crosstalk": tonemapping_crosstalk,
                    "overshoot": overshoot,
                    "hybrid_mix": hybrid_mix,
                    "dithering": dithering,
                    "dither_lut_size": dither_lut_size,
                    "dither_temporal": dither_temporal,
                    "cones": cones,
                    "cone-strength": cone_strength,
                    "custom_shader_path": custom_shader_path,
                    "custom_shader_bin": custom_shader_bin,
                    "skip_aa": skip_aa,
                    "polar_cutoff": polar_cutoff,
                    "disable_linear": disable_linear,
                    "disable_builtin": disable_builtin,
                    "force_icc_lut": force_icc_lut,
                    "force_dither": force_dither,
                    "disable_fbos": disable_fbos,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def libvmaf(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    model_path: str | float | int = Default(None),
    log_path: str | float | int = Default(None),
    log_fmt: str | float | int = Default('"xml"'),
    enable_transform: bool | int | str = Default("false"),
    psnr: bool | int | str = Default("false"),
    ssim: bool | int | str = Default("false"),
    ms_ssim: bool | int | str = Default("false"),
    pool: str | float | int = Default(None),
    n_threads: int | str = Default("0"),
    n_subsample: int | str = Default("1"),
    enable_conf_interval: bool | int | str = Default("false"),
    model: str | float | int = Default('"version=vmaf_v0.6.1"'),
    feature: str | float | int = Default(None),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the VMAF between two video streams.

    Parameters:
    ----------

    :param str model_path: use model='path=...'.
    :param str log_path: Set the file path to be used to write log.
    :param str log_fmt: Set the format of the log (csv, json, xml, or sub). (default "xml")
    :param bool enable_transform: use model='enable_transform=true'. (default false)
    :param bool psnr: use feature='name=psnr'. (default false)
    :param bool ssim: use feature='name=float_ssim'. (default false)
    :param bool ms_ssim: use feature='name=float_ms_ssim'. (default false)
    :param str pool: Set the pool method to be used for computing vmaf.
    :param int n_threads: Set number of threads to be used when computing vmaf. (from 0 to UINT32_MAX) (default 0)
    :param int n_subsample: Set interval for frame subsampling used when computing vmaf. (from 1 to UINT32_MAX) (default 1)
    :param bool enable_conf_interval: model='enable_conf_interval=true'. (default false)
    :param str model: Set the model to be used for computing vmaf. (default "version=vmaf_v0.6.1")
    :param str feature: Set the feature to be used for computing vmaf.
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#libvmaf

    """
    filter_node = FilterNode(
        name="libvmaf",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "model_path": model_path,
                    "log_path": log_path,
                    "log_fmt": log_fmt,
                    "enable_transform": enable_transform,
                    "psnr": psnr,
                    "ssim": ssim,
                    "ms_ssim": ms_ssim,
                    "pool": pool,
                    "n_threads": n_threads,
                    "n_subsample": n_subsample,
                    "enable_conf_interval": enable_conf_interval,
                    "model": model,
                    "feature": feature,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def libvmaf_cuda(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    log_path: str | float | int = Default("((void*)0)"),
    log_fmt: str | float | int = Default("xml"),
    pool: str | float | int = Default("((void*)0)"),
    n_threads: int | str = Default(0),
    n_subsample: int | str = Default(1),
    model: str | float | int = Default("version=vmaf_v0.6.1"),
    feature: str | float | int = Default("((void*)0)"),
    eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default(0),
    repeatlast: bool | int | str = Default(1),
    ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 11.146 libvmaf_cuda

    This is the CUDA variant of the libvmaf filter. It only accepts CUDA frames.

    It requires Netflix’s vmaf library (libvmaf) as a pre-requisite. After
    installing the library it can be enabled using: `./configure --enable-nonfree
    --enable-ffnvcodec --enable-libvmaf`.



    Parameters:
    ----------

    :param str log_path: Set the file path to be used to write log.
    :param str log_fmt: Set the format of the log (csv, json, xml, or sub).
    :param str pool: Set the pool method to be used for computing vmaf.
    :param int n_threads: Set number of threads to be used when computing vmaf.
    :param int n_subsample: Set interval for frame subsampling used when computing vmaf.
    :param str model: Set the model to be used for computing vmaf.
    :param str feature: Set the feature to be used for computing vmaf.
    :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
    :param bool shortest: Force the output to terminate when the shortest input terminates.
    :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
    :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

    Ref: https://ffmpeg.org/ffmpeg-filters.html#libvmaf_005fcuda

    """
    filter_node = FilterNode(
        name="libvmaf_cuda",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "log_path": log_path,
                    "log_fmt": log_fmt,
                    "pool": pool,
                    "n_threads": n_threads,
                    "n_subsample": n_subsample,
                    "model": model,
                    "feature": feature,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def limitdiff(
    *streams: "VideoStream",
    threshold: float | int | str = Default("0.00392157"),
    elasticity: float | int | str = Default("2"),
    reference: bool | int | str = Default("false"),
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with limiting difference.

    Parameters:
    ----------

    :param float threshold: set the threshold (from 0 to 1) (default 0.00392157)
    :param float elasticity: set the elasticity (from 0 to 10) (default 2)
    :param bool reference: enable reference stream (default false)
    :param int planes: set the planes to filter (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#limitdiff

    """
    filter_node = FilterNode(
        name="limitdiff",
        input_typings=tuple([StreamType.video, StreamType.video] + ([StreamType.video] if reference else [])),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "threshold": threshold,
                    "elasticity": elasticity,
                    "reference": reference,
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def lut2(
    _srcx: "VideoStream",
    _srcy: "VideoStream",
    *,
    c0: str | float | int = Default('"x"'),
    c1: str | float | int = Default('"x"'),
    c2: str | float | int = Default('"x"'),
    c3: str | float | int = Default('"x"'),
    d: int | str = Default("0"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Compute and apply a lookup table from two video inputs.

    Parameters:
    ----------

    :param str c0: set component #0 expression (default "x")
    :param str c1: set component #1 expression (default "x")
    :param str c2: set component #2 expression (default "x")
    :param str c3: set component #3 expression (default "x")
    :param int d: set output depth (from 0 to 16) (default 0)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

    """
    filter_node = FilterNode(
        name="lut2",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _srcx,
            _srcy,
        ),
        kwargs=tuple(
            (
                {
                    "c0": c0,
                    "c1": c1,
                    "c2": c2,
                    "c3": c3,
                    "d": d,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def lv2(
    *streams: "AudioStream",
    plugin: str | float | int = Default(None),
    controls: str | float | int = Default(None),
    sample_rate: int | str = Default(44100),
    nb_samples: int | str = Default(1024),
    duration: int | str = Default(-1),
    **kwargs: Any
) -> "AudioStream":
    """

    ### 8.99 lv2

    Load a LV2 (LADSPA Version 2) plugin.

    To enable compilation of this filter you need to configure FFmpeg with
    `--enable-lv2`.

    **plugin, p**

        Specifies the plugin URI. You may need to escape ’:’.

    **controls, c**

        Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). If controls is set to help, all available controls and their valid ranges are printed.

    **sample_rate, s**

        Specify the sample rate, default to 44100. Only used if plugin have zero inputs.

    **nb_samples, n**

        Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.

    **duration, d**

        Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.



    Parameters:
    ----------

    :param str plugin: Specifies the plugin URI. You may need to escape ’:’.
    :param str controls: Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). If controls is set to help, all available controls and their valid ranges are printed.
    :param int sample_rate: Specify the sample rate, default to 44100. Only used if plugin have zero inputs.
    :param int nb_samples: Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.
    :param int duration: Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#lv2

    """
    filter_node = FilterNode(
        name="lv2",
        input_typings=None,
        output_typings=tuple([StreamType.audio]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "plugin": plugin,
                    "controls": controls,
                    "sample_rate": sample_rate,
                    "nb_samples": nb_samples,
                    "duration": duration,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def maskedclamp(
    _base: "VideoStream",
    _dark: "VideoStream",
    _bright: "VideoStream",
    *,
    undershoot: int | str = Default("0"),
    overshoot: int | str = Default("0"),
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Clamp first stream with second stream and third stream.

    Parameters:
    ----------

    :param int undershoot: set undershoot (from 0 to 65535) (default 0)
    :param int overshoot: set overshoot (from 0 to 65535) (default 0)
    :param int planes: set planes (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedclamp

    """
    filter_node = FilterNode(
        name="maskedclamp",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _base,
            _dark,
            _bright,
        ),
        kwargs=tuple(
            (
                {
                    "undershoot": undershoot,
                    "overshoot": overshoot,
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def maskedmax(
    _source: "VideoStream",
    _filter1: "VideoStream",
    _filter2: "VideoStream",
    *,
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with maximum difference of two streams.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmax

    """
    filter_node = FilterNode(
        name="maskedmax",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _filter1,
            _filter2,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def maskedmerge(
    _base: "VideoStream",
    _overlay: "VideoStream",
    _mask: "VideoStream",
    *,
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Merge first stream with second stream using third stream as mask.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmerge

    """
    filter_node = FilterNode(
        name="maskedmerge",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _base,
            _overlay,
            _mask,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def maskedmin(
    _source: "VideoStream",
    _filter1: "VideoStream",
    _filter2: "VideoStream",
    *,
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with minimum difference of two streams.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmin

    """
    filter_node = FilterNode(
        name="maskedmin",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _filter1,
            _filter2,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def maskedthreshold(
    _source: "VideoStream",
    _reference: "VideoStream",
    *,
    threshold: int | str = Default("1"),
    planes: int | str = Default("15"),
    mode: int | Literal["abs", "diff"] | Default = Default("abs"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Pick pixels comparing absolute difference of two streams with threshold.

    Parameters:
    ----------

    :param int threshold: set threshold (from 0 to 65535) (default 1)
    :param int planes: set planes (from 0 to 15) (default 15)
    :param int mode: set mode (from 0 to 1) (default abs)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedthreshold

    """
    filter_node = FilterNode(
        name="maskedthreshold",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "threshold": threshold,
                    "planes": planes,
                    "mode": mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def mergeplanes(
    *streams: "VideoStream",
    mapping: int | str = Default("-1"),
    format: str | float | int = Default("yuva444p"),
    map0s: int | str = Default("0"),
    map0p: int | str = Default("0"),
    map1s: int | str = Default("0"),
    map1p: int | str = Default("0"),
    map2s: int | str = Default("0"),
    map2p: int | str = Default("0"),
    map3s: int | str = Default("0"),
    map3p: int | str = Default("0"),
    **kwargs: Any
) -> "VideoStream":
    """

    Merge planes.

    Parameters:
    ----------

    :param int mapping: set input to output plane mapping (from -1 to 8.58993e+08) (default -1)
    :param str format: set output pixel format (default yuva444p)
    :param int map0s: set 1st input to output stream mapping (from 0 to 3) (default 0)
    :param int map0p: set 1st input to output plane mapping (from 0 to 3) (default 0)
    :param int map1s: set 2nd input to output stream mapping (from 0 to 3) (default 0)
    :param int map1p: set 2nd input to output plane mapping (from 0 to 3) (default 0)
    :param int map2s: set 3rd input to output stream mapping (from 0 to 3) (default 0)
    :param int map2p: set 3rd input to output plane mapping (from 0 to 3) (default 0)
    :param int map3s: set 4th input to output stream mapping (from 0 to 3) (default 0)
    :param int map3p: set 4th input to output plane mapping (from 0 to 3) (default 0)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#mergeplanes

    """
    filter_node = FilterNode(
        name="mergeplanes",
        input_typings=tuple([StreamType.video] * int(max(hex(int(mapping))[2::2]))),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "mapping": mapping,
                    "format": format,
                    "map0s": map0s,
                    "map0p": map0p,
                    "map1s": map1s,
                    "map1p": map1p,
                    "map2s": map2s,
                    "map2p": map2p,
                    "map3s": map3s,
                    "map3p": map3p,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def midequalizer(
    _in0: "VideoStream",
    _in1: "VideoStream",
    *,
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Midway Equalization.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#midequalizer

    """
    filter_node = FilterNode(
        name="midequalizer",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _in0,
            _in1,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def mix(
    *streams: "VideoStream",
    inputs: int | str = Default("2"),
    weights: str | float | int = Default('"1 1"'),
    scale: float | int | str = Default("0"),
    planes: str | float | int = Default("F"),
    duration: int | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Mix video inputs.

    Parameters:
    ----------

    :param int inputs: set number of inputs (from 2 to 32767) (default 2)
    :param str weights: set weight for each input (default "1 1")
    :param float scale: set scale (from 0 to 32767) (default 0)
    :param str planes: set what planes to filter (default F)
    :param int duration: how to determine end of stream (from 0 to 2) (default longest)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#mix

    """
    filter_node = FilterNode(
        name="mix",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "weights": weights,
                    "scale": scale,
                    "planes": planes,
                    "duration": duration,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def morpho(
    _default: "VideoStream",
    _structure: "VideoStream",
    *,
    mode: int
    | Literal["erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"]
    | Default = Default("erode"),
    planes: int | str = Default("7"),
    structure: int | Literal["first", "all"] | Default = Default("all"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Morphological filter.

    Parameters:
    ----------

    :param int mode: set morphological transform (from 0 to 6) (default erode)
    :param int planes: set planes to filter (from 0 to 15) (default 7)
    :param int structure: when to process structures (from 0 to 1) (default all)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#morpho

    """
    filter_node = FilterNode(
        name="morpho",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _default,
            _structure,
        ),
        kwargs=tuple(
            (
                {
                    "mode": mode,
                    "planes": planes,
                    "structure": structure,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def msad(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the MSAD between two video streams.

    Parameters:
    ----------

    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#msad

    """
    filter_node = FilterNode(
        name="msad",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def multiply(
    _source: "VideoStream",
    _factor: "VideoStream",
    *,
    scale: float | int | str = Default("1"),
    offset: float | int | str = Default("0.5"),
    planes: str | float | int = Default("F"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Multiply first video stream with second video stream.

    Parameters:
    ----------

    :param float scale: set scale (from 0 to 9) (default 1)
    :param float offset: set offset (from -1 to 1) (default 0.5)
    :param str planes: set planes (default F)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#multiply

    """
    filter_node = FilterNode(
        name="multiply",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _factor,
        ),
        kwargs=tuple(
            (
                {
                    "scale": scale,
                    "offset": offset,
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def overlay(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str | float | int = Default('"0"'),
    y: str | float | int = Default('"0"'),
    eof_action: int | Literal["repeat", "endall", "pass", "repeat", "endall", "pass"] | Default = Default("repeat"),
    eval: int | Literal["init", "frame"] | Default = Default("frame"),
    shortest: bool | int | str = Default("false"),
    format: int
    | Literal["yuv420", "yuv420p10", "yuv422", "yuv422p10", "yuv444", "rgb", "gbrp", "auto"]
    | Default = Default("yuv420"),
    repeatlast: bool | int | str = Default("true"),
    alpha: int | Literal["straight", "premultiplied"] | Default = Default("straight"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Overlay a video source on top of the input.

    Parameters:
    ----------

    :param str x: set the x expression (default "0")
    :param str y: set the y expression (default "0")
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param int eval: specify when to evaluate expressions (from 0 to 1) (default frame)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param int format: set output format (from 0 to 7) (default yuv420)
    :param bool repeatlast: repeat overlay of the last overlay frame (default true)
    :param int alpha: alpha format (from 0 to 1) (default straight)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay

    """
    filter_node = FilterNode(
        name="overlay",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _overlay,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "y": y,
                    "eof_action": eof_action,
                    "eval": eval,
                    "shortest": shortest,
                    "format": format,
                    "repeatlast": repeatlast,
                    "alpha": alpha,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def overlay_cuda(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str | float | int = Default("0"),
    y: str | float | int = Default("0"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("EOF_ACTION_REPEAT"),
    eval: int | str = Default("EVAL_MODE_FRAME"),
    shortest: bool | int | str = Default(0),
    repeatlast: bool | int | str = Default(1),
    ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 11.184 overlay_cuda

    Overlay one video on top of another.

    This is the CUDA variant of the overlay filter. It only accepts CUDA frames.
    The underlying input pixel formats have to match.

    It takes two inputs and has one output. The first input is the "main" video on
    which the second input is overlaid.

    It accepts the following parameters:

    **x**

    **y**

        Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.

    **eval**

        Set when the expressions for x and y are evaluated. It accepts the following values: init Evaluate expressions once during filter initialization or when a command is processed. frame Evaluate expressions for each incoming frame Default value is frame.

    **eof_action**

        See framesync.

    **shortest**

        See framesync.

    **repeatlast**

        See framesync.

    This filter also supports the framesync options.



    Parameters:
    ----------

    :param str x: Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
    :param str y: Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
    :param int eof_action: See framesync.
    :param int eval: Set when the expressions for x and y are evaluated. It accepts the following values: init Evaluate expressions once during filter initialization or when a command is processed. frame Evaluate expressions for each incoming frame Default value is frame.
    :param bool shortest: See framesync.
    :param bool repeatlast: See framesync.
    :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fcuda

    """
    filter_node = FilterNode(
        name="overlay_cuda",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _overlay,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "y": y,
                    "eof_action": eof_action,
                    "eval": eval,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def overlay_opencl(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: int | str = Default(0),
    y: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 12.9 overlay_opencl

    Overlay one video on top of another.

    It takes two inputs and has one output. The first input is the "main" video on
    which the second input is overlaid. This filter requires same memory layout
    for all the inputs. So, format conversion may be needed.

    The filter accepts the following options:

    **x**

        Set the x coordinate of the overlaid video on the main video. Default value is 0.

    **y**

        Set the y coordinate of the overlaid video on the main video. Default value is 0.



    Parameters:
    ----------

    :param int x: Set the x coordinate of the overlaid video on the main video. Default value is 0.
    :param int y: Set the y coordinate of the overlaid video on the main video. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fopencl

    """
    filter_node = FilterNode(
        name="overlay_opencl",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _overlay,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "y": y,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def overlay_vaapi(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str | float | int = Default("0"),
    y: str | float | int = Default("0"),
    w: str | float | int = Default("overlay_iw"),
    h: str | float | int = Default("overlay_ih*w/overlay_iw"),
    alpha: float | int | str = Default(1.0),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("EOF_ACTION_REPEAT"),
    shortest: bool | int | str = Default(0),
    repeatlast: bool | int | str = Default(1),
    ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 13.1 overlay_vaapi

    Overlay one video on the top of another.

    It takes two inputs and has one output. The first input is the "main" video on
    which the second input is overlaid.

    The filter accepts the following options:

    **x**

    **y**

        Set expressions for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions.

    **w**

    **h**

        Set expressions for the width and height the overlaid video on the main video. Default values are ’overlay_iw’ for ’w’ and ’overlay_ih*w/overlay_iw’ for ’h’. The expressions can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_iw overlay_ih The overlay input width and height. overlay_w, w overlay_h, h The overlay output width and height. overlay_x, x overlay_y, y Position of the overlay layer inside of main

    **alpha**

        Set transparency of overlaid video. Allowed range is 0.0 to 1.0. Higher value means lower transparency. Default value is 1.0.

    **eof_action**

        See framesync.

    **shortest**

        See framesync.

    **repeatlast**

        See framesync.

    This filter also supports the framesync options.



    Parameters:
    ----------

    :param str x: Set expressions for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions.
    :param str y: Set expressions for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions.
    :param str w: Set expressions for the width and height the overlaid video on the main video. Default values are ’overlay_iw’ for ’w’ and ’overlay_ih*w/overlay_iw’ for ’h’. The expressions can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_iw overlay_ih The overlay input width and height. overlay_w, w overlay_h, h The overlay output width and height. overlay_x, x overlay_y, y Position of the overlay layer inside of main
    :param str h: Set expressions for the width and height the overlaid video on the main video. Default values are ’overlay_iw’ for ’w’ and ’overlay_ih*w/overlay_iw’ for ’h’. The expressions can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_iw overlay_ih The overlay input width and height. overlay_w, w overlay_h, h The overlay output width and height. overlay_x, x overlay_y, y Position of the overlay layer inside of main
    :param float alpha: Set transparency of overlaid video. Allowed range is 0.0 to 1.0. Higher value means lower transparency. Default value is 1.0.
    :param int eof_action: See framesync.
    :param bool shortest: See framesync.
    :param bool repeatlast: See framesync.
    :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvaapi

    """
    filter_node = FilterNode(
        name="overlay_vaapi",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _overlay,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "alpha": alpha,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def overlay_vulkan(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: int | str = Default(0),
    y: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 14.11 overlay_vulkan

    Overlay one video on top of another.

    It takes two inputs and has one output. The first input is the "main" video on
    which the second input is overlaid. This filter requires all inputs to use the
    same pixel format. So, format conversion may be needed.

    The filter accepts the following options:

    **x**

        Set the x coordinate of the overlaid video on the main video. Default value is 0.

    **y**

        Set the y coordinate of the overlaid video on the main video. Default value is 0.



    Parameters:
    ----------

    :param int x: Set the x coordinate of the overlaid video on the main video. Default value is 0.
    :param int y: Set the y coordinate of the overlaid video on the main video. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvulkan

    """
    filter_node = FilterNode(
        name="overlay_vulkan",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _overlay,
        ),
        kwargs=tuple(
            (
                {
                    "x": x,
                    "y": y,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def paletteuse(
    _default: "VideoStream",
    _palette: "VideoStream",
    *,
    dither: int
    | Literal["bayer", "heckbert", "floyd_steinberg", "sierra2", "sierra2_4a", "sierra3", "burkes", "atkinson"]
    | Default = Default("sierra2_4a"),
    bayer_scale: int | str = Default("2"),
    diff_mode: int | Literal["rectangle"] | Default = Default("0"),
    new: bool | int | str = Default("false"),
    alpha_threshold: int | str = Default("128"),
    debug_kdtree: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Use a palette to downsample an input video stream.

    Parameters:
    ----------

    :param int dither: select dithering mode (from 0 to 8) (default sierra2_4a)
    :param int bayer_scale: set scale for bayer dithering (from 0 to 5) (default 2)
    :param int diff_mode: set frame difference mode (from 0 to 1) (default 0)
    :param bool new: take new palette for each output frame (default false)
    :param int alpha_threshold: set the alpha threshold for transparency (from 0 to 255) (default 128)
    :param str debug_kdtree: save Graphviz graph of the kdtree in specified file

    Ref: https://ffmpeg.org/ffmpeg-filters.html#paletteuse

    """
    filter_node = FilterNode(
        name="paletteuse",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _default,
            _palette,
        ),
        kwargs=tuple(
            (
                {
                    "dither": dither,
                    "bayer_scale": bayer_scale,
                    "diff_mode": diff_mode,
                    "new": new,
                    "alpha_threshold": alpha_threshold,
                    "debug_kdtree": debug_kdtree,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def premultiply(
    *streams: "VideoStream",
    planes: int | str = Default("15"),
    inplace: bool | int | str = Default("false"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    PreMultiply first stream with first plane of second stream.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param bool inplace: enable inplace mode (default false)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#premultiply

    """
    filter_node = FilterNode(
        name="premultiply",
        input_typings=tuple([StreamType.video] + [StreamType.video] if inplace else []),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "inplace": inplace,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def program_opencl(
    *streams: "VideoStream",
    source: str | float | int = Default("((void*)0)"),
    kernel: str | float | int = Default("((void*)0)"),
    inputs: int | str = Default(1),
    size: str | float | int = Default("((void*)0)"),
    eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default(0),
    repeatlast: bool | int | str = Default(1),
    ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 12.12 program_opencl

    Filter video using an OpenCL program.

    **source**

        OpenCL program source file.

    **kernel**

        Kernel name in program.

    **inputs**

        Number of inputs to the filter. Defaults to 1.

    **size, s**

        Size of output frames. Defaults to the same as the first input.

    The `program_opencl` filter also supports the framesync options.

    The program source file must contain a kernel function with the given name,
    which will be run once for each plane of the output. Each run on a plane gets
    enqueued as a separate 2D global NDRange with one work-item for each pixel to
    be generated. The global ID offset for each work-item is therefore the
    coordinates of a pixel in the destination image.

    The kernel function needs to take the following arguments:

      * Destination image, __write_only image2d_t.

    This image will become the output; the kernel should write all of it.

      * Frame index, unsigned int.

    This is a counter starting from zero and increasing by one for each frame.

      * Source images, __read_only image2d_t.

    These are the most recent images on each input. The kernel may read from them
    to generate the output, but they can’t be written to.

    Example programs:

      * Copy the input to the output (output must be the same size as the input).

            __kernel void copy(__write_only image2d_t destination,
                           unsigned int index,
                           __read_only  image2d_t source)
        {
            const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE;

            int2 location = (int2)(get_global_id(0), get_global_id(1));

            float4 value = read_imagef(source, sampler, location);

            write_imagef(destination, location, value);
        }


      * Apply a simple transformation, rotating the input by an amount increasing with the index counter. Pixel values are linearly interpolated by the sampler, and the output need not have the same dimensions as the input.

            __kernel void rotate_image(__write_only image2d_t dst,
                                   unsigned int index,
                                   __read_only  image2d_t src)
        {
            const sampler_t sampler = (CLK_NORMALIZED_COORDS_FALSE |
                                       CLK_FILTER_LINEAR);

            float angle = (float)index / 100.0f;

            float2 dst_dim = convert_float2(get_image_dim(dst));
            float2 src_dim = convert_float2(get_image_dim(src));

            float2 dst_cen = dst_dim / 2.0f;
            float2 src_cen = src_dim / 2.0f;

            int2   dst_loc = (int2)(get_global_id(0), get_global_id(1));

            float2 dst_pos = convert_float2(dst_loc) - dst_cen;
            float2 src_pos = {
                cos(angle) * dst_pos.x - sin(angle) * dst_pos.y,
                sin(angle) * dst_pos.x + cos(angle) * dst_pos.y
            };
            src_pos = src_pos * src_dim / dst_dim;

            float2 src_loc = src_pos + src_cen;

            if (src_loc.x < 0.0f      || src_loc.y < 0.0f ||
                src_loc.x > src_dim.x || src_loc.y > src_dim.y)
                write_imagef(dst, dst_loc, 0.5f);
            else
                write_imagef(dst, dst_loc, read_imagef(src, sampler, src_loc));
        }


      * Blend two inputs together, with the amount of each input used varying with the index counter.

            __kernel void blend_images(__write_only image2d_t dst,
                                   unsigned int index,
                                   __read_only  image2d_t src1,
                                   __read_only  image2d_t src2)
        {
            const sampler_t sampler = (CLK_NORMALIZED_COORDS_FALSE |
                                       CLK_FILTER_LINEAR);

            float blend = (cos((float)index / 50.0f) + 1.0f) / 2.0f;

            int2  dst_loc = (int2)(get_global_id(0), get_global_id(1));
            int2 src1_loc = dst_loc * get_image_dim(src1) / get_image_dim(dst);
            int2 src2_loc = dst_loc * get_image_dim(src2) / get_image_dim(dst);

            float4 val1 = read_imagef(src1, sampler, src1_loc);
            float4 val2 = read_imagef(src2, sampler, src2_loc);

            write_imagef(dst, dst_loc, val1 * blend + val2 * (1.0f - blend));
        }




    Parameters:
    ----------

    :param str source: OpenCL program source file.
    :param str kernel: Kernel name in program.
    :param int inputs: Number of inputs to the filter. Defaults to 1.
    :param str size: Size of output frames. Defaults to the same as the first input.
    :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
    :param bool shortest: Force the output to terminate when the shortest input terminates.
    :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
    :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

    Ref: https://ffmpeg.org/ffmpeg-filters.html#program_005fopencl

    """
    filter_node = FilterNode(
        name="program_opencl",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "source": source,
                    "kernel": kernel,
                    "inputs": inputs,
                    "size": size,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def psnr(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    stats_file: str | float | int = Default(None),
    stats_version: int | str = Default("1"),
    output_max: bool | int | str = Default("false"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the PSNR between two video streams.

    Parameters:
    ----------

    :param str stats_file: Set file where to store per-frame difference information
    :param int stats_version: Set the format version for the stats file. (from 1 to 2) (default 1)
    :param bool output_max: Add raw stats (max values) to the output log. (default false)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#psnr

    """
    filter_node = FilterNode(
        name="psnr",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "stats_file": stats_file,
                    "stats_version": stats_version,
                    "output_max": output_max,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def remap(
    _source: "VideoStream",
    _xmap: "VideoStream",
    _ymap: "VideoStream",
    *,
    format: int | Literal["color", "gray"] | Default = Default("color"),
    fill: str | float | int = Default('"black"'),
    **kwargs: Any
) -> "VideoStream":
    """

    Remap pixels.

    Parameters:
    ----------

    :param int format: set output format (from 0 to 1) (default color)
    :param str fill: set the color of the unmapped pixels (default "black")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#remap

    """
    filter_node = FilterNode(
        name="remap",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _xmap,
            _ymap,
        ),
        kwargs=tuple(
            (
                {
                    "format": format,
                    "fill": fill,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def remap_opencl(
    _source: "VideoStream",
    _xmap: "VideoStream",
    _ymap: "VideoStream",
    *,
    interp: int | Literal["near", "linear"] | Default = Default(1),
    fill: str | float | int = Default("black"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 12.13 remap_opencl

    Remap pixels using 2nd: Xmap and 3rd: Ymap input video stream.

    Destination pixel at position (X, Y) will be picked from source (x, y)
    position where x = Xmap(X, Y) and y = Ymap(X, Y). If mapping values are out of
    range, zero value for pixel will be used for destination pixel.

    Xmap and Ymap input video streams must be of same dimensions. Output video
    stream will have Xmap/Ymap video stream dimensions. Xmap and Ymap input video
    streams are 32bit float pixel format, single channel.

    **interp**

        Specify interpolation used for remapping of pixels. Allowed values are near and linear. Default value is linear.

    **fill**

        Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.



    Parameters:
    ----------

    :param int interp: Specify interpolation used for remapping of pixels. Allowed values are near and linear. Default value is linear.
    :param str fill: Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#remap_005fopencl

    """
    filter_node = FilterNode(
        name="remap_opencl",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _source,
            _xmap,
            _ymap,
        ),
        kwargs=tuple(
            (
                {
                    "interp": interp,
                    "fill": fill,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def scale2ref(
    _default: "VideoStream",
    _ref: "VideoStream",
    *,
    w: str | float | int = Default(None),
    h: str | float | int = Default(None),
    flags: str | float | int = Default('""'),
    interl: bool | int | str = Default("false"),
    in_color_matrix: str
    | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
    | Default = Default('"auto"'),
    out_color_matrix: str
    | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
    | Default = Default(None),
    in_range: int
    | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
    | Default = Default("auto"),
    out_range: int
    | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
    | Default = Default("auto"),
    in_v_chr_pos: int | str = Default("-513"),
    in_h_chr_pos: int | str = Default("-513"),
    out_v_chr_pos: int | str = Default("-513"),
    out_h_chr_pos: int | str = Default("-513"),
    force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default("disable"),
    force_divisible_by: int | str = Default("1"),
    param0: float | int | str = Default("DBL_MAX"),
    param1: float | int | str = Default("DBL_MAX"),
    eval: int | Literal["init", "frame"] | Default = Default("init"),
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    Scale the input video size and/or convert the image format to the given reference.

    Parameters:
    ----------

    :param str w: Output video width
    :param str h: Output video height
    :param str flags: Flags to pass to libswscale (default "")
    :param bool interl: set interlacing (default false)
    :param str in_color_matrix: set input YCbCr type (default "auto")
    :param str out_color_matrix: set output YCbCr type
    :param int in_range: set input color range (from 0 to 2) (default auto)
    :param int out_range: set output color range (from 0 to 2) (default auto)
    :param int in_v_chr_pos: input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param int in_h_chr_pos: input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param int out_v_chr_pos: output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param int out_h_chr_pos: output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
    :param int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
    :param float param0: Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
    :param float param1: Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
    :param int eval: specify when to evaluate expressions (from 0 to 1) (default init)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref

    """
    filter_node = FilterNode(
        name="scale2ref",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video, StreamType.video]),
        inputs=(
            _default,
            _ref,
        ),
        kwargs=tuple(
            (
                {
                    "w": w,
                    "h": h,
                    "flags": flags,
                    "interl": interl,
                    "in_color_matrix": in_color_matrix,
                    "out_color_matrix": out_color_matrix,
                    "in_range": in_range,
                    "out_range": out_range,
                    "in_v_chr_pos": in_v_chr_pos,
                    "in_h_chr_pos": in_h_chr_pos,
                    "out_v_chr_pos": out_v_chr_pos,
                    "out_h_chr_pos": out_h_chr_pos,
                    "force_original_aspect_ratio": force_original_aspect_ratio,
                    "force_divisible_by": force_divisible_by,
                    "param0": param0,
                    "param1": param1,
                    "eval": eval,
                }
                | kwargs
            ).items()
        ),
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def scale2ref_npp(
    _default: "VideoStream",
    _ref: "VideoStream",
    *,
    w: str | float | int = Default(None),
    h: str | float | int = Default(None),
    format: str | float | int = Default("same"),
    s: str | float | int = Default("((void*)0)"),
    interp_algo: int
    | Literal["nn", "linear", "cubic", "cubic2p_bspline", "cubic2p_catmullrom", "cubic2p_b05c03", "super", "lanczos"]
    | Default = Default("NPPI_INTER_CUBIC"),
    force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
    force_divisible_by: int | str = Default(1),
    eval: int | Literal["init", "frame"] | Default = Default("EVAL_MODE_INIT"),
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    ### 11.219 scale2ref_npp

    Use the NVIDIA Performance Primitives (libnpp) to scale (resize) the input
    video, based on a reference video.

    See the scale_npp filter for available options, scale2ref_npp supports the
    same but uses the reference video instead of the main input as basis.
    scale2ref_npp also supports the following additional constants for the w and h
    options:

    **main_w**

    **main_h**

        The main input video’s width and height

    **main_a**

        The same as main_w / main_h

    **main_sar**

        The main input video’s sample aspect ratio

    **main_dar, mdar**

        The main input video’s display aspect ratio. Calculated from (main_w / main_h) * main_sar.

    **main_n**

        The (sequential) number of the main input frame, starting from 0. Only available with eval=frame.

    **main_t**

        The presentation timestamp of the main input frame, expressed as a number of seconds. Only available with eval=frame.

    **main_pos**

        The position (byte offset) of the frame in the main input stream, or NaN if this information is unavailable and/or meaningless (for example in case of synthetic video). Only available with eval=frame.



    Parameters:
    ----------

    :param str w: Output video width
    :param str h: Output video height
    :param str format: Output pixel format
    :param str s: Output video size
    :param int interp_algo: Interpolation algorithm used for resizing
    :param int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR
    :param int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used
    :param int eval: specify when to evaluate expressions

    Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref_005fnpp

    """
    filter_node = FilterNode(
        name="scale2ref_npp",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video, StreamType.video]),
        inputs=(
            _default,
            _ref,
        ),
        kwargs=tuple(
            (
                {
                    "w": w,
                    "h": h,
                    "format": format,
                    "s": s,
                    "interp_algo": interp_algo,
                    "force_original_aspect_ratio": force_original_aspect_ratio,
                    "force_divisible_by": force_divisible_by,
                    "eval": eval,
                }
                | kwargs
            ).items()
        ),
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def sidechaincompress(
    _main: "AudioStream",
    _sidechain: "AudioStream",
    *,
    level_in: float | int | str = Default("1"),
    mode: int | Literal["downward", "upward"] | Default = Default("downward"),
    threshold: float | int | str = Default("0.125"),
    ratio: float | int | str = Default("2"),
    attack: float | int | str = Default("20"),
    release: float | int | str = Default("250"),
    makeup: float | int | str = Default("1"),
    knee: float | int | str = Default("2.82843"),
    link: int | Literal["average", "maximum"] | Default = Default("average"),
    detection: int | Literal["peak", "rms"] | Default = Default("rms"),
    level_sc: float | int | str = Default("1"),
    mix: float | int | str = Default("1"),
    **kwargs: Any
) -> "AudioStream":
    """

    Sidechain compressor.

    Parameters:
    ----------

    :param float level_in: set input gain (from 0.015625 to 64) (default 1)
    :param int mode: set mode (from 0 to 1) (default downward)
    :param float threshold: set threshold (from 0.000976563 to 1) (default 0.125)
    :param float ratio: set ratio (from 1 to 20) (default 2)
    :param float attack: set attack (from 0.01 to 2000) (default 20)
    :param float release: set release (from 0.01 to 9000) (default 250)
    :param float makeup: set make up gain (from 1 to 64) (default 1)
    :param float knee: set knee (from 1 to 8) (default 2.82843)
    :param int link: set link type (from 0 to 1) (default average)
    :param int detection: set detection (from 0 to 1) (default rms)
    :param float level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
    :param float mix: set mix (from 0 to 1) (default 1)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress

    """
    filter_node = FilterNode(
        name="sidechaincompress",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _main,
            _sidechain,
        ),
        kwargs=tuple(
            (
                {
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
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def sidechaingate(
    _main: "AudioStream",
    _sidechain: "AudioStream",
    *,
    level_in: float | int | str = Default("1"),
    mode: int | Literal["downward", "upward"] | Default = Default("downward"),
    range: float | int | str = Default("0.06125"),
    threshold: float | int | str = Default("0.125"),
    ratio: float | int | str = Default("2"),
    attack: float | int | str = Default("20"),
    release: float | int | str = Default("250"),
    makeup: float | int | str = Default("1"),
    knee: float | int | str = Default("2.82843"),
    detection: int | Literal["peak", "rms"] | Default = Default("rms"),
    link: int | Literal["average", "maximum"] | Default = Default("average"),
    level_sc: float | int | str = Default("1"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Audio sidechain gate.

    Parameters:
    ----------

    :param float level_in: set input level (from 0.015625 to 64) (default 1)
    :param int mode: set mode (from 0 to 1) (default downward)
    :param float range: set max gain reduction (from 0 to 1) (default 0.06125)
    :param float threshold: set threshold (from 0 to 1) (default 0.125)
    :param float ratio: set ratio (from 1 to 9000) (default 2)
    :param float attack: set attack (from 0.01 to 9000) (default 20)
    :param float release: set release (from 0.01 to 9000) (default 250)
    :param float makeup: set makeup gain (from 1 to 64) (default 1)
    :param float knee: set knee (from 1 to 8) (default 2.82843)
    :param int detection: set detection (from 0 to 1) (default rms)
    :param int link: set link (from 0 to 1) (default average)
    :param float level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaingate

    """
    filter_node = FilterNode(
        name="sidechaingate",
        input_typings=tuple([StreamType.audio, StreamType.audio]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _main,
            _sidechain,
        ),
        kwargs=tuple(
            (
                {
                    "level_in": level_in,
                    "mode": mode,
                    "range": range,
                    "threshold": threshold,
                    "ratio": ratio,
                    "attack": attack,
                    "release": release,
                    "makeup": makeup,
                    "knee": knee,
                    "detection": detection,
                    "link": link,
                    "level_sc": level_sc,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def signature(
    *streams: "VideoStream",
    detectmode: int | Literal["off", "full", "fast"] | Default = Default("off"),
    nb_inputs: int | str = Default("1"),
    filename: str | float | int = Default('""'),
    format: int | Literal["binary", "xml"] | Default = Default("binary"),
    th_d: int | str = Default("9000"),
    th_dc: int | str = Default("60000"),
    th_xh: int | str = Default("116"),
    th_di: int | str = Default("0"),
    th_it: float | int | str = Default("0.5"),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the MPEG-7 video signature

    Parameters:
    ----------

    :param int detectmode: set the detectmode (from 0 to 2) (default off)
    :param int nb_inputs: number of inputs (from 1 to INT_MAX) (default 1)
    :param str filename: filename for output files (default "")
    :param int format: set output format (from 0 to 1) (default binary)
    :param int th_d: threshold to detect one word as similar (from 1 to INT_MAX) (default 9000)
    :param int th_dc: threshold to detect all words as similar (from 1 to INT_MAX) (default 60000)
    :param int th_xh: threshold to detect frames as similar (from 1 to INT_MAX) (default 116)
    :param int th_di: minimum length of matching sequence in frames (from 0 to INT_MAX) (default 0)
    :param float th_it: threshold for relation of good to all frames (from 0 to 1) (default 0.5)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#signature

    """
    filter_node = FilterNode(
        name="signature",
        input_typings=tuple([StreamType.video] * int(nb_inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "detectmode": detectmode,
                    "nb_inputs": nb_inputs,
                    "filename": filename,
                    "format": format,
                    "th_d": th_d,
                    "th_dc": th_dc,
                    "th_xh": th_xh,
                    "th_di": th_di,
                    "th_it": th_it,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def spectrumsynth(
    _magnitude: "VideoStream",
    _phase: "VideoStream",
    *,
    sample_rate: int | str = Default("44100"),
    channels: int | str = Default("1"),
    scale: int | Literal["lin", "log"] | Default = Default("log"),
    slide: int | Literal["replace", "scroll", "fullframe", "rscroll"] | Default = Default("fullframe"),
    win_func: int
    | Literal[
        "rect",
        "bartlett",
        "hann",
        "hanning",
        "hamming",
        "blackman",
        "welch",
        "flattop",
        "bharris",
        "bnuttall",
        "bhann",
        "sine",
        "nuttall",
        "lanczos",
        "gauss",
        "tukey",
        "dolph",
        "cauchy",
        "parzen",
        "poisson",
        "bohman",
        "kaiser",
    ]
    | Default = Default("rect"),
    overlap: float | int | str = Default("1"),
    orientation: int | Literal["vertical", "horizontal"] | Default = Default("vertical"),
    **kwargs: Any
) -> "AudioStream":
    """

    Convert input spectrum videos to audio output.

    Parameters:
    ----------

    :param int sample_rate: set sample rate (from 15 to INT_MAX) (default 44100)
    :param int channels: set channels (from 1 to 8) (default 1)
    :param int scale: set input amplitude scale (from 0 to 1) (default log)
    :param int slide: set input sliding mode (from 0 to 3) (default fullframe)
    :param int win_func: set window function (from 0 to 20) (default rect)
    :param float overlap: set window overlap (from 0 to 1) (default 1)
    :param int orientation: set orientation (from 0 to 1) (default vertical)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#spectrumsynth

    """
    filter_node = FilterNode(
        name="spectrumsynth",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.audio]),
        inputs=(
            _magnitude,
            _phase,
        ),
        kwargs=tuple(
            (
                {
                    "sample_rate": sample_rate,
                    "channels": channels,
                    "scale": scale,
                    "slide": slide,
                    "win_func": win_func,
                    "overlap": overlap,
                    "orientation": orientation,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.audio(0)


def ssim(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    stats_file: str | float | int = Default(None),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the SSIM between two video streams.

    Parameters:
    ----------

    :param str stats_file: Set file where to store per-frame difference information
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#ssim

    """
    filter_node = FilterNode(
        name="ssim",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "stats_file": stats_file,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def streamselect(
    *streams: "VideoStream", inputs: int | str = Default("2"), map: str | float | int = Default(None), **kwargs: Any
) -> FilterNode:
    """

    Select video streams

    Parameters:
    ----------

    :param int inputs: number of input streams (from 2 to INT_MAX) (default 2)
    :param str map: input indexes to remap to outputs

    Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

    """
    filter_node = FilterNode(
        name="streamselect",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video] * len(re.findall(r"\d+", str(map)))),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "map": map,
                }
                | kwargs
            ).items()
        ),
    )

    return filter_node


def threshold(
    _default: "VideoStream",
    _threshold: "VideoStream",
    _min: "VideoStream",
    _max: "VideoStream",
    *,
    planes: int | str = Default("15"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Threshold first video stream using other video streams.

    Parameters:
    ----------

    :param int planes: set planes to filter (from 0 to 15) (default 15)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#threshold

    """
    filter_node = FilterNode(
        name="threshold",
        input_typings=tuple([StreamType.video, StreamType.video, StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _default,
            _threshold,
            _min,
            _max,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def unpremultiply(
    *streams: "VideoStream",
    planes: int | str = Default("15"),
    inplace: bool | int | str = Default("false"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    UnPreMultiply first stream with first plane of second stream.

    Parameters:
    ----------

    :param int planes: set planes (from 0 to 15) (default 15)
    :param bool inplace: enable inplace mode (default false)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#unpremultiply

    """
    filter_node = FilterNode(
        name="unpremultiply",
        input_typings=tuple([StreamType.video] + ([StreamType.video] if inplace else [])),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "inplace": inplace,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def varblur(
    _default: "VideoStream",
    _radius: "VideoStream",
    *,
    min_r: int | str = Default("0"),
    max_r: int | str = Default("8"),
    planes: int | str = Default("15"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Variable Blur filter.

    Parameters:
    ----------

    :param int min_r: set min blur radius (from 0 to 254) (default 0)
    :param int max_r: set max blur radius (from 1 to 255) (default 8)
    :param int planes: set planes to filter (from 0 to 15) (default 15)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#varblur

    """
    filter_node = FilterNode(
        name="varblur",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _default,
            _radius,
        ),
        kwargs=tuple(
            (
                {
                    "min_r": min_r,
                    "max_r": max_r,
                    "planes": planes,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def vif(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the VIF between two video streams.

    Parameters:
    ----------

    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vif

    """
    filter_node = FilterNode(
        name="vif",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _reference,
        ),
        kwargs=tuple(
            (
                {
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def vstack(
    *streams: "VideoStream",
    inputs: int | str = Default("2"),
    shortest: bool | int | str = Default("false"),
    **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs vertically.

    Parameters:
    ----------

    :param int inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param bool shortest: force termination when the shortest input terminates (default false)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vstack

    """
    filter_node = FilterNode(
        name="vstack",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def vstack_qsv(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    width: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 15.2 vstack_qsv

    Stack input videos vertically.

    This is the QSV variant of the vstack filter, each input stream may have
    different width, this filter will scale down/up each input stream while
    keeping the original aspect.

    It accepts the following options:

    **inputs**

        See vstack.

    **shortest**

        See vstack.

    **width**

        Set width of output. If set to 0, this filter will set width of output to width of the first input stream. Default value is 0.



    Parameters:
    ----------

    :param int inputs: See vstack.
    :param bool shortest: See vstack.
    :param int width: Set width of output. If set to 0, this filter will set width of output to width of the first input stream. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vstack_005fqsv

    """
    filter_node = FilterNode(
        name="vstack_qsv",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "width": width,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def vstack_vaapi(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    width: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 13.4 vstack_vaapi

    Stack input videos vertically.

    This is the VA-API variant of the vstack filter, each input stream may have
    different width, this filter will scale down/up each input stream while
    keeping the original aspect.

    It accepts the following options:

    **inputs**

        See vstack.

    **shortest**

        See vstack.

    **width**

        Set width of output. If set to 0, this filter will set width of output to width of the first input stream. Default value is 0.



    Parameters:
    ----------

    :param int inputs: See vstack.
    :param bool shortest: See vstack.
    :param int width: Set width of output. If set to 0, this filter will set width of output to width of the first input stream. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vstack_005fvaapi

    """
    filter_node = FilterNode(
        name="vstack_vaapi",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "width": width,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xcorrelate(
    _primary: "VideoStream",
    _secondary: "VideoStream",
    *,
    planes: int | str = Default("7"),
    secondary: int | Literal["first", "all"] | Default = Default("all"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Cross-correlate first video stream with second video stream.

    Parameters:
    ----------

    :param int planes: set planes to cross-correlate (from 0 to 15) (default 7)
    :param int secondary: when to process secondary frame (from 0 to 1) (default all)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xcorrelate

    """
    filter_node = FilterNode(
        name="xcorrelate",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _primary,
            _secondary,
        ),
        kwargs=tuple(
            (
                {
                    "planes": planes,
                    "secondary": secondary,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xfade(
    _main: "VideoStream",
    _xfade: "VideoStream",
    *,
    transition: int
    | Literal[
        "custom",
        "fade",
        "wipeleft",
        "wiperight",
        "wipeup",
        "wipedown",
        "slideleft",
        "slideright",
        "slideup",
        "slidedown",
        "circlecrop",
        "rectcrop",
        "distance",
        "fadeblack",
        "fadewhite",
        "radial",
        "smoothleft",
        "smoothright",
        "smoothup",
        "smoothdown",
        "circleopen",
        "circleclose",
        "vertopen",
        "vertclose",
        "horzopen",
        "horzclose",
        "dissolve",
        "pixelize",
        "diagtl",
        "diagtr",
        "diagbl",
        "diagbr",
        "hlslice",
        "hrslice",
        "vuslice",
        "vdslice",
        "hblur",
        "fadegrays",
        "wipetl",
        "wipetr",
        "wipebl",
        "wipebr",
        "squeezeh",
        "squeezev",
        "zoomin",
        "fadefast",
        "fadeslow",
    ]
    | Default = Default("fade"),
    duration: str | float | int = Default("1"),
    offset: str | float | int = Default("0"),
    expr: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Cross fade one video with another video.

    Parameters:
    ----------

    :param int transition: set cross fade transition (from -1 to 45) (default fade)
    :param str duration: set cross fade duration (default 1)
    :param str offset: set cross fade start relative to first input stream (default 0)
    :param str expr: set expression for custom transition

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xfade

    """
    filter_node = FilterNode(
        name="xfade",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _xfade,
        ),
        kwargs=tuple(
            (
                {
                    "transition": transition,
                    "duration": duration,
                    "offset": offset,
                    "expr": expr,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xfade_opencl(
    _main: "VideoStream",
    _xfade: "VideoStream",
    *,
    transition: int
    | Literal[
        "custom",
        "fade",
        "wipeleft",
        "wiperight",
        "wipeup",
        "wipedown",
        "slideleft",
        "slideright",
        "slideup",
        "slidedown",
    ]
    | Default = Default(1),
    source: str | float | int = Default("((void*)0)"),
    kernel: str | float | int = Default("((void*)0)"),
    duration: int | str = Default(1000000),
    offset: int | str = Default(0),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 12.18 xfade_opencl

    Cross fade two videos with custom transition effect by using OpenCL.

    It accepts the following options:

    **transition**

        Set one of possible transition effects. custom Select custom transition effect, the actual transition description will be picked from source and kernel options. fade wipeleft wiperight wipeup wipedown slideleft slideright slideup slidedown Default transition is fade.

    **source**

        OpenCL program source file for custom transition.

    **kernel**

        Set name of kernel to use for custom transition from program source file.

    **duration**

        Set duration of video transition.

    **offset**

        Set time of start of transition relative to first video.

    The program source file must contain a kernel function with the given name,
    which will be run once for each plane of the output. Each run on a plane gets
    enqueued as a separate 2D global NDRange with one work-item for each pixel to
    be generated. The global ID offset for each work-item is therefore the
    coordinates of a pixel in the destination image.

    The kernel function needs to take the following arguments:

      * Destination image, __write_only image2d_t.

    This image will become the output; the kernel should write all of it.

      * First Source image, __read_only image2d_t. Second Source image, __read_only image2d_t.

    These are the most recent images on each input. The kernel may read from them
    to generate the output, but they can’t be written to.

      * Transition progress, float. This value is always between 0 and 1 inclusive.

    Example programs:

      * Apply dots curtain transition effect:

            __kernel void blend_images(__write_only image2d_t dst,
                                   __read_only  image2d_t src1,
                                   __read_only  image2d_t src2,
                                   float progress)
        {
            const sampler_t sampler = (CLK_NORMALIZED_COORDS_FALSE |
                                       CLK_FILTER_LINEAR);
            int2  p = (int2)(get_global_id(0), get_global_id(1));
            float2 rp = (float2)(get_global_id(0), get_global_id(1));
            float2 dim = (float2)(get_image_dim(src1).x, get_image_dim(src1).y);
            rp = rp / dim;

            float2 dots = (float2)(20.0, 20.0);
            float2 center = (float2)(0,0);
            float2 unused;

            float4 val1 = read_imagef(src1, sampler, p);
            float4 val2 = read_imagef(src2, sampler, p);
            bool next = distance(fract(rp * dots, &unused), (float2)(0.5, 0.5)) < (progress / distance(rp, center));

            write_imagef(dst, p, next ? val1 : val2);
        }




    Parameters:
    ----------

    :param int transition: Set one of possible transition effects. custom Select custom transition effect, the actual transition description will be picked from source and kernel options. fade wipeleft wiperight wipeup wipedown slideleft slideright slideup slidedown Default transition is fade.
    :param str source: OpenCL program source file for custom transition.
    :param str kernel: Set name of kernel to use for custom transition from program source file.
    :param int duration: Set duration of video transition.
    :param int offset: Set time of start of transition relative to first video.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xfade_005fopencl

    """
    filter_node = FilterNode(
        name="xfade_opencl",
        input_typings=tuple([StreamType.video, StreamType.video]),
        output_typings=tuple([StreamType.video]),
        inputs=(
            _main,
            _xfade,
        ),
        kwargs=tuple(
            (
                {
                    "transition": transition,
                    "source": source,
                    "kernel": kernel,
                    "duration": duration,
                    "offset": offset,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xmedian(
    *streams: "VideoStream",
    inputs: int | str = Default("3"),
    planes: int | str = Default("15"),
    percentile: float | int | str = Default("0.5"),
    eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: bool | int | str = Default("false"),
    repeatlast: bool | int | str = Default("true"),
    ts_sync_mode: int | Literal["default", "nearest"] | Default = Default("default"),
    enable: str | float | int = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Pick median pixels from several video inputs.

    Parameters:
    ----------

    :param int inputs: set number of inputs (from 3 to 255) (default 3)
    :param int planes: set planes to filter (from 0 to 15) (default 15)
    :param float percentile: set percentile (from 0 to 1) (default 0.5)
    :param int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param bool repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
    :param str enable: timeline editing

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xmedian

    """
    filter_node = FilterNode(
        name="xmedian",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "planes": planes,
                    "percentile": percentile,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                    "ts_sync_mode": ts_sync_mode,
                    "enable": enable,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xstack(
    *streams: "VideoStream",
    inputs: int | str = Default("2"),
    layout: str | float | int = Default(None),
    grid: str | float | int = Default(None),
    shortest: bool | int | str = Default("false"),
    fill: str | float | int = Default('"none"'),
    **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs into custom layout.

    Parameters:
    ----------

    :param int inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param str layout: set custom layout
    :param str grid: set fixed size grid layout
    :param bool shortest: force termination when the shortest input terminates (default false)
    :param str fill: set the color for unused pixels (default "none")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xstack

    """
    filter_node = FilterNode(
        name="xstack",
        input_typings=tuple([StreamType.video] * int(inputs)),
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "layout": layout,
                    "grid": grid,
                    "shortest": shortest,
                    "fill": fill,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xstack_qsv(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    layout: str | float | int = Default("((void*)0)"),
    grid: str | float | int = Default("((void*)0)"),
    grid_tile_size: str | float | int = Default("((void*)0)"),
    fill: str | float | int = Default("none"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 15.3 xstack_qsv

    Stack video inputs into custom layout.

    This is the QSV variant of the xstack filter.

    It accepts the following options:

    **inputs**

        See xstack.

    **shortest**

        See xstack.

    **layout**

        See xstack. Moreover, this permits the user to supply output size for each input stream. xstack_qsv=inputs=4:layout=0_0_1920x1080|0_h0_1920x1080|w0_0_1920x1080|w0_h0_1920x1080

    **grid**

        See xstack.

    **grid_tile_size**

        Set output size for each input stream when grid is set. If this option is not set, this filter will set output size by default to the size of the first input stream. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.

    **fill**

        See xstack.



    Parameters:
    ----------

    :param int inputs: See xstack.
    :param bool shortest: See xstack.
    :param str layout: See xstack. Moreover, this permits the user to supply output size for each input stream. xstack_qsv=inputs=4:layout=0_0_1920x1080|0_h0_1920x1080|w0_0_1920x1080|w0_h0_1920x1080
    :param str grid: See xstack.
    :param str grid_tile_size: Set output size for each input stream when grid is set. If this option is not set, this filter will set output size by default to the size of the first input stream. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
    :param str fill: See xstack.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xstack_005fqsv

    """
    filter_node = FilterNode(
        name="xstack_qsv",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "layout": layout,
                    "grid": grid,
                    "grid_tile_size": grid_tile_size,
                    "fill": fill,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)


def xstack_vaapi(
    *streams: "VideoStream",
    inputs: int | str = Default(2),
    shortest: bool | int | str = Default(0),
    layout: str | float | int = Default("((void*)0)"),
    grid: str | float | int = Default("((void*)0)"),
    grid_tile_size: str | float | int = Default("((void*)0)"),
    fill: str | float | int = Default("none"),
    **kwargs: Any
) -> "VideoStream":
    """

    ### 13.5 xstack_vaapi

    Stack video inputs into custom layout.

    This is the VA-API variant of the xstack filter, each input stream may have
    different size, this filter will scale down/up each input stream to the given
    output size, or the size of the first input stream.

    It accepts the following options:

    **inputs**

        See xstack.

    **shortest**

        See xstack.

    **layout**

        See xstack. Moreover, this permits the user to supply output size for each input stream. xstack_vaapi=inputs=4:layout=0_0_1920x1080|0_h0_1920x1080|w0_0_1920x1080|w0_h0_1920x1080

    **grid**

        See xstack.

    **grid_tile_size**

        Set output size for each input stream when grid is set. If this option is not set, this filter will set output size by default to the size of the first input stream. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.

    **fill**

        See xstack.



    Parameters:
    ----------

    :param int inputs: See xstack.
    :param bool shortest: See xstack.
    :param str layout: See xstack. Moreover, this permits the user to supply output size for each input stream. xstack_vaapi=inputs=4:layout=0_0_1920x1080|0_h0_1920x1080|w0_0_1920x1080|w0_h0_1920x1080
    :param str grid: See xstack.
    :param str grid_tile_size: Set output size for each input stream when grid is set. If this option is not set, this filter will set output size by default to the size of the first input stream. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
    :param str fill: See xstack.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xstack_005fvaapi

    """
    filter_node = FilterNode(
        name="xstack_vaapi",
        input_typings=None,
        output_typings=tuple([StreamType.video]),
        inputs=(*streams,),
        kwargs=tuple(
            (
                {
                    "inputs": inputs,
                    "shortest": shortest,
                    "layout": layout,
                    "grid": grid,
                    "grid_tile_size": grid_tile_size,
                    "fill": fill,
                }
                | kwargs
            ).items()
        ),
    )
    return filter_node.video(0)
