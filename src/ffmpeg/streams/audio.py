from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Literal

from ..nodes.nodes import FilterableStream, FilterNode
from ..schema import Default, StreamType
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
        rate: str | float | int = Default("25"),
        size: str | float | int = Default("hd720"),
        fov: float | int | str = Default("90"),
        roll: float | int | str = Default("0"),
        pitch: float | int | str = Default("0"),
        yaw: float | int | str = Default("0"),
        xzoom: float | int | str = Default("1"),
        xpos: float | int | str = Default("0"),
        length: int | str = Default("15"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to 3d scope video output.

        Parameters:
        ----------

        :param str rate: set video rate (default "25")
        :param str size: set video size (default "hd720")
        :param float fov: set camera FoV (from 40 to 150) (default 90)
        :param float roll: set camera roll (from -180 to 180) (default 0)
        :param float pitch: set camera pitch (from -180 to 180) (default 0)
        :param float yaw: set camera yaw (from -180 to 180) (default 0)
        :param float xzoom: set camera zoom (from 0.01 to 10) (default 1)
        :param float xpos: set camera position (from -60 to 60) (default 0)
        :param int length: set length (from 1 to 60) (default 15)

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
        self, *, action: int | Literal["start", "stop"] | Default = Default("start"), **kwargs: Any
    ) -> "AudioStream":
        """

        Benchmark part of a filtergraph.

        Parameters:
        ----------

        :param int action: set action (from 0 to 1) (default start)

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
        rate: str | float | int = Default("25"),
        size: str | float | int = Default("1024x256"),
        colors: str | float | int = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        mode: int | Literal["bars", "trace"] | Default = Default("bars"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to audio bit scope video output.

        Parameters:
        ----------

        :param str rate: set video rate (default "25")
        :param str size: set video size (default "1024x256")
        :param str colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param int mode: set output mode (from 0 to 1) (default bars)

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
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio compressor.

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

    def acontrast(self, *, contrast: float | int | str = Default("33"), **kwargs: Any) -> "AudioStream":
        """

        Simple audio dynamic range compression/expansion filter.

        Parameters:
        ----------

        :param float contrast: set contrast (from 0 to 100) (default 33)

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
        **kwargs: Any,
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
        split: str | float | int = Default("500"),
        order: int
        | Literal["2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"]
        | Default = Default("4th"),
        level: float | int | str = Default("1"),
        gain: str | float | int = Default("1.f"),
        precision: int | Literal["auto", "float", "double"] | Default = Default("auto"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Split audio into per-bands streams.

        Parameters:
        ----------

        :param str split: set split frequencies (default "500")
        :param int order: set filter order (from 0 to 9) (default 4th)
        :param float level: set input gain (from 0 to 1) (default 1)
        :param str gain: set output bands gain (default "1.f")
        :param int precision: set processing precision (from 0 to 2) (default auto)

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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        bits: float | int | str = Default("8"),
        mix: float | int | str = Default("0.5"),
        mode: int | Literal["lin", "log"] | Default = Default("lin"),
        dc: float | int | str = Default("1"),
        aa: float | int | str = Default("0.5"),
        samples: float | int | str = Default("1"),
        lfo: bool | int | str = Default("false"),
        lforange: float | int | str = Default("20"),
        lforate: float | int | str = Default("0.3"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Reduce audio bit resolution.

        Parameters:
        ----------

        :param float level_in: set level in (from 0.015625 to 64) (default 1)
        :param float level_out: set level out (from 0.015625 to 64) (default 1)
        :param float bits: set bit reduction (from 1 to 64) (default 8)
        :param float mix: set mix (from 0 to 1) (default 0.5)
        :param int mode: set mode (from 0 to 1) (default lin)
        :param float dc: set DC (from 0.25 to 4) (default 1)
        :param float aa: set anti-aliasing (from 0 to 1) (default 0.5)
        :param float samples: set sample reduction (from 1 to 250) (default 1)
        :param bool lfo: enable LFO (default false)
        :param float lforange: set LFO depth (from 1 to 250) (default 20)
        :param float lforate: set LFO rate (from 0.01 to 200) (default 0.3)
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
        cue: int | str = Default("0"),
        preroll: str | float | int = Default("0"),
        buffer: str | float | int = Default("0"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Delay filtering to match a cue.

        Parameters:
        ----------

        :param int cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
        :param str preroll: preroll duration in seconds (default 0)
        :param str buffer: buffer duration in seconds (default 0)

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
        window: float | int | str = Default("55"),
        overlap: float | int | str = Default("75"),
        arorder: float | int | str = Default("2"),
        threshold: float | int | str = Default("2"),
        burst: float | int | str = Default("2"),
        method: int | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove impulsive noise from input audio.

        Parameters:
        ----------

        :param float window: set window size (from 10 to 100) (default 55)
        :param float overlap: set window overlap (from 50 to 95) (default 75)
        :param float arorder: set autoregression order (from 0 to 25) (default 2)
        :param float threshold: set threshold (from 1 to 100) (default 2)
        :param float burst: set burst fusion (from 0 to 10) (default 2)
        :param int method: set overlap method (from 0 to 1) (default add)
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
        window: float | int | str = Default("55"),
        overlap: float | int | str = Default("75"),
        arorder: float | int | str = Default("8"),
        threshold: float | int | str = Default("10"),
        hsize: int | str = Default("1000"),
        method: int | Literal["add", "a", "save", "s"] | Default = Default("add"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove clipping from input audio.

        Parameters:
        ----------

        :param float window: set window size (from 10 to 100) (default 55)
        :param float overlap: set window overlap (from 50 to 95) (default 75)
        :param float arorder: set autoregression order (from 0 to 25) (default 8)
        :param float threshold: set threshold (from 1 to 100) (default 10)
        :param int hsize: set histogram size (from 100 to 9999) (default 1000)
        :param int method: set overlap method (from 0 to 1) (default add)
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
        self,
        *,
        stages: int | str = Default("6"),
        seed: int | str = Default("-1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply decorrelation to input audio.

        Parameters:
        ----------

        :param int stages: set filtering stages (from 1 to 16) (default 6)
        :param int seed: set random seed (from -1 to UINT32_MAX) (default -1)
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
        delays: str | float | int = Default(None),
        all: bool | int | str = Default("false"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Delay one or more audio channels.

        Parameters:
        ----------

        :param str delays: set list of delays for each channel
        :param bool all: use last available delay for remained channels (default false)
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
        level: float | int | str = Default("-351"),
        type: int | Literal["dc", "ac", "square", "pulse"] | Default = Default("dc"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remedy denormals by adding extremely low-level noise.

        Parameters:
        ----------

        :param float level: set level (from -451 to -90) (default -351)
        :param int type: set type (from 0 to 3) (default dc)
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

    def aderivative(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "AudioStream":
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
        m1: str | float | int = Default(""),
        fg1: str | float | int = Default("0xffff0000"),
        m2: str | float | int = Default(""),
        fg2: str | float | int = Default("0xff00ff00"),
        m3: str | float | int = Default(""),
        fg3: str | float | int = Default("0xffff00ff"),
        m4: str | float | int = Default(""),
        fg4: str | float | int = Default("0xffffff00"),
        bg: str | float | int = Default("white"),
        min: float | int | str = Default("-1"),
        max: float | int | str = Default("1"),
        mode: int | Literal["bar", "dot", "line"] | Default = Default("line"),
        slide: int | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default("frame"),
        size: str | float | int = Default("900x256"),
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a graph using input audio metadata.

        Parameters:
        ----------

        :param str m1: set 1st metadata key (default "")
        :param str fg1: set 1st foreground color expression (default "0xffff0000")
        :param str m2: set 2nd metadata key (default "")
        :param str fg2: set 2nd foreground color expression (default "0xff00ff00")
        :param str m3: set 3rd metadata key (default "")
        :param str fg3: set 3rd foreground color expression (default "0xffff00ff")
        :param str m4: set 4th metadata key (default "")
        :param str fg4: set 4th foreground color expression (default "0xffffff00")
        :param str bg: set background color (default "white")
        :param float min: set minimal value (from INT_MIN to INT_MAX) (default -1)
        :param float max: set maximal value (from INT_MIN to INT_MAX) (default 1)
        :param int mode: set graph mode (from 0 to 2) (default line)
        :param int slide: set slide mode (from 0 to 4) (default frame)
        :param str size: set graph size (default "900x256")
        :param str rate: set video rate (default "25")

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
        transfer: str | float | int = Default("p"),
        attack: float | int | str = Default("50"),
        release: float | int | str = Default("100"),
        channels: str | float | int = Default("all"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Spectral Dynamic Range Controller.

        Parameters:
        ----------

        :param str transfer: set the transfer expression (default "p")
        :param float attack: set the attack (from 1 to 1000) (default 50)
        :param float release: set the release (from 5 to 2000) (default 100)
        :param str channels: set channels to filter (default "all")
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
        threshold: float | int | str = Default("0"),
        dfrequency: float | int | str = Default("1000"),
        dqfactor: float | int | str = Default("1"),
        tfrequency: float | int | str = Default("1000"),
        tqfactor: float | int | str = Default("1"),
        attack: float | int | str = Default("20"),
        release: float | int | str = Default("200"),
        ratio: float | int | str = Default("1"),
        makeup: float | int | str = Default("0"),
        range: float | int | str = Default("50"),
        mode: int | Literal["listen", "cut", "boost"] | Default = Default("cut"),
        tftype: int | Literal["bell", "lowshelf", "highshelf"] | Default = Default("bell"),
        direction: int | Literal["downward", "upward"] | Default = Default("downward"),
        auto: int | Literal["disabled", "off", "on"] | Default = Default("disabled"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Dynamic Equalization of input audio.

        Parameters:
        ----------

        :param float threshold: set detection threshold (from 0 to 100) (default 0)
        :param float dfrequency: set detection frequency (from 2 to 1e+06) (default 1000)
        :param float dqfactor: set detection Q factor (from 0.001 to 1000) (default 1)
        :param float tfrequency: set target frequency (from 2 to 1e+06) (default 1000)
        :param float tqfactor: set target Q factor (from 0.001 to 1000) (default 1)
        :param float attack: set attack duration (from 1 to 2000) (default 20)
        :param float release: set release duration (from 1 to 2000) (default 200)
        :param float ratio: set ratio factor (from 0 to 30) (default 1)
        :param float makeup: set makeup gain (from 0 to 100) (default 0)
        :param float range: set max gain (from 1 to 200) (default 50)
        :param int mode: set mode (from -1 to 1) (default cut)
        :param int tftype: set target filter type (from 0 to 2) (default bell)
        :param int direction: set direction (from 0 to 1) (default downward)
        :param int auto: set auto threshold (from -1 to 1) (default disabled)
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
        sensitivity: float | int | str = Default("2"),
        basefreq: float | int | str = Default("22050"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Dynamic Smoothing of input audio.

        Parameters:
        ----------

        :param float sensitivity: set smooth sensitivity (from 0 to 1e+06) (default 2)
        :param float basefreq: set base frequency (from 2 to 1e+06) (default 22050)
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
        in_gain: float | int | str = Default("0.6"),
        out_gain: float | int | str = Default("0.3"),
        delays: str | float | int = Default("1000"),
        decays: str | float | int = Default("0.5"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add echoing to the audio.

        Parameters:
        ----------

        :param float in_gain: set signal input gain (from 0 to 1) (default 0.6)
        :param float out_gain: set signal output gain (from 0 to 1) (default 0.3)
        :param str delays: set list of signal delays (default "1000")
        :param str decays: set list of signal decays (default "0.5")

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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        mode: int | Literal["reproduction", "production"] | Default = Default("reproduction"),
        type: int
        | Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"]
        | Default = Default("cd"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio emphasis.

        Parameters:
        ----------

        :param float level_in: set input gain (from 0 to 64) (default 1)
        :param float level_out: set output gain (from 0 to 64) (default 1)
        :param int mode: set filter mode (from 0 to 1) (default reproduction)
        :param int type: set filter type (from 0 to 8) (default cd)
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
        exprs: str | float | int = Default(None),
        channel_layout: str | float | int = Default(None),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Filter audio signal according to a specified expression.

        Parameters:
        ----------

        :param str exprs: set the '|'-separated list of channels expressions
        :param str channel_layout: set channel layout
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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        amount: float | int | str = Default("1"),
        drive: float | int | str = Default("8.5"),
        blend: float | int | str = Default("0"),
        freq: float | int | str = Default("7500"),
        ceil: float | int | str = Default("9999"),
        listen: bool | int | str = Default("false"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Enhance high frequency part of audio.

        Parameters:
        ----------

        :param float level_in: set level in (from 0 to 64) (default 1)
        :param float level_out: set level out (from 0 to 64) (default 1)
        :param float amount: set amount (from 0 to 64) (default 1)
        :param float drive: set harmonics (from 0.1 to 10) (default 8.5)
        :param float blend: set blend harmonics (from -10 to 10) (default 0)
        :param float freq: set scope (from 2000 to 12000) (default 7500)
        :param float ceil: set ceiling (from 9999 to 20000) (default 9999)
        :param bool listen: enable listen mode (default false)
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
        type: int | Literal["in", "out"] | Default = Default("in"),
        start_sample: int | str = Default("0"),
        nb_samples: int | str = Default("44100"),
        start_time: str | float | int = Default("0"),
        duration: str | float | int = Default("0"),
        curve: int
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
        silence: float | int | str = Default("0"),
        unity: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Fade in/out input audio.

        Parameters:
        ----------

        :param int type: set the fade direction (from 0 to 1) (default in)
        :param int start_sample: set number of first sample to start fading (from 0 to I64_MAX) (default 0)
        :param int nb_samples: set number of samples for fade duration (from 1 to I64_MAX) (default 44100)
        :param str start_time: set time to start fading (default 0)
        :param str duration: set fade duration (default 0)
        :param int curve: set fade curve type (from -1 to 18) (default tri)
        :param float silence: set the silence gain (from 0 to 1) (default 0)
        :param float unity: set the unity gain (from 0 to 1) (default 1)
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
        noise_reduction: float | int | str = Default("12"),
        noise_floor: float | int | str = Default("-50"),
        noise_type: int
        | Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | Default = Default("white"),
        band_noise: str | float | int = Default(None),
        residual_floor: float | int | str = Default("-38"),
        track_noise: bool | int | str = Default("false"),
        track_residual: bool | int | str = Default("false"),
        output_mode: int | Literal["input", "i", "output", "o", "noise", "n"] | Default = Default("output"),
        adaptivity: float | int | str = Default("0.5"),
        floor_offset: float | int | str = Default("1"),
        noise_link: int | Literal["none", "min", "max", "average"] | Default = Default("min"),
        band_multiplier: float | int | str = Default("1.25"),
        sample_noise: int | Literal["none", "start", "begin", "stop", "end"] | Default = Default("none"),
        gain_smooth: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Denoise audio samples using FFT.

        Parameters:
        ----------

        :param float noise_reduction: set the noise reduction (from 0.01 to 97) (default 12)
        :param float noise_floor: set the noise floor (from -80 to -20) (default -50)
        :param int noise_type: set the noise type (from 0 to 3) (default white)
        :param str band_noise: set the custom bands noise
        :param float residual_floor: set the residual floor (from -80 to -20) (default -38)
        :param bool track_noise: track noise (default false)
        :param bool track_residual: track residual (default false)
        :param int output_mode: set output mode (from 0 to 2) (default output)
        :param float adaptivity: set adaptivity factor (from 0 to 1) (default 0.5)
        :param float floor_offset: set noise floor offset factor (from -2 to 2) (default 1)
        :param int noise_link: set the noise floor link (from 0 to 3) (default min)
        :param float band_multiplier: set band multiplier (from 0.2 to 5) (default 1.25)
        :param int sample_noise: set sample noise mode (from 0 to 2) (default none)
        :param int gain_smooth: set gain smooth radius (from 0 to 50) (default 0)
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
        real: str | float | int = Default("re"),
        imag: str | float | int = Default("im"),
        win_size: int | str = Default("4096"),
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
        | Default = Default("hann"),
        overlap: float | int | str = Default("0.75"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply arbitrary expressions to samples in frequency domain.

        Parameters:
        ----------

        :param str real: set channels real expressions (default "re")
        :param str imag: set channels imaginary expressions (default "im")
        :param int win_size: set window size (from 16 to 131072) (default 4096)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param float overlap: set window overlap (from 0 to 1) (default 0.75)
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
        sample_fmts: str | float | int = Default(None),
        sample_rates: str | float | int = Default(None),
        channel_layouts: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Convert the input audio to one of the specified formats.

        Parameters:
        ----------

        :param str sample_fmts: A '|'-separated list of sample formats.
        :param str sample_rates: A '|'-separated list of sample rates.
        :param str channel_layouts: A '|'-separated list of channel layouts.

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
        shift: float | int | str = Default("0"),
        level: float | int | str = Default("1"),
        order: int | str = Default("8"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply frequency shifting to input audio.

        Parameters:
        ----------

        :param float shift: set frequency shift (from -2.14748e+09 to INT_MAX) (default 0)
        :param float level: set output level (from 0 to 1) (default 1)
        :param int order: set filter order (from 1 to 16) (default 8)
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
        sigma: float | int | str = Default("0"),
        levels: int | str = Default("10"),
        wavet: int | Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"] | Default = Default("sym10"),
        percent: float | int | str = Default("85"),
        profile: bool | int | str = Default("false"),
        adaptive: bool | int | str = Default("false"),
        samples: int | str = Default("8192"),
        softness: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Denoise audio stream using Wavelets.

        Parameters:
        ----------

        :param float sigma: set noise sigma (from 0 to 1) (default 0)
        :param int levels: set number of wavelet levels (from 1 to 12) (default 10)
        :param int wavet: set wavelet type (from 0 to 6) (default sym10)
        :param float percent: set percent of full denoising (from 0 to 100) (default 85)
        :param bool profile: profile noise (default false)
        :param bool adaptive: adaptive profiling of noise (default false)
        :param int samples: set frame size in number of samples (from 512 to 65536) (default 8192)
        :param float softness: set thresholding softness (from 0 to 10) (default 1)
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
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio gate.

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
        size: str | float | int = Default("hd720"),
        opacity: float | int | str = Default("0.9"),
        mode: int | Literal["full", "compact"] | Default = Default("full"),
        flags: str
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
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Show various filtergraph stats.

        Parameters:
        ----------

        :param str size: set monitor size (default "hd720")
        :param float opacity: set video opacity (from 0 to 1) (default 0.9)
        :param int mode: set mode (from 0 to 1) (default full)
        :param str flags: set flags (default queue)
        :param str rate: set video rate (default "25")

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
        dmode: int | Literal["single", "separate"] | Default = Default("single"),
        rate: str | float | int = Default("25"),
        size: str | float | int = Default("hd720"),
        scale: int | Literal["log", "sqrt", "cbrt", "lin", "rlog"] | Default = Default("log"),
        ascale: int | Literal["log", "lin"] | Default = Default("log"),
        acount: int | str = Default("1"),
        rheight: float | int | str = Default("0.1"),
        slide: int | Literal["replace", "scroll"] | Default = Default("replace"),
        hmode: int | Literal["abs", "sign"] | Default = Default("abs"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to histogram video output.

        Parameters:
        ----------

        :param int dmode: set method to display channels (from 0 to 1) (default single)
        :param str rate: set video rate (default "25")
        :param str size: set video size (default "hd720")
        :param int scale: set display scale (from 0 to 4) (default log)
        :param int ascale: set amplitude scale (from 0 to 1) (default log)
        :param int acount: how much frames to accumulate (from -1 to 100) (default 1)
        :param float rheight: set histogram ratio of window height (from 0 to 1) (default 0.1)
        :param int slide: set sonogram sliding (from 0 to 1) (default replace)
        :param int hmode: set histograms mode (from 0 to 1) (default abs)

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
        zeros: str | float | int = Default("1+0i 1-0i"),
        poles: str | float | int = Default("1+0i 1-0i"),
        gains: str | float | int = Default("1|1"),
        dry: float | int | str = Default("1"),
        wet: float | int | str = Default("1"),
        format: int | Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | Default = Default("zp"),
        process: int | Literal["d", "s", "p"] | Default = Default("s"),
        precision: int | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        e: int | Literal["dbl", "flt", "i32", "i16"] | Default = Default("dbl"),
        normalize: bool | int | str = Default("true"),
        mix: float | int | str = Default("1"),
        response: bool | int | str = Default("false"),
        channel: int | str = Default("0"),
        size: str | float | int = Default("hd720"),
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Apply Infinite Impulse Response filter with supplied coefficients.

        Parameters:
        ----------

        :param str zeros: set B/numerator/zeros/reflection coefficients (default "1+0i 1-0i")
        :param str poles: set A/denominator/poles/ladder coefficients (default "1+0i 1-0i")
        :param str gains: set channels gains (default "1|1")
        :param float dry: set dry gain (from 0 to 1) (default 1)
        :param float wet: set wet gain (from 0 to 1) (default 1)
        :param int format: set coefficients format (from -2 to 4) (default zp)
        :param int process: set kind of processing (from 0 to 2) (default s)
        :param int precision: set filtering precision (from 0 to 3) (default dbl)
        :param int e: set precision (from 0 to 3) (default dbl)
        :param bool normalize: normalize coefficients (default true)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param bool response: show IR frequency response (default false)
        :param int channel: set IR channel to display frequency response (from 0 to 1024) (default 0)
        :param str size: set video size (default "hd720")
        :param str rate: set video rate (default "25")

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

    def aintegral(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "AudioStream":
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

    def alatency(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "AudioStream":
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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        limit: float | int | str = Default("1"),
        attack: float | int | str = Default("5"),
        release: float | int | str = Default("50"),
        asc: bool | int | str = Default("false"),
        asc_level: float | int | str = Default("0.5"),
        level: bool | int | str = Default("true"),
        latency: bool | int | str = Default("false"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio lookahead limiter.

        Parameters:
        ----------

        :param float level_in: set input level (from 0.015625 to 64) (default 1)
        :param float level_out: set output level (from 0.015625 to 64) (default 1)
        :param float limit: set limit (from 0.0625 to 1) (default 1)
        :param float attack: set attack (from 0.1 to 80) (default 5)
        :param float release: set release (from 1 to 8000) (default 50)
        :param bool asc: enable asc (default false)
        :param float asc_level: set asc level (from 0 to 1) (default 0.5)
        :param bool level: auto level (default true)
        :param bool latency: compensate delay (default false)
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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.707"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        order: int | str = Default("2"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole all-pass filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.707)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int order: set filter order (from 1 to 2) (default 2)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
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
        self,
        *,
        loop: int | str = Default("0"),
        size: int | str = Default("0"),
        start: int | str = Default("0"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Loop audio samples.

        Parameters:
        ----------

        :param int loop: number of loops (from -1 to INT_MAX) (default 0)
        :param int size: max number of samples to loop (from 0 to INT_MAX) (default 0)
        :param int start: set the loop start sample (from 0 to I64_MAX) (default 0)

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
        mode: int | Literal["select", "add", "modify", "delete", "print"] | Default = Default("select"),
        key: str | float | int = Default(None),
        value: str | float | int = Default(None),
        function: int
        | Literal["same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"]
        | Default = Default("same_str"),
        expr: str | float | int = Default(None),
        file: str | float | int = Default(None),
        direct: bool | int | str = Default("false"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Manipulate audio frame metadata.

        Parameters:
        ----------

        :param int mode: set a mode of operation (from 0 to 4) (default select)
        :param str key: set metadata key
        :param str value: set metadata value
        :param int function: function for comparing values (from 0 to 6) (default same_str)
        :param str expr: set expression for expr function
        :param str file: set file where to print metadata information
        :param bool direct: reduce buffering when printing to user-set file or pipe (default false)
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
        params: str | float | int = Default(""),
        curves: bool | int | str = Default("false"),
        size: str | float | int = Default("hd720"),
        mgain: float | int | str = Default("60"),
        fscale: int | Literal["lin", "log"] | Default = Default("log"),
        colors: str | float | int = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Apply high-order audio parametric multi band equalizer.

        Parameters:
        ----------

        :param str params: (default "")
        :param bool curves: draw frequency response curves (default false)
        :param str size: set video size (default "hd720")
        :param float mgain: set max gain (from -900 to 900) (default 60)
        :param int fscale: set frequency scale (from 0 to 1) (default log)
        :param str colors: set channels curves colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
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
        strength: float | int | str = Default("1e-05"),
        patch: str | float | int = Default("0.002"),
        research: str | float | int = Default("0.006"),
        output: int | Literal["i", "o", "n"] | Default = Default("o"),
        smooth: float | int | str = Default("11"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Reduce broadband noise from stream using Non-Local Means.

        Parameters:
        ----------

        :param float strength: set denoising strength (from 1e-05 to 10000) (default 1e-05)
        :param str patch: set patch duration (default 0.002)
        :param str research: set research duration (default 0.006)
        :param int output: set output mode (from 0 to 2) (default o)
        :param float smooth: set smooth factor (from 1 to 1000) (default 11)
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
        order: int | str = Default("256"),
        mu: float | int | str = Default("0.75"),
        eps: float | int | str = Default("1"),
        leakage: float | int | str = Default("0"),
        out_mode: int | Literal["i", "d", "o", "n"] | Default = Default("o"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
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
        order: int | str = Default("256"),
        mu: float | int | str = Default("0.75"),
        eps: float | int | str = Default("1"),
        leakage: float | int | str = Default("0"),
        out_mode: int | Literal["i", "d", "o", "n"] | Default = Default("o"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
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
        packet_size: int | str = Default("4096"),
        pad_len: int | str = Default("-1"),
        whole_len: int | str = Default("-1"),
        pad_dur: str | float | int = Default("-0.000001"),
        whole_dur: str | float | int = Default("-0.000001"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Pad audio with silence.

        Parameters:
        ----------

        :param int packet_size: set silence packet size (from 0 to INT_MAX) (default 4096)
        :param int pad_len: set number of samples of silence to add (from -1 to I64_MAX) (default -1)
        :param int whole_len: set minimum target number of samples in the audio stream (from -1 to I64_MAX) (default -1)
        :param str pad_dur: set duration of silence to add (default -0.000001)
        :param str whole_dur: set minimum target duration in the audio stream (default -0.000001)
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
        mode: int | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default("none"),
        seed: int | str = Default("-1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Set permissions for the output audio frame.

        Parameters:
        ----------

        :param int mode: select permissions mode (from 0 to 4) (default none)
        :param int seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
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
        rate: str | float | int = Default("25"),
        size: str | float | int = Default("800x400"),
        rc: int | str = Default("2"),
        gc: int | str = Default("7"),
        bc: int | str = Default("1"),
        mpc: str | float | int = Default("none"),
        video: bool | int | str = Default("true"),
        phasing: bool | int | str = Default("false"),
        tolerance: float | int | str = Default("0"),
        angle: float | int | str = Default("170"),
        duration: str | float | int = Default("2"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Convert input audio to phase meter video output.

        Parameters:
        ----------

        :param str rate: set video rate (default "25")
        :param str size: set video size (default "800x400")
        :param int rc: set red contrast (from 0 to 255) (default 2)
        :param int gc: set green contrast (from 0 to 255) (default 7)
        :param int bc: set blue contrast (from 0 to 255) (default 1)
        :param str mpc: set median phase color (default "none")
        :param bool video: set video output (default true)
        :param bool phasing: set mono and out-of-phase detection output (default false)
        :param float tolerance: set phase tolerance for mono detection (from 0 to 1) (default 0)
        :param float angle: set angle threshold for out-of-phase detection (from 90 to 180) (default 170)
        :param str duration: set minimum mono or out-of-phase duration in seconds (default 2)

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
        in_gain: float | int | str = Default("0.4"),
        out_gain: float | int | str = Default("0.74"),
        delay: float | int | str = Default("3"),
        decay: float | int | str = Default("0.4"),
        speed: float | int | str = Default("0.5"),
        type: int | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default("triangular"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add a phasing effect to the audio.

        Parameters:
        ----------

        :param float in_gain: set input gain (from 0 to 1) (default 0.4)
        :param float out_gain: set output gain (from 0 to 1e+09) (default 0.74)
        :param float delay: set delay in milliseconds (from 0 to 5) (default 3)
        :param float decay: set decay (from 0 to 0.99) (default 0.4)
        :param float speed: set modulation speed (from 0.1 to 2) (default 0.5)
        :param int type: set modulation type (from 0 to 1) (default triangular)

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
        shift: float | int | str = Default("0"),
        level: float | int | str = Default("1"),
        order: int | str = Default("8"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply phase shifting to input audio.

        Parameters:
        ----------

        :param float shift: set phase shift (from -1 to 1) (default 0)
        :param float level: set output level (from 0 to 1) (default 1)
        :param int order: set filter order (from 1 to 16) (default 8)
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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        clip: float | int | str = Default("1"),
        diff: bool | int | str = Default("false"),
        adaptive: float | int | str = Default("0.5"),
        iterations: int | str = Default("10"),
        level: bool | int | str = Default("false"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Psychoacoustic Clipper.

        Parameters:
        ----------

        :param float level_in: set input level (from 0.015625 to 64) (default 1)
        :param float level_out: set output level (from 0.015625 to 64) (default 1)
        :param float clip: set clip level (from 0.015625 to 1) (default 1)
        :param bool diff: enable difference (default false)
        :param float adaptive: set adaptive distortion (from 0 to 1) (default 0.5)
        :param int iterations: set iterations (from 1 to 20) (default 10)
        :param bool level: set auto level (default false)
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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        mode: int | Literal["sine", "triangle", "square", "sawup", "sawdown"] | Default = Default("sine"),
        amount: float | int | str = Default("1"),
        offset_l: float | int | str = Default("0"),
        offset_r: float | int | str = Default("0.5"),
        width: float | int | str = Default("1"),
        timing: int | Literal["bpm", "ms", "hz"] | Default = Default("hz"),
        bpm: float | int | str = Default("120"),
        ms: int | str = Default("500"),
        hz: float | int | str = Default("2"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio pulsator.

        Parameters:
        ----------

        :param float level_in: set input gain (from 0.015625 to 64) (default 1)
        :param float level_out: set output gain (from 0.015625 to 64) (default 1)
        :param int mode: set mode (from 0 to 4) (default sine)
        :param float amount: set modulation (from 0 to 1) (default 1)
        :param float offset_l: set offset L (from 0 to 1) (default 0)
        :param float offset_r: set offset R (from 0 to 1) (default 0.5)
        :param float width: set pulse width (from 0 to 2) (default 1)
        :param int timing: set timing (from 0 to 2) (default hz)
        :param float bpm: set BPM (from 30 to 300) (default 120)
        :param int ms: set ms (from 10 to 2000) (default 500)
        :param float hz: set frequency (from 0.01 to 100) (default 2)

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
        self, *, limit: str | float | int = Default("2"), speed: float | int | str = Default("1"), **kwargs: Any
    ) -> "AudioStream":
        """

        Slow down filtering to match realtime.

        Parameters:
        ----------

        :param str limit: sleep time limit (default 2)
        :param float speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)

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

    def aresample(self, *, sample_rate: int | str = Default("0"), **kwargs: Any) -> "AudioStream":
        """

        Resample audio data.

        Parameters:
        ----------

        :param int sample_rate: (from 0 to INT_MAX) (default 0)

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
        self,
        *,
        model: str | float | int = Default(None),
        mix: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Reduce noise from speech using Recurrent Neural Networks.

        Parameters:
        ----------

        :param str model: set model name
        :param float mix: set output vs input mix (from -1 to 1) (default 1)
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
        self,
        *,
        timestamps: str | float | int = Default(None),
        samples: str | float | int = Default(None),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Segment audio stream.

        Parameters:
        ----------

        :param str timestamps: timestamps of input at which to split input
        :param str samples: samples at which to split input

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

    def aselect(
        self, *, expr: str | float | int = Default("1"), outputs: int | str = Default("1"), **kwargs: Any
    ) -> FilterNode:
        """

        Select audio frames to pass in output.

        Parameters:
        ----------

        :param str expr: set an expression to use for selecting frames (default "1")
        :param int outputs: set the number of outputs (from 1 to INT_MAX) (default 1)

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
        self, *, commands: str | float | int = Default(None), filename: str | float | int = Default(None), **kwargs: Any
    ) -> "AudioStream":
        """

        Send commands to filters.

        Parameters:
        ----------

        :param str commands: set commands
        :param str filename: set commands file

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
        self, *, nb_out_samples: int | str = Default("1024"), pad: bool | int | str = Default("true"), **kwargs: Any
    ) -> "AudioStream":
        """

        Set the number of samples for each output audio frames.

        Parameters:
        ----------

        :param int nb_out_samples: set the number of per-frame output samples (from 1 to INT_MAX) (default 1024)
        :param bool pad: pad last frame with zeros (default true)

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

    def asetpts(self, *, expr: str | float | int = Default("PTS"), **kwargs: Any) -> "AudioStream":
        """

        Set PTS for the output audio frame.

        Parameters:
        ----------

        :param str expr: Expression determining the frame timestamp (default "PTS")

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

    def asetrate(self, *, sample_rate: int | str = Default("44100"), **kwargs: Any) -> "AudioStream":
        """

        Change the sample rate without altering the data.

        Parameters:
        ----------

        :param int sample_rate: set the sample rate (from 1 to INT_MAX) (default 44100)

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

    def asettb(self, *, expr: str | float | int = Default("intb"), **kwargs: Any) -> "AudioStream":
        """

        Set timebase for the audio output link.

        Parameters:
        ----------

        :param str expr: set expression determining the output timebase (default "intb")

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
        mode: int | Literal["select", "delete"] | Default = Default("select"),
        type: int
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
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Manipulate audio frame side data.

        Parameters:
        ----------

        :param int mode: set a mode of operation (from 0 to 1) (default select)
        :param int type: set side data type (from -1 to INT_MAX) (default -1)
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
        type: int
        | Literal["hard", "tanh", "atan", "cubic", "exp", "alg", "quintic", "sin", "erf"]
        | Default = Default("tanh"),
        threshold: float | int | str = Default("1"),
        output: float | int | str = Default("1"),
        param: float | int | str = Default("1"),
        oversample: int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Soft Clipper.

        Parameters:
        ----------

        :param int type: set softclip type (from -1 to 7) (default tanh)
        :param float threshold: set softclip threshold (from 1e-06 to 1) (default 1)
        :param float output: set softclip output gain (from 1e-06 to 16) (default 1)
        :param float param: set softclip parameter (from 0.01 to 3) (default 1)
        :param int oversample: set oversample factor (from 1 to 64) (default 1)
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
        win_size: int | str = Default("2048"),
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
        | Default = Default("hann"),
        overlap: float | int | str = Default("0.5"),
        measure: str
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

        :param int win_size: set the window size (from 32 to 65536) (default 2048)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param float overlap: set window overlap (from 0 to 1) (default 0.5)
        :param str measure: select the parameters which are measured (default all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff)

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

    def asplit(self, *, outputs: int | str = Default("2"), **kwargs: Any) -> FilterNode:
        """

        Pass on the audio input to N audio outputs.

        Parameters:
        ----------

        :param int outputs: set number of outputs (from 1 to INT_MAX) (default 2)

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
        length: float | int | str = Default("0.05"),
        metadata: bool | int | str = Default("false"),
        reset: int | str = Default("0"),
        measure_perchannel: str
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
        measure_overall: str
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

        :param float length: set the window length (from 0 to 10) (default 0.05)
        :param bool metadata: inject metadata in the filtergraph (default false)
        :param int reset: Set the number of frames over which cumulative stats are calculated before being reset (from 0 to INT_MAX) (default 0)
        :param str measure_perchannel: Select the parameters which are measured per channel (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate)
        :param str measure_overall: Select the parameters which are measured overall (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate)

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
        dry: float | int | str = Default("1"),
        wet: float | int | str = Default("1"),
        boost: float | int | str = Default("2"),
        decay: float | int | str = Default("0"),
        feedback: float | int | str = Default("0.9"),
        cutoff: float | int | str = Default("100"),
        slope: float | int | str = Default("0.5"),
        delay: float | int | str = Default("20"),
        channels: str | float | int = Default("all"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost subwoofer frequencies.

        Parameters:
        ----------

        :param float dry: set dry gain (from 0 to 1) (default 1)
        :param float wet: set wet gain (from 0 to 1) (default 1)
        :param float boost: set max boost (from 1 to 12) (default 2)
        :param float decay: set decay (from 0 to 1) (default 0)
        :param float feedback: set feedback (from 0 to 1) (default 0.9)
        :param float cutoff: set cutoff (from 50 to 900) (default 100)
        :param float slope: set slope (from 0.0001 to 1) (default 0.5)
        :param float delay: set delay (from 1 to 100) (default 20)
        :param str channels: set channels to filter (default "all")
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
        cutoff: float | int | str = Default("20"),
        order: int | str = Default("10"),
        level: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Cut subwoofer frequencies.

        Parameters:
        ----------

        :param float cutoff: set cutoff frequency (from 2 to 200) (default 20)
        :param int order: set filter order (from 3 to 20) (default 10)
        :param float level: set input level (from 0 to 1) (default 1)
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
        cutoff: float | int | str = Default("20000"),
        order: int | str = Default("10"),
        level: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Cut super frequencies.

        Parameters:
        ----------

        :param float cutoff: set cutoff frequency (from 20000 to 192000) (default 20000)
        :param int order: set filter order (from 3 to 20) (default 10)
        :param float level: set input level (from 0 to 1) (default 1)
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
        centerf: float | int | str = Default("1000"),
        order: int | str = Default("4"),
        qfactor: float | int | str = Default("1"),
        level: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply high order Butterworth band-pass filter.

        Parameters:
        ----------

        :param float centerf: set center frequency (from 2 to 999999) (default 1000)
        :param int order: set filter order (from 4 to 20) (default 4)
        :param float qfactor: set Q-factor (from 0.01 to 100) (default 1)
        :param float level: set input level (from 0 to 2) (default 1)
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
        centerf: float | int | str = Default("1000"),
        order: int | str = Default("4"),
        qfactor: float | int | str = Default("1"),
        level: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply high order Butterworth band-stop filter.

        Parameters:
        ----------

        :param float centerf: set center frequency (from 2 to 999999) (default 1000)
        :param int order: set filter order (from 4 to 20) (default 4)
        :param float qfactor: set Q-factor (from 0.01 to 100) (default 1)
        :param float level: set input level (from 0 to 2) (default 1)
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

    def atempo(self, *, tempo: float | int | str = Default("1"), **kwargs: Any) -> "AudioStream":
        """

        Adjust audio tempo.

        Parameters:
        ----------

        :param float tempo: set tempo scale factor (from 0.5 to 100) (default 1)

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
        freq: float | int | str = Default("10000"),
        slope: float | int | str = Default("0"),
        width: float | int | str = Default("1000"),
        order: int | str = Default("5"),
        level: float | int | str = Default("1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply spectral tilt to audio.

        Parameters:
        ----------

        :param float freq: set central frequency (from 20 to 192000) (default 10000)
        :param float slope: set filter slope (from -1 to 1) (default 0)
        :param float width: set filter width (from 100 to 10000) (default 1000)
        :param int order: set filter order (from 2 to 30) (default 5)
        :param float level: set input level (from 0 to 4) (default 1)
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
        start: str | float | int = Default("INT64_MAX"),
        end: str | float | int = Default("INT64_MAX"),
        start_pts: int | str = Default("I64_MIN"),
        end_pts: int | str = Default("I64_MIN"),
        duration: str | float | int = Default("0"),
        start_sample: int | str = Default("-1"),
        end_sample: int | str = Default("I64_MAX"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Pick one continuous section from the input, drop the rest.

        Parameters:
        ----------

        :param str start: Timestamp of the first frame that should be passed (default INT64_MAX)
        :param str end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
        :param int start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
        :param int end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
        :param str duration: Maximum duration of the output (default 0)
        :param int start_sample: Number of the first audio sample that should be passed to the output (from -1 to I64_MAX) (default -1)
        :param int end_sample: Number of the first audio sample that should be dropped again (from 0 to I64_MAX) (default I64_MAX)

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
        mode: int | Literal["lissajous", "lissajous_xy", "polar"] | Default = Default("lissajous"),
        rate: str | float | int = Default("25"),
        size: str | float | int = Default("400x400"),
        rc: int | str = Default("40"),
        gc: int | str = Default("160"),
        bc: int | str = Default("80"),
        ac: int | str = Default("255"),
        rf: int | str = Default("15"),
        gf: int | str = Default("10"),
        bf: int | str = Default("5"),
        af: int | str = Default("5"),
        zoom: float | int | str = Default("1"),
        draw: int | Literal["dot", "line", "aaline"] | Default = Default("dot"),
        scale: int | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("lin"),
        swap: bool | int | str = Default("true"),
        mirror: int | Literal["none", "x", "y", "xy"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to vectorscope video output.

        Parameters:
        ----------

        :param int mode: set mode (from 0 to 2) (default lissajous)
        :param str rate: set video rate (default "25")
        :param str size: set video size (default "400x400")
        :param int rc: set red contrast (from 0 to 255) (default 40)
        :param int gc: set green contrast (from 0 to 255) (default 160)
        :param int bc: set blue contrast (from 0 to 255) (default 80)
        :param int ac: set alpha contrast (from 0 to 255) (default 255)
        :param int rf: set red fade (from 0 to 255) (default 15)
        :param int gf: set green fade (from 0 to 255) (default 10)
        :param int bf: set blue fade (from 0 to 255) (default 5)
        :param int af: set alpha fade (from 0 to 255) (default 5)
        :param float zoom: set zoom factor (from 0 to 10) (default 1)
        :param int draw: set draw mode (from 0 to 2) (default dot)
        :param int scale: set amplitude scale mode (from 0 to 3) (default lin)
        :param bool swap: swap x axis with y axis (default true)
        :param int mirror: mirror axis (from 0 to 3) (default none)

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
        size: int | str = Default("256"),
        algo: int | Literal["slow", "fast"] | Default = Default("slow"),
        **kwargs: Any,
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

    def azmq(self, *, bind_address: str | float | int = Default("tcp://*:5555"), **kwargs: Any) -> "AudioStream":
        """

        Receive commands through ZMQ and broker them to filters.

        Parameters:
        ----------

        :param str bind_address: set bind address (default "tcp://*:5555")

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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        csg: bool | int | str = Default("false"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole Butterworth band-pass filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param bool csg: use constant skirt gain (default false)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a two-pole Butterworth band-reject filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        frequency: float | int | str = Default("100"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        gain: float | int | str = Default("0"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost or cut lower frequencies.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 100)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        a0: float | int | str = Default("1"),
        a1: float | int | str = Default("0"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a biquad IIR filter with the given coefficients.

        Parameters:
        ----------

        :param float a0: (from INT_MIN to INT_MAX) (default 1)
        :param float a1: (from INT_MIN to INT_MAX) (default 0)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        self,
        *,
        map: str | float | int = Default(None),
        channel_layout: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remap audio channels.

        Parameters:
        ----------

        :param str map: A comma-separated list of input channel numbers in output order.
        :param str channel_layout: Output channel layout.

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
        self,
        *,
        channel_layout: str | float | int = Default("stereo"),
        channels: str | float | int = Default("all"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Split audio into per-channel streams.

        Parameters:
        ----------

        :param str channel_layout: Input channel layout. (default "stereo")
        :param str channels: Channels to extract. (default "all")

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
        in_gain: float | int | str = Default("0.4"),
        out_gain: float | int | str = Default("0.4"),
        delays: str | float | int = Default(None),
        decays: str | float | int = Default(None),
        speeds: str | float | int = Default(None),
        depths: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Add a chorus effect to the audio.

        Parameters:
        ----------

        :param float in_gain: set input gain (from 0 to 1) (default 0.4)
        :param float out_gain: set output gain (from 0 to 1) (default 0.4)
        :param str delays: set delays
        :param str decays: set decays
        :param str speeds: set speeds
        :param str depths: set depths

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
        attacks: str | float | int = Default("0"),
        decays: str | float | int = Default("0.8"),
        points: str | float | int = Default("-70/-70|-60/-20|1/0"),
        soft_knee: float | int | str = Default("0.01"),
        gain: float | int | str = Default("0"),
        volume: float | int | str = Default("0"),
        delay: float | int | str = Default("0"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Compress or expand audio dynamic range.

        Parameters:
        ----------

        :param str attacks: set time over which increase of volume is determined (default "0")
        :param str decays: set time over which decrease of volume is determined (default "0.8")
        :param str points: set points of transfer function (default "-70/-70|-60/-20|1/0")
        :param float soft_knee: set soft-knee (from 0.01 to 900) (default 0.01)
        :param float gain: set output gain (from -900 to 900) (default 0)
        :param float volume: set initial volume (from -900 to 0) (default 0)
        :param float delay: set delay for samples before sending them to volume adjuster (from 0 to 20) (default 0)

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
        mm: int | str = Default("0"),
        cm: int | str = Default("0"),
        m: int | str = Default("0"),
        dry: float | int | str = Default("0"),
        wet: float | int | str = Default("1"),
        temp: int | str = Default("20"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Compensation Delay Line.

        Parameters:
        ----------

        :param int mm: set mm distance (from 0 to 10) (default 0)
        :param int cm: set cm distance (from 0 to 100) (default 0)
        :param int m: set meter distance (from 0 to 100) (default 0)
        :param float dry: set dry amount (from 0 to 1) (default 0)
        :param float wet: set wet amount (from 0 to 1) (default 1)
        :param int temp: set temperature °C (from -50 to 50) (default 20)
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
        strength: float | int | str = Default("0.2"),
        range: float | int | str = Default("0.5"),
        slope: float | int | str = Default("0.5"),
        level_in: float | int | str = Default("0.9"),
        level_out: float | int | str = Default("1"),
        block_size: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply headphone crossfeed filter.

        Parameters:
        ----------

        :param float strength: set crossfeed strength (from 0 to 1) (default 0.2)
        :param float range: set soundstage wideness (from 0 to 1) (default 0.5)
        :param float slope: set curve slope (from 0.01 to 1) (default 0.5)
        :param float level_in: set level in (from 0 to 1) (default 0.9)
        :param float level_out: set level out (from 0 to 1) (default 1)
        :param int block_size: set the block size (from 0 to 32768) (default 0)
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
        self,
        *,
        i: float | int | str = Default("2"),
        c: bool | int | str = Default("true"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Simple audio noise sharpening filter.

        Parameters:
        ----------

        :param float i: set intensity (from -10 to 10) (default 2)
        :param bool c: enable clipping (default true)
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
        shift: float | int | str = Default("0"),
        limitergain: float | int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a DC shift to the audio.

        Parameters:
        ----------

        :param float shift: set DC shift (from -1 to 1) (default 0)
        :param float limitergain: set limiter gain (from 0 to 1) (default 0)
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
        i: float | int | str = Default("0"),
        m: float | int | str = Default("0.5"),
        f: float | int | str = Default("0.5"),
        s: int | Literal["i", "o", "e"] | Default = Default("o"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply de-essing to the audio.

        Parameters:
        ----------

        :param float i: set intensity (from 0 to 1) (default 0)
        :param float m: set max deessing (from 0 to 1) (default 0.5)
        :param float f: set frequency (from 0 to 1) (default 0.5)
        :param int s: set output mode (from 0 to 2) (default o)
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
        original: float | int | str = Default("1"),
        enhance: float | int | str = Default("1"),
        voice: float | int | str = Default("2"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Dialogue Enhancement.

        Parameters:
        ----------

        :param float original: set original center factor (from 0 to 1) (default 1)
        :param float enhance: set dialogue enhance factor (from 0 to 3) (default 1)
        :param float voice: set voice detection factor (from 2 to 32) (default 2)
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

    def drmeter(self, *, length: float | int | str = Default("3"), **kwargs: Any) -> "AudioStream":
        """

        Measure audio dynamic range.

        Parameters:
        ----------

        :param float length: set the window length (from 0.01 to 10) (default 3)

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
        framelen: int | str = Default("500"),
        gausssize: int | str = Default("31"),
        peak: float | int | str = Default("0.95"),
        maxgain: float | int | str = Default("10"),
        targetrms: float | int | str = Default("0"),
        coupling: bool | int | str = Default("true"),
        correctdc: bool | int | str = Default("false"),
        altboundary: bool | int | str = Default("false"),
        compress: float | int | str = Default("0"),
        threshold: float | int | str = Default("0"),
        channels: str | float | int = Default("all"),
        overlap: float | int | str = Default("0"),
        curve: str | float | int = Default(None),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Dynamic Audio Normalizer.

        Parameters:
        ----------

        :param int framelen: set the frame length in msec (from 10 to 8000) (default 500)
        :param int gausssize: set the filter size (from 3 to 301) (default 31)
        :param float peak: set the peak value (from 0 to 1) (default 0.95)
        :param float maxgain: set the max amplification (from 1 to 100) (default 10)
        :param float targetrms: set the target RMS (from 0 to 1) (default 0)
        :param bool coupling: set channel coupling (default true)
        :param bool correctdc: set DC correction (default false)
        :param bool altboundary: set alternative boundary mode (default false)
        :param float compress: set the compress factor (from 0 to 30) (default 0)
        :param float threshold: set the threshold value (from 0 to 1) (default 0)
        :param str channels: set channels to filter (default "all")
        :param float overlap: set the frame overlap (from 0 to 1) (default 0)
        :param str curve: set the custom peak mapping curve
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
        video: bool | int | str = Default("false"),
        size: str | float | int = Default("640x480"),
        meter: int | str = Default("9"),
        framelog: int | Literal["quiet", "info", "verbose"] | Default = Default("-1"),
        metadata: bool | int | str = Default("false"),
        peak: str | Literal["none", "sample", "true"] | Default = Default("0"),
        dualmono: bool | int | str = Default("false"),
        panlaw: float | int | str = Default("-3.0103"),
        target: int | str = Default("-23"),
        gauge: int | Literal["momentary", "m", "shortterm", "s"] | Default = Default("momentary"),
        scale: int | Literal["absolute", "LUFS", "relative", "LU"] | Default = Default("absolute"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        EBU R128 scanner.

        Parameters:
        ----------

        :param bool video: set video output (default false)
        :param str size: set video size (default "640x480")
        :param int meter: set scale meter (+9 to +18) (from 9 to 18) (default 9)
        :param int framelog: force frame logging level (from INT_MIN to INT_MAX) (default -1)
        :param bool metadata: inject metadata in the filtergraph (default false)
        :param str peak: set peak mode (default 0)
        :param bool dualmono: treat mono input files as dual-mono (default false)
        :param float panlaw: set a specific pan law for dual-mono files (from -10 to 0) (default -3.0103)
        :param int target: set a specific target level in LUFS (-23 to 0) (from -23 to 0) (default -23)
        :param int gauge: set gauge display type (from 0 to 1) (default momentary)
        :param int scale: sets display method for the stats (from 0 to 1) (default absolute)

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
        frequency: float | int | str = Default("0"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("1"),
        gain: float | int | str = Default("0"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply two-pole peaking equalization (EQ) filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 0)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 1)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        self,
        *,
        m: float | int | str = Default("2.5"),
        c: bool | int | str = Default("true"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Increase difference between stereo audio channels.

        Parameters:
        ----------

        :param float m: set the difference coefficient (from -10 to 10) (default 2.5)
        :param bool c: enable clipping (default true)
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
        gain: str | float | int = Default("gain_interpolate(f"),
        gain_entry: str | float | int = Default(None),
        delay: float | int | str = Default("0.01"),
        accuracy: float | int | str = Default("5"),
        wfunc: int
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
        fixed: bool | int | str = Default("false"),
        multi: bool | int | str = Default("false"),
        zero_phase: bool | int | str = Default("false"),
        scale: int | Literal["linlin", "linlog", "loglin", "loglog"] | Default = Default("linlog"),
        dumpfile: str | float | int = Default(None),
        dumpscale: int | Literal["linlin", "linlog", "loglin", "loglog"] | Default = Default("linlog"),
        fft2: bool | int | str = Default("false"),
        min_phase: bool | int | str = Default("false"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Finite Impulse Response Equalizer.

        Parameters:
        ----------

        :param str gain: set gain curve (default "gain_interpolate(f)")
        :param str gain_entry: set gain entry
        :param float delay: set delay (from 0 to 1e+10) (default 0.01)
        :param float accuracy: set accuracy (from 0 to 1e+10) (default 5)
        :param int wfunc: set window function (from 0 to 9) (default hann)
        :param bool fixed: set fixed frame samples (default false)
        :param bool multi: set multi channels mode (default false)
        :param bool zero_phase: set zero phase mode (default false)
        :param int scale: set gain scale (from 0 to 3) (default linlog)
        :param str dumpfile: set dump file
        :param int dumpscale: set dump scale (from 0 to 3) (default linlog)
        :param bool fft2: set 2-channels fft (default false)
        :param bool min_phase: set minimum phase mode (default false)

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
        delay: float | int | str = Default("0"),
        depth: float | int | str = Default("2"),
        regen: float | int | str = Default("0"),
        width: float | int | str = Default("71"),
        speed: float | int | str = Default("0.5"),
        shape: int | Literal["triangular", "t", "sinusoidal", "s"] | Default = Default("sinusoidal"),
        phase: float | int | str = Default("25"),
        interp: int | Literal["linear", "quadratic"] | Default = Default("linear"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a flanging effect to the audio.

        Parameters:
        ----------

        :param float delay: base delay in milliseconds (from 0 to 30) (default 0)
        :param float depth: added swept delay in milliseconds (from 0 to 10) (default 2)
        :param float regen: percentage regeneration (delayed signal feedback) (from -95 to 95) (default 0)
        :param float width: percentage of delayed signal mixed with original (from 0 to 100) (default 71)
        :param float speed: sweeps per second (Hz) (from 0.1 to 10) (default 0.5)
        :param int shape: swept wave shape (from 0 to 1) (default sinusoidal)
        :param float phase: swept wave percentage phase-shift for multi-channel (from 0 to 100) (default 25)
        :param int interp: delay-line interpolation (from 0 to 1) (default linear)

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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        side_gain: float | int | str = Default("1"),
        middle_source: int | Literal["left", "right", "mid", "side"] | Default = Default("mid"),
        middle_phase: bool | int | str = Default("false"),
        left_delay: float | int | str = Default("2.05"),
        left_balance: float | int | str = Default("-1"),
        left_gain: float | int | str = Default("1"),
        left_phase: bool | int | str = Default("false"),
        right_delay: float | int | str = Default("2.12"),
        right_balance: float | int | str = Default("1"),
        right_gain: float | int | str = Default("1"),
        right_phase: bool | int | str = Default("true"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply Haas Stereo Enhancer.

        Parameters:
        ----------

        :param float level_in: set level in (from 0.015625 to 64) (default 1)
        :param float level_out: set level out (from 0.015625 to 64) (default 1)
        :param float side_gain: set side gain (from 0.015625 to 64) (default 1)
        :param int middle_source: set middle source (from 0 to 3) (default mid)
        :param bool middle_phase: set middle phase (default false)
        :param float left_delay: set left delay (from 0 to 40) (default 2.05)
        :param float left_balance: set left balance (from -1 to 1) (default -1)
        :param float left_gain: set left gain (from 0.015625 to 64) (default 1)
        :param bool left_phase: set left phase (default false)
        :param float right_delay: set right delay (from 0 to 40) (default 2.12)
        :param float right_balance: set right balance (from -1 to 1) (default 1)
        :param float right_gain: set right gain (from 0.015625 to 64) (default 1)
        :param bool right_phase: set right phase (default true)

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
        disable_autoconvert: bool | int | str = Default("true"),
        process_stereo: bool | int | str = Default("true"),
        cdt_ms: int | str = Default("2000"),
        force_pe: bool | int | str = Default("false"),
        analyze_mode: int | Literal["off", "lle", "pe", "cdt", "tgm"] | Default = Default("off"),
        bits_per_sample: int | Literal["16", "20", "24"] | Default = Default("16"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply High Definition Compatible Digital (HDCD) decoding.

        Parameters:
        ----------

        :param bool disable_autoconvert: Disable any format conversion or resampling in the filter graph. (default true)
        :param bool process_stereo: Process stereo channels together. Only apply target_gain when both channels match. (default true)
        :param int cdt_ms: Code detect timer period in ms. (from 100 to 60000) (default 2000)
        :param bool force_pe: Always extend peaks above -3dBFS even when PE is not signaled. (default false)
        :param int analyze_mode: Replace audio with solid tone and signal some processing aspect in the amplitude. (from 0 to 4) (default off)
        :param int bits_per_sample: Valid bits per sample (location of the true LSB). (from 16 to 24) (default 16)

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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.707"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a high-pass filter with 3dB point frequency.

        Parameters:
        ----------

        :param float frequency: set frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.707)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        gain: float | int | str = Default("0"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a high shelf filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        I: float | int | str = Default("-24"),
        LRA: float | int | str = Default("7"),
        TP: float | int | str = Default("-2"),
        measured_I: float | int | str = Default("0"),
        measured_LRA: float | int | str = Default("0"),
        measured_TP: float | int | str = Default("99"),
        measured_thresh: float | int | str = Default("-70"),
        offset: float | int | str = Default("0"),
        linear: bool | int | str = Default("true"),
        dual_mono: bool | int | str = Default("false"),
        print_format: int | Literal["none", "json", "summary"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        EBU R128 loudness normalization

        Parameters:
        ----------

        :param float I: set integrated loudness target (from -70 to -5) (default -24)
        :param float LRA: set loudness range target (from 1 to 50) (default 7)
        :param float TP: set maximum true peak (from -9 to 0) (default -2)
        :param float measured_I: measured IL of input file (from -99 to 0) (default 0)
        :param float measured_LRA: measured LRA of input file (from 0 to 99) (default 0)
        :param float measured_TP: measured true peak of input file (from -99 to 99) (default 99)
        :param float measured_thresh: measured threshold of input file (from -99 to 0) (default -70)
        :param float offset: set offset gain (from -99 to 99) (default 0)
        :param bool linear: normalize linearly if possible (default true)
        :param bool dual_mono: treat mono input as dual-mono (default false)
        :param int print_format: set print format for stats (from 0 to 2) (default none)

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
        frequency: float | int | str = Default("500"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.707"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a low-pass filter with 3dB point frequency.

        Parameters:
        ----------

        :param float frequency: set frequency (from 0 to 999999) (default 500)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.707)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        frequency: float | int | str = Default("100"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        gain: float | int | str = Default("0"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a low shelf filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 100)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        args: str
        | float
        | int = Default(
            "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000"
        ),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Multiband Compress or expand audio dynamic range.

        Parameters:
        ----------

        :param str args: set parameters for each band (default "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000")

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

    def pan(self, *, args: str | float | int = Default(None), **kwargs: Any) -> "AudioStream":
        """

        Remix channels with coefficients (panning).

        Parameters:
        ----------

        :param str args:

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
        tempo: float | int | str = Default("1"),
        pitch: float | int | str = Default("1"),
        transients: int | Literal["crisp", "mixed", "smooth"] | Default = Default("crisp"),
        detector: int | Literal["compound", "percussive", "soft"] | Default = Default("compound"),
        phase: int | Literal["laminar", "independent"] | Default = Default("laminar"),
        window: int | Literal["standard", "short", "long"] | Default = Default("standard"),
        smoothing: int | Literal["off", "on"] | Default = Default("off"),
        formant: int | Literal["shifted", "preserved"] | Default = Default("shifted"),
        pitchq: int | Literal["quality", "speed", "consistency"] | Default = Default("speed"),
        channels: int | Literal["apart", "together"] | Default = Default("apart"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply time-stretching and pitch-shifting.

        Parameters:
        ----------

        :param float tempo: set tempo scale factor (from 0.01 to 100) (default 1)
        :param float pitch: set pitch scale factor (from 0.01 to 100) (default 1)
        :param int transients: set transients (from 0 to INT_MAX) (default crisp)
        :param int detector: set detector (from 0 to INT_MAX) (default compound)
        :param int phase: set phase (from 0 to INT_MAX) (default laminar)
        :param int window: set window (from 0 to INT_MAX) (default standard)
        :param int smoothing: set smoothing (from 0 to INT_MAX) (default off)
        :param int formant: set formant (from 0 to INT_MAX) (default shifted)
        :param int pitchq: set pitch quality (from 0 to INT_MAX) (default speed)
        :param int channels: set channels (from 0 to INT_MAX) (default apart)

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
        size: str | float | int = Default("1920x1080"),
        fps: str | float | int = Default("25"),
        bar_h: int | str = Default("-1"),
        axis_h: int | str = Default("-1"),
        sono_h: int | str = Default("-1"),
        fullhd: bool | int | str = Default("true"),
        sono_v: str | float | int = Default("16"),
        bar_v: str | float | int = Default("sono_v"),
        sono_g: float | int | str = Default("3"),
        bar_g: float | int | str = Default("1"),
        bar_t: float | int | str = Default("1"),
        timeclamp: float | int | str = Default("0.17"),
        attack: float | int | str = Default("0"),
        basefreq: float | int | str = Default("20.0152"),
        endfreq: float | int | str = Default("20495.6"),
        coeffclamp: float | int | str = Default("1"),
        tlength: str | float | int = Default("384*tc/(384+tc*f"),
        count: int | str = Default("6"),
        fcount: int | str = Default("0"),
        fontfile: str | float | int = Default(None),
        font: str | float | int = Default(None),
        fontcolor: str | float | int = Default("st(0, (midi(f"),
        axisfile: str | float | int = Default(None),
        axis: bool | int | str = Default("true"),
        csp: int
        | Literal["unspecified", "bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "bt2020ncl"]
        | Default = Default("unspecified"),
        cscheme: str | float | int = Default("1|0.5|0|0|0.5|1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output.

        Parameters:
        ----------

        :param str size: set video size (default "1920x1080")
        :param str fps: set video rate (default "25")
        :param int bar_h: set bargraph height (from -1 to INT_MAX) (default -1)
        :param int axis_h: set axis height (from -1 to INT_MAX) (default -1)
        :param int sono_h: set sonogram height (from -1 to INT_MAX) (default -1)
        :param bool fullhd: set fullhd size (default true)
        :param str sono_v: set sonogram volume (default "16")
        :param str bar_v: set bargraph volume (default "sono_v")
        :param float sono_g: set sonogram gamma (from 1 to 7) (default 3)
        :param float bar_g: set bargraph gamma (from 1 to 7) (default 1)
        :param float bar_t: set bar transparency (from 0 to 1) (default 1)
        :param float timeclamp: set timeclamp (from 0.002 to 1) (default 0.17)
        :param float attack: set attack time (from 0 to 1) (default 0)
        :param float basefreq: set base frequency (from 10 to 100000) (default 20.0152)
        :param float endfreq: set end frequency (from 10 to 100000) (default 20495.6)
        :param float coeffclamp: set coeffclamp (from 0.1 to 10) (default 1)
        :param str tlength: set tlength (default "384*tc/(384+tc*f)")
        :param int count: set transform count (from 1 to 30) (default 6)
        :param int fcount: set frequency count (from 0 to 10) (default 0)
        :param str fontfile: set axis font file
        :param str font: set axis font
        :param str fontcolor: set font color (default "st(0, (midi(f)-59.5)/12);st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));r(1-ld(1)) + b(ld(1))")
        :param str axisfile: set axis image
        :param bool axis: draw axis (default true)
        :param int csp: set color space (from 0 to INT_MAX) (default unspecified)
        :param str cscheme: set color scheme (default "1|0.5|0|0|0.5|1")

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
        size: str | float | int = Default("640x512"),
        rate: str | float | int = Default("25"),
        scale: int | Literal["linear", "log2", "bark", "mel", "erbs"] | Default = Default("linear"),
        min: float | int | str = Default("20"),
        max: float | int | str = Default("20000"),
        logb: float | int | str = Default("0.0001"),
        deviation: float | int | str = Default("1"),
        pps: int | str = Default("64"),
        mode: int | Literal["magnitude", "phase", "magphase", "channel", "stereo"] | Default = Default("magnitude"),
        slide: int | Literal["replace", "scroll", "frame"] | Default = Default("replace"),
        direction: int | Literal["lr", "rl", "ud", "du"] | Default = Default("lr"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output.

        Parameters:
        ----------

        :param str size: set video size (default "640x512")
        :param str rate: set video rate (default "25")
        :param int scale: set frequency scale (from 0 to 4) (default linear)
        :param float min: set minimum frequency (from 1 to 2000) (default 20)
        :param float max: set maximum frequency (from 0 to 192000) (default 20000)
        :param float logb: set logarithmic basis (from 0 to 1) (default 0.0001)
        :param float deviation: set frequency deviation (from 0 to 10) (default 1)
        :param int pps: set pixels per second (from 1 to 1024) (default 64)
        :param int mode: set output mode (from 0 to 4) (default magnitude)
        :param int slide: set slide mode (from 0 to 2) (default replace)
        :param int direction: set direction mode (from 0 to 3) (default lr)

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
        size: str | float | int = Default("1024x512"),
        rate: str | float | int = Default("25"),
        mode: int | Literal["line", "bar", "dot"] | Default = Default("bar"),
        ascale: int | Literal["lin", "sqrt", "cbrt", "log"] | Default = Default("log"),
        fscale: int | Literal["lin", "log", "rlog"] | Default = Default("lin"),
        win_size: int | str = Default("2048"),
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
        | Default = Default("hann"),
        overlap: float | int | str = Default("1"),
        averaging: int | str = Default("1"),
        colors: str | float | int = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        cmode: int | Literal["combined", "separate"] | Default = Default("combined"),
        minamp: float | int | str = Default("1e-06"),
        data: int | Literal["magnitude", "phase", "delay"] | Default = Default("magnitude"),
        channels: str | float | int = Default("all"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a frequencies video output.

        Parameters:
        ----------

        :param str size: set video size (default "1024x512")
        :param str rate: set video rate (default "25")
        :param int mode: set display mode (from 0 to 2) (default bar)
        :param int ascale: set amplitude scale (from 0 to 3) (default log)
        :param int fscale: set frequency scale (from 0 to 2) (default lin)
        :param int win_size: set window size (from 16 to 65536) (default 2048)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param float overlap: set window overlap (from 0 to 1) (default 1)
        :param int averaging: set time averaging (from 0 to INT_MAX) (default 1)
        :param str colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param int cmode: set channel mode (from 0 to 1) (default combined)
        :param float minamp: set minimum amplitude (from FLT_MIN to 1e-06) (default 1e-06)
        :param int data: set data mode (from 0 to 2) (default magnitude)
        :param str channels: set channels to draw (default "all")

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
        size: str | float | int = Default("512x512"),
        win_size: int | str = Default("4096"),
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
        | Default = Default("hann"),
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spatial video output.

        Parameters:
        ----------

        :param str size: set video size (default "512x512")
        :param int win_size: set window size (from 1024 to 65536) (default 4096)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param str rate: set video rate (default "25")

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
        size: str | float | int = Default("640x512"),
        slide: int | Literal["replace", "scroll", "fullframe", "rscroll", "lreplace"] | Default = Default("replace"),
        mode: int | Literal["combined", "separate"] | Default = Default("combined"),
        color: int
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
        scale: int | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | Default = Default("sqrt"),
        fscale: int | Literal["lin", "log"] | Default = Default("lin"),
        saturation: float | int | str = Default("1"),
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
        | Default = Default("hann"),
        orientation: int | Literal["vertical", "horizontal"] | Default = Default("vertical"),
        overlap: float | int | str = Default("0"),
        gain: float | int | str = Default("1"),
        data: int | Literal["magnitude", "phase", "uphase"] | Default = Default("magnitude"),
        rotation: float | int | str = Default("0"),
        start: int | str = Default("0"),
        stop: int | str = Default("0"),
        fps: str | float | int = Default("auto"),
        legend: bool | int | str = Default("false"),
        drange: float | int | str = Default("120"),
        limit: float | int | str = Default("0"),
        opacity: float | int | str = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spectrum video output.

        Parameters:
        ----------

        :param str size: set video size (default "640x512")
        :param int slide: set sliding mode (from 0 to 4) (default replace)
        :param int mode: set channel display mode (from 0 to 1) (default combined)
        :param int color: set channel coloring (from 0 to 14) (default channel)
        :param int scale: set display scale (from 0 to 5) (default sqrt)
        :param int fscale: set frequency scale (from 0 to 1) (default lin)
        :param float saturation: color saturation multiplier (from -10 to 10) (default 1)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param int orientation: set orientation (from 0 to 1) (default vertical)
        :param float overlap: set window overlap (from 0 to 1) (default 0)
        :param float gain: set scale gain (from 0 to 128) (default 1)
        :param int data: set data mode (from 0 to 2) (default magnitude)
        :param float rotation: color rotation (from -1 to 1) (default 0)
        :param int start: start frequency (from 0 to INT_MAX) (default 0)
        :param int stop: stop frequency (from 0 to INT_MAX) (default 0)
        :param str fps: set video rate (default "auto")
        :param bool legend: draw legend (default false)
        :param float drange: set dynamic range in dBFS (from 10 to 200) (default 120)
        :param float limit: set upper limit in dBFS (from -100 to 100) (default 0)
        :param float opacity: set opacity strength (from 0 to 10) (default 1)

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
        size: str | float | int = Default("4096x2048"),
        mode: int | Literal["combined", "separate"] | Default = Default("combined"),
        color: int
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
        scale: int | Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | Default = Default("log"),
        fscale: int | Literal["lin", "log"] | Default = Default("lin"),
        saturation: float | int | str = Default("1"),
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
        | Default = Default("hann"),
        orientation: int | Literal["vertical", "horizontal"] | Default = Default("vertical"),
        gain: float | int | str = Default("1"),
        legend: bool | int | str = Default("true"),
        rotation: float | int | str = Default("0"),
        start: int | str = Default("0"),
        stop: int | str = Default("0"),
        drange: float | int | str = Default("120"),
        limit: float | int | str = Default("0"),
        opacity: float | int | str = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a spectrum video output single picture.

        Parameters:
        ----------

        :param str size: set video size (default "4096x2048")
        :param int mode: set channel display mode (from 0 to 1) (default combined)
        :param int color: set channel coloring (from 0 to 14) (default intensity)
        :param int scale: set display scale (from 0 to 5) (default log)
        :param int fscale: set frequency scale (from 0 to 1) (default lin)
        :param float saturation: color saturation multiplier (from -10 to 10) (default 1)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param int orientation: set orientation (from 0 to 1) (default vertical)
        :param float gain: set scale gain (from 0 to 128) (default 1)
        :param bool legend: draw legend (default true)
        :param float rotation: color rotation (from -1 to 1) (default 0)
        :param int start: start frequency (from 0 to INT_MAX) (default 0)
        :param int stop: stop frequency (from 0 to INT_MAX) (default 0)
        :param float drange: set dynamic range in dBFS (from 10 to 200) (default 120)
        :param float limit: set upper limit in dBFS (from -100 to 100) (default 0)
        :param float opacity: set opacity strength (from 0 to 10) (default 1)

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
        rate: str | float | int = Default("25"),
        b: int | str = Default("1"),
        w: int | str = Default("400"),
        h: int | str = Default("20"),
        f: float | int | str = Default("0.95"),
        c: str | float | int = Default("PEAK*255+floor((1-PEAK"),
        t: bool | int | str = Default("true"),
        v: bool | int | str = Default("true"),
        dm: float | int | str = Default("0"),
        dmc: str | float | int = Default("orange"),
        o: int | Literal["h", "v"] | Default = Default("h"),
        s: int | str = Default("0"),
        p: float | int | str = Default("0"),
        m: int | Literal["p", "r"] | Default = Default("p"),
        ds: int | Literal["lin", "log"] | Default = Default("lin"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio volume to video output.

        Parameters:
        ----------

        :param str rate: set video rate (default "25")
        :param int b: set border width (from 0 to 5) (default 1)
        :param int w: set channel width (from 80 to 8192) (default 400)
        :param int h: set channel height (from 1 to 900) (default 20)
        :param float f: set fade (from 0 to 1) (default 0.95)
        :param str c: set volume color expression (default "PEAK*255+floor((1-PEAK)*255)*256+0xff000000")
        :param bool t: display channel names (default true)
        :param bool v: display volume value (default true)
        :param float dm: duration for max value display (from 0 to 9000) (default 0)
        :param str dmc: set color of the max value line (default "orange")
        :param int o: set orientation (from 0 to 1) (default h)
        :param int s: set step size (from 0 to 5) (default 0)
        :param float p: set background opacity (from 0 to 1) (default 0)
        :param int m: set mode (from 0 to 1) (default p)
        :param int ds: set display scale (from 0 to 1) (default lin)

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
        size: str | float | int = Default("600x240"),
        mode: int | Literal["point", "line", "p2p", "cline"] | Default = Default("point"),
        n: int | str = Default("0"),
        rate: str | float | int = Default("25"),
        split_channels: bool | int | str = Default("false"),
        colors: str | float | int = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: int | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: int | Literal["scale", "full"] | Default = Default("scale"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a video output.

        Parameters:
        ----------

        :param str size: set video size (default "600x240")
        :param int mode: select display mode (from 0 to 3) (default point)
        :param int n: set how many samples to show in the same point (from 0 to INT_MAX) (default 0)
        :param str rate: set video rate (default "25")
        :param bool split_channels: draw channels separately (default false)
        :param str colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param int scale: set amplitude scale (from 0 to 3) (default lin)
        :param int draw: set draw mode (from 0 to 1) (default scale)

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
        size: str | float | int = Default("600x240"),
        split_channels: bool | int | str = Default("false"),
        colors: str | float | int = Default("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: int | Literal["lin", "log", "sqrt", "cbrt"] | Default = Default("lin"),
        draw: int | Literal["scale", "full"] | Default = Default("scale"),
        filter: int | Literal["average", "peak"] | Default = Default("average"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert input audio to a video output single picture.

        Parameters:
        ----------

        :param str size: set video size (default "600x240")
        :param bool split_channels: draw channels separately (default false)
        :param str colors: set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
        :param int scale: set amplitude scale (from 0 to 3) (default lin)
        :param int draw: set draw mode (from 0 to 1) (default scale)
        :param int filter: set filter mode (from 0 to 1) (default average)

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
        **kwargs: Any,
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
        **kwargs: Any,
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
        n: float | int | str = Default("0.001"),
        d: str | float | int = Default("2"),
        mono: bool | int | str = Default("false"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Detect silence.

        Parameters:
        ----------

        :param float n: set noise tolerance (from 0 to DBL_MAX) (default 0.001)
        :param str d: set minimum duration in seconds (default 2)
        :param bool mono: check each channel separately (default false)

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
        start_periods: int | str = Default("0"),
        start_duration: str | float | int = Default("0"),
        start_threshold: float | int | str = Default("0"),
        start_silence: str | float | int = Default("0"),
        start_mode: int | Literal["any", "all"] | Default = Default("any"),
        stop_periods: int | str = Default("0"),
        stop_duration: str | float | int = Default("0"),
        stop_threshold: float | int | str = Default("0"),
        stop_silence: str | float | int = Default("0"),
        stop_mode: int | Literal["any", "all"] | Default = Default("any"),
        detection: int | Literal["peak", "rms"] | Default = Default("rms"),
        window: str | float | int = Default("0.02"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Remove silence.

        Parameters:
        ----------

        :param int start_periods: set periods of silence parts to skip from start (from 0 to 9000) (default 0)
        :param str start_duration: set start duration of non-silence part (default 0)
        :param float start_threshold: set threshold for start silence detection (from 0 to DBL_MAX) (default 0)
        :param str start_silence: set start duration of silence part to keep (default 0)
        :param int start_mode: set which channel will trigger trimming from start (from 0 to 1) (default any)
        :param int stop_periods: set periods of silence parts to skip from end (from -9000 to 9000) (default 0)
        :param str stop_duration: set stop duration of non-silence part (default 0)
        :param float stop_threshold: set threshold for stop silence detection (from 0 to DBL_MAX) (default 0)
        :param str stop_silence: set stop duration of silence part to keep (default 0)
        :param int stop_mode: set which channel will trigger trimming from end (from 0 to 1) (default any)
        :param int detection: set how silence is detected (from 0 to 1) (default rms)
        :param str window: set duration of window for silence detection (default 0.02)

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
        peak: float | int | str = Default("0.95"),
        expansion: float | int | str = Default("2"),
        compression: float | int | str = Default("2"),
        threshold: float | int | str = Default("0"),
        _raise: float | int | str = Default("0.001"),
        fall: float | int | str = Default("0.001"),
        channels: str | float | int = Default("all"),
        invert: bool | int | str = Default("false"),
        link: bool | int | str = Default("false"),
        rms: float | int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Speech Normalizer.

        Parameters:
        ----------

        :param float peak: set the peak value (from 0 to 1) (default 0.95)
        :param float expansion: set the max expansion factor (from 1 to 50) (default 2)
        :param float compression: set the max compression factor (from 1 to 50) (default 2)
        :param float threshold: set the threshold value (from 0 to 1) (default 0)
        :param float _raise: set the expansion raising amount (from 0 to 1) (default 0.001)
        :param float fall: set the compression raising amount (from 0 to 1) (default 0.001)
        :param str channels: set channels to filter (default "all")
        :param bool invert: set inverted filtering (default false)
        :param bool link: set linked channels filtering (default false)
        :param float rms: set the RMS value (from 0 to 1) (default 0)
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
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        balance_in: float | int | str = Default("0"),
        balance_out: float | int | str = Default("0"),
        softclip: bool | int | str = Default("false"),
        mutel: bool | int | str = Default("false"),
        muter: bool | int | str = Default("false"),
        phasel: bool | int | str = Default("false"),
        phaser: bool | int | str = Default("false"),
        mode: int
        | Literal["lr", "ms", "lr", "ll", "rr", "r", "rl", "ll", "rr", "rl", "r"]
        | Default = Default("lr>lr"),
        slev: float | int | str = Default("1"),
        sbal: float | int | str = Default("0"),
        mlev: float | int | str = Default("1"),
        mpan: float | int | str = Default("0"),
        base: float | int | str = Default("0"),
        delay: float | int | str = Default("0"),
        sclevel: float | int | str = Default("1"),
        phase: float | int | str = Default("0"),
        bmode_in: int | Literal["balance", "amplitude", "power"] | Default = Default("balance"),
        bmode_out: int | Literal["balance", "amplitude", "power"] | Default = Default("balance"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply various stereo tools.

        Parameters:
        ----------

        :param float level_in: set level in (from 0.015625 to 64) (default 1)
        :param float level_out: set level out (from 0.015625 to 64) (default 1)
        :param float balance_in: set balance in (from -1 to 1) (default 0)
        :param float balance_out: set balance out (from -1 to 1) (default 0)
        :param bool softclip: enable softclip (default false)
        :param bool mutel: mute L (default false)
        :param bool muter: mute R (default false)
        :param bool phasel: phase L (default false)
        :param bool phaser: phase R (default false)
        :param int mode: set stereo mode (from 0 to 10) (default lr>lr)
        :param float slev: set side level (from 0.015625 to 64) (default 1)
        :param float sbal: set side balance (from -1 to 1) (default 0)
        :param float mlev: set middle level (from 0.015625 to 64) (default 1)
        :param float mpan: set middle pan (from -1 to 1) (default 0)
        :param float base: set stereo base (from -1 to 1) (default 0)
        :param float delay: set delay (from -20 to 20) (default 0)
        :param float sclevel: set S/C level (from 1 to 100) (default 1)
        :param float phase: set stereo phase (from 0 to 360) (default 0)
        :param int bmode_in: set balance in mode (from 0 to 2) (default balance)
        :param int bmode_out: set balance out mode (from 0 to 2) (default balance)
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
        delay: float | int | str = Default("20"),
        feedback: float | int | str = Default("0.3"),
        crossfeed: float | int | str = Default("0.3"),
        drymix: float | int | str = Default("0.8"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply stereo widening effect.

        Parameters:
        ----------

        :param float delay: set delay time (from 1 to 100) (default 20)
        :param float feedback: set feedback gain (from 0 to 0.9) (default 0.3)
        :param float crossfeed: set cross feed (from 0 to 0.8) (default 0.3)
        :param float drymix: set dry-mix (from 0 to 1) (default 0.8)
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
        _1b: float | int | str = Default("1"),
        _2b: float | int | str = Default("1"),
        _3b: float | int | str = Default("1"),
        _4b: float | int | str = Default("1"),
        _5b: float | int | str = Default("1"),
        _6b: float | int | str = Default("1"),
        _7b: float | int | str = Default("1"),
        _8b: float | int | str = Default("1"),
        _9b: float | int | str = Default("1"),
        _10b: float | int | str = Default("1"),
        _11b: float | int | str = Default("1"),
        _12b: float | int | str = Default("1"),
        _13b: float | int | str = Default("1"),
        _14b: float | int | str = Default("1"),
        _15b: float | int | str = Default("1"),
        _16b: float | int | str = Default("1"),
        _17b: float | int | str = Default("1"),
        _18b: float | int | str = Default("1"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply 18 band equalization filter.

        Parameters:
        ----------

        :param float _1b: set 65Hz band gain (from 0 to 20) (default 1)
        :param float _2b: set 92Hz band gain (from 0 to 20) (default 1)
        :param float _3b: set 131Hz band gain (from 0 to 20) (default 1)
        :param float _4b: set 185Hz band gain (from 0 to 20) (default 1)
        :param float _5b: set 262Hz band gain (from 0 to 20) (default 1)
        :param float _6b: set 370Hz band gain (from 0 to 20) (default 1)
        :param float _7b: set 523Hz band gain (from 0 to 20) (default 1)
        :param float _8b: set 740Hz band gain (from 0 to 20) (default 1)
        :param float _9b: set 1047Hz band gain (from 0 to 20) (default 1)
        :param float _10b: set 1480Hz band gain (from 0 to 20) (default 1)
        :param float _11b: set 2093Hz band gain (from 0 to 20) (default 1)
        :param float _12b: set 2960Hz band gain (from 0 to 20) (default 1)
        :param float _13b: set 4186Hz band gain (from 0 to 20) (default 1)
        :param float _14b: set 5920Hz band gain (from 0 to 20) (default 1)
        :param float _15b: set 8372Hz band gain (from 0 to 20) (default 1)
        :param float _16b: set 11840Hz band gain (from 0 to 20) (default 1)
        :param float _17b: set 16744Hz band gain (from 0 to 20) (default 1)
        :param float _18b: set 20000Hz band gain (from 0 to 20) (default 1)

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
        chl_out: str | float | int = Default("5.1"),
        chl_in: str | float | int = Default("stereo"),
        level_in: float | int | str = Default("1"),
        level_out: float | int | str = Default("1"),
        lfe: bool | int | str = Default("true"),
        lfe_low: int | str = Default("128"),
        lfe_high: int | str = Default("256"),
        lfe_mode: int | Literal["add", "sub"] | Default = Default("add"),
        smooth: float | int | str = Default("0"),
        angle: float | int | str = Default("90"),
        focus: float | int | str = Default("0"),
        fc_in: float | int | str = Default("1"),
        fc_out: float | int | str = Default("1"),
        fl_in: float | int | str = Default("1"),
        fl_out: float | int | str = Default("1"),
        fr_in: float | int | str = Default("1"),
        fr_out: float | int | str = Default("1"),
        sl_in: float | int | str = Default("1"),
        sl_out: float | int | str = Default("1"),
        sr_in: float | int | str = Default("1"),
        sr_out: float | int | str = Default("1"),
        bl_in: float | int | str = Default("1"),
        bl_out: float | int | str = Default("1"),
        br_in: float | int | str = Default("1"),
        br_out: float | int | str = Default("1"),
        bc_in: float | int | str = Default("1"),
        bc_out: float | int | str = Default("1"),
        lfe_in: float | int | str = Default("1"),
        lfe_out: float | int | str = Default("1"),
        allx: float | int | str = Default("-1"),
        ally: float | int | str = Default("-1"),
        fcx: float | int | str = Default("0.5"),
        flx: float | int | str = Default("0.5"),
        frx: float | int | str = Default("0.5"),
        blx: float | int | str = Default("0.5"),
        brx: float | int | str = Default("0.5"),
        slx: float | int | str = Default("0.5"),
        srx: float | int | str = Default("0.5"),
        bcx: float | int | str = Default("0.5"),
        fcy: float | int | str = Default("0.5"),
        fly: float | int | str = Default("0.5"),
        fry: float | int | str = Default("0.5"),
        bly: float | int | str = Default("0.5"),
        bry: float | int | str = Default("0.5"),
        sly: float | int | str = Default("0.5"),
        sry: float | int | str = Default("0.5"),
        bcy: float | int | str = Default("0.5"),
        win_size: int | str = Default("4096"),
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
        | Default = Default("hann"),
        overlap: float | int | str = Default("0.5"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply audio surround upmix filter.

        Parameters:
        ----------

        :param str chl_out: set output channel layout (default "5.1")
        :param str chl_in: set input channel layout (default "stereo")
        :param float level_in: set input level (from 0 to 10) (default 1)
        :param float level_out: set output level (from 0 to 10) (default 1)
        :param bool lfe: output LFE (default true)
        :param int lfe_low: LFE low cut off (from 0 to 256) (default 128)
        :param int lfe_high: LFE high cut off (from 0 to 512) (default 256)
        :param int lfe_mode: set LFE channel mode (from 0 to 1) (default add)
        :param float smooth: set temporal smoothness strength (from 0 to 1) (default 0)
        :param float angle: set soundfield transform angle (from 0 to 360) (default 90)
        :param float focus: set soundfield transform focus (from -1 to 1) (default 0)
        :param float fc_in: set front center channel input level (from 0 to 10) (default 1)
        :param float fc_out: set front center channel output level (from 0 to 10) (default 1)
        :param float fl_in: set front left channel input level (from 0 to 10) (default 1)
        :param float fl_out: set front left channel output level (from 0 to 10) (default 1)
        :param float fr_in: set front right channel input level (from 0 to 10) (default 1)
        :param float fr_out: set front right channel output level (from 0 to 10) (default 1)
        :param float sl_in: set side left channel input level (from 0 to 10) (default 1)
        :param float sl_out: set side left channel output level (from 0 to 10) (default 1)
        :param float sr_in: set side right channel input level (from 0 to 10) (default 1)
        :param float sr_out: set side right channel output level (from 0 to 10) (default 1)
        :param float bl_in: set back left channel input level (from 0 to 10) (default 1)
        :param float bl_out: set back left channel output level (from 0 to 10) (default 1)
        :param float br_in: set back right channel input level (from 0 to 10) (default 1)
        :param float br_out: set back right channel output level (from 0 to 10) (default 1)
        :param float bc_in: set back center channel input level (from 0 to 10) (default 1)
        :param float bc_out: set back center channel output level (from 0 to 10) (default 1)
        :param float lfe_in: set lfe channel input level (from 0 to 10) (default 1)
        :param float lfe_out: set lfe channel output level (from 0 to 10) (default 1)
        :param float allx: set all channel's x spread (from -1 to 15) (default -1)
        :param float ally: set all channel's y spread (from -1 to 15) (default -1)
        :param float fcx: set front center channel x spread (from 0.06 to 15) (default 0.5)
        :param float flx: set front left channel x spread (from 0.06 to 15) (default 0.5)
        :param float frx: set front right channel x spread (from 0.06 to 15) (default 0.5)
        :param float blx: set back left channel x spread (from 0.06 to 15) (default 0.5)
        :param float brx: set back right channel x spread (from 0.06 to 15) (default 0.5)
        :param float slx: set side left channel x spread (from 0.06 to 15) (default 0.5)
        :param float srx: set side right channel x spread (from 0.06 to 15) (default 0.5)
        :param float bcx: set back center channel x spread (from 0.06 to 15) (default 0.5)
        :param float fcy: set front center channel y spread (from 0.06 to 15) (default 0.5)
        :param float fly: set front left channel y spread (from 0.06 to 15) (default 0.5)
        :param float fry: set front right channel y spread (from 0.06 to 15) (default 0.5)
        :param float bly: set back left channel y spread (from 0.06 to 15) (default 0.5)
        :param float bry: set back right channel y spread (from 0.06 to 15) (default 0.5)
        :param float sly: set side left channel y spread (from 0.06 to 15) (default 0.5)
        :param float sry: set side right channel y spread (from 0.06 to 15) (default 0.5)
        :param float bcy: set back center channel y spread (from 0.06 to 15) (default 0.5)
        :param int win_size: set window size (from 1024 to 65536) (default 4096)
        :param int win_func: set window function (from 0 to 20) (default hann)
        :param float overlap: set window overlap (from 0 to 1) (default 0.5)

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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        gain: float | int | str = Default("0"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply a tilt shelf filter.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        frequency: float | int | str = Default("3000"),
        width_type: int | Literal["h", "q", "o", "s", "k"] | Default = Default("q"),
        width: float | int | str = Default("0.5"),
        gain: float | int | str = Default("0"),
        poles: int | str = Default("2"),
        mix: float | int | str = Default("1"),
        channels: str | float | int = Default("all"),
        normalize: bool | int | str = Default("false"),
        transform: int | Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | Default = Default("di"),
        precision: int | Literal["auto", "s16", "s32", "f32", "f64"] | Default = Default("auto"),
        blocksize: int | str = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Boost or cut upper frequencies.

        Parameters:
        ----------

        :param float frequency: set central frequency (from 0 to 999999) (default 3000)
        :param int width_type: set filter-width type (from 1 to 5) (default q)
        :param float width: set width (from 0 to 99999) (default 0.5)
        :param float gain: set gain (from -900 to 900) (default 0)
        :param int poles: set number of poles (from 1 to 2) (default 2)
        :param float mix: set mix (from 0 to 1) (default 1)
        :param str channels: set channels to filter (default "all")
        :param bool normalize: normalize coefficients (default false)
        :param int transform: set transform type (from 0 to 6) (default di)
        :param int precision: set filtering precision (from -1 to 3) (default auto)
        :param int blocksize: set the block size (from 0 to 32768) (default 0)
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
        self,
        *,
        f: float | int | str = Default("5"),
        d: float | int | str = Default("0.5"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply tremolo effect.

        Parameters:
        ----------

        :param float f: set frequency in hertz (from 0.1 to 20000) (default 5)
        :param float d: set depth as percentage (from 0 to 1) (default 0.5)
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
        self,
        *,
        f: float | int | str = Default("5"),
        d: float | int | str = Default("0.5"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Apply vibrato effect.

        Parameters:
        ----------

        :param float f: set frequency in hertz (from 0.1 to 20000) (default 5)
        :param float d: set depth as percentage (from 0 to 1) (default 0.5)
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
        cutoff: float | int | str = Default("250"),
        strength: float | int | str = Default("3"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Audio Virtual Bass.

        Parameters:
        ----------

        :param float cutoff: set virtual bass cutoff (from 100 to 500) (default 250)
        :param float strength: set virtual bass strength (from 0.5 to 3) (default 3)
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
        volume: str | float | int = Default("1.0"),
        precision: int | Literal["fixed", "float", "double"] | Default = Default("float"),
        eval: int | Literal["once", "frame"] | Default = Default("once"),
        replaygain: int | Literal["drop", "ignore", "track", "album"] | Default = Default("drop"),
        replaygain_preamp: float | int | str = Default("0"),
        replaygain_noclip: bool | int | str = Default("true"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Change input volume.

        Parameters:
        ----------

        :param str volume: set volume adjustment expression (default "1.0")
        :param int precision: select mathematical precision (from 0 to 2) (default float)
        :param int eval: specify when to evaluate expressions (from 0 to 1) (default once)
        :param int replaygain: Apply replaygain side data when present (from 0 to 3) (default drop)
        :param float replaygain_preamp: Apply replaygain pre-amplification (from -15 to 15) (default 0)
        :param bool replaygain_noclip: Apply replaygain clipping prevention (default true)
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
