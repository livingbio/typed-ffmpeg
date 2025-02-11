# NOTE: this file is auto-generated, do not modify


from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from ..common.schema import FFMpegFilterDef
from ..dag.factory import filter_node_factory
from ..dag.nodes import FilterableStream, FilterNode
from ..schema import Default
from ..types import (
    Boolean,
    Color,
    Double,
    Duration,
    Flags,
    Float,
    Image_size,
    Int,
    Int64,
    Rational,
    String,
    Video_rate,
)

if TYPE_CHECKING:
    from .video import VideoStream


class AudioStream(FilterableStream):
    def a3dscope(
        self,
        *,
        rate: Video_rate = Default("25"),
        size: Image_size = Default("hd720"),
        fov: Float = Default(90.0),
        roll: Float = Default(0.0),
        pitch: Float = Default(0.0),
        yaw: Float = Default(0.0),
        xzoom: Float = Default(1.0),
        xpos: Float = Default(0.0),
        length: Int = Default(15),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to 3d scope video output.

        Args:
            rate: set video rate (default "25")
            size: set video size (default "hd720")
            fov: set camera FoV (from 40 to 150) (default 90)
            roll: set camera roll (from -180 to 180) (default 0)
            pitch: set camera pitch (from -180 to 180) (default 0)
            yaw: set camera yaw (from -180 to 180) (default 0)
            xzoom: set camera zoom (from 0.01 to 10) (default 1)
            xpos: set camera position (from -60 to 60) (default 0)
            length: set length (from 1 to 60) (default 15)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#a3dscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="a3dscope", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "rate": rate,
                "size": size,
                "fov": fov,
                "roll": roll,
                "pitch": pitch,
                "yaw": yaw,
                "xzoom": xzoom,
                "xpos": xpos,
                "length": length,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def abench(
        self,
        *,
        action: Int | Literal["start", "stop"] | Default = Default("start"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Benchmark part of a filtergraph.

        Args:
            action: set action (from 0 to 1) (default start)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="abench", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "action": action,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def abitscope(
        self,
        *,
        rate: Video_rate = Default("25"),
        size: Image_size = Default("1024x256"),
        colors: String = Default(
            "red|green|blue|yellow|orange|lime|pink|magenta|brown"
        ),
        mode: Int | Literal["bars", "trace"] | Default = Default("bars"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to audio bit scope video output.

        Args:
            rate: set video rate (default "25")
            size: set video size (default "1024x256")
            colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
            mode: set output mode (from 0 to 1) (default bars)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#abitscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="abitscope", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "rate": rate,
                "size": size,
                "colors": colors,
                "mode": mode,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def acompressor(
        self,
        *,
        level_in: Double = Default(1.0),
        mode: Int | Literal["downward", "upward"] | Default = Default("downward"),
        threshold: Double = Default(0.125),
        ratio: Double = Default(2.0),
        attack: Double = Default(20.0),
        release: Double = Default(250.0),
        makeup: Double = Default(1.0),
        knee: Double = Default(2.82843),
        link: Int | Literal["average", "maximum"] | Default = Default("average"),
        detection: Int | Literal["peak", "rms"] | Default = Default("rms"),
        level_sc: Double = Default(1.0),
        mix: Double = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio compressor.

        Args:
            level_in: set input gain (from 0.015625 to 64) (default 1)
            mode: set mode (from 0 to 1) (default downward)
            threshold: set threshold (from 0.000976563 to 1) (default 0.125)
            ratio: set ratio (from 1 to 20) (default 2)
            attack: set attack (from 0.01 to 2000) (default 20)
            release: set release (from 0.01 to 9000) (default 250)
            makeup: set make up gain (from 1 to 64) (default 1)
            knee: set knee (from 1 to 8) (default 2.82843)
            link: set link type (from 0 to 1) (default average)
            detection: set detection (from 0 to 1) (default rms)
            level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
            mix: set mix (from 0 to 1) (default 1)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acompressor)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acompressor", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
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
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def acontrast(
        self,
        *,
        contrast: Float = Default(33.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Simple audio dynamic range compression/expansion filter.

        Args:
            contrast: set contrast (from 0 to 100) (default 33)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acontrast)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acontrast", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "contrast": contrast,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def acopy(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Copy the input audio unchanged to the output.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acopy)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acopy", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def acrossfade(
        self,
        _crossfade1: AudioStream,
        *,
        nb_samples: Int = Default(44100),
        duration: Duration = Default(0.0),
        overlap: Boolean = Default(True),
        curve1: Int
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
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | Default = Default("tri"),
        curve2: Int
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
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | Default = Default("tri"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Cross fade two input audio streams.

        Args:
            nb_samples: set number of samples for cross fade duration (from 1 to 2.14748e+08) (default 44100)
            duration: set cross fade duration (default 0)
            overlap: overlap 1st stream end with 2nd stream start (default true)
            curve1: set fade curve type for 1st stream (from -1 to 22) (default tri)
            curve2: set fade curve type for 2nd stream (from -1 to 22) (default tri)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acrossfade)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acrossfade",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _crossfade1,
            **{
                "nb_samples": nb_samples,
                "duration": duration,
                "overlap": overlap,
                "curve1": curve1,
                "curve2": curve2,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def acrossover(
        self,
        *,
        split: String = Default("500"),
        order: Int
        | Literal[
            "2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"
        ]
        | Default = Default("4th"),
        level: Float = Default(1.0),
        gain: String = Default("1.f"),
        precision: Int | Literal["auto", "float", "double"] | Default = Default("auto"),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Split audio into per-bands streams.

        Args:
            split: set split frequencies (default "500")
            order: set filter order (from 0 to 9) (default 4th)
            level: set input gain (from 0 to 1) (default 1)
            gain: set output bands gain (default "1.f")
            precision: set processing precision (from 0 to 2) (default auto)

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acrossover)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acrossover",
                typings_input=("audio",),
                typings_output="[StreamType.audio] * len(re.split(r'[ |]+', str(split)))",
            ),
            self,
            **{
                "split": split,
                "order": order,
                "level": level,
                "gain": gain,
                "precision": precision,
            }
            | (extra_options or {}),
        )

        return filter_node

    def acrusher(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        bits: Double = Default(8.0),
        mix: Double = Default(0.5),
        mode: Int | Literal["lin", "log"] | Default = Default("lin"),
        dc: Double = Default(1.0),
        aa: Double = Default(0.5),
        samples: Double = Default(1.0),
        lfo: Boolean = Default(False),
        lforange: Double = Default(20.0),
        lforate: Double = Default(0.3),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Reduce audio bit resolution.

        Args:
            level_in: set level in (from 0.015625 to 64) (default 1)
            level_out: set level out (from 0.015625 to 64) (default 1)
            bits: set bit reduction (from 1 to 64) (default 8)
            mix: set mix (from 0 to 1) (default 0.5)
            mode: set mode (from 0 to 1) (default lin)
            dc: set DC (from 0.25 to 4) (default 1)
            aa: set anti-aliasing (from 0 to 1) (default 0.5)
            samples: set sample reduction (from 1 to 250) (default 1)
            lfo: enable LFO (default false)
            lforange: set LFO depth (from 1 to 250) (default 20)
            lforate: set LFO rate (from 0.01 to 200) (default 0.3)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acrusher)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acrusher", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
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
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def acue(
        self,
        *,
        cue: Int64 = Default(0),
        preroll: Duration = Default(0.0),
        buffer: Duration = Default(0.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Delay filtering to match a cue.

        Args:
            cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
            preroll: preroll duration in seconds (default 0)
            buffer: buffer duration in seconds (default 0)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#acue)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="acue", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adeclick(
        self,
        *,
        window: Double = Default(55.0),
        overlap: Double = Default(75.0),
        arorder: Double = Default(2.0),
        threshold: Double = Default(2.0),
        burst: Double = Default(2.0),
        method: Int | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remove impulsive noise from input audio.

        Args:
            window: set window size (from 10 to 100) (default 55)
            overlap: set window overlap (from 50 to 95) (default 75)
            arorder: set autoregression order (from 0 to 25) (default 2)
            threshold: set threshold (from 1 to 100) (default 2)
            burst: set burst fusion (from 0 to 10) (default 2)
            method: set overlap method (from 0 to 1) (default add)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adeclick)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adeclick", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "burst": burst,
                "method": method,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adeclip(
        self,
        *,
        window: Double = Default(55.0),
        overlap: Double = Default(75.0),
        arorder: Double = Default(8.0),
        threshold: Double = Default(10.0),
        hsize: Int = Default(1000),
        method: Int | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remove clipping from input audio.

        Args:
            window: set window size (from 10 to 100) (default 55)
            overlap: set window overlap (from 50 to 95) (default 75)
            arorder: set autoregression order (from 0 to 25) (default 8)
            threshold: set threshold (from 1 to 100) (default 10)
            hsize: set histogram size (from 100 to 9999) (default 1000)
            method: set overlap method (from 0 to 1) (default add)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adeclip)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adeclip", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "hsize": hsize,
                "method": method,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adecorrelate(
        self,
        *,
        stages: Int = Default(6),
        seed: Int64 = Default(-1),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply decorrelation to input audio.

        Args:
            stages: set filtering stages (from 1 to 16) (default 6)
            seed: set random seed (from -1 to UINT32_MAX) (default -1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adecorrelate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adecorrelate", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "stages": stages,
                "seed": seed,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adelay(
        self,
        *,
        delays: String = Default(None),
        all: Boolean = Default(False),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Delay one or more audio channels.

        Args:
            delays: set list of delays for each channel
            all: use last available delay for remained channels (default false)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adelay)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adelay", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "delays": delays,
                "all": all,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adenorm(
        self,
        *,
        level: Double = Default(-351.0),
        type: Int | Literal["dc", "ac", "square", "pulse"] | Default = Default("dc"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remedy denormals by adding extremely low-level noise.

        Args:
            level: set level (from -451 to -90) (default -351)
            type: set type (from 0 to 3) (default dc)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adenorm)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adenorm", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level": level,
                "type": type,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aderivative(
        self,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Compute derivative of input audio.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aderivative", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adrawgraph(
        self,
        *,
        m1: String = Default(""),
        fg1: String = Default("0xffff0000"),
        m2: String = Default(""),
        fg2: String = Default("0xff00ff00"),
        m3: String = Default(""),
        fg3: String = Default("0xffff00ff"),
        m4: String = Default(""),
        fg4: String = Default("0xffffff00"),
        bg: Color = Default("white"),
        min: Float = Default(-1.0),
        max: Float = Default(1.0),
        mode: Int | Literal["bar", "dot", "line"] | Default = Default("line"),
        slide: Int
        | Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | Default = Default("frame"),
        size: Image_size = Default("900x256"),
        rate: Video_rate = Default("25"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Draw a graph using input audio metadata.

        Args:
            m1: set 1st metadata key (default "")
            fg1: set 1st foreground color expression (default "0xffff0000")
            m2: set 2nd metadata key (default "")
            fg2: set 2nd foreground color expression (default "0xff00ff00")
            m3: set 3rd metadata key (default "")
            fg3: set 3rd foreground color expression (default "0xffff00ff")
            m4: set 4th metadata key (default "")
            fg4: set 4th foreground color expression (default "0xffffff00")
            bg: set background color (default "white")
            min: set minimal value (from INT_MIN to INT_MAX) (default -1)
            max: set maximal value (from INT_MIN to INT_MAX) (default 1)
            mode: set graph mode (from 0 to 2) (default line)
            slide: set slide mode (from 0 to 4) (default frame)
            size: set graph size (default "900x256")
            rate: set video rate (default "25")

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adrawgraph)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adrawgraph", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "bg": bg,
                "min": min,
                "max": max,
                "mode": mode,
                "slide": slide,
                "size": size,
                "rate": rate,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def adrc(
        self,
        *,
        transfer: String = Default("p"),
        attack: Double = Default(50.0),
        release: Double = Default(100.0),
        channels: String = Default("all"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Spectral Dynamic Range Controller.

        Args:
            transfer: set the transfer expression (default "p")
            attack: set the attack (from 1 to 1000) (default 50)
            release: set the release (from 5 to 2000) (default 100)
            channels: set channels to filter (default "all")
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adrc)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adrc", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "transfer": transfer,
                "attack": attack,
                "release": release,
                "channels": channels,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adynamicequalizer(
        self,
        *,
        threshold: Double = Default(0.0),
        dfrequency: Double = Default(1000.0),
        dqfactor: Double = Default(1.0),
        tfrequency: Double = Default(1000.0),
        tqfactor: Double = Default(1.0),
        attack: Double = Default(20.0),
        release: Double = Default(200.0),
        ratio: Double = Default(1.0),
        makeup: Double = Default(0.0),
        range: Double = Default(50.0),
        mode: Int | Literal["listen", "cut", "boost"] | Default = Default("cut"),
        dftype: Int
        | Literal["bandpass", "lowpass", "highpass", "peak"]
        | Default = Default("bandpass"),
        tftype: Int | Literal["bell", "lowshelf", "highshelf"] | Default = Default(
            "bell"
        ),
        direction: Int | Literal["downward", "upward"] | Default = Default("downward"),
        auto: Int | Literal["disabled", "off", "on"] | Default = Default("disabled"),
        precision: Int | Literal["auto", "float", "double"] | Default = Default("auto"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Dynamic Equalization of input audio.

        Args:
            threshold: set detection threshold (from 0 to 100) (default 0)
            dfrequency: set detection frequency (from 2 to 1e+06) (default 1000)
            dqfactor: set detection Q factor (from 0.001 to 1000) (default 1)
            tfrequency: set target frequency (from 2 to 1e+06) (default 1000)
            tqfactor: set target Q factor (from 0.001 to 1000) (default 1)
            attack: set attack duration (from 1 to 2000) (default 20)
            release: set release duration (from 1 to 2000) (default 200)
            ratio: set ratio factor (from 0 to 30) (default 1)
            makeup: set makeup gain (from 0 to 100) (default 0)
            range: set max gain (from 1 to 200) (default 50)
            mode: set mode (from -1 to 1) (default cut)
            dftype: set detection filter type (from 0 to 3) (default bandpass)
            tftype: set target filter type (from 0 to 2) (default bell)
            direction: set direction (from 0 to 1) (default downward)
            auto: set auto threshold (from -1 to 1) (default disabled)
            precision: set processing precision (from 0 to 2) (default auto)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adynamicequalizer",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
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
                "direction": direction,
                "auto": auto,
                "precision": precision,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def adynamicsmooth(
        self,
        *,
        sensitivity: Double = Default(2.0),
        basefreq: Double = Default(22050.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Dynamic Smoothing of input audio.

        Args:
            sensitivity: set smooth sensitivity (from 0 to 1e+06) (default 2)
            basefreq: set base frequency (from 2 to 1e+06) (default 22050)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="adynamicsmooth",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "sensitivity": sensitivity,
                "basefreq": basefreq,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aecho(
        self,
        *,
        in_gain: Float = Default(0.6),
        out_gain: Float = Default(0.3),
        delays: String = Default("1000"),
        decays: String = Default("0.5"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Add echoing to the audio.

        Args:
            in_gain: set signal input gain (from 0 to 1) (default 0.6)
            out_gain: set signal output gain (from 0 to 1) (default 0.3)
            delays: set list of signal delays (default "1000")
            decays: set list of signal decays (default "0.5")

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aecho)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aecho", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aemphasis(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        mode: Int | Literal["reproduction", "production"] | Default = Default(
            "reproduction"
        ),
        type: Int
        | Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"]
        | Default = Default("cd"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio emphasis.

        Args:
            level_in: set input gain (from 0 to 64) (default 1)
            level_out: set output gain (from 0 to 64) (default 1)
            mode: set filter mode (from 0 to 1) (default reproduction)
            type: set filter type (from 0 to 8) (default cd)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aemphasis)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aemphasis", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "type": type,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aeval(
        self,
        *,
        exprs: String = Default(None),
        channel_layout: String = Default(None),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Filter audio signal according to a specified expression.

        Args:
            exprs: set the '|'-separated list of channels expressions
            channel_layout: set channel layout
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aeval)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aeval", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "exprs": exprs,
                "channel_layout": channel_layout,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aexciter(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        amount: Double = Default(1.0),
        drive: Double = Default(8.5),
        blend: Double = Default(0.0),
        freq: Double = Default(7500.0),
        ceil: Double = Default(9999.0),
        listen: Boolean = Default(False),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Enhance high frequency part of audio.

        Args:
            level_in: set level in (from 0 to 64) (default 1)
            level_out: set level out (from 0 to 64) (default 1)
            amount: set amount (from 0 to 64) (default 1)
            drive: set harmonics (from 0.1 to 10) (default 8.5)
            blend: set blend harmonics (from -10 to 10) (default 0)
            freq: set scope (from 2000 to 12000) (default 7500)
            ceil: set ceiling (from 9999 to 20000) (default 9999)
            listen: enable listen mode (default false)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aexciter)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aexciter", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "amount": amount,
                "drive": drive,
                "blend": blend,
                "freq": freq,
                "ceil": ceil,
                "listen": listen,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def afade(
        self,
        *,
        type: Int | Literal["in", "out"] | Default = Default("in"),
        start_sample: Int64 = Default(0),
        nb_samples: Int64 = Default(44100),
        start_time: Duration = Default(0.0),
        duration: Duration = Default(0.0),
        curve: Int
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
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | Default = Default("tri"),
        silence: Double = Default(0.0),
        unity: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Fade in/out input audio.

        Args:
            type: set the fade direction (from 0 to 1) (default in)
            start_sample: set number of first sample to start fading (from 0 to I64_MAX) (default 0)
            nb_samples: set number of samples for fade duration (from 1 to I64_MAX) (default 44100)
            start_time: set time to start fading (default 0)
            duration: set fade duration (default 0)
            curve: set fade curve type (from -1 to 22) (default tri)
            silence: set the silence gain (from 0 to 1) (default 0)
            unity: set the unity gain (from 0 to 1) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afade)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="afade", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "type": type,
                "start_sample": start_sample,
                "nb_samples": nb_samples,
                "start_time": start_time,
                "duration": duration,
                "curve": curve,
                "silence": silence,
                "unity": unity,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def afftdn(
        self,
        *,
        noise_reduction: Float = Default(12.0),
        noise_floor: Float = Default(-50.0),
        noise_type: Int
        | Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | Default = Default("white"),
        band_noise: String = Default(None),
        residual_floor: Float = Default(-38.0),
        track_noise: Boolean = Default(False),
        track_residual: Boolean = Default(False),
        output_mode: Int
        | Literal["input", "i", "output", "o", "noise", "n"]
        | Default = Default("output"),
        adaptivity: Float = Default(0.5),
        floor_offset: Float = Default(1.0),
        noise_link: Int | Literal["none", "min", "max", "average"] | Default = Default(
            "min"
        ),
        band_multiplier: Float = Default(1.25),
        sample_noise: Int
        | Literal["none", "start", "begin", "stop", "end"]
        | Default = Default("none"),
        gain_smooth: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Denoise audio samples using FFT.

        Args:
            noise_reduction: set the noise reduction (from 0.01 to 97) (default 12)
            noise_floor: set the noise floor (from -80 to -20) (default -50)
            noise_type: set the noise type (from 0 to 3) (default white)
            band_noise: set the custom bands noise
            residual_floor: set the residual floor (from -80 to -20) (default -38)
            track_noise: track noise (default false)
            track_residual: track residual (default false)
            output_mode: set output mode (from 0 to 2) (default output)
            adaptivity: set adaptivity factor (from 0 to 1) (default 0.5)
            floor_offset: set noise floor offset factor (from -2 to 2) (default 1)
            noise_link: set the noise floor link (from 0 to 3) (default min)
            band_multiplier: set band multiplier (from 0.2 to 5) (default 1.25)
            sample_noise: set sample noise mode (from 0 to 2) (default none)
            gain_smooth: set gain smooth radius (from 0 to 50) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afftdn)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="afftdn", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
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
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def afftfilt(
        self,
        *,
        real: String = Default("re"),
        imag: String = Default("im"),
        win_size: Int = Default(4096),
        win_func: Int
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
        | Default = Default("hann"),
        overlap: Float = Default(0.75),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply arbitrary expressions to samples in frequency domain.

        Args:
            real: set channels real expressions (default "re")
            imag: set channels imaginary expressions (default "im")
            win_size: set window size (from 16 to 131072) (default 4096)
            win_func: set window function (from 0 to 20) (default hann)
            overlap: set window overlap (from 0 to 1) (default 0.75)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afftfilt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="afftfilt", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "real": real,
                "imag": imag,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aformat(
        self,
        *,
        sample_fmts: String = Default(None),
        sample_rates: String = Default(None),
        channel_layouts: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Convert the input audio to one of the specified formats.

        Args:
            sample_fmts: A '|'-separated list of sample formats.
            sample_rates: A '|'-separated list of sample rates.
            channel_layouts: A '|'-separated list of channel layouts.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aformat)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aformat", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "sample_fmts": sample_fmts,
                "sample_rates": sample_rates,
                "channel_layouts": channel_layouts,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def afreqshift(
        self,
        *,
        shift: Double = Default(0.0),
        level: Double = Default(1.0),
        order: Int = Default(8),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply frequency shifting to input audio.

        Args:
            shift: set frequency shift (from -2.14748e+09 to INT_MAX) (default 0)
            level: set output level (from 0 to 1) (default 1)
            order: set filter order (from 1 to 16) (default 8)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afreqshift)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="afreqshift", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "shift": shift,
                "level": level,
                "order": order,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def afwtdn(
        self,
        *,
        sigma: Double = Default(0.0),
        levels: Int = Default(10),
        wavet: Int
        | Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"]
        | Default = Default("sym10"),
        percent: Double = Default(85.0),
        profile: Boolean = Default(False),
        adaptive: Boolean = Default(False),
        samples: Int = Default(8192),
        softness: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Denoise audio stream using Wavelets.

        Args:
            sigma: set noise sigma (from 0 to 1) (default 0)
            levels: set number of wavelet levels (from 1 to 12) (default 10)
            wavet: set wavelet type (from 0 to 6) (default sym10)
            percent: set percent of full denoising (from 0 to 100) (default 85)
            profile: profile noise (default false)
            adaptive: adaptive profiling of noise (default false)
            samples: set frame size in number of samples (from 512 to 65536) (default 8192)
            softness: set thresholding softness (from 0 to 10) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#afwtdn)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="afwtdn", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "sigma": sigma,
                "levels": levels,
                "wavet": wavet,
                "percent": percent,
                "profile": profile,
                "adaptive": adaptive,
                "samples": samples,
                "softness": softness,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def agate(
        self,
        *,
        level_in: Double = Default(1.0),
        mode: Int | Literal["downward", "upward"] | Default = Default("downward"),
        range: Double = Default(0.06125),
        threshold: Double = Default(0.125),
        ratio: Double = Default(2.0),
        attack: Double = Default(20.0),
        release: Double = Default(250.0),
        makeup: Double = Default(1.0),
        knee: Double = Default(2.82843),
        detection: Int | Literal["peak", "rms"] | Default = Default("rms"),
        link: Int | Literal["average", "maximum"] | Default = Default("average"),
        level_sc: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio gate.

        Args:
            level_in: set input level (from 0.015625 to 64) (default 1)
            mode: set mode (from 0 to 1) (default downward)
            range: set max gain reduction (from 0 to 1) (default 0.06125)
            threshold: set threshold (from 0 to 1) (default 0.125)
            ratio: set ratio (from 1 to 9000) (default 2)
            attack: set attack (from 0.01 to 9000) (default 20)
            release: set release (from 0.01 to 9000) (default 250)
            makeup: set makeup gain (from 1 to 64) (default 1)
            knee: set knee (from 1 to 8) (default 2.82843)
            detection: set detection (from 0 to 1) (default rms)
            link: set link (from 0 to 1) (default average)
            level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#agate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="agate", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
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
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def agraphmonitor(
        self,
        *,
        size: Image_size = Default("hd720"),
        opacity: Float = Default(0.9),
        mode: Flags
        | Literal["full", "compact", "nozero", "noeof", "nodisabled"]
        | Default = Default("0"),
        flags: Flags
        | Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ]
        | Default = Default("all+queue"),
        rate: Video_rate = Default("25"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Show various filtergraph stats.

        Args:
            size: set monitor size (default "hd720")
            opacity: set video opacity (from 0 to 1) (default 0.9)
            mode: set mode (default 0)
            flags: set flags (default all+queue)
            rate: set video rate (default "25")

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#agraphmonitor)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="agraphmonitor",
                typings_input=("audio",),
                typings_output=("video",),
            ),
            self,
            **{
                "size": size,
                "opacity": opacity,
                "mode": mode,
                "flags": flags,
                "rate": rate,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def ahistogram(
        self,
        *,
        dmode: Int | Literal["single", "separate"] | Default = Default("single"),
        rate: Video_rate = Default("25"),
        size: Image_size = Default("hd720"),
        scale: Int | Literal["log", "sqrt", "cbrt", "lin", "rlog"] | Default = Default(
            "log"
        ),
        ascale: Int | Literal["log", "lin"] | Default = Default("log"),
        acount: Int = Default(1),
        rheight: Float = Default(0.1),
        slide: Int | Literal["replace", "scroll"] | Default = Default("replace"),
        hmode: Int | Literal["abs", "sign"] | Default = Default("abs"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to histogram video output.

        Args:
            dmode: set method to display channels (from 0 to 1) (default single)
            rate: set video rate (default "25")
            size: set video size (default "hd720")
            scale: set display scale (from 0 to 4) (default log)
            ascale: set amplitude scale (from 0 to 1) (default log)
            acount: how much frames to accumulate (from -1 to 100) (default 1)
            rheight: set histogram ratio of window height (from 0 to 1) (default 0.1)
            slide: set sonogram sliding (from 0 to 1) (default replace)
            hmode: set histograms mode (from 0 to 1) (default abs)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ahistogram)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ahistogram", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "dmode": dmode,
                "rate": rate,
                "size": size,
                "scale": scale,
                "ascale": ascale,
                "acount": acount,
                "rheight": rheight,
                "slide": slide,
                "hmode": hmode,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def aiir(
        self,
        *,
        zeros: String = Default("1+0i 1-0i"),
        poles: String = Default("1+0i 1-0i"),
        gains: String = Default("1|1"),
        dry: Double = Default(1.0),
        wet: Double = Default(1.0),
        format: Int
        | Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"]
        | Default = Default("zp"),
        process: Int | Literal["d", "s", "p"] | Default = Default("s"),
        precision: Int | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        e: Int | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        normalize: Boolean = Default(True),
        mix: Double = Default(1.0),
        response: Boolean = Default(False),
        channel: Int = Default(0),
        size: Image_size = Default("hd720"),
        rate: Video_rate = Default("25"),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Apply Infinite Impulse Response filter with supplied coefficients.

        Args:
            zeros: set B/numerator/zeros/reflection coefficients (default "1+0i 1-0i")
            poles: set A/denominator/poles/ladder coefficients (default "1+0i 1-0i")
            gains: set channels gains (default "1|1")
            dry: set dry gain (from 0 to 1) (default 1)
            wet: set wet gain (from 0 to 1) (default 1)
            format: set coefficients format (from -2 to 4) (default zp)
            process: set kind of processing (from 0 to 2) (default s)
            precision: set filtering precision (from 0 to 3) (default dbl)
            e: set precision (from 0 to 3) (default dbl)
            normalize: normalize coefficients (default true)
            mix: set mix (from 0 to 1) (default 1)
            response: show IR frequency response (default false)
            channel: set IR channel to display frequency response (from 0 to 1024) (default 0)
            size: set video size (default "hd720")
            rate: set video rate (default "25")

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aiir)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aiir",
                typings_input=("audio",),
                typings_output="[StreamType.audio] + [StreamType.video] if response else []",
            ),
            self,
            **{
                "zeros": zeros,
                "poles": poles,
                "gains": gains,
                "dry": dry,
                "wet": wet,
                "format": format,
                "process": process,
                "precision": precision,
                "e": e,
                "normalize": normalize,
                "mix": mix,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
            }
            | (extra_options or {}),
        )

        return filter_node

    def aintegral(
        self,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Compute integral of input audio.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aintegral", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def alatency(
        self,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Report audio filtering latency.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="alatency", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def alimiter(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        limit: Double = Default(1.0),
        attack: Double = Default(5.0),
        release: Double = Default(50.0),
        asc: Boolean = Default(False),
        asc_level: Double = Default(0.5),
        level: Boolean = Default(True),
        latency: Boolean = Default(False),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio lookahead limiter.

        Args:
            level_in: set input level (from 0.015625 to 64) (default 1)
            level_out: set output level (from 0.015625 to 64) (default 1)
            limit: set limit (from 0.0625 to 1) (default 1)
            attack: set attack (from 0.1 to 80) (default 5)
            release: set release (from 1 to 8000) (default 50)
            asc: enable asc (default false)
            asc_level: set asc level (from 0 to 1) (default 0.5)
            level: auto level (default true)
            latency: compensate delay (default false)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#alimiter)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="alimiter", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "limit": limit,
                "attack": attack,
                "release": release,
                "asc": asc,
                "asc_level": asc_level,
                "level": level,
                "latency": latency,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def allpass(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.707),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        order: Int = Default(2),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a two-pole all-pass filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.707)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            order: set filter order (from 1 to 2) (default 2)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#allpass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="allpass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "order": order,
                "transform": transform,
                "precision": precision,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aloop(
        self,
        *,
        loop: Int = Default(0),
        size: Int64 = Default(0),
        start: Int64 = Default(0),
        time: Duration = Default("INT64_MAX"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Loop audio samples.

        Args:
            loop: number of loops (from -1 to INT_MAX) (default 0)
            size: max number of samples to loop (from 0 to INT_MAX) (default 0)
            start: set the loop start sample (from -1 to I64_MAX) (default 0)
            time: set the loop start time (default INT64_MAX)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aloop)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aloop", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def ametadata(
        self,
        *,
        mode: Int
        | Literal["select", "add", "modify", "delete", "print"]
        | Default = Default("select"),
        key: String = Default(None),
        value: String = Default(None),
        function: Int
        | Literal[
            "same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"
        ]
        | Default = Default("same_str"),
        expr: String = Default(None),
        file: String = Default(None),
        direct: Boolean = Default(False),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Manipulate audio frame metadata.

        Args:
            mode: set a mode of operation (from 0 to 4) (default select)
            key: set metadata key
            value: set metadata value
            function: function for comparing values (from 0 to 6) (default same_str)
            expr: set expression for expr function
            file: set file where to print metadata information
            direct: reduce buffering when printing to user-set file or pipe (default false)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#metadata_002c-ametadata)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ametadata", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def amultiply(
        self,
        _multiply1: AudioStream,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Multiply two audio streams.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#amultiply)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="amultiply",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _multiply1,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def anequalizer(
        self,
        *,
        params: String = Default(""),
        curves: Boolean = Default(False),
        size: Image_size = Default("hd720"),
        mgain: Double = Default(60.0),
        fscale: Int | Literal["lin", "log"] | Default = Default("log"),
        colors: String = Default(
            "red|green|blue|yellow|orange|lime|pink|magenta|brown"
        ),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Apply high-order audio parametric multi band equalizer.

        Args:
            params: (default "")
            curves: draw frequency response curves (default false)
            size: set video size (default "hd720")
            mgain: set max gain (from -900 to 900) (default 60)
            fscale: set frequency scale (from 0 to 1) (default log)
            colors: set channels curves colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
            enable: timeline editing

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="anequalizer",
                typings_input=("audio",),
                typings_output="[StreamType.audio] + [StreamType.video] if curves else []",
            ),
            self,
            **{
                "params": params,
                "curves": curves,
                "size": size,
                "mgain": mgain,
                "fscale": fscale,
                "colors": colors,
                "enable": enable,
            }
            | (extra_options or {}),
        )

        return filter_node

    def anlmdn(
        self,
        *,
        strength: Float = Default(1e-05),
        patch: Duration = Default(0.002),
        research: Duration = Default(0.006),
        output: Int | Literal["i", "o", "n"] | Default = Default("o"),
        smooth: Float = Default(11.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Reduce broadband noise from stream using Non-Local Means.

        Args:
            strength: set denoising strength (from 1e-05 to 10000) (default 1e-05)
            patch: set patch duration (default 0.002)
            research: set research duration (default 0.006)
            output: set output mode (from 0 to 2) (default o)
            smooth: set smooth factor (from 1 to 1000) (default 11)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anlmdn)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="anlmdn", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "strength": strength,
                "patch": patch,
                "research": research,
                "output": output,
                "smooth": smooth,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def anlmf(
        self,
        _desired: AudioStream,
        *,
        order: Int = Default(256),
        mu: Float = Default(0.75),
        eps: Float = Default(1.0),
        leakage: Float = Default(0.0),
        out_mode: Int | Literal["i", "d", "o", "n", "e"] | Default = Default("o"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Normalized Least-Mean-Fourth algorithm to first audio stream.

        Args:
            order: set the filter order (from 1 to 32767) (default 256)
            mu: set the filter mu (from 0 to 2) (default 0.75)
            eps: set the filter eps (from 0 to 1) (default 1)
            leakage: set the filter leakage (from 0 to 1) (default 0)
            out_mode: set output mode (from 0 to 4) (default o)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="anlmf",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _desired,
            **{
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def anlms(
        self,
        _desired: AudioStream,
        *,
        order: Int = Default(256),
        mu: Float = Default(0.75),
        eps: Float = Default(1.0),
        leakage: Float = Default(0.0),
        out_mode: Int | Literal["i", "d", "o", "n", "e"] | Default = Default("o"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Normalized Least-Mean-Squares algorithm to first audio stream.

        Args:
            order: set the filter order (from 1 to 32767) (default 256)
            mu: set the filter mu (from 0 to 2) (default 0.75)
            eps: set the filter eps (from 0 to 1) (default 1)
            leakage: set the filter leakage (from 0 to 1) (default 0)
            out_mode: set output mode (from 0 to 4) (default o)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="anlms",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _desired,
            **{
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def anull(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Pass the source unchanged to the output.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#anull)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="anull", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def apad(
        self,
        *,
        packet_size: Int = Default(4096),
        pad_len: Int64 = Default(-1),
        whole_len: Int64 = Default(-1),
        pad_dur: Duration = Default(-1e-06),
        whole_dur: Duration = Default(-1e-06),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Pad audio with silence.

        Args:
            packet_size: set silence packet size (from 0 to INT_MAX) (default 4096)
            pad_len: set number of samples of silence to add (from -1 to I64_MAX) (default -1)
            whole_len: set minimum target number of samples in the audio stream (from -1 to I64_MAX) (default -1)
            pad_dur: set duration of silence to add (default -0.000001)
            whole_dur: set minimum target duration in the audio stream (default -0.000001)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#apad)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="apad", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "packet_size": packet_size,
                "pad_len": pad_len,
                "whole_len": whole_len,
                "pad_dur": pad_dur,
                "whole_dur": whole_dur,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aperms(
        self,
        *,
        mode: Int | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default(
            "none"
        ),
        seed: Int64 = Default(-1),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Set permissions for the output audio frame.

        Args:
            mode: select permissions mode (from 0 to 4) (default none)
            seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aperms", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "mode": mode,
                "seed": seed,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aphasemeter(
        self,
        *,
        rate: Video_rate = Default("25"),
        size: Image_size = Default("800x400"),
        rc: Int = Default(2),
        gc: Int = Default(7),
        bc: Int = Default(1),
        mpc: String = Default("none"),
        video: Boolean = Default(True),
        phasing: Boolean = Default(False),
        tolerance: Float = Default(0.0),
        angle: Float = Default(170.0),
        duration: Duration = Default(2.0),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Convert input audio to phase meter video output.

        Args:
            rate: set video rate (default "25")
            size: set video size (default "800x400")
            rc: set red contrast (from 0 to 255) (default 2)
            gc: set green contrast (from 0 to 255) (default 7)
            bc: set blue contrast (from 0 to 255) (default 1)
            mpc: set median phase color (default "none")
            video: set video output (default true)
            phasing: set mono and out-of-phase detection output (default false)
            tolerance: set phase tolerance for mono detection (from 0 to 1) (default 0)
            angle: set angle threshold for out-of-phase detection (from 90 to 180) (default 170)
            duration: set minimum mono or out-of-phase duration in seconds (default 2)

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aphasemeter)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aphasemeter",
                typings_input=("audio",),
                typings_output="[StreamType.audio] + ([StreamType.video] if video else [])",
            ),
            self,
            **{
                "rate": rate,
                "size": size,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "mpc": mpc,
                "video": video,
                "phasing": phasing,
                "tolerance": tolerance,
                "angle": angle,
                "duration": duration,
            }
            | (extra_options or {}),
        )

        return filter_node

    def aphaser(
        self,
        *,
        in_gain: Double = Default(0.4),
        out_gain: Double = Default(0.74),
        delay: Double = Default(3.0),
        decay: Double = Default(0.4),
        speed: Double = Default(0.5),
        type: Int | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default(
            "triangular"
        ),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Add a phasing effect to the audio.

        Args:
            in_gain: set input gain (from 0 to 1) (default 0.4)
            out_gain: set output gain (from 0 to 1e+09) (default 0.74)
            delay: set delay in milliseconds (from 0 to 5) (default 3)
            decay: set decay (from 0 to 0.99) (default 0.4)
            speed: set modulation speed (from 0.1 to 2) (default 0.5)
            type: set modulation type (from 0 to 1) (default triangular)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aphaser)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aphaser", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delay": delay,
                "decay": decay,
                "speed": speed,
                "type": type,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aphaseshift(
        self,
        *,
        shift: Double = Default(0.0),
        level: Double = Default(1.0),
        order: Int = Default(8),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply phase shifting to input audio.

        Args:
            shift: set phase shift (from -1 to 1) (default 0)
            level: set output level (from 0 to 1) (default 1)
            order: set filter order (from 1 to 16) (default 8)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aphaseshift)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aphaseshift", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "shift": shift,
                "level": level,
                "order": order,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def apsnr(
        self,
        _input1: AudioStream,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Measure Audio Peak Signal-to-Noise Ratio.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#apsnr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="apsnr",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _input1,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def apsyclip(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        clip: Double = Default(1.0),
        diff: Boolean = Default(False),
        adaptive: Double = Default(0.5),
        iterations: Int = Default(10),
        level: Boolean = Default(False),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Psychoacoustic Clipper.

        Args:
            level_in: set input level (from 0.015625 to 64) (default 1)
            level_out: set output level (from 0.015625 to 64) (default 1)
            clip: set clip level (from 0.015625 to 1) (default 1)
            diff: enable difference (default false)
            adaptive: set adaptive distortion (from 0 to 1) (default 0.5)
            iterations: set iterations (from 1 to 20) (default 10)
            level: set auto level (default false)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#apsyclip)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="apsyclip", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "clip": clip,
                "diff": diff,
                "adaptive": adaptive,
                "iterations": iterations,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def apulsator(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        mode: Int
        | Literal["sine", "triangle", "square", "sawup", "sawdown"]
        | Default = Default("sine"),
        amount: Double = Default(1.0),
        offset_l: Double = Default(0.0),
        offset_r: Double = Default(0.5),
        width: Double = Default(1.0),
        timing: Int | Literal["bpm", "ms", "hz"] | Default = Default("hz"),
        bpm: Double = Default(120.0),
        ms: Int = Default(500),
        hz: Double = Default(2.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio pulsator.

        Args:
            level_in: set input gain (from 0.015625 to 64) (default 1)
            level_out: set output gain (from 0.015625 to 64) (default 1)
            mode: set mode (from 0 to 4) (default sine)
            amount: set modulation (from 0 to 1) (default 1)
            offset_l: set offset L (from 0 to 1) (default 0)
            offset_r: set offset R (from 0 to 1) (default 0.5)
            width: set pulse width (from 0 to 2) (default 1)
            timing: set timing (from 0 to 2) (default hz)
            bpm: set BPM (from 30 to 300) (default 120)
            ms: set ms (from 10 to 2000) (default 500)
            hz: set frequency (from 0.01 to 100) (default 2)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#apulsator)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="apulsator", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "amount": amount,
                "offset_l": offset_l,
                "offset_r": offset_r,
                "width": width,
                "timing": timing,
                "bpm": bpm,
                "ms": ms,
                "hz": hz,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def arealtime(
        self,
        *,
        limit: Duration = Default(2.0),
        speed: Double = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Slow down filtering to match realtime.

        Args:
            limit: sleep time limit (default 2)
            speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="arealtime", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "limit": limit,
                "speed": speed,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aresample(
        self,
        *,
        sample_rate: Int = Default(0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Resample audio data.

        Args:
            sample_rate: (from 0 to INT_MAX) (default 0)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aresample)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aresample", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "sample_rate": sample_rate,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def areverse(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Reverse an audio clip.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#areverse)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="areverse", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def arls(
        self,
        _desired: AudioStream,
        *,
        order: Int = Default(16),
        _lambda: Float = Default(1.0),
        delta: Float = Default(2.0),
        out_mode: Int | Literal["i", "d", "o", "n", "e"] | Default = Default("o"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Recursive Least Squares algorithm to first audio stream.

        Args:
            order: set the filter order (from 1 to 32767) (default 16)
            _lambda: set the filter lambda (from 0 to 1) (default 1)
            delta: set the filter delta (from 0 to 32767) (default 2)
            out_mode: set output mode (from 0 to 4) (default o)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#arls)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="arls", typings_input=("audio", "audio"), typings_output=("audio",)
            ),
            self,
            _desired,
            **{
                "order": order,
                "lambda": _lambda,
                "delta": delta,
                "out_mode": out_mode,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def arnndn(
        self,
        *,
        model: String = Default(None),
        mix: Float = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Reduce noise from speech using Recurrent Neural Networks.

        Args:
            model: set model name
            mix: set output vs input mix (from -1 to 1) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#arnndn)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="arnndn", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "model": model,
                "mix": mix,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asdr(
        self,
        _input1: AudioStream,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Measure Audio Signal-to-Distortion Ratio.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asdr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asdr", typings_input=("audio", "audio"), typings_output=("audio",)
            ),
            self,
            _input1,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asegment(
        self,
        *,
        timestamps: String = Default(None),
        samples: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Segment audio stream.

        Args:
            timestamps: timestamps of input at which to split input
            samples: samples at which to split input

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asegment",
                typings_input=("audio",),
                typings_output="[StreamType.audio] * len(str(timestamps or samples).split('|'))",
            ),
            self,
            **{
                "timestamps": timestamps,
                "samples": samples,
            }
            | (extra_options or {}),
        )

        return filter_node

    def aselect(
        self,
        *,
        expr: String = Default("1"),
        outputs: Int = Default(1),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Select audio frames to pass in output.

        Args:
            expr: set an expression to use for selecting frames (default "1")
            outputs: set the number of outputs (from 1 to INT_MAX) (default 1)

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aselect",
                typings_input=("audio",),
                typings_output="[StreamType.audio] * int(outputs)",
            ),
            self,
            **{
                "expr": expr,
                "outputs": outputs,
            }
            | (extra_options or {}),
        )

        return filter_node

    def asendcmd(
        self,
        *,
        commands: String = Default(None),
        filename: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Send commands to filters.

        Args:
            commands: set commands
            filename: set commands file

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asendcmd", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "commands": commands,
                "filename": filename,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asetnsamples(
        self,
        *,
        nb_out_samples: Int = Default(1024),
        pad: Boolean = Default(True),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Set the number of samples for each output audio frames.

        Args:
            nb_out_samples: set the number of per-frame output samples (from 1 to INT_MAX) (default 1024)
            pad: pad last frame with zeros (default true)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asetnsamples)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asetnsamples", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "nb_out_samples": nb_out_samples,
                "pad": pad,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asetpts(
        self,
        *,
        expr: String = Default("PTS"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Set PTS for the output audio frame.

        Args:
            expr: Expression determining the frame timestamp (default "PTS")

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asetpts", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "expr": expr,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asetrate(
        self,
        *,
        sample_rate: Int = Default(44100),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Change the sample rate without altering the data.

        Args:
            sample_rate: set the sample rate (from 1 to INT_MAX) (default 44100)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asetrate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asetrate", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "sample_rate": sample_rate,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asettb(
        self,
        *,
        expr: String = Default("intb"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Set timebase for the audio output link.

        Args:
            expr: set expression determining the output timebase (default "intb")

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asettb", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "expr": expr,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def ashowinfo(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Show textual information for each audio frame.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ashowinfo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ashowinfo", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asidedata(
        self,
        *,
        mode: Int | Literal["select", "delete"] | Default = Default("select"),
        type: Int
        | Literal[
            "PANSCAN",
            "A53_CC",
            "STEREO3D",
            "MATRIXENCODING",
            "DOWNMIX_INFO",
            "REPLAYGAIN",
            "DISPLAYMATRIX",
            "AFD",
            "MOTION_VECTORS",
            "SKIP_SAMPLES",
            "AUDIO_SERVICE_TYPE",
            "MASTERING_DISPLAY_METADATA",
            "GOP_TIMECODE",
            "SPHERICAL",
            "CONTENT_LIGHT_LEVEL",
            "ICC_PROFILE",
            "S12M_TIMECOD",
            "DYNAMIC_HDR_PLUS",
            "REGIONS_OF_INTEREST",
            "DETECTION_BOUNDING_BOXES",
            "SEI_UNREGISTERED",
        ]
        | Default = Default(-1),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Manipulate audio frame side data.

        Args:
            mode: set a mode of operation (from 0 to 1) (default select)
            type: set side data type (from -1 to INT_MAX) (default -1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asidedata", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "mode": mode,
                "type": type,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asisdr(
        self,
        _input1: AudioStream,
        *,
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Measure Audio Scale-Invariant Signal-to-Distortion Ratio.

        Args:
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asisdr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asisdr",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _input1,
            **{
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asoftclip(
        self,
        *,
        type: Int
        | Literal[
            "hard", "tanh", "atan", "cubic", "exp", "alg", "quintic", "sin", "erf"
        ]
        | Default = Default("tanh"),
        threshold: Double = Default(1.0),
        output: Double = Default(1.0),
        param: Double = Default(1.0),
        oversample: Int = Default(1),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Soft Clipper.

        Args:
            type: set softclip type (from -1 to 7) (default tanh)
            threshold: set softclip threshold (from 1e-06 to 1) (default 1)
            output: set softclip output gain (from 1e-06 to 16) (default 1)
            param: set softclip parameter (from 0.01 to 3) (default 1)
            oversample: set oversample factor (from 1 to 64) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asoftclip)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asoftclip", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "type": type,
                "threshold": threshold,
                "output": output,
                "param": param,
                "oversample": oversample,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def aspectralstats(
        self,
        *,
        win_size: Int = Default(2048),
        win_func: Int
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
        | Default = Default("hann"),
        overlap: Float = Default(0.5),
        measure: Flags
        | Literal[
            "none",
            "all",
            "mean",
            "variance",
            "centroid",
            "spread",
            "skewness",
            "kurtosis",
            "entropy",
            "flatness",
            "crest",
            "flux",
            "slope",
            "decrease",
            "rolloff",
        ]
        | Default = Default(
            "all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff"
        ),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Show frequency domain statistics about audio frames.

        Args:
            win_size: set the window size (from 32 to 65536) (default 2048)
            win_func: set window function (from 0 to 20) (default hann)
            overlap: set window overlap (from 0 to 1) (default 0.5)
            measure: select the parameters which are measured (default all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#aspectralstats)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="aspectralstats",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "measure": measure,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asplit(
        self,
        *,
        outputs: Int = Default(2),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Pass on the audio input to N audio outputs.

        Args:
            outputs: set number of outputs (from 1 to INT_MAX) (default 2)

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asplit",
                typings_input=("audio",),
                typings_output="[StreamType.audio] * int(outputs)",
            ),
            self,
            **{
                "outputs": outputs,
            }
            | (extra_options or {}),
        )

        return filter_node

    def astats(
        self,
        *,
        length: Double = Default(0.05),
        metadata: Boolean = Default(False),
        reset: Int = Default(0),
        measure_perchannel: Flags
        | Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ]
        | Default = Default(
            "all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count"
        ),
        measure_overall: Flags
        | Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ]
        | Default = Default(
            "all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count"
        ),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Show time domain statistics about audio frames.

        Args:
            length: set the window length (from 0 to 10) (default 0.05)
            metadata: inject metadata in the filtergraph (default false)
            reset: Set the number of frames over which cumulative stats are calculated before being reset (from 0 to INT_MAX) (default 0)
            measure_perchannel: Select the parameters which are measured per channel (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count)
            measure_overall: Select the parameters which are measured overall (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#astats)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="astats", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "length": length,
                "metadata": metadata,
                "reset": reset,
                "measure_perchannel": measure_perchannel,
                "measure_overall": measure_overall,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asubboost(
        self,
        *,
        dry: Double = Default(1.0),
        wet: Double = Default(1.0),
        boost: Double = Default(2.0),
        decay: Double = Default(0.0),
        feedback: Double = Default(0.9),
        cutoff: Double = Default(100.0),
        slope: Double = Default(0.5),
        delay: Double = Default(20.0),
        channels: String = Default("all"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Boost subwoofer frequencies.

        Args:
            dry: set dry gain (from 0 to 1) (default 1)
            wet: set wet gain (from 0 to 1) (default 1)
            boost: set max boost (from 1 to 12) (default 2)
            decay: set decay (from 0 to 1) (default 0)
            feedback: set feedback (from 0 to 1) (default 0.9)
            cutoff: set cutoff (from 50 to 900) (default 100)
            slope: set slope (from 0.0001 to 1) (default 0.5)
            delay: set delay (from 1 to 100) (default 20)
            channels: set channels to filter (default "all")
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asubboost)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asubboost", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "dry": dry,
                "wet": wet,
                "boost": boost,
                "decay": decay,
                "feedback": feedback,
                "cutoff": cutoff,
                "slope": slope,
                "delay": delay,
                "channels": channels,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asubcut(
        self,
        *,
        cutoff: Double = Default(20.0),
        order: Int = Default(10),
        level: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Cut subwoofer frequencies.

        Args:
            cutoff: set cutoff frequency (from 2 to 200) (default 20)
            order: set filter order (from 3 to 20) (default 10)
            level: set input level (from 0 to 1) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asubcut)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asubcut", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "cutoff": cutoff,
                "order": order,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asupercut(
        self,
        *,
        cutoff: Double = Default(20000.0),
        order: Int = Default(10),
        level: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Cut super frequencies.

        Args:
            cutoff: set cutoff frequency (from 20000 to 192000) (default 20000)
            order: set filter order (from 3 to 20) (default 10)
            level: set input level (from 0 to 1) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asupercut)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asupercut", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "cutoff": cutoff,
                "order": order,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asuperpass(
        self,
        *,
        centerf: Double = Default(1000.0),
        order: Int = Default(4),
        qfactor: Double = Default(1.0),
        level: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply high order Butterworth band-pass filter.

        Args:
            centerf: set center frequency (from 2 to 999999) (default 1000)
            order: set filter order (from 4 to 20) (default 4)
            qfactor: set Q-factor (from 0.01 to 100) (default 1)
            level: set input level (from 0 to 2) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asuperpass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asuperpass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def asuperstop(
        self,
        *,
        centerf: Double = Default(1000.0),
        order: Int = Default(4),
        qfactor: Double = Default(1.0),
        level: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply high order Butterworth band-stop filter.

        Args:
            centerf: set center frequency (from 2 to 999999) (default 1000)
            order: set filter order (from 4 to 20) (default 4)
            qfactor: set Q-factor (from 0.01 to 100) (default 1)
            level: set input level (from 0 to 2) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#asuperstop)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="asuperstop", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def atempo(
        self,
        *,
        tempo: Double = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Adjust audio tempo.

        Args:
            tempo: set tempo scale factor (from 0.5 to 100) (default 1)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#atempo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="atempo", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "tempo": tempo,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def atilt(
        self,
        *,
        freq: Double = Default(10000.0),
        slope: Double = Default(0.0),
        width: Double = Default(1000.0),
        order: Int = Default(5),
        level: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply spectral tilt to audio.

        Args:
            freq: set central frequency (from 20 to 192000) (default 10000)
            slope: set filter slope (from -1 to 1) (default 0)
            width: set filter width (from 100 to 10000) (default 1000)
            order: set filter order (from 2 to 30) (default 5)
            level: set input level (from 0 to 4) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#atilt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="atilt", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "freq": freq,
                "slope": slope,
                "width": width,
                "order": order,
                "level": level,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def atrim(
        self,
        *,
        start: Duration = Default("INT64_MAX"),
        end: Duration = Default("INT64_MAX"),
        start_pts: Int64 = Default("I64_MIN"),
        end_pts: Int64 = Default("I64_MIN"),
        duration: Duration = Default(0.0),
        start_sample: Int64 = Default(-1),
        end_sample: Int64 = Default("I64_MAX"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Pick one continuous section from the input, drop the rest.

        Args:
            start: Timestamp of the first frame that should be passed (default INT64_MAX)
            end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
            start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
            end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
            duration: Maximum duration of the output (default 0)
            start_sample: Number of the first audio sample that should be passed to the output (from -1 to I64_MAX) (default -1)
            end_sample: Number of the first audio sample that should be dropped again (from 0 to I64_MAX) (default I64_MAX)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#atrim)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="atrim", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "start": start,
                "end": end,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "start_sample": start_sample,
                "end_sample": end_sample,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def avectorscope(
        self,
        *,
        mode: Int | Literal["lissajous", "lissajous_xy", "polar"] | Default = Default(
            "lissajous"
        ),
        rate: Video_rate = Default("25"),
        size: Image_size = Default("400x400"),
        rc: Int = Default(40),
        gc: Int = Default(160),
        bc: Int = Default(80),
        ac: Int = Default(255),
        rf: Int = Default(15),
        gf: Int = Default(10),
        bf: Int = Default(5),
        af: Int = Default(5),
        zoom: Double = Default(1.0),
        draw: Int | Literal["dot", "line", "aaline"] | Default = Default("dot"),
        scale: Int | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("lin"),
        swap: Boolean = Default(True),
        mirror: Int | Literal["none", "x", "y", "xy"] | Default = Default("none"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to vectorscope video output.

        Args:
            mode: set mode (from 0 to 2) (default lissajous)
            rate: set video rate (default "25")
            size: set video size (default "400x400")
            rc: set red contrast (from 0 to 255) (default 40)
            gc: set green contrast (from 0 to 255) (default 160)
            bc: set blue contrast (from 0 to 255) (default 80)
            ac: set alpha contrast (from 0 to 255) (default 255)
            rf: set red fade (from 0 to 255) (default 15)
            gf: set green fade (from 0 to 255) (default 10)
            bf: set blue fade (from 0 to 255) (default 5)
            af: set alpha fade (from 0 to 255) (default 5)
            zoom: set zoom factor (from 0 to 10) (default 1)
            draw: set draw mode (from 0 to 2) (default dot)
            scale: set amplitude scale mode (from 0 to 3) (default lin)
            swap: swap x axis with y axis (default true)
            mirror: mirror axis (from 0 to 3) (default none)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#avectorscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="avectorscope", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "mode": mode,
                "rate": rate,
                "size": size,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "ac": ac,
                "rf": rf,
                "gf": gf,
                "bf": bf,
                "af": af,
                "zoom": zoom,
                "draw": draw,
                "scale": scale,
                "swap": swap,
                "mirror": mirror,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def axcorrelate(
        self,
        _axcorrelate1: AudioStream,
        *,
        size: Int = Default(256),
        algo: Int | Literal["slow", "fast", "best"] | Default = Default("best"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Cross-correlate two audio streams.

        Args:
            size: set the segment size (from 2 to 131072) (default 256)
            algo: set the algorithm (from 0 to 2) (default best)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#axcorrelate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="axcorrelate",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _axcorrelate1,
            **{
                "size": size,
                "algo": algo,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def azmq(
        self,
        *,
        bind_address: String = Default("tcp://*:5555"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Receive commands through ZMQ and broker them to filters.

        Args:
            bind_address: set bind address (default "tcp://*:5555")

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#zmq_002c-azmq)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="azmq", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "bind_address": bind_address,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def bandpass(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        csg: Boolean = Default(False),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a two-pole Butterworth band-pass filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            csg: use constant skirt gain (default false)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bandpass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bandpass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "csg": csg,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def bandreject(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a two-pole Butterworth band-reject filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bandreject)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bandreject", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def bass(
        self,
        *,
        frequency: Double = Default(100.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        gain: Double = Default(0.0),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Boost or cut lower frequencies.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 100)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            gain: set gain (from -900 to 900) (default 0)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def biquad(
        self,
        *,
        a0: Double = Default(1.0),
        a1: Double = Default(0.0),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a biquad IIR filter with the given coefficients.

        Args:
            a0: (from INT_MIN to INT_MAX) (default 1)
            a1: (from INT_MIN to INT_MAX) (default 0)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#biquad)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="biquad", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "a0": a0,
                "a1": a1,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def channelmap(
        self,
        *,
        map: String = Default(None),
        channel_layout: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remap audio channels.

        Args:
            map: A comma-separated list of input channel numbers in output order.
            channel_layout: Output channel layout.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#channelmap)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="channelmap", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "map": map,
                "channel_layout": channel_layout,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def channelsplit(
        self,
        *,
        channel_layout: String = Default("stereo"),
        channels: String = Default("all"),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        Split audio into per-channel streams.

        Args:
            channel_layout: Input channel layout. (default "stereo")
            channels: Channels to extract. (default "all")

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#channelsplit)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="channelsplit",
                typings_input=("audio",),
                typings_output="[StreamType.audio] * CHANNEL_LAYOUT[str(channel_layout)]",
            ),
            self,
            **{
                "channel_layout": channel_layout,
                "channels": channels,
            }
            | (extra_options or {}),
        )

        return filter_node

    def chorus(
        self,
        *,
        in_gain: Float = Default(0.4),
        out_gain: Float = Default(0.4),
        delays: String = Default(None),
        decays: String = Default(None),
        speeds: String = Default(None),
        depths: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Add a chorus effect to the audio.

        Args:
            in_gain: set input gain (from 0 to 1) (default 0.4)
            out_gain: set output gain (from 0 to 1) (default 0.4)
            delays: set delays
            decays: set decays
            speeds: set speeds
            depths: set depths

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chorus)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chorus", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
                "speeds": speeds,
                "depths": depths,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def compand(
        self,
        *,
        attacks: String = Default("0"),
        decays: String = Default("0.8"),
        points: String = Default("-70/-70|-60/-20|1/0"),
        soft_knee: Double = Default(0.01),
        gain: Double = Default(0.0),
        volume: Double = Default(0.0),
        delay: Double = Default(0.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Compress or expand audio dynamic range.

        Args:
            attacks: set time over which increase of volume is determined (default "0")
            decays: set time over which decrease of volume is determined (default "0.8")
            points: set points of transfer function (default "-70/-70|-60/-20|1/0")
            soft_knee: set soft-knee (from 0.01 to 900) (default 0.01)
            gain: set output gain (from -900 to 900) (default 0)
            volume: set initial volume (from -900 to 0) (default 0)
            delay: set delay for samples before sending them to volume adjuster (from 0 to 20) (default 0)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#compand)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="compand", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "attacks": attacks,
                "decays": decays,
                "points": points,
                "soft-knee": soft_knee,
                "gain": gain,
                "volume": volume,
                "delay": delay,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def compensationdelay(
        self,
        *,
        mm: Int = Default(0),
        cm: Int = Default(0),
        m: Int = Default(0),
        dry: Double = Default(0.0),
        wet: Double = Default(1.0),
        temp: Int = Default(20),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Compensation Delay Line.

        Args:
            mm: set mm distance (from 0 to 10) (default 0)
            cm: set cm distance (from 0 to 100) (default 0)
            m: set meter distance (from 0 to 100) (default 0)
            dry: set dry amount (from 0 to 1) (default 0)
            wet: set wet amount (from 0 to 1) (default 1)
            temp: set temperature °C (from -50 to 50) (default 20)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#compensationdelay)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="compensationdelay",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "mm": mm,
                "cm": cm,
                "m": m,
                "dry": dry,
                "wet": wet,
                "temp": temp,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def crossfeed(
        self,
        *,
        strength: Double = Default(0.2),
        range: Double = Default(0.5),
        slope: Double = Default(0.5),
        level_in: Double = Default(0.9),
        level_out: Double = Default(1.0),
        block_size: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply headphone crossfeed filter.

        Args:
            strength: set crossfeed strength (from 0 to 1) (default 0.2)
            range: set soundstage wideness (from 0 to 1) (default 0.5)
            slope: set curve slope (from 0.01 to 1) (default 0.5)
            level_in: set level in (from 0 to 1) (default 0.9)
            level_out: set level out (from 0 to 1) (default 1)
            block_size: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#crossfeed)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="crossfeed", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "strength": strength,
                "range": range,
                "slope": slope,
                "level_in": level_in,
                "level_out": level_out,
                "block_size": block_size,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def crystalizer(
        self,
        *,
        i: Float = Default(2.0),
        c: Boolean = Default(True),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Simple audio noise sharpening filter.

        Args:
            i: set intensity (from -10 to 10) (default 2)
            c: enable clipping (default true)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#crystalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="crystalizer", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "i": i,
                "c": c,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def dcshift(
        self,
        *,
        shift: Double = Default(0.0),
        limitergain: Double = Default(0.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a DC shift to the audio.

        Args:
            shift: set DC shift (from -1 to 1) (default 0)
            limitergain: set limiter gain (from 0 to 1) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dcshift)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dcshift", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "shift": shift,
                "limitergain": limitergain,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def deesser(
        self,
        *,
        i: Double = Default(0.0),
        m: Double = Default(0.5),
        f: Double = Default(0.5),
        s: Int | Literal["i", "o", "e"] | Default = Default("o"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply de-essing to the audio.

        Args:
            i: set intensity (from 0 to 1) (default 0)
            m: set max deessing (from 0 to 1) (default 0.5)
            f: set frequency (from 0 to 1) (default 0.5)
            s: set output mode (from 0 to 2) (default o)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deesser)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deesser", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "i": i,
                "m": m,
                "f": f,
                "s": s,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def dialoguenhance(
        self,
        *,
        original: Double = Default(1.0),
        enhance: Double = Default(1.0),
        voice: Double = Default(2.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Dialogue Enhancement.

        Args:
            original: set original center factor (from 0 to 1) (default 1)
            enhance: set dialogue enhance factor (from 0 to 3) (default 1)
            voice: set voice detection factor (from 2 to 32) (default 2)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dialoguenhance",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "original": original,
                "enhance": enhance,
                "voice": voice,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def drmeter(
        self,
        *,
        length: Double = Default(3.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Measure audio dynamic range.

        Args:
            length: set the window length (from 0.01 to 10) (default 3)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#drmeter)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="drmeter", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "length": length,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def dynaudnorm(
        self,
        *,
        framelen: Int = Default(500),
        gausssize: Int = Default(31),
        peak: Double = Default(0.95),
        maxgain: Double = Default(10.0),
        targetrms: Double = Default(0.0),
        coupling: Boolean = Default(True),
        correctdc: Boolean = Default(False),
        altboundary: Boolean = Default(False),
        compress: Double = Default(0.0),
        threshold: Double = Default(0.0),
        channels: String = Default("all"),
        overlap: Double = Default(0.0),
        curve: String = Default(None),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Dynamic Audio Normalizer.

        Args:
            framelen: set the frame length in msec (from 10 to 8000) (default 500)
            gausssize: set the filter size (from 3 to 301) (default 31)
            peak: set the peak value (from 0 to 1) (default 0.95)
            maxgain: set the max amplification (from 1 to 100) (default 10)
            targetrms: set the target RMS (from 0 to 1) (default 0)
            coupling: set channel coupling (default true)
            correctdc: set DC correction (default false)
            altboundary: set alternative boundary mode (default false)
            compress: set the compress factor (from 0 to 30) (default 0)
            threshold: set the threshold value (from 0 to 1) (default 0)
            channels: set channels to filter (default "all")
            overlap: set the frame overlap (from 0 to 1) (default 0)
            curve: set the custom peak mapping curve
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dynaudnorm", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "framelen": framelen,
                "gausssize": gausssize,
                "peak": peak,
                "maxgain": maxgain,
                "targetrms": targetrms,
                "coupling": coupling,
                "correctdc": correctdc,
                "altboundary": altboundary,
                "compress": compress,
                "threshold": threshold,
                "channels": channels,
                "overlap": overlap,
                "curve": curve,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def earwax(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Widen the stereo image.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#earwax)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="earwax", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)

    def ebur128(
        self,
        *,
        video: Boolean = Default(False),
        size: Image_size = Default("640x480"),
        meter: Int = Default(9),
        framelog: Int | Literal["quiet", "info", "verbose"] | Default = Default(-1),
        metadata: Boolean = Default(False),
        peak: Flags | Literal["none", "sample", "true"] | Default = Default("0"),
        dualmono: Boolean = Default(False),
        panlaw: Double = Default(-3.0103),
        target: Int = Default(-23),
        gauge: Int | Literal["momentary", "m", "shortterm", "s"] | Default = Default(
            "momentary"
        ),
        scale: Int | Literal["absolute", "LUFS", "relative", "LU"] | Default = Default(
            "absolute"
        ),
        integrated: Double = Default(0.0),
        range: Double = Default(0.0),
        lra_low: Double = Default(0.0),
        lra_high: Double = Default(0.0),
        sample_peak: Double = Default(0.0),
        true_peak: Double = Default(0.0),
        extra_options: dict[str, Any] = None,
    ) -> FilterNode:
        """

        EBU R128 scanner.

        Args:
            video: set video output (default false)
            size: set video size (default "640x480")
            meter: set scale meter (+9 to +18) (from 9 to 18) (default 9)
            framelog: force frame logging level (from INT_MIN to INT_MAX) (default -1)
            metadata: inject metadata in the filtergraph (default false)
            peak: set peak mode (default 0)
            dualmono: treat mono input files as dual-mono (default false)
            panlaw: set a specific pan law for dual-mono files (from -10 to 0) (default -3.0103)
            target: set a specific target level in LUFS (-23 to 0) (from -23 to 0) (default -23)
            gauge: set gauge display type (from 0 to 1) (default momentary)
            scale: sets display method for the stats (from 0 to 1) (default absolute)
            integrated: integrated loudness (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
            range: loudness range (LU) (from -DBL_MAX to DBL_MAX) (default 0)
            lra_low: LRA low (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
            lra_high: LRA high (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
            sample_peak: sample peak (dBFS) (from -DBL_MAX to DBL_MAX) (default 0)
            true_peak: true peak (dBFS) (from -DBL_MAX to DBL_MAX) (default 0)

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ebur128)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ebur128",
                typings_input=("audio",),
                typings_output="[StreamType.video] if video else [] + [StreamType.audio]",
            ),
            self,
            **{
                "video": video,
                "size": size,
                "meter": meter,
                "framelog": framelog,
                "metadata": metadata,
                "peak": peak,
                "dualmono": dualmono,
                "panlaw": panlaw,
                "target": target,
                "gauge": gauge,
                "scale": scale,
                "integrated": integrated,
                "range": range,
                "lra_low": lra_low,
                "lra_high": lra_high,
                "sample_peak": sample_peak,
                "true_peak": true_peak,
            }
            | (extra_options or {}),
        )

        return filter_node

    def equalizer(
        self,
        *,
        frequency: Double = Default(0.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(1.0),
        gain: Double = Default(0.0),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply two-pole peaking equalization (EQ) filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 0)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 1)
            gain: set gain (from -900 to 900) (default 0)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#equalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="equalizer", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def extrastereo(
        self,
        *,
        m: Float = Default(2.5),
        c: Boolean = Default(True),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Increase difference between stereo audio channels.

        Args:
            m: set the difference coefficient (from -10 to 10) (default 2.5)
            c: enable clipping (default true)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#extrastereo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="extrastereo", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "m": m,
                "c": c,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def firequalizer(
        self,
        *,
        gain: String = Default("gain_interpolate(f"),
        gain_entry: String = Default(None),
        delay: Double = Default(0.01),
        accuracy: Double = Default(5.0),
        wfunc: Int
        | Literal[
            "rectangular",
            "hann",
            "hamming",
            "blackman",
            "nuttall3",
            "mnuttall3",
            "nuttall",
            "bnuttall",
            "bharris",
            "tukey",
        ]
        | Default = Default("hann"),
        fixed: Boolean = Default(False),
        multi: Boolean = Default(False),
        zero_phase: Boolean = Default(False),
        scale: Int
        | Literal["linlin", "linlog", "loglin", "loglog"]
        | Default = Default("linlog"),
        dumpfile: String = Default(None),
        dumpscale: Int
        | Literal["linlin", "linlog", "loglin", "loglog"]
        | Default = Default("linlog"),
        fft2: Boolean = Default(False),
        min_phase: Boolean = Default(False),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Finite Impulse Response Equalizer.

        Args:
            gain: set gain curve (default "gain_interpolate(f)")
            gain_entry: set gain entry
            delay: set delay (from 0 to 1e+10) (default 0.01)
            accuracy: set accuracy (from 0 to 1e+10) (default 5)
            wfunc: set window function (from 0 to 9) (default hann)
            fixed: set fixed frame samples (default false)
            multi: set multi channels mode (default false)
            zero_phase: set zero phase mode (default false)
            scale: set gain scale (from 0 to 3) (default linlog)
            dumpfile: set dump file
            dumpscale: set dump scale (from 0 to 3) (default linlog)
            fft2: set 2-channels fft (default false)
            min_phase: set minimum phase mode (default false)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#firequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="firequalizer", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "gain": gain,
                "gain_entry": gain_entry,
                "delay": delay,
                "accuracy": accuracy,
                "wfunc": wfunc,
                "fixed": fixed,
                "multi": multi,
                "zero_phase": zero_phase,
                "scale": scale,
                "dumpfile": dumpfile,
                "dumpscale": dumpscale,
                "fft2": fft2,
                "min_phase": min_phase,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def flanger(
        self,
        *,
        delay: Double = Default(0.0),
        depth: Double = Default(2.0),
        regen: Double = Default(0.0),
        width: Double = Default(71.0),
        speed: Double = Default(0.5),
        shape: Int | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default(
            "sinusoidal"
        ),
        phase: Double = Default(25.0),
        interp: Int | Literal["linear", "quadratic"] | Default = Default("linear"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a flanging effect to the audio.

        Args:
            delay: base delay in milliseconds (from 0 to 30) (default 0)
            depth: added swept delay in milliseconds (from 0 to 10) (default 2)
            regen: percentage regeneration (delayed signal feedback) (from -95 to 95) (default 0)
            width: percentage of delayed signal mixed with original (from 0 to 100) (default 71)
            speed: sweeps per second (Hz) (from 0.1 to 10) (default 0.5)
            shape: swept wave shape (from 0 to 1) (default sinusoidal)
            phase: swept wave percentage phase-shift for multi-channel (from 0 to 100) (default 25)
            interp: delay-line interpolation (from 0 to 1) (default linear)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#flanger)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="flanger", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "delay": delay,
                "depth": depth,
                "regen": regen,
                "width": width,
                "speed": speed,
                "shape": shape,
                "phase": phase,
                "interp": interp,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def haas(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        side_gain: Double = Default(1.0),
        middle_source: Int
        | Literal["left", "right", "mid", "side"]
        | Default = Default("mid"),
        middle_phase: Boolean = Default(False),
        left_delay: Double = Default(2.05),
        left_balance: Double = Default(-1.0),
        left_gain: Double = Default(1.0),
        left_phase: Boolean = Default(False),
        right_delay: Double = Default(2.12),
        right_balance: Double = Default(1.0),
        right_gain: Double = Default(1.0),
        right_phase: Boolean = Default(True),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply Haas Stereo Enhancer.

        Args:
            level_in: set level in (from 0.015625 to 64) (default 1)
            level_out: set level out (from 0.015625 to 64) (default 1)
            side_gain: set side gain (from 0.015625 to 64) (default 1)
            middle_source: set middle source (from 0 to 3) (default mid)
            middle_phase: set middle phase (default false)
            left_delay: set left delay (from 0 to 40) (default 2.05)
            left_balance: set left balance (from -1 to 1) (default -1)
            left_gain: set left gain (from 0.015625 to 64) (default 1)
            left_phase: set left phase (default false)
            right_delay: set right delay (from 0 to 40) (default 2.12)
            right_balance: set right balance (from -1 to 1) (default 1)
            right_gain: set right gain (from 0.015625 to 64) (default 1)
            right_phase: set right phase (default true)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#haas)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="haas", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "side_gain": side_gain,
                "middle_source": middle_source,
                "middle_phase": middle_phase,
                "left_delay": left_delay,
                "left_balance": left_balance,
                "left_gain": left_gain,
                "left_phase": left_phase,
                "right_delay": right_delay,
                "right_balance": right_balance,
                "right_gain": right_gain,
                "right_phase": right_phase,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def hdcd(
        self,
        *,
        disable_autoconvert: Boolean = Default(True),
        process_stereo: Boolean = Default(True),
        cdt_ms: Int = Default(2000),
        force_pe: Boolean = Default(False),
        analyze_mode: Int
        | Literal["off", "lle", "pe", "cdt", "tgm"]
        | Default = Default("off"),
        bits_per_sample: Int | Literal["16", "20", "24"] | Default = Default(16),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply High Definition Compatible Digital (HDCD) decoding.

        Args:
            disable_autoconvert: Disable any format conversion or resampling in the filter graph. (default true)
            process_stereo: Process stereo channels together. Only apply target_gain when both channels match. (default true)
            cdt_ms: Code detect timer period in ms. (from 100 to 60000) (default 2000)
            force_pe: Always extend peaks above -3dBFS even when PE is not signaled. (default false)
            analyze_mode: Replace audio with solid tone and signal some processing aspect in the amplitude. (from 0 to 4) (default off)
            bits_per_sample: Valid bits per sample (location of the true LSB). (from 16 to 24) (default 16)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hdcd)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hdcd", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "disable_autoconvert": disable_autoconvert,
                "process_stereo": process_stereo,
                "cdt_ms": cdt_ms,
                "force_pe": force_pe,
                "analyze_mode": analyze_mode,
                "bits_per_sample": bits_per_sample,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def highpass(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.707),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a high-pass filter with 3dB point frequency.

        Args:
            frequency: set frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.707)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#highpass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="highpass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def highshelf(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        gain: Double = Default(0.0),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a high shelf filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            gain: set gain (from -900 to 900) (default 0)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="highshelf", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def loudnorm(
        self,
        *,
        I: Double = Default(-24.0),
        LRA: Double = Default(7.0),
        TP: Double = Default(-2.0),
        measured_I: Double = Default(0.0),
        measured_LRA: Double = Default(0.0),
        measured_TP: Double = Default(99.0),
        measured_thresh: Double = Default(-70.0),
        offset: Double = Default(0.0),
        linear: Boolean = Default(True),
        dual_mono: Boolean = Default(False),
        print_format: Int | Literal["none", "json", "summary"] | Default = Default(
            "none"
        ),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        EBU R128 loudness normalization

        Args:
            I: set integrated loudness target (from -70 to -5) (default -24)
            LRA: set loudness range target (from 1 to 50) (default 7)
            TP: set maximum true peak (from -9 to 0) (default -2)
            measured_I: measured IL of input file (from -99 to 0) (default 0)
            measured_LRA: measured LRA of input file (from 0 to 99) (default 0)
            measured_TP: measured true peak of input file (from -99 to 99) (default 99)
            measured_thresh: measured threshold of input file (from -99 to 0) (default -70)
            offset: set offset gain (from -99 to 99) (default 0)
            linear: normalize linearly if possible (default true)
            dual_mono: treat mono input as dual-mono (default false)
            print_format: set print format for stats (from 0 to 2) (default none)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#loudnorm)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="loudnorm", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "I": I,
                "LRA": LRA,
                "TP": TP,
                "measured_I": measured_I,
                "measured_LRA": measured_LRA,
                "measured_TP": measured_TP,
                "measured_thresh": measured_thresh,
                "offset": offset,
                "linear": linear,
                "dual_mono": dual_mono,
                "print_format": print_format,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def lowpass(
        self,
        *,
        frequency: Double = Default(500.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.707),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a low-pass filter with 3dB point frequency.

        Args:
            frequency: set frequency (from 0 to 999999) (default 500)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.707)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lowpass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lowpass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def lowshelf(
        self,
        *,
        frequency: Double = Default(100.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        gain: Double = Default(0.0),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a low shelf filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 100)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            gain: set gain (from -900 to 900) (default 0)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lowshelf", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def mcompand(
        self,
        *,
        args: String = Default(
            "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000"
        ),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Multiband Compress or expand audio dynamic range.

        Args:
            args: set parameters for each band (default "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000")

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mcompand)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="mcompand", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "args": args,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def pan(
        self,
        *,
        args: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remix channels with coefficients (panning).

        Args:
            args:

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pan", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "args": args,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def replaygain(
        self,
        *,
        track_gain: Float = Default(0.0),
        track_peak: Float = Default(0.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        ReplayGain scanner.

        Args:
            track_gain: track gain (dB) (from -FLT_MAX to FLT_MAX) (default 0)
            track_peak: track peak (from -FLT_MAX to FLT_MAX) (default 0)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#replaygain)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="replaygain", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "track_gain": track_gain,
                "track_peak": track_peak,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def rubberband(
        self,
        *,
        tempo: Double = Default(1.0),
        pitch: Double = Default(1.0),
        transients: Int | Literal["crisp", "mixed", "smooth"] | Default = Default(
            "crisp"
        ),
        detector: Int | Literal["compound", "percussive", "soft"] | Default = Default(
            "compound"
        ),
        phase: Int | Literal["laminar", "independent"] | Default = Default("laminar"),
        window: Int | Literal["standard", "short", "long"] | Default = Default(
            "standard"
        ),
        smoothing: Int | Literal["off", "on"] | Default = Default("off"),
        formant: Int | Literal["shifted", "preserved"] | Default = Default("shifted"),
        pitchq: Int | Literal["quality", "speed", "consistency"] | Default = Default(
            "speed"
        ),
        channels: Int | Literal["apart", "together"] | Default = Default("apart"),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply time-stretching and pitch-shifting.

        Args:
            tempo: set tempo scale factor (from 0.01 to 100) (default 1)
            pitch: set pitch scale factor (from 0.01 to 100) (default 1)
            transients: set transients (from 0 to INT_MAX) (default crisp)
            detector: set detector (from 0 to INT_MAX) (default compound)
            phase: set phase (from 0 to INT_MAX) (default laminar)
            window: set window (from 0 to INT_MAX) (default standard)
            smoothing: set smoothing (from 0 to INT_MAX) (default off)
            formant: set formant (from 0 to INT_MAX) (default shifted)
            pitchq: set pitch quality (from 0 to INT_MAX) (default speed)
            channels: set channels (from 0 to INT_MAX) (default apart)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#rubberband)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="rubberband", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "tempo": tempo,
                "pitch": pitch,
                "transients": transients,
                "detector": detector,
                "phase": phase,
                "window": window,
                "smoothing": smoothing,
                "formant": formant,
                "pitchq": pitchq,
                "channels": channels,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def showcqt(
        self,
        *,
        size: Image_size = Default("1920x1080"),
        fps: Video_rate = Default("25"),
        bar_h: Int = Default(-1),
        axis_h: Int = Default(-1),
        sono_h: Int = Default(-1),
        fullhd: Boolean = Default(True),
        sono_v: String = Default("16"),
        bar_v: String = Default("sono_v"),
        sono_g: Float = Default(3.0),
        bar_g: Float = Default(1.0),
        bar_t: Float = Default(1.0),
        timeclamp: Double = Default(0.17),
        attack: Double = Default(0.0),
        basefreq: Double = Default(20.0152),
        endfreq: Double = Default(20495.6),
        coeffclamp: Float = Default(1.0),
        tlength: String = Default("384*tc/(384+tc*f"),
        count: Int = Default(6),
        fcount: Int = Default(0),
        fontfile: String = Default(None),
        font: String = Default(None),
        fontcolor: String = Default("st(0, (midi(f"),
        axisfile: String = Default(None),
        axis: Boolean = Default(True),
        csp: Int
        | Literal[
            "unspecified",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020ncl",
        ]
        | Default = Default("unspecified"),
        cscheme: String = Default("1|0.5|0|0|0.5|1"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output.

        Args:
            size: set video size (default "1920x1080")
            fps: set video rate (default "25")
            bar_h: set bargraph height (from -1 to INT_MAX) (default -1)
            axis_h: set axis height (from -1 to INT_MAX) (default -1)
            sono_h: set sonogram height (from -1 to INT_MAX) (default -1)
            fullhd: set fullhd size (default true)
            sono_v: set sonogram volume (default "16")
            bar_v: set bargraph volume (default "sono_v")
            sono_g: set sonogram gamma (from 1 to 7) (default 3)
            bar_g: set bargraph gamma (from 1 to 7) (default 1)
            bar_t: set bar transparency (from 0 to 1) (default 1)
            timeclamp: set timeclamp (from 0.002 to 1) (default 0.17)
            attack: set attack time (from 0 to 1) (default 0)
            basefreq: set base frequency (from 10 to 100000) (default 20.0152)
            endfreq: set end frequency (from 10 to 100000) (default 20495.6)
            coeffclamp: set coeffclamp (from 0.1 to 10) (default 1)
            tlength: set tlength (default "384*tc/(384+tc*f)")
            count: set transform count (from 1 to 30) (default 6)
            fcount: set frequency count (from 0 to 10) (default 0)
            fontfile: set axis font file
            font: set axis font
            fontcolor: set font color (default "st(0, (midi(f)-59.5)/12);st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));r(1-ld(1)) + b(ld(1))")
            axisfile: set axis image
            axis: draw axis (default true)
            csp: set color space (from 0 to INT_MAX) (default unspecified)
            cscheme: set color scheme (default "1|0.5|0|0|0.5|1")

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showcqt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showcqt", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "fps": fps,
                "bar_h": bar_h,
                "axis_h": axis_h,
                "sono_h": sono_h,
                "fullhd": fullhd,
                "sono_v": sono_v,
                "bar_v": bar_v,
                "sono_g": sono_g,
                "bar_g": bar_g,
                "bar_t": bar_t,
                "timeclamp": timeclamp,
                "attack": attack,
                "basefreq": basefreq,
                "endfreq": endfreq,
                "coeffclamp": coeffclamp,
                "tlength": tlength,
                "count": count,
                "fcount": fcount,
                "fontfile": fontfile,
                "font": font,
                "fontcolor": fontcolor,
                "axisfile": axisfile,
                "axis": axis,
                "csp": csp,
                "cscheme": cscheme,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showcwt(
        self,
        *,
        size: Image_size = Default("640x512"),
        rate: String = Default("25"),
        scale: Int
        | Literal["linear", "log", "bark", "mel", "erbs", "sqrt", "cbrt", "qdrt"]
        | Default = Default("linear"),
        iscale: Int
        | Literal["linear", "log", "sqrt", "cbrt", "qdrt"]
        | Default = Default("log"),
        min: Float = Default(20.0),
        max: Float = Default(20000.0),
        imin: Float = Default(0.0),
        imax: Float = Default(1.0),
        logb: Float = Default(0.0001),
        deviation: Float = Default(1.0),
        pps: Int = Default(64),
        mode: Int
        | Literal["magnitude", "phase", "magphase", "channel", "stereo"]
        | Default = Default("magnitude"),
        slide: Int | Literal["replace", "scroll", "frame"] | Default = Default(
            "replace"
        ),
        direction: Int | Literal["lr", "rl", "ud", "du"] | Default = Default("lr"),
        bar: Float = Default(0.0),
        rotation: Float = Default(0.0),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output.

        Args:
            size: set video size (default "640x512")
            rate: set video rate (default "25")
            scale: set frequency scale (from 0 to 7) (default linear)
            iscale: set intensity scale (from 0 to 4) (default log)
            min: set minimum frequency (from 1 to 192000) (default 20)
            max: set maximum frequency (from 1 to 192000) (default 20000)
            imin: set minimum intensity (from 0 to 1) (default 0)
            imax: set maximum intensity (from 0 to 1) (default 1)
            logb: set logarithmic basis (from 0 to 1) (default 0.0001)
            deviation: set frequency deviation (from 0 to 100) (default 1)
            pps: set pixels per second (from 1 to 1024) (default 64)
            mode: set output mode (from 0 to 4) (default magnitude)
            slide: set slide mode (from 0 to 2) (default replace)
            direction: set direction mode (from 0 to 3) (default lr)
            bar: set bar ratio (from 0 to 1) (default 0)
            rotation: set color rotation (from -1 to 1) (default 0)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showcwt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showcwt", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "rate": rate,
                "scale": scale,
                "iscale": iscale,
                "min": min,
                "max": max,
                "imin": imin,
                "imax": imax,
                "logb": logb,
                "deviation": deviation,
                "pps": pps,
                "mode": mode,
                "slide": slide,
                "direction": direction,
                "bar": bar,
                "rotation": rotation,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showfreqs(
        self,
        *,
        size: Image_size = Default("1024x512"),
        rate: Video_rate = Default("25"),
        mode: Int | Literal["line", "bar", "dot"] | Default = Default("bar"),
        ascale: Int | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("log"),
        fscale: Int | Literal["lin", "log", "rlog"] | Default = Default("lin"),
        win_size: Int = Default(2048),
        win_func: Int
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
        | Default = Default("hann"),
        overlap: Float = Default(1.0),
        averaging: Int = Default(1),
        colors: String = Default(
            "red|green|blue|yellow|orange|lime|pink|magenta|brown"
        ),
        cmode: Int | Literal["combined", "separate"] | Default = Default("combined"),
        minamp: Float = Default(1e-06),
        data: Int | Literal["magnitude", "phase", "delay"] | Default = Default(
            "magnitude"
        ),
        channels: String = Default("all"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a frequencies video output.

        Args:
            size: set video size (default "1024x512")
            rate: set video rate (default "25")
            mode: set display mode (from 0 to 2) (default bar)
            ascale: set amplitude scale (from 0 to 3) (default log)
            fscale: set frequency scale (from 0 to 2) (default lin)
            win_size: set window size (from 16 to 65536) (default 2048)
            win_func: set window function (from 0 to 20) (default hann)
            overlap: set window overlap (from 0 to 1) (default 1)
            averaging: set time averaging (from 0 to INT_MAX) (default 1)
            colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
            cmode: set channel mode (from 0 to 1) (default combined)
            minamp: set minimum amplitude (from FLT_MIN to 1e-06) (default 1e-06)
            data: set data mode (from 0 to 2) (default magnitude)
            channels: set channels to draw (default "all")

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showfreqs)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showfreqs", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "rate": rate,
                "mode": mode,
                "ascale": ascale,
                "fscale": fscale,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "averaging": averaging,
                "colors": colors,
                "cmode": cmode,
                "minamp": minamp,
                "data": data,
                "channels": channels,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showspatial(
        self,
        *,
        size: Image_size = Default("512x512"),
        win_size: Int = Default(4096),
        win_func: Int
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
        | Default = Default("hann"),
        rate: Video_rate = Default("25"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a spatial video output.

        Args:
            size: set video size (default "512x512")
            win_size: set window size (from 1024 to 65536) (default 4096)
            win_func: set window function (from 0 to 20) (default hann)
            rate: set video rate (default "25")

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showspatial)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showspatial", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "win_size": win_size,
                "win_func": win_func,
                "rate": rate,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showspectrum(
        self,
        *,
        size: Image_size = Default("640x512"),
        slide: Int
        | Literal["replace", "scroll", "fullframe", "rscroll", "lreplace"]
        | Default = Default("replace"),
        mode: Int | Literal["combined", "separate"] | Default = Default("combined"),
        color: Int
        | Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | Default = Default("channel"),
        scale: Int
        | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"]
        | Default = Default("sqrt"),
        fscale: Int | Literal["lin", "log"] | Default = Default("lin"),
        saturation: Float = Default(1.0),
        win_func: Int
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
        | Default = Default("hann"),
        orientation: Int | Literal["vertical", "horizontal"] | Default = Default(
            "vertical"
        ),
        overlap: Float = Default(0.0),
        gain: Float = Default(1.0),
        data: Int | Literal["magnitude", "phase", "uphase"] | Default = Default(
            "magnitude"
        ),
        rotation: Float = Default(0.0),
        start: Int = Default(0),
        stop: Int = Default(0),
        fps: String = Default("auto"),
        legend: Boolean = Default(False),
        drange: Float = Default(120.0),
        limit: Float = Default(0.0),
        opacity: Float = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a spectrum video output.

        Args:
            size: set video size (default "640x512")
            slide: set sliding mode (from 0 to 4) (default replace)
            mode: set channel display mode (from 0 to 1) (default combined)
            color: set channel coloring (from 0 to 14) (default channel)
            scale: set display scale (from 0 to 5) (default sqrt)
            fscale: set frequency scale (from 0 to 1) (default lin)
            saturation: color saturation multiplier (from -10 to 10) (default 1)
            win_func: set window function (from 0 to 20) (default hann)
            orientation: set orientation (from 0 to 1) (default vertical)
            overlap: set window overlap (from 0 to 1) (default 0)
            gain: set scale gain (from 0 to 128) (default 1)
            data: set data mode (from 0 to 2) (default magnitude)
            rotation: color rotation (from -1 to 1) (default 0)
            start: start frequency (from 0 to INT_MAX) (default 0)
            stop: stop frequency (from 0 to INT_MAX) (default 0)
            fps: set video rate (default "auto")
            legend: draw legend (default false)
            drange: set dynamic range in dBFS (from 10 to 200) (default 120)
            limit: set upper limit in dBFS (from -100 to 100) (default 0)
            opacity: set opacity strength (from 0 to 10) (default 1)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showspectrum)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showspectrum", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "slide": slide,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "overlap": overlap,
                "gain": gain,
                "data": data,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "fps": fps,
                "legend": legend,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showspectrumpic(
        self,
        *,
        size: Image_size = Default("4096x2048"),
        mode: Int | Literal["combined", "separate"] | Default = Default("combined"),
        color: Int
        | Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | Default = Default("intensity"),
        scale: Int
        | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"]
        | Default = Default("log"),
        fscale: Int | Literal["lin", "log"] | Default = Default("lin"),
        saturation: Float = Default(1.0),
        win_func: Int
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
        | Default = Default("hann"),
        orientation: Int | Literal["vertical", "horizontal"] | Default = Default(
            "vertical"
        ),
        gain: Float = Default(1.0),
        legend: Boolean = Default(True),
        rotation: Float = Default(0.0),
        start: Int = Default(0),
        stop: Int = Default(0),
        drange: Float = Default(120.0),
        limit: Float = Default(0.0),
        opacity: Float = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a spectrum video output single picture.

        Args:
            size: set video size (default "4096x2048")
            mode: set channel display mode (from 0 to 1) (default combined)
            color: set channel coloring (from 0 to 14) (default intensity)
            scale: set display scale (from 0 to 5) (default log)
            fscale: set frequency scale (from 0 to 1) (default lin)
            saturation: color saturation multiplier (from -10 to 10) (default 1)
            win_func: set window function (from 0 to 20) (default hann)
            orientation: set orientation (from 0 to 1) (default vertical)
            gain: set scale gain (from 0 to 128) (default 1)
            legend: draw legend (default true)
            rotation: color rotation (from -1 to 1) (default 0)
            start: start frequency (from 0 to INT_MAX) (default 0)
            stop: stop frequency (from 0 to INT_MAX) (default 0)
            drange: set dynamic range in dBFS (from 10 to 200) (default 120)
            limit: set upper limit in dBFS (from -100 to 100) (default 0)
            opacity: set opacity strength (from 0 to 10) (default 1)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showspectrumpic)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showspectrumpic",
                typings_input=("audio",),
                typings_output=("video",),
            ),
            self,
            **{
                "size": size,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "gain": gain,
                "legend": legend,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showvolume(
        self,
        *,
        rate: Video_rate = Default("25"),
        b: Int = Default(1),
        w: Int = Default(400),
        h: Int = Default(20),
        f: Double = Default(0.95),
        c: String = Default("PEAK*255+floor((1-PEAK"),
        t: Boolean = Default(True),
        v: Boolean = Default(True),
        dm: Double = Default(0.0),
        dmc: Color = Default("orange"),
        o: Int | Literal["h", "v"] | Default = Default("h"),
        s: Int = Default(0),
        p: Float = Default(0.0),
        m: Int | Literal["p", "r"] | Default = Default("p"),
        ds: Int | Literal["lin", "log"] | Default = Default("lin"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio volume to video output.

        Args:
            rate: set video rate (default "25")
            b: set border width (from 0 to 5) (default 1)
            w: set channel width (from 80 to 8192) (default 400)
            h: set channel height (from 1 to 900) (default 20)
            f: set fade (from 0 to 1) (default 0.95)
            c: set volume color expression (default "PEAK*255+floor((1-PEAK)*255)*256+0xff000000")
            t: display channel names (default true)
            v: display volume value (default true)
            dm: duration for max value display (from 0 to 9000) (default 0)
            dmc: set color of the max value line (default "orange")
            o: set orientation (from 0 to 1) (default h)
            s: set step size (from 0 to 5) (default 0)
            p: set background opacity (from 0 to 1) (default 0)
            m: set mode (from 0 to 1) (default p)
            ds: set display scale (from 0 to 1) (default lin)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showvolume)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showvolume", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "rate": rate,
                "b": b,
                "w": w,
                "h": h,
                "f": f,
                "c": c,
                "t": t,
                "v": v,
                "dm": dm,
                "dmc": dmc,
                "o": o,
                "s": s,
                "p": p,
                "m": m,
                "ds": ds,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showwaves(
        self,
        *,
        size: Image_size = Default("600x240"),
        mode: Int | Literal["point", "line", "p2p", "cline"] | Default = Default(
            "point"
        ),
        n: Rational = Default("0/1"),
        rate: Video_rate = Default("25"),
        split_channels: Boolean = Default(False),
        colors: String = Default(
            "red|green|blue|yellow|orange|lime|pink|magenta|brown"
        ),
        scale: Int | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: Int | Literal["scale", "full"] | Default = Default("scale"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a video output.

        Args:
            size: set video size (default "600x240")
            mode: select display mode (from 0 to 3) (default point)
            n: set how many samples to show in the same point (from 0 to INT_MAX) (default 0/1)
            rate: set video rate (default "25")
            split_channels: draw channels separately (default false)
            colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
            scale: set amplitude scale (from 0 to 3) (default lin)
            draw: set draw mode (from 0 to 1) (default scale)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showwaves)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showwaves", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "mode": mode,
                "n": n,
                "rate": rate,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def showwavespic(
        self,
        *,
        size: Image_size = Default("600x240"),
        split_channels: Boolean = Default(False),
        colors: String = Default(
            "red|green|blue|yellow|orange|lime|pink|magenta|brown"
        ),
        scale: Int | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: Int | Literal["scale", "full"] | Default = Default("scale"),
        filter: Int | Literal["average", "peak"] | Default = Default("average"),
        extra_options: dict[str, Any] = None,
    ) -> VideoStream:
        """

        Convert input audio to a video output single picture.

        Args:
            size: set video size (default "600x240")
            split_channels: draw channels separately (default false)
            colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
            scale: set amplitude scale (from 0 to 3) (default lin)
            draw: set draw mode (from 0 to 1) (default scale)
            filter: set filter mode (from 0 to 1) (default average)

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showwavespic)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showwavespic", typings_input=("audio",), typings_output=("video",)
            ),
            self,
            **{
                "size": size,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
                "filter": filter,
            }
            | (extra_options or {}),
        )
        return filter_node.video(0)

    def sidechaincompress(
        self,
        _sidechain: AudioStream,
        *,
        level_in: Double = Default(1.0),
        mode: Int | Literal["downward", "upward"] | Default = Default("downward"),
        threshold: Double = Default(0.125),
        ratio: Double = Default(2.0),
        attack: Double = Default(20.0),
        release: Double = Default(250.0),
        makeup: Double = Default(1.0),
        knee: Double = Default(2.82843),
        link: Int | Literal["average", "maximum"] | Default = Default("average"),
        detection: Int | Literal["peak", "rms"] | Default = Default("rms"),
        level_sc: Double = Default(1.0),
        mix: Double = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Sidechain compressor.

        Args:
            level_in: set input gain (from 0.015625 to 64) (default 1)
            mode: set mode (from 0 to 1) (default downward)
            threshold: set threshold (from 0.000976563 to 1) (default 0.125)
            ratio: set ratio (from 1 to 20) (default 2)
            attack: set attack (from 0.01 to 2000) (default 20)
            release: set release (from 0.01 to 9000) (default 250)
            makeup: set make up gain (from 1 to 64) (default 1)
            knee: set knee (from 1 to 8) (default 2.82843)
            link: set link type (from 0 to 1) (default average)
            detection: set detection (from 0 to 1) (default rms)
            level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
            mix: set mix (from 0 to 1) (default 1)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sidechaincompress",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _sidechain,
            **{
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
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def sidechaingate(
        self,
        _sidechain: AudioStream,
        *,
        level_in: Double = Default(1.0),
        mode: Int | Literal["downward", "upward"] | Default = Default("downward"),
        range: Double = Default(0.06125),
        threshold: Double = Default(0.125),
        ratio: Double = Default(2.0),
        attack: Double = Default(20.0),
        release: Double = Default(250.0),
        makeup: Double = Default(1.0),
        knee: Double = Default(2.82843),
        detection: Int | Literal["peak", "rms"] | Default = Default("rms"),
        link: Int | Literal["average", "maximum"] | Default = Default("average"),
        level_sc: Double = Default(1.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio sidechain gate.

        Args:
            level_in: set input level (from 0.015625 to 64) (default 1)
            mode: set mode (from 0 to 1) (default downward)
            range: set max gain reduction (from 0 to 1) (default 0.06125)
            threshold: set threshold (from 0 to 1) (default 0.125)
            ratio: set ratio (from 1 to 9000) (default 2)
            attack: set attack (from 0.01 to 9000) (default 20)
            release: set release (from 0.01 to 9000) (default 250)
            makeup: set makeup gain (from 1 to 64) (default 1)
            knee: set knee (from 1 to 8) (default 2.82843)
            detection: set detection (from 0 to 1) (default rms)
            link: set link (from 0 to 1) (default average)
            level_sc: set sidechain gain (from 0.015625 to 64) (default 1)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sidechaingate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sidechaingate",
                typings_input=("audio", "audio"),
                typings_output=("audio",),
            ),
            self,
            _sidechain,
            **{
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
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def silencedetect(
        self,
        *,
        n: Double = Default(0.001),
        d: Duration = Default(2.0),
        mono: Boolean = Default(False),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Detect silence.

        Args:
            n: set noise tolerance (from 0 to DBL_MAX) (default 0.001)
            d: set minimum duration in seconds (default 2)
            mono: check each channel separately (default false)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#silencedetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="silencedetect",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "n": n,
                "d": d,
                "mono": mono,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def silenceremove(
        self,
        *,
        start_periods: Int = Default(0),
        start_duration: Duration = Default(0.0),
        start_threshold: Double = Default(0.0),
        start_silence: Duration = Default(0.0),
        start_mode: Int | Literal["any", "all"] | Default = Default("any"),
        stop_periods: Int = Default(0),
        stop_duration: Duration = Default(0.0),
        stop_threshold: Double = Default(0.0),
        stop_silence: Duration = Default(0.0),
        stop_mode: Int | Literal["any", "all"] | Default = Default("all"),
        detection: Int
        | Literal["avg", "rms", "peak", "median", "ptp", "dev"]
        | Default = Default("rms"),
        window: Duration = Default(0.02),
        timestamp: Int | Literal["write", "copy"] | Default = Default("write"),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Remove silence.

        Args:
            start_periods: set periods of silence parts to skip from start (from 0 to 9000) (default 0)
            start_duration: set start duration of non-silence part (default 0)
            start_threshold: set threshold for start silence detection (from 0 to DBL_MAX) (default 0)
            start_silence: set start duration of silence part to keep (default 0)
            start_mode: set which channel will trigger trimming from start (from 0 to 1) (default any)
            stop_periods: set periods of silence parts to skip from end (from -9000 to 9000) (default 0)
            stop_duration: set stop duration of silence part (default 0)
            stop_threshold: set threshold for stop silence detection (from 0 to DBL_MAX) (default 0)
            stop_silence: set stop duration of silence part to keep (default 0)
            stop_mode: set which channel will trigger trimming from end (from 0 to 1) (default all)
            detection: set how silence is detected (from 0 to 5) (default rms)
            window: set duration of window for silence detection (default 0.02)
            timestamp: set how every output frame timestamp is processed (from 0 to 1) (default write)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#silenceremove)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="silenceremove",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "start_periods": start_periods,
                "start_duration": start_duration,
                "start_threshold": start_threshold,
                "start_silence": start_silence,
                "start_mode": start_mode,
                "stop_periods": stop_periods,
                "stop_duration": stop_duration,
                "stop_threshold": stop_threshold,
                "stop_silence": stop_silence,
                "stop_mode": stop_mode,
                "detection": detection,
                "window": window,
                "timestamp": timestamp,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def speechnorm(
        self,
        *,
        peak: Double = Default(0.95),
        expansion: Double = Default(2.0),
        compression: Double = Default(2.0),
        threshold: Double = Default(0.0),
        _raise: Double = Default(0.001),
        fall: Double = Default(0.001),
        channels: String = Default("all"),
        invert: Boolean = Default(False),
        link: Boolean = Default(False),
        rms: Double = Default(0.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Speech Normalizer.

        Args:
            peak: set the peak value (from 0 to 1) (default 0.95)
            expansion: set the max expansion factor (from 1 to 50) (default 2)
            compression: set the max compression factor (from 1 to 50) (default 2)
            threshold: set the threshold value (from 0 to 1) (default 0)
            _raise: set the expansion raising amount (from 0 to 1) (default 0.001)
            fall: set the compression raising amount (from 0 to 1) (default 0.001)
            channels: set channels to filter (default "all")
            invert: set inverted filtering (default false)
            link: set linked channels filtering (default false)
            rms: set the RMS value (from 0 to 1) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#speechnorm)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="speechnorm", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "peak": peak,
                "expansion": expansion,
                "compression": compression,
                "threshold": threshold,
                "raise": _raise,
                "fall": fall,
                "channels": channels,
                "invert": invert,
                "link": link,
                "rms": rms,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def stereotools(
        self,
        *,
        level_in: Double = Default(1.0),
        level_out: Double = Default(1.0),
        balance_in: Double = Default(0.0),
        balance_out: Double = Default(0.0),
        softclip: Boolean = Default(False),
        mutel: Boolean = Default(False),
        muter: Boolean = Default(False),
        phasel: Boolean = Default(False),
        phaser: Boolean = Default(False),
        mode: Int
        | Literal["lr", "ms", "lr", "ll", "rr", "r", "rl", "ll", "rr", "rl", "r"]
        | Default = Default("lr>lr"),
        slev: Double = Default(1.0),
        sbal: Double = Default(0.0),
        mlev: Double = Default(1.0),
        mpan: Double = Default(0.0),
        base: Double = Default(0.0),
        delay: Double = Default(0.0),
        sclevel: Double = Default(1.0),
        phase: Double = Default(0.0),
        bmode_in: Int | Literal["balance", "amplitude", "power"] | Default = Default(
            "balance"
        ),
        bmode_out: Int | Literal["balance", "amplitude", "power"] | Default = Default(
            "balance"
        ),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply various stereo tools.

        Args:
            level_in: set level in (from 0.015625 to 64) (default 1)
            level_out: set level out (from 0.015625 to 64) (default 1)
            balance_in: set balance in (from -1 to 1) (default 0)
            balance_out: set balance out (from -1 to 1) (default 0)
            softclip: enable softclip (default false)
            mutel: mute L (default false)
            muter: mute R (default false)
            phasel: phase L (default false)
            phaser: phase R (default false)
            mode: set stereo mode (from 0 to 10) (default lr>lr)
            slev: set side level (from 0.015625 to 64) (default 1)
            sbal: set side balance (from -1 to 1) (default 0)
            mlev: set middle level (from 0.015625 to 64) (default 1)
            mpan: set middle pan (from -1 to 1) (default 0)
            base: set stereo base (from -1 to 1) (default 0)
            delay: set delay (from -20 to 20) (default 0)
            sclevel: set S/C level (from 1 to 100) (default 1)
            phase: set stereo phase (from 0 to 360) (default 0)
            bmode_in: set balance in mode (from 0 to 2) (default balance)
            bmode_out: set balance out mode (from 0 to 2) (default balance)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#stereotools)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="stereotools", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "level_in": level_in,
                "level_out": level_out,
                "balance_in": balance_in,
                "balance_out": balance_out,
                "softclip": softclip,
                "mutel": mutel,
                "muter": muter,
                "phasel": phasel,
                "phaser": phaser,
                "mode": mode,
                "slev": slev,
                "sbal": sbal,
                "mlev": mlev,
                "mpan": mpan,
                "base": base,
                "delay": delay,
                "sclevel": sclevel,
                "phase": phase,
                "bmode_in": bmode_in,
                "bmode_out": bmode_out,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def stereowiden(
        self,
        *,
        delay: Float = Default(20.0),
        feedback: Float = Default(0.3),
        crossfeed: Float = Default(0.3),
        drymix: Float = Default(0.8),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply stereo widening effect.

        Args:
            delay: set delay time (from 1 to 100) (default 20)
            feedback: set feedback gain (from 0 to 0.9) (default 0.3)
            crossfeed: set cross feed (from 0 to 0.8) (default 0.3)
            drymix: set dry-mix (from 0 to 1) (default 0.8)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#stereowiden)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="stereowiden", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "delay": delay,
                "feedback": feedback,
                "crossfeed": crossfeed,
                "drymix": drymix,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def superequalizer(
        self,
        *,
        _1b: Float = Default(1.0),
        _2b: Float = Default(1.0),
        _3b: Float = Default(1.0),
        _4b: Float = Default(1.0),
        _5b: Float = Default(1.0),
        _6b: Float = Default(1.0),
        _7b: Float = Default(1.0),
        _8b: Float = Default(1.0),
        _9b: Float = Default(1.0),
        _10b: Float = Default(1.0),
        _11b: Float = Default(1.0),
        _12b: Float = Default(1.0),
        _13b: Float = Default(1.0),
        _14b: Float = Default(1.0),
        _15b: Float = Default(1.0),
        _16b: Float = Default(1.0),
        _17b: Float = Default(1.0),
        _18b: Float = Default(1.0),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply 18 band equalization filter.

        Args:
            _1b: set 65Hz band gain (from 0 to 20) (default 1)
            _2b: set 92Hz band gain (from 0 to 20) (default 1)
            _3b: set 131Hz band gain (from 0 to 20) (default 1)
            _4b: set 185Hz band gain (from 0 to 20) (default 1)
            _5b: set 262Hz band gain (from 0 to 20) (default 1)
            _6b: set 370Hz band gain (from 0 to 20) (default 1)
            _7b: set 523Hz band gain (from 0 to 20) (default 1)
            _8b: set 740Hz band gain (from 0 to 20) (default 1)
            _9b: set 1047Hz band gain (from 0 to 20) (default 1)
            _10b: set 1480Hz band gain (from 0 to 20) (default 1)
            _11b: set 2093Hz band gain (from 0 to 20) (default 1)
            _12b: set 2960Hz band gain (from 0 to 20) (default 1)
            _13b: set 4186Hz band gain (from 0 to 20) (default 1)
            _14b: set 5920Hz band gain (from 0 to 20) (default 1)
            _15b: set 8372Hz band gain (from 0 to 20) (default 1)
            _16b: set 11840Hz band gain (from 0 to 20) (default 1)
            _17b: set 16744Hz band gain (from 0 to 20) (default 1)
            _18b: set 20000Hz band gain (from 0 to 20) (default 1)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#superequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="superequalizer",
                typings_input=("audio",),
                typings_output=("audio",),
            ),
            self,
            **{
                "1b": _1b,
                "2b": _2b,
                "3b": _3b,
                "4b": _4b,
                "5b": _5b,
                "6b": _6b,
                "7b": _7b,
                "8b": _8b,
                "9b": _9b,
                "10b": _10b,
                "11b": _11b,
                "12b": _12b,
                "13b": _13b,
                "14b": _14b,
                "15b": _15b,
                "16b": _16b,
                "17b": _17b,
                "18b": _18b,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def surround(
        self,
        *,
        chl_out: String = Default("5.1"),
        chl_in: String = Default("stereo"),
        level_in: Float = Default(1.0),
        level_out: Float = Default(1.0),
        lfe: Boolean = Default(True),
        lfe_low: Int = Default(128),
        lfe_high: Int = Default(256),
        lfe_mode: Int | Literal["add", "sub"] | Default = Default("add"),
        smooth: Float = Default(0.0),
        angle: Float = Default(90.0),
        focus: Float = Default(0.0),
        fc_in: Float = Default(1.0),
        fc_out: Float = Default(1.0),
        fl_in: Float = Default(1.0),
        fl_out: Float = Default(1.0),
        fr_in: Float = Default(1.0),
        fr_out: Float = Default(1.0),
        sl_in: Float = Default(1.0),
        sl_out: Float = Default(1.0),
        sr_in: Float = Default(1.0),
        sr_out: Float = Default(1.0),
        bl_in: Float = Default(1.0),
        bl_out: Float = Default(1.0),
        br_in: Float = Default(1.0),
        br_out: Float = Default(1.0),
        bc_in: Float = Default(1.0),
        bc_out: Float = Default(1.0),
        lfe_in: Float = Default(1.0),
        lfe_out: Float = Default(1.0),
        allx: Float = Default(-1.0),
        ally: Float = Default(-1.0),
        fcx: Float = Default(0.5),
        flx: Float = Default(0.5),
        frx: Float = Default(0.5),
        blx: Float = Default(0.5),
        brx: Float = Default(0.5),
        slx: Float = Default(0.5),
        srx: Float = Default(0.5),
        bcx: Float = Default(0.5),
        fcy: Float = Default(0.5),
        fly: Float = Default(0.5),
        fry: Float = Default(0.5),
        bly: Float = Default(0.5),
        bry: Float = Default(0.5),
        sly: Float = Default(0.5),
        sry: Float = Default(0.5),
        bcy: Float = Default(0.5),
        win_size: Int = Default(4096),
        win_func: Int
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
        | Default = Default("hann"),
        overlap: Float = Default(0.5),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply audio surround upmix filter.

        Args:
            chl_out: set output channel layout (default "5.1")
            chl_in: set input channel layout (default "stereo")
            level_in: set input level (from 0 to 10) (default 1)
            level_out: set output level (from 0 to 10) (default 1)
            lfe: output LFE (default true)
            lfe_low: LFE low cut off (from 0 to 256) (default 128)
            lfe_high: LFE high cut off (from 0 to 512) (default 256)
            lfe_mode: set LFE channel mode (from 0 to 1) (default add)
            smooth: set temporal smoothness strength (from 0 to 1) (default 0)
            angle: set soundfield transform angle (from 0 to 360) (default 90)
            focus: set soundfield transform focus (from -1 to 1) (default 0)
            fc_in: set front center channel input level (from 0 to 10) (default 1)
            fc_out: set front center channel output level (from 0 to 10) (default 1)
            fl_in: set front left channel input level (from 0 to 10) (default 1)
            fl_out: set front left channel output level (from 0 to 10) (default 1)
            fr_in: set front right channel input level (from 0 to 10) (default 1)
            fr_out: set front right channel output level (from 0 to 10) (default 1)
            sl_in: set side left channel input level (from 0 to 10) (default 1)
            sl_out: set side left channel output level (from 0 to 10) (default 1)
            sr_in: set side right channel input level (from 0 to 10) (default 1)
            sr_out: set side right channel output level (from 0 to 10) (default 1)
            bl_in: set back left channel input level (from 0 to 10) (default 1)
            bl_out: set back left channel output level (from 0 to 10) (default 1)
            br_in: set back right channel input level (from 0 to 10) (default 1)
            br_out: set back right channel output level (from 0 to 10) (default 1)
            bc_in: set back center channel input level (from 0 to 10) (default 1)
            bc_out: set back center channel output level (from 0 to 10) (default 1)
            lfe_in: set lfe channel input level (from 0 to 10) (default 1)
            lfe_out: set lfe channel output level (from 0 to 10) (default 1)
            allx: set all channel's x spread (from -1 to 15) (default -1)
            ally: set all channel's y spread (from -1 to 15) (default -1)
            fcx: set front center channel x spread (from 0.06 to 15) (default 0.5)
            flx: set front left channel x spread (from 0.06 to 15) (default 0.5)
            frx: set front right channel x spread (from 0.06 to 15) (default 0.5)
            blx: set back left channel x spread (from 0.06 to 15) (default 0.5)
            brx: set back right channel x spread (from 0.06 to 15) (default 0.5)
            slx: set side left channel x spread (from 0.06 to 15) (default 0.5)
            srx: set side right channel x spread (from 0.06 to 15) (default 0.5)
            bcx: set back center channel x spread (from 0.06 to 15) (default 0.5)
            fcy: set front center channel y spread (from 0.06 to 15) (default 0.5)
            fly: set front left channel y spread (from 0.06 to 15) (default 0.5)
            fry: set front right channel y spread (from 0.06 to 15) (default 0.5)
            bly: set back left channel y spread (from 0.06 to 15) (default 0.5)
            bry: set back right channel y spread (from 0.06 to 15) (default 0.5)
            sly: set side left channel y spread (from 0.06 to 15) (default 0.5)
            sry: set side right channel y spread (from 0.06 to 15) (default 0.5)
            bcy: set back center channel y spread (from 0.06 to 15) (default 0.5)
            win_size: set window size (from 1024 to 65536) (default 4096)
            win_func: set window function (from 0 to 20) (default hann)
            overlap: set window overlap (from 0 to 1) (default 0.5)

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#surround)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="surround", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "chl_out": chl_out,
                "chl_in": chl_in,
                "level_in": level_in,
                "level_out": level_out,
                "lfe": lfe,
                "lfe_low": lfe_low,
                "lfe_high": lfe_high,
                "lfe_mode": lfe_mode,
                "smooth": smooth,
                "angle": angle,
                "focus": focus,
                "fc_in": fc_in,
                "fc_out": fc_out,
                "fl_in": fl_in,
                "fl_out": fl_out,
                "fr_in": fr_in,
                "fr_out": fr_out,
                "sl_in": sl_in,
                "sl_out": sl_out,
                "sr_in": sr_in,
                "sr_out": sr_out,
                "bl_in": bl_in,
                "bl_out": bl_out,
                "br_in": br_in,
                "br_out": br_out,
                "bc_in": bc_in,
                "bc_out": bc_out,
                "lfe_in": lfe_in,
                "lfe_out": lfe_out,
                "allx": allx,
                "ally": ally,
                "fcx": fcx,
                "flx": flx,
                "frx": frx,
                "blx": blx,
                "brx": brx,
                "slx": slx,
                "srx": srx,
                "bcx": bcx,
                "fcy": fcy,
                "fly": fly,
                "fry": fry,
                "bly": bly,
                "bry": bry,
                "sly": sly,
                "sry": sry,
                "bcy": bcy,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def tiltshelf(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        gain: Double = Default(0.0),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply a tilt shelf filter.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            gain: set gain (from -900 to 900) (default 0)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tiltshelf)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tiltshelf", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def treble(
        self,
        *,
        frequency: Double = Default(3000.0),
        width_type: Int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: Double = Default(0.5),
        gain: Double = Default(0.0),
        poles: Int = Default(2),
        mix: Double = Default(1.0),
        channels: String = Default("all"),
        normalize: Boolean = Default(False),
        transform: Int
        | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | Default = Default("di"),
        precision: Int
        | Literal["auto", "s16", "s32", "f32", "f64"]
        | Default = Default("auto"),
        blocksize: Int = Default(0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Boost or cut upper frequencies.

        Args:
            frequency: set central frequency (from 0 to 999999) (default 3000)
            width_type: set filter-width type (from 1 to 5) (default q)
            width: set width (from 0 to 99999) (default 0.5)
            gain: set gain (from -900 to 900) (default 0)
            poles: set number of poles (from 1 to 2) (default 2)
            mix: set mix (from 0 to 1) (default 1)
            channels: set channels to filter (default "all")
            normalize: normalize coefficients (default false)
            transform: set transform type (from 0 to 6) (default di)
            precision: set filtering precision (from -1 to 3) (default auto)
            blocksize: set the block size (from 0 to 32768) (default 0)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="treble", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "gain": gain,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def tremolo(
        self,
        *,
        f: Double = Default(5.0),
        d: Double = Default(0.5),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply tremolo effect.

        Args:
            f: set frequency in hertz (from 0.1 to 20000) (default 5)
            d: set depth as percentage (from 0 to 1) (default 0.5)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tremolo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tremolo", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "f": f,
                "d": d,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def vibrato(
        self,
        *,
        f: Double = Default(5.0),
        d: Double = Default(0.5),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Apply vibrato effect.

        Args:
            f: set frequency in hertz (from 0.1 to 20000) (default 5)
            d: set depth as percentage (from 0 to 1) (default 0.5)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vibrato)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vibrato", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "f": f,
                "d": d,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def virtualbass(
        self,
        *,
        cutoff: Double = Default(250.0),
        strength: Double = Default(3.0),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Audio Virtual Bass.

        Args:
            cutoff: set virtual bass cutoff (from 100 to 500) (default 250)
            strength: set virtual bass strength (from 0.5 to 3) (default 3)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#virtualbass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="virtualbass", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "cutoff": cutoff,
                "strength": strength,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def volume(
        self,
        *,
        volume: String = Default("1.0"),
        precision: Int | Literal["fixed", "float", "double"] | Default = Default(
            "float"
        ),
        eval: Int | Literal["once", "frame"] | Default = Default("once"),
        replaygain: Int
        | Literal["drop", "ignore", "track", "album"]
        | Default = Default("drop"),
        replaygain_preamp: Double = Default(0.0),
        replaygain_noclip: Boolean = Default(True),
        enable: String = Default(None),
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Change input volume.

        Args:
            volume: set volume adjustment expression (default "1.0")
            precision: select mathematical precision (from 0 to 2) (default float)
            eval: specify when to evaluate expressions (from 0 to 1) (default once)
            replaygain: Apply replaygain side data when present (from 0 to 3) (default drop)
            replaygain_preamp: Apply replaygain pre-amplification (from -15 to 15) (default 0)
            replaygain_noclip: Apply replaygain clipping prevention (default true)
            enable: timeline editing

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#volume)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="volume", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{
                "volume": volume,
                "precision": precision,
                "eval": eval,
                "replaygain": replaygain,
                "replaygain_preamp": replaygain_preamp,
                "replaygain_noclip": replaygain_noclip,
                "enable": enable,
            }
            | (extra_options or {}),
        )
        return filter_node.audio(0)

    def volumedetect(
        self,
        extra_options: dict[str, Any] = None,
    ) -> AudioStream:
        """

        Detect audio volume.

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#volumedetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="volumedetect", typings_input=("audio",), typings_output=("audio",)
            ),
            self,
            **{} | (extra_options or {}),
        )
        return filter_node.audio(0)
