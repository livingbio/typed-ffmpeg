# NOTE: this file is auto-generated, do not modify
"""
FFmpeg sources.
"""


from typing import Any, Literal


from ffmpeg_core.types import Binary, Boolean, Color, Dictionary, Double, Duration, Flags, Float, Func, Image_size, Int, Int64, Pix_fmt, Rational, Sample_fmt, String, Time, Video_rate
from .dag.factory import filter_node_factory
from ffmpeg_core.utils.frozendict import FrozenDict, merge
from ffmpeg_core.utils.typing import override
from ffmpeg_core.schema import Default, StreamType, Auto, FFMpegOptionGroup
from ffmpeg_core.common.schema import FFMpegFilterDef
from .options.framesync import FFMpegFrameSyncOption
from .options.timeline import FFMpegTimelineOption

from .options.codec import FFMpegAVCodecContextEncoderOption, FFMpegAVCodecContextDecoderOption


from .options.format import FFMpegAVFormatContextEncoderOption, FFMpegAVFormatContextDecoderOption

from .streams.av import AVStream
from .streams.channel_layout import CHANNEL_LAYOUT
from .codecs.schema import FFMpegEncoderOption, FFMpegDecoderOption
from .formats.schema import FFMpegMuxerOption, FFMpegDemuxerOption

from .dag.nodes import FilterableStream, FilterNode, OutputStream, OutputNode, InputNode, GlobalNode, GlobalStream


from .streams.video import VideoStream


from .streams.audio import AudioStream



import re










def abuffer(





    *,
    time_base: Rational = Default('0/1'),sample_rate: Int = Default('0'),sample_fmt: Sample_fmt = Default('none'),channel_layout: String = Default(None),channels: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    time_base: (from 0 to INT_MAX) (default 0/1)
    sample_rate: (from 0 to INT_MAX) (default 0)
    sample_fmt: (default none)
    channel_layout:
    channels: (from 0 to INT_MAX) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#abuffer)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='abuffer', typings_input=(), typings_output=('audio',)),





        **merge({

            "time_base": time_base,

            "sample_rate": sample_rate,

            "sample_fmt": sample_fmt,

            "channel_layout": channel_layout,

            "channels": channels,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)


















































def aevalsrc(





    *,
    exprs: String = Default(None),nb_samples: Int = Default('1024'),sample_rate: String = Default('44100'),duration: Duration = Default('-0.000001'),channel_layout: String = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    exprs: set the '|'-separated list of channels expressions
    nb_samples: set the number of samples per requested frame (from 0 to INT_MAX) (default 1024)
    sample_rate: set the sample rate (default "44100")
    duration: set audio duration (default -0.000001)
    channel_layout: set channel layout
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aevalsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='aevalsrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "exprs": exprs,

            "nb_samples": nb_samples,

            "sample_rate": sample_rate,

            "duration": duration,

            "channel_layout": channel_layout,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)










def afdelaysrc(





    *,
    delay: Double = Default('0'),sample_rate: Int = Default('44100'),nb_samples: Int = Default('1024'),taps: Int = Default('0'),channel_layout: String = Default('stereo'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


.. note:: New in FFmpeg 6.0.


Args:
    delay: set fractional delay (from 0 to 32767) (default 0)
    sample_rate: set sample rate (from 1 to INT_MAX) (default 44100)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    taps: set number of taps for delay filter (from 0 to 32768) (default 0)
    channel_layout: set channel layout (default "stereo")
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afdelaysrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='afdelaysrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "delay": delay,

            "sample_rate": sample_rate,

            "nb_samples": nb_samples,

            "taps": taps,

            "channel_layout": channel_layout,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)










def afireqsrc(





    *,
    preset: Int| Literal["custom","flat","acoustic","bass","beats","classic","clear","deep bass","dubstep","electronic","hardstyle","hip-hop","jazz","metal","movie","pop","r&b","rock","vocal booster"] | Default = Default('flat'),gains: String = Default('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'),bands: String = Default('25 40 63 100 160 250 400 630 1000 1600 2500 4000 6300 10000 16000 24000'),taps: Int = Default('4096'),sample_rate: Int = Default('44100'),nb_samples: Int = Default('1024'),interp: Int| Literal["linear","cubic"] | Default = Default('linear'),phase: Int| Literal["linear","min"] | Default = Default('min'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


.. note:: New in FFmpeg 6.0.


Args:
    preset: set equalizer preset (from -1 to 17) (default flat)
    gains: set gain values per band (default "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
    bands: set central frequency values per band (default "25 40 63 100 160 250 400 630 1000 1600 2500 4000 6300 10000 16000 24000")
    taps: set number of taps (from 16 to 65535) (default 4096)
    sample_rate: set sample rate (from 1 to INT_MAX) (default 44100)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    interp: set the interpolation (from 0 to 1) (default linear)
    phase: set the phase (from 0 to 1) (default min)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afireqsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='afireqsrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "preset": preset,

            "gains": gains,

            "bands": bands,

            "taps": taps,

            "sample_rate": sample_rate,

            "nb_samples": nb_samples,

            "interp": interp,

            "phase": phase,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)






def afirsrc(





    *,
    taps: Int = Default('1025'),frequency: String = Default('0 1'),magnitude: String = Default('1 1'),phase: String = Default('0 0'),sample_rate: Int = Default('44100'),nb_samples: Int = Default('1024'),win_func: Int| Literal["rect","bartlett","hann","hanning","hamming","blackman","welch","flattop","bharris","bnuttall","bhann","sine","nuttall","lanczos","gauss","tukey","dolph","cauchy","parzen","poisson","bohman","kaiser"] | Default = Default('blackman'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    taps: set number of taps (from 9 to 65535) (default 1025)
    frequency: set frequency points (default "0 1")
    magnitude: set magnitude values (default "1 1")
    phase: set phase values (default "0 0")
    sample_rate: set sample rate (from 1 to INT_MAX) (default 44100)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    win_func: set window function (from 0 to 20) (default blackman)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afirsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='afirsrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "taps": taps,

            "frequency": frequency,

            "magnitude": magnitude,

            "phase": phase,

            "sample_rate": sample_rate,

            "nb_samples": nb_samples,

            "win_func": win_func,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)






















def ainterleave(



    *streams: AudioStream,




    nb_inputs: Int = Auto('len(streams)'),duration: Int| Literal["longest","shortest","first"] | Default = Default('longest'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    duration: how to determine the end-of-stream (from 0 to 2) (default longest)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='ainterleave', typings_input='[StreamType.audio] * int(nb_inputs)', typings_output=('audio',)),



        *streams,



        **merge({

            "nb_inputs": nb_inputs,

            "duration": duration,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)












def allrgb(





    *,
    rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='allrgb', typings_input=(), typings_output=('video',)),





        **merge({

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def allyuv(





    *,
    rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='allyuv', typings_input=(), typings_output=('video',)),





        **merge({

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)












def amerge(



    *streams: AudioStream,




    inputs: Int = Auto('len(streams)'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    inputs: specify the number of inputs (from 1 to 64) (default 2)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#amerge)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='amerge', typings_input='[StreamType.audio] * int(inputs)', typings_output=('audio',)),



        *streams,



        **merge({

            "inputs": inputs,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)








def amix(



    *streams: AudioStream,




    inputs: Int = Auto('len(streams)'),duration: Int| Literal["longest","shortest","first"] | Default = Default('longest'),dropout_transition: Float = Default('2'),weights: String = Default('1 1'),normalize: Boolean = Default('true'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    inputs: Number of inputs. (from 1 to 32767) (default 2)
    duration: How to determine the end-of-stream. (from 0 to 2) (default longest)
    dropout_transition: Transition time, in seconds, for volume renormalization when an input stream ends. (from 0 to INT_MAX) (default 2)
    weights: Set weight for each input. (default "1 1")
    normalize: Scale inputs (default true)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#amix)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='amix', typings_input='[StreamType.audio] * int(inputs)', typings_output=('audio',)),



        *streams,



        **merge({

            "inputs": inputs,

            "duration": duration,

            "dropout_transition": dropout_transition,

            "weights": weights,

            "normalize": normalize,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)






def amovie(





    *,
    filename: String = Default(None),format_name: String = Default(None),stream_index: Int = Default('-1'),seek_point: Double = Default('0'),streams: String = Default(None),loop: Int = Default('1'),discontinuity: Duration = Default('0'),dec_threads: Int = Default('0'),format_opts: Dictionary = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> FilterNode:
    """

Inputs:


Args:
    filename:
    format_name: set format name
    stream_index: set stream index (from -1 to INT_MAX) (default -1)
    seek_point: set seekpoint (seconds) (from 0 to 9.22337e+12) (default 0)
    streams: set streams
    loop: set loop count (from 0 to INT_MAX) (default 1)
    discontinuity: set discontinuity threshold (default 0)
    dec_threads: set the number of threads for decoding (from 0 to INT_MAX) (default 0)
    format_opts: set format options for the opened file
    extra_options: Extra options for the filter

Returns:
    filter_node: the filter node


References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#amovie)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='amovie', typings_input="[StreamType.audio] * len(streams.split('+'))", typings_output="[StreamType.audio] * len(streams.split('+'))"),





        **merge({

            "filename": filename,

            "format_name": format_name,

            "stream_index": stream_index,

            "seek_point": seek_point,

            "streams": streams,

            "loop": loop,

            "discontinuity": discontinuity,

            "dec_threads": dec_threads,

            "format_opts": format_opts,

        },
        extra_options,


        )
    )

    return filter_node


















def anoisesrc(





    *,
    sample_rate: Int = Default('48000'),amplitude: Double = Default('1'),duration: Duration = Default('0'),color: Int| Literal["white","pink","brown","blue","violet","velvet"] | Default = Default('white'),seed: Int64 = Default('-1'),nb_samples: Int = Default('1024'),density: Double = Default('0.05'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    sample_rate: set sample rate (from 15 to INT_MAX) (default 48000)
    amplitude: set amplitude (from 0 to 1) (default 1)
    duration: set duration (default 0)
    color: set noise color (from 0 to 5) (default white)
    seed: set random seed (from -1 to UINT32_MAX) (default -1)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    density: set density (from 0 to 1) (default 0.05)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anoisesrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='anoisesrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "sample_rate": sample_rate,

            "amplitude": amplitude,

            "duration": duration,

            "color": color,

            "seed": seed,

            "nb_samples": nb_samples,

            "density": density,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)










def anullsrc(





    *,
    channel_layout: String = Default('stereo'),sample_rate: String = Default('44100'),nb_samples: Int = Default('1024'),duration: Duration = Default('-0.000001'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    channel_layout: set channel_layout (default "stereo")
    sample_rate: set sample rate (default "44100")
    nb_samples: set the number of samples per requested frame (from 1 to 65535) (default 1024)
    duration: set the audio duration (default -0.000001)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anullsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='anullsrc', typings_input=(), typings_output=('audio',)),





        **merge({

            "channel_layout": channel_layout,

            "sample_rate": sample_rate,

            "nb_samples": nb_samples,

            "duration": duration,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)
































































def astreamselect(



    *streams: AudioStream,




    inputs: Int = Auto('len(streams)'),map: String = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> FilterNode:
    """

Inputs:


Args:
    inputs: number of input streams (from 2 to INT_MAX) (default 2)
    map: input indexes to remap to outputs
    extra_options: Extra options for the filter

Returns:
    filter_node: the filter node


References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='astreamselect', typings_input='[StreamType.audio] * int(inputs)', typings_output="[StreamType.audio] * len(re.findall(r'\\d+', str(map)))"),



        *streams,



        **merge({

            "inputs": inputs,

            "map": map,

        },
        extra_options,


        )
    )

    return filter_node




























def avsynctest(





    *,
    size: Image_size = Default('hd720'),framerate: Video_rate = Default('30'),samplerate: Int = Default('44100'),amplitude: Float = Default('0.7'),period: Int = Default('3'),delay: Int = Default('0'),cycle: Boolean = Default('false'),duration: Duration = Default('0'),fg: Color = Default('white'),bg: Color = Default('black'),ag: Color = Default('gray'),


    extra_options: dict[str, Any] | None = None,
)-> tuple[


            AudioStream,



            VideoStream,


]:
    """

Inputs:


Args:
    size: set frame size (default "hd720")
    framerate: set frame rate (default "30")
    samplerate: set sample rate (from 8000 to 384000) (default 44100)
    amplitude: set beep amplitude (from 0 to 1) (default 0.7)
    period: set beep period (from 1 to 99) (default 3)
    delay: set flash delay (from -30 to 30) (default 0)
    cycle: set delay cycle (default false)
    duration: set duration (default 0)
    fg: set foreground color (default "white")
    bg: set background color (default "black")
    ag: set additional color (default "gray")
    extra_options: Extra options for the filter

Returns:
    audio: the audio stream
    video: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#avsynctest)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='avsynctest', typings_input=(), typings_output=('audio', 'video')),





        **merge({

            "size": size,

            "framerate": framerate,

            "samplerate": samplerate,

            "amplitude": amplitude,

            "period": period,

            "delay": delay,

            "cycle": cycle,

            "duration": duration,

            "fg": fg,

            "bg": bg,

            "ag": ag,

        },
        extra_options,


        )
    )
    return (


                filter_node.audio(0),



                filter_node.video(0),


    )







































def bm3d(



    *streams: VideoStream,




    sigma: Float = Default('1'),block: Int = Default('16'),bstep: Int = Default('4'),group: Int = Default('1'),range: Int = Default('9'),mstep: Int = Default('1'),thmse: Float = Default('0'),hdthr: Float = Default('2.7'),estim: Int| Literal["basic","final"] | Default = Default('basic'),ref: Boolean = Default('false'),planes: Int = Default('7'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    sigma: set denoising strength (from 0 to 99999.9) (default 1)
    block: set size of local patch (from 8 to 64) (default 16)
    bstep: set sliding step for processing blocks (from 1 to 64) (default 4)
    group: set maximal number of similar blocks (from 1 to 256) (default 1)
    range: set block matching range (from 1 to INT_MAX) (default 9)
    mstep: set step for block matching (from 1 to 64) (default 1)
    thmse: set threshold of mean square error for block matching (from 0 to INT_MAX) (default 0)
    hdthr: set hard threshold for 3D transfer domain (from 0 to INT_MAX) (default 2.7)
    estim: set filtering estimation mode (from 0 to 1) (default basic)
    ref: have reference stream (default false)
    planes: set planes to filter (from 0 to 15) (default 7)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bm3d)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='bm3d', typings_input='[StreamType.video] + [StreamType.video] if ref else []', typings_output=('video',)),



        *streams,



        **merge({

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

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)








def buffer(





    *,
    width: Int = Default('0'),video_size: Image_size = Default(None),height: Int = Default('0'),pix_fmt: Pix_fmt = Default('none'),sar: Rational = Default('0/1'),time_base: Rational = Default('0/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    width: (from 0 to INT_MAX) (default 0)
    video_size:
    height: (from 0 to INT_MAX) (default 0)
    pix_fmt: (default none)
    sar: sample aspect ratio (from 0 to DBL_MAX) (default 0/1)
    time_base: (from 0 to DBL_MAX) (default 0/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#buffer)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='buffer', typings_input=(), typings_output=('video',)),





        **merge({

            "width": width,

            "video_size": video_size,

            "height": height,

            "pix_fmt": pix_fmt,

            "sar": sar,

            "time_base": time_base,

        },
        extra_options,


        )
    )
    return filter_node.video(0)














def cellauto(





    *,
    filename: String = Default(None),pattern: String = Default(None),rate: Video_rate = Default('25'),size: Image_size = Default(None),rule: Int = Default('110'),random_fill_ratio: Double = Default('0.618034'),random_seed: Int64 = Default('-1'),scroll: Boolean = Default('true'),start_full: Boolean = Default('false'),full: Boolean = Default('true'),stitch: Boolean = Default('true'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    filename: read initial pattern from file
    pattern: set initial pattern
    rate: set video rate (default "25")
    size: set video size
    rule: set rule (from 0 to 255) (default 110)
    random_fill_ratio: set fill ratio for filling initial grid randomly (from 0 to 1) (default 0.618034)
    random_seed: set the seed for filling the initial grid randomly (from -1 to UINT32_MAX) (default -1)
    scroll: scroll pattern downward (default true)
    start_full: start filling the whole video (default false)
    full: start filling the whole video (default true)
    stitch: stitch boundaries (default true)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#cellauto)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='cellauto', typings_input=(), typings_output=('video',)),





        **merge({

            "filename": filename,

            "pattern": pattern,

            "rate": rate,

            "size": size,

            "rule": rule,

            "random_fill_ratio": random_fill_ratio,

            "random_seed": random_seed,

            "scroll": scroll,

            "start_full": start_full,

            "full": full,

            "stitch": stitch,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
























def color(





    *,
    color: Color = Default('black'),size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    color: set color (default "black")
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='color', typings_input=(), typings_output=('video',)),





        **merge({

            "color": color,

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)










def colorchart(





    *,
    rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),patch_size: Image_size = Default('64x64'),preset: Int| Literal["reference","skintones"] | Default = Default('reference'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    patch_size: set the single patch size (default "64x64")
    preset: set the color checker chart preset (from 0 to 1) (default reference)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='colorchart', typings_input=(), typings_output=('video',)),





        **merge({

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "patch_size": patch_size,

            "preset": preset,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
























def colorspectrum(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),type: Int| Literal["black","white","all"] | Default = Default('black'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    type: set the color spectrum type (from 0 to 2) (default black)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='colorspectrum', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "type": type,

        },
        extra_options,


        )
    )
    return filter_node.video(0)












def concat(



    *streams: FilterableStream,




    n: Int = Auto('len(streams) // (int(v) + int(a))'),v: Int = Default('1'),a: Int = Default('0'),unsafe: Boolean = Default('false'),


    extra_options: dict[str, Any] | None = None,
)-> FilterNode:
    """

Inputs:


Args:
    n: specify the number of segments (from 1 to INT_MAX) (default 2)
    v: specify the number of video streams (from 0 to INT_MAX) (default 1)
    a: specify the number of audio streams (from 0 to INT_MAX) (default 0)
    unsafe: enable unsafe mode (default false)
    extra_options: Extra options for the filter

Returns:
    filter_node: the filter node


References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#concat)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='concat', typings_input='([StreamType.video]*int(v) + [StreamType.audio]*int(a))*int(n)', typings_output='[StreamType.video]*int(v) + [StreamType.audio]*int(a)'),



        *streams,



        **merge({

            "n": n,

            "v": v,

            "a": a,

            "unsafe": unsafe,

        },
        extra_options,


        )
    )

    return filter_node








































def decimate(



    *streams: VideoStream,




    cycle: Int = Default('5'),dupthresh: Double = Default('1.1'),scthresh: Double = Default('15'),blockx: Int = Default('32'),blocky: Int = Default('32'),ppsrc: Boolean = Default('false'),chroma: Boolean = Default('true'),mixed: Boolean = Default('false'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    cycle: set the number of frame from which one will be dropped (from 2 to 25) (default 5)
    dupthresh: set duplicate threshold (from 0 to 100) (default 1.1)
    scthresh: set scene change threshold (from 0 to 100) (default 15)
    blockx: set the size of the x-axis blocks used during metric calculations (from 4 to 512) (default 32)
    blocky: set the size of the y-axis blocks used during metric calculations (from 4 to 512) (default 32)
    ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    chroma: set whether or not chroma is considered in the metric calculations (default true)
    mixed: set whether or not the input only partially contains content to be decimated (default false)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#decimate)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='decimate', typings_input='[StreamType.video] + ([StreamType.video] if ppsrc else [])', typings_output=('video',)),



        *streams,



        **merge({

            "cycle": cycle,

            "dupthresh": dupthresh,

            "scthresh": scthresh,

            "blockx": blockx,

            "blocky": blocky,

            "ppsrc": ppsrc,

            "chroma": chroma,

            "mixed": mixed,

        },
        extra_options,


        )
    )
    return filter_node.video(0)




























































































def fieldmatch(



    *streams: VideoStream,




    order: Int| Literal["auto","bff","tff"] | Default = Default('auto'),mode: Int| Literal["pc","pc_n","pc_u","pc_n_ub","pcn","pcn_ub"] | Default = Default('pc_n'),ppsrc: Boolean = Default('false'),field: Int| Literal["auto","bottom","top"] | Default = Default('auto'),mchroma: Boolean = Default('true'),y0: Int = Default('0'),scthresh: Double = Default('12'),combmatch: Int| Literal["none","sc","full"] | Default = Default('sc'),combdbg: Int| Literal["none","pcn","pcnub"] | Default = Default('none'),cthresh: Int = Default('9'),chroma: Boolean = Default('false'),blockx: Int = Default('16'),blocky: Int = Default('16'),combpel: Int = Default('80'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    order: specify the assumed field order (from -1 to 1) (default auto)
    mode: set the matching mode or strategy to use (from 0 to 5) (default pc_n)
    ppsrc: mark main input as a pre-processed input and activate clean source input stream (default false)
    field: set the field to match from (from -1 to 1) (default auto)
    mchroma: set whether or not chroma is included during the match comparisons (default true)
    y0: define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX) (default 0)
    scthresh: set scene change detection threshold (from 0 to 100) (default 12)
    combmatch: set combmatching mode (from 0 to 2) (default sc)
    combdbg: enable comb debug (from 0 to 2) (default none)
    cthresh: set the area combing threshold used for combed frame detection (from -1 to 255) (default 9)
    chroma: set whether or not chroma is considered in the combed frame decision (default false)
    blockx: set the x-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    blocky: set the y-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
    combpel: set the number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed (from 0 to INT_MAX) (default 80)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fieldmatch)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='fieldmatch', typings_input='[StreamType.video] + [StreamType.video] if ppsrc else []', typings_output=('video',)),



        *streams,



        **merge({

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

        },
        extra_options,


        )
    )
    return filter_node.video(0)








































def gradients(





    *,
    size: Image_size = Default('640x480'),rate: Video_rate = Default('25'),c0: Color = Default('random'),c1: Color = Default('random'),c2: Color = Default('random'),c3: Color = Default('random'),c4: Color = Default('random'),c5: Color = Default('random'),c6: Color = Default('random'),c7: Color = Default('random'),x0: Int = Default('-1'),y0: Int = Default('-1'),x1: Int = Default('-1'),y1: Int = Default('-1'),nb_colors: Int = Default('2'),seed: Int64 = Default('-1'),duration: Duration = Default('-0.000001'),speed: Float = Default('0.01'),type: Int| Literal["linear","radial","circular","spiral"] | Default = Default('linear'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    size: set frame size (default "640x480")
    rate: set frame rate (default "25")
    c0: set 1st color (default "random")
    c1: set 2nd color (default "random")
    c2: set 3rd color (default "random")
    c3: set 4th color (default "random")
    c4: set 5th color (default "random")
    c5: set 6th color (default "random")
    c6: set 7th color (default "random")
    c7: set 8th color (default "random")
    x0: set gradient line source x0 (from -1 to INT_MAX) (default -1)
    y0: set gradient line source y0 (from -1 to INT_MAX) (default -1)
    x1: set gradient line destination x1 (from -1 to INT_MAX) (default -1)
    y1: set gradient line destination y1 (from -1 to INT_MAX) (default -1)
    nb_colors: set the number of colors (from 2 to 8) (default 2)
    seed: set the seed (from -1 to UINT32_MAX) (default -1)
    duration: set video duration (default -0.000001)
    speed: set gradients rotation speed (from 1e-05 to 1) (default 0.01)
    type: set gradient type (from 0 to 3) (default linear)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#gradients)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='gradients', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "c0": c0,

            "c1": c1,

            "c2": c2,

            "c3": c3,

            "c4": c4,

            "c5": c5,

            "c6": c6,

            "c7": c7,

            "x0": x0,

            "y0": y0,

            "x1": x1,

            "y1": y1,

            "nb_colors": nb_colors,

            "seed": seed,

            "duration": duration,

            "speed": speed,

            "type": type,

        },
        extra_options,


        )
    )
    return filter_node.video(0)












def guided(



    *streams: VideoStream,




    radius: Int = Default('3'),eps: Float = Default('0.01'),mode: Int| Literal["basic","fast"] | Default = Default('basic'),sub: Int = Default('4'),guidance: Int| Literal["off","on"] | Default = Default('off'),planes: Int = Default('1'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    radius: set the box radius (from 1 to 20) (default 3)
    eps: set the regularization parameter (with square) (from 0 to 1) (default 0.01)
    mode: set filtering mode (0: basic mode; 1: fast mode) (from 0 to 1) (default basic)
    sub: subsampling ratio for fast mode (from 2 to 64) (default 4)
    guidance: set guidance mode (0: off mode; 1: on mode) (from 0 to 1) (default off)
    planes: set planes to filter (from 0 to 15) (default 1)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#guided)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='guided', typings_input='[StreamType.video] + [StreamType.video] if guidance else []', typings_output=('video',)),



        *streams,



        **merge({

            "radius": radius,

            "eps": eps,

            "mode": mode,

            "sub": sub,

            "guidance": guidance,

            "planes": planes,

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)










def haldclutsrc(





    *,
    level: Int = Default('6'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    level: set level (from 2 to 16) (default 6)
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='haldclutsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "level": level,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)








def headphone(



    *streams: AudioStream,




    map: String = Default(None),gain: Float = Default('0'),lfe: Float = Default('0'),type: Int| Literal["time","freq"] | Default = Default('freq'),size: Int = Default('1024'),hrir: Int| Literal["stereo","multich"] | Default = Default('stereo'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

slice threading supported


Args:
    map: set channels convolution mappings
    gain: set gain in dB (from -20 to 40) (default 0)
    lfe: set lfe gain in dB (from -20 to 40) (default 0)
    type: set processing (from 0 to 1) (default freq)
    size: set frame size (from 1024 to 96000) (default 1024)
    hrir: set hrir format (from 0 to 1) (default stereo)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#headphone)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='headphone', typings_input="[StreamType.audio] + [StreamType.audio] * (len(str(map).split('|')) - 1) if int(hrir) == 1 else []", typings_output=('audio',)),



        *streams,



        **merge({

            "map": map,

            "gain": gain,

            "lfe": lfe,

            "type": type,

            "size": size,

            "hrir": hrir,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)












def hilbert(





    *,
    sample_rate: Int = Default('44100'),taps: Int = Default('22051'),nb_samples: Int = Default('1024'),win_func: Int| Literal["rect","bartlett","hann","hanning","hamming","blackman","welch","flattop","bharris","bnuttall","bhann","sine","nuttall","lanczos","gauss","tukey","dolph","cauchy","parzen","poisson","bohman","kaiser"] | Default = Default('blackman'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    sample_rate: set sample rate (from 1 to INT_MAX) (default 44100)
    taps: set number of taps (from 11 to 65535) (default 22051)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    win_func: set window function (from 0 to 20) (default blackman)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hilbert)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='hilbert', typings_input=(), typings_output=('audio',)),





        **merge({

            "sample_rate": sample_rate,

            "taps": taps,

            "nb_samples": nb_samples,

            "win_func": win_func,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)














def hstack(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),shortest: Boolean = Default('false'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    shortest: force termination when the shortest input terminates (default false)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hstack)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='hstack', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "shortest": shortest,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def hstack_vaapi(



    *streams: VideoStream,




    inputs: Int = Default('2'),shortest: Boolean = Default('false'),height: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


.. note:: New in FFmpeg 6.0.


Args:
    inputs: Set number of inputs (from 2 to 65535) (default 2)
    shortest: Force termination when the shortest input terminates (default false)
    height: Set output height (0 to use the height of input 0) (from 0 to 65535) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hstack_005fvaapi)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='hstack_vaapi', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "shortest": shortest,

            "height": height,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
































def interleave(



    *streams: VideoStream,




    nb_inputs: Int = Auto('len(streams)'),duration: Int| Literal["longest","shortest","first"] | Default = Default('longest'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    nb_inputs: set number of inputs (from 1 to INT_MAX) (default 2)
    duration: how to determine the end-of-stream (from 0 to 2) (default longest)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='interleave', typings_input='[StreamType.video] * int(nb_inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "nb_inputs": nb_inputs,

            "duration": duration,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def join(



    *streams: AudioStream,




    inputs: Int = Auto('len(streams)'),channel_layout: String = Default('stereo'),map: String = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    inputs: Number of input streams. (from 1 to INT_MAX) (default 2)
    channel_layout: Channel layout of the output stream. (default "stereo")
    map: A comma-separated list of channels maps in the format 'input_stream.input_channel-output_channel.
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#join)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='join', typings_input='[StreamType.audio] * int(inputs)', typings_output=('audio',)),



        *streams,



        **merge({

            "inputs": inputs,

            "channel_layout": channel_layout,

            "map": map,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)


















def life(





    *,
    filename: String = Default(None),size: Image_size = Default(None),rate: Video_rate = Default('25'),rule: String = Default('B3/S23'),random_fill_ratio: Double = Default('0.618034'),random_seed: Int64 = Default('-1'),stitch: Boolean = Default('true'),mold: Int = Default('0'),life_color: Color = Default('white'),death_color: Color = Default('black'),mold_color: Color = Default('black'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    filename: set source file
    size: set video size
    rate: set video rate (default "25")
    rule: set rule (default "B3/S23")
    random_fill_ratio: set fill ratio for filling initial grid randomly (from 0 to 1) (default 0.618034)
    random_seed: set the seed for filling the initial grid randomly (from -1 to UINT32_MAX) (default -1)
    stitch: stitch boundaries (default true)
    mold: set mold speed for dead cells (from 0 to 255) (default 0)
    life_color: set life color (default "white")
    death_color: set death color (default "black")
    mold_color: set mold color (default "black")
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#life)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='life', typings_input=(), typings_output=('video',)),





        **merge({

            "filename": filename,

            "size": size,

            "rate": rate,

            "rule": rule,

            "random_fill_ratio": random_fill_ratio,

            "random_seed": random_seed,

            "stitch": stitch,

            "mold": mold,

            "life_color": life_color,

            "death_color": death_color,

            "mold_color": mold_color,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def limitdiff(



    *streams: VideoStream,




    threshold: Float = Default('0.00392157'),elasticity: Float = Default('2'),reference: Boolean = Default('false'),planes: Int = Default('15'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    threshold: set the threshold (from 0 to 1) (default 0.00392157)
    elasticity: set the elasticity (from 0 to 10) (default 2)
    reference: enable reference stream (default false)
    planes: set the planes to filter (from 0 to 15) (default 15)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#limitdiff)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='limitdiff', typings_input='[StreamType.video, StreamType.video] + ([StreamType.video] if reference else [])', typings_output=('video',)),



        *streams,



        **merge({

            "threshold": threshold,

            "elasticity": elasticity,

            "reference": reference,

            "planes": planes,

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)






























def mandelbrot(





    *,
    size: Image_size = Default('640x480'),rate: Video_rate = Default('25'),maxiter: Int = Default('7189'),start_x: Double = Default('-0.743644'),start_y: Double = Default('-0.131826'),start_scale: Double = Default('3'),end_scale: Double = Default('0.3'),end_pts: Double = Default('400'),bailout: Double = Default('10'),morphxf: Double = Default('0.01'),morphyf: Double = Default('0.0123'),morphamp: Double = Default('0'),outer: Int| Literal["iteration_count","normalized_iteration_count","white","outz"] | Default = Default('normalized_iteration_count'),inner: Int| Literal["black","period","convergence","mincol"] | Default = Default('mincol'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set frame size (default "640x480")
    rate: set frame rate (default "25")
    maxiter: set max iterations number (from 1 to INT_MAX) (default 7189)
    start_x: set the initial x position (from -100 to 100) (default -0.743644)
    start_y: set the initial y position (from -100 to 100) (default -0.131826)
    start_scale: set the initial scale value (from 0 to FLT_MAX) (default 3)
    end_scale: set the terminal scale value (from 0 to FLT_MAX) (default 0.3)
    end_pts: set the terminal pts value (from 0 to I64_MAX) (default 400)
    bailout: set the bailout value (from 0 to FLT_MAX) (default 10)
    morphxf: set morph x frequency (from -FLT_MAX to FLT_MAX) (default 0.01)
    morphyf: set morph y frequency (from -FLT_MAX to FLT_MAX) (default 0.0123)
    morphamp: set morph amplitude (from -FLT_MAX to FLT_MAX) (default 0)
    outer: set outer coloring mode (from 0 to INT_MAX) (default normalized_iteration_count)
    inner: set inner coloring mode (from 0 to INT_MAX) (default mincol)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mandelbrot)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='mandelbrot', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "maxiter": maxiter,

            "start_x": start_x,

            "start_y": start_y,

            "start_scale": start_scale,

            "end_scale": end_scale,

            "end_pts": end_pts,

            "bailout": bailout,

            "morphxf": morphxf,

            "morphyf": morphyf,

            "morphamp": morphamp,

            "outer": outer,

            "inner": inner,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
























def mergeplanes(



    *streams: VideoStream,




    mapping: Int = Default('-1'),format: Pix_fmt = Default('yuva444p'),map0s: Int = Default('0'),map0p: Int = Default('0'),map1s: Int = Default('0'),map1p: Int = Default('0'),map2s: Int = Default('0'),map2p: Int = Default('0'),map3s: Int = Default('0'),map3p: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    mapping: set input to output plane mapping (from -1 to 8.58993e+08) (default -1)
    format: set output pixel format (default yuva444p)
    map0s: set 1st input to output stream mapping (from 0 to 3) (default 0)
    map0p: set 1st input to output plane mapping (from 0 to 3) (default 0)
    map1s: set 2nd input to output stream mapping (from 0 to 3) (default 0)
    map1p: set 2nd input to output plane mapping (from 0 to 3) (default 0)
    map2s: set 3rd input to output stream mapping (from 0 to 3) (default 0)
    map2p: set 3rd input to output plane mapping (from 0 to 3) (default 0)
    map3s: set 4th input to output stream mapping (from 0 to 3) (default 0)
    map3p: set 4th input to output plane mapping (from 0 to 3) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mergeplanes)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='mergeplanes', typings_input='[StreamType.video] * int(max(hex(int(mapping))[2::2]))', typings_output=('video',)),



        *streams,



        **merge({

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

        },
        extra_options,


        )
    )
    return filter_node.video(0)














def mix(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),weights: String = Default('1 1'),scale: Float = Default('0'),planes: Flags = Default('F'),duration: Int| Literal["longest","shortest","first"] | Default = Default('longest'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    inputs: set number of inputs (from 2 to 32767) (default 2)
    weights: set weight for each input (default "1 1")
    scale: set scale (from 0 to 32767) (default 0)
    planes: set what planes to filter (default F)
    duration: how to determine end of stream (from 0 to 2) (default longest)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mix)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='mix', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "weights": weights,

            "scale": scale,

            "planes": planes,

            "duration": duration,

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)










def movie(





    *,
    filename: String = Default(None),format_name: String = Default(None),stream_index: Int = Default('-1'),seek_point: Double = Default('0'),streams: String = Default(None),loop: Int = Default('1'),discontinuity: Duration = Default('0'),dec_threads: Int = Default('0'),format_opts: Dictionary = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> FilterNode:
    """

Inputs:


Args:
    filename:
    format_name: set format name
    stream_index: set stream index (from -1 to INT_MAX) (default -1)
    seek_point: set seekpoint (seconds) (from 0 to 9.22337e+12) (default 0)
    streams: set streams
    loop: set loop count (from 0 to INT_MAX) (default 1)
    discontinuity: set discontinuity threshold (default 0)
    dec_threads: set the number of threads for decoding (from 0 to INT_MAX) (default 0)
    format_opts: set format options for the opened file
    extra_options: Extra options for the filter

Returns:
    filter_node: the filter node


References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#movie)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='movie', typings_input="[StreamType.video] * len(streams.split('+'))", typings_output="[StreamType.video] * len(streams.split('+'))"),





        **merge({

            "filename": filename,

            "format_name": format_name,

            "stream_index": stream_index,

            "seek_point": seek_point,

            "streams": streams,

            "loop": loop,

            "discontinuity": discontinuity,

            "dec_threads": dec_threads,

            "format_opts": format_opts,

        },
        extra_options,


        )
    )

    return filter_node








def mptestsrc(





    *,
    rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),test: Int| Literal["dc_luma","dc_chroma","freq_luma","freq_chroma","amp_luma","amp_chroma","cbp","mv","ring1","ring2","all"] | Default = Default('all'),max_frames: Int64 = Default('30'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    test: set test to perform (from 0 to INT_MAX) (default all)
    max_frames: Set the maximum number of frames generated for each test (from 1 to I64_MAX) (default 30)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mptestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='mptestsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "rate": rate,

            "duration": duration,

            "test": test,

            "max_frames": max_frames,

        },
        extra_options,


        )
    )
    return filter_node.video(0)


























def nullsrc(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='nullsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
















def pal100bars(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='pal100bars', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def pal75bars(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='pal75bars', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)




























def premultiply(



    *streams: VideoStream,




    planes: Int = Default('15'),inplace: Boolean = Default('false'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    planes: set planes (from 0 to 15) (default 15)
    inplace: enable inplace mode (default false)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#premultiply)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='premultiply', typings_input='[StreamType.video] + [StreamType.video] if inplace else []', typings_output=('video',)),



        *streams,



        **merge({

            "planes": planes,

            "inplace": inplace,

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)






































def rgbtestsrc(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),complement: Boolean = Default('false'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    complement: set complement colors (default false)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='rgbtestsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "complement": complement,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
















































































def sierpinski(





    *,
    size: Image_size = Default('640x480'),rate: Video_rate = Default('25'),seed: Int64 = Default('-1'),jump: Int = Default('100'),type: Int| Literal["carpet","triangle"] | Default = Default('carpet'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    size: set frame size (default "640x480")
    rate: set frame rate (default "25")
    seed: set the seed (from -1 to UINT32_MAX) (default -1)
    jump: set the jump (from 1 to 10000) (default 100)
    type: set fractal type (from 0 to 1) (default carpet)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sierpinski)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='sierpinski', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "seed": seed,

            "jump": jump,

            "type": type,

        },
        extra_options,


        )
    )
    return filter_node.video(0)








def signature(



    *streams: VideoStream,




    detectmode: Int| Literal["off","full","fast"] | Default = Default('off'),nb_inputs: Int = Auto('len(streams)'),filename: String = Default(''),format: Int| Literal["binary","xml"] | Default = Default('binary'),th_d: Int = Default('9000'),th_dc: Int = Default('60000'),th_xh: Int = Default('116'),th_di: Int = Default('0'),th_it: Double = Default('0.5'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    detectmode: set the detectmode (from 0 to 2) (default off)
    nb_inputs: number of inputs (from 1 to INT_MAX) (default 1)
    filename: filename for output files (default "")
    format: set output format (from 0 to 1) (default binary)
    th_d: threshold to detect one word as similar (from 1 to INT_MAX) (default 9000)
    th_dc: threshold to detect all words as similar (from 1 to INT_MAX) (default 60000)
    th_xh: threshold to detect frames as similar (from 1 to INT_MAX) (default 116)
    th_di: minimum length of matching sequence in frames (from 0 to INT_MAX) (default 0)
    th_it: threshold for relation of good to all frames (from 0 to 1) (default 0.5)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#signature)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='signature', typings_input='[StreamType.video] * int(nb_inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "detectmode": detectmode,

            "nb_inputs": nb_inputs,

            "filename": filename,

            "format": format,

            "th_d": th_d,

            "th_dc": th_dc,

            "th_xh": th_xh,

            "th_di": th_di,

            "th_it": th_it,

        },
        extra_options,


        )
    )
    return filter_node.video(0)










def sinc(





    *,
    sample_rate: Int = Default('44100'),nb_samples: Int = Default('1024'),hp: Float = Default('0'),lp: Float = Default('0'),phase: Float = Default('50'),beta: Float = Default('-1'),att: Float = Default('120'),round: Boolean = Default('false'),hptaps: Int = Default('0'),lptaps: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    sample_rate: set sample rate (from 1 to INT_MAX) (default 44100)
    nb_samples: set the number of samples per requested frame (from 1 to INT_MAX) (default 1024)
    hp: set high-pass filter frequency (from 0 to INT_MAX) (default 0)
    lp: set low-pass filter frequency (from 0 to INT_MAX) (default 0)
    phase: set filter phase response (from 0 to 100) (default 50)
    beta: set kaiser window beta (from -1 to 256) (default -1)
    att: set stop-band attenuation (from 40 to 180) (default 120)
    round: enable rounding (default false)
    hptaps: set number of taps for high-pass filter (from 0 to 32768) (default 0)
    lptaps: set number of taps for low-pass filter (from 0 to 32768) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sinc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='sinc', typings_input=(), typings_output=('audio',)),





        **merge({

            "sample_rate": sample_rate,

            "nb_samples": nb_samples,

            "hp": hp,

            "lp": lp,

            "phase": phase,

            "beta": beta,

            "att": att,

            "round": round,

            "hptaps": hptaps,

            "lptaps": lptaps,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)






def sine(





    *,
    frequency: Double = Default('440'),beep_factor: Double = Default('0'),sample_rate: Int = Default('44100'),duration: Duration = Default('0'),samples_per_frame: String = Default('1024'),


    extra_options: dict[str, Any] | None = None,
)-> AudioStream:
    """

Inputs:


Args:
    frequency: set the sine frequency (from 0 to DBL_MAX) (default 440)
    beep_factor: set the beep frequency factor (from 0 to DBL_MAX) (default 0)
    sample_rate: set the sample rate (from 1 to INT_MAX) (default 44100)
    duration: set the audio duration (default 0)
    samples_per_frame: set the number of samples per frame (default "1024")
    extra_options: Extra options for the filter

Returns:
    default: the audio stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sine)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='sine', typings_input=(), typings_output=('audio',)),





        **merge({

            "frequency": frequency,

            "beep_factor": beep_factor,

            "sample_rate": sample_rate,

            "duration": duration,

            "samples_per_frame": samples_per_frame,

        },
        extra_options,


        )
    )
    return filter_node.audio(0)










def smptebars(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='smptebars', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def smptehdbars(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='smptehdbars', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)


























def streamselect(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),map: String = Default(None),


    extra_options: dict[str, Any] | None = None,
)-> FilterNode:
    """

Inputs:


Args:
    inputs: number of input streams (from 2 to INT_MAX) (default 2)
    map: input indexes to remap to outputs
    extra_options: Extra options for the filter

Returns:
    filter_node: the filter node


References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='streamselect', typings_input='[StreamType.video] * int(inputs)', typings_output="[StreamType.video] * len(re.findall(r'\\d+', str(map)))"),



        *streams,



        **merge({

            "inputs": inputs,

            "map": map,

        },
        extra_options,


        )
    )

    return filter_node






















def testsrc(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),decimals: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    decimals: set number of decimals to show (from 0 to 17) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='testsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "decimals": decimals,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def testsrc2(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),alpha: Int = Default('255'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    alpha: set global alpha (opacity) (from 0 to 255) (default 255)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='testsrc2', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "alpha": alpha,

        },
        extra_options,


        )
    )
    return filter_node.video(0)








































def unpremultiply(



    *streams: VideoStream,




    planes: Int = Default('15'),inplace: Boolean = Default('false'),


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    planes: set planes (from 0 to 15) (default 15)
    inplace: enable inplace mode (default false)
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#unpremultiply)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='unpremultiply', typings_input='[StreamType.video] + ([StreamType.video] if inplace else [])', typings_output=('video',)),



        *streams,



        **merge({

            "planes": planes,

            "inplace": inplace,

        },
        extra_options,


        timeline_options,

        )
    )
    return filter_node.video(0)












































def vstack(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),shortest: Boolean = Default('false'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    shortest: force termination when the shortest input terminates (default false)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vstack)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='vstack', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "shortest": shortest,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def vstack_vaapi(



    *streams: VideoStream,




    inputs: Int = Default('2'),shortest: Boolean = Default('false'),width: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


.. note:: New in FFmpeg 6.0.


Args:
    inputs: Set number of inputs (from 2 to 65535) (default 2)
    shortest: Force termination when the shortest input terminates (default false)
    width: Set output width (0 to use the width of input 0) (from 0 to 65535) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vstack_005fvaapi)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='vstack_vaapi', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "shortest": shortest,

            "width": width,

        },
        extra_options,


        )
    )
    return filter_node.video(0)


















def xmedian(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),planes: Int = Default('15'),percentile: Float = Default('0.5'),

    framesync_options: FFMpegFrameSyncOption | None = None,


    timeline_options: FFMpegTimelineOption | None = None,

    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    inputs: set number of inputs (from 3 to 255) (default 3)
    planes: set planes to filter (from 0 to 15) (default 15)
    percentile: set percentile (from 0 to 1) (default 0.5)
    framesync_options: Framesync options
    timeline_options: Timeline options
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xmedian)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='xmedian', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "planes": planes,

            "percentile": percentile,

        },
        extra_options,

        framesync_options,


        timeline_options,

        )
    )
    return filter_node.video(0)






def xstack(



    *streams: VideoStream,




    inputs: Int = Auto('len(streams)'),layout: String = Default(None),grid: Image_size = Default(None),shortest: Boolean = Default('false'),fill: String = Default('none'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


Args:
    inputs: set number of inputs (from 2 to INT_MAX) (default 2)
    layout: set custom layout
    grid: set fixed size grid layout
    shortest: force termination when the shortest input terminates (default false)
    fill: set the color for unused pixels (default "none")
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xstack)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='xstack', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "layout": layout,

            "grid": grid,

            "shortest": shortest,

            "fill": fill,

        },
        extra_options,


        )
    )
    return filter_node.video(0)






def xstack_vaapi(



    *streams: VideoStream,




    inputs: Int = Default('2'),shortest: Boolean = Default('false'),layout: String = Default(None),grid: Image_size = Default(None),grid_tile_size: Image_size = Default(None),fill: String = Default('none'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


.. note:: New in FFmpeg 6.0.


Args:
    inputs: Set number of inputs (from 2 to 65535) (default 2)
    shortest: Force termination when the shortest input terminates (default false)
    layout: Set custom layout
    grid: set fixed size grid layout
    grid_tile_size: set tile size in grid layout
    fill: Set the color for unused pixels (default "none")
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xstack_005fvaapi)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='xstack_vaapi', typings_input='[StreamType.video] * int(inputs)', typings_output=('video',)),



        *streams,



        **merge({

            "inputs": inputs,

            "shortest": shortest,

            "layout": layout,

            "grid": grid,

            "grid_tile_size": grid_tile_size,

            "fill": fill,

        },
        extra_options,


        )
    )
    return filter_node.video(0)










def yuvtestsrc(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

Inputs:


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allrgb_002c-allyuv_002c-color_002c-colorchart_002c-colorspectrum_002c-haldclutsrc_002c-nullsrc_002c-pal75bars_002c-pal100bars_002c-rgbtestsrc_002c-smptebars_002c-smptehdbars_002c-testsrc_002c-testsrc2_002c-yuvtestsrc)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='yuvtestsrc', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

        },
        extra_options,


        )
    )
    return filter_node.video(0)








def zoneplate(





    *,
    size: Image_size = Default('320x240'),rate: Video_rate = Default('25'),duration: Duration = Default('-0.000001'),sar: Rational = Default('1/1'),precision: Int = Default('10'),xo: Int = Default('0'),yo: Int = Default('0'),to: Int = Default('0'),k0: Int = Default('0'),kx: Int = Default('0'),ky: Int = Default('0'),kt: Int = Default('0'),kxt: Int = Default('0'),kyt: Int = Default('0'),kxy: Int = Default('0'),kx2: Int = Default('0'),ky2: Int = Default('0'),kt2: Int = Default('0'),ku: Int = Default('0'),kv: Int = Default('0'),


    extra_options: dict[str, Any] | None = None,
)-> VideoStream:
    """

slice threading supported


.. note:: New in FFmpeg 6.0.


Args:
    size: set video size (default "320x240")
    rate: set video rate (default "25")
    duration: set video duration (default -0.000001)
    sar: set video sample aspect ratio (from 0 to INT_MAX) (default 1/1)
    precision: set LUT precision (from 4 to 16) (default 10)
    xo: set X-axis offset (from INT_MIN to INT_MAX) (default 0)
    yo: set Y-axis offset (from INT_MIN to INT_MAX) (default 0)
    to: set T-axis offset (from INT_MIN to INT_MAX) (default 0)
    k0: set 0-order phase (from INT_MIN to INT_MAX) (default 0)
    kx: set 1-order X-axis phase (from INT_MIN to INT_MAX) (default 0)
    ky: set 1-order Y-axis phase (from INT_MIN to INT_MAX) (default 0)
    kt: set 1-order T-axis phase (from INT_MIN to INT_MAX) (default 0)
    kxt: set X-axis*T-axis product phase (from INT_MIN to INT_MAX) (default 0)
    kyt: set Y-axis*T-axis product phase (from INT_MIN to INT_MAX) (default 0)
    kxy: set X-axis*Y-axis product phase (from INT_MIN to INT_MAX) (default 0)
    kx2: set 2-order X-axis phase (from INT_MIN to INT_MAX) (default 0)
    ky2: set 2-order Y-axis phase (from INT_MIN to INT_MAX) (default 0)
    kt2: set 2-order T-axis phase (from INT_MIN to INT_MAX) (default 0)
    ku: set 0-order U-color phase (from INT_MIN to INT_MAX) (default 0)
    kv: set 0-order V-color phase (from INT_MIN to INT_MAX) (default 0)
    extra_options: Extra options for the filter

Returns:
    default: the video stream

References:
    [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#zoneplate)

    """
    filter_node = filter_node_factory(
        FFMpegFilterDef(name='zoneplate', typings_input=(), typings_output=('video',)),





        **merge({

            "size": size,

            "rate": rate,

            "duration": duration,

            "sar": sar,

            "precision": precision,

            "xo": xo,

            "yo": yo,

            "to": to,

            "k0": k0,

            "kx": kx,

            "ky": ky,

            "kt": kt,

            "kxt": kxt,

            "kyt": kyt,

            "kxy": kxy,

            "kx2": kx2,

            "ky2": ky2,

            "kt2": kt2,

            "ku": ku,

            "kv": kv,

        },
        extra_options,


        )
    )
    return filter_node.video(0)
