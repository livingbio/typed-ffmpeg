from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Literal

from ..nodes.nodes import FilterableStream, FilterNode
from ..schema import (
    BOOLEAN,
    COLOR,
    DOUBLE,
    DURATION,
    FLAGS,
    FLOAT,
    IMAGE_SIZE,
    INT,
    INT64,
    STRING,
    VIDEO_RATE,
    Default,
    StreamType,
)
from .channel_layout import CHANNEL_LAYOUT

if TYPE_CHECKING:
    from .video import VideoStream


class AudioStream(FilterableStream):
    @property
    def video(self) -> "VideoStream":
        raise NotImplementedError("This stream does not have a video component")

    @property
    def audio(self) -> "AudioStream":
        return AudioStream(node=self.node, selector=StreamType.audio, index=self.index)

    def a3dscope(
        self,
        *,
        rate: VIDEO_RATE = Default("25"),
        size: IMAGE_SIZE = Default("hd720"),
        fov: FLOAT = Default("90"),
        roll: FLOAT = Default("0"),
        pitch: FLOAT = Default("0"),
        yaw: FLOAT = Default("0"),
        xzoom: FLOAT = Default("1"),
        xpos: FLOAT = Default("0"),
        length: INT = Default("15"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to 3d scope video output.

        Parameters:
        ----------

        :param VIDEO_RATE rate: set video rate (default "25")
        :param IMAGE_SIZE size: set video size (default "hd720")
        :param FLOAT fov: set camera FoV (from 40 to 150) (default 90)
        :param FLOAT roll: set camera roll (from -180 to 180) (default 0)
        :param FLOAT pitch: set camera pitch (from -180 to 180) (default 0)
        :param FLOAT yaw: set camera yaw (from -180 to 180) (default 0)
        :param FLOAT xzoom: set camera zoom (from 0.01 to 10) (default 1)
        :param FLOAT xpos: set camera position (from -60 to 60) (default 0)
        :param INT length: set length (from 1 to 60) (default 15)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#a3dscope

        """
        filter_node = FilterNode(
            name="a3dscope",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def abench(
        self, *, action: INT | Literal["start", "stop"] | Default = Default("start"), **kwargs: Any
    ) -> "AudioStream":
        """

        Benchmark part of a filtergraph.

        Parameters:
        ----------

        :param INT action: set action (from 0 to 1) (default start)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench

        """
        filter_node = FilterNode(
            name="abench",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "action": action,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def abitscope(
        self,
        *,
        rate: VIDEO_RATE = Default("25"),
        size: IMAGE_SIZE = Default("1024x256"),
        colors: STRING = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        mode: INT | Literal["bars", "trace"] | Default = Default("bars"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to audio bit scope video output.

        Parameters:
        ----------

        :param VIDEO_RATE rate: set video rate (default "25")
        :param IMAGE_SIZE size: set video size (default "1024x256")
        :param STRING colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param INT mode: set output mode (from 0 to 1) (default bars)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#abitscope

        """
        filter_node = FilterNode(
            name="abitscope",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rate": rate,
                        "size": size,
                        "colors": colors,
                        "mode": mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def acompressor(
        self,
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
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio compressor.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acompressor

        """
        filter_node = FilterNode(
            name="acompressor",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
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

    def acontrast(self, *, contrast: FLOAT = Default("33"), **kwargs: Any) -> "AudioStream":
        """

        Simple audio dynamic range compression/expansion filter.

        Parameters:
        ----------

        :param FLOAT contrast: set contrast (from 0 to 100) (default 33)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acontrast

        """
        filter_node = FilterNode(
            name="acontrast",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "contrast": contrast,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def acopy(self, **kwargs: Any) -> "AudioStream":
        """

        Copy the input audio unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#acopy

        """
        filter_node = FilterNode(
            name="acopy",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def acrossfade(
        self,
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
        **kwargs: Any,
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
                self,
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

    def acrossover(
        self,
        *,
        split: STRING = Default("500"),
        order: INT
        | Literal["2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"]
        | Default = Default("4th"),
        level: FLOAT = Default("1"),
        gain: STRING = Default("1.f"),
        precision: INT | Literal["auto", "float", "double"] | Default = Default("auto"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Split audio into per-bands streams.

        Parameters:
        ----------

        :param STRING split: set split frequencies (default "500")
        :param INT order: set filter order (from 0 to 9) (default 4th)
        :param FLOAT level: set input gain (from 0 to 1) (default 1)
        :param STRING gain: set output bands gain (default "1.f")
        :param INT precision: set processing precision (from 0 to 2) (default auto)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossover

        """
        filter_node = FilterNode(
            name="acrossover",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] * len(re.split(r"[ |]+", str(split)))),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "split": split,
                        "order": order,
                        "level": level,
                        "gain": gain,
                        "precision": precision,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def acrusher(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        bits: DOUBLE = Default("8"),
        mix: DOUBLE = Default("0.5"),
        mode: INT | Literal["lin", "log"] | Default = Default("lin"),
        dc: DOUBLE = Default("1"),
        aa: DOUBLE = Default("0.5"),
        samples: DOUBLE = Default("1"),
        lfo: BOOLEAN = Default("false"),
        lforange: DOUBLE = Default("20"),
        lforate: DOUBLE = Default("0.3"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Reduce audio bit resolution.

        Parameters:
        ----------

        :param DOUBLE level_in: set level in (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set level out (from 0.015625 to 64) (default 1)
        :param DOUBLE bits: set bit reduction (from 1 to 64) (default 8)
        :param DOUBLE mix: set mix (from 0 to 1) (default 0.5)
        :param INT mode: set mode (from 0 to 1) (default lin)
        :param DOUBLE dc: set DC (from 0.25 to 4) (default 1)
        :param DOUBLE aa: set anti-aliasing (from 0 to 1) (default 0.5)
        :param DOUBLE samples: set sample reduction (from 1 to 250) (default 1)
        :param BOOLEAN lfo: enable LFO (default false)
        :param DOUBLE lforange: set LFO depth (from 1 to 250) (default 20)
        :param DOUBLE lforate: set LFO rate (from 0.01 to 200) (default 0.3)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrusher

        """
        filter_node = FilterNode(
            name="acrusher",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def acue(
        self,
        *,
        cue: INT64 = Default("0"),
        preroll: DURATION = Default("0"),
        buffer: DURATION = Default("0"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Delay filtering to match a cue.

        Parameters:
        ----------

        :param INT64 cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
        :param DURATION preroll: preroll duration in seconds (default 0)
        :param DURATION buffer: buffer duration in seconds (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acue

        """
        filter_node = FilterNode(
            name="acue",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cue": cue,
                        "preroll": preroll,
                        "buffer": buffer,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adeclick(
        self,
        *,
        window: DOUBLE = Default("55"),
        overlap: DOUBLE = Default("75"),
        arorder: DOUBLE = Default("2"),
        threshold: DOUBLE = Default("2"),
        burst: DOUBLE = Default("2"),
        method: INT | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove impulsive noise from input audio.

        Parameters:
        ----------

        :param DOUBLE window: set window size (from 10 to 100) (default 55)
        :param DOUBLE overlap: set window overlap (from 50 to 95) (default 75)
        :param DOUBLE arorder: set autoregression order (from 0 to 25) (default 2)
        :param DOUBLE threshold: set threshold (from 1 to 100) (default 2)
        :param DOUBLE burst: set burst fusion (from 0 to 10) (default 2)
        :param INT method: set overlap method (from 0 to 1) (default add)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclick

        """
        filter_node = FilterNode(
            name="adeclick",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "window": window,
                        "overlap": overlap,
                        "arorder": arorder,
                        "threshold": threshold,
                        "burst": burst,
                        "method": method,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adeclip(
        self,
        *,
        window: DOUBLE = Default("55"),
        overlap: DOUBLE = Default("75"),
        arorder: DOUBLE = Default("8"),
        threshold: DOUBLE = Default("10"),
        hsize: INT = Default("1000"),
        method: INT | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove clipping from input audio.

        Parameters:
        ----------

        :param DOUBLE window: set window size (from 10 to 100) (default 55)
        :param DOUBLE overlap: set window overlap (from 50 to 95) (default 75)
        :param DOUBLE arorder: set autoregression order (from 0 to 25) (default 8)
        :param DOUBLE threshold: set threshold (from 1 to 100) (default 10)
        :param INT hsize: set histogram size (from 100 to 9999) (default 1000)
        :param INT method: set overlap method (from 0 to 1) (default add)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclip

        """
        filter_node = FilterNode(
            name="adeclip",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "window": window,
                        "overlap": overlap,
                        "arorder": arorder,
                        "threshold": threshold,
                        "hsize": hsize,
                        "method": method,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adecorrelate(
        self, *, stages: INT = Default("6"), seed: INT64 = Default("-1"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Apply decorrelation to input audio.

        Parameters:
        ----------

        :param INT stages: set filtering stages (from 1 to 16) (default 6)
        :param INT64 seed: set random seed (from -1 to UINT32_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adecorrelate

        """
        filter_node = FilterNode(
            name="adecorrelate",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "stages": stages,
                        "seed": seed,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adelay(
        self,
        *,
        delays: STRING = Default(None),
        all: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Delay one or more audio channels.

        Parameters:
        ----------

        :param STRING delays: set list of delays for each channel
        :param BOOLEAN all: use last available delay for remained channels (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adelay

        """
        filter_node = FilterNode(
            name="adelay",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "delays": delays,
                        "all": all,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adenorm(
        self,
        *,
        level: DOUBLE = Default("-351"),
        type: INT | Literal["dc", "ac", "square", "pulse"] | Default = Default("dc"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remedy denormals by adding extremely low-level noise.

        Parameters:
        ----------

        :param DOUBLE level: set level (from -451 to -90) (default -351)
        :param INT type: set type (from 0 to 3) (default dc)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adenorm

        """
        filter_node = FilterNode(
            name="adenorm",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "level": level,
                        "type": type,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aderivative(self, *, enable: str = Default(None), **kwargs: Any) -> "AudioStream":
        """

        Compute derivative of input audio.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        filter_node = FilterNode(
            name="aderivative",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
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

    def adrawgraph(
        self,
        *,
        m1: STRING = Default(""),
        fg1: STRING = Default("0xffff0000"),
        m2: STRING = Default(""),
        fg2: STRING = Default("0xff00ff00"),
        m3: STRING = Default(""),
        fg3: STRING = Default("0xffff00ff"),
        m4: STRING = Default(""),
        fg4: STRING = Default("0xffffff00"),
        bg: COLOR = Default("white"),
        min: FLOAT = Default("-1"),
        max: FLOAT = Default("1"),
        mode: INT | Literal["bar", "dot", "line"] | Default = Default("line"),
        slide: INT | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default("frame"),
        size: IMAGE_SIZE = Default("900x256"),
        rate: VIDEO_RATE = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a graph using input audio metadata.

        Parameters:
        ----------

        :param STRING m1: set 1st metadata key (default "")
        :param STRING fg1: set 1st foreground color expression (default "0xffff0000")
        :param STRING m2: set 2nd metadata key (default "")
        :param STRING fg2: set 2nd foreground color expression (default "0xff00ff00")
        :param STRING m3: set 3rd metadata key (default "")
        :param STRING fg3: set 3rd foreground color expression (default "0xffff00ff")
        :param STRING m4: set 4th metadata key (default "")
        :param STRING fg4: set 4th foreground color expression (default "0xffffff00")
        :param COLOR bg: set background color (default "white")
        :param FLOAT min: set minimal value (from INT_MIN to INT_MAX) (default -1)
        :param FLOAT max: set maximal value (from INT_MIN to INT_MAX) (default 1)
        :param INT mode: set graph mode (from 0 to 2) (default line)
        :param INT slide: set slide mode (from 0 to 4) (default frame)
        :param IMAGE_SIZE size: set graph size (default "900x256")
        :param VIDEO_RATE rate: set video rate (default "25")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adrawgraph

        """
        filter_node = FilterNode(
            name="adrawgraph",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def adrc(
        self,
        *,
        transfer: STRING = Default("p"),
        attack: DOUBLE = Default("50"),
        release: DOUBLE = Default("100"),
        channels: STRING = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Spectral Dynamic Range Controller.

        Parameters:
        ----------

        :param STRING transfer: set the transfer expression (default "p")
        :param DOUBLE attack: set the attack (from 1 to 1000) (default 50)
        :param DOUBLE release: set the release (from 5 to 2000) (default 100)
        :param STRING channels: set channels to filter (default "all")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adrc

        """
        filter_node = FilterNode(
            name="adrc",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "transfer": transfer,
                        "attack": attack,
                        "release": release,
                        "channels": channels,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adynamicequalizer(
        self,
        *,
        threshold: DOUBLE = Default("0"),
        dfrequency: DOUBLE = Default("1000"),
        dqfactor: DOUBLE = Default("1"),
        tfrequency: DOUBLE = Default("1000"),
        tqfactor: DOUBLE = Default("1"),
        attack: DOUBLE = Default("20"),
        release: DOUBLE = Default("200"),
        ratio: DOUBLE = Default("1"),
        makeup: DOUBLE = Default("0"),
        range: DOUBLE = Default("50"),
        mode: INT | Literal["listen", "cut", "boost"] | Default = Default("cut"),
        tftype: INT | Literal["bell", "lowshelf", "highshelf"] | Default = Default("bell"),
        direction: INT | Literal["downward", "upward"] | Default = Default("downward"),
        auto: INT | Literal["disabled", "off", "on"] | Default = Default("disabled"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Dynamic Equalization of input audio.

        Parameters:
        ----------

        :param DOUBLE threshold: set detection threshold (from 0 to 100) (default 0)
        :param DOUBLE dfrequency: set detection frequency (from 2 to 1e+06) (default 1000)
        :param DOUBLE dqfactor: set detection Q factor (from 0.001 to 1000) (default 1)
        :param DOUBLE tfrequency: set target frequency (from 2 to 1e+06) (default 1000)
        :param DOUBLE tqfactor: set target Q factor (from 0.001 to 1000) (default 1)
        :param DOUBLE attack: set attack duration (from 1 to 2000) (default 20)
        :param DOUBLE release: set release duration (from 1 to 2000) (default 200)
        :param DOUBLE ratio: set ratio factor (from 0 to 30) (default 1)
        :param DOUBLE makeup: set makeup gain (from 0 to 100) (default 0)
        :param DOUBLE range: set max gain (from 1 to 200) (default 50)
        :param INT mode: set mode (from -1 to 1) (default cut)
        :param INT tftype: set target filter type (from 0 to 2) (default bell)
        :param INT direction: set direction (from 0 to 1) (default downward)
        :param INT auto: set auto threshold (from -1 to 1) (default disabled)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer

        """
        filter_node = FilterNode(
            name="adynamicequalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                        "tftype": tftype,
                        "direction": direction,
                        "auto": auto,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def adynamicsmooth(
        self,
        *,
        sensitivity: DOUBLE = Default("2"),
        basefreq: DOUBLE = Default("22050"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Dynamic Smoothing of input audio.

        Parameters:
        ----------

        :param DOUBLE sensitivity: set smooth sensitivity (from 0 to 1e+06) (default 2)
        :param DOUBLE basefreq: set base frequency (from 2 to 1e+06) (default 22050)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth

        """
        filter_node = FilterNode(
            name="adynamicsmooth",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sensitivity": sensitivity,
                        "basefreq": basefreq,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aecho(
        self,
        *,
        in_gain: FLOAT = Default("0.6"),
        out_gain: FLOAT = Default("0.3"),
        delays: STRING = Default("1000"),
        decays: STRING = Default("0.5"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add echoing to the audio.

        Parameters:
        ----------

        :param FLOAT in_gain: set signal input gain (from 0 to 1) (default 0.6)
        :param FLOAT out_gain: set signal output gain (from 0 to 1) (default 0.3)
        :param STRING delays: set list of signal delays (default "1000")
        :param STRING decays: set list of signal decays (default "0.5")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aecho

        """
        filter_node = FilterNode(
            name="aecho",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "in_gain": in_gain,
                        "out_gain": out_gain,
                        "delays": delays,
                        "decays": decays,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aemphasis(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        mode: INT | Literal["reproduction", "production"] | Default = Default("reproduction"),
        type: INT
        | Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"]
        | Default = Default("cd"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio emphasis.

        Parameters:
        ----------

        :param DOUBLE level_in: set input gain (from 0 to 64) (default 1)
        :param DOUBLE level_out: set output gain (from 0 to 64) (default 1)
        :param INT mode: set filter mode (from 0 to 1) (default reproduction)
        :param INT type: set filter type (from 0 to 8) (default cd)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aemphasis

        """
        filter_node = FilterNode(
            name="aemphasis",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "level_in": level_in,
                        "level_out": level_out,
                        "mode": mode,
                        "type": type,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aeval(
        self,
        *,
        exprs: STRING = Default(None),
        channel_layout: STRING = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Filter audio signal according to a specified expression.

        Parameters:
        ----------

        :param STRING exprs: set the '|'-separated list of channels expressions
        :param STRING channel_layout: set channel layout
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aeval

        """
        filter_node = FilterNode(
            name="aeval",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "exprs": exprs,
                        "channel_layout": channel_layout,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aexciter(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        amount: DOUBLE = Default("1"),
        drive: DOUBLE = Default("8.5"),
        blend: DOUBLE = Default("0"),
        freq: DOUBLE = Default("7500"),
        ceil: DOUBLE = Default("9999"),
        listen: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Enhance high frequency part of audio.

        Parameters:
        ----------

        :param DOUBLE level_in: set level in (from 0 to 64) (default 1)
        :param DOUBLE level_out: set level out (from 0 to 64) (default 1)
        :param DOUBLE amount: set amount (from 0 to 64) (default 1)
        :param DOUBLE drive: set harmonics (from 0.1 to 10) (default 8.5)
        :param DOUBLE blend: set blend harmonics (from -10 to 10) (default 0)
        :param DOUBLE freq: set scope (from 2000 to 12000) (default 7500)
        :param DOUBLE ceil: set ceiling (from 9999 to 20000) (default 9999)
        :param BOOLEAN listen: enable listen mode (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aexciter

        """
        filter_node = FilterNode(
            name="aexciter",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afade(
        self,
        *,
        type: INT | Literal["in", "out"] | Default = Default("in"),
        start_sample: INT64 = Default("0"),
        nb_samples: INT64 = Default("44100"),
        start_time: DURATION = Default("0"),
        duration: DURATION = Default("0"),
        curve: INT
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
        silence: DOUBLE = Default("0"),
        unity: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Fade in/out input audio.

        Parameters:
        ----------

        :param INT type: set the fade direction (from 0 to 1) (default in)
        :param INT64 start_sample: set number of first sample to start fading (from 0 to I64_MAX) (default 0)
        :param INT64 nb_samples: set number of samples for fade duration (from 1 to I64_MAX) (default 44100)
        :param DURATION start_time: set time to start fading (default 0)
        :param DURATION duration: set fade duration (default 0)
        :param INT curve: set fade curve type (from -1 to 18) (default tri)
        :param DOUBLE silence: set the silence gain (from 0 to 1) (default 0)
        :param DOUBLE unity: set the unity gain (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afade

        """
        filter_node = FilterNode(
            name="afade",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afftdn(
        self,
        *,
        noise_reduction: FLOAT = Default("12"),
        noise_floor: FLOAT = Default("-50"),
        noise_type: INT
        | Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | Default = Default("white"),
        band_noise: STRING = Default(None),
        residual_floor: FLOAT = Default("-38"),
        track_noise: BOOLEAN = Default("false"),
        track_residual: BOOLEAN = Default("false"),
        output_mode: INT | Literal["input", "i", "output", "o", "noise", "n"] | Default = Default("output"),
        adaptivity: FLOAT = Default("0.5"),
        floor_offset: FLOAT = Default("1"),
        noise_link: INT | Literal["none", "min", "max", "average"] | Default = Default("min"),
        band_multiplier: FLOAT = Default("1.25"),
        sample_noise: INT | Literal["none", "start", "begin", "stop", "end"] | Default = Default("none"),
        gain_smooth: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Denoise audio samples using FFT.

        Parameters:
        ----------

        :param FLOAT noise_reduction: set the noise reduction (from 0.01 to 97) (default 12)
        :param FLOAT noise_floor: set the noise floor (from -80 to -20) (default -50)
        :param INT noise_type: set the noise type (from 0 to 3) (default white)
        :param STRING band_noise: set the custom bands noise
        :param FLOAT residual_floor: set the residual floor (from -80 to -20) (default -38)
        :param BOOLEAN track_noise: track noise (default false)
        :param BOOLEAN track_residual: track residual (default false)
        :param INT output_mode: set output mode (from 0 to 2) (default output)
        :param FLOAT adaptivity: set adaptivity factor (from 0 to 1) (default 0.5)
        :param FLOAT floor_offset: set noise floor offset factor (from -2 to 2) (default 1)
        :param INT noise_link: set the noise floor link (from 0 to 3) (default min)
        :param FLOAT band_multiplier: set band multiplier (from 0.2 to 5) (default 1.25)
        :param INT sample_noise: set sample noise mode (from 0 to 2) (default none)
        :param INT gain_smooth: set gain smooth radius (from 0 to 50) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftdn

        """
        filter_node = FilterNode(
            name="afftdn",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afftfilt(
        self,
        *,
        real: STRING = Default("re"),
        imag: STRING = Default("im"),
        win_size: INT = Default("4096"),
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
        | Default = Default("hann"),
        overlap: FLOAT = Default("0.75"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply arbitrary expressions to samples in frequency domain.

        Parameters:
        ----------

        :param STRING real: set channels real expressions (default "re")
        :param STRING imag: set channels imaginary expressions (default "im")
        :param INT win_size: set window size (from 16 to 131072) (default 4096)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param FLOAT overlap: set window overlap (from 0 to 1) (default 0.75)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftfilt

        """
        filter_node = FilterNode(
            name="afftfilt",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "real": real,
                        "imag": imag,
                        "win_size": win_size,
                        "win_func": win_func,
                        "overlap": overlap,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afifo(self, **kwargs: Any) -> "AudioStream":
        """

        Buffer input frames and send them when they are requested.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#fifo_002c-afifo

        """
        filter_node = FilterNode(
            name="afifo",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def aformat(
        self,
        *,
        sample_fmts: STRING = Default(None),
        sample_rates: STRING = Default(None),
        channel_layouts: STRING = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Convert the input audio to one of the specified formats.

        Parameters:
        ----------

        :param STRING sample_fmts: A '|'-separated list of sample formats.
        :param STRING sample_rates: A '|'-separated list of sample rates.
        :param STRING channel_layouts: A '|'-separated list of channel layouts.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aformat

        """
        filter_node = FilterNode(
            name="aformat",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sample_fmts": sample_fmts,
                        "sample_rates": sample_rates,
                        "channel_layouts": channel_layouts,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afreqshift(
        self,
        *,
        shift: DOUBLE = Default("0"),
        level: DOUBLE = Default("1"),
        order: INT = Default("8"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply frequency shifting to input audio.

        Parameters:
        ----------

        :param DOUBLE shift: set frequency shift (from -2.14748e+09 to INT_MAX) (default 0)
        :param DOUBLE level: set output level (from 0 to 1) (default 1)
        :param INT order: set filter order (from 1 to 16) (default 8)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afreqshift

        """
        filter_node = FilterNode(
            name="afreqshift",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "shift": shift,
                        "level": level,
                        "order": order,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def afwtdn(
        self,
        *,
        sigma: DOUBLE = Default("0"),
        levels: INT = Default("10"),
        wavet: INT | Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"] | Default = Default("sym10"),
        percent: DOUBLE = Default("85"),
        profile: BOOLEAN = Default("false"),
        adaptive: BOOLEAN = Default("false"),
        samples: INT = Default("8192"),
        softness: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Denoise audio stream using Wavelets.

        Parameters:
        ----------

        :param DOUBLE sigma: set noise sigma (from 0 to 1) (default 0)
        :param INT levels: set number of wavelet levels (from 1 to 12) (default 10)
        :param INT wavet: set wavelet type (from 0 to 6) (default sym10)
        :param DOUBLE percent: set percent of full denoising (from 0 to 100) (default 85)
        :param BOOLEAN profile: profile noise (default false)
        :param BOOLEAN adaptive: adaptive profiling of noise (default false)
        :param INT samples: set frame size in number of samples (from 512 to 65536) (default 8192)
        :param DOUBLE softness: set thresholding softness (from 0 to 10) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afwtdn

        """
        filter_node = FilterNode(
            name="afwtdn",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def agate(
        self,
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
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio gate.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#agate

        """
        filter_node = FilterNode(
            name="agate",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
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

    def agraphmonitor(
        self,
        *,
        size: IMAGE_SIZE = Default("hd720"),
        opacity: FLOAT = Default("0.9"),
        mode: INT | Literal["full", "compact"] | Default = Default("full"),
        flags: FLAGS
        | Literal[
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
        ]
        | Default = Default("queue"),
        rate: VIDEO_RATE = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Show various filtergraph stats.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set monitor size (default "hd720")
        :param FLOAT opacity: set video opacity (from 0 to 1) (default 0.9)
        :param INT mode: set mode (from 0 to 1) (default full)
        :param FLAGS flags: set flags (default queue)
        :param VIDEO_RATE rate: set video rate (default "25")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#agraphmonitor

        """
        filter_node = FilterNode(
            name="agraphmonitor",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "opacity": opacity,
                        "mode": mode,
                        "flags": flags,
                        "rate": rate,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def ahistogram(
        self,
        *,
        dmode: INT | Literal["single", "separate"] | Default = Default("single"),
        rate: VIDEO_RATE = Default("25"),
        size: IMAGE_SIZE = Default("hd720"),
        scale: INT | Literal["log", "sqrt", "cbrt", "lin", "rlog"] | Default = Default("log"),
        ascale: INT | Literal["log", "lin"] | Default = Default("log"),
        acount: INT = Default("1"),
        rheight: FLOAT = Default("0.1"),
        slide: INT | Literal["replace", "scroll"] | Default = Default("replace"),
        hmode: INT | Literal["abs", "sign"] | Default = Default("abs"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to histogram video output.

        Parameters:
        ----------

        :param INT dmode: set method to display channels (from 0 to 1) (default single)
        :param VIDEO_RATE rate: set video rate (default "25")
        :param IMAGE_SIZE size: set video size (default "hd720")
        :param INT scale: set display scale (from 0 to 4) (default log)
        :param INT ascale: set amplitude scale (from 0 to 1) (default log)
        :param INT acount: how much frames to accumulate (from -1 to 100) (default 1)
        :param FLOAT rheight: set histogram ratio of window height (from 0 to 1) (default 0.1)
        :param INT slide: set sonogram sliding (from 0 to 1) (default replace)
        :param INT hmode: set histograms mode (from 0 to 1) (default abs)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ahistogram

        """
        filter_node = FilterNode(
            name="ahistogram",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def aiir(
        self,
        *,
        zeros: STRING = Default("1+0i 1-0i"),
        poles: STRING = Default("1+0i 1-0i"),
        gains: STRING = Default("1|1"),
        dry: DOUBLE = Default("1"),
        wet: DOUBLE = Default("1"),
        format: INT | Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | Default = Default("zp"),
        process: INT | Literal["d", "s", "p"] | Default = Default("s"),
        precision: INT | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        e: INT | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        normalize: BOOLEAN = Default("true"),
        mix: DOUBLE = Default("1"),
        response: BOOLEAN = Default("false"),
        channel: INT = Default("0"),
        size: IMAGE_SIZE = Default("hd720"),
        rate: VIDEO_RATE = Default("25"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Apply Infinite Impulse Response filter with supplied coefficients.

        Parameters:
        ----------

        :param STRING zeros: set B/numerator/zeros/reflection coefficients (default "1+0i 1-0i")
        :param STRING poles: set A/denominator/poles/ladder coefficients (default "1+0i 1-0i")
        :param STRING gains: set channels gains (default "1|1")
        :param DOUBLE dry: set dry gain (from 0 to 1) (default 1)
        :param DOUBLE wet: set wet gain (from 0 to 1) (default 1)
        :param INT format: set coefficients format (from -2 to 4) (default zp)
        :param INT process: set kind of processing (from 0 to 2) (default s)
        :param INT precision: set filtering precision (from 0 to 3) (default dbl)
        :param INT e: set precision (from 0 to 3) (default dbl)
        :param BOOLEAN normalize: normalize coefficients (default true)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param BOOLEAN response: show IR frequency response (default false)
        :param INT channel: set IR channel to display frequency response (from 0 to 1024) (default 0)
        :param IMAGE_SIZE size: set video size (default "hd720")
        :param VIDEO_RATE rate: set video rate (default "25")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aiir

        """
        filter_node = FilterNode(
            name="aiir",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] + [StreamType.video] if response else []),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def aintegral(self, *, enable: str = Default(None), **kwargs: Any) -> "AudioStream":
        """

        Compute integral of input audio.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        filter_node = FilterNode(
            name="aintegral",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
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

    def alatency(self, *, enable: str = Default(None), **kwargs: Any) -> "AudioStream":
        """

        Report audio filtering latency.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency

        """
        filter_node = FilterNode(
            name="alatency",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
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

    def alimiter(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        limit: DOUBLE = Default("1"),
        attack: DOUBLE = Default("5"),
        release: DOUBLE = Default("50"),
        asc: BOOLEAN = Default("false"),
        asc_level: DOUBLE = Default("0.5"),
        level: BOOLEAN = Default("true"),
        latency: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio lookahead limiter.

        Parameters:
        ----------

        :param DOUBLE level_in: set input level (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set output level (from 0.015625 to 64) (default 1)
        :param DOUBLE limit: set limit (from 0.0625 to 1) (default 1)
        :param DOUBLE attack: set attack (from 0.1 to 80) (default 5)
        :param DOUBLE release: set release (from 1 to 8000) (default 50)
        :param BOOLEAN asc: enable asc (default false)
        :param DOUBLE asc_level: set asc level (from 0 to 1) (default 0.5)
        :param BOOLEAN level: auto level (default true)
        :param BOOLEAN latency: compensate delay (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#alimiter

        """
        filter_node = FilterNode(
            name="alimiter",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def allpass(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.707"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        order: INT = Default("2"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole all-pass filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.707)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT order: set filter order (from 1 to 2) (default 2)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#allpass

        """
        filter_node = FilterNode(
            name="allpass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aloop(
        self, *, loop: INT = Default("0"), size: INT64 = Default("0"), start: INT64 = Default("0"), **kwargs: Any
    ) -> "AudioStream":
        """

        Loop audio samples.

        Parameters:
        ----------

        :param INT loop: number of loops (from -1 to INT_MAX) (default 0)
        :param INT64 size: max number of samples to loop (from 0 to INT_MAX) (default 0)
        :param INT64 start: set the loop start sample (from 0 to I64_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aloop

        """
        filter_node = FilterNode(
            name="aloop",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "loop": loop,
                        "size": size,
                        "start": start,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def ametadata(
        self,
        *,
        mode: INT | Literal["select", "add", "modify", "delete", "print"] | Default = Default("select"),
        key: STRING = Default(None),
        value: STRING = Default(None),
        function: INT
        | Literal["same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"]
        | Default = Default("same_str"),
        expr: STRING = Default(None),
        file: STRING = Default(None),
        direct: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Manipulate audio frame metadata.

        Parameters:
        ----------

        :param INT mode: set a mode of operation (from 0 to 4) (default select)
        :param STRING key: set metadata key
        :param STRING value: set metadata value
        :param INT function: function for comparing values (from 0 to 6) (default same_str)
        :param STRING expr: set expression for expr function
        :param STRING file: set file where to print metadata information
        :param BOOLEAN direct: reduce buffering when printing to user-set file or pipe (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#metadata_002c-ametadata

        """
        filter_node = FilterNode(
            name="ametadata",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "key": key,
                        "value": value,
                        "function": function,
                        "expr": expr,
                        "file": file,
                        "direct": direct,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def amultiply(self, _multiply1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
                self,
                _multiply1,
            ),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def anequalizer(
        self,
        *,
        params: STRING = Default(""),
        curves: BOOLEAN = Default("false"),
        size: IMAGE_SIZE = Default("hd720"),
        mgain: DOUBLE = Default("60"),
        fscale: INT | Literal["lin", "log"] | Default = Default("log"),
        colors: STRING = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Apply high-order audio parametric multi band equalizer.

        Parameters:
        ----------

        :param STRING params: (default "")
        :param BOOLEAN curves: draw frequency response curves (default false)
        :param IMAGE_SIZE size: set video size (default "hd720")
        :param DOUBLE mgain: set max gain (from -900 to 900) (default 60)
        :param INT fscale: set frequency scale (from 0 to 1) (default log)
        :param STRING colors: set channels curves colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anequalizer

        """
        filter_node = FilterNode(
            name="anequalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] + [StreamType.video] if curves else []),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "params": params,
                        "curves": curves,
                        "size": size,
                        "mgain": mgain,
                        "fscale": fscale,
                        "colors": colors,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def anlmdn(
        self,
        *,
        strength: FLOAT = Default("1e-05"),
        patch: DURATION = Default("0.002"),
        research: DURATION = Default("0.006"),
        output: INT | Literal["i", "o", "n"] | Default = Default("o"),
        smooth: FLOAT = Default("11"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Reduce broadband noise from stream using Non-Local Means.

        Parameters:
        ----------

        :param FLOAT strength: set denoising strength (from 1e-05 to 10000) (default 1e-05)
        :param DURATION patch: set patch duration (default 0.002)
        :param DURATION research: set research duration (default 0.006)
        :param INT output: set output mode (from 0 to 2) (default o)
        :param FLOAT smooth: set smooth factor (from 1 to 1000) (default 11)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmdn

        """
        filter_node = FilterNode(
            name="anlmdn",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "strength": strength,
                        "patch": patch,
                        "research": research,
                        "output": output,
                        "smooth": smooth,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def anlmf(
        self,
        _desired: "AudioStream",
        *,
        order: INT = Default("256"),
        mu: FLOAT = Default("0.75"),
        eps: FLOAT = Default("1"),
        leakage: FLOAT = Default("0"),
        out_mode: INT | Literal["i", "d", "o", "n"] | Default = Default("o"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _desired: "AudioStream",
        *,
        order: INT = Default("256"),
        mu: FLOAT = Default("0.75"),
        eps: FLOAT = Default("1"),
        leakage: FLOAT = Default("0"),
        out_mode: INT | Literal["i", "d", "o", "n"] | Default = Default("o"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def anull(self, **kwargs: Any) -> "AudioStream":
        """

        Pass the source unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#anull

        """
        filter_node = FilterNode(
            name="anull",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def apad(
        self,
        *,
        packet_size: INT = Default("4096"),
        pad_len: INT64 = Default("-1"),
        whole_len: INT64 = Default("-1"),
        pad_dur: DURATION = Default("-0.000001"),
        whole_dur: DURATION = Default("-0.000001"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Pad audio with silence.

        Parameters:
        ----------

        :param INT packet_size: set silence packet size (from 0 to INT_MAX) (default 4096)
        :param INT64 pad_len: set number of samples of silence to add (from -1 to I64_MAX) (default -1)
        :param INT64 whole_len: set minimum target number of samples in the audio stream (from -1 to I64_MAX) (default -1)
        :param DURATION pad_dur: set duration of silence to add (default -0.000001)
        :param DURATION whole_dur: set minimum target duration in the audio stream (default -0.000001)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apad

        """
        filter_node = FilterNode(
            name="apad",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "packet_size": packet_size,
                        "pad_len": pad_len,
                        "whole_len": whole_len,
                        "pad_dur": pad_dur,
                        "whole_dur": whole_dur,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aperms(
        self,
        *,
        mode: INT | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default("none"),
        seed: INT64 = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Set permissions for the output audio frame.

        Parameters:
        ----------

        :param INT mode: select permissions mode (from 0 to 4) (default none)
        :param INT64 seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms

        """
        filter_node = FilterNode(
            name="aperms",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "seed": seed,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aphasemeter(
        self,
        *,
        rate: VIDEO_RATE = Default("25"),
        size: IMAGE_SIZE = Default("800x400"),
        rc: INT = Default("2"),
        gc: INT = Default("7"),
        bc: INT = Default("1"),
        mpc: STRING = Default("none"),
        video: BOOLEAN = Default("true"),
        phasing: BOOLEAN = Default("false"),
        tolerance: FLOAT = Default("0"),
        angle: FLOAT = Default("170"),
        duration: DURATION = Default("2"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Convert input audio to phase meter video output.

        Parameters:
        ----------

        :param VIDEO_RATE rate: set video rate (default "25")
        :param IMAGE_SIZE size: set video size (default "800x400")
        :param INT rc: set red contrast (from 0 to 255) (default 2)
        :param INT gc: set green contrast (from 0 to 255) (default 7)
        :param INT bc: set blue contrast (from 0 to 255) (default 1)
        :param STRING mpc: set median phase color (default "none")
        :param BOOLEAN video: set video output (default true)
        :param BOOLEAN phasing: set mono and out-of-phase detection output (default false)
        :param FLOAT tolerance: set phase tolerance for mono detection (from 0 to 1) (default 0)
        :param FLOAT angle: set angle threshold for out-of-phase detection (from 90 to 180) (default 170)
        :param DURATION duration: set minimum mono or out-of-phase duration in seconds (default 2)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphasemeter

        """
        filter_node = FilterNode(
            name="aphasemeter",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] + ([StreamType.video] if video else [])),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def aphaser(
        self,
        *,
        in_gain: DOUBLE = Default("0.4"),
        out_gain: DOUBLE = Default("0.74"),
        delay: DOUBLE = Default("3"),
        decay: DOUBLE = Default("0.4"),
        speed: DOUBLE = Default("0.5"),
        type: INT | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default("triangular"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add a phasing effect to the audio.

        Parameters:
        ----------

        :param DOUBLE in_gain: set input gain (from 0 to 1) (default 0.4)
        :param DOUBLE out_gain: set output gain (from 0 to 1e+09) (default 0.74)
        :param DOUBLE delay: set delay in milliseconds (from 0 to 5) (default 3)
        :param DOUBLE decay: set decay (from 0 to 0.99) (default 0.4)
        :param DOUBLE speed: set modulation speed (from 0.1 to 2) (default 0.5)
        :param INT type: set modulation type (from 0 to 1) (default triangular)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaser

        """
        filter_node = FilterNode(
            name="aphaser",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "in_gain": in_gain,
                        "out_gain": out_gain,
                        "delay": delay,
                        "decay": decay,
                        "speed": speed,
                        "type": type,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aphaseshift(
        self,
        *,
        shift: DOUBLE = Default("0"),
        level: DOUBLE = Default("1"),
        order: INT = Default("8"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply phase shifting to input audio.

        Parameters:
        ----------

        :param DOUBLE shift: set phase shift (from -1 to 1) (default 0)
        :param DOUBLE level: set output level (from 0 to 1) (default 1)
        :param INT order: set filter order (from 1 to 16) (default 8)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaseshift

        """
        filter_node = FilterNode(
            name="aphaseshift",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "shift": shift,
                        "level": level,
                        "order": order,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def apsyclip(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        clip: DOUBLE = Default("1"),
        diff: BOOLEAN = Default("false"),
        adaptive: DOUBLE = Default("0.5"),
        iterations: INT = Default("10"),
        level: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Psychoacoustic Clipper.

        Parameters:
        ----------

        :param DOUBLE level_in: set input level (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set output level (from 0.015625 to 64) (default 1)
        :param DOUBLE clip: set clip level (from 0.015625 to 1) (default 1)
        :param BOOLEAN diff: enable difference (default false)
        :param DOUBLE adaptive: set adaptive distortion (from 0 to 1) (default 0.5)
        :param INT iterations: set iterations (from 1 to 20) (default 10)
        :param BOOLEAN level: set auto level (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apsyclip

        """
        filter_node = FilterNode(
            name="apsyclip",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "level_in": level_in,
                        "level_out": level_out,
                        "clip": clip,
                        "diff": diff,
                        "adaptive": adaptive,
                        "iterations": iterations,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def apulsator(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        mode: INT | Literal["sine", "triangle", "square", "sawup", "sawdown"] | Default = Default("sine"),
        amount: DOUBLE = Default("1"),
        offset_l: DOUBLE = Default("0"),
        offset_r: DOUBLE = Default("0.5"),
        width: DOUBLE = Default("1"),
        timing: INT | Literal["bpm", "ms", "hz"] | Default = Default("hz"),
        bpm: DOUBLE = Default("120"),
        ms: INT = Default("500"),
        hz: DOUBLE = Default("2"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio pulsator.

        Parameters:
        ----------

        :param DOUBLE level_in: set input gain (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set output gain (from 0.015625 to 64) (default 1)
        :param INT mode: set mode (from 0 to 4) (default sine)
        :param DOUBLE amount: set modulation (from 0 to 1) (default 1)
        :param DOUBLE offset_l: set offset L (from 0 to 1) (default 0)
        :param DOUBLE offset_r: set offset R (from 0 to 1) (default 0.5)
        :param DOUBLE width: set pulse width (from 0 to 2) (default 1)
        :param INT timing: set timing (from 0 to 2) (default hz)
        :param DOUBLE bpm: set BPM (from 30 to 300) (default 120)
        :param INT ms: set ms (from 10 to 2000) (default 500)
        :param DOUBLE hz: set frequency (from 0.01 to 100) (default 2)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apulsator

        """
        filter_node = FilterNode(
            name="apulsator",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def arealtime(
        self, *, limit: DURATION = Default("2"), speed: DOUBLE = Default("1"), **kwargs: Any
    ) -> "AudioStream":
        """

        Slow down filtering to match realtime.

        Parameters:
        ----------

        :param DURATION limit: sleep time limit (default 2)
        :param DOUBLE speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime

        """
        filter_node = FilterNode(
            name="arealtime",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "limit": limit,
                        "speed": speed,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aresample(self, *, sample_rate: INT = Default("0"), **kwargs: Any) -> "AudioStream":
        """

        Resample audio data.

        Parameters:
        ----------

        :param INT sample_rate: (from 0 to INT_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aresample

        """
        filter_node = FilterNode(
            name="aresample",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sample_rate": sample_rate,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def areverse(self, **kwargs: Any) -> "AudioStream":
        """

        Reverse an audio clip.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#areverse

        """
        filter_node = FilterNode(
            name="areverse",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def arnndn(
        self, *, model: STRING = Default(None), mix: FLOAT = Default("1"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Reduce noise from speech using Recurrent Neural Networks.

        Parameters:
        ----------

        :param STRING model: set model name
        :param FLOAT mix: set output vs input mix (from -1 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#arnndn

        """
        filter_node = FilterNode(
            name="arnndn",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "model": model,
                        "mix": mix,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asdr(self, _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
                self,
                _input1,
            ),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def asegment(
        self, *, timestamps: STRING = Default(None), samples: STRING = Default(None), **kwargs: Any
    ) -> FilterNode:
        """

        Segment audio stream.

        Parameters:
        ----------

        :param STRING timestamps: timestamps of input at which to split input
        :param STRING samples: samples at which to split input

        Ref: https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment

        """
        filter_node = FilterNode(
            name="asegment",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] * len(str(timestamps or samples).split("|"))),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "timestamps": timestamps,
                        "samples": samples,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def aselect(self, *, expr: STRING = Default("1"), outputs: INT = Default("1"), **kwargs: Any) -> FilterNode:
        """

        Select audio frames to pass in output.

        Parameters:
        ----------

        :param STRING expr: set an expression to use for selecting frames (default "1")
        :param INT outputs: set the number of outputs (from 1 to INT_MAX) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect

        """
        filter_node = FilterNode(
            name="aselect",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] * int(outputs)),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "expr": expr,
                        "outputs": outputs,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def asendcmd(
        self, *, commands: STRING = Default(None), filename: STRING = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Send commands to filters.

        Parameters:
        ----------

        :param STRING commands: set commands
        :param STRING filename: set commands file

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd

        """
        filter_node = FilterNode(
            name="asendcmd",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "commands": commands,
                        "filename": filename,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asetnsamples(
        self, *, nb_out_samples: INT = Default("1024"), pad: BOOLEAN = Default("true"), **kwargs: Any
    ) -> "AudioStream":
        """

        Set the number of samples for each output audio frames.

        Parameters:
        ----------

        :param INT nb_out_samples: set the number of per-frame output samples (from 1 to INT_MAX) (default 1024)
        :param BOOLEAN pad: pad last frame with zeros (default true)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetnsamples

        """
        filter_node = FilterNode(
            name="asetnsamples",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "nb_out_samples": nb_out_samples,
                        "pad": pad,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asetpts(self, *, expr: STRING = Default("PTS"), **kwargs: Any) -> "AudioStream":
        """

        Set PTS for the output audio frame.

        Parameters:
        ----------

        :param STRING expr: Expression determining the frame timestamp (default "PTS")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts

        """
        filter_node = FilterNode(
            name="asetpts",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "expr": expr,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asetrate(self, *, sample_rate: INT = Default("44100"), **kwargs: Any) -> "AudioStream":
        """

        Change the sample rate without altering the data.

        Parameters:
        ----------

        :param INT sample_rate: set the sample rate (from 1 to INT_MAX) (default 44100)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetrate

        """
        filter_node = FilterNode(
            name="asetrate",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sample_rate": sample_rate,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asettb(self, *, expr: STRING = Default("intb"), **kwargs: Any) -> "AudioStream":
        """

        Set timebase for the audio output link.

        Parameters:
        ----------

        :param STRING expr: set expression determining the output timebase (default "intb")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb

        """
        filter_node = FilterNode(
            name="asettb",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "expr": expr,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def ashowinfo(self, **kwargs: Any) -> "AudioStream":
        """

        Show textual information for each audio frame.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#ashowinfo

        """
        filter_node = FilterNode(
            name="ashowinfo",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def asidedata(
        self,
        *,
        mode: INT | Literal["select", "delete"] | Default = Default("select"),
        type: INT
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
        | Default = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Manipulate audio frame side data.

        Parameters:
        ----------

        :param INT mode: set a mode of operation (from 0 to 1) (default select)
        :param INT type: set side data type (from -1 to INT_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata

        """
        filter_node = FilterNode(
            name="asidedata",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "type": type,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asoftclip(
        self,
        *,
        type: INT
        | Literal["hard", "tanh", "atan", "cubic", "exp", "alg", "quintic", "sin", "erf"]
        | Default = Default("tanh"),
        threshold: DOUBLE = Default("1"),
        output: DOUBLE = Default("1"),
        param: DOUBLE = Default("1"),
        oversample: INT = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Soft Clipper.

        Parameters:
        ----------

        :param INT type: set softclip type (from -1 to 7) (default tanh)
        :param DOUBLE threshold: set softclip threshold (from 1e-06 to 1) (default 1)
        :param DOUBLE output: set softclip output gain (from 1e-06 to 16) (default 1)
        :param DOUBLE param: set softclip parameter (from 0.01 to 3) (default 1)
        :param INT oversample: set oversample factor (from 1 to 64) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asoftclip

        """
        filter_node = FilterNode(
            name="asoftclip",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "type": type,
                        "threshold": threshold,
                        "output": output,
                        "param": param,
                        "oversample": oversample,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def aspectralstats(
        self,
        *,
        win_size: INT = Default("2048"),
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
        | Default = Default("hann"),
        overlap: FLOAT = Default("0.5"),
        measure: FLAGS
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
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Show frequency domain statistics about audio frames.

        Parameters:
        ----------

        :param INT win_size: set the window size (from 32 to 65536) (default 2048)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param FLOAT overlap: set window overlap (from 0 to 1) (default 0.5)
        :param FLAGS measure: select the parameters which are measured (default all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aspectralstats

        """
        filter_node = FilterNode(
            name="aspectralstats",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "win_size": win_size,
                        "win_func": win_func,
                        "overlap": overlap,
                        "measure": measure,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asplit(self, *, outputs: INT = Default("2"), **kwargs: Any) -> FilterNode:
        """

        Pass on the audio input to N audio outputs.

        Parameters:
        ----------

        :param INT outputs: set number of outputs (from 1 to INT_MAX) (default 2)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit

        """
        filter_node = FilterNode(
            name="asplit",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] * int(outputs)),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "outputs": outputs,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def astats(
        self,
        *,
        length: DOUBLE = Default("0.05"),
        metadata: BOOLEAN = Default("false"),
        reset: INT = Default("0"),
        measure_perchannel: FLAGS
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
        ]
        | Default = Default(
            "all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate"
        ),
        measure_overall: FLAGS
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
        ]
        | Default = Default(
            "all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate"
        ),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Show time domain statistics about audio frames.

        Parameters:
        ----------

        :param DOUBLE length: set the window length (from 0 to 10) (default 0.05)
        :param BOOLEAN metadata: inject metadata in the filtergraph (default false)
        :param INT reset: Set the number of frames over which cumulative stats are calculated before being reset (from 0 to INT_MAX) (default 0)
        :param FLAGS measure_perchannel: Select the parameters which are measured per channel (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate)
        :param FLAGS measure_overall: Select the parameters which are measured overall (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#astats

        """
        filter_node = FilterNode(
            name="astats",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "length": length,
                        "metadata": metadata,
                        "reset": reset,
                        "measure_perchannel": measure_perchannel,
                        "measure_overall": measure_overall,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asubboost(
        self,
        *,
        dry: DOUBLE = Default("1"),
        wet: DOUBLE = Default("1"),
        boost: DOUBLE = Default("2"),
        decay: DOUBLE = Default("0"),
        feedback: DOUBLE = Default("0.9"),
        cutoff: DOUBLE = Default("100"),
        slope: DOUBLE = Default("0.5"),
        delay: DOUBLE = Default("20"),
        channels: STRING = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost subwoofer frequencies.

        Parameters:
        ----------

        :param DOUBLE dry: set dry gain (from 0 to 1) (default 1)
        :param DOUBLE wet: set wet gain (from 0 to 1) (default 1)
        :param DOUBLE boost: set max boost (from 1 to 12) (default 2)
        :param DOUBLE decay: set decay (from 0 to 1) (default 0)
        :param DOUBLE feedback: set feedback (from 0 to 1) (default 0.9)
        :param DOUBLE cutoff: set cutoff (from 50 to 900) (default 100)
        :param DOUBLE slope: set slope (from 0.0001 to 1) (default 0.5)
        :param DOUBLE delay: set delay (from 1 to 100) (default 20)
        :param STRING channels: set channels to filter (default "all")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubboost

        """
        filter_node = FilterNode(
            name="asubboost",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asubcut(
        self,
        *,
        cutoff: DOUBLE = Default("20"),
        order: INT = Default("10"),
        level: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Cut subwoofer frequencies.

        Parameters:
        ----------

        :param DOUBLE cutoff: set cutoff frequency (from 2 to 200) (default 20)
        :param INT order: set filter order (from 3 to 20) (default 10)
        :param DOUBLE level: set input level (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubcut

        """
        filter_node = FilterNode(
            name="asubcut",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cutoff": cutoff,
                        "order": order,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asupercut(
        self,
        *,
        cutoff: DOUBLE = Default("20000"),
        order: INT = Default("10"),
        level: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Cut super frequencies.

        Parameters:
        ----------

        :param DOUBLE cutoff: set cutoff frequency (from 20000 to 192000) (default 20000)
        :param INT order: set filter order (from 3 to 20) (default 10)
        :param DOUBLE level: set input level (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asupercut

        """
        filter_node = FilterNode(
            name="asupercut",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cutoff": cutoff,
                        "order": order,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asuperpass(
        self,
        *,
        centerf: DOUBLE = Default("1000"),
        order: INT = Default("4"),
        qfactor: DOUBLE = Default("1"),
        level: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply high order Butterworth band-pass filter.

        Parameters:
        ----------

        :param DOUBLE centerf: set center frequency (from 2 to 999999) (default 1000)
        :param INT order: set filter order (from 4 to 20) (default 4)
        :param DOUBLE qfactor: set Q-factor (from 0.01 to 100) (default 1)
        :param DOUBLE level: set input level (from 0 to 2) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperpass

        """
        filter_node = FilterNode(
            name="asuperpass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "centerf": centerf,
                        "order": order,
                        "qfactor": qfactor,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def asuperstop(
        self,
        *,
        centerf: DOUBLE = Default("1000"),
        order: INT = Default("4"),
        qfactor: DOUBLE = Default("1"),
        level: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply high order Butterworth band-stop filter.

        Parameters:
        ----------

        :param DOUBLE centerf: set center frequency (from 2 to 999999) (default 1000)
        :param INT order: set filter order (from 4 to 20) (default 4)
        :param DOUBLE qfactor: set Q-factor (from 0.01 to 100) (default 1)
        :param DOUBLE level: set input level (from 0 to 2) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperstop

        """
        filter_node = FilterNode(
            name="asuperstop",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "centerf": centerf,
                        "order": order,
                        "qfactor": qfactor,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def atempo(self, *, tempo: DOUBLE = Default("1"), **kwargs: Any) -> "AudioStream":
        """

        Adjust audio tempo.

        Parameters:
        ----------

        :param DOUBLE tempo: set tempo scale factor (from 0.5 to 100) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atempo

        """
        filter_node = FilterNode(
            name="atempo",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "tempo": tempo,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def atilt(
        self,
        *,
        freq: DOUBLE = Default("10000"),
        slope: DOUBLE = Default("0"),
        width: DOUBLE = Default("1000"),
        order: INT = Default("5"),
        level: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply spectral tilt to audio.

        Parameters:
        ----------

        :param DOUBLE freq: set central frequency (from 20 to 192000) (default 10000)
        :param DOUBLE slope: set filter slope (from -1 to 1) (default 0)
        :param DOUBLE width: set filter width (from 100 to 10000) (default 1000)
        :param INT order: set filter order (from 2 to 30) (default 5)
        :param DOUBLE level: set input level (from 0 to 4) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atilt

        """
        filter_node = FilterNode(
            name="atilt",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "freq": freq,
                        "slope": slope,
                        "width": width,
                        "order": order,
                        "level": level,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def atrim(
        self,
        *,
        start: DURATION = Default("INT64_MAX"),
        end: DURATION = Default("INT64_MAX"),
        start_pts: INT64 = Default("I64_MIN"),
        end_pts: INT64 = Default("I64_MIN"),
        duration: DURATION = Default("0"),
        start_sample: INT64 = Default("-1"),
        end_sample: INT64 = Default("I64_MAX"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Pick one continuous section from the input, drop the rest.

        Parameters:
        ----------

        :param DURATION start: Timestamp of the first frame that should be passed (default INT64_MAX)
        :param DURATION end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
        :param INT64 start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
        :param INT64 end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
        :param DURATION duration: Maximum duration of the output (default 0)
        :param INT64 start_sample: Number of the first audio sample that should be passed to the output (from -1 to I64_MAX) (default -1)
        :param INT64 end_sample: Number of the first audio sample that should be dropped again (from 0 to I64_MAX) (default I64_MAX)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atrim

        """
        filter_node = FilterNode(
            name="atrim",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "start": start,
                        "end": end,
                        "start_pts": start_pts,
                        "end_pts": end_pts,
                        "duration": duration,
                        "start_sample": start_sample,
                        "end_sample": end_sample,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def avectorscope(
        self,
        *,
        mode: INT | Literal["lissajous", "lissajous_xy", "polar"] | Default = Default("lissajous"),
        rate: VIDEO_RATE = Default("25"),
        size: IMAGE_SIZE = Default("400x400"),
        rc: INT = Default("40"),
        gc: INT = Default("160"),
        bc: INT = Default("80"),
        ac: INT = Default("255"),
        rf: INT = Default("15"),
        gf: INT = Default("10"),
        bf: INT = Default("5"),
        af: INT = Default("5"),
        zoom: DOUBLE = Default("1"),
        draw: INT | Literal["dot", "line", "aaline"] | Default = Default("dot"),
        scale: INT | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("lin"),
        swap: BOOLEAN = Default("true"),
        mirror: INT | Literal["none", "x", "y", "xy"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to vectorscope video output.

        Parameters:
        ----------

        :param INT mode: set mode (from 0 to 2) (default lissajous)
        :param VIDEO_RATE rate: set video rate (default "25")
        :param IMAGE_SIZE size: set video size (default "400x400")
        :param INT rc: set red contrast (from 0 to 255) (default 40)
        :param INT gc: set green contrast (from 0 to 255) (default 160)
        :param INT bc: set blue contrast (from 0 to 255) (default 80)
        :param INT ac: set alpha contrast (from 0 to 255) (default 255)
        :param INT rf: set red fade (from 0 to 255) (default 15)
        :param INT gf: set green fade (from 0 to 255) (default 10)
        :param INT bf: set blue fade (from 0 to 255) (default 5)
        :param INT af: set alpha fade (from 0 to 255) (default 5)
        :param DOUBLE zoom: set zoom factor (from 0 to 10) (default 1)
        :param INT draw: set draw mode (from 0 to 2) (default dot)
        :param INT scale: set amplitude scale mode (from 0 to 3) (default lin)
        :param BOOLEAN swap: swap x axis with y axis (default true)
        :param INT mirror: mirror axis (from 0 to 3) (default none)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avectorscope

        """
        filter_node = FilterNode(
            name="avectorscope",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def axcorrelate(
        self,
        _axcorrelate1: "AudioStream",
        *,
        size: INT = Default("256"),
        algo: INT | Literal["slow", "fast"] | Default = Default("slow"),
        **kwargs: Any,
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
                self,
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

    def azmq(self, *, bind_address: STRING = Default("tcp://*:5555"), **kwargs: Any) -> "AudioStream":
        """

        Receive commands through ZMQ and broker them to filters.

        Parameters:
        ----------

        :param STRING bind_address: set bind address (default "tcp://*:5555")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zmq_002c-azmq

        """
        filter_node = FilterNode(
            name="azmq",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "bind_address": bind_address,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def bandpass(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        csg: BOOLEAN = Default("false"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole Butterworth band-pass filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param BOOLEAN csg: use constant skirt gain (default false)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandpass

        """
        filter_node = FilterNode(
            name="bandpass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def bandreject(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole Butterworth band-reject filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandreject

        """
        filter_node = FilterNode(
            name="bandreject",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def bass(
        self,
        *,
        frequency: DOUBLE = Default("100"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        gain: DOUBLE = Default("0"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost or cut lower frequencies.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 100)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        filter_node = FilterNode(
            name="bass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def biquad(
        self,
        *,
        a0: DOUBLE = Default("1"),
        a1: DOUBLE = Default("0"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a biquad IIR filter with the given coefficients.

        Parameters:
        ----------

        :param DOUBLE a0: (from INT_MIN to INT_MAX) (default 1)
        :param DOUBLE a1: (from INT_MIN to INT_MAX) (default 0)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#biquad

        """
        filter_node = FilterNode(
            name="biquad",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def channelmap(
        self, *, map: STRING = Default(None), channel_layout: STRING = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Remap audio channels.

        Parameters:
        ----------

        :param STRING map: A comma-separated list of input channel numbers in output order.
        :param STRING channel_layout: Output channel layout.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelmap

        """
        filter_node = FilterNode(
            name="channelmap",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "map": map,
                        "channel_layout": channel_layout,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def channelsplit(
        self, *, channel_layout: STRING = Default("stereo"), channels: STRING = Default("all"), **kwargs: Any
    ) -> FilterNode:
        """

        Split audio into per-channel streams.

        Parameters:
        ----------

        :param STRING channel_layout: Input channel layout. (default "stereo")
        :param STRING channels: Channels to extract. (default "all")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelsplit

        """
        filter_node = FilterNode(
            name="channelsplit",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio] * CHANNEL_LAYOUT[str(channel_layout)]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "channel_layout": channel_layout,
                        "channels": channels,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def chorus(
        self,
        *,
        in_gain: FLOAT = Default("0.4"),
        out_gain: FLOAT = Default("0.4"),
        delays: STRING = Default(None),
        decays: STRING = Default(None),
        speeds: STRING = Default(None),
        depths: STRING = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add a chorus effect to the audio.

        Parameters:
        ----------

        :param FLOAT in_gain: set input gain (from 0 to 1) (default 0.4)
        :param FLOAT out_gain: set output gain (from 0 to 1) (default 0.4)
        :param STRING delays: set delays
        :param STRING decays: set decays
        :param STRING speeds: set speeds
        :param STRING depths: set depths

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chorus

        """
        filter_node = FilterNode(
            name="chorus",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "in_gain": in_gain,
                        "out_gain": out_gain,
                        "delays": delays,
                        "decays": decays,
                        "speeds": speeds,
                        "depths": depths,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def compand(
        self,
        *,
        attacks: STRING = Default("0"),
        decays: STRING = Default("0.8"),
        points: STRING = Default("-70/-70|-60/-20|1/0"),
        soft_knee: DOUBLE = Default("0.01"),
        gain: DOUBLE = Default("0"),
        volume: DOUBLE = Default("0"),
        delay: DOUBLE = Default("0"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Compress or expand audio dynamic range.

        Parameters:
        ----------

        :param STRING attacks: set time over which increase of volume is determined (default "0")
        :param STRING decays: set time over which decrease of volume is determined (default "0.8")
        :param STRING points: set points of transfer function (default "-70/-70|-60/-20|1/0")
        :param DOUBLE soft_knee: set soft-knee (from 0.01 to 900) (default 0.01)
        :param DOUBLE gain: set output gain (from -900 to 900) (default 0)
        :param DOUBLE volume: set initial volume (from -900 to 0) (default 0)
        :param DOUBLE delay: set delay for samples before sending them to volume adjuster (from 0 to 20) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compand

        """
        filter_node = FilterNode(
            name="compand",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "attacks": attacks,
                        "decays": decays,
                        "points": points,
                        "soft-knee": soft_knee,
                        "gain": gain,
                        "volume": volume,
                        "delay": delay,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def compensationdelay(
        self,
        *,
        mm: INT = Default("0"),
        cm: INT = Default("0"),
        m: INT = Default("0"),
        dry: DOUBLE = Default("0"),
        wet: DOUBLE = Default("1"),
        temp: INT = Default("20"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Compensation Delay Line.

        Parameters:
        ----------

        :param INT mm: set mm distance (from 0 to 10) (default 0)
        :param INT cm: set cm distance (from 0 to 100) (default 0)
        :param INT m: set meter distance (from 0 to 100) (default 0)
        :param DOUBLE dry: set dry amount (from 0 to 1) (default 0)
        :param DOUBLE wet: set wet amount (from 0 to 1) (default 1)
        :param INT temp: set temperature °C (from -50 to 50) (default 20)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compensationdelay

        """
        filter_node = FilterNode(
            name="compensationdelay",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mm": mm,
                        "cm": cm,
                        "m": m,
                        "dry": dry,
                        "wet": wet,
                        "temp": temp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def crossfeed(
        self,
        *,
        strength: DOUBLE = Default("0.2"),
        range: DOUBLE = Default("0.5"),
        slope: DOUBLE = Default("0.5"),
        level_in: DOUBLE = Default("0.9"),
        level_out: DOUBLE = Default("1"),
        block_size: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply headphone crossfeed filter.

        Parameters:
        ----------

        :param DOUBLE strength: set crossfeed strength (from 0 to 1) (default 0.2)
        :param DOUBLE range: set soundstage wideness (from 0 to 1) (default 0.5)
        :param DOUBLE slope: set curve slope (from 0.01 to 1) (default 0.5)
        :param DOUBLE level_in: set level in (from 0 to 1) (default 0.9)
        :param DOUBLE level_out: set level out (from 0 to 1) (default 1)
        :param INT block_size: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crossfeed

        """
        filter_node = FilterNode(
            name="crossfeed",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "strength": strength,
                        "range": range,
                        "slope": slope,
                        "level_in": level_in,
                        "level_out": level_out,
                        "block_size": block_size,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def crystalizer(
        self, *, i: FLOAT = Default("2"), c: BOOLEAN = Default("true"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Simple audio noise sharpening filter.

        Parameters:
        ----------

        :param FLOAT i: set intensity (from -10 to 10) (default 2)
        :param BOOLEAN c: enable clipping (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crystalizer

        """
        filter_node = FilterNode(
            name="crystalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "i": i,
                        "c": c,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def dcshift(
        self,
        *,
        shift: DOUBLE = Default("0"),
        limitergain: DOUBLE = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a DC shift to the audio.

        Parameters:
        ----------

        :param DOUBLE shift: set DC shift (from -1 to 1) (default 0)
        :param DOUBLE limitergain: set limiter gain (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dcshift

        """
        filter_node = FilterNode(
            name="dcshift",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "shift": shift,
                        "limitergain": limitergain,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def deesser(
        self,
        *,
        i: DOUBLE = Default("0"),
        m: DOUBLE = Default("0.5"),
        f: DOUBLE = Default("0.5"),
        s: INT | Literal["i", "o", "e"] | Default = Default("o"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply de-essing to the audio.

        Parameters:
        ----------

        :param DOUBLE i: set intensity (from 0 to 1) (default 0)
        :param DOUBLE m: set max deessing (from 0 to 1) (default 0.5)
        :param DOUBLE f: set frequency (from 0 to 1) (default 0.5)
        :param INT s: set output mode (from 0 to 2) (default o)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deesser

        """
        filter_node = FilterNode(
            name="deesser",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "i": i,
                        "m": m,
                        "f": f,
                        "s": s,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def dialoguenhance(
        self,
        *,
        original: DOUBLE = Default("1"),
        enhance: DOUBLE = Default("1"),
        voice: DOUBLE = Default("2"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Dialogue Enhancement.

        Parameters:
        ----------

        :param DOUBLE original: set original center factor (from 0 to 1) (default 1)
        :param DOUBLE enhance: set dialogue enhance factor (from 0 to 3) (default 1)
        :param DOUBLE voice: set voice detection factor (from 2 to 32) (default 2)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance

        """
        filter_node = FilterNode(
            name="dialoguenhance",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "original": original,
                        "enhance": enhance,
                        "voice": voice,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def drmeter(self, *, length: DOUBLE = Default("3"), **kwargs: Any) -> "AudioStream":
        """

        Measure audio dynamic range.

        Parameters:
        ----------

        :param DOUBLE length: set the window length (from 0.01 to 10) (default 3)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drmeter

        """
        filter_node = FilterNode(
            name="drmeter",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "length": length,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def dynaudnorm(
        self,
        *,
        framelen: INT = Default("500"),
        gausssize: INT = Default("31"),
        peak: DOUBLE = Default("0.95"),
        maxgain: DOUBLE = Default("10"),
        targetrms: DOUBLE = Default("0"),
        coupling: BOOLEAN = Default("true"),
        correctdc: BOOLEAN = Default("false"),
        altboundary: BOOLEAN = Default("false"),
        compress: DOUBLE = Default("0"),
        threshold: DOUBLE = Default("0"),
        channels: STRING = Default("all"),
        overlap: DOUBLE = Default("0"),
        curve: STRING = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Dynamic Audio Normalizer.

        Parameters:
        ----------

        :param INT framelen: set the frame length in msec (from 10 to 8000) (default 500)
        :param INT gausssize: set the filter size (from 3 to 301) (default 31)
        :param DOUBLE peak: set the peak value (from 0 to 1) (default 0.95)
        :param DOUBLE maxgain: set the max amplification (from 1 to 100) (default 10)
        :param DOUBLE targetrms: set the target RMS (from 0 to 1) (default 0)
        :param BOOLEAN coupling: set channel coupling (default true)
        :param BOOLEAN correctdc: set DC correction (default false)
        :param BOOLEAN altboundary: set alternative boundary mode (default false)
        :param DOUBLE compress: set the compress factor (from 0 to 30) (default 0)
        :param DOUBLE threshold: set the threshold value (from 0 to 1) (default 0)
        :param STRING channels: set channels to filter (default "all")
        :param DOUBLE overlap: set the frame overlap (from 0 to 1) (default 0)
        :param STRING curve: set the custom peak mapping curve
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm

        """
        filter_node = FilterNode(
            name="dynaudnorm",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def earwax(self, **kwargs: Any) -> "AudioStream":
        """

        Widen the stereo image.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#earwax

        """
        filter_node = FilterNode(
            name="earwax",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def ebur128(
        self,
        *,
        video: BOOLEAN = Default("false"),
        size: IMAGE_SIZE = Default("640x480"),
        meter: INT = Default("9"),
        framelog: INT | Literal["quiet", "info", "verbose"] | Default = Default("-1"),
        metadata: BOOLEAN = Default("false"),
        peak: FLAGS | Literal["none", "sample", "true"] | Default = Default("0"),
        dualmono: BOOLEAN = Default("false"),
        panlaw: DOUBLE = Default("-3.0103"),
        target: INT = Default("-23"),
        gauge: INT | Literal["momentary", "m", "shortterm", "s"] | Default = Default("momentary"),
        scale: INT | Literal["absolute", "LUFS", "relative", "LU"] | Default = Default("absolute"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        EBU R128 scanner.

        Parameters:
        ----------

        :param BOOLEAN video: set video output (default false)
        :param IMAGE_SIZE size: set video size (default "640x480")
        :param INT meter: set scale meter (+9 to +18) (from 9 to 18) (default 9)
        :param INT framelog: force frame logging level (from INT_MIN to INT_MAX) (default -1)
        :param BOOLEAN metadata: inject metadata in the filtergraph (default false)
        :param FLAGS peak: set peak mode (default 0)
        :param BOOLEAN dualmono: treat mono input files as dual-mono (default false)
        :param DOUBLE panlaw: set a specific pan law for dual-mono files (from -10 to 0) (default -3.0103)
        :param INT target: set a specific target level in LUFS (-23 to 0) (from -23 to 0) (default -23)
        :param INT gauge: set gauge display type (from 0 to 1) (default momentary)
        :param INT scale: sets display method for the stats (from 0 to 1) (default absolute)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ebur128

        """
        filter_node = FilterNode(
            name="ebur128",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video] if video else [] + [StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def equalizer(
        self,
        *,
        frequency: DOUBLE = Default("0"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("1"),
        gain: DOUBLE = Default("0"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply two-pole peaking equalization (EQ) filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 0)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 1)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#equalizer

        """
        filter_node = FilterNode(
            name="equalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def extrastereo(
        self, *, m: FLOAT = Default("2.5"), c: BOOLEAN = Default("true"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Increase difference between stereo audio channels.

        Parameters:
        ----------

        :param FLOAT m: set the difference coefficient (from -10 to 10) (default 2.5)
        :param BOOLEAN c: enable clipping (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extrastereo

        """
        filter_node = FilterNode(
            name="extrastereo",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "m": m,
                        "c": c,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def firequalizer(
        self,
        *,
        gain: STRING = Default("gain_interpolate(f"),
        gain_entry: STRING = Default(None),
        delay: DOUBLE = Default("0.01"),
        accuracy: DOUBLE = Default("5"),
        wfunc: INT
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
        fixed: BOOLEAN = Default("false"),
        multi: BOOLEAN = Default("false"),
        zero_phase: BOOLEAN = Default("false"),
        scale: INT | Literal["linlin", "linlog", "loglin", "loglog"] | Default = Default("linlog"),
        dumpfile: STRING = Default(None),
        dumpscale: INT | Literal["linlin", "linlog", "loglin", "loglog"] | Default = Default("linlog"),
        fft2: BOOLEAN = Default("false"),
        min_phase: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Finite Impulse Response Equalizer.

        Parameters:
        ----------

        :param STRING gain: set gain curve (default "gain_interpolate(f)")
        :param STRING gain_entry: set gain entry
        :param DOUBLE delay: set delay (from 0 to 1e+10) (default 0.01)
        :param DOUBLE accuracy: set accuracy (from 0 to 1e+10) (default 5)
        :param INT wfunc: set window function (from 0 to 9) (default hann)
        :param BOOLEAN fixed: set fixed frame samples (default false)
        :param BOOLEAN multi: set multi channels mode (default false)
        :param BOOLEAN zero_phase: set zero phase mode (default false)
        :param INT scale: set gain scale (from 0 to 3) (default linlog)
        :param STRING dumpfile: set dump file
        :param INT dumpscale: set dump scale (from 0 to 3) (default linlog)
        :param BOOLEAN fft2: set 2-channels fft (default false)
        :param BOOLEAN min_phase: set minimum phase mode (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#firequalizer

        """
        filter_node = FilterNode(
            name="firequalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def flanger(
        self,
        *,
        delay: DOUBLE = Default("0"),
        depth: DOUBLE = Default("2"),
        regen: DOUBLE = Default("0"),
        width: DOUBLE = Default("71"),
        speed: DOUBLE = Default("0.5"),
        shape: INT | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default("sinusoidal"),
        phase: DOUBLE = Default("25"),
        interp: INT | Literal["linear", "quadratic"] | Default = Default("linear"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a flanging effect to the audio.

        Parameters:
        ----------

        :param DOUBLE delay: base delay in milliseconds (from 0 to 30) (default 0)
        :param DOUBLE depth: added swept delay in milliseconds (from 0 to 10) (default 2)
        :param DOUBLE regen: percentage regeneration (delayed signal feedback) (from -95 to 95) (default 0)
        :param DOUBLE width: percentage of delayed signal mixed with original (from 0 to 100) (default 71)
        :param DOUBLE speed: sweeps per second (Hz) (from 0.1 to 10) (default 0.5)
        :param INT shape: swept wave shape (from 0 to 1) (default sinusoidal)
        :param DOUBLE phase: swept wave percentage phase-shift for multi-channel (from 0 to 100) (default 25)
        :param INT interp: delay-line interpolation (from 0 to 1) (default linear)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#flanger

        """
        filter_node = FilterNode(
            name="flanger",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "delay": delay,
                        "depth": depth,
                        "regen": regen,
                        "width": width,
                        "speed": speed,
                        "shape": shape,
                        "phase": phase,
                        "interp": interp,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def haas(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        side_gain: DOUBLE = Default("1"),
        middle_source: INT | Literal["left", "right", "mid", "side"] | Default = Default("mid"),
        middle_phase: BOOLEAN = Default("false"),
        left_delay: DOUBLE = Default("2.05"),
        left_balance: DOUBLE = Default("-1"),
        left_gain: DOUBLE = Default("1"),
        left_phase: BOOLEAN = Default("false"),
        right_delay: DOUBLE = Default("2.12"),
        right_balance: DOUBLE = Default("1"),
        right_gain: DOUBLE = Default("1"),
        right_phase: BOOLEAN = Default("true"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Haas Stereo Enhancer.

        Parameters:
        ----------

        :param DOUBLE level_in: set level in (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set level out (from 0.015625 to 64) (default 1)
        :param DOUBLE side_gain: set side gain (from 0.015625 to 64) (default 1)
        :param INT middle_source: set middle source (from 0 to 3) (default mid)
        :param BOOLEAN middle_phase: set middle phase (default false)
        :param DOUBLE left_delay: set left delay (from 0 to 40) (default 2.05)
        :param DOUBLE left_balance: set left balance (from -1 to 1) (default -1)
        :param DOUBLE left_gain: set left gain (from 0.015625 to 64) (default 1)
        :param BOOLEAN left_phase: set left phase (default false)
        :param DOUBLE right_delay: set right delay (from 0 to 40) (default 2.12)
        :param DOUBLE right_balance: set right balance (from -1 to 1) (default 1)
        :param DOUBLE right_gain: set right gain (from 0.015625 to 64) (default 1)
        :param BOOLEAN right_phase: set right phase (default true)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#haas

        """
        filter_node = FilterNode(
            name="haas",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def hdcd(
        self,
        *,
        disable_autoconvert: BOOLEAN = Default("true"),
        process_stereo: BOOLEAN = Default("true"),
        cdt_ms: INT = Default("2000"),
        force_pe: BOOLEAN = Default("false"),
        analyze_mode: INT | Literal["off", "lle", "pe", "cdt", "tgm"] | Default = Default("off"),
        bits_per_sample: INT | Literal["16", "20", "24"] | Default = Default("16"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply High Definition Compatible Digital (HDCD) decoding.

        Parameters:
        ----------

        :param BOOLEAN disable_autoconvert: Disable any format conversion or resampling in the filter graph. (default true)
        :param BOOLEAN process_stereo: Process stereo channels together. Only apply target_gain when both channels match. (default true)
        :param INT cdt_ms: Code detect timer period in ms. (from 100 to 60000) (default 2000)
        :param BOOLEAN force_pe: Always extend peaks above -3dBFS even when PE is not signaled. (default false)
        :param INT analyze_mode: Replace audio with solid tone and signal some processing aspect in the amplitude. (from 0 to 4) (default off)
        :param INT bits_per_sample: Valid bits per sample (location of the true LSB). (from 16 to 24) (default 16)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hdcd

        """
        filter_node = FilterNode(
            name="hdcd",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "disable_autoconvert": disable_autoconvert,
                        "process_stereo": process_stereo,
                        "cdt_ms": cdt_ms,
                        "force_pe": force_pe,
                        "analyze_mode": analyze_mode,
                        "bits_per_sample": bits_per_sample,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def highpass(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.707"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a high-pass filter with 3dB point frequency.

        Parameters:
        ----------

        :param DOUBLE frequency: set frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.707)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#highpass

        """
        filter_node = FilterNode(
            name="highpass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def highshelf(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        gain: DOUBLE = Default("0"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a high shelf filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        filter_node = FilterNode(
            name="highshelf",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def loudnorm(
        self,
        *,
        I: DOUBLE = Default("-24"),
        LRA: DOUBLE = Default("7"),
        TP: DOUBLE = Default("-2"),
        measured_I: DOUBLE = Default("0"),
        measured_LRA: DOUBLE = Default("0"),
        measured_TP: DOUBLE = Default("99"),
        measured_thresh: DOUBLE = Default("-70"),
        offset: DOUBLE = Default("0"),
        linear: BOOLEAN = Default("true"),
        dual_mono: BOOLEAN = Default("false"),
        print_format: INT | Literal["none", "json", "summary"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        EBU R128 loudness normalization

        Parameters:
        ----------

        :param DOUBLE I: set integrated loudness target (from -70 to -5) (default -24)
        :param DOUBLE LRA: set loudness range target (from 1 to 50) (default 7)
        :param DOUBLE TP: set maximum true peak (from -9 to 0) (default -2)
        :param DOUBLE measured_I: measured IL of input file (from -99 to 0) (default 0)
        :param DOUBLE measured_LRA: measured LRA of input file (from 0 to 99) (default 0)
        :param DOUBLE measured_TP: measured true peak of input file (from -99 to 99) (default 99)
        :param DOUBLE measured_thresh: measured threshold of input file (from -99 to 0) (default -70)
        :param DOUBLE offset: set offset gain (from -99 to 99) (default 0)
        :param BOOLEAN linear: normalize linearly if possible (default true)
        :param BOOLEAN dual_mono: treat mono input as dual-mono (default false)
        :param INT print_format: set print format for stats (from 0 to 2) (default none)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#loudnorm

        """
        filter_node = FilterNode(
            name="loudnorm",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def lowpass(
        self,
        *,
        frequency: DOUBLE = Default("500"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.707"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a low-pass filter with 3dB point frequency.

        Parameters:
        ----------

        :param DOUBLE frequency: set frequency (from 0 to 999999) (default 500)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.707)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lowpass

        """
        filter_node = FilterNode(
            name="lowpass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def lowshelf(
        self,
        *,
        frequency: DOUBLE = Default("100"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        gain: DOUBLE = Default("0"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a low shelf filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 100)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        filter_node = FilterNode(
            name="lowshelf",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def mcompand(
        self,
        *,
        args: STRING = Default(
            "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000"
        ),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Multiband Compress or expand audio dynamic range.

        Parameters:
        ----------

        :param STRING args: set parameters for each band (default "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcompand

        """
        filter_node = FilterNode(
            name="mcompand",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "args": args,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def pan(self, *, args: STRING = Default(None), **kwargs: Any) -> "AudioStream":
        """

        Remix channels with coefficients (panning).

        Parameters:
        ----------

        :param STRING args:

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pan

        """
        filter_node = FilterNode(
            name="pan",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "args": args,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def replaygain(self, **kwargs: Any) -> "AudioStream":
        """

        ReplayGain scanner.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#replaygain

        """
        filter_node = FilterNode(
            name="replaygain",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)

    def rubberband(
        self,
        *,
        tempo: DOUBLE = Default("1"),
        pitch: DOUBLE = Default("1"),
        transients: INT | Literal["crisp", "mixed", "smooth"] | Default = Default("crisp"),
        detector: INT | Literal["compound", "percussive", "soft"] | Default = Default("compound"),
        phase: INT | Literal["laminar", "independent"] | Default = Default("laminar"),
        window: INT | Literal["standard", "short", "long"] | Default = Default("standard"),
        smoothing: INT | Literal["off", "on"] | Default = Default("off"),
        formant: INT | Literal["shifted", "preserved"] | Default = Default("shifted"),
        pitchq: INT | Literal["quality", "speed", "consistency"] | Default = Default("speed"),
        channels: INT | Literal["apart", "together"] | Default = Default("apart"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply time-stretching and pitch-shifting.

        Parameters:
        ----------

        :param DOUBLE tempo: set tempo scale factor (from 0.01 to 100) (default 1)
        :param DOUBLE pitch: set pitch scale factor (from 0.01 to 100) (default 1)
        :param INT transients: set transients (from 0 to INT_MAX) (default crisp)
        :param INT detector: set detector (from 0 to INT_MAX) (default compound)
        :param INT phase: set phase (from 0 to INT_MAX) (default laminar)
        :param INT window: set window (from 0 to INT_MAX) (default standard)
        :param INT smoothing: set smoothing (from 0 to INT_MAX) (default off)
        :param INT formant: set formant (from 0 to INT_MAX) (default shifted)
        :param INT pitchq: set pitch quality (from 0 to INT_MAX) (default speed)
        :param INT channels: set channels (from 0 to INT_MAX) (default apart)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rubberband

        """
        filter_node = FilterNode(
            name="rubberband",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def showcqt(
        self,
        *,
        size: IMAGE_SIZE = Default("1920x1080"),
        fps: VIDEO_RATE = Default("25"),
        bar_h: INT = Default("-1"),
        axis_h: INT = Default("-1"),
        sono_h: INT = Default("-1"),
        fullhd: BOOLEAN = Default("true"),
        sono_v: STRING = Default("16"),
        bar_v: STRING = Default("sono_v"),
        sono_g: FLOAT = Default("3"),
        bar_g: FLOAT = Default("1"),
        bar_t: FLOAT = Default("1"),
        timeclamp: DOUBLE = Default("0.17"),
        attack: DOUBLE = Default("0"),
        basefreq: DOUBLE = Default("20.0152"),
        endfreq: DOUBLE = Default("20495.6"),
        coeffclamp: FLOAT = Default("1"),
        tlength: STRING = Default("384*tc/(384+tc*f"),
        count: INT = Default("6"),
        fcount: INT = Default("0"),
        fontfile: STRING = Default(None),
        font: STRING = Default(None),
        fontcolor: STRING = Default("st(0, (midi(f"),
        axisfile: STRING = Default(None),
        axis: BOOLEAN = Default("true"),
        csp: INT
        | Literal["unspecified", "bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "bt2020ncl"]
        | Default = Default("unspecified"),
        cscheme: STRING = Default("1|0.5|0|0|0.5|1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "1920x1080")
        :param VIDEO_RATE fps: set video rate (default "25")
        :param INT bar_h: set bargraph height (from -1 to INT_MAX) (default -1)
        :param INT axis_h: set axis height (from -1 to INT_MAX) (default -1)
        :param INT sono_h: set sonogram height (from -1 to INT_MAX) (default -1)
        :param BOOLEAN fullhd: set fullhd size (default true)
        :param STRING sono_v: set sonogram volume (default "16")
        :param STRING bar_v: set bargraph volume (default "sono_v")
        :param FLOAT sono_g: set sonogram gamma (from 1 to 7) (default 3)
        :param FLOAT bar_g: set bargraph gamma (from 1 to 7) (default 1)
        :param FLOAT bar_t: set bar transparency (from 0 to 1) (default 1)
        :param DOUBLE timeclamp: set timeclamp (from 0.002 to 1) (default 0.17)
        :param DOUBLE attack: set attack time (from 0 to 1) (default 0)
        :param DOUBLE basefreq: set base frequency (from 10 to 100000) (default 20.0152)
        :param DOUBLE endfreq: set end frequency (from 10 to 100000) (default 20495.6)
        :param FLOAT coeffclamp: set coeffclamp (from 0.1 to 10) (default 1)
        :param STRING tlength: set tlength (default "384*tc/(384+tc*f)")
        :param INT count: set transform count (from 1 to 30) (default 6)
        :param INT fcount: set frequency count (from 0 to 10) (default 0)
        :param STRING fontfile: set axis font file
        :param STRING font: set axis font
        :param STRING fontcolor: set font color (default "st(0, (midi(f)-59.5)/12);st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));r(1-ld(1)) + b(ld(1))")
        :param STRING axisfile: set axis image
        :param BOOLEAN axis: draw axis (default true)
        :param INT csp: set color space (from 0 to INT_MAX) (default unspecified)
        :param STRING cscheme: set color scheme (default "1|0.5|0|0|0.5|1")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showcqt

        """
        filter_node = FilterNode(
            name="showcqt",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showcwt(
        self,
        *,
        size: IMAGE_SIZE = Default("640x512"),
        rate: STRING = Default("25"),
        scale: INT | Literal["linear", "log2", "bark", "mel", "erbs"] | Default = Default("linear"),
        min: FLOAT = Default("20"),
        max: FLOAT = Default("20000"),
        logb: FLOAT = Default("0.0001"),
        deviation: FLOAT = Default("1"),
        pps: INT = Default("64"),
        mode: INT | Literal["magnitude", "phase", "magphase", "channel", "stereo"] | Default = Default("magnitude"),
        slide: INT | Literal["replace", "scroll", "frame"] | Default = Default("replace"),
        direction: INT | Literal["lr", "rl", "ud", "du"] | Default = Default("lr"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "640x512")
        :param STRING rate: set video rate (default "25")
        :param INT scale: set frequency scale (from 0 to 4) (default linear)
        :param FLOAT min: set minimum frequency (from 1 to 2000) (default 20)
        :param FLOAT max: set maximum frequency (from 0 to 192000) (default 20000)
        :param FLOAT logb: set logarithmic basis (from 0 to 1) (default 0.0001)
        :param FLOAT deviation: set frequency deviation (from 0 to 10) (default 1)
        :param INT pps: set pixels per second (from 1 to 1024) (default 64)
        :param INT mode: set output mode (from 0 to 4) (default magnitude)
        :param INT slide: set slide mode (from 0 to 2) (default replace)
        :param INT direction: set direction mode (from 0 to 3) (default lr)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showcwt

        """
        filter_node = FilterNode(
            name="showcwt",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "rate": rate,
                        "scale": scale,
                        "min": min,
                        "max": max,
                        "logb": logb,
                        "deviation": deviation,
                        "pps": pps,
                        "mode": mode,
                        "slide": slide,
                        "direction": direction,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showfreqs(
        self,
        *,
        size: IMAGE_SIZE = Default("1024x512"),
        rate: VIDEO_RATE = Default("25"),
        mode: INT | Literal["line", "bar", "dot"] | Default = Default("bar"),
        ascale: INT | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("log"),
        fscale: INT | Literal["lin", "log", "rlog"] | Default = Default("lin"),
        win_size: INT = Default("2048"),
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
        | Default = Default("hann"),
        overlap: FLOAT = Default("1"),
        averaging: INT = Default("1"),
        colors: STRING = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        cmode: INT | Literal["combined", "separate"] | Default = Default("combined"),
        minamp: FLOAT = Default("1e-06"),
        data: INT | Literal["magnitude", "phase", "delay"] | Default = Default("magnitude"),
        channels: STRING = Default("all"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a frequencies video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "1024x512")
        :param VIDEO_RATE rate: set video rate (default "25")
        :param INT mode: set display mode (from 0 to 2) (default bar)
        :param INT ascale: set amplitude scale (from 0 to 3) (default log)
        :param INT fscale: set frequency scale (from 0 to 2) (default lin)
        :param INT win_size: set window size (from 16 to 65536) (default 2048)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param FLOAT overlap: set window overlap (from 0 to 1) (default 1)
        :param INT averaging: set time averaging (from 0 to INT_MAX) (default 1)
        :param STRING colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param INT cmode: set channel mode (from 0 to 1) (default combined)
        :param FLOAT minamp: set minimum amplitude (from FLT_MIN to 1e-06) (default 1e-06)
        :param INT data: set data mode (from 0 to 2) (default magnitude)
        :param STRING channels: set channels to draw (default "all")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showfreqs

        """
        filter_node = FilterNode(
            name="showfreqs",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showspatial(
        self,
        *,
        size: IMAGE_SIZE = Default("512x512"),
        win_size: INT = Default("4096"),
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
        | Default = Default("hann"),
        rate: VIDEO_RATE = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spatial video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "512x512")
        :param INT win_size: set window size (from 1024 to 65536) (default 4096)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param VIDEO_RATE rate: set video rate (default "25")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspatial

        """
        filter_node = FilterNode(
            name="showspatial",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "win_size": win_size,
                        "win_func": win_func,
                        "rate": rate,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showspectrum(
        self,
        *,
        size: IMAGE_SIZE = Default("640x512"),
        slide: INT | Literal["replace", "scroll", "fullframe", "rscroll", "lreplace"] | Default = Default("replace"),
        mode: INT | Literal["combined", "separate"] | Default = Default("combined"),
        color: INT
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
        scale: INT | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | Default = Default("sqrt"),
        fscale: INT | Literal["lin", "log"] | Default = Default("lin"),
        saturation: FLOAT = Default("1"),
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
        | Default = Default("hann"),
        orientation: INT | Literal["vertical", "horizontal"] | Default = Default("vertical"),
        overlap: FLOAT = Default("0"),
        gain: FLOAT = Default("1"),
        data: INT | Literal["magnitude", "phase", "uphase"] | Default = Default("magnitude"),
        rotation: FLOAT = Default("0"),
        start: INT = Default("0"),
        stop: INT = Default("0"),
        fps: STRING = Default("auto"),
        legend: BOOLEAN = Default("false"),
        drange: FLOAT = Default("120"),
        limit: FLOAT = Default("0"),
        opacity: FLOAT = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spectrum video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "640x512")
        :param INT slide: set sliding mode (from 0 to 4) (default replace)
        :param INT mode: set channel display mode (from 0 to 1) (default combined)
        :param INT color: set channel coloring (from 0 to 14) (default channel)
        :param INT scale: set display scale (from 0 to 5) (default sqrt)
        :param INT fscale: set frequency scale (from 0 to 1) (default lin)
        :param FLOAT saturation: color saturation multiplier (from -10 to 10) (default 1)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param INT orientation: set orientation (from 0 to 1) (default vertical)
        :param FLOAT overlap: set window overlap (from 0 to 1) (default 0)
        :param FLOAT gain: set scale gain (from 0 to 128) (default 1)
        :param INT data: set data mode (from 0 to 2) (default magnitude)
        :param FLOAT rotation: color rotation (from -1 to 1) (default 0)
        :param INT start: start frequency (from 0 to INT_MAX) (default 0)
        :param INT stop: stop frequency (from 0 to INT_MAX) (default 0)
        :param STRING fps: set video rate (default "auto")
        :param BOOLEAN legend: draw legend (default false)
        :param FLOAT drange: set dynamic range in dBFS (from 10 to 200) (default 120)
        :param FLOAT limit: set upper limit in dBFS (from -100 to 100) (default 0)
        :param FLOAT opacity: set opacity strength (from 0 to 10) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspectrum

        """
        filter_node = FilterNode(
            name="showspectrum",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showspectrumpic(
        self,
        *,
        size: IMAGE_SIZE = Default("4096x2048"),
        mode: INT | Literal["combined", "separate"] | Default = Default("combined"),
        color: INT
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
        scale: INT | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | Default = Default("log"),
        fscale: INT | Literal["lin", "log"] | Default = Default("lin"),
        saturation: FLOAT = Default("1"),
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
        | Default = Default("hann"),
        orientation: INT | Literal["vertical", "horizontal"] | Default = Default("vertical"),
        gain: FLOAT = Default("1"),
        legend: BOOLEAN = Default("true"),
        rotation: FLOAT = Default("0"),
        start: INT = Default("0"),
        stop: INT = Default("0"),
        drange: FLOAT = Default("120"),
        limit: FLOAT = Default("0"),
        opacity: FLOAT = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spectrum video output single picture.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "4096x2048")
        :param INT mode: set channel display mode (from 0 to 1) (default combined)
        :param INT color: set channel coloring (from 0 to 14) (default intensity)
        :param INT scale: set display scale (from 0 to 5) (default log)
        :param INT fscale: set frequency scale (from 0 to 1) (default lin)
        :param FLOAT saturation: color saturation multiplier (from -10 to 10) (default 1)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param INT orientation: set orientation (from 0 to 1) (default vertical)
        :param FLOAT gain: set scale gain (from 0 to 128) (default 1)
        :param BOOLEAN legend: draw legend (default true)
        :param FLOAT rotation: color rotation (from -1 to 1) (default 0)
        :param INT start: start frequency (from 0 to INT_MAX) (default 0)
        :param INT stop: stop frequency (from 0 to INT_MAX) (default 0)
        :param FLOAT drange: set dynamic range in dBFS (from 10 to 200) (default 120)
        :param FLOAT limit: set upper limit in dBFS (from -100 to 100) (default 0)
        :param FLOAT opacity: set opacity strength (from 0 to 10) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspectrumpic

        """
        filter_node = FilterNode(
            name="showspectrumpic",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showvolume(
        self,
        *,
        rate: VIDEO_RATE = Default("25"),
        b: INT = Default("1"),
        w: INT = Default("400"),
        h: INT = Default("20"),
        f: DOUBLE = Default("0.95"),
        c: STRING = Default("PEAK*255+floor((1-PEAK"),
        t: BOOLEAN = Default("true"),
        v: BOOLEAN = Default("true"),
        dm: DOUBLE = Default("0"),
        dmc: COLOR = Default("orange"),
        o: INT | Literal["h", "v"] | Default = Default("h"),
        s: INT = Default("0"),
        p: FLOAT = Default("0"),
        m: INT | Literal["p", "r"] | Default = Default("p"),
        ds: INT | Literal["lin", "log"] | Default = Default("lin"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio volume to video output.

        Parameters:
        ----------

        :param VIDEO_RATE rate: set video rate (default "25")
        :param INT b: set border width (from 0 to 5) (default 1)
        :param INT w: set channel width (from 80 to 8192) (default 400)
        :param INT h: set channel height (from 1 to 900) (default 20)
        :param DOUBLE f: set fade (from 0 to 1) (default 0.95)
        :param STRING c: set volume color expression (default "PEAK*255+floor((1-PEAK)*255)*256+0xff000000")
        :param BOOLEAN t: display channel names (default true)
        :param BOOLEAN v: display volume value (default true)
        :param DOUBLE dm: duration for max value display (from 0 to 9000) (default 0)
        :param COLOR dmc: set color of the max value line (default "orange")
        :param INT o: set orientation (from 0 to 1) (default h)
        :param INT s: set step size (from 0 to 5) (default 0)
        :param FLOAT p: set background opacity (from 0 to 1) (default 0)
        :param INT m: set mode (from 0 to 1) (default p)
        :param INT ds: set display scale (from 0 to 1) (default lin)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showvolume

        """
        filter_node = FilterNode(
            name="showvolume",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showwaves(
        self,
        *,
        size: IMAGE_SIZE = Default("600x240"),
        mode: INT | Literal["point", "line", "p2p", "cline"] | Default = Default("point"),
        n: INT = Default("0"),
        rate: VIDEO_RATE = Default("25"),
        split_channels: BOOLEAN = Default("false"),
        colors: STRING = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: INT | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: INT | Literal["scale", "full"] | Default = Default("scale"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a video output.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "600x240")
        :param INT mode: select display mode (from 0 to 3) (default point)
        :param INT n: set how many samples to show in the same point (from 0 to INT_MAX) (default 0)
        :param VIDEO_RATE rate: set video rate (default "25")
        :param BOOLEAN split_channels: draw channels separately (default false)
        :param STRING colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param INT scale: set amplitude scale (from 0 to 3) (default lin)
        :param INT draw: set draw mode (from 0 to 1) (default scale)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showwaves

        """
        filter_node = FilterNode(
            name="showwaves",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "mode": mode,
                        "n": n,
                        "rate": rate,
                        "split_channels": split_channels,
                        "colors": colors,
                        "scale": scale,
                        "draw": draw,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showwavespic(
        self,
        *,
        size: IMAGE_SIZE = Default("600x240"),
        split_channels: BOOLEAN = Default("false"),
        colors: STRING = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: INT | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: INT | Literal["scale", "full"] | Default = Default("scale"),
        filter: INT | Literal["average", "peak"] | Default = Default("average"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a video output single picture.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set video size (default "600x240")
        :param BOOLEAN split_channels: draw channels separately (default false)
        :param STRING colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param INT scale: set amplitude scale (from 0 to 3) (default lin)
        :param INT draw: set draw mode (from 0 to 1) (default scale)
        :param INT filter: set filter mode (from 0 to 1) (default average)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showwavespic

        """
        filter_node = FilterNode(
            name="showwavespic",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "split_channels": split_channels,
                        "colors": colors,
                        "scale": scale,
                        "draw": draw,
                        "filter": filter,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sidechaincompress(
        self,
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
        **kwargs: Any,
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
                self,
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
        self,
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
        **kwargs: Any,
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
                self,
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

    def silencedetect(
        self,
        *,
        n: DOUBLE = Default("0.001"),
        d: DURATION = Default("2"),
        mono: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Detect silence.

        Parameters:
        ----------

        :param DOUBLE n: set noise tolerance (from 0 to DBL_MAX) (default 0.001)
        :param DURATION d: set minimum duration in seconds (default 2)
        :param BOOLEAN mono: check each channel separately (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silencedetect

        """
        filter_node = FilterNode(
            name="silencedetect",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                        "d": d,
                        "mono": mono,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def silenceremove(
        self,
        *,
        start_periods: INT = Default("0"),
        start_duration: DURATION = Default("0"),
        start_threshold: DOUBLE = Default("0"),
        start_silence: DURATION = Default("0"),
        start_mode: INT | Literal["any", "all"] | Default = Default("any"),
        stop_periods: INT = Default("0"),
        stop_duration: DURATION = Default("0"),
        stop_threshold: DOUBLE = Default("0"),
        stop_silence: DURATION = Default("0"),
        stop_mode: INT | Literal["any", "all"] | Default = Default("any"),
        detection: INT | Literal["peak", "rms"] | Default = Default("rms"),
        window: DURATION = Default("0.02"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove silence.

        Parameters:
        ----------

        :param INT start_periods: set periods of silence parts to skip from start (from 0 to 9000) (default 0)
        :param DURATION start_duration: set start duration of non-silence part (default 0)
        :param DOUBLE start_threshold: set threshold for start silence detection (from 0 to DBL_MAX) (default 0)
        :param DURATION start_silence: set start duration of silence part to keep (default 0)
        :param INT start_mode: set which channel will trigger trimming from start (from 0 to 1) (default any)
        :param INT stop_periods: set periods of silence parts to skip from end (from -9000 to 9000) (default 0)
        :param DURATION stop_duration: set stop duration of non-silence part (default 0)
        :param DOUBLE stop_threshold: set threshold for stop silence detection (from 0 to DBL_MAX) (default 0)
        :param DURATION stop_silence: set stop duration of silence part to keep (default 0)
        :param INT stop_mode: set which channel will trigger trimming from end (from 0 to 1) (default any)
        :param INT detection: set how silence is detected (from 0 to 1) (default rms)
        :param DURATION window: set duration of window for silence detection (default 0.02)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silenceremove

        """
        filter_node = FilterNode(
            name="silenceremove",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def speechnorm(
        self,
        *,
        peak: DOUBLE = Default("0.95"),
        expansion: DOUBLE = Default("2"),
        compression: DOUBLE = Default("2"),
        threshold: DOUBLE = Default("0"),
        _raise: DOUBLE = Default("0.001"),
        fall: DOUBLE = Default("0.001"),
        channels: STRING = Default("all"),
        invert: BOOLEAN = Default("false"),
        link: BOOLEAN = Default("false"),
        rms: DOUBLE = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Speech Normalizer.

        Parameters:
        ----------

        :param DOUBLE peak: set the peak value (from 0 to 1) (default 0.95)
        :param DOUBLE expansion: set the max expansion factor (from 1 to 50) (default 2)
        :param DOUBLE compression: set the max compression factor (from 1 to 50) (default 2)
        :param DOUBLE threshold: set the threshold value (from 0 to 1) (default 0)
        :param DOUBLE _raise: set the expansion raising amount (from 0 to 1) (default 0.001)
        :param DOUBLE fall: set the compression raising amount (from 0 to 1) (default 0.001)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN invert: set inverted filtering (default false)
        :param BOOLEAN link: set linked channels filtering (default false)
        :param DOUBLE rms: set the RMS value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#speechnorm

        """
        filter_node = FilterNode(
            name="speechnorm",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def stereotools(
        self,
        *,
        level_in: DOUBLE = Default("1"),
        level_out: DOUBLE = Default("1"),
        balance_in: DOUBLE = Default("0"),
        balance_out: DOUBLE = Default("0"),
        softclip: BOOLEAN = Default("false"),
        mutel: BOOLEAN = Default("false"),
        muter: BOOLEAN = Default("false"),
        phasel: BOOLEAN = Default("false"),
        phaser: BOOLEAN = Default("false"),
        mode: INT
        | Literal["lr", "ms", "lr", "ll", "rr", "r", "rl", "ll", "rr", "rl", "r"]
        | Default = Default("lr>lr"),
        slev: DOUBLE = Default("1"),
        sbal: DOUBLE = Default("0"),
        mlev: DOUBLE = Default("1"),
        mpan: DOUBLE = Default("0"),
        base: DOUBLE = Default("0"),
        delay: DOUBLE = Default("0"),
        sclevel: DOUBLE = Default("1"),
        phase: DOUBLE = Default("0"),
        bmode_in: INT | Literal["balance", "amplitude", "power"] | Default = Default("balance"),
        bmode_out: INT | Literal["balance", "amplitude", "power"] | Default = Default("balance"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply various stereo tools.

        Parameters:
        ----------

        :param DOUBLE level_in: set level in (from 0.015625 to 64) (default 1)
        :param DOUBLE level_out: set level out (from 0.015625 to 64) (default 1)
        :param DOUBLE balance_in: set balance in (from -1 to 1) (default 0)
        :param DOUBLE balance_out: set balance out (from -1 to 1) (default 0)
        :param BOOLEAN softclip: enable softclip (default false)
        :param BOOLEAN mutel: mute L (default false)
        :param BOOLEAN muter: mute R (default false)
        :param BOOLEAN phasel: phase L (default false)
        :param BOOLEAN phaser: phase R (default false)
        :param INT mode: set stereo mode (from 0 to 10) (default lr>lr)
        :param DOUBLE slev: set side level (from 0.015625 to 64) (default 1)
        :param DOUBLE sbal: set side balance (from -1 to 1) (default 0)
        :param DOUBLE mlev: set middle level (from 0.015625 to 64) (default 1)
        :param DOUBLE mpan: set middle pan (from -1 to 1) (default 0)
        :param DOUBLE base: set stereo base (from -1 to 1) (default 0)
        :param DOUBLE delay: set delay (from -20 to 20) (default 0)
        :param DOUBLE sclevel: set S/C level (from 1 to 100) (default 1)
        :param DOUBLE phase: set stereo phase (from 0 to 360) (default 0)
        :param INT bmode_in: set balance in mode (from 0 to 2) (default balance)
        :param INT bmode_out: set balance out mode (from 0 to 2) (default balance)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereotools

        """
        filter_node = FilterNode(
            name="stereotools",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def stereowiden(
        self,
        *,
        delay: FLOAT = Default("20"),
        feedback: FLOAT = Default("0.3"),
        crossfeed: FLOAT = Default("0.3"),
        drymix: FLOAT = Default("0.8"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply stereo widening effect.

        Parameters:
        ----------

        :param FLOAT delay: set delay time (from 1 to 100) (default 20)
        :param FLOAT feedback: set feedback gain (from 0 to 0.9) (default 0.3)
        :param FLOAT crossfeed: set cross feed (from 0 to 0.8) (default 0.3)
        :param FLOAT drymix: set dry-mix (from 0 to 1) (default 0.8)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereowiden

        """
        filter_node = FilterNode(
            name="stereowiden",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "delay": delay,
                        "feedback": feedback,
                        "crossfeed": crossfeed,
                        "drymix": drymix,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def superequalizer(
        self,
        *,
        _1b: FLOAT = Default("1"),
        _2b: FLOAT = Default("1"),
        _3b: FLOAT = Default("1"),
        _4b: FLOAT = Default("1"),
        _5b: FLOAT = Default("1"),
        _6b: FLOAT = Default("1"),
        _7b: FLOAT = Default("1"),
        _8b: FLOAT = Default("1"),
        _9b: FLOAT = Default("1"),
        _10b: FLOAT = Default("1"),
        _11b: FLOAT = Default("1"),
        _12b: FLOAT = Default("1"),
        _13b: FLOAT = Default("1"),
        _14b: FLOAT = Default("1"),
        _15b: FLOAT = Default("1"),
        _16b: FLOAT = Default("1"),
        _17b: FLOAT = Default("1"),
        _18b: FLOAT = Default("1"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply 18 band equalization filter.

        Parameters:
        ----------

        :param FLOAT _1b: set 65Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _2b: set 92Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _3b: set 131Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _4b: set 185Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _5b: set 262Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _6b: set 370Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _7b: set 523Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _8b: set 740Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _9b: set 1047Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _10b: set 1480Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _11b: set 2093Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _12b: set 2960Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _13b: set 4186Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _14b: set 5920Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _15b: set 8372Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _16b: set 11840Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _17b: set 16744Hz band gain (from 0 to 20) (default 1)
        :param FLOAT _18b: set 20000Hz band gain (from 0 to 20) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#superequalizer

        """
        filter_node = FilterNode(
            name="superequalizer",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def surround(
        self,
        *,
        chl_out: STRING = Default("5.1"),
        chl_in: STRING = Default("stereo"),
        level_in: FLOAT = Default("1"),
        level_out: FLOAT = Default("1"),
        lfe: BOOLEAN = Default("true"),
        lfe_low: INT = Default("128"),
        lfe_high: INT = Default("256"),
        lfe_mode: INT | Literal["add", "sub"] | Default = Default("add"),
        smooth: FLOAT = Default("0"),
        angle: FLOAT = Default("90"),
        focus: FLOAT = Default("0"),
        fc_in: FLOAT = Default("1"),
        fc_out: FLOAT = Default("1"),
        fl_in: FLOAT = Default("1"),
        fl_out: FLOAT = Default("1"),
        fr_in: FLOAT = Default("1"),
        fr_out: FLOAT = Default("1"),
        sl_in: FLOAT = Default("1"),
        sl_out: FLOAT = Default("1"),
        sr_in: FLOAT = Default("1"),
        sr_out: FLOAT = Default("1"),
        bl_in: FLOAT = Default("1"),
        bl_out: FLOAT = Default("1"),
        br_in: FLOAT = Default("1"),
        br_out: FLOAT = Default("1"),
        bc_in: FLOAT = Default("1"),
        bc_out: FLOAT = Default("1"),
        lfe_in: FLOAT = Default("1"),
        lfe_out: FLOAT = Default("1"),
        allx: FLOAT = Default("-1"),
        ally: FLOAT = Default("-1"),
        fcx: FLOAT = Default("0.5"),
        flx: FLOAT = Default("0.5"),
        frx: FLOAT = Default("0.5"),
        blx: FLOAT = Default("0.5"),
        brx: FLOAT = Default("0.5"),
        slx: FLOAT = Default("0.5"),
        srx: FLOAT = Default("0.5"),
        bcx: FLOAT = Default("0.5"),
        fcy: FLOAT = Default("0.5"),
        fly: FLOAT = Default("0.5"),
        fry: FLOAT = Default("0.5"),
        bly: FLOAT = Default("0.5"),
        bry: FLOAT = Default("0.5"),
        sly: FLOAT = Default("0.5"),
        sry: FLOAT = Default("0.5"),
        bcy: FLOAT = Default("0.5"),
        win_size: INT = Default("4096"),
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
        | Default = Default("hann"),
        overlap: FLOAT = Default("0.5"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply audio surround upmix filter.

        Parameters:
        ----------

        :param STRING chl_out: set output channel layout (default "5.1")
        :param STRING chl_in: set input channel layout (default "stereo")
        :param FLOAT level_in: set input level (from 0 to 10) (default 1)
        :param FLOAT level_out: set output level (from 0 to 10) (default 1)
        :param BOOLEAN lfe: output LFE (default true)
        :param INT lfe_low: LFE low cut off (from 0 to 256) (default 128)
        :param INT lfe_high: LFE high cut off (from 0 to 512) (default 256)
        :param INT lfe_mode: set LFE channel mode (from 0 to 1) (default add)
        :param FLOAT smooth: set temporal smoothness strength (from 0 to 1) (default 0)
        :param FLOAT angle: set soundfield transform angle (from 0 to 360) (default 90)
        :param FLOAT focus: set soundfield transform focus (from -1 to 1) (default 0)
        :param FLOAT fc_in: set front center channel input level (from 0 to 10) (default 1)
        :param FLOAT fc_out: set front center channel output level (from 0 to 10) (default 1)
        :param FLOAT fl_in: set front left channel input level (from 0 to 10) (default 1)
        :param FLOAT fl_out: set front left channel output level (from 0 to 10) (default 1)
        :param FLOAT fr_in: set front right channel input level (from 0 to 10) (default 1)
        :param FLOAT fr_out: set front right channel output level (from 0 to 10) (default 1)
        :param FLOAT sl_in: set side left channel input level (from 0 to 10) (default 1)
        :param FLOAT sl_out: set side left channel output level (from 0 to 10) (default 1)
        :param FLOAT sr_in: set side right channel input level (from 0 to 10) (default 1)
        :param FLOAT sr_out: set side right channel output level (from 0 to 10) (default 1)
        :param FLOAT bl_in: set back left channel input level (from 0 to 10) (default 1)
        :param FLOAT bl_out: set back left channel output level (from 0 to 10) (default 1)
        :param FLOAT br_in: set back right channel input level (from 0 to 10) (default 1)
        :param FLOAT br_out: set back right channel output level (from 0 to 10) (default 1)
        :param FLOAT bc_in: set back center channel input level (from 0 to 10) (default 1)
        :param FLOAT bc_out: set back center channel output level (from 0 to 10) (default 1)
        :param FLOAT lfe_in: set lfe channel input level (from 0 to 10) (default 1)
        :param FLOAT lfe_out: set lfe channel output level (from 0 to 10) (default 1)
        :param FLOAT allx: set all channel's x spread (from -1 to 15) (default -1)
        :param FLOAT ally: set all channel's y spread (from -1 to 15) (default -1)
        :param FLOAT fcx: set front center channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT flx: set front left channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT frx: set front right channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT blx: set back left channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT brx: set back right channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT slx: set side left channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT srx: set side right channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT bcx: set back center channel x spread (from 0.06 to 15) (default 0.5)
        :param FLOAT fcy: set front center channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT fly: set front left channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT fry: set front right channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT bly: set back left channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT bry: set back right channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT sly: set side left channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT sry: set side right channel y spread (from 0.06 to 15) (default 0.5)
        :param FLOAT bcy: set back center channel y spread (from 0.06 to 15) (default 0.5)
        :param INT win_size: set window size (from 1024 to 65536) (default 4096)
        :param INT win_func: set window function (from 0 to 20) (default hann)
        :param FLOAT overlap: set window overlap (from 0 to 1) (default 0.5)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#surround

        """
        filter_node = FilterNode(
            name="surround",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def tiltshelf(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        gain: DOUBLE = Default("0"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a tilt shelf filter.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tiltshelf

        """
        filter_node = FilterNode(
            name="tiltshelf",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def treble(
        self,
        *,
        frequency: DOUBLE = Default("3000"),
        width_type: INT | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: DOUBLE = Default("0.5"),
        gain: DOUBLE = Default("0"),
        poles: INT = Default("2"),
        mix: DOUBLE = Default("1"),
        channels: STRING = Default("all"),
        normalize: BOOLEAN = Default("false"),
        transform: INT | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: INT | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost or cut upper frequencies.

        Parameters:
        ----------

        :param DOUBLE frequency: set central frequency (from 0 to 999999) (default 3000)
        :param INT width_type: set filter-width type (from 1 to 5) (default q)
        :param DOUBLE width: set width (from 0 to 99999) (default 0.5)
        :param DOUBLE gain: set gain (from -900 to 900) (default 0)
        :param INT poles: set number of poles (from 1 to 2) (default 2)
        :param DOUBLE mix: set mix (from 0 to 1) (default 1)
        :param STRING channels: set channels to filter (default "all")
        :param BOOLEAN normalize: normalize coefficients (default false)
        :param INT transform: set transform type (from 0 to 6) (default di)
        :param INT precision: set filtering precision (from -1 to 3) (default auto)
        :param INT blocksize: set the block size (from 0 to 32768) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        filter_node = FilterNode(
            name="treble",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def tremolo(
        self, *, f: DOUBLE = Default("5"), d: DOUBLE = Default("0.5"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Apply tremolo effect.

        Parameters:
        ----------

        :param DOUBLE f: set frequency in hertz (from 0.1 to 20000) (default 5)
        :param DOUBLE d: set depth as percentage (from 0 to 1) (default 0.5)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tremolo

        """
        filter_node = FilterNode(
            name="tremolo",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "f": f,
                        "d": d,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def vibrato(
        self, *, f: DOUBLE = Default("5"), d: DOUBLE = Default("0.5"), enable: str = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Apply vibrato effect.

        Parameters:
        ----------

        :param DOUBLE f: set frequency in hertz (from 0.1 to 20000) (default 5)
        :param DOUBLE d: set depth as percentage (from 0 to 1) (default 0.5)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrato

        """
        filter_node = FilterNode(
            name="vibrato",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "f": f,
                        "d": d,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def virtualbass(
        self,
        *,
        cutoff: DOUBLE = Default("250"),
        strength: DOUBLE = Default("3"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Virtual Bass.

        Parameters:
        ----------

        :param DOUBLE cutoff: set virtual bass cutoff (from 100 to 500) (default 250)
        :param DOUBLE strength: set virtual bass strength (from 0.5 to 3) (default 3)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#virtualbass

        """
        filter_node = FilterNode(
            name="virtualbass",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cutoff": cutoff,
                        "strength": strength,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def volume(
        self,
        *,
        volume: STRING = Default("1.0"),
        precision: INT | Literal["fixed", "float", "double"] | Default = Default("float"),
        eval: INT | Literal["once", "frame"] | Default = Default("once"),
        replaygain: INT | Literal["drop", "ignore", "track", "album"] | Default = Default("drop"),
        replaygain_preamp: DOUBLE = Default("0"),
        replaygain_noclip: BOOLEAN = Default("true"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Change input volume.

        Parameters:
        ----------

        :param STRING volume: set volume adjustment expression (default "1.0")
        :param INT precision: select mathematical precision (from 0 to 2) (default float)
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default once)
        :param INT replaygain: Apply replaygain side data when present (from 0 to 3) (default drop)
        :param DOUBLE replaygain_preamp: Apply replaygain pre-amplification (from -15 to 15) (default 0)
        :param BOOLEAN replaygain_noclip: Apply replaygain clipping prevention (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#volume

        """
        filter_node = FilterNode(
            name="volume",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "volume": volume,
                        "precision": precision,
                        "eval": eval,
                        "replaygain": replaygain,
                        "replaygain_preamp": replaygain_preamp,
                        "replaygain_noclip": replaygain_noclip,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.audio(0)

    def volumedetect(self, **kwargs: Any) -> "AudioStream":
        """

        Detect audio volume.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#volumedetect

        """
        filter_node = FilterNode(
            name="volumedetect",
            input_typings=tuple([StreamType.audio]),
            output_typings=tuple([StreamType.audio]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.audio(0)
