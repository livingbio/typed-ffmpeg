import re
from typing import Any, Literal

from .nodes.nodes import FilterableStream, FilterNode
from .schema import (
    BOOLEAN,
    COLOR,
    DOUBLE,
    DURATION,
    FLAGS,
    FLOAT,
    IMAGE_SIZE,
    INT,
    INT64,
    PIX_FMT,
    STRING,
    VIDEO_RATE,
    Default,
    StreamType,
)
from .streams.audio import AudioStream
from .streams.video import VideoStream


def acrossfade(
    _crossfade0: "AudioStream",
    _crossfade1: "AudioStream",
    *,
    nb_samples: INT = Default("44100"),
    duration: DURATION = Default("0"),
    overlap: BOOLEAN = Default("true"),
    curve1: INT
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
    curve2: INT
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

    :param INT nb_samples: set number of samples for cross fade duration (from 1 to 2.14748e+08) (default 44100)
    :param DURATION duration: set cross fade duration (default 0)
    :param BOOLEAN overlap: overlap 1st stream end with 2nd stream start (default true)
    :param INT curve1: set fade curve type for 1st stream (from -1 to 18) (default tri)
    :param INT curve2: set fade curve type for 2nd stream (from -1 to 18) (default tri)

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
    dry: FLOAT = Default("1"),
    wet: FLOAT = Default("1"),
    length: FLOAT = Default("1"),
    gtype: INT | Literal["none", "peak", "dc", "gn", "ac", "rms"] | Default = Default("peak"),
    irgain: FLOAT = Default("1"),
    irfmt: INT | Literal["mono", "input"] | Default = Default("input"),
    maxir: FLOAT = Default("30"),
    response: BOOLEAN = Default("false"),
    channel: INT = Default("0"),
    size: IMAGE_SIZE = Default("hd720"),
    rate: VIDEO_RATE = Default("25"),
    minp: INT = Default("8192"),
    maxp: INT = Default("8192"),
    nbirs: INT = Default("1"),
    ir: INT = Default("0"),
    precision: INT | Literal["auto", "float", "double"] | Default = Default("auto"),
    **kwargs: Any
) -> FilterNode:
    """

    Apply Finite Impulse Response filter with supplied coefficients in additional stream(s).

    Parameters:
    ----------

    :param FLOAT dry: set dry gain (from 0 to 10) (default 1)
    :param FLOAT wet: set wet gain (from 0 to 10) (default 1)
    :param FLOAT length: set IR length (from 0 to 1) (default 1)
    :param INT gtype: set IR auto gain type (from -1 to 4) (default peak)
    :param FLOAT irgain: set IR gain (from 0 to 1) (default 1)
    :param INT irfmt: set IR format (from 0 to 1) (default input)
    :param FLOAT maxir: set max IR length (from 0.1 to 60) (default 30)
    :param BOOLEAN response: show IR frequency response (default false)
    :param INT channel: set IR channel to display frequency response (from 0 to 1024) (default 0)
    :param IMAGE_SIZE size: set video size (default "hd720")
    :param VIDEO_RATE rate: set video rate (default "25")
    :param INT minp: set min partition size (from 1 to 65536) (default 8192)
    :param INT maxp: set max partition size (from 8 to 65536) (default 8192)
    :param INT nbirs: set number of input IRs (from 1 to 32) (default 1)
    :param INT ir: select IR (from 0 to 31) (default 0)
    :param INT precision: set processing precision (from 0 to 2) (default auto)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afir

    """
    filter_node = FilterNode(
        name="afir",
        input_typings=tuple([StreamType.audio] * int(nbirs)),
        output_typings=None,
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

    return filter_node


def ainterleave(
    *streams: "AudioStream",
    nb_inputs: INT = Default("2"),
    duration: INT | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    **kwargs: Any
) -> "AudioStream":
    """

    Temporally interleave audio inputs.

    Parameters:
    ----------

    :param INT nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    :param INT duration: how to determine the end-of-stream (from 0 to 2) (default longest)

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
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Copy the luma value of the second input into the alpha channel of the first input.

    Parameters:
    ----------

    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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


def amerge(*streams: "AudioStream", inputs: INT = Default("2"), **kwargs: Any) -> "AudioStream":
    """

    Merge two or more audio streams into a single multi-channel stream.

    Parameters:
    ----------

    :param INT inputs: specify the number of inputs (from 1 to 64) (default 2)

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
    inputs: INT = Default("2"),
    duration: INT | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    dropout_transition: FLOAT = Default("2"),
    weights: STRING = Default("1 1"),
    normalize: BOOLEAN = Default("true"),
    **kwargs: Any
) -> "AudioStream":
    """

    Audio mixing.

    Parameters:
    ----------

    :param INT inputs: Number of inputs. (from 1 to 32767) (default 2)
    :param INT duration: How to determine the end-of-stream. (from 0 to 2) (default longest)
    :param FLOAT dropout_transition: Transition time, in seconds, for volume renormalization when an input stream ends. (from 0 to INT_MAX) (default 2)
    :param STRING weights: Set weight for each input. (default "1 1")
    :param BOOLEAN normalize: Scale inputs (default true)

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
    order: INT = Default("256"),
    mu: FLOAT = Default("0.75"),
    eps: FLOAT = Default("1"),
    leakage: FLOAT = Default("0"),
    out_mode: INT | Literal["i", "d", "o", "n"] | Default = Default("o"),
    enable: str = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply Normalized Least-Mean-Fourth algorithm to first audio stream.

    Parameters:
    ----------

    :param INT order: set the filter order (from 1 to 32767) (default 256)
    :param FLOAT mu: set the filter mu (from 0 to 2) (default 0.75)
    :param FLOAT eps: set the filter eps (from 0 to 1) (default 1)
    :param FLOAT leakage: set the filter leakage (from 0 to 1) (default 0)
    :param INT out_mode: set output mode (from 0 to 3) (default o)
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
    order: INT = Default("256"),
    mu: FLOAT = Default("0.75"),
    eps: FLOAT = Default("1"),
    leakage: FLOAT = Default("0"),
    out_mode: INT | Literal["i", "d", "o", "n"] | Default = Default("o"),
    enable: str = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply Normalized Least-Mean-Squares algorithm to first audio stream.

    Parameters:
    ----------

    :param INT order: set the filter order (from 1 to 32767) (default 256)
    :param FLOAT mu: set the filter mu (from 0 to 2) (default 0.75)
    :param FLOAT eps: set the filter eps (from 0 to 1) (default 1)
    :param FLOAT leakage: set the filter leakage (from 0 to 1) (default 0)
    :param INT out_mode: set output mode (from 0 to 3) (default o)
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


def astreamselect(
    *streams: "AudioStream", inputs: INT = Default("2"), map: STRING = Default(None), **kwargs: Any
) -> FilterNode:
    """

    Select audio streams

    Parameters:
    ----------

    :param INT inputs: number of input streams (from 2 to INT_MAX) (default 2)
    :param STRING map: input indexes to remap to outputs

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
    size: INT = Default("256"),
    algo: INT | Literal["slow", "fast"] | Default = Default("slow"),
    **kwargs: Any
) -> "AudioStream":
    """

    Cross-correlate two audio streams.

    Parameters:
    ----------

    :param INT size: set segment size (from 2 to 131072) (default 256)
    :param INT algo: set algorithm (from 0 to 1) (default slow)

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
    c0_mode: INT
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
    c1_mode: INT
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
    c2_mode: INT
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
    c3_mode: INT
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
    all_mode: INT
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
    c0_expr: STRING = Default(None),
    c1_expr: STRING = Default(None),
    c2_expr: STRING = Default(None),
    c3_expr: STRING = Default(None),
    all_expr: STRING = Default(None),
    c0_opacity: DOUBLE = Default("1"),
    c1_opacity: DOUBLE = Default("1"),
    c2_opacity: DOUBLE = Default("1"),
    c3_opacity: DOUBLE = Default("1"),
    all_opacity: DOUBLE = Default("1"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Blend two video frames into each other.

    Parameters:
    ----------

    :param INT c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
    :param INT c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
    :param INT c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
    :param INT c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
    :param INT all_mode: set blend mode for all components (from -1 to 39) (default -1)
    :param STRING c0_expr: set color component #0 expression
    :param STRING c1_expr: set color component #1 expression
    :param STRING c2_expr: set color component #2 expression
    :param STRING c3_expr: set color component #3 expression
    :param STRING all_expr: set expression for all color components
    :param DOUBLE c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
    :param DOUBLE c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
    :param DOUBLE c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
    :param DOUBLE c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
    :param DOUBLE all_opacity: set opacity for all color components (from 0 to 1) (default 1)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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


def bm3d(
    *streams: "VideoStream",
    sigma: FLOAT = Default("1"),
    block: INT = Default("16"),
    bstep: INT = Default("4"),
    group: INT = Default("1"),
    range: INT = Default("9"),
    mstep: INT = Default("1"),
    thmse: FLOAT = Default("0"),
    hdthr: FLOAT = Default("2.7"),
    estim: INT | Literal["basic", "final"] | Default = Default("basic"),
    ref: BOOLEAN = Default("false"),
    planes: INT = Default("7"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Block-Matching 3D denoiser.

    Parameters:
    ----------

    :param FLOAT sigma: set denoising strength (from 0 to 99999.9) (default 1)
    :param INT block: set size of local patch (from 8 to 64) (default 16)
    :param INT bstep: set sliding step for processing blocks (from 1 to 64) (default 4)
    :param INT group: set maximal number of similar blocks (from 1 to 256) (default 1)
    :param INT range: set block matching range (from 1 to INT_MAX) (default 9)
    :param INT mstep: set step for block matching (from 1 to 64) (default 1)
    :param FLOAT thmse: set threshold of mean square error for block matching (from 0 to INT_MAX) (default 0)
    :param FLOAT hdthr: set hard threshold for 3D transfer domain (from 0 to INT_MAX) (default 2.7)
    :param INT estim: set filtering estimation mode (from 0 to 1) (default basic)
    :param BOOLEAN ref: have reference stream (default false)
    :param INT planes: set planes to filter (from 0 to 15) (default 7)
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
    patch_size: IMAGE_SIZE = Default("64x64"),
    nb_patches: INT = Default("0"),
    type: INT | Literal["relative", "absolute"] | Default = Default("absolute"),
    kernel: INT | Literal["euclidean", "weuclidean"] | Default = Default("euclidean"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply custom Color Maps to video stream.

    Parameters:
    ----------

    :param IMAGE_SIZE patch_size: set patch size (default "64x64")
    :param INT nb_patches: set number of patches (from 0 to 64) (default 0)
    :param INT type: set the target type used (from 0 to 1) (default absolute)
    :param INT kernel: set the kernel used for measuring color difference (from 0 to 1) (default euclidean)
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
    n: INT = Default("2"),
    v: INT = Default("1"),
    a: INT = Default("0"),
    unsafe: BOOLEAN = Default("false"),
    **kwargs: Any
) -> FilterNode:
    """

    Concatenate audio and video streams.

    Parameters:
    ----------

    :param INT n: specify the number of segments (from 1 to INT_MAX) (default 2)
    :param INT v: specify the number of video streams (from 0 to INT_MAX) (default 1)
    :param INT a: specify the number of audio streams (from 0 to INT_MAX) (default 0)
    :param BOOLEAN unsafe: enable unsafe mode (default false)

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
    planes: INT = Default("7"),
    impulse: INT | Literal["first", "all"] | Default = Default("all"),
    noise: FLOAT = Default("1e-07"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Convolve first video stream with second video stream.

    Parameters:
    ----------

    :param INT planes: set planes to convolve (from 0 to 15) (default 7)
    :param INT impulse: when to process impulses (from 0 to 1) (default all)
    :param FLOAT noise: set noise (from 0 to 1) (default 1e-07)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the correlation between two video streams.

    Parameters:
    ----------

    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    cycle: INT = Default("5"),
    dupthresh: DOUBLE = Default("1.1"),
    scthresh: DOUBLE = Default("15"),
    blockx: INT = Default("32"),
    blocky: INT = Default("32"),
    ppsrc: BOOLEAN = Default("false"),
    chroma: BOOLEAN = Default("true"),
    mixed: BOOLEAN = Default("false"),
    **kwargs: Any
) -> "VideoStream":
    """

    Decimate frames (post field matching filter).

    Parameters:
    ----------

    :param INT cycle: set the number of frame from which one will be dropped (from 2 to 25) (default 5)
    :param DOUBLE dupthresh: set duplicate threshold (from 0 to 100) (default 1.1)
    :param DOUBLE scthresh: set scene change threshold (from 0 to 100) (default 15)
    :param INT blockx: set the size of the x-axis blocks used during metric calculations (from 4 to 512) (default 32)
    :param INT blocky: set the size of the y-axis blocks used during metric calculations (from 4 to 512) (default 32)
    :param BOOLEAN ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    :param BOOLEAN chroma: set whether or not chroma is considered in the metric calculations (default true)
    :param BOOLEAN mixed: set whether or not the input only partially contains content to be decimated (default false)

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
    planes: INT = Default("7"),
    impulse: INT | Literal["first", "all"] | Default = Default("all"),
    noise: FLOAT = Default("1e-07"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Deconvolve first video stream with second video stream.

    Parameters:
    ----------

    :param INT planes: set planes to deconvolve (from 0 to 15) (default 7)
    :param INT impulse: when to process impulses (from 0 to 1) (default all)
    :param FLOAT noise: set noise (from 0 to 1) (default 1e-07)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    edge: INT | Literal["blank", "smear", "wrap", "mirror"] | Default = Default("smear"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Displace pixels.

    Parameters:
    ----------

    :param INT edge: set edge mode (from 0 to 3) (default smear)
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
    _default: "VideoStream", _feedin: "VideoStream", *, x: INT = Default("0"), w: INT = Default("0"), **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    Apply feedback video filter.

    Parameters:
    ----------

    :param INT x: set top left crop position (from 0 to INT_MAX) (default 0)
    :param INT w: set crop size (from 0 to INT_MAX) (default 0)

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
    order: INT | Literal["auto", "bff", "tff"] | Default = Default("auto"),
    mode: INT | Literal["pc", "pc_n", "pc_u", "pc_n_ub", "pcn", "pcn_ub"] | Default = Default("pc_n"),
    ppsrc: BOOLEAN = Default("false"),
    field: INT | Literal["auto", "bottom", "top"] | Default = Default("auto"),
    mchroma: BOOLEAN = Default("true"),
    y0: INT = Default("0"),
    scthresh: DOUBLE = Default("12"),
    combmatch: INT | Literal["none", "sc", "full"] | Default = Default("sc"),
    combdbg: INT | Literal["none", "pcn", "pcnub"] | Default = Default("none"),
    cthresh: INT = Default("9"),
    chroma: BOOLEAN = Default("false"),
    blockx: INT = Default("16"),
    blocky: INT = Default("16"),
    combpel: INT = Default("80"),
    **kwargs: Any
) -> "VideoStream":
    """

    Field matching for inverse telecine.

    Parameters:
    ----------

    :param INT order: specify the assumed field order (from -1 to 1) (default auto)
    :param INT mode: set the matching mode or strategy to use (from 0 to 5) (default pc_n)
    :param BOOLEAN ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    :param INT field: set the field to match from (from -1 to 1) (default auto)
    :param BOOLEAN mchroma: set whether or not chroma is included during the match comparisons (default true)
    :param INT y0: define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX) (default 0)
    :param DOUBLE scthresh: set scene change detection threshold (from 0 to 100) (default 12)
    :param INT combmatch: set combmatching mode (from 0 to 2) (default sc)
    :param INT combdbg: enable comb debug (from 0 to 2) (default none)
    :param INT cthresh: set the area combing threshold used for combed frame detection (from -1 to 255) (default 9)
    :param BOOLEAN chroma: set whether or not chroma is considered in the combed frame decision (default false)
    :param INT blockx: set the x-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    :param INT blocky: set the y-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    :param INT combpel: set the number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed (from 0 to INT_MAX) (default 80)

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
    format: INT | Literal["sbs", "tab", "frameseq", "lines", "columns"] | Default = Default("sbs"),
    **kwargs: Any
) -> "VideoStream":
    """

    Generate a frame packed stereoscopic video.

    Parameters:
    ----------

    :param INT format: Frame pack output format (from 0 to INT_MAX) (default sbs)

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
    first: INT64 = Default("0"),
    last: INT64 = Default("0"),
    replace: INT64 = Default("0"),
    **kwargs: Any
) -> "VideoStream":
    """

    Freeze video frames.

    Parameters:
    ----------

    :param INT64 first: set first frame to freeze (from 0 to I64_MAX) (default 0)
    :param INT64 last: set last frame to freeze (from 0 to I64_MAX) (default 0)
    :param INT64 replace: set frame to replace (from 0 to I64_MAX) (default 0)

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
    radius: INT = Default("3"),
    eps: FLOAT = Default("0.01"),
    mode: INT | Literal["basic", "fast"] | Default = Default("basic"),
    sub: INT = Default("4"),
    guidance: INT | Literal["off", "on"] | Default = Default("off"),
    planes: INT = Default("1"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Guided filter.

    Parameters:
    ----------

    :param INT radius: set the box radius (from 1 to 20) (default 3)
    :param FLOAT eps: set the regularization parameter (with square) (from 0 to 1) (default 0.01)
    :param INT mode: set filtering mode (0: basic mode; 1: fast mode) (from 0 to 1) (default basic)
    :param INT sub: subsampling ratio for fast mode (from 2 to 64) (default 4)
    :param INT guidance: set guidance mode (0: off mode; 1: on mode) (from 0 to 1) (default off)
    :param INT planes: set planes to filter (from 0 to 15) (default 1)
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
    clut: INT | Literal["first", "all"] | Default = Default("all"),
    interp: INT | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"] | Default = Default("tetrahedral"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Adjust colors using a Hald CLUT.

    Parameters:
    ----------

    :param INT clut: when to process CLUT (from 0 to 1) (default all)
    :param INT interp: select interpolation mode (from 0 to 4) (default tetrahedral)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    map: STRING = Default(None),
    gain: FLOAT = Default("0"),
    lfe: FLOAT = Default("0"),
    type: INT | Literal["time", "freq"] | Default = Default("freq"),
    size: INT = Default("1024"),
    hrir: INT | Literal["stereo", "multich"] | Default = Default("stereo"),
    **kwargs: Any
) -> "AudioStream":
    """

    Apply headphone binaural spatialization with HRTFs in additional streams.

    Parameters:
    ----------

    :param STRING map: set channels convolution mappings
    :param FLOAT gain: set gain in dB (from -20 to 40) (default 0)
    :param FLOAT lfe: set lfe gain in dB (from -20 to 40) (default 0)
    :param INT type: set processing (from 0 to 1) (default freq)
    :param INT size: set frame size (from 1024 to 96000) (default 1024)
    :param INT hrir: set hrir format (from 0 to 1) (default stereo)

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
    *streams: "VideoStream", inputs: INT = Default("2"), shortest: BOOLEAN = Default("false"), **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs horizontally.

    Parameters:
    ----------

    :param INT inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)

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


def hysteresis(
    _base: "VideoStream",
    _alt: "VideoStream",
    *,
    planes: INT = Default("15"),
    threshold: INT = Default("0"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Grow first stream into second stream by connecting components.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
    :param INT threshold: set threshold (from 0 to 65535) (default 0)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the Identity between two video streams.

    Parameters:
    ----------

    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    nb_inputs: INT = Default("2"),
    duration: INT | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    **kwargs: Any
) -> "VideoStream":
    """

    Temporally interleave video inputs.

    Parameters:
    ----------

    :param INT nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    :param INT duration: how to determine the end-of-stream (from 0 to 2) (default longest)

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
    inputs: INT = Default("2"),
    channel_layout: STRING = Default("stereo"),
    map: STRING = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Join multiple audio streams into multi-channel output.

    Parameters:
    ----------

    :param INT inputs: Number of input streams. (from 1 to INT_MAX) (default 2)
    :param STRING channel_layout: Channel layout of the output stream. (default "stereo")
    :param STRING map: A comma-separated list of channels maps in the format 'input_stream.input_channel-output_channel.

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


def libvmaf(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    model_path: STRING = Default(None),
    log_path: STRING = Default(None),
    log_fmt: STRING = Default("xml"),
    enable_transform: BOOLEAN = Default("false"),
    psnr: BOOLEAN = Default("false"),
    ssim: BOOLEAN = Default("false"),
    ms_ssim: BOOLEAN = Default("false"),
    pool: STRING = Default(None),
    n_threads: INT = Default("0"),
    n_subsample: INT = Default("1"),
    enable_conf_interval: BOOLEAN = Default("false"),
    model: STRING = Default("version=vmaf_v0.6.1"),
    feature: STRING = Default(None),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the VMAF between two video streams.

    Parameters:
    ----------

    :param STRING model_path: use model='path=...'.
    :param STRING log_path: Set the file path to be used to write log.
    :param STRING log_fmt: Set the format of the log (csv, json, xml, or sub). (default "xml")
    :param BOOLEAN enable_transform: use model='enable_transform=true'. (default false)
    :param BOOLEAN psnr: use feature='name=psnr'. (default false)
    :param BOOLEAN ssim: use feature='name=float_ssim'. (default false)
    :param BOOLEAN ms_ssim: use feature='name=float_ms_ssim'. (default false)
    :param STRING pool: Set the pool method to be used for computing vmaf.
    :param INT n_threads: Set number of threads to be used when computing vmaf. (from 0 to UINT32_MAX) (default 0)
    :param INT n_subsample: Set interval for frame subsampling used when computing vmaf. (from 1 to UINT32_MAX) (default 1)
    :param BOOLEAN enable_conf_interval: model='enable_conf_interval=true'. (default false)
    :param STRING model: Set the model to be used for computing vmaf. (default "version=vmaf_v0.6.1")
    :param STRING feature: Set the feature to be used for computing vmaf.
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)

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


def limitdiff(
    *streams: "VideoStream",
    threshold: FLOAT = Default("0.00392157"),
    elasticity: FLOAT = Default("2"),
    reference: BOOLEAN = Default("false"),
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with limiting difference.

    Parameters:
    ----------

    :param FLOAT threshold: set the threshold (from 0 to 1) (default 0.00392157)
    :param FLOAT elasticity: set the elasticity (from 0 to 10) (default 2)
    :param BOOLEAN reference: enable reference stream (default false)
    :param INT planes: set the planes to filter (from 0 to 15) (default 15)
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
    c0: STRING = Default("x"),
    c1: STRING = Default("x"),
    c2: STRING = Default("x"),
    c3: STRING = Default("x"),
    d: INT = Default("0"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Compute and apply a lookup table from two video inputs.

    Parameters:
    ----------

    :param STRING c0: set component #0 expression (default "x")
    :param STRING c1: set component #1 expression (default "x")
    :param STRING c2: set component #2 expression (default "x")
    :param STRING c3: set component #3 expression (default "x")
    :param INT d: set output depth (from 0 to 16) (default 0)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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


def maskedclamp(
    _base: "VideoStream",
    _dark: "VideoStream",
    _bright: "VideoStream",
    *,
    undershoot: INT = Default("0"),
    overshoot: INT = Default("0"),
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Clamp first stream with second stream and third stream.

    Parameters:
    ----------

    :param INT undershoot: set undershoot (from 0 to 65535) (default 0)
    :param INT overshoot: set overshoot (from 0 to 65535) (default 0)
    :param INT planes: set planes (from 0 to 15) (default 15)
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
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with maximum difference of two streams.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
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
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Merge first stream with second stream using third stream as mask.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
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
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply filtering with minimum difference of two streams.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
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
    threshold: INT = Default("1"),
    planes: INT = Default("15"),
    mode: INT | Literal["abs", "diff"] | Default = Default("abs"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Pick pixels comparing absolute difference of two streams with threshold.

    Parameters:
    ----------

    :param INT threshold: set threshold (from 0 to 65535) (default 1)
    :param INT planes: set planes (from 0 to 15) (default 15)
    :param INT mode: set mode (from 0 to 1) (default abs)
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
    mapping: INT = Default("-1"),
    format: PIX_FMT = Default("yuva444p"),
    map0s: INT = Default("0"),
    map0p: INT = Default("0"),
    map1s: INT = Default("0"),
    map1p: INT = Default("0"),
    map2s: INT = Default("0"),
    map2p: INT = Default("0"),
    map3s: INT = Default("0"),
    map3p: INT = Default("0"),
    **kwargs: Any
) -> "VideoStream":
    """

    Merge planes.

    Parameters:
    ----------

    :param INT mapping: set input to output plane mapping (from -1 to 8.58993e+08) (default -1)
    :param PIX_FMT format: set output pixel format (default yuva444p)
    :param INT map0s: set 1st input to output stream mapping (from 0 to 3) (default 0)
    :param INT map0p: set 1st input to output plane mapping (from 0 to 3) (default 0)
    :param INT map1s: set 2nd input to output stream mapping (from 0 to 3) (default 0)
    :param INT map1p: set 2nd input to output plane mapping (from 0 to 3) (default 0)
    :param INT map2s: set 3rd input to output stream mapping (from 0 to 3) (default 0)
    :param INT map2p: set 3rd input to output plane mapping (from 0 to 3) (default 0)
    :param INT map3s: set 4th input to output stream mapping (from 0 to 3) (default 0)
    :param INT map3p: set 4th input to output plane mapping (from 0 to 3) (default 0)

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
    _in0: "VideoStream", _in1: "VideoStream", *, planes: INT = Default("15"), enable: str = Default(None), **kwargs: Any
) -> "VideoStream":
    """

    Apply Midway Equalization.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
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
    inputs: INT = Default("2"),
    weights: STRING = Default("1 1"),
    scale: FLOAT = Default("0"),
    planes: FLAGS = Default("F"),
    duration: INT | Literal["longest", "shortest", "first"] | Default = Default("longest"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Mix video inputs.

    Parameters:
    ----------

    :param INT inputs: set number of inputs (from 2 to 32767) (default 2)
    :param STRING weights: set weight for each input (default "1 1")
    :param FLOAT scale: set scale (from 0 to 32767) (default 0)
    :param FLAGS planes: set what planes to filter (default F)
    :param INT duration: how to determine end of stream (from 0 to 2) (default longest)
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
    mode: INT
    | Literal["erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"]
    | Default = Default("erode"),
    planes: INT = Default("7"),
    structure: INT | Literal["first", "all"] | Default = Default("all"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Morphological filter.

    Parameters:
    ----------

    :param INT mode: set morphological transform (from 0 to 6) (default erode)
    :param INT planes: set planes to filter (from 0 to 15) (default 7)
    :param INT structure: when to process structures (from 0 to 1) (default all)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the MSAD between two video streams.

    Parameters:
    ----------

    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    scale: FLOAT = Default("1"),
    offset: FLOAT = Default("0.5"),
    planes: FLAGS = Default("F"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Multiply first video stream with second video stream.

    Parameters:
    ----------

    :param FLOAT scale: set scale (from 0 to 9) (default 1)
    :param FLOAT offset: set offset (from -1 to 1) (default 0.5)
    :param FLAGS planes: set planes (default F)
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
    x: STRING = Default("0"),
    y: STRING = Default("0"),
    eof_action: INT | Literal["repeat", "endall", "pass", "repeat", "endall", "pass"] | Default = Default("repeat"),
    eval: INT | Literal["init", "frame"] | Default = Default("frame"),
    shortest: BOOLEAN = Default("false"),
    format: INT
    | Literal["yuv420", "yuv420p10", "yuv422", "yuv422p10", "yuv444", "rgb", "gbrp", "auto"]
    | Default = Default("yuv420"),
    repeatlast: BOOLEAN = Default("true"),
    alpha: INT | Literal["straight", "premultiplied"] | Default = Default("straight"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Overlay a video source on top of the input.

    Parameters:
    ----------

    :param STRING x: set the x expression (default "0")
    :param STRING y: set the y expression (default "0")
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param INT eval: specify when to evaluate expressions (from 0 to 1) (default frame)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param INT format: set output format (from 0 to 7) (default yuv420)
    :param BOOLEAN repeatlast: repeat overlay of the last overlay frame (default true)
    :param INT alpha: alpha format (from 0 to 1) (default straight)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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


def paletteuse(
    _default: "VideoStream",
    _palette: "VideoStream",
    *,
    dither: INT
    | Literal["bayer", "heckbert", "floyd_steinberg", "sierra2", "sierra2_4a", "sierra3", "burkes", "atkinson"]
    | Default = Default("sierra2_4a"),
    bayer_scale: INT = Default("2"),
    diff_mode: INT | Literal["rectangle"] | Default = Default("0"),
    new: BOOLEAN = Default("false"),
    alpha_threshold: INT = Default("128"),
    debug_kdtree: STRING = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Use a palette to downsample an input video stream.

    Parameters:
    ----------

    :param INT dither: select dithering mode (from 0 to 8) (default sierra2_4a)
    :param INT bayer_scale: set scale for bayer dithering (from 0 to 5) (default 2)
    :param INT diff_mode: set frame difference mode (from 0 to 1) (default 0)
    :param BOOLEAN new: take new palette for each output frame (default false)
    :param INT alpha_threshold: set the alpha threshold for transparency (from 0 to 255) (default 128)
    :param STRING debug_kdtree: save Graphviz graph of the kdtree in specified file

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
    planes: INT = Default("15"),
    inplace: BOOLEAN = Default("false"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    PreMultiply first stream with first plane of second stream.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
    :param BOOLEAN inplace: enable inplace mode (default false)
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


def psnr(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    stats_file: STRING = Default(None),
    stats_version: INT = Default("1"),
    output_max: BOOLEAN = Default("false"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the PSNR between two video streams.

    Parameters:
    ----------

    :param STRING stats_file: Set file where to store per-frame difference information
    :param INT stats_version: Set the format version for the stats file. (from 1 to 2) (default 1)
    :param BOOLEAN output_max: Add raw stats (max values) to the output log. (default false)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    format: INT | Literal["color", "gray"] | Default = Default("color"),
    fill: COLOR = Default("black"),
    **kwargs: Any
) -> "VideoStream":
    """

    Remap pixels.

    Parameters:
    ----------

    :param INT format: set output format (from 0 to 1) (default color)
    :param COLOR fill: set the color of the unmapped pixels (default "black")

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


def scale2ref(
    _default: "VideoStream",
    _ref: "VideoStream",
    *,
    w: STRING = Default(None),
    h: STRING = Default(None),
    flags: STRING = Default(""),
    interl: BOOLEAN = Default("false"),
    in_color_matrix: STRING
    | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
    | Default = Default("auto"),
    out_color_matrix: STRING
    | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
    | Default = Default(None),
    in_range: INT
    | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
    | Default = Default("auto"),
    out_range: INT
    | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
    | Default = Default("auto"),
    in_v_chr_pos: INT = Default("-513"),
    in_h_chr_pos: INT = Default("-513"),
    out_v_chr_pos: INT = Default("-513"),
    out_h_chr_pos: INT = Default("-513"),
    force_original_aspect_ratio: INT | Literal["disable", "decrease", "increase"] | Default = Default("disable"),
    force_divisible_by: INT = Default("1"),
    param0: DOUBLE = Default("DBL_MAX"),
    param1: DOUBLE = Default("DBL_MAX"),
    eval: INT | Literal["init", "frame"] | Default = Default("init"),
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    Scale the input video size and/or convert the image format to the given reference.

    Parameters:
    ----------

    :param STRING w: Output video width
    :param STRING h: Output video height
    :param STRING flags: Flags to pass to libswscale (default "")
    :param BOOLEAN interl: set interlacing (default false)
    :param STRING in_color_matrix: set input YCbCr type (default "auto")
    :param STRING out_color_matrix: set output YCbCr type
    :param INT in_range: set input color range (from 0 to 2) (default auto)
    :param INT out_range: set output color range (from 0 to 2) (default auto)
    :param INT in_v_chr_pos: input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param INT in_h_chr_pos: input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param INT out_v_chr_pos: output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param INT out_h_chr_pos: output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
    :param INT force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
    :param INT force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
    :param DOUBLE param0: Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
    :param DOUBLE param1: Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
    :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)

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


def sidechaincompress(
    _main: "AudioStream",
    _sidechain: "AudioStream",
    *,
    level_in: DOUBLE = Default("1"),
    mode: INT | Literal["downward", "upward"] | Default = Default("downward"),
    threshold: DOUBLE = Default("0.125"),
    ratio: DOUBLE = Default("2"),
    attack: DOUBLE = Default("20"),
    release: DOUBLE = Default("250"),
    makeup: DOUBLE = Default("1"),
    knee: DOUBLE = Default("2.82843"),
    link: INT | Literal["average", "maximum"] | Default = Default("average"),
    detection: INT | Literal["peak", "rms"] | Default = Default("rms"),
    level_sc: DOUBLE = Default("1"),
    mix: DOUBLE = Default("1"),
    **kwargs: Any
) -> "AudioStream":
    """

    Sidechain compressor.

    Parameters:
    ----------

    :param DOUBLE level_in: set input gain (from 0.015625 to 64) (default 1)
    :param INT mode: set mode (from 0 to 1) (default downward)
    :param DOUBLE threshold: set threshold (from 0.000976563 to 1) (default 0.125)
    :param DOUBLE ratio: set ratio (from 1 to 20) (default 2)
    :param DOUBLE attack: set attack (from 0.01 to 2000) (default 20)
    :param DOUBLE release: set release (from 0.01 to 9000) (default 250)
    :param DOUBLE makeup: set make up gain (from 1 to 64) (default 1)
    :param DOUBLE knee: set knee (from 1 to 8) (default 2.82843)
    :param INT link: set link type (from 0 to 1) (default average)
    :param INT detection: set detection (from 0 to 1) (default rms)
    :param DOUBLE level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
    :param DOUBLE mix: set mix (from 0 to 1) (default 1)

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
    level_in: DOUBLE = Default("1"),
    mode: INT | Literal["downward", "upward"] | Default = Default("downward"),
    range: DOUBLE = Default("0.06125"),
    threshold: DOUBLE = Default("0.125"),
    ratio: DOUBLE = Default("2"),
    attack: DOUBLE = Default("20"),
    release: DOUBLE = Default("250"),
    makeup: DOUBLE = Default("1"),
    knee: DOUBLE = Default("2.82843"),
    detection: INT | Literal["peak", "rms"] | Default = Default("rms"),
    link: INT | Literal["average", "maximum"] | Default = Default("average"),
    level_sc: DOUBLE = Default("1"),
    enable: str = Default(None),
    **kwargs: Any
) -> "AudioStream":
    """

    Audio sidechain gate.

    Parameters:
    ----------

    :param DOUBLE level_in: set input level (from 0.015625 to 64) (default 1)
    :param INT mode: set mode (from 0 to 1) (default downward)
    :param DOUBLE range: set max gain reduction (from 0 to 1) (default 0.06125)
    :param DOUBLE threshold: set threshold (from 0 to 1) (default 0.125)
    :param DOUBLE ratio: set ratio (from 1 to 9000) (default 2)
    :param DOUBLE attack: set attack (from 0.01 to 9000) (default 20)
    :param DOUBLE release: set release (from 0.01 to 9000) (default 250)
    :param DOUBLE makeup: set makeup gain (from 1 to 64) (default 1)
    :param DOUBLE knee: set knee (from 1 to 8) (default 2.82843)
    :param INT detection: set detection (from 0 to 1) (default rms)
    :param INT link: set link (from 0 to 1) (default average)
    :param DOUBLE level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
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
    detectmode: INT | Literal["off", "full", "fast"] | Default = Default("off"),
    nb_inputs: INT = Default("1"),
    filename: STRING = Default(""),
    format: INT | Literal["binary", "xml"] | Default = Default("binary"),
    th_d: INT = Default("9000"),
    th_dc: INT = Default("60000"),
    th_xh: INT = Default("116"),
    th_di: INT = Default("0"),
    th_it: DOUBLE = Default("0.5"),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the MPEG-7 video signature

    Parameters:
    ----------

    :param INT detectmode: set the detectmode (from 0 to 2) (default off)
    :param INT nb_inputs: number of inputs (from 1 to INT_MAX) (default 1)
    :param STRING filename: filename for output files (default "")
    :param INT format: set output format (from 0 to 1) (default binary)
    :param INT th_d: threshold to detect one word as similar (from 1 to INT_MAX) (default 9000)
    :param INT th_dc: threshold to detect all words as similar (from 1 to INT_MAX) (default 60000)
    :param INT th_xh: threshold to detect frames as similar (from 1 to INT_MAX) (default 116)
    :param INT th_di: minimum length of matching sequence in frames (from 0 to INT_MAX) (default 0)
    :param DOUBLE th_it: threshold for relation of good to all frames (from 0 to 1) (default 0.5)

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
    sample_rate: INT = Default("44100"),
    channels: INT = Default("1"),
    scale: INT | Literal["lin", "log"] | Default = Default("log"),
    slide: INT | Literal["replace", "scroll", "fullframe", "rscroll"] | Default = Default("fullframe"),
    win_func: INT
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
    overlap: FLOAT = Default("1"),
    orientation: INT | Literal["vertical", "horizontal"] | Default = Default("vertical"),
    **kwargs: Any
) -> "AudioStream":
    """

    Convert input spectrum videos to audio output.

    Parameters:
    ----------

    :param INT sample_rate: set sample rate (from 15 to INT_MAX) (default 44100)
    :param INT channels: set channels (from 1 to 8) (default 1)
    :param INT scale: set input amplitude scale (from 0 to 1) (default log)
    :param INT slide: set input sliding mode (from 0 to 3) (default fullframe)
    :param INT win_func: set window function (from 0 to 20) (default rect)
    :param FLOAT overlap: set window overlap (from 0 to 1) (default 1)
    :param INT orientation: set orientation (from 0 to 1) (default vertical)

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
    stats_file: STRING = Default(None),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the SSIM between two video streams.

    Parameters:
    ----------

    :param STRING stats_file: Set file where to store per-frame difference information
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    *streams: "VideoStream", inputs: INT = Default("2"), map: STRING = Default(None), **kwargs: Any
) -> FilterNode:
    """

    Select video streams

    Parameters:
    ----------

    :param INT inputs: number of input streams (from 2 to INT_MAX) (default 2)
    :param STRING map: input indexes to remap to outputs

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
    planes: INT = Default("15"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Threshold first video stream using other video streams.

    Parameters:
    ----------

    :param INT planes: set planes to filter (from 0 to 15) (default 15)
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
    planes: INT = Default("15"),
    inplace: BOOLEAN = Default("false"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    UnPreMultiply first stream with first plane of second stream.

    Parameters:
    ----------

    :param INT planes: set planes (from 0 to 15) (default 15)
    :param BOOLEAN inplace: enable inplace mode (default false)
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
    min_r: INT = Default("0"),
    max_r: INT = Default("8"),
    planes: INT = Default("15"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Apply Variable Blur filter.

    Parameters:
    ----------

    :param INT min_r: set min blur radius (from 0 to 254) (default 0)
    :param INT max_r: set max blur radius (from 1 to 255) (default 8)
    :param INT planes: set planes to filter (from 0 to 15) (default 15)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Calculate the VIF between two video streams.

    Parameters:
    ----------

    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    *streams: "VideoStream", inputs: INT = Default("2"), shortest: BOOLEAN = Default("false"), **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs vertically.

    Parameters:
    ----------

    :param INT inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)

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


def xcorrelate(
    _primary: "VideoStream",
    _secondary: "VideoStream",
    *,
    planes: INT = Default("7"),
    secondary: INT | Literal["first", "all"] | Default = Default("all"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Cross-correlate first video stream with second video stream.

    Parameters:
    ----------

    :param INT planes: set planes to cross-correlate (from 0 to 15) (default 7)
    :param INT secondary: when to process secondary frame (from 0 to 1) (default all)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    transition: INT
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
    duration: DURATION = Default("1"),
    offset: DURATION = Default("0"),
    expr: STRING = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Cross fade one video with another video.

    Parameters:
    ----------

    :param INT transition: set cross fade transition (from -1 to 45) (default fade)
    :param DURATION duration: set cross fade duration (default 1)
    :param DURATION offset: set cross fade start relative to first input stream (default 0)
    :param STRING expr: set expression for custom transition

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


def xmedian(
    *streams: "VideoStream",
    inputs: INT = Default("3"),
    planes: INT = Default("15"),
    percentile: FLOAT = Default("0.5"),
    eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
    shortest: BOOLEAN = Default("false"),
    repeatlast: BOOLEAN = Default("true"),
    ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
    enable: str = Default(None),
    **kwargs: Any
) -> "VideoStream":
    """

    Pick median pixels from several video inputs.

    Parameters:
    ----------

    :param INT inputs: set number of inputs (from 3 to 255) (default 3)
    :param INT planes: set planes to filter (from 0 to 15) (default 15)
    :param FLOAT percentile: set percentile (from 0 to 1) (default 0.5)
    :param INT eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param BOOLEAN repeatlast: extend last frame of secondary streams beyond EOF (default true)
    :param INT ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
    inputs: INT = Default("2"),
    layout: STRING = Default(None),
    grid: IMAGE_SIZE = Default(None),
    shortest: BOOLEAN = Default("false"),
    fill: STRING = Default("none"),
    **kwargs: Any
) -> "VideoStream":
    """

    Stack video inputs into custom layout.

    Parameters:
    ----------

    :param INT inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    :param STRING layout: set custom layout
    :param IMAGE_SIZE grid: set fixed size grid layout
    :param BOOLEAN shortest: force termination when the shortest input terminates (default false)
    :param STRING fill: set the color for unused pixels (default "none")

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
