from typing import Any

from .base import FilterNode
from .stream import AudioStream, VideoStream


def aap(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int = None,
    projection: int = None,
    mu: float = None,
    delta: float = None,
    out_mode: int = None,
    precision: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.1 aap
    Apply Affine Projection algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to estimate unknown audio based on multiple input audio samples.
    Affine projection algorithm can make trade-offs between computation complexity with convergence speed.

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int order: Set the filter order.
    :param int projection: Set the projection order.
    :param float mu: Set the filter mu.
    :param float delta: Set the coefficient to initialize internal covariance matrix.
    :param int out_mode: Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aap

    """
    filter_node = FilterNode(
        name="aap",
        streams=[
            _input,
            _desired,
        ],
        kwargs={
            "order": order,
            "projection": projection,
            "mu": mu,
            "delta": delta,
            "out_mode": out_mode,
            "precision": precision,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def acrossfade(
    _crossfade0: "AudioStream",
    _crossfade1: "AudioStream",
    *,
    nb_samples: int = None,
    duration: int = None,
    overlap: bool = None,
    curve1: int = None,
    curve2: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.5 acrossfade
    Apply cross fade from one input audio stream to another input audio stream.
    The cross fade is applied for specified duration near the end of first stream.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int nb_samples: Specify the number of samples for which the cross fade effect has to last. At the end of the cross fade effect the first input audio will be completely silent. Default is 44100.
    :param int duration: Specify the duration of the cross fade effect. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. By default the duration is determined by nb_samples. If set this option is used instead of nb_samples.
    :param bool overlap: Should first stream end overlap with second stream start. Default is enabled.
    :param int curve1: Set curve for cross fade transition for first stream.
    :param int curve2: Set curve for cross fade transition for second stream. For description of available curve types see afade filter description.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossfade

    """
    filter_node = FilterNode(
        name="acrossfade",
        streams=[
            _crossfade0,
            _crossfade1,
        ],
        kwargs={
            "nb_samples": nb_samples,
            "duration": duration,
            "overlap": overlap,
            "curve1": curve1,
            "curve2": curve2,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def afir(
    *streams: "AudioStream",
    dry: float = None,
    wet: float = None,
    length: float = None,
    gtype: int = None,
    irnorm: float = None,
    irlink: bool = None,
    irgain: float = None,
    irfmt: int = None,
    maxir: float = None,
    response: bool = None,
    channel: int = None,
    size: str = None,
    rate: str = None,
    minp: int = None,
    maxp: int = None,
    nbirs: int = None,
    ir: int = None,
    precision: int = None,
    irload: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.25 afir
    Apply an arbitrary Finite Impulse Response filter.

    This filter is designed for applying long FIR filters,
    up to 60 seconds long.

    It can be used as component for digital crossover filters,
    room equalization, cross talk cancellation, wavefield synthesis,
    auralization, ambiophonics, ambisonics and spatialization.

    This filter uses the streams higher than first one as FIR coefficients.
    If the non-first stream holds a single channel, it will be used
    for all input channels in the first stream, otherwise
    the number of channels in the non-first stream must be same as
    the number of channels in the first stream.

    It accepts the following parameters:

    Parameters:
    ----------

    :param float dry: Set dry gain. This sets input gain.
    :param float wet: Set wet gain. This sets final output gain.
    :param float length: Set Impulse Response filter length. Default is 1, which means whole IR is processed.
    :param int gtype: This option is deprecated, and does nothing.
    :param float irnorm: Set norm to be applied to IR coefficients before filtering. Allowed range is from -1 to 2. IR coefficients are normalized with calculated vector norm set by this option. For negative values, no norm is calculated, and IR coefficients are not modified at all. Default is 1.
    :param bool irlink: For multichannel IR if this option is set to true, all IR channels will be normalized with maximal measured gain of all IR channels coefficients as set by irnorm option. When disabled, all IR coefficients in each IR channel will be normalized independently. Default is true.
    :param float irgain: Set gain to be applied to IR coefficients before filtering. Allowed range is 0 to 1. This gain is applied after any gain applied with irnorm option.
    :param int irfmt: Set format of IR stream. Can be mono or input. Default is input.
    :param float maxir: Set max allowed Impulse Response filter duration in seconds. Default is 30 seconds. Allowed range is 0.1 to 60 seconds.
    :param bool response: This option is deprecated, and does nothing.
    :param int channel: This option is deprecated, and does nothing.
    :param str size: This option is deprecated, and does nothing.
    :param str rate: This option is deprecated, and does nothing.
    :param int minp: Set minimal partition size used for convolution. Default is 8192. Allowed range is from 1 to 65536. Lower values decreases latency at cost of higher CPU usage.
    :param int maxp: Set maximal partition size used for convolution. Default is 8192. Allowed range is from 8 to 65536. Lower values may increase CPU usage.
    :param int nbirs: Set number of input impulse responses streams which will be switchable at runtime. Allowed range is from 1 to 32. Default is 1.
    :param int ir: Set IR stream which will be used for convolution, starting from 0, should always be lower than supplied value by nbirs option. Default is 0. This option can be changed at runtime via commands.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format. Default value is auto.
    :param int irload: Set when to load IR stream. Can be init or access. First one load and prepares all IRs on initialization, second one once on first access of specific IR. Default is init.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#afir

    """
    filter_node = FilterNode(
        name="afir",
        streams=[
            *streams,
        ],
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
        }
        | kwargs,
    )
    return filter_node.audio(0)


def ainterleave(*streams: "AudioStream", nb_inputs: int = None, duration: int = None, **kwargs: Any) -> "AudioStream":
    """

    18.11 interleave, ainterleave
    Temporally interleave frames from several inputs.

    interleave works with video inputs, ainterleave with audio.

    These filters read frames from several inputs and send the oldest
    queued frame to the output.

    Input streams must have well defined, monotonically increasing frame
    timestamp values.

    In order to submit one frame to output, these filters need to enqueue
    at least one frame for each input, so they cannot work in case one
    input is not yet terminated and will not receive incoming frames.

    For example consider the case when one input is a select filter
    which always drops input frames. The interleave filter will keep
    reading from that input, but it will never be able to send new frames
    to output until the input sends an end-of-stream signal.

    Also, depending on inputs synchronization, the filters will drop
    frames in case one input receives more frames than the other ones, and
    the queue is already filled.

    These filters accept the following options:

    Parameters:
    ----------

    :param int nb_inputs: Set the number of different inputs, it is 2 by default.
    :param int duration: How to determine the end-of-stream. longest The duration of the longest input. (default) shortest The duration of the shortest input. first The duration of the first input.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave

    """
    filter_node = FilterNode(
        name="ainterleave",
        streams=[
            *streams,
        ],
        kwargs={
            "nb_inputs": nb_inputs,
            "duration": duration,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def alphamerge(_main: "VideoStream", _alpha: "VideoStream", **kwargs: Any) -> "VideoStream":
    """

    11.3 alphamerge
    Add or replace the alpha component of the primary input with the
    grayscale value of a second input. This is intended for use with
    alphaextract to allow the transmission or storage of frame
    sequences that have alpha in a format that doesn’t support an alpha
    channel.

    For example, to reconstruct full frames from a normal YUV-encoded video
    and a separate video created with alphaextract, you might use:

    movie=in_alpha.mkv [alpha]; [in][alpha] alphamerge [out]

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#alphamerge

    """
    filter_node = FilterNode(
        name="alphamerge",
        streams=[
            _main,
            _alpha,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.video(0)


def amerge(*streams: "AudioStream", inputs: int = None, **kwargs: Any) -> "AudioStream":
    """

    8.34 amerge
    Merge two or more audio streams into a single multi-channel stream.

    The filter accepts the following options:


    If the channel layouts of the inputs are disjoint, and therefore compatible,
    the channel layout of the output will be set accordingly and the channels
    will be reordered as necessary. If the channel layouts of the inputs are not
    disjoint, the output will have all the channels of the first input then all
    the channels of the second input, in that order, and the channel layout of
    the output will be the default value corresponding to the total number of
    channels.

    For example, if the first input is in 2.1 (FL+FR+LF) and the second input
    is FC+BL+BR, then the output will be in 5.1, with the channels in the
    following order: a1, a2, b1, a3, b2, b3 (a1 is the first channel of the
    first input, b1 is the first channel of the second input).

    On the other hand, if both input are in stereo, the output channels will be
    in the default order: a1, a2, b1, b2, and the channel layout will be
    arbitrarily set to 4.0, which may or may not be the expected value.

    All inputs must have the same sample rate, and format.

    If inputs do not have the same duration, the output will stop with the
    shortest.

    Parameters:
    ----------

    :param int inputs: Set the number of inputs. Default is 2.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amerge

    """
    filter_node = FilterNode(
        name="amerge",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def amix(
    *streams: "AudioStream",
    inputs: int = None,
    duration: int = None,
    dropout_transition: float = None,
    weights: str = None,
    normalize: bool = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.35 amix
    Mixes multiple audio inputs into a single output.

    Note that this filter only supports float samples (the amerge
    and pan audio filters support many formats). If the amix
    input has integer samples then aresample will be automatically
    inserted to perform the conversion to float samples.

    It accepts the following parameters:

    Parameters:
    ----------

    :param int inputs: The number of inputs. If unspecified, it defaults to 2.
    :param int duration: How to determine the end-of-stream. longest The duration of the longest input. (default) shortest The duration of the shortest input. first The duration of the first input.
    :param float dropout_transition: The transition time, in seconds, for volume renormalization when an input stream ends. The default value is 2 seconds.
    :param str weights: Specify weight of each input audio stream as a sequence of numbers separated by a space. If fewer weights are specified compared to number of inputs, the last weight is assigned to the remaining inputs. Default weight for each input is 1.
    :param bool normalize: Always scale inputs instead of only doing summation of samples. Beware of heavy clipping if inputs are not normalized prior or after filtering by this filter if this option is disabled. By default is enabled.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amix

    """
    filter_node = FilterNode(
        name="amix",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "duration": duration,
            "dropout_transition": dropout_transition,
            "weights": weights,
            "normalize": normalize,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def amultiply(_multiply0: "AudioStream", _multiply1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    8.36 amultiply
    Multiply first audio stream with second audio stream and store result
    in output audio stream. Multiplication is done by multiplying each
    sample from first stream with sample at same position from second stream.

    With this element-wise multiplication one can create amplitude fades and
    amplitude modulations.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#amultiply

    """
    filter_node = FilterNode(
        name="amultiply",
        streams=[
            _multiply0,
            _multiply1,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.audio(0)


def anlmf(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int = None,
    mu: float = None,
    eps: float = None,
    leakage: float = None,
    out_mode: int = None,
    precision: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.39 anlmf, anlms
    Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to mimic a desired filter by finding the filter coefficients that
    relate to producing the least mean square of the error signal (difference between the desired,
    2nd input audio stream and the actual signal, the 1st input audio stream).

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int order: Set filter order.
    :param float mu: Set filter mu.
    :param float eps: Set the filter eps.
    :param float leakage: Set the filter leakage.
    :param int out_mode: It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

    """
    filter_node = FilterNode(
        name="anlmf",
        streams=[
            _input,
            _desired,
        ],
        kwargs={
            "order": order,
            "mu": mu,
            "eps": eps,
            "leakage": leakage,
            "out_mode": out_mode,
            "precision": precision,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def anlms(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int = None,
    mu: float = None,
    eps: float = None,
    leakage: float = None,
    out_mode: int = None,
    precision: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.39 anlmf, anlms
    Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to mimic a desired filter by finding the filter coefficients that
    relate to producing the least mean square of the error signal (difference between the desired,
    2nd input audio stream and the actual signal, the 1st input audio stream).

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int order: Set filter order.
    :param float mu: Set filter mu.
    :param float eps: Set the filter eps.
    :param float leakage: Set the filter leakage.
    :param int out_mode: It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

    """
    filter_node = FilterNode(
        name="anlms",
        streams=[
            _input,
            _desired,
        ],
        kwargs={
            "order": order,
            "mu": mu,
            "eps": eps,
            "leakage": leakage,
            "out_mode": out_mode,
            "precision": precision,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def apsnr(_input0: "AudioStream", _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    8.44 apsnr
    Measure Audio Peak Signal-to-Noise Ratio.

    This filter takes two audio streams for input, and outputs first
    audio stream.
    Results are in dB per channel at end of either input.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#apsnr

    """
    filter_node = FilterNode(
        name="apsnr",
        streams=[
            _input0,
            _input1,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.audio(0)


def arls(
    _input: "AudioStream",
    _desired: "AudioStream",
    *,
    order: int = None,
    _lambda: float = None,
    delta: float = None,
    out_mode: int = None,
    precision: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.49 arls
    Apply Recursive Least Squares algorithm to the first audio stream using the second audio stream.

    This adaptive filter is used to mimic a desired filter by recursively finding the filter coefficients that
    relate to producing the minimal weighted linear least squares cost function of the error signal (difference
    between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream).

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int order: Set the filter order.
    :param float _lambda: Set the forgetting factor.
    :param float delta: Set the coefficient to initialize internal covariance matrix.
    :param int out_mode: Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
    :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#arls

    """
    filter_node = FilterNode(
        name="arls",
        streams=[
            _input,
            _desired,
        ],
        kwargs={
            "order": order,
            "lambda": _lambda,
            "delta": delta,
            "out_mode": out_mode,
            "precision": precision,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def asdr(_input0: "AudioStream", _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    8.51 asdr
    Measure Audio Signal-to-Distortion Ratio.

    This filter takes two audio streams for input, and outputs first
    audio stream.
    Results are in dB per channel at end of either input.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#asdr

    """
    filter_node = FilterNode(
        name="asdr",
        streams=[
            _input0,
            _input1,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.audio(0)


def asisdr(_input0: "AudioStream", _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
    """

    8.55 asisdr
    Measure Audio Scaled-Invariant Signal-to-Distortion Ratio.

    This filter takes two audio streams for input, and outputs first
    audio stream.
    Results are in dB per channel at end of either input.

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#asisdr

    """
    filter_node = FilterNode(
        name="asisdr",
        streams=[
            _input0,
            _input1,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.audio(0)


def astreamselect(*streams: "AudioStream", inputs: int = None, map: str, **kwargs: Any) -> FilterNode:
    """

    11.245 streamselect, astreamselect
    Select video or audio streams.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int inputs: Set number of inputs. Default is 2.
    :param str map: Set input indexes to remap to outputs.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

    """
    filter_node = FilterNode(
        name="astreamselect",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "map": map,
        }
        | kwargs,
    )

    return filter_node


def axcorrelate(
    _axcorrelate0: "AudioStream", _axcorrelate1: "AudioStream", *, size: int = None, algo: int = None, **kwargs: Any
) -> "AudioStream":
    """

    8.68 axcorrelate
    Calculate normalized windowed cross-correlation between two input audio streams.

    Resulted samples are always between -1 and 1 inclusive.
    If result is 1 it means two input samples are highly correlated in that selected segment.
    Result 0 means they are not correlated at all.
    If result is -1 it means two input samples are out of phase, which means they cancel each
    other.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int size: Set size of segment over which cross-correlation is calculated. Default is 256. Allowed range is from 2 to 131072.
    :param int algo: Set algorithm for cross-correlation. Can be slow or fast or best. Default is best. Fast algorithm assumes mean values over any given segment are always zero and thus need much less calculations to make. This is generally not true, but is valid for typical audio streams.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#axcorrelate

    """
    filter_node = FilterNode(
        name="axcorrelate",
        streams=[
            _axcorrelate0,
            _axcorrelate1,
        ],
        kwargs={
            "size": size,
            "algo": algo,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def blend(
    _top: "VideoStream",
    _bottom: "VideoStream",
    *,
    c0_mode: int = None,
    c1_mode: int = None,
    c2_mode: int = None,
    c3_mode: int = None,
    all_mode: int = None,
    c0_expr: str,
    c1_expr: str,
    c2_expr: str,
    c3_expr: str,
    all_expr: str,
    c0_opacity: float = None,
    c1_opacity: float = None,
    c2_opacity: float = None,
    c3_opacity: float = None,
    all_opacity: float = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.15 blend
    Blend two video frames into each other.

    The blend filter takes two input streams and outputs one
    stream, the first input is the "top" layer and second input is
    "bottom" layer.  By default, the output terminates when the longest input terminates.

    The tblend (time blend) filter takes two consecutive frames
    from one single stream, and outputs the result obtained by blending
    the new frame on top of the old frame.

    A description of the accepted options follows.


    The blend filter also supports the framesync options.

    Parameters:
    ----------

    :param int c0_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
    :param int c1_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
    :param int c2_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
    :param int c3_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
    :param int all_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
    :param str c0_expr: Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
    :param str c1_expr: Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
    :param str c2_expr: Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
    :param str c3_expr: Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
    :param str all_expr: Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
    :param float c0_opacity: Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
    :param float c1_opacity: Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
    :param float c2_opacity: Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
    :param float c3_opacity: Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
    :param float all_opacity: Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#blend

    """
    filter_node = FilterNode(
        name="blend",
        streams=[
            _top,
            _bottom,
        ],
        kwargs={
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
        }
        | kwargs,
    )
    return filter_node.video(0)


def blend_vulkan(
    _top: "VideoStream",
    _bottom: "VideoStream",
    *,
    c0_mode: int = None,
    c1_mode: int = None,
    c2_mode: int = None,
    c3_mode: int = None,
    all_mode: int = None,
    c0_opacity: float = None,
    c1_opacity: float = None,
    c2_opacity: float = None,
    c3_opacity: float = None,
    all_opacity: float = None,
    **kwargs: Any
) -> "VideoStream":
    """

    14.2 blend_vulkan
    Blend two Vulkan frames into each other.

    The blend filter takes two input streams and outputs one
    stream, the first input is the "top" layer and second input is
    "bottom" layer.  By default, the output terminates when the longest input terminates.

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int c0_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c1_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c2_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int c3_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param int all_mode: Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘normal’ ‘multiply’
    :param float c0_opacity: None
    :param float c1_opacity: None
    :param float c2_opacity: None
    :param float c3_opacity: None
    :param float all_opacity: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#blend_005fvulkan

    """
    filter_node = FilterNode(
        name="blend_vulkan",
        streams=[
            _top,
            _bottom,
        ],
        kwargs={
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
        | kwargs,
    )
    return filter_node.video(0)


def bm3d(
    *streams: "VideoStream",
    sigma: float = None,
    block: int = None,
    bstep: int = None,
    group: int = None,
    range: int = None,
    mstep: int = None,
    thmse: float = None,
    hdthr: float = None,
    estim: int = None,
    ref: bool = None,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.18 bm3d
    Denoise frames using Block-Matching 3D algorithm.

    The filter accepts the following options.

    Parameters:
    ----------

    :param float sigma: Set denoising strength. Default value is 1. Allowed range is from 0 to 999.9. The denoising algorithm is very sensitive to sigma, so adjust it according to the source.
    :param int block: Set local patch size. This sets dimensions in 2D.
    :param int bstep: Set sliding step for processing blocks. Default value is 4. Allowed range is from 1 to 64. Smaller values allows processing more reference blocks and is slower.
    :param int group: Set maximal number of similar blocks for 3rd dimension. Default value is 1. When set to 1, no block matching is done. Larger values allows more blocks in single group. Allowed range is from 1 to 256.
    :param int range: Set radius for search block matching. Default is 9. Allowed range is from 1 to INT32_MAX.
    :param int mstep: Set step between two search locations for block matching. Default is 1. Allowed range is from 1 to 64. Smaller is slower.
    :param float thmse: Set threshold of mean square error for block matching. Valid range is 0 to INT32_MAX.
    :param float hdthr: Set thresholding parameter for hard thresholding in 3D transformed domain. Larger values results in stronger hard-thresholding filtering in frequency domain.
    :param int estim: Set filtering estimation mode. Can be basic or final. Default is basic.
    :param bool ref: If enabled, filter will use 2nd stream for block matching. Default is disabled for basic value of estim option, and always enabled if value of estim is final.
    :param int planes: Set planes to filter. Default is all available except alpha.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#bm3d

    """
    filter_node = FilterNode(
        name="bm3d",
        streams=[
            *streams,
        ],
        kwargs={
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
        }
        | kwargs,
    )
    return filter_node.video(0)


def colormap(
    _default: "VideoStream",
    _source: "VideoStream",
    _target: "VideoStream",
    *,
    patch_size: str = None,
    nb_patches: int = None,
    type: int = None,
    kernel: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.39 colormap
    Apply custom color maps to video stream.

    This filter needs three input video streams.
    First stream is video stream that is going to be filtered out.
    Second and third video stream specify color patches for source
    color to target color mapping.

    The filter accepts the following options:

    Parameters:
    ----------

    :param str patch_size: Set the source and target video stream patch size in pixels.
    :param int nb_patches: Set the max number of used patches from source and target video stream. Default value is number of patches available in additional video streams. Max allowed number of patches is 64.
    :param int type: Set the adjustments used for target colors. Can be relative or absolute. Defaults is absolute.
    :param int kernel: Set the kernel used to measure color differences between mapped colors. The accepted values are: ‘euclidean’ ‘weuclidean’ Default is euclidean.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#colormap

    """
    filter_node = FilterNode(
        name="colormap",
        streams=[
            _default,
            _source,
            _target,
        ],
        kwargs={
            "patch_size": patch_size,
            "nb_patches": nb_patches,
            "type": type,
            "kernel": kernel,
        }
        | kwargs,
    )
    return filter_node.video(0)


def concat(
    *streams: "AudioStream", n: int = None, v: int = None, a: int = None, unsafe: bool = None, **kwargs: Any
) -> FilterNode:
    """

    18.9 concat
    Concatenate audio and video streams, joining them together one after the
    other.

    The filter works on segments of synchronized video and audio streams. All
    segments must have the same number of streams of each type, and that will
    also be the number of streams at output.

    The filter accepts the following options:


    The filter has v+a outputs: first v video outputs, then
    a audio outputs.

    There are nx(v+a) inputs: first the inputs for the first
    segment, in the same order as the outputs, then the inputs for the second
    segment, etc.

    Related streams do not always have exactly the same duration, for various
    reasons including codec frame size or sloppy authoring. For that reason,
    related synchronized streams (e.g. a video and its audio track) should be
    concatenated at once. The concat filter will use the duration of the longest
    stream in each segment (except the last one), and if necessary pad shorter
    audio streams with silence.

    For this filter to work correctly, all segments must start at timestamp 0.

    All corresponding streams must have the same parameters in all segments; the
    filtering system will automatically select a common pixel format for video
    streams, and a common sample format, sample rate and channel layout for
    audio streams, but other settings, such as resolution, must be converted
    explicitly by the user.

    Different frame rates are acceptable but will result in variable frame rate
    at output; be sure to configure the output file to handle it.

    Parameters:
    ----------

    :param int n: Set the number of segments. Default is 2.
    :param int v: Set the number of output video streams, that is also the number of video streams in each segment. Default is 1.
    :param int a: Set the number of output audio streams, that is also the number of audio streams in each segment. Default is 0.
    :param bool unsafe: Activate unsafe mode: do not fail if segments have a different format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#concat

    """
    filter_node = FilterNode(
        name="concat",
        streams=[
            *streams,
        ],
        kwargs={
            "n": n,
            "v": v,
            "a": a,
            "unsafe": unsafe,
        }
        | kwargs,
    )

    return filter_node


def convolve(
    _main: "VideoStream",
    _impulse: "VideoStream",
    *,
    planes: int = None,
    impulse: int = None,
    noise: float = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.45 convolve
    Apply 2D convolution of video stream in frequency domain using second stream
    as impulse.

    The filter accepts the following options:


    The convolve filter also supports the framesync options.

    Parameters:
    ----------

    :param int planes: Set which planes to process.
    :param int impulse: Set which impulse video frames will be processed, can be first or all. Default is all.
    :param float noise: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#convolve

    """
    filter_node = FilterNode(
        name="convolve",
        streams=[
            _main,
            _impulse,
        ],
        kwargs={
            "planes": planes,
            "impulse": impulse,
            "noise": noise,
        }
        | kwargs,
    )
    return filter_node.video(0)


def corr(_main: "VideoStream", _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
    """

    11.48 corr
    Obtain the correlation between two input videos.

    This filter takes two input videos.

    Both input videos must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The obtained per component, average, min and max correlation is printed through
    the logging system.

    The filter stores the calculated correlation of each frame in frame metadata.

    This filter also supports the framesync options.

    In the below example the input file main.mpg being processed is compared
    with the reference file ref.mpg.


    ffmpeg -i main.mpg -i ref.mpg -lavfi corr -f null -

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#corr

    """
    filter_node = FilterNode(
        name="corr",
        streams=[
            _main,
            _reference,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.video(0)


def decimate(
    *streams: "VideoStream",
    cycle: int = None,
    dupthresh: float = None,
    scthresh: float = None,
    blockx: int = None,
    blocky: int = None,
    ppsrc: bool = None,
    chroma: bool = None,
    mixed: bool = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.59 decimate
    Drop duplicated frames at regular intervals.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int cycle: Set the number of frames from which one will be dropped. Setting this to N means one frame in every batch of N frames will be dropped. Default is 5.
    :param float dupthresh: Set the threshold for duplicate detection. If the difference metric for a frame is less than or equal to this value, then it is declared as duplicate. Default is 1.1
    :param float scthresh: Set scene change threshold. Default is 15.
    :param int blockx: Set the size of the x and y-axis blocks used during metric calculations. Larger blocks give better noise suppression, but also give worse detection of small movements. Must be a power of two. Default is 32.
    :param int blocky: Set the size of the x and y-axis blocks used during metric calculations. Larger blocks give better noise suppression, but also give worse detection of small movements. Must be a power of two. Default is 32.
    :param bool ppsrc: Mark main input as a pre-processed input and activate clean source input stream. This allows the input to be pre-processed with various filters to help the metrics calculation while keeping the frame selection lossless. When set to 1, the first stream is for the pre-processed input, and the second stream is the clean source from where the kept frames are chosen. Default is 0.
    :param bool chroma: Set whether or not chroma is considered in the metric calculations. Default is 1.
    :param bool mixed: Set whether or not the input only partially contains content to be decimated. Default is false. If enabled video output stream will be in variable frame rate.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#decimate

    """
    filter_node = FilterNode(
        name="decimate",
        streams=[
            *streams,
        ],
        kwargs={
            "cycle": cycle,
            "dupthresh": dupthresh,
            "scthresh": scthresh,
            "blockx": blockx,
            "blocky": blocky,
            "ppsrc": ppsrc,
            "chroma": chroma,
            "mixed": mixed,
        }
        | kwargs,
    )
    return filter_node.video(0)


def deconvolve(
    _main: "VideoStream",
    _impulse: "VideoStream",
    *,
    planes: int = None,
    impulse: int = None,
    noise: float = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.60 deconvolve
    Apply 2D deconvolution of video stream in frequency domain using second stream
    as impulse.

    The filter accepts the following options:


    The deconvolve filter also supports the framesync options.

    Parameters:
    ----------

    :param int planes: Set which planes to process.
    :param int impulse: Set which impulse video frames will be processed, can be first or all. Default is all.
    :param float noise: Set noise when doing divisions. Default is 0.0000001. Useful when width and height are not same and not power of 2 or if stream prior to convolving had noise.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#deconvolve

    """
    filter_node = FilterNode(
        name="deconvolve",
        streams=[
            _main,
            _impulse,
        ],
        kwargs={
            "planes": planes,
            "impulse": impulse,
            "noise": noise,
        }
        | kwargs,
    )
    return filter_node.video(0)


def displace(
    _source: "VideoStream", _xmap: "VideoStream", _ymap: "VideoStream", *, edge: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.71 displace
    Displace pixels as indicated by second and third input stream.

    It takes three input streams and outputs one stream, the first input is the
    source, and second and third input are displacement maps.

    The second input specifies how much to displace pixels along the
    x-axis, while the third input specifies how much to displace pixels
    along the y-axis.
    If one of displacement map streams terminates, last frame from that
    displacement map will be used.

    Note that once generated, displacements maps can be reused over and over again.

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int edge: Set displace behavior for pixels that are out of range. Available values are: ‘blank’ Missing pixels are replaced by black pixels. ‘smear’ Adjacent pixels will spread out to replace missing pixels. ‘wrap’ Out of range pixels are wrapped so they point to pixels of other side. ‘mirror’ Out of range pixels will be replaced with mirrored pixels. Default is ‘smear’.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#displace

    """
    filter_node = FilterNode(
        name="displace",
        streams=[
            _source,
            _xmap,
            _ymap,
        ],
        kwargs={
            "edge": edge,
        }
        | kwargs,
    )
    return filter_node.video(0)


def feedback(
    _default: "VideoStream",
    _feedin: "VideoStream",
    *,
    x: int = None,
    y: int = None,
    w: int = None,
    h: int = None,
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    11.89 feedback
    Apply feedback video filter.

    This filter pass cropped input frames to 2nd output.
    From there it can be filtered with other video filters.
    After filter receives frame from 2nd input, that frame
    is combined on top of original frame from 1st input and passed
    to 1st output.

    The typical usage is filter only part of frame.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int x: Set the top left crop position.
    :param int y: Set the top left crop position.
    :param int w: Set the crop size.
    :param int h: Set the crop size.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#feedback

    """
    filter_node = FilterNode(
        name="feedback",
        streams=[
            _default,
            _feedin,
        ],
        kwargs={
            "x": x,
            "y": y,
            "w": w,
            "h": h,
        }
        | kwargs,
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def fieldmatch(
    *streams: "VideoStream",
    order: int = None,
    mode: int = None,
    ppsrc: bool = None,
    field: int = None,
    mchroma: bool = None,
    y0: int = None,
    y1: int = None,
    scthresh: float = None,
    combmatch: int = None,
    combdbg: int = None,
    cthresh: int = None,
    chroma: bool = None,
    blockx: int = None,
    blocky: int = None,
    combpel: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.94 fieldmatch
    Field matching filter for inverse telecine. It is meant to reconstruct the
    progressive frames from a telecined stream. The filter does not drop duplicated
    frames, so to achieve a complete inverse telecine fieldmatch needs to be
    followed by a decimation filter such as decimate in the filtergraph.

    The separation of the field matching and the decimation is notably motivated by
    the possibility of inserting a de-interlacing filter fallback between the two.
    If the source has mixed telecined and real interlaced content,
    fieldmatch will not be able to match fields for the interlaced parts.
    But these remaining combed frames will be marked as interlaced, and thus can be
    de-interlaced by a later filter such as yadif before decimation.

    In addition to the various configuration options, fieldmatch can take an
    optional second stream, activated through the ppsrc option. If
    enabled, the frames reconstruction will be based on the fields and frames from
    this second stream. This allows the first input to be pre-processed in order to
    help the various algorithms of the filter, while keeping the output lossless
    (assuming the fields are matched properly). Typically, a field-aware denoiser,
    or brightness/contrast adjustments can help.

    Note that this filter uses the same algorithms as TIVTC/TFM (AviSynth project)
    and VIVTC/VFM (VapourSynth project). The later is a light clone of TFM from
    which fieldmatch is based on. While the semantic and usage are very
    close, some behaviour and options names can differ.

    The decimate filter currently only works for constant frame rate input.
    If your input has mixed telecined (30fps) and progressive content with a lower
    framerate like 24fps use the following filterchain to produce the necessary cfr
    stream: dejudder,fps=30000/1001,fieldmatch,decimate.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int order: Specify the assumed field order of the input stream. Available values are: ‘auto’ Auto detect parity (use FFmpeg’s internal parity value). ‘bff’ Assume bottom field first. ‘tff’ Assume top field first. Note that it is sometimes recommended not to trust the parity announced by the stream. Default value is auto.
    :param int mode: Set the matching mode or strategy to use. pc mode is the safest in the sense that it won’t risk creating jerkiness due to duplicate frames when possible, but if there are bad edits or blended fields it will end up outputting combed frames when a good match might actually exist. On the other hand, pcn_ub mode is the most risky in terms of creating jerkiness, but will almost always find a good frame if there is one. The other values are all somewhere in between pc and pcn_ub in terms of risking jerkiness and creating duplicate frames versus finding good matches in sections with bad edits, orphaned fields, blended fields, etc. More details about p/c/n/u/b are available in p/c/n/u/b meaning section. Available values are: ‘pc’ 2-way matching (p/c) ‘pc_n’ 2-way matching, and trying 3rd match if still combed (p/c + n) ‘pc_u’ 2-way matching, and trying 3rd match (same order) if still combed (p/c + u) ‘pc_n_ub’ 2-way matching, trying 3rd match if still combed, and trying 4th/5th matches if still combed (p/c + n + u/b) ‘pcn’ 3-way matching (p/c/n) ‘pcn_ub’ 3-way matching, and trying 4th/5th matches if all 3 of the original matches are detected as combed (p/c/n + u/b) The parenthesis at the end indicate the matches that would be used for that mode assuming order=tff (and field on auto or top). In terms of speed pc mode is by far the fastest and pcn_ub is the slowest. Default value is pc_n.
    :param bool ppsrc: Mark the main input stream as a pre-processed input, and enable the secondary input stream as the clean source to pick the fields from. See the filter introduction for more details. It is similar to the clip2 feature from VFM/TFM. Default value is 0 (disabled).
    :param int field: Set the field to match from. It is recommended to set this to the same value as order unless you experience matching failures with that setting. In certain circumstances changing the field that is used to match from can have a large impact on matching performance. Available values are: ‘auto’ Automatic (same value as order). ‘bottom’ Match from the bottom field. ‘top’ Match from the top field. Default value is auto.
    :param bool mchroma: Set whether or not chroma is included during the match comparisons. In most cases it is recommended to leave this enabled. You should set this to 0 only if your clip has bad chroma problems such as heavy rainbowing or other artifacts. Setting this to 0 could also be used to speed things up at the cost of some accuracy. Default value is 1.
    :param int y0: These define an exclusion band which excludes the lines between y0 and y1 from being included in the field matching decision. An exclusion band can be used to ignore subtitles, a logo, or other things that may interfere with the matching. y0 sets the starting scan line and y1 sets the ending line; all lines in between y0 and y1 (including y0 and y1) will be ignored. Setting y0 and y1 to the same value will disable the feature. y0 and y1 defaults to 0.
    :param int y1: These define an exclusion band which excludes the lines between y0 and y1 from being included in the field matching decision. An exclusion band can be used to ignore subtitles, a logo, or other things that may interfere with the matching. y0 sets the starting scan line and y1 sets the ending line; all lines in between y0 and y1 (including y0 and y1) will be ignored. Setting y0 and y1 to the same value will disable the feature. y0 and y1 defaults to 0.
    :param float scthresh: Set the scene change detection threshold as a percentage of maximum change on the luma plane. Good values are in the [8.0, 14.0] range. Scene change detection is only relevant in case combmatch=sc. The range for scthresh is [0.0, 100.0]. Default value is 12.0.
    :param int combmatch: When combatch is not none, fieldmatch will take into account the combed scores of matches when deciding what match to use as the final match. Available values are: ‘none’ No final matching based on combed scores. ‘sc’ Combed scores are only used when a scene change is detected. ‘full’ Use combed scores all the time. Default is sc.
    :param int combdbg: Force fieldmatch to calculate the combed metrics for certain matches and print them. This setting is known as micout in TFM/VFM vocabulary. Available values are: ‘none’ No forced calculation. ‘pcn’ Force p/c/n calculations. ‘pcnub’ Force p/c/n/u/b calculations. Default value is none.
    :param int cthresh: This is the area combing threshold used for combed frame detection. This essentially controls how "strong" or "visible" combing must be to be detected. Larger values mean combing must be more visible and smaller values mean combing can be less visible or strong and still be detected. Valid settings are from -1 (every pixel will be detected as combed) to 255 (no pixel will be detected as combed). This is basically a pixel difference value. A good range is [8, 12]. Default value is 9.
    :param bool chroma: Sets whether or not chroma is considered in the combed frame decision. Only disable this if your source has chroma problems (rainbowing, etc.) that are causing problems for the combed frame detection with chroma enabled. Actually, using chroma=0 is usually more reliable, except for the case where there is chroma only combing in the source. Default value is 0.
    :param int blockx: Respectively set the x-axis and y-axis size of the window used during combed frame detection. This has to do with the size of the area in which combpel pixels are required to be detected as combed for a frame to be declared combed. See the combpel parameter description for more info. Possible values are any number that is a power of 2 starting at 4 and going up to 512. Default value is 16.
    :param int blocky: Respectively set the x-axis and y-axis size of the window used during combed frame detection. This has to do with the size of the area in which combpel pixels are required to be detected as combed for a frame to be declared combed. See the combpel parameter description for more info. Possible values are any number that is a power of 2 starting at 4 and going up to 512. Default value is 16.
    :param int combpel: The number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed. While cthresh controls how "visible" the combing must be, this setting controls "how much" combing there must be in any localized area (a window defined by the blockx and blocky settings) on the frame. Minimum value is 0 and maximum is blocky x blockx (at which point no frames will ever be detected as combed). This setting is known as MI in TFM/VFM vocabulary. Default value is 80.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldmatch

    """
    filter_node = FilterNode(
        name="fieldmatch",
        streams=[
            *streams,
        ],
        kwargs={
            "order": order,
            "mode": mode,
            "ppsrc": ppsrc,
            "field": field,
            "mchroma": mchroma,
            "y0": y0,
            "y1": y1,
            "scthresh": scthresh,
            "combmatch": combmatch,
            "combdbg": combdbg,
            "cthresh": cthresh,
            "chroma": chroma,
            "blockx": blockx,
            "blocky": blocky,
            "combpel": combpel,
        }
        | kwargs,
    )
    return filter_node.video(0)


def framepack(_left: "VideoStream", _right: "VideoStream", *, format: int = None, **kwargs: Any) -> "VideoStream":
    """

    11.102 framepack
    Pack two different video streams into a stereoscopic video, setting proper
    metadata on supported codecs. The two views should have the same size and
    framerate and processing will stop when the shorter video ends. Please note
    that you may conveniently adjust view properties with the scale and
    fps filters.

    It accepts the following parameters:

    Some examples:


    # Convert left and right views into a frame-sequential video
    ffmpeg -i LEFT -i RIGHT -filter_complex framepack=frameseq OUTPUT

    # Convert views into a side-by-side video with the same output resolution as the input
    ffmpeg -i LEFT -i RIGHT -filter_complex [0:v]scale=w=iw/2[left],[1:v]scale=w=iw/2[right],[left][right]framepack=sbs OUTPUT

    Parameters:
    ----------

    :param int format: The desired packing format. Supported values are: sbs The views are next to each other (default). tab The views are on top of each other. lines The views are packed by line. columns The views are packed by column. frameseq The views are temporally interleaved.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#framepack

    """
    filter_node = FilterNode(
        name="framepack",
        streams=[
            _left,
            _right,
        ],
        kwargs={
            "format": format,
        }
        | kwargs,
    )
    return filter_node.video(0)


def freezeframes(
    _source: "VideoStream",
    _replace: "VideoStream",
    *,
    first: int = None,
    last: int = None,
    replace: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.106 freezeframes
    Freeze video frames.

    This filter freezes video frames using frame from 2nd input.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int first: Set number of first frame from which to start freeze.
    :param int last: Set number of last frame from which to end freeze.
    :param int replace: Set number of frame from 2nd input which will be used instead of replaced frames.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#freezeframes

    """
    filter_node = FilterNode(
        name="freezeframes",
        streams=[
            _source,
            _replace,
        ],
        kwargs={
            "first": first,
            "last": last,
            "replace": replace,
        }
        | kwargs,
    )
    return filter_node.video(0)


def guided(
    *streams: "VideoStream",
    radius: int = None,
    eps: float = None,
    mode: int = None,
    sub: int = None,
    guidance: int = None,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.115 guided
    Apply guided filter for edge-preserving smoothing, dehazing and so on.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int radius: Set the box radius in pixels. Allowed range is 1 to 20. Default is 3.
    :param float eps: Set regularization parameter (with square). Allowed range is 0 to 1. Default is 0.01.
    :param int mode: Set filter mode. Can be basic or fast. Default is basic.
    :param int sub: Set subsampling ratio for fast mode. Range is 2 to 64. Default is 4. No subsampling occurs in basic mode.
    :param int guidance: Set guidance mode. Can be off or on. Default is off. If off, single input is required. If on, two inputs of the same resolution and pixel format are required. The second input serves as the guidance.
    :param int planes: Set planes to filter. Default is first only.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#guided

    """
    filter_node = FilterNode(
        name="guided",
        streams=[
            *streams,
        ],
        kwargs={
            "radius": radius,
            "eps": eps,
            "mode": mode,
            "sub": sub,
            "guidance": guidance,
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def haldclut(
    _main: "VideoStream", _clut: "VideoStream", *, clut: int = None, interp: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.116 haldclut
    Apply a Hald CLUT to a video stream.

    First input is the video stream to process, and second one is the Hald CLUT.
    The Hald CLUT input can be a simple picture or a complete video stream.

    The filter accepts the following options:


    haldclut also has the same interpolation options as lut3d (both
    filters share the same internals).

    This filter also supports the framesync options.

    More information about the Hald CLUT can be found on Eskil Steenberg’s website
    (Hald CLUT author) at http://www.quelsolaar.com/technology/clut.html.

    Parameters:
    ----------

    :param int clut: Set which CLUT video frames will be processed from second input stream, can be first or all. Default is all.
    :param int interp: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#haldclut

    """
    filter_node = FilterNode(
        name="haldclut",
        streams=[
            _main,
            _clut,
        ],
        kwargs={
            "clut": clut,
            "interp": interp,
        }
        | kwargs,
    )
    return filter_node.video(0)


def headphone(
    *streams: "AudioStream",
    map: str,
    gain: float = None,
    lfe: float = None,
    type: int = None,
    size: int = None,
    hrir: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.93 headphone
    Apply head-related transfer functions (HRTFs) to create virtual
    loudspeakers around the user for binaural listening via headphones.
    The HRIRs are provided via additional streams, for each channel
    one stereo input stream is needed.

    The filter accepts the following options:

    Parameters:
    ----------

    :param str map: Set mapping of input streams for convolution. The argument is a ’|’-separated list of channel names in order as they are given as additional stream inputs for filter. This also specify number of input streams. Number of input streams must be not less than number of channels in first stream plus one.
    :param float gain: Set gain applied to audio. Value is in dB. Default is 0.
    :param float lfe: Set custom gain for LFE channels. Value is in dB. Default is 0.
    :param int type: Set processing type. Can be time or freq. time is processing audio in time domain which is slow. freq is processing audio in frequency domain which is fast. Default is freq.
    :param int size: Set size of frame in number of samples which will be processed at once. Default value is 1024. Allowed range is from 1024 to 96000.
    :param int hrir: Set format of hrir stream. Default value is stereo. Alternative value is multich. If value is set to stereo, number of additional streams should be greater or equal to number of input channels in first input stream. Also each additional stream should have stereo number of channels. If value is set to multich, number of additional streams should be exactly one. Also number of input channels of additional stream should be equal or greater than twice number of channels of first input stream.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#headphone

    """
    filter_node = FilterNode(
        name="headphone",
        streams=[
            *streams,
        ],
        kwargs={
            "map": map,
            "gain": gain,
            "lfe": lfe,
            "type": type,
            "size": size,
            "hrir": hrir,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def hstack(*streams: "VideoStream", inputs: int = None, shortest: bool = None, **kwargs: Any) -> "VideoStream":
    """

    11.126 hstack
    Stack input videos horizontally.

    All streams must be of same pixel format and of same height.

    Note that this filter is faster than using overlay and pad filter
    to create same output.

    The filter accepts the following option:

    Parameters:
    ----------

    :param int inputs: Set number of input streams. Default is 2.
    :param bool shortest: If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hstack

    """
    filter_node = FilterNode(
        name="hstack",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "shortest": shortest,
        }
        | kwargs,
    )
    return filter_node.video(0)


def hysteresis(
    _base: "VideoStream", _alt: "VideoStream", *, planes: int = None, threshold: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.131 hysteresis
    Grow first stream into second stream by connecting components.
    This makes it possible to build more robust edge masks.

    This filter accepts the following options:


    The hysteresis filter also supports the framesync options.

    Parameters:
    ----------

    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
    :param int threshold: Set threshold which is used in filtering. If pixel component value is higher than this value filter algorithm for connecting components is activated. By default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#hysteresis

    """
    filter_node = FilterNode(
        name="hysteresis",
        streams=[
            _base,
            _alt,
        ],
        kwargs={
            "planes": planes,
            "threshold": threshold,
        }
        | kwargs,
    )
    return filter_node.video(0)


def identity(_main: "VideoStream", _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
    """

    11.134 identity
    Obtain the identity score between two input videos.

    This filter takes two input videos.

    Both input videos must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The obtained per component, average, min and max identity score is printed through
    the logging system.

    The filter stores the calculated identity scores of each frame in frame metadata.

    This filter also supports the framesync options.

    In the below example the input file main.mpg being processed is compared
    with the reference file ref.mpg.


    ffmpeg -i main.mpg -i ref.mpg -lavfi identity -f null -

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#identity

    """
    filter_node = FilterNode(
        name="identity",
        streams=[
            _main,
            _reference,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.video(0)


def interleave(*streams: "VideoStream", nb_inputs: int = None, duration: int = None, **kwargs: Any) -> "VideoStream":
    """

    18.11 interleave, ainterleave
    Temporally interleave frames from several inputs.

    interleave works with video inputs, ainterleave with audio.

    These filters read frames from several inputs and send the oldest
    queued frame to the output.

    Input streams must have well defined, monotonically increasing frame
    timestamp values.

    In order to submit one frame to output, these filters need to enqueue
    at least one frame for each input, so they cannot work in case one
    input is not yet terminated and will not receive incoming frames.

    For example consider the case when one input is a select filter
    which always drops input frames. The interleave filter will keep
    reading from that input, but it will never be able to send new frames
    to output until the input sends an end-of-stream signal.

    Also, depending on inputs synchronization, the filters will drop
    frames in case one input receives more frames than the other ones, and
    the queue is already filled.

    These filters accept the following options:

    Parameters:
    ----------

    :param int nb_inputs: Set the number of different inputs, it is 2 by default.
    :param int duration: How to determine the end-of-stream. longest The duration of the longest input. (default) shortest The duration of the shortest input. first The duration of the first input.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave

    """
    filter_node = FilterNode(
        name="interleave",
        streams=[
            *streams,
        ],
        kwargs={
            "nb_inputs": nb_inputs,
            "duration": duration,
        }
        | kwargs,
    )
    return filter_node.video(0)


def join(
    *streams: "AudioStream", inputs: int = None, channel_layout: str = None, map: str, **kwargs: Any
) -> "AudioStream":
    """

    8.95 join
    Join multiple input streams into one multi-channel stream.

    It accepts the following parameters:

    The filter will attempt to guess the mappings when they are not specified
    explicitly. It does so by first trying to find an unused matching input channel
    and if that fails it picks the first unused input channel.

    Join 3 inputs (with properly set channel layouts):

    ffmpeg -i INPUT1 -i INPUT2 -i INPUT3 -filter_complex join=inputs=3 OUTPUT

    Build a 5.1 output from 6 single-channel streams:

    ffmpeg -i fl -i fr -i fc -i sl -i sr -i lfe -filter_complex
    'join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-SL|4.0-SR|5.0-LFE'
    out

    Parameters:
    ----------

    :param int inputs: The number of input streams. It defaults to 2.
    :param str channel_layout: The desired output channel layout. It defaults to stereo.
    :param str map: Map channels from inputs to output. The argument is a ’|’-separated list of mappings, each in the input_idx.in_channel-out_channel form. input_idx is the 0-based index of the input stream. in_channel can be either the name of the input channel (e.g. FL for front left) or its index in the specified input stream. out_channel is the name of the output channel.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#join

    """
    filter_node = FilterNode(
        name="join",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "channel_layout": channel_layout,
            "map": map,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def ladspa(
    *streams: "AudioStream",
    file: str,
    plugin: str,
    controls: str,
    sample_rate: int = None,
    nb_samples: int = None,
    duration: int = None,
    latency: bool = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.96 ladspa
    Load a LADSPA (Linux Audio Developer’s Simple Plugin API) plugin.

    To enable compilation of this filter you need to configure FFmpeg with
    --enable-ladspa.

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
        streams=[
            *streams,
        ],
        kwargs={
            "file": file,
            "plugin": plugin,
            "controls": controls,
            "sample_rate": sample_rate,
            "nb_samples": nb_samples,
            "duration": duration,
            "latency": latency,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def libplacebo(
    *streams: "VideoStream",
    inputs: int = None,
    w: str = None,
    h: str = None,
    fps: str = None,
    crop_x: str = None,
    crop_y: str = None,
    crop_w: str = None,
    crop_h: str = None,
    pos_x: str = None,
    pos_y: str = None,
    pos_w: str = None,
    pos_h: str = None,
    format: str,
    force_original_aspect_ratio: int = None,
    force_divisible_by: int = None,
    normalize_sar: bool = None,
    pad_crop_ratio: float = None,
    fillcolor: str = None,
    corner_rounding: float = None,
    extra_opts: str,
    colorspace: int = None,
    range: int = None,
    color_primaries: int = None,
    color_trc: int = None,
    upscaler: str = None,
    downscaler: str = None,
    frame_mixer: str = None,
    lut_entries: int = None,
    antiringing: float = None,
    sigmoid: bool = None,
    apply_filmgrain: bool = None,
    apply_dolbyvision: bool = None,
    deband: bool = None,
    deband_iterations: int = None,
    deband_threshold: float = None,
    deband_radius: float = None,
    deband_grain: float = None,
    brightness: float = None,
    contrast: float = None,
    saturation: float = None,
    hue: float = None,
    gamma: float = None,
    peak_detect: bool = None,
    smoothing_period: float = None,
    minimum_peak: float = None,
    scene_threshold_low: float = None,
    scene_threshold_high: float = None,
    percentile: float = None,
    gamut_mode: int = None,
    tonemapping: int = None,
    tonemapping_param: float = None,
    inverse_tonemapping: bool = None,
    tonemapping_lut_size: int = None,
    contrast_recovery: float = None,
    contrast_smoothness: float = None,
    desaturation_strength: float = None,
    desaturation_exponent: float = None,
    gamut_warning: bool = None,
    gamut_clipping: bool = None,
    intent: int = None,
    tonemapping_mode: int = None,
    tonemapping_crosstalk: float = None,
    overshoot: float = None,
    hybrid_mix: float = None,
    dithering: int = None,
    dither_lut_size: int = None,
    dither_temporal: bool = None,
    cones: str = None,
    cone_strength: float = None,
    custom_shader_path: str,
    custom_shader_bin: str,
    skip_aa: bool = None,
    polar_cutoff: float = None,
    disable_linear: bool = None,
    disable_builtin: bool = None,
    force_icc_lut: bool = None,
    force_dither: bool = None,
    disable_fbos: bool = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.144 libplacebo
    Flexible GPU-accelerated processing filter based on libplacebo
    (https://code.videolan.org/videolan/libplacebo).

    Parameters:
    ----------

    :param int inputs: None
    :param str w: None
    :param str h: None
    :param str fps: None
    :param str crop_x: None
    :param str crop_y: None
    :param str crop_w: None
    :param str crop_h: None
    :param str pos_x: None
    :param str pos_y: None
    :param str pos_w: None
    :param str pos_h: None
    :param str format: None
    :param int force_original_aspect_ratio: None
    :param int force_divisible_by: None
    :param bool normalize_sar: None
    :param float pad_crop_ratio: None
    :param str fillcolor: None
    :param float corner_rounding: None
    :param str extra_opts: None
    :param int colorspace: None
    :param int range: None
    :param int color_primaries: None
    :param int color_trc: None
    :param str upscaler: None
    :param str downscaler: None
    :param str frame_mixer: None
    :param int lut_entries: None
    :param float antiringing: None
    :param bool sigmoid: None
    :param bool apply_filmgrain: None
    :param bool apply_dolbyvision: None
    :param bool deband: None
    :param int deband_iterations: None
    :param float deband_threshold: None
    :param float deband_radius: None
    :param float deband_grain: None
    :param float brightness: None
    :param float contrast: None
    :param float saturation: None
    :param float hue: None
    :param float gamma: None
    :param bool peak_detect: None
    :param float smoothing_period: None
    :param float minimum_peak: None
    :param float scene_threshold_low: None
    :param float scene_threshold_high: None
    :param float percentile: None
    :param int gamut_mode: None
    :param int tonemapping: None
    :param float tonemapping_param: None
    :param bool inverse_tonemapping: None
    :param int tonemapping_lut_size: None
    :param float contrast_recovery: None
    :param float contrast_smoothness: None
    :param float desaturation_strength: None
    :param float desaturation_exponent: None
    :param bool gamut_warning: None
    :param bool gamut_clipping: None
    :param int intent: None
    :param int tonemapping_mode: None
    :param float tonemapping_crosstalk: None
    :param float overshoot: None
    :param float hybrid_mix: None
    :param int dithering: None
    :param int dither_lut_size: None
    :param bool dither_temporal: None
    :param str cones: None
    :param float cone_strength: None
    :param str custom_shader_path: None
    :param str custom_shader_bin: None
    :param bool skip_aa: None
    :param float polar_cutoff: None
    :param bool disable_linear: None
    :param bool disable_builtin: None
    :param bool force_icc_lut: None
    :param bool force_dither: None
    :param bool disable_fbos: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#libplacebo

    """
    filter_node = FilterNode(
        name="libplacebo",
        streams=[
            *streams,
        ],
        kwargs={
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
        | kwargs,
    )
    return filter_node.video(0)


def libvmaf(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    log_path: str,
    log_fmt: str = None,
    pool: str,
    n_threads: int = None,
    n_subsample: int = None,
    model: str = None,
    feature: str,
    **kwargs: Any
) -> "VideoStream":
    """

    11.145 libvmaf
    Calculate the VMAF (Video Multi-Method Assessment Fusion) score for a
    reference/distorted pair of input videos.

    The first input is the distorted video, and the second input is the reference video.

    The obtained VMAF score is printed through the logging system.

    It requires Netflix’s vmaf library (libvmaf) as a pre-requisite.
    After installing the library it can be enabled using:
    ./configure --enable-libvmaf.

    The filter has following options:


    This filter also supports the framesync options.

    Parameters:
    ----------

    :param str log_path: Set the file path to be used to store log files.
    :param str log_fmt: Set the format of the log file (xml, json, csv, or sub).
    :param str pool: Set the pool method to be used for computing vmaf. Options are min, harmonic_mean or mean (default).
    :param int n_threads: Set number of threads to be used when initializing libvmaf. Default value: 0, no threads.
    :param int n_subsample: Set frame subsampling interval to be used.
    :param str model: A ‘|‘ delimited list of vmaf models. Each model can be configured with a number of parameters. Default value: "version=vmaf_v0.6.1"
    :param str feature: A ‘|‘ delimited list of features. Each feature can be configured with a number of parameters.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#libvmaf

    """
    filter_node = FilterNode(
        name="libvmaf",
        streams=[
            _main,
            _reference,
        ],
        kwargs={
            "log_path": log_path,
            "log_fmt": log_fmt,
            "pool": pool,
            "n_threads": n_threads,
            "n_subsample": n_subsample,
            "model": model,
            "feature": feature,
        }
        | kwargs,
    )
    return filter_node.video(0)


def limitdiff(
    *streams: "VideoStream",
    threshold: float = None,
    elasticity: float = None,
    reference: bool = None,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.147 limitdiff
    Apply limited difference filter using second and optionally third video stream.

    The filter accepts the following options:

    Parameters:
    ----------

    :param float threshold: Set the threshold to use when allowing certain differences between video streams. Any absolute difference value lower or exact than this threshold will pick pixel components from first video stream.
    :param float elasticity: Set the elasticity of soft thresholding when processing video streams. This value multiplied with first one sets second threshold. Any absolute difference value greater or exact than second threshold will pick pixel components from second video stream. For values between those two threshold linear interpolation between first and second video stream will be used.
    :param bool reference: Enable the reference (third) video stream processing. By default is disabled. If set, this video stream will be used for calculating absolute difference with first video stream.
    :param int planes: Specify which planes will be processed. Defaults to all available.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#limitdiff

    """
    filter_node = FilterNode(
        name="limitdiff",
        streams=[
            *streams,
        ],
        kwargs={
            "threshold": threshold,
            "elasticity": elasticity,
            "reference": reference,
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def lut2(
    _srcx: "VideoStream",
    _srcy: "VideoStream",
    *,
    c0: str = None,
    c1: str = None,
    c2: str = None,
    c3: str = None,
    d: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.154 lut2, tlut2
    The lut2 filter takes two input streams and outputs one
    stream.

    The tlut2 (time lut2) filter takes two consecutive frames
    from one single stream.

    This filter accepts the following parameters:

    The lut2 filter also supports the framesync options.

    Each of them specifies the expression to use for computing the lookup table for
    the corresponding pixel component values.

    The exact component associated to each of the c* options depends on the
    format in inputs.

    The expressions can contain the following constants:


    All expressions default to "x".

    Parameters:
    ----------

    :param str c0: set first pixel component expression
    :param str c1: set second pixel component expression
    :param str c2: set third pixel component expression
    :param str c3: set fourth pixel component expression, corresponds to the alpha component
    :param int d: set output bit depth, only available for lut2 filter. By default is 0, which means bit depth is automatically picked from first input format.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

    """
    filter_node = FilterNode(
        name="lut2",
        streams=[
            _srcx,
            _srcy,
        ],
        kwargs={
            "c0": c0,
            "c1": c1,
            "c2": c2,
            "c3": c3,
            "d": d,
        }
        | kwargs,
    )
    return filter_node.video(0)


def lv2(
    *streams: "AudioStream",
    plugin: str,
    controls: str,
    sample_rate: int = None,
    nb_samples: int = None,
    duration: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.99 lv2
    Load a LV2 (LADSPA Version 2) plugin.

    To enable compilation of this filter you need to configure FFmpeg with
    --enable-lv2.

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
        streams=[
            *streams,
        ],
        kwargs={
            "plugin": plugin,
            "controls": controls,
            "sample_rate": sample_rate,
            "nb_samples": nb_samples,
            "duration": duration,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def maskedclamp(
    _base: "VideoStream",
    _dark: "VideoStream",
    _bright: "VideoStream",
    *,
    undershoot: int = None,
    overshoot: int = None,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.155 maskedclamp
    Clamp the first input stream with the second input and third input stream.

    Returns the value of first stream to be between second input
    stream - undershoot and third input stream + overshoot.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int undershoot: Default value is 0.
    :param int overshoot: Default value is 0.
    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedclamp

    """
    filter_node = FilterNode(
        name="maskedclamp",
        streams=[
            _base,
            _dark,
            _bright,
        ],
        kwargs={
            "undershoot": undershoot,
            "overshoot": overshoot,
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def maskedmax(
    _source: "VideoStream", _filter1: "VideoStream", _filter2: "VideoStream", *, planes: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.156 maskedmax
    Merge the second and third input stream into output stream using absolute differences
    between second input stream and first input stream and absolute difference between
    third input stream and first input stream. The picked value will be from second input
    stream if second absolute difference is greater than first one or from third input stream
    otherwise.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmax

    """
    filter_node = FilterNode(
        name="maskedmax",
        streams=[
            _source,
            _filter1,
            _filter2,
        ],
        kwargs={
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def maskedmerge(
    _base: "VideoStream", _overlay: "VideoStream", _mask: "VideoStream", *, planes: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.157 maskedmerge
    Merge the first input stream with the second input stream using per pixel
    weights in the third input stream.

    A value of 0 in the third stream pixel component means that pixel component
    from first stream is returned unchanged, while maximum value (eg. 255 for
    8-bit videos) means that pixel component from second stream is returned
    unchanged. Intermediate values define the amount of merging between both
    input stream’s pixel components.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmerge

    """
    filter_node = FilterNode(
        name="maskedmerge",
        streams=[
            _base,
            _overlay,
            _mask,
        ],
        kwargs={
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def maskedmin(
    _source: "VideoStream", _filter1: "VideoStream", _filter2: "VideoStream", *, planes: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.158 maskedmin
    Merge the second and third input stream into output stream using absolute differences
    between second input stream and first input stream and absolute difference between
    third input stream and first input stream. The picked value will be from second input
    stream if second absolute difference is less than first one or from third input stream
    otherwise.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmin

    """
    filter_node = FilterNode(
        name="maskedmin",
        streams=[
            _source,
            _filter1,
            _filter2,
        ],
        kwargs={
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def maskedthreshold(
    _source: "VideoStream",
    _reference: "VideoStream",
    *,
    threshold: int = None,
    planes: int = None,
    mode: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.159 maskedthreshold
    Pick pixels comparing absolute difference of two video streams with fixed
    threshold.

    If absolute difference between pixel component of first and second video
    stream is equal or lower than user supplied threshold than pixel component
    from first video stream is picked, otherwise pixel component from second
    video stream is picked.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int threshold: Set threshold used when picking pixels from absolute difference from two input video streams.
    :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from second stream. By default value 0xf, all planes will be processed.
    :param int mode: Set mode of filter operation. Can be abs or diff. Default is abs.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedthreshold

    """
    filter_node = FilterNode(
        name="maskedthreshold",
        streams=[
            _source,
            _reference,
        ],
        kwargs={
            "threshold": threshold,
            "planes": planes,
            "mode": mode,
        }
        | kwargs,
    )
    return filter_node.video(0)


def mergeplanes(
    *streams: "VideoStream",
    mapping: int = None,
    format: str = None,
    map0s: int = None,
    map0p: int = None,
    map1s: int = None,
    map1p: int = None,
    map2s: int = None,
    map2p: int = None,
    map3s: int = None,
    map3p: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.163 mergeplanes
    Merge color channel components from several video streams.

    The filter accepts up to 4 input streams, and merge selected input
    planes to the output video.

    This filter accepts the following options:

    Parameters:
    ----------

    :param int mapping: Set input to output plane mapping. Default is 0. The mappings is specified as a bitmap. It should be specified as a hexadecimal number in the form 0xAa[Bb[Cc[Dd]]]. ’Aa’ describes the mapping for the first plane of the output stream. ’A’ sets the number of the input stream to use (from 0 to 3), and ’a’ the plane number of the corresponding input to use (from 0 to 3). The rest of the mappings is similar, ’Bb’ describes the mapping for the output stream second plane, ’Cc’ describes the mapping for the output stream third plane and ’Dd’ describes the mapping for the output stream fourth plane.
    :param str format: Set output pixel format. Default is yuva444p.
    :param int map0s: Set input to output stream mapping for output Nth plane. Default is 0.
    :param int map0p: Set input to output plane mapping for output Nth plane. Default is 0.
    :param int map1s: Set input to output stream mapping for output Nth plane. Default is 0.
    :param int map1p: Set input to output plane mapping for output Nth plane. Default is 0.
    :param int map2s: Set input to output stream mapping for output Nth plane. Default is 0.
    :param int map2p: Set input to output plane mapping for output Nth plane. Default is 0.
    :param int map3s: Set input to output stream mapping for output Nth plane. Default is 0.
    :param int map3p: Set input to output plane mapping for output Nth plane. Default is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#mergeplanes

    """
    filter_node = FilterNode(
        name="mergeplanes",
        streams=[
            *streams,
        ],
        kwargs={
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
        | kwargs,
    )
    return filter_node.video(0)


def midequalizer(_in0: "VideoStream", _in1: "VideoStream", *, planes: int = None, **kwargs: Any) -> "VideoStream":
    """

    11.165 midequalizer
    Apply Midway Image Equalization effect using two video streams.

    Midway Image Equalization adjusts a pair of images to have the same
    histogram, while maintaining their dynamics as much as possible. It’s
    useful for e.g. matching exposures from a pair of stereo cameras.

    This filter has two inputs and one output, which must be of same pixel format, but
    may be of different sizes. The output of filter is first input adjusted with
    midway histogram of both inputs.

    This filter accepts the following option:

    Parameters:
    ----------

    :param int planes: Set which planes to process. Default is 15, which is all available planes.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#midequalizer

    """
    filter_node = FilterNode(
        name="midequalizer",
        streams=[
            _in0,
            _in1,
        ],
        kwargs={
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def mix(
    *streams: "VideoStream",
    inputs: int = None,
    weights: str = None,
    scale: float = None,
    planes: str = None,
    duration: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.167 mix
    Mix several video input streams into one video stream.

    A description of the accepted options follows.

    Parameters:
    ----------

    :param int inputs: The number of inputs. If unspecified, it defaults to 2.
    :param str weights: Specify weight of each input video stream as sequence. Each weight is separated by space. If number of weights is smaller than number of frames last specified weight will be used for all remaining unset weights.
    :param float scale: Specify scale, if it is set it will be multiplied with sum of each weight multiplied with pixel values to give final destination pixel value. By default scale is auto scaled to sum of weights.
    :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.
    :param int duration: Specify how end of stream is determined. ‘longest’ The duration of the longest input. (default) ‘shortest’ The duration of the shortest input. ‘first’ The duration of the first input.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#mix

    """
    filter_node = FilterNode(
        name="mix",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "weights": weights,
            "scale": scale,
            "planes": planes,
            "duration": duration,
        }
        | kwargs,
    )
    return filter_node.video(0)


def morpho(
    _default: "VideoStream",
    _structure: "VideoStream",
    *,
    mode: int = None,
    planes: int = None,
    structure: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.169 morpho
    This filter allows to apply main morphological grayscale transforms,
    erode and dilate with arbitrary structures set in second input stream.

    Unlike naive implementation and much slower performance in erosion
    and dilation filters, when speed is critical morpho filter
    should be used instead.

    A description of accepted options follows,


    The morpho filter also supports the framesync options.

    Parameters:
    ----------

    :param int mode: Set morphological transform to apply, can be: ‘erode’ ‘dilate’ ‘open’ ‘close’ ‘gradient’ ‘tophat’ ‘blackhat’ Default is erode.
    :param int planes: Set planes to filter, by default all planes except alpha are filtered.
    :param int structure: Set which structure video frames will be processed from second input stream, can be first or all. Default is all.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#morpho

    """
    filter_node = FilterNode(
        name="morpho",
        streams=[
            _default,
            _structure,
        ],
        kwargs={
            "mode": mode,
            "planes": planes,
            "structure": structure,
        }
        | kwargs,
    )
    return filter_node.video(0)


def msad(_main: "VideoStream", _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
    """

    11.171 msad
    Obtain the MSAD (Mean Sum of Absolute Differences) between two input videos.

    This filter takes two input videos.

    Both input videos must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The obtained per component, average, min and max MSAD is printed through
    the logging system.

    The filter stores the calculated MSAD of each frame in frame metadata.

    This filter also supports the framesync options.

    In the below example the input file main.mpg being processed is compared
    with the reference file ref.mpg.


    ffmpeg -i main.mpg -i ref.mpg -lavfi msad -f null -

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#msad

    """
    filter_node = FilterNode(
        name="msad",
        streams=[
            _main,
            _reference,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.video(0)


def multiply(
    _source: "VideoStream",
    _factor: "VideoStream",
    *,
    scale: float = None,
    offset: float = None,
    planes: str = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.172 multiply
    Multiply first video stream pixels values with second video stream pixels values.

    The filter accepts the following options:

    Parameters:
    ----------

    :param float scale: Set the scale applied to second video stream. By default is 1. Allowed range is from 0 to 9.
    :param float offset: Set the offset applied to second video stream. By default is 0.5. Allowed range is from -1 to 1.
    :param str planes: Specify planes from input video stream that will be processed. By default all planes are processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#multiply

    """
    filter_node = FilterNode(
        name="multiply",
        streams=[
            _source,
            _factor,
        ],
        kwargs={
            "scale": scale,
            "offset": offset,
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def overlay(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str = None,
    y: str = None,
    eof_action: int = None,
    eval: int = None,
    shortest: bool = None,
    format: int = None,
    repeatlast: bool = None,
    alpha: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.183 overlay
    Overlay one video on top of another.

    It takes two inputs and has one output. The first input is the "main"
    video on which the second input is overlaid.

    It accepts the following parameters:

    A description of the accepted options follows.


    The x, and y expressions can contain the following
    parameters.


    This filter also supports the framesync options.

    Note that the n, t variables are available only
    when evaluation is done per frame, and will evaluate to NAN
    when eval is set to ‘init’.

    Be aware that frames are taken from each input video in timestamp
    order, hence, if their initial timestamps differ, it is a good idea
    to pass the two inputs through a setpts=PTS-STARTPTS filter to
    have them begin in the same zero timestamp, as the example for
    the movie filter does.

    You can chain together more overlays but you should test the
    efficiency of such approach.

    Parameters:
    ----------

    :param str x: Set the expression for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions. In case the expression is invalid, it is set to a huge value (meaning that the overlay will not be displayed within the output visible area).
    :param str y: Set the expression for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions. In case the expression is invalid, it is set to a huge value (meaning that the overlay will not be displayed within the output visible area).
    :param int eof_action: See framesync.
    :param int eval: Set when the expressions for x, and y are evaluated. It accepts the following values: ‘init’ only evaluate expressions once during the filter initialization or when a command is processed ‘frame’ evaluate expressions for each incoming frame Default value is ‘frame’.
    :param bool shortest: See framesync.
    :param int format: Set the format for the output video. It accepts the following values: ‘yuv420’ force YUV 4:2:0 8-bit planar output ‘yuv420p10’ force YUV 4:2:0 10-bit planar output ‘yuv422’ force YUV 4:2:2 8-bit planar output ‘yuv422p10’ force YUV 4:2:2 10-bit planar output ‘yuv444’ force YUV 4:4:4 8-bit planar output ‘yuv444p10’ force YUV 4:4:4 10-bit planar output ‘rgb’ force RGB 8-bit packed output ‘gbrp’ force RGB 8-bit planar output ‘auto’ automatically pick format Default value is ‘yuv420’.
    :param bool repeatlast: See framesync.
    :param int alpha: Set format of alpha of the overlaid video, it can be straight or premultiplied. Default is straight.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay

    """
    filter_node = FilterNode(
        name="overlay",
        streams=[
            _main,
            _overlay,
        ],
        kwargs={
            "x": x,
            "y": y,
            "eof_action": eof_action,
            "eval": eval,
            "shortest": shortest,
            "format": format,
            "repeatlast": repeatlast,
            "alpha": alpha,
        }
        | kwargs,
    )
    return filter_node.video(0)


def overlay_cuda(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str = None,
    y: str = None,
    eof_action: int = None,
    eval: int = None,
    shortest: bool = None,
    repeatlast: bool = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.184 overlay_cuda
    Overlay one video on top of another.

    This is the CUDA variant of the overlay filter.
    It only accepts CUDA frames. The underlying input pixel formats have to match.

    It takes two inputs and has one output. The first input is the "main"
    video on which the second input is overlaid.

    It accepts the following parameters:


    This filter also supports the framesync options.

    Parameters:
    ----------

    :param str x: Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
    :param str y: Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
    :param int eof_action: See framesync.
    :param int eval: Set when the expressions for x and y are evaluated. It accepts the following values: init Evaluate expressions once during filter initialization or when a command is processed. frame Evaluate expressions for each incoming frame Default value is frame.
    :param bool shortest: See framesync.
    :param bool repeatlast: See framesync.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fcuda

    """
    filter_node = FilterNode(
        name="overlay_cuda",
        streams=[
            _main,
            _overlay,
        ],
        kwargs={
            "x": x,
            "y": y,
            "eof_action": eof_action,
            "eval": eval,
            "shortest": shortest,
            "repeatlast": repeatlast,
        }
        | kwargs,
    )
    return filter_node.video(0)


def overlay_opencl(
    _main: "VideoStream", _overlay: "VideoStream", *, x: int = None, y: int = None, **kwargs: Any
) -> "VideoStream":
    """

    12.9 overlay_opencl
    Overlay one video on top of another.

    It takes two inputs and has one output. The first input is the "main" video on which the second input is overlaid.
    This filter requires same memory layout for all the inputs. So, format conversion may be needed.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int x: Set the x coordinate of the overlaid video on the main video. Default value is 0.
    :param int y: Set the y coordinate of the overlaid video on the main video. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fopencl

    """
    filter_node = FilterNode(
        name="overlay_opencl",
        streams=[
            _main,
            _overlay,
        ],
        kwargs={
            "x": x,
            "y": y,
        }
        | kwargs,
    )
    return filter_node.video(0)


def overlay_vaapi(
    _main: "VideoStream",
    _overlay: "VideoStream",
    *,
    x: str = None,
    y: str = None,
    w: str = None,
    h: str = None,
    alpha: float = None,
    eof_action: int = None,
    shortest: bool = None,
    repeatlast: bool = None,
    **kwargs: Any
) -> "VideoStream":
    """

    13.1 overlay_vaapi
    Overlay one video on the top of another.

    It takes two inputs and has one output. The first input is the "main" video on which the second input is overlaid.

    The filter accepts the following options:


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

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvaapi

    """
    filter_node = FilterNode(
        name="overlay_vaapi",
        streams=[
            _main,
            _overlay,
        ],
        kwargs={
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "alpha": alpha,
            "eof_action": eof_action,
            "shortest": shortest,
            "repeatlast": repeatlast,
        }
        | kwargs,
    )
    return filter_node.video(0)


def overlay_vulkan(
    _main: "VideoStream", _overlay: "VideoStream", *, x: int = None, y: int = None, **kwargs: Any
) -> "VideoStream":
    """

    14.11 overlay_vulkan
    Overlay one video on top of another.

    It takes two inputs and has one output. The first input is the "main" video on which the second input is overlaid.
    This filter requires all inputs to use the same pixel format. So, format conversion may be needed.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int x: Set the x coordinate of the overlaid video on the main video. Default value is 0.
    :param int y: Set the y coordinate of the overlaid video on the main video. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvulkan

    """
    filter_node = FilterNode(
        name="overlay_vulkan",
        streams=[
            _main,
            _overlay,
        ],
        kwargs={
            "x": x,
            "y": y,
        }
        | kwargs,
    )
    return filter_node.video(0)


def paletteuse(
    _default: "VideoStream",
    _palette: "VideoStream",
    *,
    dither: int = None,
    bayer_scale: int = None,
    diff_mode: int = None,
    new: bool = None,
    alpha_threshold: int = None,
    debug_kdtree: str,
    **kwargs: Any
) -> "VideoStream":
    """

    11.188 paletteuse
    Use a palette to downsample an input video stream.

    The filter takes two inputs: one video stream and a palette. The palette must
    be a 256 pixels image.

    It accepts the following options:

    Parameters:
    ----------

    :param int dither: Select dithering mode. Available algorithms are: ‘bayer’ Ordered 8x8 bayer dithering (deterministic) ‘heckbert’ Dithering as defined by Paul Heckbert in 1982 (simple error diffusion). Note: this dithering is sometimes considered "wrong" and is included as a reference. ‘floyd_steinberg’ Floyd and Steingberg dithering (error diffusion) ‘sierra2’ Frankie Sierra dithering v2 (error diffusion) ‘sierra2_4a’ Frankie Sierra dithering v2 "Lite" (error diffusion) ‘sierra3’ Frankie Sierra dithering v3 (error diffusion) ‘burkes’ Burkes dithering (error diffusion) ‘atkinson’ Atkinson dithering by Bill Atkinson at Apple Computer (error diffusion) ‘none’ Disable dithering. Default is sierra2_4a.
    :param int bayer_scale: When bayer dithering is selected, this option defines the scale of the pattern (how much the crosshatch pattern is visible). A low value means more visible pattern for less banding, and higher value means less visible pattern at the cost of more banding. The option must be an integer value in the range [0,5]. Default is 2.
    :param int diff_mode: If set, define the zone to process ‘rectangle’ Only the changing rectangle will be reprocessed. This is similar to GIF cropping/offsetting compression mechanism. This option can be useful for speed if only a part of the image is changing, and has use cases such as limiting the scope of the error diffusal dither to the rectangle that bounds the moving scene (it leads to more deterministic output if the scene doesn’t change much, and as a result less moving noise and better GIF compression). Default is none.
    :param bool new: Take new palette for each output frame.
    :param int alpha_threshold: Sets the alpha threshold for transparency. Alpha values above this threshold will be treated as completely opaque, and values below this threshold will be treated as completely transparent. The option must be an integer value in the range [0,255]. Default is 128.
    :param str debug_kdtree: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#paletteuse

    """
    filter_node = FilterNode(
        name="paletteuse",
        streams=[
            _default,
            _palette,
        ],
        kwargs={
            "dither": dither,
            "bayer_scale": bayer_scale,
            "diff_mode": diff_mode,
            "new": new,
            "alpha_threshold": alpha_threshold,
            "debug_kdtree": debug_kdtree,
        }
        | kwargs,
    )
    return filter_node.video(0)


def premultiply(*streams: "VideoStream", planes: int = None, inplace: bool = None, **kwargs: Any) -> "VideoStream":
    """

    11.197 premultiply
    Apply alpha premultiply effect to input video stream using first plane
    of second stream as alpha.

    Both streams must have same dimensions and same pixel format.

    The filter accepts the following option:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
    :param bool inplace: Do not require 2nd input for processing, instead use alpha plane from input stream.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#premultiply

    """
    filter_node = FilterNode(
        name="premultiply",
        streams=[
            *streams,
        ],
        kwargs={
            "planes": planes,
            "inplace": inplace,
        }
        | kwargs,
    )
    return filter_node.video(0)


def psnr(
    _main: "VideoStream",
    _reference: "VideoStream",
    *,
    stats_file: str,
    stats_version: int = None,
    output_max: bool = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.200 psnr
    Obtain the average, maximum and minimum PSNR (Peak Signal to Noise
    Ratio) between two input videos.

    This filter takes in input two input videos, the first input is
    considered the "main" source and is passed unchanged to the
    output. The second input is used as a "reference" video for computing
    the PSNR.

    Both video inputs must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The obtained average PSNR is printed through the logging system.

    The filter stores the accumulated MSE (mean squared error) of each
    frame, and at the end of the processing it is averaged across all frames
    equally, and the following formula is applied to obtain the PSNR:


    PSNR = 10*log10(MAX^2/MSE)

    Where MAX is the average of the maximum values of each component of the
    image.

    The description of the accepted parameters follows.


    This filter also supports the framesync options.

    The file printed if stats_file is selected, contains a sequence of
    key/value pairs of the form key:value for each compared
    couple of frames.

    If a stats_version greater than 1 is specified, a header line precedes
    the list of per-frame-pair stats, with key value pairs following the frame
    format with the following parameters:


    A description of each shown per-frame-pair parameter follows:

    Parameters:
    ----------

    :param str stats_file: If specified the filter will use the named file to save the PSNR of each individual frame. When filename equals "-" the data is sent to standard output.
    :param int stats_version: Specifies which version of the stats file format to use. Details of each format are written below. Default value is 1.
    :param bool output_max: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#psnr

    """
    filter_node = FilterNode(
        name="psnr",
        streams=[
            _main,
            _reference,
        ],
        kwargs={
            "stats_file": stats_file,
            "stats_version": stats_version,
            "output_max": output_max,
        }
        | kwargs,
    )
    return filter_node.video(0)


def remap(
    _source: "VideoStream",
    _xmap: "VideoStream",
    _ymap: "VideoStream",
    *,
    format: int = None,
    fill: str = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.206 remap
    Remap pixels using 2nd: Xmap and 3rd: Ymap input video stream.

    Destination pixel at position (X, Y) will be picked from source (x, y) position
    where x = Xmap(X, Y) and y = Ymap(X, Y). If mapping values are out of range, zero
    value for pixel will be used for destination pixel.

    Xmap and Ymap input video streams must be of same dimensions. Output video stream
    will have Xmap/Ymap video stream dimensions.
    Xmap and Ymap input video streams are 16bit depth, single channel.

    Parameters:
    ----------

    :param int format: Specify pixel format of output from this filter. Can be color or gray. Default is color.
    :param str fill: Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#remap

    """
    filter_node = FilterNode(
        name="remap",
        streams=[
            _source,
            _xmap,
            _ymap,
        ],
        kwargs={
            "format": format,
            "fill": fill,
        }
        | kwargs,
    )
    return filter_node.video(0)


def remap_opencl(
    _source: "VideoStream",
    _xmap: "VideoStream",
    _ymap: "VideoStream",
    *,
    interp: int = None,
    fill: str = None,
    **kwargs: Any
) -> "VideoStream":
    """

    12.13 remap_opencl
    Remap pixels using 2nd: Xmap and 3rd: Ymap input video stream.

    Destination pixel at position (X, Y) will be picked from source (x, y) position
    where x = Xmap(X, Y) and y = Ymap(X, Y). If mapping values are out of range, zero
    value for pixel will be used for destination pixel.

    Xmap and Ymap input video streams must be of same dimensions. Output video stream
    will have Xmap/Ymap video stream dimensions.
    Xmap and Ymap input video streams are 32bit float pixel format, single channel.

    Parameters:
    ----------

    :param int interp: Specify interpolation used for remapping of pixels. Allowed values are near and linear. Default value is linear.
    :param str fill: Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#remap_005fopencl

    """
    filter_node = FilterNode(
        name="remap_opencl",
        streams=[
            _source,
            _xmap,
            _ymap,
        ],
        kwargs={
            "interp": interp,
            "fill": fill,
        }
        | kwargs,
    )
    return filter_node.video(0)


def scale2ref(
    _default: "VideoStream",
    _ref: "VideoStream",
    *,
    w: str,
    h: str,
    flags: str = None,
    interl: bool = None,
    size: str,
    in_color_matrix: int = None,
    out_color_matrix: int = None,
    in_range: int = None,
    out_range: int = None,
    in_v_chr_pos: int = None,
    in_h_chr_pos: int = None,
    out_v_chr_pos: int = None,
    out_h_chr_pos: int = None,
    force_original_aspect_ratio: int = None,
    force_divisible_by: int = None,
    param0: float = None,
    param1: float = None,
    eval: int = None,
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    11.218 scale2ref
    Scale (resize) the input video, based on a reference video.

    See the scale filter for available options, scale2ref supports the same but
    uses the reference video instead of the main input as basis. scale2ref also
    supports the following additional constants for the w and
    h options:

    Parameters:
    ----------

    :param str w: None
    :param str h: None
    :param str flags: None
    :param bool interl: None
    :param str size: None
    :param int in_color_matrix: None
    :param int out_color_matrix: None
    :param int in_range: None
    :param int out_range: None
    :param int in_v_chr_pos: None
    :param int in_h_chr_pos: None
    :param int out_v_chr_pos: None
    :param int out_h_chr_pos: None
    :param int force_original_aspect_ratio: None
    :param int force_divisible_by: None
    :param float param0: None
    :param float param1: None
    :param int eval: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref

    """
    filter_node = FilterNode(
        name="scale2ref",
        streams=[
            _default,
            _ref,
        ],
        kwargs={
            "w": w,
            "h": h,
            "flags": flags,
            "interl": interl,
            "size": size,
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
        | kwargs,
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def scale2ref_npp(
    _default: "VideoStream",
    _ref: "VideoStream",
    *,
    w: str,
    h: str,
    format: str = None,
    s: str,
    interp_algo: int = None,
    force_original_aspect_ratio: int = None,
    force_divisible_by: int = None,
    eval: int = None,
    **kwargs: Any
) -> tuple["VideoStream", "VideoStream",]:
    """

    11.219 scale2ref_npp
    Use the NVIDIA Performance Primitives (libnpp) to scale (resize) the input
    video, based on a reference video.

    See the scale_npp filter for available options, scale2ref_npp supports the same
    but uses the reference video instead of the main input as basis. scale2ref_npp
    also supports the following additional constants for the w and
    h options:

    Parameters:
    ----------

    :param str w: None
    :param str h: None
    :param str format: None
    :param str s: None
    :param int interp_algo: None
    :param int force_original_aspect_ratio: None
    :param int force_divisible_by: None
    :param int eval: None

    Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref_005fnpp

    """
    filter_node = FilterNode(
        name="scale2ref_npp",
        streams=[
            _default,
            _ref,
        ],
        kwargs={
            "w": w,
            "h": h,
            "format": format,
            "s": s,
            "interp_algo": interp_algo,
            "force_original_aspect_ratio": force_original_aspect_ratio,
            "force_divisible_by": force_divisible_by,
            "eval": eval,
        }
        | kwargs,
    )
    return (
        filter_node.video(0),
        filter_node.video(1),
    )


def sidechaincompress(
    _main: "AudioStream",
    _sidechain: "AudioStream",
    *,
    level_in: float = None,
    mode: int = None,
    threshold: float = None,
    ratio: float = None,
    attack: float = None,
    release: float = None,
    makeup: float = None,
    knee: float = None,
    link: int = None,
    detection: int = None,
    level_sc: float = None,
    mix: float = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.105 sidechaincompress
    This filter acts like normal compressor but has the ability to compress
    detected signal using second input signal.
    It needs two input streams and returns one output stream.
    First input stream will be processed depending on second stream signal.
    The filtered signal then can be filtered with other filters in later stages of
    processing. See pan and amerge filter.

    The filter accepts the following options:

    Parameters:
    ----------

    :param float level_in: Set input gain. Default is 1. Range is between 0.015625 and 64.
    :param int mode: Set mode of compressor operation. Can be upward or downward. Default is downward.
    :param float threshold: If a signal of second stream raises above this level it will affect the gain reduction of first stream. By default is 0.125. Range is between 0.00097563 and 1.
    :param float ratio: Set a ratio about which the signal is reduced. 1:2 means that if the level raised 4dB above the threshold, it will be only 2dB above after the reduction. Default is 2. Range is between 1 and 20.
    :param float attack: Amount of milliseconds the signal has to rise above the threshold before gain reduction starts. Default is 20. Range is between 0.01 and 2000.
    :param float release: Amount of milliseconds the signal has to fall below the threshold before reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
    :param float makeup: Set the amount by how much signal will be amplified after processing. Default is 1. Range is from 1 to 64.
    :param float knee: Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.82843. Range is between 1 and 8.
    :param int link: Choose if the average level between all channels of side-chain stream or the louder(maximum) channel of side-chain stream affects the reduction. Default is average.
    :param int detection: Should the exact signal be taken in case of peak or an RMS one in case of rms. Default is rms which is mainly smoother.
    :param float level_sc: Set sidechain gain. Default is 1. Range is between 0.015625 and 64.
    :param float mix: How much to use compressed signal in output. Default is 1. Range is between 0 and 1.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress

    """
    filter_node = FilterNode(
        name="sidechaincompress",
        streams=[
            _main,
            _sidechain,
        ],
        kwargs={
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
        | kwargs,
    )
    return filter_node.audio(0)


def sidechaingate(
    _main: "AudioStream",
    _sidechain: "AudioStream",
    *,
    level_in: float = None,
    mode: int = None,
    range: float = None,
    threshold: float = None,
    ratio: float = None,
    attack: float = None,
    release: float = None,
    makeup: float = None,
    knee: float = None,
    detection: int = None,
    link: int = None,
    level_sc: float = None,
    **kwargs: Any
) -> "AudioStream":
    """

    8.106 sidechaingate
    A sidechain gate acts like a normal (wideband) gate but has the ability to
    filter the detected signal before sending it to the gain reduction stage.
    Normally a gate uses the full range signal to detect a level above the
    threshold.
    For example: If you cut all lower frequencies from your sidechain signal
    the gate will decrease the volume of your track only if not enough highs
    appear. With this technique you are able to reduce the resonation of a
    natural drum or remove "rumbling" of muted strokes from a heavily distorted
    guitar.
    It needs two input streams and returns one output stream.
    First input stream will be processed depending on second stream signal.

    The filter accepts the following options:

    Parameters:
    ----------

    :param float level_in: Set input level before filtering. Default is 1. Allowed range is from 0.015625 to 64.
    :param int mode: Set the mode of operation. Can be upward or downward. Default is downward. If set to upward mode, higher parts of signal will be amplified, expanding dynamic range in upward direction. Otherwise, in case of downward lower parts of signal will be reduced.
    :param float range: Set the level of gain reduction when the signal is below the threshold. Default is 0.06125. Allowed range is from 0 to 1. Setting this to 0 disables reduction and then filter behaves like expander.
    :param float threshold: If a signal rises above this level the gain reduction is released. Default is 0.125. Allowed range is from 0 to 1.
    :param float ratio: Set a ratio about which the signal is reduced. Default is 2. Allowed range is from 1 to 9000.
    :param float attack: Amount of milliseconds the signal has to rise above the threshold before gain reduction stops. Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
    :param float release: Amount of milliseconds the signal has to fall below the threshold before the reduction is increased again. Default is 250 milliseconds. Allowed range is from 0.01 to 9000.
    :param float makeup: Set amount of amplification of signal after processing. Default is 1. Allowed range is from 1 to 64.
    :param float knee: Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.828427125. Allowed range is from 1 to 8.
    :param int detection: Choose if exact signal should be taken for detection or an RMS like one. Default is rms. Can be peak or rms.
    :param int link: Choose if the average level between all channels or the louder channel affects the reduction. Default is average. Can be average or maximum.
    :param float level_sc: Set sidechain gain. Default is 1. Range is from 0.015625 to 64.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaingate

    """
    filter_node = FilterNode(
        name="sidechaingate",
        streams=[
            _main,
            _sidechain,
        ],
        kwargs={
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
        }
        | kwargs,
    )
    return filter_node.audio(0)


def signature(
    *streams: "VideoStream",
    detectmode: int = None,
    nb_inputs: int = None,
    filename: str = None,
    format: int = None,
    th_d: int = None,
    th_dc: int = None,
    th_xh: int = None,
    th_di: int = None,
    th_it: float = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.237 signature
    Calculates the MPEG-7 Video Signature. The filter can handle more than one
    input. In this case the matching between the inputs can be calculated additionally.
    The filter always passes through the first input. The signature of each stream can
    be written into a file.

    It accepts the following options:

    Parameters:
    ----------

    :param int detectmode: Enable or disable the matching process. Available values are: ‘off’ Disable the calculation of a matching (default). ‘full’ Calculate the matching for the whole video and output whether the whole video matches or only parts. ‘fast’ Calculate only until a matching is found or the video ends. Should be faster in some cases.
    :param int nb_inputs: Set the number of inputs. The option value must be a non negative integer. Default value is 1.
    :param str filename: Set the path to which the output is written. If there is more than one input, the path must be a prototype, i.e. must contain %d or %0nd (where n is a positive integer), that will be replaced with the input number. If no filename is specified, no output will be written. This is the default.
    :param int format: Choose the output format. Available values are: ‘binary’ Use the specified binary representation (default). ‘xml’ Use the specified xml representation.
    :param int th_d: Set threshold to detect one word as similar. The option value must be an integer greater than zero. The default value is 9000.
    :param int th_dc: Set threshold to detect all words as similar. The option value must be an integer greater than zero. The default value is 60000.
    :param int th_xh: Set threshold to detect frames as similar. The option value must be an integer greater than zero. The default value is 116.
    :param int th_di: Set the minimum length of a sequence in frames to recognize it as matching sequence. The option value must be a non negative integer value. The default value is 0.
    :param float th_it: Set the minimum relation, that matching frames to all frames must have. The option value must be a double value between 0 and 1. The default value is 0.5.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#signature

    """
    filter_node = FilterNode(
        name="signature",
        streams=[
            *streams,
        ],
        kwargs={
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
        | kwargs,
    )
    return filter_node.video(0)


def spectrumsynth(
    _magnitude: "VideoStream",
    _phase: "VideoStream",
    *,
    sample_rate: int = None,
    channels: int = None,
    scale: int = None,
    slide: int = None,
    win_func: int = None,
    overlap: float = None,
    orientation: int = None,
    **kwargs: Any
) -> "AudioStream":
    """

    18.32 spectrumsynth
    Synthesize audio from 2 input video spectrums, first input stream represents
    magnitude across time and second represents phase across time.
    The filter will transform from frequency domain as displayed in videos back
    to time domain as presented in audio output.

    This filter is primarily created for reversing processed showspectrum
    filter outputs, but can synthesize sound from other spectrograms too.
    But in such case results are going to be poor if the phase data is not
    available, because in such cases phase data need to be recreated, usually
    it’s just recreated from random noise.
    For best results use gray only output (channel color mode in
    showspectrum filter) and log scale for magnitude video and
    lin scale for phase video. To produce phase, for 2nd video, use
    data option. Inputs videos should generally use fullframe
    slide mode as that saves resources needed for decoding video.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int sample_rate: Specify sample rate of output audio, the sample rate of audio from which spectrum was generated may differ.
    :param int channels: Set number of channels represented in input video spectrums.
    :param int scale: Set scale which was used when generating magnitude input spectrum. Can be lin or log. Default is log.
    :param int slide: Set slide which was used when generating inputs spectrums. Can be replace, scroll, fullframe or rscroll. Default is fullframe.
    :param int win_func: Set window function used for resynthesis.
    :param float overlap: Set window overlap. In range [0, 1]. Default is 1, which means optimal overlap for selected window function will be picked.
    :param int orientation: Set orientation of input videos. Can be vertical or horizontal. Default is vertical.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#spectrumsynth

    """
    filter_node = FilterNode(
        name="spectrumsynth",
        streams=[
            _magnitude,
            _phase,
        ],
        kwargs={
            "sample_rate": sample_rate,
            "channels": channels,
            "scale": scale,
            "slide": slide,
            "win_func": win_func,
            "overlap": overlap,
            "orientation": orientation,
        }
        | kwargs,
    )
    return filter_node.audio(0)


def ssim(_main: "VideoStream", _reference: "VideoStream", *, stats_file: str, **kwargs: Any) -> "VideoStream":
    """

    11.243 ssim
    Obtain the SSIM (Structural SImilarity Metric) between two input videos.

    This filter takes in input two input videos, the first input is
    considered the "main" source and is passed unchanged to the
    output. The second input is used as a "reference" video for computing
    the SSIM.

    Both video inputs must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The filter stores the calculated SSIM of each frame.

    The description of the accepted parameters follows.


    The file printed if stats_file is selected, contains a sequence of
    key/value pairs of the form key:value for each compared
    couple of frames.

    A description of each shown parameter follows:


    This filter also supports the framesync options.

    Parameters:
    ----------

    :param str stats_file: If specified the filter will use the named file to save the SSIM of each individual frame. When filename equals "-" the data is sent to standard output.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#ssim

    """
    filter_node = FilterNode(
        name="ssim",
        streams=[
            _main,
            _reference,
        ],
        kwargs={
            "stats_file": stats_file,
        }
        | kwargs,
    )
    return filter_node.video(0)


def streamselect(*streams: "VideoStream", inputs: int = None, map: str, **kwargs: Any) -> FilterNode:
    """

    11.245 streamselect, astreamselect
    Select video or audio streams.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int inputs: Set number of inputs. Default is 2.
    :param str map: Set input indexes to remap to outputs.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

    """
    filter_node = FilterNode(
        name="streamselect",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "map": map,
        }
        | kwargs,
    )

    return filter_node


def threshold(
    _default: "VideoStream",
    _threshold: "VideoStream",
    _min: "VideoStream",
    _max: "VideoStream",
    *,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.253 threshold
    Apply threshold effect to video stream.

    This filter needs four video streams to perform thresholding.
    First stream is stream we are filtering.
    Second stream is holding threshold values, third stream is holding min values,
    and last, fourth stream is holding max values.

    The filter accepts the following option:


    For example if first stream pixel’s component value is less then threshold value
    of pixel component from 2nd threshold stream, third stream value will picked,
    otherwise fourth stream pixel component value will be picked.

    Using color source filter one can perform various types of thresholding:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#threshold

    """
    filter_node = FilterNode(
        name="threshold",
        streams=[
            _default,
            _threshold,
            _min,
            _max,
        ],
        kwargs={
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def unpremultiply(*streams: "VideoStream", planes: int = None, inplace: bool = None, **kwargs: Any) -> "VideoStream":
    """

    11.266 unpremultiply
    Apply alpha unpremultiply effect to input video stream using first plane
    of second stream as alpha.

    Both streams must have same dimensions and same pixel format.

    The filter accepts the following option:

    Parameters:
    ----------

    :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed. If the format has 1 or 2 components, then luma is bit 0. If the format has 3 or 4 components: for RGB formats bit 0 is green, bit 1 is blue and bit 2 is red; for YUV formats bit 0 is luma, bit 1 is chroma-U and bit 2 is chroma-V. If present, the alpha channel is always the last bit.
    :param bool inplace: Do not require 2nd input for processing, instead use alpha plane from input stream.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#unpremultiply

    """
    filter_node = FilterNode(
        name="unpremultiply",
        streams=[
            *streams,
        ],
        kwargs={
            "planes": planes,
            "inplace": inplace,
        }
        | kwargs,
    )
    return filter_node.video(0)


def varblur(
    _default: "VideoStream",
    _radius: "VideoStream",
    *,
    min_r: int = None,
    max_r: int = None,
    planes: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.272 varblur
    Apply variable blur filter by using 2nd video stream to set blur radius.
    The 2nd stream must have the same dimensions.

    This filter accepts the following options:


    The varblur filter also supports the framesync options.

    Parameters:
    ----------

    :param int min_r: Set min allowed radius. Allowed range is from 0 to 254. Default is 0.
    :param int max_r: Set max allowed radius. Allowed range is from 1 to 255. Default is 8.
    :param int planes: Set which planes to process. By default, all are used.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#varblur

    """
    filter_node = FilterNode(
        name="varblur",
        streams=[
            _default,
            _radius,
        ],
        kwargs={
            "min_r": min_r,
            "max_r": max_r,
            "planes": planes,
        }
        | kwargs,
    )
    return filter_node.video(0)


def vif(_main: "VideoStream", _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
    """

    11.279 vif
    Obtain the average VIF (Visual Information Fidelity) between two input videos.

    This filter takes two input videos.

    Both input videos must have the same resolution and pixel format for
    this filter to work correctly. Also it assumes that both inputs
    have the same number of frames, which are compared one by one.

    The obtained average VIF score is printed through the logging system.

    The filter stores the calculated VIF score of each frame.

    This filter also supports the framesync options.

    In the below example the input file main.mpg being processed is compared
    with the reference file ref.mpg.


    ffmpeg -i main.mpg -i ref.mpg -lavfi vif -f null -

    Parameters:
    ----------


    Ref: https://ffmpeg.org/ffmpeg-filters.html#vif

    """
    filter_node = FilterNode(
        name="vif",
        streams=[
            _main,
            _reference,
        ],
        kwargs={} | kwargs,
    )
    return filter_node.video(0)


def vstack(*streams: "VideoStream", inputs: int = None, shortest: bool = None, **kwargs: Any) -> "VideoStream":
    """

    11.282 vstack
    Stack input videos vertically.

    All streams must be of same pixel format and of same width.

    Note that this filter is faster than using overlay and pad filter
    to create same output.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int inputs: Set number of input streams. Default is 2.
    :param bool shortest: If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#vstack

    """
    filter_node = FilterNode(
        name="vstack",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "shortest": shortest,
        }
        | kwargs,
    )
    return filter_node.video(0)


def xcorrelate(
    _primary: "VideoStream", _secondary: "VideoStream", *, planes: int = None, secondary: int = None, **kwargs: Any
) -> "VideoStream":
    """

    11.287 xcorrelate
    Apply normalized cross-correlation between first and second input video stream.

    Second input video stream dimensions must be lower than first input video stream.

    The filter accepts the following options:


    The xcorrelate filter also supports the framesync options.

    Parameters:
    ----------

    :param int planes: Set which planes to process.
    :param int secondary: Set which secondary video frames will be processed from second input video stream, can be first or all. Default is all.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xcorrelate

    """
    filter_node = FilterNode(
        name="xcorrelate",
        streams=[
            _primary,
            _secondary,
        ],
        kwargs={
            "planes": planes,
            "secondary": secondary,
        }
        | kwargs,
    )
    return filter_node.video(0)


def xfade(
    _main: "VideoStream",
    _xfade: "VideoStream",
    *,
    transition: int = None,
    duration: int = None,
    offset: int = None,
    expr: str,
    **kwargs: Any
) -> "VideoStream":
    """

    11.288 xfade
    Apply cross fade from one input video stream to another input video stream.
    The cross fade is applied for specified duration.

    Both inputs must be constant frame-rate and have the same resolution, pixel format,
    frame rate and timebase.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int transition: Set one of available transition effects: ‘custom’ ‘fade’ ‘wipeleft’ ‘wiperight’ ‘wipeup’ ‘wipedown’ ‘slideleft’ ‘slideright’ ‘slideup’ ‘slidedown’ ‘circlecrop’ ‘rectcrop’ ‘distance’ ‘fadeblack’ ‘fadewhite’ ‘radial’ ‘smoothleft’ ‘smoothright’ ‘smoothup’ ‘smoothdown’ ‘circleopen’ ‘circleclose’ ‘vertopen’ ‘vertclose’ ‘horzopen’ ‘horzclose’ ‘dissolve’ ‘pixelize’ ‘diagtl’ ‘diagtr’ ‘diagbl’ ‘diagbr’ ‘hlslice’ ‘hrslice’ ‘vuslice’ ‘vdslice’ ‘hblur’ ‘fadegrays’ ‘wipetl’ ‘wipetr’ ‘wipebl’ ‘wipebr’ ‘squeezeh’ ‘squeezev’ ‘zoomin’ ‘fadefast’ ‘fadeslow’ ‘hlwind’ ‘hrwind’ ‘vuwind’ ‘vdwind’ ‘coverleft’ ‘coverright’ ‘coverup’ ‘coverdown’ ‘revealleft’ ‘revealright’ ‘revealup’ ‘revealdown’ Default transition effect is fade.
    :param int duration: Set cross fade duration in seconds. Range is 0 to 60 seconds. Default duration is 1 second.
    :param int offset: Set cross fade start relative to first input stream in seconds. Default offset is 0.
    :param str expr: Set expression for custom transition effect. The expressions can use the following variables and functions: X Y The coordinates of the current sample. W H The width and height of the image. P Progress of transition effect. PLANE Currently processed plane. A Return value of first input at current location and plane. B Return value of second input at current location and plane. a0(x, y) a1(x, y) a2(x, y) a3(x, y) Return the value of the pixel at location (x,y) of the first/second/third/fourth component of first input. b0(x, y) b1(x, y) b2(x, y) b3(x, y) Return the value of the pixel at location (x,y) of the first/second/third/fourth component of second input.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xfade

    """
    filter_node = FilterNode(
        name="xfade",
        streams=[
            _main,
            _xfade,
        ],
        kwargs={
            "transition": transition,
            "duration": duration,
            "offset": offset,
            "expr": expr,
        }
        | kwargs,
    )
    return filter_node.video(0)


def xfade_opencl(
    _main: "VideoStream",
    _xfade: "VideoStream",
    *,
    transition: int = None,
    source: str,
    kernel: str,
    duration: int = None,
    offset: int = None,
    **kwargs: Any
) -> "VideoStream":
    """

    12.18 xfade_opencl
    Cross fade two videos with custom transition effect by using OpenCL.

    It accepts the following options:


    The program source file must contain a kernel function with the given name,
    which will be run once for each plane of the output.  Each run on a plane
    gets enqueued as a separate 2D global NDRange with one work-item for each
    pixel to be generated.  The global ID offset for each work-item is therefore
    the coordinates of a pixel in the destination image.

    The kernel function needs to take the following arguments:

     Destination image, __write_only image2d_t.

    This image will become the output; the kernel should write all of it.

     First Source image, __read_only image2d_t.
    Second Source image, __read_only image2d_t.

    These are the most recent images on each input.  The kernel may read from
    them to generate the output, but they can’t be written to.

     Transition progress, float. This value is always between 0 and 1 inclusive.

    Example programs:


     Apply dots curtain transition effect:
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
        streams=[
            _main,
            _xfade,
        ],
        kwargs={
            "transition": transition,
            "source": source,
            "kernel": kernel,
            "duration": duration,
            "offset": offset,
        }
        | kwargs,
    )
    return filter_node.video(0)


def xmedian(
    *streams: "VideoStream", inputs: int = None, planes: int = None, percentile: float = None, **kwargs: Any
) -> "VideoStream":
    """

    11.289 xmedian
    Pick median pixels from several input videos.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int inputs: Set number of inputs. Default is 3. Allowed range is from 3 to 255. If number of inputs is even number, than result will be mean value between two median values.
    :param int planes: Set which planes to filter. Default value is 15, by which all planes are processed.
    :param float percentile: Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xmedian

    """
    filter_node = FilterNode(
        name="xmedian",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "planes": planes,
            "percentile": percentile,
        }
        | kwargs,
    )
    return filter_node.video(0)


def xstack(
    *streams: "VideoStream",
    inputs: int = None,
    layout: str,
    grid: str,
    shortest: bool = None,
    fill: str = None,
    **kwargs: Any
) -> "VideoStream":
    """

    11.290 xstack
    Stack video inputs into custom layout.

    All streams must be of same pixel format.

    The filter accepts the following options:

    Parameters:
    ----------

    :param int inputs: Set number of input streams. Default is 2.
    :param str layout: Specify layout of inputs. This option requires the desired layout configuration to be explicitly set by the user. This sets position of each video input in output. Each input is separated by ’|’. The first number represents the column, and the second number represents the row. Numbers start at 0 and are separated by ’_’. Optionally one can use wX and hX, where X is video input from which to take width or height. Multiple values can be used when separated by ’+’. In such case values are summed together. Note that if inputs are of different sizes gaps may appear, as not all of the output video frame will be filled. Similarly, videos can overlap each other if their position doesn’t leave enough space for the full frame of adjoining videos. For 2 inputs, a default layout of 0_0|w0_0 (equivalent to grid=2x1) is set. In all other cases, a layout or a grid must be set by the user. Either grid or layout can be specified at a time. Specifying both will result in an error.
    :param str grid: Specify a fixed size grid of inputs. This option is used to create a fixed size grid of the input streams. Set the grid size in the form COLUMNSxROWS. There must be ROWS * COLUMNS input streams and they will be arranged as a grid with ROWS rows and COLUMNS columns. When using this option, each input stream within a row must have the same height and all the rows must have the same width. If grid is set, then inputs option is ignored and is implicitly set to ROWS * COLUMNS. For 2 inputs, a default grid of 2x1 (equivalent to layout=0_0|w0_0) is set. In all other cases, a layout or a grid must be set by the user. Either grid or layout can be specified at a time. Specifying both will result in an error.
    :param bool shortest: If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.
    :param str fill: If set to valid color, all unused pixels will be filled with that color. By default fill is set to none, so it is disabled.

    Ref: https://ffmpeg.org/ffmpeg-filters.html#xstack

    """
    filter_node = FilterNode(
        name="xstack",
        streams=[
            *streams,
        ],
        kwargs={
            "inputs": inputs,
            "layout": layout,
            "grid": grid,
            "shortest": shortest,
            "fill": fill,
        }
        | kwargs,
    )
    return filter_node.video(0)
