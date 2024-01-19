from __future__ import annotations

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
    RATIONAL,
    STRING,
    VIDEO_RATE,
    Default,
    StreamType,
)

if TYPE_CHECKING:
    from .audio import AudioStream


class VideoStream(FilterableStream):
    @property
    def video(self) -> "VideoStream":
        return VideoStream(node=self.node, index=self.index, selector=StreamType.video)

    @property
    def audio(self) -> "AudioStream":
        raise NotImplementedError("Cannot convert video to audio")

    def addroi(
        self,
        *,
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        w: STRING = Default("0"),
        h: STRING = Default("0"),
        qoffset: RATIONAL = Default("-1/10"),
        clear: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add region of interest to frame.

        Parameters:
        ----------

        :param STRING x: Region distance from left edge of frame. (default "0")
        :param STRING y: Region distance from top edge of frame. (default "0")
        :param STRING w: Region width. (default "0")
        :param STRING h: Region height. (default "0")
        :param RATIONAL qoffset: Quantisation offset to apply in the region. (from -1 to 1) (default -1/10)
        :param BOOLEAN clear: Remove any existing regions of interest before adding the new one. (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#addroi

        """
        filter_node = FilterNode(
            name="addroi",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h,
                        "qoffset": qoffset,
                        "clear": clear,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def alphaextract(self, **kwargs: Any) -> "VideoStream":
        """

        Extract an alpha channel as a grayscale image component.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#alphaextract

        """
        filter_node = FilterNode(
            name="alphaextract",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def alphamerge(
        self,
        _alpha: "VideoStream",
        *,
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def amplify(
        self,
        *,
        radius: INT = Default("2"),
        factor: FLOAT = Default("2"),
        threshold: FLOAT = Default("10"),
        tolerance: FLOAT = Default("0"),
        low: FLOAT = Default("65535"),
        high: FLOAT = Default("65535"),
        planes: FLAGS = Default("7"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Amplify changes between successive video frames.

        Parameters:
        ----------

        :param INT radius: set radius (from 1 to 63) (default 2)
        :param FLOAT factor: set factor (from 0 to 65535) (default 2)
        :param FLOAT threshold: set threshold (from 0 to 65535) (default 10)
        :param FLOAT tolerance: set tolerance (from 0 to 65535) (default 0)
        :param FLOAT low: set low limit for amplification (from 0 to 65535) (default 65535)
        :param FLOAT high: set high limit for amplification (from 0 to 65535) (default 65535)
        :param FLAGS planes: set what planes to filter (default 7)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amplify

        """
        filter_node = FilterNode(
            name="amplify",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "radius": radius,
                        "factor": factor,
                        "threshold": threshold,
                        "tolerance": tolerance,
                        "low": low,
                        "high": high,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def ass(
        self,
        *,
        filename: STRING = Default(None),
        original_size: IMAGE_SIZE = Default(None),
        fontsdir: STRING = Default(None),
        alpha: BOOLEAN = Default("false"),
        shaping: INT | Literal["auto", "simple", "complex"] | Default = Default("auto"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render ASS subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param STRING filename: set the filename of file to read
        :param IMAGE_SIZE original_size: set the size of the original video (used to scale fonts)
        :param STRING fontsdir: set the directory containing the fonts to read
        :param BOOLEAN alpha: enable processing of alpha channel (default false)
        :param INT shaping: set shaping engine (from -1 to 1) (default auto)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ass

        """
        filter_node = FilterNode(
            name="ass",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filename": filename,
                        "original_size": original_size,
                        "fontsdir": fontsdir,
                        "alpha": alpha,
                        "shaping": shaping,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def atadenoise(
        self,
        *,
        _0a: FLOAT = Default("0.02"),
        _0b: FLOAT = Default("0.04"),
        _1a: FLOAT = Default("0.02"),
        _1b: FLOAT = Default("0.04"),
        _2a: FLOAT = Default("0.02"),
        _2b: FLOAT = Default("0.04"),
        s: INT = Default("9"),
        p: FLAGS = Default("7"),
        a: INT | Literal["p", "s"] | Default = Default("p"),
        _0s: FLOAT = Default("32767"),
        _1s: FLOAT = Default("32767"),
        _2s: FLOAT = Default("32767"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an Adaptive Temporal Averaging Denoiser.

        Parameters:
        ----------

        :param FLOAT _0a: set threshold A for 1st plane (from 0 to 0.3) (default 0.02)
        :param FLOAT _0b: set threshold B for 1st plane (from 0 to 5) (default 0.04)
        :param FLOAT _1a: set threshold A for 2nd plane (from 0 to 0.3) (default 0.02)
        :param FLOAT _1b: set threshold B for 2nd plane (from 0 to 5) (default 0.04)
        :param FLOAT _2a: set threshold A for 3rd plane (from 0 to 0.3) (default 0.02)
        :param FLOAT _2b: set threshold B for 3rd plane (from 0 to 5) (default 0.04)
        :param INT s: set how many frames to use (from 5 to 129) (default 9)
        :param FLAGS p: set what planes to filter (default 7)
        :param INT a: set variant of algorithm (from 0 to 1) (default p)
        :param FLOAT _0s: set sigma for 1st plane (from 0 to 32767) (default 32767)
        :param FLOAT _1s: set sigma for 2nd plane (from 0 to 32767) (default 32767)
        :param FLOAT _2s: set sigma for 3rd plane (from 0 to 32767) (default 32767)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atadenoise

        """
        filter_node = FilterNode(
            name="atadenoise",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "0a": _0a,
                        "0b": _0b,
                        "1a": _1a,
                        "1b": _1b,
                        "2a": _2a,
                        "2b": _2b,
                        "s": s,
                        "p": p,
                        "a": a,
                        "0s": _0s,
                        "1s": _1s,
                        "2s": _2s,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def avgblur(
        self,
        *,
        sizeX: INT = Default("1"),
        planes: INT = Default("15"),
        sizeY: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Average Blur filter.

        Parameters:
        ----------

        :param INT sizeX: set horizontal size (from 1 to 1024) (default 1)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param INT sizeY: set vertical size (from 0 to 1024) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur

        """
        filter_node = FilterNode(
            name="avgblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sizeX": sizeX,
                        "planes": planes,
                        "sizeY": sizeY,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def backgroundkey(
        self,
        *,
        threshold: FLOAT = Default("0.08"),
        similarity: FLOAT = Default("0.1"),
        blend: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a static background into transparency.

        Parameters:
        ----------

        :param FLOAT threshold: set the scene change threshold (from 0 to 1) (default 0.08)
        :param FLOAT similarity: set the similarity (from 0 to 1) (default 0.1)
        :param FLOAT blend: set the blend value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#backgroundkey

        """
        filter_node = FilterNode(
            name="backgroundkey",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold": threshold,
                        "similarity": similarity,
                        "blend": blend,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bbox(self, *, min_val: INT = Default("16"), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Compute bounding box for each frame.

        Parameters:
        ----------

        :param INT min_val: set minimum luminance value for bounding box (from 0 to 65535) (default 16)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bbox

        """
        filter_node = FilterNode(
            name="bbox",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "min_val": min_val,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bench(
        self, *, action: INT | Literal["start", "stop"] | Default = Default("start"), **kwargs: Any
    ) -> "VideoStream":
        """

        Benchmark part of a filtergraph.

        Parameters:
        ----------

        :param INT action: set action (from 0 to 1) (default start)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench

        """
        filter_node = FilterNode(
            name="bench",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def bilateral(
        self,
        *,
        sigmaS: FLOAT = Default("0.1"),
        sigmaR: FLOAT = Default("0.1"),
        planes: INT = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Bilateral filter.

        Parameters:
        ----------

        :param FLOAT sigmaS: set spatial sigma (from 0 to 512) (default 0.1)
        :param FLOAT sigmaR: set range sigma (from 0 to 1) (default 0.1)
        :param INT planes: set planes to filter (from 0 to 15) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral

        """
        filter_node = FilterNode(
            name="bilateral",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigmaS": sigmaS,
                        "sigmaR": sigmaR,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bitplanenoise(
        self,
        *,
        bitplane: INT = Default("1"),
        filter: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure bit plane noise.

        Parameters:
        ----------

        :param INT bitplane: set bit plane to use for measuring noise (from 1 to 16) (default 1)
        :param BOOLEAN filter: show noisy pixels (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bitplanenoise

        """
        filter_node = FilterNode(
            name="bitplanenoise",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "bitplane": bitplane,
                        "filter": filter,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def blackdetect(
        self,
        *,
        d: DOUBLE = Default("2"),
        picture_black_ratio_th: DOUBLE = Default("0.98"),
        pixel_black_th: DOUBLE = Default("0.1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect video intervals that are (almost) black.

        Parameters:
        ----------

        :param DOUBLE d: set minimum detected black duration in seconds (from 0 to DBL_MAX) (default 2)
        :param DOUBLE picture_black_ratio_th: set the picture black ratio threshold (from 0 to 1) (default 0.98)
        :param DOUBLE pixel_black_th: set the pixel black threshold (from 0 to 1) (default 0.1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackdetect

        """
        filter_node = FilterNode(
            name="blackdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "d": d,
                        "picture_black_ratio_th": picture_black_ratio_th,
                        "pixel_black_th": pixel_black_th,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def blackframe(
        self, *, amount: INT = Default("98"), threshold: INT = Default("32"), **kwargs: Any
    ) -> "VideoStream":
        """

        Detect frames that are (almost) black.

        Parameters:
        ----------

        :param INT amount: percentage of the pixels that have to be below the threshold for the frame to be considered black (from 0 to 100) (default 98)
        :param INT threshold: threshold below which a pixel value is considered black (from 0 to 255) (default 32)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackframe

        """
        filter_node = FilterNode(
            name="blackframe",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "amount": amount,
                        "threshold": threshold,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def blend(
        self,
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
        **kwargs: Any,
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
                self,
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

    def blockdetect(
        self,
        *,
        period_min: INT = Default("3"),
        period_max: INT = Default("24"),
        planes: INT = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blockdetect filter.

        Parameters:
        ----------

        :param INT period_min: Minimum period to search for (from 2 to 32) (default 3)
        :param INT period_max: Maximum period to search for (from 2 to 64) (default 24)
        :param INT planes: set planes to filter (from 0 to 15) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blockdetect

        """
        filter_node = FilterNode(
            name="blockdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "period_min": period_min,
                        "period_max": period_max,
                        "planes": planes,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def blurdetect(
        self,
        *,
        high: FLOAT = Default("0.117647"),
        low: FLOAT = Default("0.0588235"),
        radius: INT = Default("50"),
        block_pct: INT = Default("80"),
        block_width: INT = Default("-1"),
        planes: INT = Default("1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blurdetect filter.

        Parameters:
        ----------

        :param FLOAT high: set high threshold (from 0 to 1) (default 0.117647)
        :param FLOAT low: set low threshold (from 0 to 1) (default 0.0588235)
        :param INT radius: search radius for maxima detection (from 1 to 100) (default 50)
        :param INT block_pct: block pooling threshold when calculating blurriness (from 1 to 100) (default 80)
        :param INT block_width: block size for block-based abbreviation of blurriness (from -1 to INT_MAX) (default -1)
        :param INT planes: set planes to filter (from 0 to 15) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blurdetect

        """
        filter_node = FilterNode(
            name="blurdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "high": high,
                        "low": low,
                        "radius": radius,
                        "block_pct": block_pct,
                        "block_width": block_width,
                        "planes": planes,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def boxblur(
        self,
        *,
        luma_radius: STRING = Default("2"),
        luma_power: INT = Default("2"),
        chroma_radius: STRING = Default(None),
        chroma_power: INT = Default("-1"),
        alpha_radius: STRING = Default(None),
        alpha_power: INT = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input.

        Parameters:
        ----------

        :param STRING luma_radius: Radius of the luma blurring box (default "2")
        :param INT luma_power: How many times should the boxblur be applied to luma (from 0 to INT_MAX) (default 2)
        :param STRING chroma_radius: Radius of the chroma blurring box
        :param INT chroma_power: How many times should the boxblur be applied to chroma (from -1 to INT_MAX) (default -1)
        :param STRING alpha_radius: Radius of the alpha blurring box
        :param INT alpha_power: How many times should the boxblur be applied to alpha (from -1 to INT_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#boxblur

        """
        filter_node = FilterNode(
            name="boxblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_radius": luma_radius,
                        "luma_power": luma_power,
                        "chroma_radius": chroma_radius,
                        "chroma_power": chroma_power,
                        "alpha_radius": alpha_radius,
                        "alpha_power": alpha_power,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bwdif(
        self,
        *,
        mode: INT | Literal["send_frame", "send_field"] | Default = Default("send_field"),
        parity: INT | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: INT | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param INT mode: specify the interlacing mode (from 0 to 1) (default send_field)
        :param INT parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param INT deint: specify which frames to deinterlace (from 0 to 1) (default all)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif

        """
        filter_node = FilterNode(
            name="bwdif",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "parity": parity,
                        "deint": deint,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def cas(
        self,
        *,
        strength: FLOAT = Default("0"),
        planes: FLAGS = Default("7"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Contrast Adaptive Sharpen.

        Parameters:
        ----------

        :param FLOAT strength: set the sharpening strength (from 0 to 1) (default 0)
        :param FLAGS planes: set what planes to filter (default 7)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cas

        """
        filter_node = FilterNode(
            name="cas",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "strength": strength,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromahold(
        self,
        *,
        color: COLOR = Default("black"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        yuv: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray.

        Parameters:
        ----------

        :param COLOR color: set the chromahold key color (default "black")
        :param FLOAT similarity: set the chromahold similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the chromahold blend value (from 0 to 1) (default 0)
        :param BOOLEAN yuv: color parameter is in yuv instead of rgb (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromahold

        """
        filter_node = FilterNode(
            name="chromahold",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color": color,
                        "similarity": similarity,
                        "blend": blend,
                        "yuv": yuv,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromakey(
        self,
        *,
        color: COLOR = Default("black"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        yuv: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param COLOR color: set the chromakey key color (default "black")
        :param FLOAT similarity: set the chromakey similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the chromakey key blend value (from 0 to 1) (default 0)
        :param BOOLEAN yuv: color parameter is in yuv instead of rgb (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey

        """
        filter_node = FilterNode(
            name="chromakey",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color": color,
                        "similarity": similarity,
                        "blend": blend,
                        "yuv": yuv,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromanr(
        self,
        *,
        thres: FLOAT = Default("30"),
        sizew: INT = Default("5"),
        sizeh: INT = Default("5"),
        stepw: INT = Default("1"),
        steph: INT = Default("1"),
        threy: FLOAT = Default("200"),
        threu: FLOAT = Default("200"),
        threv: FLOAT = Default("200"),
        distance: INT | Literal["manhattan", "euclidean"] | Default = Default("manhattan"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce chrominance noise.

        Parameters:
        ----------

        :param FLOAT thres: set y+u+v threshold (from 1 to 200) (default 30)
        :param INT sizew: set horizontal patch size (from 1 to 100) (default 5)
        :param INT sizeh: set vertical patch size (from 1 to 100) (default 5)
        :param INT stepw: set horizontal step (from 1 to 50) (default 1)
        :param INT steph: set vertical step (from 1 to 50) (default 1)
        :param FLOAT threy: set y threshold (from 1 to 200) (default 200)
        :param FLOAT threu: set u threshold (from 1 to 200) (default 200)
        :param FLOAT threv: set v threshold (from 1 to 200) (default 200)
        :param INT distance: set distance type (from 0 to 1) (default manhattan)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromanr

        """
        filter_node = FilterNode(
            name="chromanr",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "thres": thres,
                        "sizew": sizew,
                        "sizeh": sizeh,
                        "stepw": stepw,
                        "steph": steph,
                        "threy": threy,
                        "threu": threu,
                        "threv": threv,
                        "distance": distance,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromashift(
        self,
        *,
        cbh: INT = Default("0"),
        cbv: INT = Default("0"),
        crh: INT = Default("0"),
        crv: INT = Default("0"),
        edge: INT | Literal["smear", "wrap"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift chroma.

        Parameters:
        ----------

        :param INT cbh: shift chroma-blue horizontally (from -255 to 255) (default 0)
        :param INT cbv: shift chroma-blue vertically (from -255 to 255) (default 0)
        :param INT crh: shift chroma-red horizontally (from -255 to 255) (default 0)
        :param INT crv: shift chroma-red vertically (from -255 to 255) (default 0)
        :param INT edge: set edge operation (from 0 to 1) (default smear)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromashift

        """
        filter_node = FilterNode(
            name="chromashift",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cbh": cbh,
                        "cbv": cbv,
                        "crh": crh,
                        "crv": crv,
                        "edge": edge,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def ciescope(
        self,
        *,
        system: INT
        | Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ]
        | Default = Default("hdtv"),
        cie: INT | Literal["xyy", "ucs", "luv"] | Default = Default("xyy"),
        gamuts: FLAGS
        | Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ]
        | Default = Default("0"),
        size: INT = Default("512"),
        intensity: FLOAT = Default("0.001"),
        contrast: FLOAT = Default("0.75"),
        corrgamma: BOOLEAN = Default("true"),
        showwhite: BOOLEAN = Default("false"),
        gamma: DOUBLE = Default("2.6"),
        fill: BOOLEAN = Default("true"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video CIE scope.

        Parameters:
        ----------

        :param INT system: set color system (from 0 to 9) (default hdtv)
        :param INT cie: set cie system (from 0 to 2) (default xyy)
        :param FLAGS gamuts: set what gamuts to draw (default 0)
        :param INT size: set ciescope size (from 256 to 8192) (default 512)
        :param FLOAT intensity: set ciescope intensity (from 0 to 1) (default 0.001)
        :param FLOAT contrast: (from 0 to 1) (default 0.75)
        :param BOOLEAN corrgamma: (default true)
        :param BOOLEAN showwhite: (default false)
        :param DOUBLE gamma: (from 0.1 to 6) (default 2.6)
        :param BOOLEAN fill: fill with CIE colors (default true)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ciescope

        """
        filter_node = FilterNode(
            name="ciescope",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "system": system,
                        "cie": cie,
                        "gamuts": gamuts,
                        "size": size,
                        "intensity": intensity,
                        "contrast": contrast,
                        "corrgamma": corrgamma,
                        "showwhite": showwhite,
                        "gamma": gamma,
                        "fill": fill,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def codecview(
        self,
        *,
        mv: FLAGS | Literal["pf", "bf", "bb"] | Default = Default("0"),
        qp: BOOLEAN = Default("false"),
        mv_type: FLAGS | Literal["fp", "bp"] | Default = Default("0"),
        frame_type: FLAGS | Literal["if", "pf", "bf"] | Default = Default("0"),
        block: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Visualize information about some codecs.

        Parameters:
        ----------

        :param FLAGS mv: set motion vectors to visualize (default 0)
        :param BOOLEAN qp: (default false)
        :param FLAGS mv_type: set motion vectors type (default 0)
        :param FLAGS frame_type: set frame types to visualize motion vectors of (default 0)
        :param BOOLEAN block: set block partitioning structure to visualize (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#codecview

        """
        filter_node = FilterNode(
            name="codecview",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mv": mv,
                        "qp": qp,
                        "mv_type": mv_type,
                        "frame_type": frame_type,
                        "block": block,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorbalance(
        self,
        *,
        rs: FLOAT = Default("0"),
        gs: FLOAT = Default("0"),
        bs: FLOAT = Default("0"),
        rm: FLOAT = Default("0"),
        gm: FLOAT = Default("0"),
        bm: FLOAT = Default("0"),
        rh: FLOAT = Default("0"),
        gh: FLOAT = Default("0"),
        bh: FLOAT = Default("0"),
        pl: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color balance.

        Parameters:
        ----------

        :param FLOAT rs: set red shadows (from -1 to 1) (default 0)
        :param FLOAT gs: set green shadows (from -1 to 1) (default 0)
        :param FLOAT bs: set blue shadows (from -1 to 1) (default 0)
        :param FLOAT rm: set red midtones (from -1 to 1) (default 0)
        :param FLOAT gm: set green midtones (from -1 to 1) (default 0)
        :param FLOAT bm: set blue midtones (from -1 to 1) (default 0)
        :param FLOAT rh: set red highlights (from -1 to 1) (default 0)
        :param FLOAT gh: set green highlights (from -1 to 1) (default 0)
        :param FLOAT bh: set blue highlights (from -1 to 1) (default 0)
        :param BOOLEAN pl: preserve lightness (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorbalance

        """
        filter_node = FilterNode(
            name="colorbalance",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rs": rs,
                        "gs": gs,
                        "bs": bs,
                        "rm": rm,
                        "gm": gm,
                        "bm": bm,
                        "rh": rh,
                        "gh": gh,
                        "bh": bh,
                        "pl": pl,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorchannelmixer(
        self,
        *,
        rr: DOUBLE = Default("1"),
        rg: DOUBLE = Default("0"),
        rb: DOUBLE = Default("0"),
        ra: DOUBLE = Default("0"),
        gr: DOUBLE = Default("0"),
        gg: DOUBLE = Default("1"),
        gb: DOUBLE = Default("0"),
        ga: DOUBLE = Default("0"),
        br: DOUBLE = Default("0"),
        bg: DOUBLE = Default("0"),
        bb: DOUBLE = Default("1"),
        ba: DOUBLE = Default("0"),
        ar: DOUBLE = Default("0"),
        ag: DOUBLE = Default("0"),
        ab: DOUBLE = Default("0"),
        aa: DOUBLE = Default("1"),
        pc: INT | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default("none"),
        pa: DOUBLE = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors by mixing color channels.

        Parameters:
        ----------

        :param DOUBLE rr: set the red gain for the red channel (from -2 to 2) (default 1)
        :param DOUBLE rg: set the green gain for the red channel (from -2 to 2) (default 0)
        :param DOUBLE rb: set the blue gain for the red channel (from -2 to 2) (default 0)
        :param DOUBLE ra: set the alpha gain for the red channel (from -2 to 2) (default 0)
        :param DOUBLE gr: set the red gain for the green channel (from -2 to 2) (default 0)
        :param DOUBLE gg: set the green gain for the green channel (from -2 to 2) (default 1)
        :param DOUBLE gb: set the blue gain for the green channel (from -2 to 2) (default 0)
        :param DOUBLE ga: set the alpha gain for the green channel (from -2 to 2) (default 0)
        :param DOUBLE br: set the red gain for the blue channel (from -2 to 2) (default 0)
        :param DOUBLE bg: set the green gain for the blue channel (from -2 to 2) (default 0)
        :param DOUBLE bb: set the blue gain for the blue channel (from -2 to 2) (default 1)
        :param DOUBLE ba: set the alpha gain for the blue channel (from -2 to 2) (default 0)
        :param DOUBLE ar: set the red gain for the alpha channel (from -2 to 2) (default 0)
        :param DOUBLE ag: set the green gain for the alpha channel (from -2 to 2) (default 0)
        :param DOUBLE ab: set the blue gain for the alpha channel (from -2 to 2) (default 0)
        :param DOUBLE aa: set the alpha gain for the alpha channel (from -2 to 2) (default 1)
        :param INT pc: set the preserve color mode (from 0 to 6) (default none)
        :param DOUBLE pa: set the preserve color amount (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer

        """
        filter_node = FilterNode(
            name="colorchannelmixer",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rr": rr,
                        "rg": rg,
                        "rb": rb,
                        "ra": ra,
                        "gr": gr,
                        "gg": gg,
                        "gb": gb,
                        "ga": ga,
                        "br": br,
                        "bg": bg,
                        "bb": bb,
                        "ba": ba,
                        "ar": ar,
                        "ag": ag,
                        "ab": ab,
                        "aa": aa,
                        "pc": pc,
                        "pa": pa,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorcontrast(
        self,
        *,
        rc: FLOAT = Default("0"),
        gm: FLOAT = Default("0"),
        by: FLOAT = Default("0"),
        rcw: FLOAT = Default("0"),
        gmw: FLOAT = Default("0"),
        byw: FLOAT = Default("0"),
        pl: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color contrast between RGB components.

        Parameters:
        ----------

        :param FLOAT rc: set the red-cyan contrast (from -1 to 1) (default 0)
        :param FLOAT gm: set the green-magenta contrast (from -1 to 1) (default 0)
        :param FLOAT by: set the blue-yellow contrast (from -1 to 1) (default 0)
        :param FLOAT rcw: set the red-cyan weight (from 0 to 1) (default 0)
        :param FLOAT gmw: set the green-magenta weight (from 0 to 1) (default 0)
        :param FLOAT byw: set the blue-yellow weight (from 0 to 1) (default 0)
        :param FLOAT pl: set the amount of preserving lightness (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcontrast

        """
        filter_node = FilterNode(
            name="colorcontrast",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rc": rc,
                        "gm": gm,
                        "by": by,
                        "rcw": rcw,
                        "gmw": gmw,
                        "byw": byw,
                        "pl": pl,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorcorrect(
        self,
        *,
        rl: FLOAT = Default("0"),
        bl: FLOAT = Default("0"),
        rh: FLOAT = Default("0"),
        bh: FLOAT = Default("0"),
        saturation: FLOAT = Default("1"),
        analyze: INT | Literal["manual", "average", "minmax", "median"] | Default = Default("manual"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color white balance selectively for blacks and whites.

        Parameters:
        ----------

        :param FLOAT rl: set the red shadow spot (from -1 to 1) (default 0)
        :param FLOAT bl: set the blue shadow spot (from -1 to 1) (default 0)
        :param FLOAT rh: set the red highlight spot (from -1 to 1) (default 0)
        :param FLOAT bh: set the blue highlight spot (from -1 to 1) (default 0)
        :param FLOAT saturation: set the amount of saturation (from -3 to 3) (default 1)
        :param INT analyze: set the analyze mode (from 0 to 3) (default manual)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcorrect

        """
        filter_node = FilterNode(
            name="colorcorrect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rl": rl,
                        "bl": bl,
                        "rh": rh,
                        "bh": bh,
                        "saturation": saturation,
                        "analyze": analyze,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorhold(
        self,
        *,
        color: COLOR = Default("black"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray. Operates on RGB colors.

        Parameters:
        ----------

        :param COLOR color: set the colorhold key color (default "black")
        :param FLOAT similarity: set the colorhold similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the colorhold blend value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorhold

        """
        filter_node = FilterNode(
            name="colorhold",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color": color,
                        "similarity": similarity,
                        "blend": blend,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorize(
        self,
        *,
        hue: FLOAT = Default("0"),
        saturation: FLOAT = Default("0.5"),
        lightness: FLOAT = Default("0.5"),
        mix: FLOAT = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Overlay a solid color on the video stream.

        Parameters:
        ----------

        :param FLOAT hue: set the hue (from 0 to 360) (default 0)
        :param FLOAT saturation: set the saturation (from 0 to 1) (default 0.5)
        :param FLOAT lightness: set the lightness (from 0 to 1) (default 0.5)
        :param FLOAT mix: set the mix of source lightness (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorize

        """
        filter_node = FilterNode(
            name="colorize",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "hue": hue,
                        "saturation": saturation,
                        "lightness": lightness,
                        "mix": mix,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorkey(
        self,
        *,
        color: COLOR = Default("black"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on RGB colors.

        Parameters:
        ----------

        :param COLOR color: set the colorkey key color (default "black")
        :param FLOAT similarity: set the colorkey similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the colorkey key blend value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorkey

        """
        filter_node = FilterNode(
            name="colorkey",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color": color,
                        "similarity": similarity,
                        "blend": blend,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorlevels(
        self,
        *,
        rimin: DOUBLE = Default("0"),
        gimin: DOUBLE = Default("0"),
        bimin: DOUBLE = Default("0"),
        aimin: DOUBLE = Default("0"),
        rimax: DOUBLE = Default("1"),
        gimax: DOUBLE = Default("1"),
        bimax: DOUBLE = Default("1"),
        aimax: DOUBLE = Default("1"),
        romin: DOUBLE = Default("0"),
        gomin: DOUBLE = Default("0"),
        bomin: DOUBLE = Default("0"),
        aomin: DOUBLE = Default("0"),
        romax: DOUBLE = Default("1"),
        gomax: DOUBLE = Default("1"),
        bomax: DOUBLE = Default("1"),
        aomax: DOUBLE = Default("1"),
        preserve: INT | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default("none"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color levels.

        Parameters:
        ----------

        :param DOUBLE rimin: set input red black point (from -1 to 1) (default 0)
        :param DOUBLE gimin: set input green black point (from -1 to 1) (default 0)
        :param DOUBLE bimin: set input blue black point (from -1 to 1) (default 0)
        :param DOUBLE aimin: set input alpha black point (from -1 to 1) (default 0)
        :param DOUBLE rimax: set input red white point (from -1 to 1) (default 1)
        :param DOUBLE gimax: set input green white point (from -1 to 1) (default 1)
        :param DOUBLE bimax: set input blue white point (from -1 to 1) (default 1)
        :param DOUBLE aimax: set input alpha white point (from -1 to 1) (default 1)
        :param DOUBLE romin: set output red black point (from 0 to 1) (default 0)
        :param DOUBLE gomin: set output green black point (from 0 to 1) (default 0)
        :param DOUBLE bomin: set output blue black point (from 0 to 1) (default 0)
        :param DOUBLE aomin: set output alpha black point (from 0 to 1) (default 0)
        :param DOUBLE romax: set output red white point (from 0 to 1) (default 1)
        :param DOUBLE gomax: set output green white point (from 0 to 1) (default 1)
        :param DOUBLE bomax: set output blue white point (from 0 to 1) (default 1)
        :param DOUBLE aomax: set output alpha white point (from 0 to 1) (default 1)
        :param INT preserve: set preserve color mode (from 0 to 6) (default none)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorlevels

        """
        filter_node = FilterNode(
            name="colorlevels",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rimin": rimin,
                        "gimin": gimin,
                        "bimin": bimin,
                        "aimin": aimin,
                        "rimax": rimax,
                        "gimax": gimax,
                        "bimax": bimax,
                        "aimax": aimax,
                        "romin": romin,
                        "gomin": gomin,
                        "bomin": bomin,
                        "aomin": aomin,
                        "romax": romax,
                        "gomax": gomax,
                        "bomax": bomax,
                        "aomax": aomax,
                        "preserve": preserve,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colormap(
        self,
        _source: "VideoStream",
        _target: "VideoStream",
        *,
        patch_size: IMAGE_SIZE = Default("64x64"),
        nb_patches: INT = Default("0"),
        type: INT | Literal["relative", "absolute"] | Default = Default("absolute"),
        kernel: INT | Literal["euclidean", "weuclidean"] | Default = Default("euclidean"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def colormatrix(
        self,
        *,
        src: INT
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("-1"),
        dst: INT
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert color matrix.

        Parameters:
        ----------

        :param INT src: set source color matrix (from -1 to 4) (default -1)
        :param INT dst: set destination color matrix (from -1 to 4) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colormatrix

        """
        filter_node = FilterNode(
            name="colormatrix",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "src": src,
                        "dst": dst,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorspace(
        self,
        *,
        all: INT
        | Literal["bt470m", "bt470bg", "525", "625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("0"),
        space: INT
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default("2"),
        range: INT | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("0"),
        primaries: INT
        | Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "p22",
            "ebu3213",
        ]
        | Default = Default("2"),
        trc: INT
        | Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "1",
            "xvycc",
            "4",
            "10",
            "12",
        ]
        | Default = Default("2"),
        format: INT
        | Literal[
            "yuv420p",
            "yuv420p10",
            "yuv420p12",
            "yuv422p",
            "yuv422p10",
            "yuv422p12",
            "yuv444p",
            "yuv444p10",
            "yuv444p12",
        ]
        | Default = Default("-1"),
        fast: BOOLEAN = Default("false"),
        dither: INT | Literal["none", "fsb"] | Default = Default("none"),
        wpadapt: INT | Literal["bradford", "vonkries", "identity"] | Default = Default("bradford"),
        iall: INT
        | Literal["bt470m", "bt470bg", "525", "625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("0"),
        ispace: INT
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default("2"),
        irange: INT | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("0"),
        iprimaries: INT
        | Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "p22",
            "ebu3213",
        ]
        | Default = Default("2"),
        itrc: INT
        | Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "1",
            "xvycc",
            "4",
            "10",
            "12",
        ]
        | Default = Default("2"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert between colorspaces.

        Parameters:
        ----------

        :param INT all: Set all color properties together (from 0 to 8) (default 0)
        :param INT space: Output colorspace (from 0 to 14) (default 2)
        :param INT range: Output color range (from 0 to 2) (default 0)
        :param INT primaries: Output color primaries (from 0 to 22) (default 2)
        :param INT trc: Output transfer characteristics (from 0 to 18) (default 2)
        :param INT format: Output pixel format (from -1 to 162) (default -1)
        :param BOOLEAN fast: Ignore primary chromaticity and gamma correction (default false)
        :param INT dither: Dithering mode (from 0 to 1) (default none)
        :param INT wpadapt: Whitepoint adaptation method (from 0 to 2) (default bradford)
        :param INT iall: Set all input color properties together (from 0 to 8) (default 0)
        :param INT ispace: Input colorspace (from 0 to 22) (default 2)
        :param INT irange: Input color range (from 0 to 2) (default 0)
        :param INT iprimaries: Input color primaries (from 0 to 22) (default 2)
        :param INT itrc: Input transfer characteristics (from 0 to 18) (default 2)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace

        """
        filter_node = FilterNode(
            name="colorspace",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "all": all,
                        "space": space,
                        "range": range,
                        "primaries": primaries,
                        "trc": trc,
                        "format": format,
                        "fast": fast,
                        "dither": dither,
                        "wpadapt": wpadapt,
                        "iall": iall,
                        "ispace": ispace,
                        "irange": irange,
                        "iprimaries": iprimaries,
                        "itrc": itrc,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colortemperature(
        self,
        *,
        temperature: FLOAT = Default("6500"),
        mix: FLOAT = Default("1"),
        pl: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color temperature of video.

        Parameters:
        ----------

        :param FLOAT temperature: set the temperature in Kelvin (from 1000 to 40000) (default 6500)
        :param FLOAT mix: set the mix with filtered output (from 0 to 1) (default 1)
        :param FLOAT pl: set the amount of preserving lightness (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colortemperature

        """
        filter_node = FilterNode(
            name="colortemperature",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "temperature": temperature,
                        "mix": mix,
                        "pl": pl,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def convolution(
        self,
        *,
        _0m: STRING = Default("0 0 0 0 1 0 0 0 0"),
        _1m: STRING = Default("0 0 0 0 1 0 0 0 0"),
        _2m: STRING = Default("0 0 0 0 1 0 0 0 0"),
        _3m: STRING = Default("0 0 0 0 1 0 0 0 0"),
        _0rdiv: FLOAT = Default("0"),
        _1rdiv: FLOAT = Default("0"),
        _2rdiv: FLOAT = Default("0"),
        _3rdiv: FLOAT = Default("0"),
        _0bias: FLOAT = Default("0"),
        _1bias: FLOAT = Default("0"),
        _2bias: FLOAT = Default("0"),
        _3bias: FLOAT = Default("0"),
        _0mode: INT | Literal["square", "row", "column"] | Default = Default("square"),
        _1mode: INT | Literal["square", "row", "column"] | Default = Default("square"),
        _2mode: INT | Literal["square", "row", "column"] | Default = Default("square"),
        _3mode: INT | Literal["square", "row", "column"] | Default = Default("square"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply convolution filter.

        Parameters:
        ----------

        :param STRING _0m: set matrix for 1st plane (default "0 0 0 0 1 0 0 0 0")
        :param STRING _1m: set matrix for 2nd plane (default "0 0 0 0 1 0 0 0 0")
        :param STRING _2m: set matrix for 3rd plane (default "0 0 0 0 1 0 0 0 0")
        :param STRING _3m: set matrix for 4th plane (default "0 0 0 0 1 0 0 0 0")
        :param FLOAT _0rdiv: set rdiv for 1st plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _1rdiv: set rdiv for 2nd plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _2rdiv: set rdiv for 3rd plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _3rdiv: set rdiv for 4th plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _0bias: set bias for 1st plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _1bias: set bias for 2nd plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _2bias: set bias for 3rd plane (from 0 to INT_MAX) (default 0)
        :param FLOAT _3bias: set bias for 4th plane (from 0 to INT_MAX) (default 0)
        :param INT _0mode: set matrix mode for 1st plane (from 0 to 2) (default square)
        :param INT _1mode: set matrix mode for 2nd plane (from 0 to 2) (default square)
        :param INT _2mode: set matrix mode for 3rd plane (from 0 to 2) (default square)
        :param INT _3mode: set matrix mode for 4th plane (from 0 to 2) (default square)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#convolution

        """
        filter_node = FilterNode(
            name="convolution",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "0m": _0m,
                        "1m": _1m,
                        "2m": _2m,
                        "3m": _3m,
                        "0rdiv": _0rdiv,
                        "1rdiv": _1rdiv,
                        "2rdiv": _2rdiv,
                        "3rdiv": _3rdiv,
                        "0bias": _0bias,
                        "1bias": _1bias,
                        "2bias": _2bias,
                        "3bias": _3bias,
                        "0mode": _0mode,
                        "1mode": _1mode,
                        "2mode": _2mode,
                        "3mode": _3mode,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def convolve(
        self,
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
        **kwargs: Any,
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
                self,
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

    def copy(self, **kwargs: Any) -> "VideoStream":
        """

        Copy the input video unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#copy

        """
        filter_node = FilterNode(
            name="copy",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def coreimage(
        self,
        *,
        list_filters: BOOLEAN = Default("false"),
        list_generators: BOOLEAN = Default("false"),
        filter: STRING = Default(None),
        output_rect: STRING = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video filtering using CoreImage API.

        Parameters:
        ----------

        :param BOOLEAN list_filters: list available filters (default false)
        :param BOOLEAN list_generators: list available generators (default false)
        :param STRING filter: names and options of filters to apply
        :param STRING output_rect: output rectangle within output image

        Ref: https://ffmpeg.org/ffmpeg-filters.html#coreimage

        """
        filter_node = FilterNode(
            name="coreimage",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "list_filters": list_filters,
                        "list_generators": list_generators,
                        "filter": filter,
                        "output_rect": output_rect,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def corr(
        self,
        _reference: "VideoStream",
        *,
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def cover_rect(
        self,
        *,
        cover: STRING = Default(None),
        mode: INT | Literal["cover", "blur"] | Default = Default("blur"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find and cover a user specified object.

        Parameters:
        ----------

        :param STRING cover: cover bitmap filename
        :param INT mode: set removal mode (from 0 to 1) (default blur)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cover_005frect

        """
        filter_node = FilterNode(
            name="cover_rect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cover": cover,
                        "mode": mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def crop(
        self,
        *,
        out_w: STRING = Default("iw"),
        out_h: STRING = Default("ih"),
        x: STRING = Default("(in_w-out_w"),
        y: STRING = Default("(in_h-out_h"),
        keep_aspect: BOOLEAN = Default("false"),
        exact: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Crop the input video.

        Parameters:
        ----------

        :param STRING out_w: set the width crop area expression (default "iw")
        :param STRING out_h: set the height crop area expression (default "ih")
        :param STRING x: set the x crop area expression (default "(in_w-out_w)/2")
        :param STRING y: set the y crop area expression (default "(in_h-out_h)/2")
        :param BOOLEAN keep_aspect: keep aspect ratio (default false)
        :param BOOLEAN exact: do exact cropping (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crop

        """
        filter_node = FilterNode(
            name="crop",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "out_w": out_w,
                        "out_h": out_h,
                        "x": x,
                        "y": y,
                        "keep_aspect": keep_aspect,
                        "exact": exact,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def cropdetect(
        self,
        *,
        limit: FLOAT = Default("0.0941176"),
        round: INT = Default("16"),
        reset: INT = Default("0"),
        skip: INT = Default("2"),
        reset_count: INT = Default("0"),
        max_outliers: INT = Default("0"),
        mode: INT | Literal["black", "mvedges"] | Default = Default("black"),
        high: FLOAT = Default("0.0980392"),
        low: FLOAT = Default("0.0588235"),
        mv_threshold: INT = Default("8"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Auto-detect crop size.

        Parameters:
        ----------

        :param FLOAT limit: Threshold below which the pixel is considered black (from 0 to 65535) (default 0.0941176)
        :param INT round: Value by which the width/height should be divisible (from 0 to INT_MAX) (default 16)
        :param INT reset: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
        :param INT skip: Number of initial frames to skip (from 0 to INT_MAX) (default 2)
        :param INT reset_count: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
        :param INT max_outliers: Threshold count of outliers (from 0 to INT_MAX) (default 0)
        :param INT mode: set mode (from 0 to 1) (default black)
        :param FLOAT high: Set high threshold for edge detection (from 0 to 1) (default 0.0980392)
        :param FLOAT low: Set low threshold for edge detection (from 0 to 1) (default 0.0588235)
        :param INT mv_threshold: motion vector threshold when estimating video window size (from 0 to 100) (default 8)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cropdetect

        """
        filter_node = FilterNode(
            name="cropdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "limit": limit,
                        "round": round,
                        "reset": reset,
                        "skip": skip,
                        "reset_count": reset_count,
                        "max_outliers": max_outliers,
                        "mode": mode,
                        "high": high,
                        "low": low,
                        "mv_threshold": mv_threshold,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def cue(
        self,
        *,
        cue: INT64 = Default("0"),
        preroll: DURATION = Default("0"),
        buffer: DURATION = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Delay filtering to match a cue.

        Parameters:
        ----------

        :param INT64 cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
        :param DURATION preroll: preroll duration in seconds (default 0)
        :param DURATION buffer: buffer duration in seconds (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cue

        """
        filter_node = FilterNode(
            name="cue",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def curves(
        self,
        *,
        preset: INT
        | Literal[
            "none",
            "color_negative",
            "cross_process",
            "darker",
            "increase_contrast",
            "lighter",
            "linear_contrast",
            "medium_contrast",
            "negative",
            "strong_contrast",
            "vintage",
        ]
        | Default = Default("none"),
        master: STRING = Default(None),
        red: STRING = Default(None),
        green: STRING = Default(None),
        blue: STRING = Default(None),
        all: STRING = Default(None),
        psfile: STRING = Default(None),
        plot: STRING = Default(None),
        interp: INT | Literal["natural", "pchip"] | Default = Default("natural"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust components curves.

        Parameters:
        ----------

        :param INT preset: select a color curves preset (from 0 to 10) (default none)
        :param STRING master: set master points coordinates
        :param STRING red: set red points coordinates
        :param STRING green: set green points coordinates
        :param STRING blue: set blue points coordinates
        :param STRING all: set points coordinates for all components
        :param STRING psfile: set Photoshop curves file name
        :param STRING plot: save Gnuplot script of the curves in specified file
        :param INT interp: specify the kind of interpolation (from 0 to 1) (default natural)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#curves

        """
        filter_node = FilterNode(
            name="curves",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "preset": preset,
                        "master": master,
                        "red": red,
                        "green": green,
                        "blue": blue,
                        "all": all,
                        "psfile": psfile,
                        "plot": plot,
                        "interp": interp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def datascope(
        self,
        *,
        size: IMAGE_SIZE = Default("hd720"),
        x: INT = Default("0"),
        y: INT = Default("0"),
        mode: INT | Literal["mono", "color", "color2"] | Default = Default("mono"),
        axis: BOOLEAN = Default("false"),
        opacity: FLOAT = Default("0.75"),
        format: INT | Literal["hex", "dec"] | Default = Default("hex"),
        components: INT = Default("15"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video data analysis.

        Parameters:
        ----------

        :param IMAGE_SIZE size: set output size (default "hd720")
        :param INT x: set x offset (from 0 to INT_MAX) (default 0)
        :param INT y: set y offset (from 0 to INT_MAX) (default 0)
        :param INT mode: set scope mode (from 0 to 2) (default mono)
        :param BOOLEAN axis: draw column/row numbers (default false)
        :param FLOAT opacity: set background opacity (from 0 to 1) (default 0.75)
        :param INT format: set display number format (from 0 to 1) (default hex)
        :param INT components: set components to display (from 1 to 15) (default 15)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#datascope

        """
        filter_node = FilterNode(
            name="datascope",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "x": x,
                        "y": y,
                        "mode": mode,
                        "axis": axis,
                        "opacity": opacity,
                        "format": format,
                        "components": components,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dblur(
        self,
        *,
        angle: FLOAT = Default("45"),
        radius: FLOAT = Default("5"),
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Directional Blur filter.

        Parameters:
        ----------

        :param FLOAT angle: set angle (from 0 to 360) (default 45)
        :param FLOAT radius: set radius (from 0 to 8192) (default 5)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dblur

        """
        filter_node = FilterNode(
            name="dblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "angle": angle,
                        "radius": radius,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dctdnoiz(
        self,
        *,
        sigma: FLOAT = Default("0"),
        overlap: INT = Default("-1"),
        expr: STRING = Default(None),
        n: INT = Default("3"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise frames using 2D DCT.

        Parameters:
        ----------

        :param FLOAT sigma: set noise sigma constant (from 0 to 999) (default 0)
        :param INT overlap: set number of block overlapping pixels (from -1 to 15) (default -1)
        :param STRING expr: set coefficient factor expression
        :param INT n: set the block size, expressed in bits (from 3 to 4) (default 3)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dctdnoiz

        """
        filter_node = FilterNode(
            name="dctdnoiz",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigma": sigma,
                        "overlap": overlap,
                        "expr": expr,
                        "n": n,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deband(
        self,
        *,
        _1thr: FLOAT = Default("0.02"),
        _2thr: FLOAT = Default("0.02"),
        _3thr: FLOAT = Default("0.02"),
        _4thr: FLOAT = Default("0.02"),
        range: INT = Default("16"),
        direction: FLOAT = Default("6.28319"),
        blur: BOOLEAN = Default("true"),
        coupling: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Debands video.

        Parameters:
        ----------

        :param FLOAT _1thr: set 1st plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param FLOAT _2thr: set 2nd plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param FLOAT _3thr: set 3rd plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param FLOAT _4thr: set 4th plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param INT range: set range (from INT_MIN to INT_MAX) (default 16)
        :param FLOAT direction: set direction (from -6.28319 to 6.28319) (default 6.28319)
        :param BOOLEAN blur: set blur (default true)
        :param BOOLEAN coupling: set plane coupling (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deband

        """
        filter_node = FilterNode(
            name="deband",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "1thr": _1thr,
                        "2thr": _2thr,
                        "3thr": _3thr,
                        "4thr": _4thr,
                        "range": range,
                        "direction": direction,
                        "blur": blur,
                        "coupling": coupling,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deblock(
        self,
        *,
        filter: INT | Literal["weak", "strong"] | Default = Default("strong"),
        block: INT = Default("8"),
        alpha: FLOAT = Default("0.098"),
        beta: FLOAT = Default("0.05"),
        gamma: FLOAT = Default("0.05"),
        delta: FLOAT = Default("0.05"),
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deblock video.

        Parameters:
        ----------

        :param INT filter: set type of filter (from 0 to 1) (default strong)
        :param INT block: set size of block (from 4 to 512) (default 8)
        :param FLOAT alpha: set 1st detection threshold (from 0 to 1) (default 0.098)
        :param FLOAT beta: set 2nd detection threshold (from 0 to 1) (default 0.05)
        :param FLOAT gamma: set 3rd detection threshold (from 0 to 1) (default 0.05)
        :param FLOAT delta: set 4th detection threshold (from 0 to 1) (default 0.05)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deblock

        """
        filter_node = FilterNode(
            name="deblock",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filter": filter,
                        "block": block,
                        "alpha": alpha,
                        "beta": beta,
                        "gamma": gamma,
                        "delta": delta,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deconvolve(
        self,
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
        **kwargs: Any,
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
                self,
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

    def dedot(
        self,
        *,
        m: FLAGS | Literal["dotcrawl", "rainbows"] | Default = Default("dotcrawl+rainbows"),
        lt: FLOAT = Default("0.079"),
        tl: FLOAT = Default("0.079"),
        tc: FLOAT = Default("0.058"),
        ct: FLOAT = Default("0.019"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce cross-luminance and cross-color.

        Parameters:
        ----------

        :param FLAGS m: set filtering mode (default dotcrawl+rainbows)
        :param FLOAT lt: set spatial luma threshold (from 0 to 1) (default 0.079)
        :param FLOAT tl: set tolerance for temporal luma (from 0 to 1) (default 0.079)
        :param FLOAT tc: set tolerance for chroma temporal variation (from 0 to 1) (default 0.058)
        :param FLOAT ct: set temporal chroma threshold (from 0 to 1) (default 0.019)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dedot

        """
        filter_node = FilterNode(
            name="dedot",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "m": m,
                        "lt": lt,
                        "tl": tl,
                        "tc": tc,
                        "ct": ct,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deflate(
        self,
        *,
        threshold0: INT = Default("65535"),
        threshold1: INT = Default("65535"),
        threshold2: INT = Default("65535"),
        threshold3: INT = Default("65535"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply deflate effect.

        Parameters:
        ----------

        :param INT threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param INT threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param INT threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param INT threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflate

        """
        filter_node = FilterNode(
            name="deflate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold0": threshold0,
                        "threshold1": threshold1,
                        "threshold2": threshold2,
                        "threshold3": threshold3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deflicker(
        self,
        *,
        size: INT = Default("5"),
        mode: INT | Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | Default = Default("am"),
        bypass: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove temporal frame luminance variations.

        Parameters:
        ----------

        :param INT size: set how many frames to use (from 2 to 129) (default 5)
        :param INT mode: set how to smooth luminance (from 0 to 6) (default am)
        :param BOOLEAN bypass: leave frames unchanged (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflicker

        """
        filter_node = FilterNode(
            name="deflicker",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "size": size,
                        "mode": mode,
                        "bypass": bypass,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dejudder(self, *, cycle: INT = Default("4"), **kwargs: Any) -> "VideoStream":
        """

        Remove judder produced by pullup.

        Parameters:
        ----------

        :param INT cycle: set the length of the cycle to use for dejuddering (from 2 to 240) (default 4)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dejudder

        """
        filter_node = FilterNode(
            name="dejudder",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cycle": cycle,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def delogo(
        self,
        *,
        x: STRING = Default("-1"),
        y: STRING = Default("-1"),
        w: STRING = Default("-1"),
        h: STRING = Default("-1"),
        show: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove logo from input video.

        Parameters:
        ----------

        :param STRING x: set logo x position (default "-1")
        :param STRING y: set logo y position (default "-1")
        :param STRING w: set logo width (default "-1")
        :param STRING h: set logo height (default "-1")
        :param BOOLEAN show: show delogo area (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#delogo

        """
        filter_node = FilterNode(
            name="delogo",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h,
                        "show": show,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def derain(
        self,
        *,
        filter_type: INT | Literal["derain", "dehaze"] | Default = Default("derain"),
        dnn_backend: INT | Literal["native"] | Default = Default("native"),
        model: STRING = Default(None),
        input: STRING = Default("x"),
        output: STRING = Default("y"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply derain filter to the input.

        Parameters:
        ----------

        :param INT filter_type: filter type(derain/dehaze) (from 0 to 1) (default derain)
        :param INT dnn_backend: DNN backend (from 0 to 1) (default native)
        :param STRING model: path to model file
        :param STRING input: input name of the model (default "x")
        :param STRING output: output name of the model (default "y")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#derain

        """
        filter_node = FilterNode(
            name="derain",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filter_type": filter_type,
                        "dnn_backend": dnn_backend,
                        "model": model,
                        "input": input,
                        "output": output,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def deshake(
        self,
        *,
        x: INT = Default("-1"),
        y: INT = Default("-1"),
        w: INT = Default("-1"),
        h: INT = Default("-1"),
        rx: INT = Default("16"),
        ry: INT = Default("16"),
        edge: INT | Literal["blank", "original", "clamp", "mirror"] | Default = Default("mirror"),
        blocksize: INT = Default("8"),
        contrast: INT = Default("125"),
        search: INT | Literal["exhaustive", "less"] | Default = Default("exhaustive"),
        filename: STRING = Default(None),
        opencl: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Stabilize shaky video.

        Parameters:
        ----------

        :param INT x: set x for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param INT y: set y for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param INT w: set width for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param INT h: set height for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param INT rx: set x for the rectangular search area (from 0 to 64) (default 16)
        :param INT ry: set y for the rectangular search area (from 0 to 64) (default 16)
        :param INT edge: set edge mode (from 0 to 3) (default mirror)
        :param INT blocksize: set motion search blocksize (from 4 to 128) (default 8)
        :param INT contrast: set contrast threshold for blocks (from 1 to 255) (default 125)
        :param INT search: set search strategy (from 0 to 1) (default exhaustive)
        :param STRING filename: set motion search detailed log file name
        :param BOOLEAN opencl: ignored (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deshake

        """
        filter_node = FilterNode(
            name="deshake",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h,
                        "rx": rx,
                        "ry": ry,
                        "edge": edge,
                        "blocksize": blocksize,
                        "contrast": contrast,
                        "search": search,
                        "filename": filename,
                        "opencl": opencl,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def despill(
        self,
        *,
        type: INT | Literal["green", "blue"] | Default = Default("green"),
        mix: FLOAT = Default("0.5"),
        expand: FLOAT = Default("0"),
        red: FLOAT = Default("0"),
        green: FLOAT = Default("-1"),
        blue: FLOAT = Default("0"),
        brightness: FLOAT = Default("0"),
        alpha: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Despill video.

        Parameters:
        ----------

        :param INT type: set the screen type (from 0 to 1) (default green)
        :param FLOAT mix: set the spillmap mix (from 0 to 1) (default 0.5)
        :param FLOAT expand: set the spillmap expand (from 0 to 1) (default 0)
        :param FLOAT red: set red scale (from -100 to 100) (default 0)
        :param FLOAT green: set green scale (from -100 to 100) (default -1)
        :param FLOAT blue: set blue scale (from -100 to 100) (default 0)
        :param FLOAT brightness: set brightness (from -10 to 10) (default 0)
        :param BOOLEAN alpha: change alpha component (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#despill

        """
        filter_node = FilterNode(
            name="despill",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "type": type,
                        "mix": mix,
                        "expand": expand,
                        "red": red,
                        "green": green,
                        "blue": blue,
                        "brightness": brightness,
                        "alpha": alpha,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def detelecine(
        self,
        *,
        first_field: INT | Literal["top", "t", "bottom", "b"] | Default = Default("top"),
        pattern: STRING = Default("23"),
        start_frame: INT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an inverse telecine pattern.

        Parameters:
        ----------

        :param INT first_field: select first field (from 0 to 1) (default top)
        :param STRING pattern: pattern that describe for how many fields a frame is to be displayed (default "23")
        :param INT start_frame: position of first frame with respect to the pattern if stream is cut (from 0 to 13) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#detelecine

        """
        filter_node = FilterNode(
            name="detelecine",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "first_field": first_field,
                        "pattern": pattern,
                        "start_frame": start_frame,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dilation(
        self,
        *,
        coordinates: INT = Default("255"),
        threshold0: INT = Default("65535"),
        threshold1: INT = Default("65535"),
        threshold2: INT = Default("65535"),
        threshold3: INT = Default("65535"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply dilation effect.

        Parameters:
        ----------

        :param INT coordinates: set coordinates (from 0 to 255) (default 255)
        :param INT threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param INT threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param INT threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param INT threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dilation

        """
        filter_node = FilterNode(
            name="dilation",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "coordinates": coordinates,
                        "threshold0": threshold0,
                        "threshold1": threshold1,
                        "threshold2": threshold2,
                        "threshold3": threshold3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def displace(
        self,
        _xmap: "VideoStream",
        _ymap: "VideoStream",
        *,
        edge: INT | Literal["blank", "smear", "wrap", "mirror"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def dnn_classify(
        self,
        *,
        dnn_backend: INT = Default("2"),
        model: STRING = Default(None),
        input: STRING = Default(None),
        output: STRING = Default(None),
        backend_configs: STRING = Default(None),
        options: STRING = Default(None),
        _async: BOOLEAN = Default("true"),
        confidence: FLOAT = Default("0.5"),
        labels: STRING = Default(None),
        target: STRING = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN classify filter to the input.

        Parameters:
        ----------

        :param INT dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
        :param STRING model: path to model file
        :param STRING input: input name of the model
        :param STRING output: output name of the model
        :param STRING backend_configs: backend configs
        :param STRING options: backend configs (deprecated, use backend_configs)
        :param BOOLEAN _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
        :param FLOAT confidence: threshold of confidence (from 0 to 1) (default 0.5)
        :param STRING labels: path to labels file
        :param STRING target: which one to be classified

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fclassify

        """
        filter_node = FilterNode(
            name="dnn_classify",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dnn_backend": dnn_backend,
                        "model": model,
                        "input": input,
                        "output": output,
                        "backend_configs": backend_configs,
                        "options": options,
                        "async": _async,
                        "confidence": confidence,
                        "labels": labels,
                        "target": target,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dnn_detect(
        self,
        *,
        dnn_backend: INT = Default("2"),
        model: STRING = Default(None),
        input: STRING = Default(None),
        output: STRING = Default(None),
        backend_configs: STRING = Default(None),
        options: STRING = Default(None),
        _async: BOOLEAN = Default("true"),
        confidence: FLOAT = Default("0.5"),
        labels: STRING = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN detect filter to the input.

        Parameters:
        ----------

        :param INT dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
        :param STRING model: path to model file
        :param STRING input: input name of the model
        :param STRING output: output name of the model
        :param STRING backend_configs: backend configs
        :param STRING options: backend configs (deprecated, use backend_configs)
        :param BOOLEAN _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
        :param FLOAT confidence: threshold of confidence (from 0 to 1) (default 0.5)
        :param STRING labels: path to labels file

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fdetect

        """
        filter_node = FilterNode(
            name="dnn_detect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dnn_backend": dnn_backend,
                        "model": model,
                        "input": input,
                        "output": output,
                        "backend_configs": backend_configs,
                        "options": options,
                        "async": _async,
                        "confidence": confidence,
                        "labels": labels,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dnn_processing(
        self,
        *,
        dnn_backend: INT | Literal["native"] | Default = Default("native"),
        model: STRING = Default(None),
        input: STRING = Default(None),
        output: STRING = Default(None),
        backend_configs: STRING = Default(None),
        options: STRING = Default(None),
        _async: BOOLEAN = Default("true"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN processing filter to the input.

        Parameters:
        ----------

        :param INT dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default native)
        :param STRING model: path to model file
        :param STRING input: input name of the model
        :param STRING output: output name of the model
        :param STRING backend_configs: backend configs
        :param STRING options: backend configs (deprecated, use backend_configs)
        :param BOOLEAN _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fprocessing

        """
        filter_node = FilterNode(
            name="dnn_processing",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dnn_backend": dnn_backend,
                        "model": model,
                        "input": input,
                        "output": output,
                        "backend_configs": backend_configs,
                        "options": options,
                        "async": _async,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def doubleweave(
        self, *, first_field: INT | Literal["top", "t", "bottom", "b"] | Default = Default("top"), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into double number of frames.

        Parameters:
        ----------

        :param INT first_field: set first field (from 0 to 1) (default top)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        filter_node = FilterNode(
            name="doubleweave",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "first_field": first_field,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def drawbox(
        self,
        *,
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        width: STRING = Default("0"),
        height: STRING = Default("0"),
        color: STRING = Default("black"),
        thickness: STRING = Default("3"),
        replace: BOOLEAN = Default("false"),
        box_source: STRING = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored box on the input video.

        Parameters:
        ----------

        :param STRING x: set horizontal position of the left box edge (default "0")
        :param STRING y: set vertical position of the top box edge (default "0")
        :param STRING width: set width of the box (default "0")
        :param STRING height: set height of the box (default "0")
        :param STRING color: set color of the box (default "black")
        :param STRING thickness: set the box thickness (default "3")
        :param BOOLEAN replace: replace color & alpha (default false)
        :param STRING box_source: use datas from bounding box in side data
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawbox

        """
        filter_node = FilterNode(
            name="drawbox",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "width": width,
                        "height": height,
                        "color": color,
                        "thickness": thickness,
                        "replace": replace,
                        "box_source": box_source,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def drawgraph(
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

        Draw a graph using input video metadata.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawgraph

        """
        filter_node = FilterNode(
            name="drawgraph",
            input_typings=tuple([StreamType.video]),
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

    def drawgrid(
        self,
        *,
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        width: STRING = Default("0"),
        height: STRING = Default("0"),
        color: STRING = Default("black"),
        thickness: STRING = Default("1"),
        replace: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored grid on the input video.

        Parameters:
        ----------

        :param STRING x: set horizontal offset (default "0")
        :param STRING y: set vertical offset (default "0")
        :param STRING width: set width of grid cell (default "0")
        :param STRING height: set height of grid cell (default "0")
        :param STRING color: set color of the grid (default "black")
        :param STRING thickness: set grid line thickness (default "1")
        :param BOOLEAN replace: replace color & alpha (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawgrid

        """
        filter_node = FilterNode(
            name="drawgrid",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "width": width,
                        "height": height,
                        "color": color,
                        "thickness": thickness,
                        "replace": replace,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def drawtext(
        self,
        *,
        fontfile: STRING = Default(None),
        text: STRING = Default(None),
        textfile: STRING = Default(None),
        fontcolor: COLOR = Default("black"),
        fontcolor_expr: STRING = Default(""),
        boxcolor: COLOR = Default("white"),
        bordercolor: COLOR = Default("black"),
        shadowcolor: COLOR = Default("black"),
        box: BOOLEAN = Default("false"),
        boxborderw: INT = Default("0"),
        line_spacing: INT = Default("0"),
        fontsize: STRING = Default(None),
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        shadowx: INT = Default("0"),
        shadowy: INT = Default("0"),
        borderw: INT = Default("0"),
        tabsize: INT = Default("4"),
        basetime: INT64 = Default("I64_MIN"),
        font: STRING = Default("Sans"),
        expansion: INT | Literal["none", "normal", "strftime"] | Default = Default("normal"),
        timecode: STRING = Default(None),
        tc24hmax: BOOLEAN = Default("false"),
        timecode_rate: RATIONAL = Default("0/1"),
        reload: INT = Default("0"),
        alpha: STRING = Default("1"),
        fix_bounds: BOOLEAN = Default("false"),
        start_number: INT = Default("0"),
        text_source: STRING = Default(None),
        ft_load_flags: FLAGS
        | Literal[
            "default",
            "no_scale",
            "no_hinting",
            "render",
            "no_bitmap",
            "vertical_layout",
            "force_autohint",
            "crop_bitmap",
            "pedantic",
            "ignore_global_advance_width",
            "no_recurse",
            "ignore_transform",
            "monochrome",
            "linear_design",
            "no_autohint",
        ]
        | Default = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw text on top of video frames using libfreetype library.

        Parameters:
        ----------

        :param STRING fontfile: set font file
        :param STRING text: set text
        :param STRING textfile: set text file
        :param COLOR fontcolor: set foreground color (default "black")
        :param STRING fontcolor_expr: set foreground color expression (default "")
        :param COLOR boxcolor: set box color (default "white")
        :param COLOR bordercolor: set border color (default "black")
        :param COLOR shadowcolor: set shadow color (default "black")
        :param BOOLEAN box: set box (default false)
        :param INT boxborderw: set box border width (from INT_MIN to INT_MAX) (default 0)
        :param INT line_spacing: set line spacing in pixels (from INT_MIN to INT_MAX) (default 0)
        :param STRING fontsize: set font size
        :param STRING x: set x expression (default "0")
        :param STRING y: set y expression (default "0")
        :param INT shadowx: set shadow x offset (from INT_MIN to INT_MAX) (default 0)
        :param INT shadowy: set shadow y offset (from INT_MIN to INT_MAX) (default 0)
        :param INT borderw: set border width (from INT_MIN to INT_MAX) (default 0)
        :param INT tabsize: set tab size (from 0 to INT_MAX) (default 4)
        :param INT64 basetime: set base time (from I64_MIN to I64_MAX) (default I64_MIN)
        :param STRING font: Font name (default "Sans")
        :param INT expansion: set the expansion mode (from 0 to 2) (default normal)
        :param STRING timecode: set initial timecode
        :param BOOLEAN tc24hmax: set 24 hours max (timecode only) (default false)
        :param RATIONAL timecode_rate: set rate (timecode only) (from 0 to INT_MAX) (default 0/1)
        :param INT reload: reload text file at specified frame interval (from 0 to INT_MAX) (default 0)
        :param STRING alpha: apply alpha while rendering (default "1")
        :param BOOLEAN fix_bounds: check and fix text coords to avoid clipping (default false)
        :param INT start_number: start frame number for n/frame_num variable (from 0 to INT_MAX) (default 0)
        :param STRING text_source: the source of text
        :param FLAGS ft_load_flags: set font loading flags for libfreetype (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawtext

        """
        filter_node = FilterNode(
            name="drawtext",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "fontfile": fontfile,
                        "text": text,
                        "textfile": textfile,
                        "fontcolor": fontcolor,
                        "fontcolor_expr": fontcolor_expr,
                        "boxcolor": boxcolor,
                        "bordercolor": bordercolor,
                        "shadowcolor": shadowcolor,
                        "box": box,
                        "boxborderw": boxborderw,
                        "line_spacing": line_spacing,
                        "fontsize": fontsize,
                        "x": x,
                        "y": y,
                        "shadowx": shadowx,
                        "shadowy": shadowy,
                        "borderw": borderw,
                        "tabsize": tabsize,
                        "basetime": basetime,
                        "font": font,
                        "expansion": expansion,
                        "timecode": timecode,
                        "tc24hmax": tc24hmax,
                        "timecode_rate": timecode_rate,
                        "reload": reload,
                        "alpha": alpha,
                        "fix_bounds": fix_bounds,
                        "start_number": start_number,
                        "text_source": text_source,
                        "ft_load_flags": ft_load_flags,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def edgedetect(
        self,
        *,
        high: DOUBLE = Default("0.196078"),
        low: DOUBLE = Default("0.0784314"),
        mode: INT | Literal["wires", "colormix", "canny"] | Default = Default("wires"),
        planes: FLAGS | Literal["y", "u", "v", "r", "g", "b"] | Default = Default("y+u+v+r+g+b"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect and draw edge.

        Parameters:
        ----------

        :param DOUBLE high: set high threshold (from 0 to 1) (default 0.196078)
        :param DOUBLE low: set low threshold (from 0 to 1) (default 0.0784314)
        :param INT mode: set mode (from 0 to 2) (default wires)
        :param FLAGS planes: set planes to filter (default y+u+v+r+g+b)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#edgedetect

        """
        filter_node = FilterNode(
            name="edgedetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "high": high,
                        "low": low,
                        "mode": mode,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def elbg(
        self,
        *,
        codebook_length: INT = Default("256"),
        nb_steps: INT = Default("1"),
        seed: INT64 = Default("-1"),
        pal8: BOOLEAN = Default("false"),
        use_alpha: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply posterize effect, using the ELBG algorithm.

        Parameters:
        ----------

        :param INT codebook_length: set codebook length (from 1 to INT_MAX) (default 256)
        :param INT nb_steps: set max number of steps used to compute the mapping (from 1 to INT_MAX) (default 1)
        :param INT64 seed: set the random seed (from -1 to UINT32_MAX) (default -1)
        :param BOOLEAN pal8: set the pal8 output (default false)
        :param BOOLEAN use_alpha: use alpha channel for mapping (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#elbg

        """
        filter_node = FilterNode(
            name="elbg",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "codebook_length": codebook_length,
                        "nb_steps": nb_steps,
                        "seed": seed,
                        "pal8": pal8,
                        "use_alpha": use_alpha,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def entropy(
        self,
        *,
        mode: INT | Literal["normal", "diff"] | Default = Default("normal"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure video frames entropy.

        Parameters:
        ----------

        :param INT mode: set kind of histogram entropy measurement (from 0 to 1) (default normal)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#entropy

        """
        filter_node = FilterNode(
            name="entropy",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def epx(self, *, n: INT = Default("3"), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using EPX algorithm.

        Parameters:
        ----------

        :param INT n: set scale factor (from 2 to 3) (default 3)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#epx

        """
        filter_node = FilterNode(
            name="epx",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def eq(
        self,
        *,
        contrast: STRING = Default("1.0"),
        brightness: STRING = Default("0.0"),
        saturation: STRING = Default("1.0"),
        gamma: STRING = Default("1.0"),
        gamma_r: STRING = Default("1.0"),
        gamma_g: STRING = Default("1.0"),
        gamma_b: STRING = Default("1.0"),
        gamma_weight: STRING = Default("1.0"),
        eval: INT | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust brightness, contrast, gamma, and saturation.

        Parameters:
        ----------

        :param STRING contrast: set the contrast adjustment, negative values give a negative image (default "1.0")
        :param STRING brightness: set the brightness adjustment (default "0.0")
        :param STRING saturation: set the saturation adjustment (default "1.0")
        :param STRING gamma: set the initial gamma value (default "1.0")
        :param STRING gamma_r: gamma value for red (default "1.0")
        :param STRING gamma_g: gamma value for green (default "1.0")
        :param STRING gamma_b: gamma value for blue (default "1.0")
        :param STRING gamma_weight: set the gamma weight which reduces the effect of gamma on bright areas (default "1.0")
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#eq

        """
        filter_node = FilterNode(
            name="eq",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "contrast": contrast,
                        "brightness": brightness,
                        "saturation": saturation,
                        "gamma": gamma,
                        "gamma_r": gamma_r,
                        "gamma_g": gamma_g,
                        "gamma_b": gamma_b,
                        "gamma_weight": gamma_weight,
                        "eval": eval,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def erosion(
        self,
        *,
        coordinates: INT = Default("255"),
        threshold0: INT = Default("65535"),
        threshold1: INT = Default("65535"),
        threshold2: INT = Default("65535"),
        threshold3: INT = Default("65535"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply erosion effect.

        Parameters:
        ----------

        :param INT coordinates: set coordinates (from 0 to 255) (default 255)
        :param INT threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param INT threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param INT threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param INT threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#erosion

        """
        filter_node = FilterNode(
            name="erosion",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "coordinates": coordinates,
                        "threshold0": threshold0,
                        "threshold1": threshold1,
                        "threshold2": threshold2,
                        "threshold3": threshold3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def estdif(
        self,
        *,
        mode: INT | Literal["frame", "field"] | Default = Default("field"),
        parity: INT | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: INT | Literal["all", "interlaced"] | Default = Default("all"),
        rslope: INT = Default("1"),
        redge: INT = Default("2"),
        ecost: FLOAT = Default("1"),
        mcost: FLOAT = Default("0.5"),
        dcost: FLOAT = Default("0.5"),
        interp: INT | Literal["2p", "4p", "6p"] | Default = Default("4p"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Edge Slope Tracing deinterlace.

        Parameters:
        ----------

        :param INT mode: specify the mode (from 0 to 1) (default field)
        :param INT parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param INT deint: specify which frames to deinterlace (from 0 to 1) (default all)
        :param INT rslope: specify the search radius for edge slope tracing (from 1 to 15) (default 1)
        :param INT redge: specify the search radius for best edge matching (from 0 to 15) (default 2)
        :param FLOAT ecost: specify the edge cost for edge matching (from 0 to 9) (default 1)
        :param FLOAT mcost: specify the middle cost for edge matching (from 0 to 1) (default 0.5)
        :param FLOAT dcost: specify the distance cost for edge matching (from 0 to 1) (default 0.5)
        :param INT interp: specify the type of interpolation (from 0 to 2) (default 4p)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#estdif

        """
        filter_node = FilterNode(
            name="estdif",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "parity": parity,
                        "deint": deint,
                        "rslope": rslope,
                        "redge": redge,
                        "ecost": ecost,
                        "mcost": mcost,
                        "dcost": dcost,
                        "interp": interp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def exposure(
        self, *, exposure: FLOAT = Default("0"), black: FLOAT = Default("0"), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Adjust exposure of the video stream.

        Parameters:
        ----------

        :param FLOAT exposure: set the exposure correction (from -3 to 3) (default 0)
        :param FLOAT black: set the black level correction (from -1 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#exposure

        """
        filter_node = FilterNode(
            name="exposure",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "exposure": exposure,
                        "black": black,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def extractplanes(
        self, *, planes: FLAGS | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default("r"), **kwargs: Any
    ) -> FilterNode:
        """

        Extract planes as grayscale frames.

        Parameters:
        ----------

        :param FLAGS planes: set planes (default r)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extractplanes

        """
        filter_node = FilterNode(
            name="extractplanes",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video] * len(planes.split("+"))),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def fade(
        self,
        *,
        type: INT | Literal["in", "out"] | Default = Default("in"),
        start_frame: INT = Default("0"),
        nb_frames: INT = Default("25"),
        alpha: BOOLEAN = Default("false"),
        start_time: DURATION = Default("0"),
        duration: DURATION = Default("0"),
        color: COLOR = Default("black"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fade in/out input video.

        Parameters:
        ----------

        :param INT type: set the fade direction (from 0 to 1) (default in)
        :param INT start_frame: Number of the first frame to which to apply the effect. (from 0 to INT_MAX) (default 0)
        :param INT nb_frames: Number of frames to which the effect should be applied. (from 1 to INT_MAX) (default 25)
        :param BOOLEAN alpha: fade alpha if it is available on the input (default false)
        :param DURATION start_time: Number of seconds of the beginning of the effect. (default 0)
        :param DURATION duration: Duration of the effect in seconds. (default 0)
        :param COLOR color: set color (default "black")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fade

        """
        filter_node = FilterNode(
            name="fade",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "type": type,
                        "start_frame": start_frame,
                        "nb_frames": nb_frames,
                        "alpha": alpha,
                        "start_time": start_time,
                        "duration": duration,
                        "color": color,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def feedback(
        self, _feedin: "VideoStream", *, x: INT = Default("0"), w: INT = Default("0"), **kwargs: Any
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
                self,
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

    def fftdnoiz(
        self,
        *,
        sigma: FLOAT = Default("1"),
        amount: FLOAT = Default("1"),
        block: INT = Default("32"),
        overlap: FLOAT = Default("0.5"),
        method: INT | Literal["wiener", "hard"] | Default = Default("wiener"),
        prev: INT = Default("0"),
        next: INT = Default("0"),
        planes: INT = Default("7"),
        window: INT
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
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise frames using 3D FFT.

        Parameters:
        ----------

        :param FLOAT sigma: set denoise strength (from 0 to 100) (default 1)
        :param FLOAT amount: set amount of denoising (from 0.01 to 1) (default 1)
        :param INT block: set block size (from 8 to 256) (default 32)
        :param FLOAT overlap: set block overlap (from 0.2 to 0.8) (default 0.5)
        :param INT method: set method of denoising (from 0 to 1) (default wiener)
        :param INT prev: set number of previous frames for temporal denoising (from 0 to 1) (default 0)
        :param INT next: set number of next frames for temporal denoising (from 0 to 1) (default 0)
        :param INT planes: set planes to filter (from 0 to 15) (default 7)
        :param INT window: set window function (from 0 to 20) (default hann)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz

        """
        filter_node = FilterNode(
            name="fftdnoiz",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigma": sigma,
                        "amount": amount,
                        "block": block,
                        "overlap": overlap,
                        "method": method,
                        "prev": prev,
                        "next": next,
                        "planes": planes,
                        "window": window,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fftfilt(
        self,
        *,
        dc_Y: INT = Default("0"),
        dc_U: INT = Default("0"),
        dc_V: INT = Default("0"),
        weight_Y: STRING = Default("1"),
        weight_U: STRING = Default(None),
        weight_V: STRING = Default(None),
        eval: INT | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply arbitrary expressions to pixels in frequency domain.

        Parameters:
        ----------

        :param INT dc_Y: adjust gain in Y plane (from 0 to 1000) (default 0)
        :param INT dc_U: adjust gain in U plane (from 0 to 1000) (default 0)
        :param INT dc_V: adjust gain in V plane (from 0 to 1000) (default 0)
        :param STRING weight_Y: set luminance expression in Y plane (default "1")
        :param STRING weight_U: set chrominance expression in U plane
        :param STRING weight_V: set chrominance expression in V plane
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fftfilt

        """
        filter_node = FilterNode(
            name="fftfilt",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dc_Y": dc_Y,
                        "dc_U": dc_U,
                        "dc_V": dc_V,
                        "weight_Y": weight_Y,
                        "weight_U": weight_U,
                        "weight_V": weight_V,
                        "eval": eval,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def field(self, *, type: INT | Literal["top", "bottom"] | Default = Default("top"), **kwargs: Any) -> "VideoStream":
        """

        Extract a field from the input video.

        Parameters:
        ----------

        :param INT type: set field type (top or bottom) (from 0 to 1) (default top)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#field

        """
        filter_node = FilterNode(
            name="field",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "type": type,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fieldhint(
        self,
        *,
        hint: STRING = Default(None),
        mode: INT | Literal["absolute", "relative", "pattern"] | Default = Default("absolute"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Field matching using hints.

        Parameters:
        ----------

        :param STRING hint: set hint file
        :param INT mode: set hint mode (from 0 to 2) (default absolute)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldhint

        """
        filter_node = FilterNode(
            name="fieldhint",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "hint": hint,
                        "mode": mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fieldorder(
        self,
        *,
        order: INT | Literal["bff", "tff"] | Default = Default("tff"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Set the field order.

        Parameters:
        ----------

        :param INT order: output field order (from 0 to 1) (default tff)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldorder

        """
        filter_node = FilterNode(
            name="fieldorder",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "order": order,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fifo(self, **kwargs: Any) -> "VideoStream":
        """

        Buffer input images and send them when they are requested.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#fifo_002c-afifo

        """
        filter_node = FilterNode(
            name="fifo",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def fillborders(
        self,
        *,
        left: INT = Default("0"),
        right: INT = Default("0"),
        top: INT = Default("0"),
        bottom: INT = Default("0"),
        mode: INT
        | Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | Default = Default("smear"),
        color: COLOR = Default("black"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill borders of the input video.

        Parameters:
        ----------

        :param INT left: set the left fill border (from 0 to INT_MAX) (default 0)
        :param INT right: set the right fill border (from 0 to INT_MAX) (default 0)
        :param INT top: set the top fill border (from 0 to INT_MAX) (default 0)
        :param INT bottom: set the bottom fill border (from 0 to INT_MAX) (default 0)
        :param INT mode: set the fill borders mode (from 0 to 6) (default smear)
        :param COLOR color: set the color for the fixed/fade mode (default "black")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fillborders

        """
        filter_node = FilterNode(
            name="fillborders",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "left": left,
                        "right": right,
                        "top": top,
                        "bottom": bottom,
                        "mode": mode,
                        "color": color,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def find_rect(
        self,
        *,
        object: STRING = Default(None),
        threshold: FLOAT = Default("0.5"),
        mipmaps: INT = Default("3"),
        xmin: INT = Default("0"),
        discard: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find a user specified object.

        Parameters:
        ----------

        :param STRING object: object bitmap filename
        :param FLOAT threshold: set threshold (from 0 to 1) (default 0.5)
        :param INT mipmaps: set mipmaps (from 1 to 5) (default 3)
        :param INT xmin: (from 0 to INT_MAX) (default 0)
        :param BOOLEAN discard: (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#find_005frect

        """
        filter_node = FilterNode(
            name="find_rect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "object": object,
                        "threshold": threshold,
                        "mipmaps": mipmaps,
                        "xmin": xmin,
                        "discard": discard,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def floodfill(
        self,
        *,
        x: INT = Default("0"),
        y: INT = Default("0"),
        s0: INT = Default("0"),
        s1: INT = Default("0"),
        s2: INT = Default("0"),
        s3: INT = Default("0"),
        d0: INT = Default("0"),
        d1: INT = Default("0"),
        d2: INT = Default("0"),
        d3: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill area with same color with another color.

        Parameters:
        ----------

        :param INT x: set pixel x coordinate (from 0 to 65535) (default 0)
        :param INT y: set pixel y coordinate (from 0 to 65535) (default 0)
        :param INT s0: set source #0 component value (from -1 to 65535) (default 0)
        :param INT s1: set source #1 component value (from -1 to 65535) (default 0)
        :param INT s2: set source #2 component value (from -1 to 65535) (default 0)
        :param INT s3: set source #3 component value (from -1 to 65535) (default 0)
        :param INT d0: set destination #0 component value (from 0 to 65535) (default 0)
        :param INT d1: set destination #1 component value (from 0 to 65535) (default 0)
        :param INT d2: set destination #2 component value (from 0 to 65535) (default 0)
        :param INT d3: set destination #3 component value (from 0 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#floodfill

        """
        filter_node = FilterNode(
            name="floodfill",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "s0": s0,
                        "s1": s1,
                        "s2": s2,
                        "s3": s3,
                        "d0": d0,
                        "d1": d1,
                        "d2": d2,
                        "d3": d3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def format(self, *, pix_fmts: STRING = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Convert the input video to one of the specified pixel formats.

        Parameters:
        ----------

        :param STRING pix_fmts: A '|'-separated list of pixel formats

        Ref: https://ffmpeg.org/ffmpeg-filters.html#format

        """
        filter_node = FilterNode(
            name="format",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "pix_fmts": pix_fmts,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fps(
        self,
        *,
        fps: STRING = Default("25"),
        start_time: DOUBLE = Default("DBL_MAX"),
        round: INT | Literal["zero", "inf", "down", "up", "near"] | Default = Default("near"),
        eof_action: INT | Literal["round", "pass"] | Default = Default("round"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force constant framerate.

        Parameters:
        ----------

        :param STRING fps: A string describing desired output framerate (default "25")
        :param DOUBLE start_time: Assume the first PTS should be this value. (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param INT round: set rounding method for timestamps (from 0 to 5) (default near)
        :param INT eof_action: action performed for last frame (from 0 to 1) (default round)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fps

        """
        filter_node = FilterNode(
            name="fps",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "fps": fps,
                        "start_time": start_time,
                        "round": round,
                        "eof_action": eof_action,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def framepack(
        self,
        _right: "VideoStream",
        *,
        format: INT | Literal["sbs", "tab", "frameseq", "lines", "columns"] | Default = Default("sbs"),
        **kwargs: Any,
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
                self,
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

    def framerate(
        self,
        *,
        fps: VIDEO_RATE = Default("50"),
        interp_start: INT = Default("15"),
        interp_end: INT = Default("240"),
        scene: DOUBLE = Default("8.2"),
        flags: FLAGS | Literal["scene_change_detect", "scd"] | Default = Default("scene_change_detect+scd"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Upsamples or downsamples progressive source between specified frame rates.

        Parameters:
        ----------

        :param VIDEO_RATE fps: required output frames per second rate (default "50")
        :param INT interp_start: point to start linear interpolation (from 0 to 255) (default 15)
        :param INT interp_end: point to end linear interpolation (from 0 to 255) (default 240)
        :param DOUBLE scene: scene change level (from 0 to 100) (default 8.2)
        :param FLAGS flags: set flags (default scene_change_detect+scd)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framerate

        """
        filter_node = FilterNode(
            name="framerate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "fps": fps,
                        "interp_start": interp_start,
                        "interp_end": interp_end,
                        "scene": scene,
                        "flags": flags,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def framestep(self, *, step: INT = Default("1"), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Select one frame every N frames.

        Parameters:
        ----------

        :param INT step: set frame step (from 1 to INT_MAX) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framestep

        """
        filter_node = FilterNode(
            name="framestep",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "step": step,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def freezedetect(self, *, n: DOUBLE = Default("0.001"), d: DURATION = Default("2"), **kwargs: Any) -> "VideoStream":
        """

        Detects frozen video input.

        Parameters:
        ----------

        :param DOUBLE n: set noise tolerance (from 0 to 1) (default 0.001)
        :param DURATION d: set minimum duration in seconds (default 2)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#freezedetect

        """
        filter_node = FilterNode(
            name="freezedetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                        "d": d,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def freezeframes(
        self,
        _replace: "VideoStream",
        *,
        first: INT64 = Default("0"),
        last: INT64 = Default("0"),
        replace: INT64 = Default("0"),
        **kwargs: Any,
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
                self,
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

    def frei0r(
        self,
        *,
        filter_name: STRING = Default(None),
        filter_params: STRING = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a frei0r effect.

        Parameters:
        ----------

        :param STRING filter_name:
        :param STRING filter_params:
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#frei0r

        """
        filter_node = FilterNode(
            name="frei0r",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filter_name": filter_name,
                        "filter_params": filter_params,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def fspp(
        self,
        *,
        quality: INT = Default("4"),
        qp: INT = Default("0"),
        strength: INT = Default("0"),
        use_bframe_qp: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Fast Simple Post-processing filter.

        Parameters:
        ----------

        :param INT quality: set quality (from 4 to 5) (default 4)
        :param INT qp: force a constant quantizer parameter (from 0 to 64) (default 0)
        :param INT strength: set filter strength (from -15 to 32) (default 0)
        :param BOOLEAN use_bframe_qp: use B-frames' QP (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fspp

        """
        filter_node = FilterNode(
            name="fspp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "quality": quality,
                        "qp": qp,
                        "strength": strength,
                        "use_bframe_qp": use_bframe_qp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def gblur(
        self,
        *,
        sigma: FLOAT = Default("0.5"),
        steps: INT = Default("1"),
        planes: INT = Default("15"),
        sigmaV: FLOAT = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Gaussian Blur filter.

        Parameters:
        ----------

        :param FLOAT sigma: set sigma (from 0 to 1024) (default 0.5)
        :param INT steps: set number of steps (from 1 to 6) (default 1)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT sigmaV: set vertical sigma (from -1 to 1024) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gblur

        """
        filter_node = FilterNode(
            name="gblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigma": sigma,
                        "steps": steps,
                        "planes": planes,
                        "sigmaV": sigmaV,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def geq(
        self,
        *,
        lum_expr: STRING = Default(None),
        cb_expr: STRING = Default(None),
        cr_expr: STRING = Default(None),
        alpha_expr: STRING = Default(None),
        red_expr: STRING = Default(None),
        green_expr: STRING = Default(None),
        blue_expr: STRING = Default(None),
        interpolation: INT | Literal["nearest", "n", "bilinear", "b"] | Default = Default("bilinear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply generic equation to each pixel.

        Parameters:
        ----------

        :param STRING lum_expr: set luminance expression
        :param STRING cb_expr: set chroma blue expression
        :param STRING cr_expr: set chroma red expression
        :param STRING alpha_expr: set alpha expression
        :param STRING red_expr: set red expression
        :param STRING green_expr: set green expression
        :param STRING blue_expr: set blue expression
        :param INT interpolation: set interpolation method (from 0 to 1) (default bilinear)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#geq

        """
        filter_node = FilterNode(
            name="geq",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "lum_expr": lum_expr,
                        "cb_expr": cb_expr,
                        "cr_expr": cr_expr,
                        "alpha_expr": alpha_expr,
                        "red_expr": red_expr,
                        "green_expr": green_expr,
                        "blue_expr": blue_expr,
                        "interpolation": interpolation,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def gradfun(
        self,
        *,
        strength: FLOAT = Default("1.2"),
        radius: INT = Default("16"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Debands video quickly using gradients.

        Parameters:
        ----------

        :param FLOAT strength: The maximum amount by which the filter will change any one pixel. (from 0.51 to 64) (default 1.2)
        :param INT radius: The neighborhood to fit the gradient to. (from 4 to 32) (default 16)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gradfun

        """
        filter_node = FilterNode(
            name="gradfun",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "strength": strength,
                        "radius": radius,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def graphmonitor(
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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#graphmonitor

        """
        filter_node = FilterNode(
            name="graphmonitor",
            input_typings=tuple([StreamType.video]),
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

    def grayworld(self, *, enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Adjust white balance using LAB gray world algorithm

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#grayworld

        """
        filter_node = FilterNode(
            name="grayworld",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def greyedge(
        self,
        *,
        difford: INT = Default("1"),
        minknorm: INT = Default("1"),
        sigma: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Estimates scene illumination by grey edge assumption.

        Parameters:
        ----------

        :param INT difford: set differentiation order (from 0 to 2) (default 1)
        :param INT minknorm: set Minkowski norm (from 0 to 20) (default 1)
        :param DOUBLE sigma: set sigma (from 0 to 1024) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#greyedge

        """
        filter_node = FilterNode(
            name="greyedge",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "difford": difford,
                        "minknorm": minknorm,
                        "sigma": sigma,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def haldclut(
        self,
        _clut: "VideoStream",
        *,
        clut: INT | Literal["first", "all"] | Default = Default("all"),
        interp: INT
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("tetrahedral"),
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def hflip(self, *, enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Horizontally flip the input video.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hflip

        """
        filter_node = FilterNode(
            name="hflip",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def histeq(
        self,
        *,
        strength: FLOAT = Default("0.2"),
        intensity: FLOAT = Default("0.21"),
        antibanding: INT | Literal["none", "weak", "strong"] | Default = Default("none"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply global color histogram equalization.

        Parameters:
        ----------

        :param FLOAT strength: set the strength (from 0 to 1) (default 0.2)
        :param FLOAT intensity: set the intensity (from 0 to 1) (default 0.21)
        :param INT antibanding: set the antibanding level (from 0 to 2) (default none)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#histeq

        """
        filter_node = FilterNode(
            name="histeq",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "strength": strength,
                        "intensity": intensity,
                        "antibanding": antibanding,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def histogram(
        self,
        *,
        level_height: INT = Default("200"),
        scale_height: INT = Default("12"),
        display_mode: INT | Literal["overlay", "parade", "stack"] | Default = Default("stack"),
        levels_mode: INT | Literal["linear", "logarithmic"] | Default = Default("linear"),
        components: INT = Default("7"),
        fgopacity: FLOAT = Default("0.7"),
        bgopacity: FLOAT = Default("0.5"),
        colors_mode: INT
        | Literal[
            "whiteonblack",
            "blackonwhite",
            "whiteongray",
            "blackongray",
            "coloronblack",
            "coloronwhite",
            "colorongray",
            "blackoncolor",
            "whiteoncolor",
            "grayoncolor",
        ]
        | Default = Default("whiteonblack"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and draw a histogram.

        Parameters:
        ----------

        :param INT level_height: set level height (from 50 to 2048) (default 200)
        :param INT scale_height: set scale height (from 0 to 40) (default 12)
        :param INT display_mode: set display mode (from 0 to 2) (default stack)
        :param INT levels_mode: set levels mode (from 0 to 1) (default linear)
        :param INT components: set color components to display (from 1 to 15) (default 7)
        :param FLOAT fgopacity: set foreground opacity (from 0 to 1) (default 0.7)
        :param FLOAT bgopacity: set background opacity (from 0 to 1) (default 0.5)
        :param INT colors_mode: set colors mode (from 0 to 9) (default whiteonblack)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#histogram

        """
        filter_node = FilterNode(
            name="histogram",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "level_height": level_height,
                        "scale_height": scale_height,
                        "display_mode": display_mode,
                        "levels_mode": levels_mode,
                        "components": components,
                        "fgopacity": fgopacity,
                        "bgopacity": bgopacity,
                        "colors_mode": colors_mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hqdn3d(
        self,
        *,
        luma_spatial: DOUBLE = Default("0"),
        chroma_spatial: DOUBLE = Default("0"),
        luma_tmp: DOUBLE = Default("0"),
        chroma_tmp: DOUBLE = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a High Quality 3D Denoiser.

        Parameters:
        ----------

        :param DOUBLE luma_spatial: spatial luma strength (from 0 to DBL_MAX) (default 0)
        :param DOUBLE chroma_spatial: spatial chroma strength (from 0 to DBL_MAX) (default 0)
        :param DOUBLE luma_tmp: temporal luma strength (from 0 to DBL_MAX) (default 0)
        :param DOUBLE chroma_tmp: temporal chroma strength (from 0 to DBL_MAX) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqdn3d

        """
        filter_node = FilterNode(
            name="hqdn3d",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_spatial": luma_spatial,
                        "chroma_spatial": chroma_spatial,
                        "luma_tmp": luma_tmp,
                        "chroma_tmp": chroma_tmp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hqx(self, *, n: INT = Default("3"), **kwargs: Any) -> "VideoStream":
        """

        Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

        Parameters:
        ----------

        :param INT n: set scale factor (from 2 to 4) (default 3)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqx

        """
        filter_node = FilterNode(
            name="hqx",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hsvhold(
        self,
        *,
        hue: FLOAT = Default("0"),
        sat: FLOAT = Default("0"),
        val: FLOAT = Default("0"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into gray.

        Parameters:
        ----------

        :param FLOAT hue: set the hue value (from -360 to 360) (default 0)
        :param FLOAT sat: set the saturation value (from -1 to 1) (default 0)
        :param FLOAT val: set the value value (from -1 to 1) (default 0)
        :param FLOAT similarity: set the hsvhold similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the hsvhold blend value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvhold

        """
        filter_node = FilterNode(
            name="hsvhold",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "hue": hue,
                        "sat": sat,
                        "val": val,
                        "similarity": similarity,
                        "blend": blend,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hsvkey(
        self,
        *,
        hue: FLOAT = Default("0"),
        sat: FLOAT = Default("0"),
        val: FLOAT = Default("0"),
        similarity: FLOAT = Default("0.01"),
        blend: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param FLOAT hue: set the hue value (from -360 to 360) (default 0)
        :param FLOAT sat: set the saturation value (from -1 to 1) (default 0)
        :param FLOAT val: set the value value (from -1 to 1) (default 0)
        :param FLOAT similarity: set the hsvkey similarity value (from 1e-05 to 1) (default 0.01)
        :param FLOAT blend: set the hsvkey blend value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvkey

        """
        filter_node = FilterNode(
            name="hsvkey",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "hue": hue,
                        "sat": sat,
                        "val": val,
                        "similarity": similarity,
                        "blend": blend,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hue(
        self,
        *,
        h: STRING = Default(None),
        s: STRING = Default("1"),
        H: STRING = Default(None),
        b: STRING = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the hue and saturation of the input video.

        Parameters:
        ----------

        :param STRING h: set the hue angle degrees expression
        :param STRING s: set the saturation expression (default "1")
        :param STRING H: set the hue angle radians expression
        :param STRING b: set the brightness expression (default "0")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hue

        """
        filter_node = FilterNode(
            name="hue",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "h": h,
                        "s": s,
                        "H": H,
                        "b": b,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def huesaturation(
        self,
        *,
        hue: FLOAT = Default("0"),
        saturation: FLOAT = Default("0"),
        intensity: FLOAT = Default("0"),
        colors: FLAGS | Literal["r", "y", "g", "c", "b", "m", "a"] | Default = Default("r+y+g+c+b+m+a"),
        strength: FLOAT = Default("1"),
        rw: FLOAT = Default("0.333"),
        gw: FLOAT = Default("0.334"),
        bw: FLOAT = Default("0.333"),
        lightness: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply hue-saturation-intensity adjustments.

        Parameters:
        ----------

        :param FLOAT hue: set the hue shift (from -180 to 180) (default 0)
        :param FLOAT saturation: set the saturation shift (from -1 to 1) (default 0)
        :param FLOAT intensity: set the intensity shift (from -1 to 1) (default 0)
        :param FLAGS colors: set colors range (default r+y+g+c+b+m+a)
        :param FLOAT strength: set the filtering strength (from 0 to 100) (default 1)
        :param FLOAT rw: set the red weight (from 0 to 1) (default 0.333)
        :param FLOAT gw: set the green weight (from 0 to 1) (default 0.334)
        :param FLOAT bw: set the blue weight (from 0 to 1) (default 0.333)
        :param BOOLEAN lightness: set the preserve lightness (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#huesaturation

        """
        filter_node = FilterNode(
            name="huesaturation",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "hue": hue,
                        "saturation": saturation,
                        "intensity": intensity,
                        "colors": colors,
                        "strength": strength,
                        "rw": rw,
                        "gw": gw,
                        "bw": bw,
                        "lightness": lightness,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hwdownload(self, **kwargs: Any) -> "VideoStream":
        """

        Download a hardware frame to a normal frame

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwdownload

        """
        filter_node = FilterNode(
            name="hwdownload",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def hwmap(
        self,
        *,
        mode: FLAGS | Literal["read", "write", "overwrite", "direct"] | Default = Default("read+write"),
        derive_device: STRING = Default(None),
        reverse: INT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Map hardware frames

        Parameters:
        ----------

        :param FLAGS mode: Frame mapping mode (default read+write)
        :param STRING derive_device: Derive a new device of this type
        :param INT reverse: Map in reverse (create and allocate in the sink) (from 0 to 1) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwmap

        """
        filter_node = FilterNode(
            name="hwmap",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "derive_device": derive_device,
                        "reverse": reverse,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hwupload(self, *, derive_device: STRING = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Upload a normal frame to a hardware frame

        Parameters:
        ----------

        :param STRING derive_device: Derive a new device of this type

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload

        """
        filter_node = FilterNode(
            name="hwupload",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "derive_device": derive_device,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def hysteresis(
        self,
        _alt: "VideoStream",
        *,
        planes: INT = Default("15"),
        threshold: INT = Default("0"),
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _reference: "VideoStream",
        *,
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def idet(
        self,
        *,
        intl_thres: FLOAT = Default("1.04"),
        prog_thres: FLOAT = Default("1.5"),
        rep_thres: FLOAT = Default("3"),
        half_life: FLOAT = Default("0"),
        analyze_interlaced_flag: INT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Interlace detect Filter.

        Parameters:
        ----------

        :param FLOAT intl_thres: set interlacing threshold (from -1 to FLT_MAX) (default 1.04)
        :param FLOAT prog_thres: set progressive threshold (from -1 to FLT_MAX) (default 1.5)
        :param FLOAT rep_thres: set repeat threshold (from -1 to FLT_MAX) (default 3)
        :param FLOAT half_life: half life of cumulative statistics (from -1 to INT_MAX) (default 0)
        :param INT analyze_interlaced_flag: set number of frames to use to determine if the interlace flag is accurate (from 0 to INT_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#idet

        """
        filter_node = FilterNode(
            name="idet",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "intl_thres": intl_thres,
                        "prog_thres": prog_thres,
                        "rep_thres": rep_thres,
                        "half_life": half_life,
                        "analyze_interlaced_flag": analyze_interlaced_flag,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def il(
        self,
        *,
        luma_mode: INT | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        chroma_mode: INT | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        alpha_mode: INT | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        luma_swap: BOOLEAN = Default("false"),
        chroma_swap: BOOLEAN = Default("false"),
        alpha_swap: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterleave or interleave fields.

        Parameters:
        ----------

        :param INT luma_mode: select luma mode (from 0 to 2) (default none)
        :param INT chroma_mode: select chroma mode (from 0 to 2) (default none)
        :param INT alpha_mode: select alpha mode (from 0 to 2) (default none)
        :param BOOLEAN luma_swap: swap luma fields (default false)
        :param BOOLEAN chroma_swap: swap chroma fields (default false)
        :param BOOLEAN alpha_swap: swap alpha fields (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#il

        """
        filter_node = FilterNode(
            name="il",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_mode": luma_mode,
                        "chroma_mode": chroma_mode,
                        "alpha_mode": alpha_mode,
                        "luma_swap": luma_swap,
                        "chroma_swap": chroma_swap,
                        "alpha_swap": alpha_swap,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def inflate(
        self,
        *,
        threshold0: INT = Default("65535"),
        threshold1: INT = Default("65535"),
        threshold2: INT = Default("65535"),
        threshold3: INT = Default("65535"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply inflate effect.

        Parameters:
        ----------

        :param INT threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param INT threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param INT threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param INT threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#inflate

        """
        filter_node = FilterNode(
            name="inflate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold0": threshold0,
                        "threshold1": threshold1,
                        "threshold2": threshold2,
                        "threshold3": threshold3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def interlace(
        self,
        *,
        scan: INT | Literal["tff", "bff"] | Default = Default("tff"),
        lowpass: INT | Literal["off", "linear", "complex"] | Default = Default("linear"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert progressive video into interlaced.

        Parameters:
        ----------

        :param INT scan: scanning mode (from 0 to 1) (default tff)
        :param INT lowpass: set vertical low-pass filter (from 0 to 2) (default linear)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#interlace

        """
        filter_node = FilterNode(
            name="interlace",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "scan": scan,
                        "lowpass": lowpass,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def kerndeint(
        self,
        *,
        thresh: INT = Default("10"),
        map: BOOLEAN = Default("false"),
        order: BOOLEAN = Default("false"),
        sharp: BOOLEAN = Default("false"),
        twoway: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kernel deinterlacing to the input.

        Parameters:
        ----------

        :param INT thresh: set the threshold (from 0 to 255) (default 10)
        :param BOOLEAN map: set the map (default false)
        :param BOOLEAN order: set the order (default false)
        :param BOOLEAN sharp: set sharpening (default false)
        :param BOOLEAN twoway: set twoway (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#kerndeint

        """
        filter_node = FilterNode(
            name="kerndeint",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "thresh": thresh,
                        "map": map,
                        "order": order,
                        "sharp": sharp,
                        "twoway": twoway,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def kirsch(
        self,
        *,
        planes: INT = Default("15"),
        scale: FLOAT = Default("1"),
        delta: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kirsch operator.

        Parameters:
        ----------

        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT scale: set scale (from 0 to 65535) (default 1)
        :param FLOAT delta: set delta (from -65535 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#kirsch

        """
        filter_node = FilterNode(
            name="kirsch",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lagfun(
        self,
        *,
        decay: FLOAT = Default("0.95"),
        planes: FLAGS = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Slowly update darker pixels.

        Parameters:
        ----------

        :param FLOAT decay: set decay (from 0 to 1) (default 0.95)
        :param FLAGS planes: set what planes to filter (default F)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lagfun

        """
        filter_node = FilterNode(
            name="lagfun",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "decay": decay,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def latency(self, *, enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Report video filtering latency.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency

        """
        filter_node = FilterNode(
            name="latency",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def lenscorrection(
        self,
        *,
        cx: DOUBLE = Default("0.5"),
        cy: DOUBLE = Default("0.5"),
        k1: DOUBLE = Default("0"),
        k2: DOUBLE = Default("0"),
        i: INT | Literal["nearest", "bilinear"] | Default = Default("nearest"),
        fc: COLOR = Default("black@0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rectify the image by correcting for lens distortion.

        Parameters:
        ----------

        :param DOUBLE cx: set relative center x (from 0 to 1) (default 0.5)
        :param DOUBLE cy: set relative center y (from 0 to 1) (default 0.5)
        :param DOUBLE k1: set quadratic distortion factor (from -1 to 1) (default 0)
        :param DOUBLE k2: set double quadratic distortion factor (from -1 to 1) (default 0)
        :param INT i: set interpolation type (from 0 to 64) (default nearest)
        :param COLOR fc: set the color of the unmapped pixels (default "black@0")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lenscorrection

        """
        filter_node = FilterNode(
            name="lenscorrection",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cx": cx,
                        "cy": cy,
                        "k1": k1,
                        "k2": k2,
                        "i": i,
                        "fc": fc,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def libvmaf(
        self,
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
        **kwargs: Any,
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
                self,
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

    def limiter(
        self,
        *,
        min: INT = Default("0"),
        max: INT = Default("65535"),
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Limit pixels components to the specified range.

        Parameters:
        ----------

        :param INT min: set min value (from 0 to 65535) (default 0)
        :param INT max: set max value (from 0 to 65535) (default 65535)
        :param INT planes: set planes (from 0 to 15) (default 15)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#limiter

        """
        filter_node = FilterNode(
            name="limiter",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "min": min,
                        "max": max,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def loop(
        self, *, loop: INT = Default("0"), size: INT64 = Default("0"), start: INT64 = Default("0"), **kwargs: Any
    ) -> "VideoStream":
        """

        Loop video frames.

        Parameters:
        ----------

        :param INT loop: number of loops (from -1 to INT_MAX) (default 0)
        :param INT64 size: max number of frames to loop (from 0 to 32767) (default 0)
        :param INT64 start: set the loop start frame (from 0 to I64_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#loop

        """
        filter_node = FilterNode(
            name="loop",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def lumakey(
        self,
        *,
        threshold: DOUBLE = Default("0"),
        tolerance: DOUBLE = Default("0.01"),
        softness: DOUBLE = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain luma into transparency.

        Parameters:
        ----------

        :param DOUBLE threshold: set the threshold value (from 0 to 1) (default 0)
        :param DOUBLE tolerance: set the tolerance value (from 0 to 1) (default 0.01)
        :param DOUBLE softness: set the softness value (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lumakey

        """
        filter_node = FilterNode(
            name="lumakey",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold": threshold,
                        "tolerance": tolerance,
                        "softness": softness,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lut(
        self,
        *,
        c0: STRING = Default("clipval"),
        c1: STRING = Default("clipval"),
        c2: STRING = Default("clipval"),
        c3: STRING = Default("clipval"),
        y: STRING = Default("clipval"),
        u: STRING = Default("clipval"),
        v: STRING = Default("clipval"),
        r: STRING = Default("clipval"),
        g: STRING = Default("clipval"),
        b: STRING = Default("clipval"),
        a: STRING = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB/YUV input video.

        Parameters:
        ----------

        :param STRING c0: set component #0 expression (default "clipval")
        :param STRING c1: set component #1 expression (default "clipval")
        :param STRING c2: set component #2 expression (default "clipval")
        :param STRING c3: set component #3 expression (default "clipval")
        :param STRING y: set Y expression (default "clipval")
        :param STRING u: set U expression (default "clipval")
        :param STRING v: set V expression (default "clipval")
        :param STRING r: set R expression (default "clipval")
        :param STRING g: set G expression (default "clipval")
        :param STRING b: set B expression (default "clipval")
        :param STRING a: set A expression (default "clipval")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lut",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "c0": c0,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "y": y,
                        "u": u,
                        "v": v,
                        "r": r,
                        "g": g,
                        "b": b,
                        "a": a,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lut1d(
        self,
        *,
        file: STRING = Default(None),
        interp: INT | Literal["nearest", "linear", "cosine", "cubic", "spline"] | Default = Default("linear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 1D LUT.

        Parameters:
        ----------

        :param STRING file: set 1D LUT file name
        :param INT interp: select interpolation mode (from 0 to 4) (default linear)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut1d

        """
        filter_node = FilterNode(
            name="lut1d",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "file": file,
                        "interp": interp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lut2(
        self,
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
        **kwargs: Any,
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
                self,
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

    def lut3d(
        self,
        *,
        file: STRING = Default(None),
        clut: INT | Literal["first", "all"] | Default = Default("all"),
        interp: INT
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("tetrahedral"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 3D LUT.

        Parameters:
        ----------

        :param STRING file: set 3D LUT file name
        :param INT clut: when to process CLUT (from 0 to 1) (default all)
        :param INT interp: select interpolation mode (from 0 to 4) (default tetrahedral)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut3d

        """
        filter_node = FilterNode(
            name="lut3d",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "file": file,
                        "clut": clut,
                        "interp": interp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lutrgb(
        self,
        *,
        c0: STRING = Default("clipval"),
        c1: STRING = Default("clipval"),
        c2: STRING = Default("clipval"),
        c3: STRING = Default("clipval"),
        y: STRING = Default("clipval"),
        u: STRING = Default("clipval"),
        v: STRING = Default("clipval"),
        r: STRING = Default("clipval"),
        g: STRING = Default("clipval"),
        b: STRING = Default("clipval"),
        a: STRING = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB input video.

        Parameters:
        ----------

        :param STRING c0: set component #0 expression (default "clipval")
        :param STRING c1: set component #1 expression (default "clipval")
        :param STRING c2: set component #2 expression (default "clipval")
        :param STRING c3: set component #3 expression (default "clipval")
        :param STRING y: set Y expression (default "clipval")
        :param STRING u: set U expression (default "clipval")
        :param STRING v: set V expression (default "clipval")
        :param STRING r: set R expression (default "clipval")
        :param STRING g: set G expression (default "clipval")
        :param STRING b: set B expression (default "clipval")
        :param STRING a: set A expression (default "clipval")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lutrgb",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "c0": c0,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "y": y,
                        "u": u,
                        "v": v,
                        "r": r,
                        "g": g,
                        "b": b,
                        "a": a,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lutyuv(
        self,
        *,
        c0: STRING = Default("clipval"),
        c1: STRING = Default("clipval"),
        c2: STRING = Default("clipval"),
        c3: STRING = Default("clipval"),
        y: STRING = Default("clipval"),
        u: STRING = Default("clipval"),
        v: STRING = Default("clipval"),
        r: STRING = Default("clipval"),
        g: STRING = Default("clipval"),
        b: STRING = Default("clipval"),
        a: STRING = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the YUV input video.

        Parameters:
        ----------

        :param STRING c0: set component #0 expression (default "clipval")
        :param STRING c1: set component #1 expression (default "clipval")
        :param STRING c2: set component #2 expression (default "clipval")
        :param STRING c3: set component #3 expression (default "clipval")
        :param STRING y: set Y expression (default "clipval")
        :param STRING u: set U expression (default "clipval")
        :param STRING v: set V expression (default "clipval")
        :param STRING r: set R expression (default "clipval")
        :param STRING g: set G expression (default "clipval")
        :param STRING b: set B expression (default "clipval")
        :param STRING a: set A expression (default "clipval")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lutyuv",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "c0": c0,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "y": y,
                        "u": u,
                        "v": v,
                        "r": r,
                        "g": g,
                        "b": b,
                        "a": a,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def maskedclamp(
        self,
        _dark: "VideoStream",
        _bright: "VideoStream",
        *,
        undershoot: INT = Default("0"),
        overshoot: INT = Default("0"),
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _filter1: "VideoStream",
        _filter2: "VideoStream",
        *,
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _overlay: "VideoStream",
        _mask: "VideoStream",
        *,
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _filter1: "VideoStream",
        _filter2: "VideoStream",
        *,
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _reference: "VideoStream",
        *,
        threshold: INT = Default("1"),
        planes: INT = Default("15"),
        mode: INT | Literal["abs", "diff"] | Default = Default("abs"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def maskfun(
        self,
        *,
        low: INT = Default("10"),
        high: INT = Default("10"),
        planes: INT = Default("15"),
        fill: INT = Default("0"),
        sum: INT = Default("10"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Create Mask.

        Parameters:
        ----------

        :param INT low: set low threshold (from 0 to 65535) (default 10)
        :param INT high: set high threshold (from 0 to 65535) (default 10)
        :param INT planes: set planes (from 0 to 15) (default 15)
        :param INT fill: set fill value (from 0 to 65535) (default 0)
        :param INT sum: set sum value (from 0 to 65535) (default 10)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskfun

        """
        filter_node = FilterNode(
            name="maskfun",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "low": low,
                        "high": high,
                        "planes": planes,
                        "fill": fill,
                        "sum": sum,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def median(
        self,
        *,
        radius: INT = Default("1"),
        planes: INT = Default("15"),
        radiusV: INT = Default("0"),
        percentile: FLOAT = Default("0.5"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Median filter.

        Parameters:
        ----------

        :param INT radius: set median radius (from 1 to 127) (default 1)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param INT radiusV: set median vertical radius (from 0 to 127) (default 0)
        :param FLOAT percentile: set median percentile (from 0 to 1) (default 0.5)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#median

        """
        filter_node = FilterNode(
            name="median",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "radius": radius,
                        "planes": planes,
                        "radiusV": radiusV,
                        "percentile": percentile,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def mestimate(
        self,
        *,
        method: INT
        | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | Default = Default("esa"),
        mb_size: INT = Default("16"),
        search_param: INT = Default("7"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate motion vectors.

        Parameters:
        ----------

        :param INT method: motion estimation method (from 1 to 9) (default esa)
        :param INT mb_size: macroblock size (from 8 to INT_MAX) (default 16)
        :param INT search_param: search parameter (from 4 to INT_MAX) (default 7)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mestimate

        """
        filter_node = FilterNode(
            name="mestimate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "method": method,
                        "mb_size": mb_size,
                        "search_param": search_param,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def metadata(
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
    ) -> "VideoStream":
        """

        Manipulate video frame metadata.

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
            name="metadata",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def midequalizer(
        self, _in1: "VideoStream", *, planes: INT = Default("15"), enable: str = Default(None), **kwargs: Any
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
                self,
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

    def minterpolate(
        self,
        *,
        fps: VIDEO_RATE = Default("60"),
        mi_mode: INT | Literal["dup", "blend", "mci"] | Default = Default("mci"),
        mc_mode: INT | Literal["obmc", "aobmc"] | Default = Default("obmc"),
        me_mode: INT | Literal["bidir", "bilat"] | Default = Default("bilat"),
        me: INT
        | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | Default = Default("epzs"),
        mb_size: INT = Default("16"),
        search_param: INT = Default("32"),
        vsbmc: INT = Default("0"),
        scd: INT | Literal["none", "fdiff"] | Default = Default("fdiff"),
        scd_threshold: DOUBLE = Default("10"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Frame rate conversion using Motion Interpolation.

        Parameters:
        ----------

        :param VIDEO_RATE fps: output's frame rate (default "60")
        :param INT mi_mode: motion interpolation mode (from 0 to 2) (default mci)
        :param INT mc_mode: motion compensation mode (from 0 to 1) (default obmc)
        :param INT me_mode: motion estimation mode (from 0 to 1) (default bilat)
        :param INT me: motion estimation method (from 1 to 9) (default epzs)
        :param INT mb_size: macroblock size (from 4 to 16) (default 16)
        :param INT search_param: search parameter (from 4 to INT_MAX) (default 32)
        :param INT vsbmc: variable-size block motion compensation (from 0 to 1) (default 0)
        :param INT scd: scene change detection method (from 0 to 1) (default fdiff)
        :param DOUBLE scd_threshold: scene change threshold (from 0 to 100) (default 10)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#minterpolate

        """
        filter_node = FilterNode(
            name="minterpolate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "fps": fps,
                        "mi_mode": mi_mode,
                        "mc_mode": mc_mode,
                        "me_mode": me_mode,
                        "me": me,
                        "mb_size": mb_size,
                        "search_param": search_param,
                        "vsbmc": vsbmc,
                        "scd": scd,
                        "scd_threshold": scd_threshold,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def monochrome(
        self,
        *,
        cb: FLOAT = Default("0"),
        cr: FLOAT = Default("0"),
        size: FLOAT = Default("1"),
        high: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert video to gray using custom color filter.

        Parameters:
        ----------

        :param FLOAT cb: set the chroma blue spot (from -1 to 1) (default 0)
        :param FLOAT cr: set the chroma red spot (from -1 to 1) (default 0)
        :param FLOAT size: set the color filter size (from 0.1 to 10) (default 1)
        :param FLOAT high: set the highlights strength (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#monochrome

        """
        filter_node = FilterNode(
            name="monochrome",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "cb": cb,
                        "cr": cr,
                        "size": size,
                        "high": high,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def morpho(
        self,
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
        **kwargs: Any,
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
                self,
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

    def mpdecimate(
        self,
        *,
        max: INT = Default("0"),
        hi: INT = Default("768"),
        lo: INT = Default("320"),
        frac: FLOAT = Default("0.33"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove near-duplicate frames.

        Parameters:
        ----------

        :param INT max: set the maximum number of consecutive dropped frames (positive), or the minimum interval between dropped frames (negative) (from INT_MIN to INT_MAX) (default 0)
        :param INT hi: set high dropping threshold (from INT_MIN to INT_MAX) (default 768)
        :param INT lo: set low dropping threshold (from INT_MIN to INT_MAX) (default 320)
        :param FLOAT frac: set fraction dropping threshold (from 0 to 1) (default 0.33)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mpdecimate

        """
        filter_node = FilterNode(
            name="mpdecimate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "max": max,
                        "hi": hi,
                        "lo": lo,
                        "frac": frac,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def msad(
        self,
        _reference: "VideoStream",
        *,
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
        _factor: "VideoStream",
        *,
        scale: FLOAT = Default("1"),
        offset: FLOAT = Default("0.5"),
        planes: FLAGS = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def negate(
        self,
        *,
        components: FLAGS | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default("y+u+v+r+g+b"),
        negate_alpha: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Negate input video.

        Parameters:
        ----------

        :param FLAGS components: set components to negate (default y+u+v+r+g+b)
        :param BOOLEAN negate_alpha: (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#negate

        """
        filter_node = FilterNode(
            name="negate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "components": components,
                        "negate_alpha": negate_alpha,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def nlmeans(
        self,
        *,
        s: DOUBLE = Default("1"),
        p: INT = Default("7"),
        pc: INT = Default("0"),
        r: INT = Default("15"),
        rc: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Non-local means denoiser.

        Parameters:
        ----------

        :param DOUBLE s: denoising strength (from 1 to 30) (default 1)
        :param INT p: patch size (from 0 to 99) (default 7)
        :param INT pc: patch size for chroma planes (from 0 to 99) (default 0)
        :param INT r: research window (from 0 to 99) (default 15)
        :param INT rc: research window for chroma planes (from 0 to 99) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans

        """
        filter_node = FilterNode(
            name="nlmeans",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "s": s,
                        "p": p,
                        "pc": pc,
                        "r": r,
                        "rc": rc,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def nnedi(
        self,
        *,
        weights: STRING = Default("nnedi3_weights.bin"),
        deint: INT | Literal["all", "interlaced"] | Default = Default("all"),
        field: INT | Literal["af", "a", "t", "b", "tf", "bf"] | Default = Default("a"),
        planes: INT = Default("7"),
        nsize: INT | Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"] | Default = Default("s32x4"),
        nns: INT | Literal["n16", "n32", "n64", "n128", "n256"] | Default = Default("n32"),
        qual: INT | Literal["fast", "slow"] | Default = Default("fast"),
        etype: INT | Literal["a", "abs", "s", "mse"] | Default = Default("a"),
        pscrn: INT | Literal["none", "original", "new", "new2", "new3"] | Default = Default("new"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply neural network edge directed interpolation intra-only deinterlacer.

        Parameters:
        ----------

        :param STRING weights: set weights file (default "nnedi3_weights.bin")
        :param INT deint: set which frames to deinterlace (from 0 to 1) (default all)
        :param INT field: set mode of operation (from -2 to 3) (default a)
        :param INT planes: set which planes to process (from 0 to 15) (default 7)
        :param INT nsize: set size of local neighborhood around each pixel, used by the predictor neural network (from 0 to 6) (default s32x4)
        :param INT nns: set number of neurons in predictor neural network (from 0 to 4) (default n32)
        :param INT qual: set quality (from 1 to 2) (default fast)
        :param INT etype: set which set of weights to use in the predictor (from 0 to 1) (default a)
        :param INT pscrn: set prescreening (from 0 to 4) (default new)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nnedi

        """
        filter_node = FilterNode(
            name="nnedi",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "weights": weights,
                        "deint": deint,
                        "field": field,
                        "planes": planes,
                        "nsize": nsize,
                        "nns": nns,
                        "qual": qual,
                        "etype": etype,
                        "pscrn": pscrn,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def noformat(self, *, pix_fmts: STRING = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

        Parameters:
        ----------

        :param STRING pix_fmts: A '|'-separated list of pixel formats

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noformat

        """
        filter_node = FilterNode(
            name="noformat",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "pix_fmts": pix_fmts,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def noise(
        self,
        *,
        all_seed: INT = Default("-1"),
        all_strength: INT = Default("0"),
        all_flags: FLAGS | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c0_seed: INT = Default("-1"),
        c0_strength: INT = Default("0"),
        c0_flags: FLAGS | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c1_seed: INT = Default("-1"),
        c1_strength: INT = Default("0"),
        c1_flags: FLAGS | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c2_seed: INT = Default("-1"),
        c2_strength: INT = Default("0"),
        c2_flags: FLAGS | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c3_seed: INT = Default("-1"),
        c3_strength: INT = Default("0"),
        c3_flags: FLAGS | Literal["a", "p", "t", "u"] | Default = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add noise.

        Parameters:
        ----------

        :param INT all_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
        :param INT all_strength: set component #0 strength (from 0 to 100) (default 0)
        :param FLAGS all_flags: set component #0 flags (default 0)
        :param INT c0_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
        :param INT c0_strength: set component #0 strength (from 0 to 100) (default 0)
        :param FLAGS c0_flags: set component #0 flags (default 0)
        :param INT c1_seed: set component #1 noise seed (from -1 to INT_MAX) (default -1)
        :param INT c1_strength: set component #1 strength (from 0 to 100) (default 0)
        :param FLAGS c1_flags: set component #1 flags (default 0)
        :param INT c2_seed: set component #2 noise seed (from -1 to INT_MAX) (default -1)
        :param INT c2_strength: set component #2 strength (from 0 to 100) (default 0)
        :param FLAGS c2_flags: set component #2 flags (default 0)
        :param INT c3_seed: set component #3 noise seed (from -1 to INT_MAX) (default -1)
        :param INT c3_strength: set component #3 strength (from 0 to 100) (default 0)
        :param FLAGS c3_flags: set component #3 flags (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noise

        """
        filter_node = FilterNode(
            name="noise",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "all_seed": all_seed,
                        "all_strength": all_strength,
                        "all_flags": all_flags,
                        "c0_seed": c0_seed,
                        "c0_strength": c0_strength,
                        "c0_flags": c0_flags,
                        "c1_seed": c1_seed,
                        "c1_strength": c1_strength,
                        "c1_flags": c1_flags,
                        "c2_seed": c2_seed,
                        "c2_strength": c2_strength,
                        "c2_flags": c2_flags,
                        "c3_seed": c3_seed,
                        "c3_strength": c3_strength,
                        "c3_flags": c3_flags,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def normalize(
        self,
        *,
        blackpt: COLOR = Default("black"),
        whitept: COLOR = Default("white"),
        smoothing: INT = Default("0"),
        independence: FLOAT = Default("1"),
        strength: FLOAT = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Normalize RGB video.

        Parameters:
        ----------

        :param COLOR blackpt: output color to which darkest input color is mapped (default "black")
        :param COLOR whitept: output color to which brightest input color is mapped (default "white")
        :param INT smoothing: amount of temporal smoothing of the input range, to reduce flicker (from 0 to 2.68435e+08) (default 0)
        :param FLOAT independence: proportion of independent to linked channel normalization (from 0 to 1) (default 1)
        :param FLOAT strength: strength of filter, from no effect to full normalization (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#normalize

        """
        filter_node = FilterNode(
            name="normalize",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "blackpt": blackpt,
                        "whitept": whitept,
                        "smoothing": smoothing,
                        "independence": independence,
                        "strength": strength,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def null(self, **kwargs: Any) -> "VideoStream":
        """

        Pass the source unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#null

        """
        filter_node = FilterNode(
            name="null",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def ocr(
        self,
        *,
        datapath: STRING = Default(None),
        language: STRING = Default("eng"),
        whitelist: STRING = Default("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?\"'[]{}("),
        blacklist: STRING = Default(""),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Optical Character Recognition.

        Parameters:
        ----------

        :param STRING datapath: set datapath
        :param STRING language: set language (default "eng")
        :param STRING whitelist: set character whitelist (default "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?"'[]{}()|/\=*&%$#@!~ ")
        :param STRING blacklist: set character blacklist (default "")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ocr

        """
        filter_node = FilterNode(
            name="ocr",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "datapath": datapath,
                        "language": language,
                        "whitelist": whitelist,
                        "blacklist": blacklist,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def oscilloscope(
        self,
        *,
        x: FLOAT = Default("0.5"),
        y: FLOAT = Default("0.5"),
        s: FLOAT = Default("0.8"),
        t: FLOAT = Default("0.5"),
        o: FLOAT = Default("0.8"),
        tx: FLOAT = Default("0.5"),
        ty: FLOAT = Default("0.9"),
        tw: FLOAT = Default("0.8"),
        th: FLOAT = Default("0.3"),
        c: INT = Default("7"),
        g: BOOLEAN = Default("true"),
        st: BOOLEAN = Default("true"),
        sc: BOOLEAN = Default("true"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        2D Video Oscilloscope.

        Parameters:
        ----------

        :param FLOAT x: set scope x position (from 0 to 1) (default 0.5)
        :param FLOAT y: set scope y position (from 0 to 1) (default 0.5)
        :param FLOAT s: set scope size (from 0 to 1) (default 0.8)
        :param FLOAT t: set scope tilt (from 0 to 1) (default 0.5)
        :param FLOAT o: set trace opacity (from 0 to 1) (default 0.8)
        :param FLOAT tx: set trace x position (from 0 to 1) (default 0.5)
        :param FLOAT ty: set trace y position (from 0 to 1) (default 0.9)
        :param FLOAT tw: set trace width (from 0.1 to 1) (default 0.8)
        :param FLOAT th: set trace height (from 0.1 to 1) (default 0.3)
        :param INT c: set components to trace (from 0 to 15) (default 7)
        :param BOOLEAN g: draw trace grid (default true)
        :param BOOLEAN st: draw statistics (default true)
        :param BOOLEAN sc: draw scope (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#oscilloscope

        """
        filter_node = FilterNode(
            name="oscilloscope",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "s": s,
                        "t": t,
                        "o": o,
                        "tx": tx,
                        "ty": ty,
                        "tw": tw,
                        "th": th,
                        "c": c,
                        "g": g,
                        "st": st,
                        "sc": sc,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def overlay(
        self,
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
        **kwargs: Any,
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
                self,
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

    def owdenoise(
        self,
        *,
        depth: INT = Default("8"),
        luma_strength: DOUBLE = Default("1"),
        chroma_strength: DOUBLE = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise using wavelets.

        Parameters:
        ----------

        :param INT depth: set depth (from 8 to 16) (default 8)
        :param DOUBLE luma_strength: set luma strength (from 0 to 1000) (default 1)
        :param DOUBLE chroma_strength: set chroma strength (from 0 to 1000) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#owdenoise

        """
        filter_node = FilterNode(
            name="owdenoise",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "depth": depth,
                        "luma_strength": luma_strength,
                        "chroma_strength": chroma_strength,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pad(
        self,
        *,
        width: STRING = Default("iw"),
        height: STRING = Default("ih"),
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        color: COLOR = Default("black"),
        eval: INT | Literal["init", "frame"] | Default = Default("init"),
        aspect: RATIONAL = Default("0/1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pad the input video.

        Parameters:
        ----------

        :param STRING width: set the pad area width expression (default "iw")
        :param STRING height: set the pad area height expression (default "ih")
        :param STRING x: set the x offset expression for the input image position (default "0")
        :param STRING y: set the y offset expression for the input image position (default "0")
        :param COLOR color: set the color of the padded area border (default "black")
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param RATIONAL aspect: pad to fit an aspect instead of a resolution (from 0 to DBL_MAX) (default 0/1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pad

        """
        filter_node = FilterNode(
            name="pad",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "width": width,
                        "height": height,
                        "x": x,
                        "y": y,
                        "color": color,
                        "eval": eval,
                        "aspect": aspect,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def palettegen(
        self,
        *,
        max_colors: INT = Default("256"),
        reserve_transparent: BOOLEAN = Default("true"),
        transparency_color: COLOR = Default("lime"),
        stats_mode: INT | Literal["full", "diff", "single"] | Default = Default("full"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find the optimal palette for a given stream.

        Parameters:
        ----------

        :param INT max_colors: set the maximum number of colors to use in the palette (from 2 to 256) (default 256)
        :param BOOLEAN reserve_transparent: reserve a palette entry for transparency (default true)
        :param COLOR transparency_color: set a background color for transparency (default "lime")
        :param INT stats_mode: set statistics mode (from 0 to 2) (default full)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#palettegen

        """
        filter_node = FilterNode(
            name="palettegen",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "max_colors": max_colors,
                        "reserve_transparent": reserve_transparent,
                        "transparency_color": transparency_color,
                        "stats_mode": stats_mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def paletteuse(
        self,
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
        **kwargs: Any,
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
                self,
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

    def perms(
        self,
        *,
        mode: INT | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default("none"),
        seed: INT64 = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Set permissions for the output video frame.

        Parameters:
        ----------

        :param INT mode: select permissions mode (from 0 to 4) (default none)
        :param INT64 seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms

        """
        filter_node = FilterNode(
            name="perms",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def perspective(
        self,
        *,
        x0: STRING = Default("0"),
        y0: STRING = Default("0"),
        x1: STRING = Default("W"),
        y1: STRING = Default("0"),
        x2: STRING = Default("0"),
        y2: STRING = Default("H"),
        x3: STRING = Default("W"),
        y3: STRING = Default("H"),
        interpolation: INT | Literal["linear", "cubic"] | Default = Default("linear"),
        sense: INT | Literal["source", "destination"] | Default = Default("source"),
        eval: INT | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Correct the perspective of video.

        Parameters:
        ----------

        :param STRING x0: set top left x coordinate (default "0")
        :param STRING y0: set top left y coordinate (default "0")
        :param STRING x1: set top right x coordinate (default "W")
        :param STRING y1: set top right y coordinate (default "0")
        :param STRING x2: set bottom left x coordinate (default "0")
        :param STRING y2: set bottom left y coordinate (default "H")
        :param STRING x3: set bottom right x coordinate (default "W")
        :param STRING y3: set bottom right y coordinate (default "H")
        :param INT interpolation: set interpolation (from 0 to 1) (default linear)
        :param INT sense: specify the sense of the coordinates (from 0 to 1) (default source)
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perspective

        """
        filter_node = FilterNode(
            name="perspective",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x0": x0,
                        "y0": y0,
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2,
                        "x3": x3,
                        "y3": y3,
                        "interpolation": interpolation,
                        "sense": sense,
                        "eval": eval,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def phase(
        self,
        *,
        mode: INT | Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"] | Default = Default("A"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Phase shift fields.

        Parameters:
        ----------

        :param INT mode: set phase mode (from 0 to 8) (default A)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#phase

        """
        filter_node = FilterNode(
            name="phase",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def photosensitivity(
        self,
        *,
        frames: INT = Default("30"),
        threshold: FLOAT = Default("1"),
        skip: INT = Default("1"),
        bypass: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Filter out photosensitive epilepsy seizure-inducing flashes.

        Parameters:
        ----------

        :param INT frames: set how many frames to use (from 2 to 240) (default 30)
        :param FLOAT threshold: set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX) (default 1)
        :param INT skip: set pixels to skip when sampling frames (from 1 to 1024) (default 1)
        :param BOOLEAN bypass: leave frames unchanged (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#photosensitivity

        """
        filter_node = FilterNode(
            name="photosensitivity",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "frames": frames,
                        "threshold": threshold,
                        "skip": skip,
                        "bypass": bypass,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pixdesctest(self, **kwargs: Any) -> "VideoStream":
        """

        Test pixel format definitions.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixdesctest

        """
        filter_node = FilterNode(
            name="pixdesctest",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def pixelize(
        self,
        *,
        width: INT = Default("16"),
        height: INT = Default("16"),
        mode: INT | Literal["avg", "min", "max"] | Default = Default("avg"),
        planes: FLAGS = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixelize video.

        Parameters:
        ----------

        :param INT width: set block width (from 1 to 1024) (default 16)
        :param INT height: set block height (from 1 to 1024) (default 16)
        :param INT mode: set the pixelize mode (from 0 to 2) (default avg)
        :param FLAGS planes: set what planes to filter (default F)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixelize

        """
        filter_node = FilterNode(
            name="pixelize",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "width": width,
                        "height": height,
                        "mode": mode,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pixscope(
        self,
        *,
        x: FLOAT = Default("0.5"),
        y: FLOAT = Default("0.5"),
        w: INT = Default("7"),
        h: INT = Default("7"),
        o: FLOAT = Default("0.5"),
        wx: FLOAT = Default("-1"),
        wy: FLOAT = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixel data analysis.

        Parameters:
        ----------

        :param FLOAT x: set scope x offset (from 0 to 1) (default 0.5)
        :param FLOAT y: set scope y offset (from 0 to 1) (default 0.5)
        :param INT w: set scope width (from 1 to 80) (default 7)
        :param INT h: set scope height (from 1 to 80) (default 7)
        :param FLOAT o: set window opacity (from 0 to 1) (default 0.5)
        :param FLOAT wx: set window x offset (from -1 to 1) (default -1)
        :param FLOAT wy: set window y offset (from -1 to 1) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixscope

        """
        filter_node = FilterNode(
            name="pixscope",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h,
                        "o": o,
                        "wx": wx,
                        "wy": wy,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pp(self, *, subfilters: STRING = Default("de"), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Filter video using libpostproc.

        Parameters:
        ----------

        :param STRING subfilters: set postprocess subfilters (default "de")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp

        """
        filter_node = FilterNode(
            name="pp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "subfilters": subfilters,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pp7(
        self,
        *,
        qp: INT = Default("0"),
        mode: INT | Literal["hard", "soft", "medium"] | Default = Default("medium"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Postprocessing 7 filter.

        Parameters:
        ----------

        :param INT qp: force a constant quantizer parameter (from 0 to 64) (default 0)
        :param INT mode: set thresholding mode (from 0 to 2) (default medium)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp7

        """
        filter_node = FilterNode(
            name="pp7",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "qp": qp,
                        "mode": mode,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def prewitt(
        self,
        *,
        planes: INT = Default("15"),
        scale: FLOAT = Default("1"),
        delta: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply prewitt operator.

        Parameters:
        ----------

        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT scale: set scale (from 0 to 65535) (default 1)
        :param FLOAT delta: set delta (from -65535 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#prewitt

        """
        filter_node = FilterNode(
            name="prewitt",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pseudocolor(
        self,
        *,
        c0: STRING = Default("val"),
        c1: STRING = Default("val"),
        c2: STRING = Default("val"),
        c3: STRING = Default("val"),
        index: INT = Default("0"),
        preset: INT
        | Literal[
            "none",
            "magma",
            "inferno",
            "plasma",
            "viridis",
            "turbo",
            "cividis",
            "range1",
            "range2",
            "shadows",
            "highlights",
            "solar",
            "nominal",
            "preferred",
            "total",
            "spectral",
        ]
        | Default = Default("none"),
        opacity: FLOAT = Default("1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make pseudocolored video frames.

        Parameters:
        ----------

        :param STRING c0: set component #0 expression (default "val")
        :param STRING c1: set component #1 expression (default "val")
        :param STRING c2: set component #2 expression (default "val")
        :param STRING c3: set component #3 expression (default "val")
        :param INT index: set component as base (from 0 to 3) (default 0)
        :param INT preset: set preset (from -1 to 14) (default none)
        :param FLOAT opacity: set pseudocolor opacity (from 0 to 1) (default 1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pseudocolor

        """
        filter_node = FilterNode(
            name="pseudocolor",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "c0": c0,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "index": index,
                        "preset": preset,
                        "opacity": opacity,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def psnr(
        self,
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
        **kwargs: Any,
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
                self,
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

    def pullup(
        self,
        *,
        jl: INT = Default("1"),
        jr: INT = Default("1"),
        jt: INT = Default("4"),
        jb: INT = Default("4"),
        sb: BOOLEAN = Default("false"),
        mp: INT | Literal["y", "u", "v"] | Default = Default("y"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pullup from field sequence to frames.

        Parameters:
        ----------

        :param INT jl: set left junk size (from 0 to INT_MAX) (default 1)
        :param INT jr: set right junk size (from 0 to INT_MAX) (default 1)
        :param INT jt: set top junk size (from 1 to INT_MAX) (default 4)
        :param INT jb: set bottom junk size (from 1 to INT_MAX) (default 4)
        :param BOOLEAN sb: set strict breaks (default false)
        :param INT mp: set metric plane (from 0 to 2) (default y)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pullup

        """
        filter_node = FilterNode(
            name="pullup",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "jl": jl,
                        "jr": jr,
                        "jt": jt,
                        "jb": jb,
                        "sb": sb,
                        "mp": mp,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def qp(self, *, qp: STRING = Default(None), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Change video quantization parameters.

        Parameters:
        ----------

        :param STRING qp: set qp expression
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#qp

        """
        filter_node = FilterNode(
            name="qp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "qp": qp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def random(self, *, frames: INT = Default("30"), seed: INT64 = Default("-1"), **kwargs: Any) -> "VideoStream":
        """

        Return random frames.

        Parameters:
        ----------

        :param INT frames: set number of frames in cache (from 2 to 512) (default 30)
        :param INT64 seed: set the seed (from -1 to UINT32_MAX) (default -1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#random

        """
        filter_node = FilterNode(
            name="random",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "frames": frames,
                        "seed": seed,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def readeia608(
        self,
        *,
        scan_min: INT = Default("0"),
        scan_max: INT = Default("29"),
        spw: FLOAT = Default("0.27"),
        chp: BOOLEAN = Default("false"),
        lp: BOOLEAN = Default("true"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

        Parameters:
        ----------

        :param INT scan_min: set from which line to scan for codes (from 0 to INT_MAX) (default 0)
        :param INT scan_max: set to which line to scan for codes (from 0 to INT_MAX) (default 29)
        :param FLOAT spw: set ratio of width reserved for sync code detection (from 0.1 to 0.7) (default 0.27)
        :param BOOLEAN chp: check and apply parity bit (default false)
        :param BOOLEAN lp: lowpass line prior to processing (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#readeia608

        """
        filter_node = FilterNode(
            name="readeia608",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "scan_min": scan_min,
                        "scan_max": scan_max,
                        "spw": spw,
                        "chp": chp,
                        "lp": lp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def readvitc(
        self,
        *,
        scan_max: INT = Default("45"),
        thr_b: DOUBLE = Default("0.2"),
        thr_w: DOUBLE = Default("0.6"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Read vertical interval timecode and write it to frame metadata.

        Parameters:
        ----------

        :param INT scan_max: maximum line numbers to scan for VITC data (from -1 to INT_MAX) (default 45)
        :param DOUBLE thr_b: black color threshold (from 0 to 1) (default 0.2)
        :param DOUBLE thr_w: white color threshold (from 0 to 1) (default 0.6)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#readvitc

        """
        filter_node = FilterNode(
            name="readvitc",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "scan_max": scan_max,
                        "thr_b": thr_b,
                        "thr_w": thr_w,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def realtime(self, *, limit: DURATION = Default("2"), speed: DOUBLE = Default("1"), **kwargs: Any) -> "VideoStream":
        """

        Slow down filtering to match realtime.

        Parameters:
        ----------

        :param DURATION limit: sleep time limit (default 2)
        :param DOUBLE speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime

        """
        filter_node = FilterNode(
            name="realtime",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def remap(
        self,
        _xmap: "VideoStream",
        _ymap: "VideoStream",
        *,
        format: INT | Literal["color", "gray"] | Default = Default("color"),
        fill: COLOR = Default("black"),
        **kwargs: Any,
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
                self,
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

    def removegrain(
        self,
        *,
        m0: INT = Default("0"),
        m1: INT = Default("0"),
        m2: INT = Default("0"),
        m3: INT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove grain.

        Parameters:
        ----------

        :param INT m0: set mode for 1st plane (from 0 to 24) (default 0)
        :param INT m1: set mode for 2nd plane (from 0 to 24) (default 0)
        :param INT m2: set mode for 3rd plane (from 0 to 24) (default 0)
        :param INT m3: set mode for 4th plane (from 0 to 24) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removegrain

        """
        filter_node = FilterNode(
            name="removegrain",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "m0": m0,
                        "m1": m1,
                        "m2": m2,
                        "m3": m3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def removelogo(
        self, *, filename: STRING = Default(None), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Remove a TV logo based on a mask image.

        Parameters:
        ----------

        :param STRING filename: set bitmap filename
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removelogo

        """
        filter_node = FilterNode(
            name="removelogo",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filename": filename,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def repeatfields(self, **kwargs: Any) -> "VideoStream":
        """

        Hard repeat fields based on MPEG repeat field flag.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#repeatfields

        """
        filter_node = FilterNode(
            name="repeatfields",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def reverse(self, **kwargs: Any) -> "VideoStream":
        """

        Reverse a clip.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#reverse

        """
        filter_node = FilterNode(
            name="reverse",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def rgbashift(
        self,
        *,
        rh: INT = Default("0"),
        rv: INT = Default("0"),
        gh: INT = Default("0"),
        gv: INT = Default("0"),
        bh: INT = Default("0"),
        bv: INT = Default("0"),
        ah: INT = Default("0"),
        av: INT = Default("0"),
        edge: INT | Literal["smear", "wrap"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift RGBA.

        Parameters:
        ----------

        :param INT rh: shift red horizontally (from -255 to 255) (default 0)
        :param INT rv: shift red vertically (from -255 to 255) (default 0)
        :param INT gh: shift green horizontally (from -255 to 255) (default 0)
        :param INT gv: shift green vertically (from -255 to 255) (default 0)
        :param INT bh: shift blue horizontally (from -255 to 255) (default 0)
        :param INT bv: shift blue vertically (from -255 to 255) (default 0)
        :param INT ah: shift alpha horizontally (from -255 to 255) (default 0)
        :param INT av: shift alpha vertically (from -255 to 255) (default 0)
        :param INT edge: set edge operation (from 0 to 1) (default smear)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rgbashift

        """
        filter_node = FilterNode(
            name="rgbashift",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "rh": rh,
                        "rv": rv,
                        "gh": gh,
                        "gv": gv,
                        "bh": bh,
                        "bv": bv,
                        "ah": ah,
                        "av": av,
                        "edge": edge,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def roberts(
        self,
        *,
        planes: INT = Default("15"),
        scale: FLOAT = Default("1"),
        delta: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply roberts cross operator.

        Parameters:
        ----------

        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT scale: set scale (from 0 to 65535) (default 1)
        :param FLOAT delta: set delta (from -65535 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#roberts

        """
        filter_node = FilterNode(
            name="roberts",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def rotate(
        self,
        *,
        angle: STRING = Default("0"),
        out_w: STRING = Default("iw"),
        out_h: STRING = Default("ih"),
        fillcolor: STRING = Default("black"),
        bilinear: BOOLEAN = Default("true"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rotate the input image.

        Parameters:
        ----------

        :param STRING angle: set angle (in radians) (default "0")
        :param STRING out_w: set output width expression (default "iw")
        :param STRING out_h: set output height expression (default "ih")
        :param STRING fillcolor: set background fill color (default "black")
        :param BOOLEAN bilinear: use bilinear interpolation (default true)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rotate

        """
        filter_node = FilterNode(
            name="rotate",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "angle": angle,
                        "out_w": out_w,
                        "out_h": out_h,
                        "fillcolor": fillcolor,
                        "bilinear": bilinear,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sab(
        self,
        *,
        luma_radius: FLOAT = Default("1"),
        luma_pre_filter_radius: FLOAT = Default("1"),
        luma_strength: FLOAT = Default("1"),
        chroma_radius: FLOAT = Default("-0.9"),
        chroma_pre_filter_radius: FLOAT = Default("-0.9"),
        chroma_strength: FLOAT = Default("-0.9"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply shape adaptive blur.

        Parameters:
        ----------

        :param FLOAT luma_radius: set luma radius (from 0.1 to 4) (default 1)
        :param FLOAT luma_pre_filter_radius: set luma pre-filter radius (from 0.1 to 2) (default 1)
        :param FLOAT luma_strength: set luma strength (from 0.1 to 100) (default 1)
        :param FLOAT chroma_radius: set chroma radius (from -0.9 to 4) (default -0.9)
        :param FLOAT chroma_pre_filter_radius: set chroma pre-filter radius (from -0.9 to 2) (default -0.9)
        :param FLOAT chroma_strength: set chroma strength (from -0.9 to 100) (default -0.9)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sab

        """
        filter_node = FilterNode(
            name="sab",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_radius": luma_radius,
                        "luma_pre_filter_radius": luma_pre_filter_radius,
                        "luma_strength": luma_strength,
                        "chroma_radius": chroma_radius,
                        "chroma_pre_filter_radius": chroma_pre_filter_radius,
                        "chroma_strength": chroma_strength,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scale(
        self,
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
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scale the input video size and/or convert the image format.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale

        """
        filter_node = FilterNode(
            name="scale",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
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
        return filter_node.video(0)

    def scale2ref(
        self,
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
        **kwargs: Any,
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
                self,
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

    def scdet(
        self, *, threshold: DOUBLE = Default("10"), sc_pass: BOOLEAN = Default("false"), **kwargs: Any
    ) -> "VideoStream":
        """

        Detect video scene change

        Parameters:
        ----------

        :param DOUBLE threshold: set scene change detect threshold (from 0 to 100) (default 10)
        :param BOOLEAN sc_pass: Set the flag to pass scene change frames (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scdet

        """
        filter_node = FilterNode(
            name="scdet",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold": threshold,
                        "sc_pass": sc_pass,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scharr(
        self,
        *,
        planes: INT = Default("15"),
        scale: FLOAT = Default("1"),
        delta: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply scharr operator.

        Parameters:
        ----------

        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT scale: set scale (from 0 to 65535) (default 1)
        :param FLOAT delta: set delta (from -65535 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scharr

        """
        filter_node = FilterNode(
            name="scharr",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scroll(
        self,
        *,
        horizontal: FLOAT = Default("0"),
        vertical: FLOAT = Default("0"),
        hpos: FLOAT = Default("0"),
        vpos: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scroll input video.

        Parameters:
        ----------

        :param FLOAT horizontal: set the horizontal scrolling speed (from -1 to 1) (default 0)
        :param FLOAT vertical: set the vertical scrolling speed (from -1 to 1) (default 0)
        :param FLOAT hpos: set initial horizontal position (from 0 to 1) (default 0)
        :param FLOAT vpos: set initial vertical position (from 0 to 1) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scroll

        """
        filter_node = FilterNode(
            name="scroll",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "horizontal": horizontal,
                        "vertical": vertical,
                        "hpos": hpos,
                        "vpos": vpos,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def segment(
        self, *, timestamps: STRING = Default(None), frames: STRING = Default(None), **kwargs: Any
    ) -> FilterNode:
        """

        Segment video stream.

        Parameters:
        ----------

        :param STRING timestamps: timestamps of input at which to split input
        :param STRING frames: frames at which to split input

        Ref: https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment

        """
        filter_node = FilterNode(
            name="segment",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video] * len((str(timestamps or frames)).split("|"))),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "timestamps": timestamps,
                        "frames": frames,
                    }
                    | kwargs
                ).items()
            ),
        )

        return filter_node

    def select(self, *, expr: STRING = Default("1"), outputs: INT = Default("1"), **kwargs: Any) -> FilterNode:
        """

        Select video frames to pass in output.

        Parameters:
        ----------

        :param STRING expr: set an expression to use for selecting frames (default "1")
        :param INT outputs: set the number of outputs (from 1 to INT_MAX) (default 1)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect

        """
        filter_node = FilterNode(
            name="select",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video] * int(outputs)),
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

    def selectivecolor(
        self,
        *,
        correction_method: INT | Literal["absolute", "relative"] | Default = Default("absolute"),
        reds: STRING = Default(None),
        yellows: STRING = Default(None),
        greens: STRING = Default(None),
        cyans: STRING = Default(None),
        blues: STRING = Default(None),
        magentas: STRING = Default(None),
        whites: STRING = Default(None),
        neutrals: STRING = Default(None),
        blacks: STRING = Default(None),
        psfile: STRING = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply CMYK adjustments to specific color ranges.

        Parameters:
        ----------

        :param INT correction_method: select correction method (from 0 to 1) (default absolute)
        :param STRING reds: adjust red regions
        :param STRING yellows: adjust yellow regions
        :param STRING greens: adjust green regions
        :param STRING cyans: adjust cyan regions
        :param STRING blues: adjust blue regions
        :param STRING magentas: adjust magenta regions
        :param STRING whites: adjust white regions
        :param STRING neutrals: adjust neutral regions
        :param STRING blacks: adjust black regions
        :param STRING psfile: set Photoshop selectivecolor file name
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#selectivecolor

        """
        filter_node = FilterNode(
            name="selectivecolor",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "correction_method": correction_method,
                        "reds": reds,
                        "yellows": yellows,
                        "greens": greens,
                        "cyans": cyans,
                        "blues": blues,
                        "magentas": magentas,
                        "whites": whites,
                        "neutrals": neutrals,
                        "blacks": blacks,
                        "psfile": psfile,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sendcmd(
        self, *, commands: STRING = Default(None), filename: STRING = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Send commands to filters.

        Parameters:
        ----------

        :param STRING commands: set commands
        :param STRING filename: set commands file

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd

        """
        filter_node = FilterNode(
            name="sendcmd",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def separatefields(self, **kwargs: Any) -> "VideoStream":
        """

        Split input video frames into fields.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#separatefields

        """
        filter_node = FilterNode(
            name="separatefields",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def setdar(self, *, dar: STRING = Default("0"), max: INT = Default("100"), **kwargs: Any) -> "VideoStream":
        """

        Set the frame display aspect ratio.

        Parameters:
        ----------

        :param STRING dar: set display aspect ratio (default "0")
        :param INT max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        filter_node = FilterNode(
            name="setdar",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dar": dar,
                        "max": max,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def setfield(
        self, *, mode: INT | Literal["auto", "bff", "tff", "prog"] | Default = Default("auto"), **kwargs: Any
    ) -> "VideoStream":
        """

        Force field for the output video frame.

        Parameters:
        ----------

        :param INT mode: select interlace mode (from -1 to 2) (default auto)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setfield

        """
        filter_node = FilterNode(
            name="setfield",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def setparams(
        self,
        *,
        field_mode: INT | Literal["auto", "bff", "tff", "prog"] | Default = Default("auto"),
        range: INT
        | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
        | Default = Default("auto"),
        color_primaries: INT
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
            "p22",
            "ebu3213",
        ]
        | Default = Default("auto"),
        color_trc: INT
        | Literal[
            "auto",
            "bt709",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "linear",
            "log100",
            "log316",
            "4",
            "bt1361e",
            "1",
            "10",
            "12",
            "smpte2084",
            "smpte428",
            "b67",
        ]
        | Default = Default("auto"),
        colorspace: INT
        | Literal[
            "auto",
            "gbr",
            "bt709",
            "unknown",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "smpte2085",
            "nc",
            "c",
            "ictcp",
        ]
        | Default = Default("auto"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force field, or color property for the output video frame.

        Parameters:
        ----------

        :param INT field_mode: select interlace mode (from -1 to 2) (default auto)
        :param INT range: select color range (from -1 to 2) (default auto)
        :param INT color_primaries: select color primaries (from -1 to 22) (default auto)
        :param INT color_trc: select color transfer (from -1 to 18) (default auto)
        :param INT colorspace: select colorspace (from -1 to 14) (default auto)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setparams

        """
        filter_node = FilterNode(
            name="setparams",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "field_mode": field_mode,
                        "range": range,
                        "color_primaries": color_primaries,
                        "color_trc": color_trc,
                        "colorspace": colorspace,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def setpts(self, *, expr: STRING = Default("PTS"), **kwargs: Any) -> "VideoStream":
        """

        Set PTS for the output video frame.

        Parameters:
        ----------

        :param STRING expr: Expression determining the frame timestamp (default "PTS")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts

        """
        filter_node = FilterNode(
            name="setpts",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def setrange(
        self,
        *,
        range: INT
        | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
        | Default = Default("auto"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force color range for the output video frame.

        Parameters:
        ----------

        :param INT range: select color range (from -1 to 2) (default auto)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setrange

        """
        filter_node = FilterNode(
            name="setrange",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "range": range,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def setsar(self, *, sar: STRING = Default("0"), max: INT = Default("100"), **kwargs: Any) -> "VideoStream":
        """

        Set the pixel sample aspect ratio.

        Parameters:
        ----------

        :param STRING sar: set sample (pixel) aspect ratio (default "0")
        :param INT max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        filter_node = FilterNode(
            name="setsar",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sar": sar,
                        "max": max,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def settb(self, *, expr: STRING = Default("intb"), **kwargs: Any) -> "VideoStream":
        """

        Set timebase for the video output link.

        Parameters:
        ----------

        :param STRING expr: set expression determining the output timebase (default "intb")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb

        """
        filter_node = FilterNode(
            name="settb",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def shear(
        self,
        *,
        shx: FLOAT = Default("0"),
        shy: FLOAT = Default("0"),
        fillcolor: STRING = Default("black"),
        interp: INT | Literal["nearest", "bilinear"] | Default = Default("bilinear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shear transform the input image.

        Parameters:
        ----------

        :param FLOAT shx: set x shear factor (from -2 to 2) (default 0)
        :param FLOAT shy: set y shear factor (from -2 to 2) (default 0)
        :param STRING fillcolor: set background fill color (default "black")
        :param INT interp: set interpolation (from 0 to 1) (default bilinear)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shear

        """
        filter_node = FilterNode(
            name="shear",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "shx": shx,
                        "shy": shy,
                        "fillcolor": fillcolor,
                        "interp": interp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showinfo(self, *, checksum: BOOLEAN = Default("true"), **kwargs: Any) -> "VideoStream":
        """

        Show textual information for each video frame.

        Parameters:
        ----------

        :param BOOLEAN checksum: calculate checksums (default true)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showinfo

        """
        filter_node = FilterNode(
            name="showinfo",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "checksum": checksum,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def showpalette(self, *, s: INT = Default("30"), **kwargs: Any) -> "VideoStream":
        """

        Display frame palette.

        Parameters:
        ----------

        :param INT s: set pixel box size (from 1 to 100) (default 30)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showpalette

        """
        filter_node = FilterNode(
            name="showpalette",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "s": s,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def shuffleframes(
        self, *, mapping: STRING = Default("0"), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Shuffle video frames.

        Parameters:
        ----------

        :param STRING mapping: set destination indexes of input frames (default "0")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleframes

        """
        filter_node = FilterNode(
            name="shuffleframes",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mapping": mapping,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def shufflepixels(
        self,
        *,
        direction: INT | Literal["forward", "inverse"] | Default = Default("forward"),
        mode: INT | Literal["horizontal", "vertical", "block"] | Default = Default("horizontal"),
        width: INT = Default("10"),
        height: INT = Default("10"),
        seed: INT64 = Default("-1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video pixels.

        Parameters:
        ----------

        :param INT direction: set shuffle direction (from 0 to 1) (default forward)
        :param INT mode: set shuffle mode (from 0 to 2) (default horizontal)
        :param INT width: set block width (from 1 to 8000) (default 10)
        :param INT height: set block height (from 1 to 8000) (default 10)
        :param INT64 seed: set random seed (from -1 to UINT32_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shufflepixels

        """
        filter_node = FilterNode(
            name="shufflepixels",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "direction": direction,
                        "mode": mode,
                        "width": width,
                        "height": height,
                        "seed": seed,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def shuffleplanes(
        self,
        *,
        map0: INT = Default("0"),
        map1: INT = Default("1"),
        map2: INT = Default("2"),
        map3: INT = Default("3"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video planes.

        Parameters:
        ----------

        :param INT map0: Index of the input plane to be used as the first output plane (from 0 to 3) (default 0)
        :param INT map1: Index of the input plane to be used as the second output plane (from 0 to 3) (default 1)
        :param INT map2: Index of the input plane to be used as the third output plane (from 0 to 3) (default 2)
        :param INT map3: Index of the input plane to be used as the fourth output plane (from 0 to 3) (default 3)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleplanes

        """
        filter_node = FilterNode(
            name="shuffleplanes",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "map0": map0,
                        "map1": map1,
                        "map2": map2,
                        "map3": map3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sidedata(
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
    ) -> "VideoStream":
        """

        Manipulate video frame side data.

        Parameters:
        ----------

        :param INT mode: set a mode of operation (from 0 to 1) (default select)
        :param INT type: set side data type (from -1 to INT_MAX) (default -1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata

        """
        filter_node = FilterNode(
            name="sidedata",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def signalstats(
        self,
        *,
        stat: FLAGS | Literal["tout", "vrep", "brng"] | Default = Default("0"),
        out: INT | Literal["tout", "vrep", "brng"] | Default = Default("-1"),
        c: COLOR = Default("yellow"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate statistics from video analysis.

        Parameters:
        ----------

        :param FLAGS stat: set statistics filters (default 0)
        :param INT out: set video filter (from -1 to 2) (default -1)
        :param COLOR c: set highlight color (default "yellow")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#signalstats

        """
        filter_node = FilterNode(
            name="signalstats",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "stat": stat,
                        "out": out,
                        "c": c,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def siti(self, *, print_summary: BOOLEAN = Default("false"), **kwargs: Any) -> "VideoStream":
        """

        Calculate spatial information (SI) and temporal information (TI).

        Parameters:
        ----------

        :param BOOLEAN print_summary: Print summary showing average values (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#siti

        """
        filter_node = FilterNode(
            name="siti",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "print_summary": print_summary,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def smartblur(
        self,
        *,
        luma_radius: FLOAT = Default("1"),
        luma_strength: FLOAT = Default("1"),
        luma_threshold: INT = Default("0"),
        chroma_radius: FLOAT = Default("-0.9"),
        chroma_strength: FLOAT = Default("-2"),
        chroma_threshold: INT = Default("-31"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input video without impacting the outlines.

        Parameters:
        ----------

        :param FLOAT luma_radius: set luma radius (from 0.1 to 5) (default 1)
        :param FLOAT luma_strength: set luma strength (from -1 to 1) (default 1)
        :param INT luma_threshold: set luma threshold (from -30 to 30) (default 0)
        :param FLOAT chroma_radius: set chroma radius (from -0.9 to 5) (default -0.9)
        :param FLOAT chroma_strength: set chroma strength (from -2 to 1) (default -2)
        :param INT chroma_threshold: set chroma threshold (from -31 to 30) (default -31)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#smartblur

        """
        filter_node = FilterNode(
            name="smartblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_radius": luma_radius,
                        "luma_strength": luma_strength,
                        "luma_threshold": luma_threshold,
                        "chroma_radius": chroma_radius,
                        "chroma_strength": chroma_strength,
                        "chroma_threshold": chroma_threshold,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sobel(
        self,
        *,
        planes: INT = Default("15"),
        scale: FLOAT = Default("1"),
        delta: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply sobel operator.

        Parameters:
        ----------

        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT scale: set scale (from 0 to 65535) (default 1)
        :param FLOAT delta: set delta (from -65535 to 65535) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sobel

        """
        filter_node = FilterNode(
            name="sobel",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def spectrumsynth(
        self,
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
        **kwargs: Any,
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
                self,
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

    def split(self, *, outputs: INT = Default("2"), **kwargs: Any) -> FilterNode:
        """

        Pass on the input to N video outputs.

        Parameters:
        ----------

        :param INT outputs: set number of outputs (from 1 to INT_MAX) (default 2)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit

        """
        filter_node = FilterNode(
            name="split",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video] * int(outputs)),
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

    def spp(
        self,
        *,
        quality: INT = Default("3"),
        qp: INT = Default("0"),
        mode: INT | Literal["hard", "soft"] | Default = Default("hard"),
        use_bframe_qp: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a simple post processing filter.

        Parameters:
        ----------

        :param INT quality: set quality (from 0 to 6) (default 3)
        :param INT qp: force a constant quantizer parameter (from 0 to 63) (default 0)
        :param INT mode: set thresholding mode (from 0 to 1) (default hard)
        :param BOOLEAN use_bframe_qp: use B-frames' QP (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#spp

        """
        filter_node = FilterNode(
            name="spp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "quality": quality,
                        "qp": qp,
                        "mode": mode,
                        "use_bframe_qp": use_bframe_qp,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def sr(
        self,
        *,
        dnn_backend: INT | Literal["native"] | Default = Default("native"),
        scale_factor: INT = Default("2"),
        model: STRING = Default(None),
        input: STRING = Default("x"),
        output: STRING = Default("y"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN-based image super resolution to the input.

        Parameters:
        ----------

        :param INT dnn_backend: DNN backend used for model execution (from 0 to 1) (default native)
        :param INT scale_factor: scale factor for SRCNN model (from 2 to 4) (default 2)
        :param STRING model: path to model file specifying network architecture and its parameters
        :param STRING input: input name of the model (default "x")
        :param STRING output: output name of the model (default "y")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sr

        """
        filter_node = FilterNode(
            name="sr",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dnn_backend": dnn_backend,
                        "scale_factor": scale_factor,
                        "model": model,
                        "input": input,
                        "output": output,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def ssim(
        self,
        _reference: "VideoStream",
        *,
        stats_file: STRING = Default(None),
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def stereo3d(
        self,
        *,
        _in: INT
        | Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "al",
            "ar",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "irl",
            "irr",
            "icl",
            "icr",
        ]
        | Default = Default("sbsl"),
        out: INT
        | Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "agmc",
            "agmd",
            "agmg",
            "agmh",
            "al",
            "ar",
            "arbg",
            "arcc",
            "arcd",
            "arcg",
            "arch",
            "argg",
            "aybc",
            "aybd",
            "aybg",
            "aybh",
            "irl",
            "irr",
            "ml",
            "mr",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "chl",
            "chr",
            "icl",
            "icr",
            "hdmi",
        ]
        | Default = Default("arcd"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert video stereoscopic 3D view.

        Parameters:
        ----------

        :param INT _in: set input format (from 16 to 32) (default sbsl)
        :param INT out: set output format (from 0 to 32) (default arcd)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereo3d

        """
        filter_node = FilterNode(
            name="stereo3d",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "in": _in,
                        "out": out,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def subtitles(
        self,
        *,
        filename: STRING = Default(None),
        original_size: IMAGE_SIZE = Default(None),
        fontsdir: STRING = Default(None),
        alpha: BOOLEAN = Default("false"),
        charenc: STRING = Default(None),
        stream_index: INT = Default("-1"),
        force_style: STRING = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render text subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param STRING filename: set the filename of file to read
        :param IMAGE_SIZE original_size: set the size of the original video (used to scale fonts)
        :param STRING fontsdir: set the directory containing the fonts to read
        :param BOOLEAN alpha: enable processing of alpha channel (default false)
        :param STRING charenc: set input character encoding
        :param INT stream_index: set stream index (from -1 to INT_MAX) (default -1)
        :param STRING force_style: force subtitle style

        Ref: https://ffmpeg.org/ffmpeg-filters.html#subtitles

        """
        filter_node = FilterNode(
            name="subtitles",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filename": filename,
                        "original_size": original_size,
                        "fontsdir": fontsdir,
                        "alpha": alpha,
                        "charenc": charenc,
                        "stream_index": stream_index,
                        "force_style": force_style,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def super2xsai(self, **kwargs: Any) -> "VideoStream":
        """

        Scale the input by 2x using the Super2xSaI pixel art algorithm.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#super2xsai

        """
        filter_node = FilterNode(
            name="super2xsai",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def swaprect(
        self,
        *,
        w: STRING = Default("w/2"),
        h: STRING = Default("h/2"),
        x1: STRING = Default("w/2"),
        y1: STRING = Default("h/2"),
        x2: STRING = Default("0"),
        y2: STRING = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Swap 2 rectangular objects in video.

        Parameters:
        ----------

        :param STRING w: set rect width (default "w/2")
        :param STRING h: set rect height (default "h/2")
        :param STRING x1: set 1st rect x top left coordinate (default "w/2")
        :param STRING y1: set 1st rect y top left coordinate (default "h/2")
        :param STRING x2: set 2nd rect x top left coordinate (default "0")
        :param STRING y2: set 2nd rect y top left coordinate (default "0")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#swaprect

        """
        filter_node = FilterNode(
            name="swaprect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "w": w,
                        "h": h,
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def swapuv(self, *, enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Swap U and V components.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#swapuv

        """
        filter_node = FilterNode(
            name="swapuv",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def tblend(
        self,
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
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blend successive frames.

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
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tblend

        """
        filter_node = FilterNode(
            name="tblend",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
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
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def telecine(
        self,
        *,
        first_field: INT | Literal["top", "t", "bottom", "b"] | Default = Default("top"),
        pattern: STRING = Default("23"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a telecine pattern.

        Parameters:
        ----------

        :param INT first_field: select first field (from 0 to 1) (default top)
        :param STRING pattern: pattern that describe for how many fields a frame is to be displayed (default "23")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#telecine

        """
        filter_node = FilterNode(
            name="telecine",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "first_field": first_field,
                        "pattern": pattern,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def thistogram(
        self,
        *,
        width: INT = Default("0"),
        display_mode: INT | Literal["overlay", "parade", "stack"] | Default = Default("stack"),
        levels_mode: INT | Literal["linear", "logarithmic"] | Default = Default("linear"),
        components: INT = Default("7"),
        bgopacity: FLOAT = Default("0.9"),
        envelope: BOOLEAN = Default("false"),
        ecolor: COLOR = Default("gold"),
        slide: INT | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default("replace"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and draw a temporal histogram.

        Parameters:
        ----------

        :param INT width: set width (from 0 to 8192) (default 0)
        :param INT display_mode: set display mode (from 0 to 2) (default stack)
        :param INT levels_mode: set levels mode (from 0 to 1) (default linear)
        :param INT components: set color components to display (from 1 to 15) (default 7)
        :param FLOAT bgopacity: set background opacity (from 0 to 1) (default 0.9)
        :param BOOLEAN envelope: display envelope (default false)
        :param COLOR ecolor: set envelope color (default "gold")
        :param INT slide: set slide mode (from 0 to 4) (default replace)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#thistogram

        """
        filter_node = FilterNode(
            name="thistogram",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "width": width,
                        "display_mode": display_mode,
                        "levels_mode": levels_mode,
                        "components": components,
                        "bgopacity": bgopacity,
                        "envelope": envelope,
                        "ecolor": ecolor,
                        "slide": slide,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def threshold(
        self,
        _threshold: "VideoStream",
        _min: "VideoStream",
        _max: "VideoStream",
        *,
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def thumbnail(
        self,
        *,
        n: INT = Default("100"),
        log: INT | Literal["quiet", "info", "verbose"] | Default = Default("info"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Select the most representative frame in a given sequence of consecutive frames.

        Parameters:
        ----------

        :param INT n: set the frames batch size (from 2 to INT_MAX) (default 100)
        :param INT log: force stats logging level (from INT_MIN to INT_MAX) (default info)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#thumbnail

        """
        filter_node = FilterNode(
            name="thumbnail",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                        "log": log,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tile(
        self,
        *,
        layout: IMAGE_SIZE = Default("6x5"),
        nb_frames: INT = Default("0"),
        margin: INT = Default("0"),
        padding: INT = Default("0"),
        color: COLOR = Default("black"),
        overlap: INT = Default("0"),
        init_padding: INT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Tile several successive frames together.

        Parameters:
        ----------

        :param IMAGE_SIZE layout: set grid size (default "6x5")
        :param INT nb_frames: set maximum number of frame to render (from 0 to INT_MAX) (default 0)
        :param INT margin: set outer border margin in pixels (from 0 to 1024) (default 0)
        :param INT padding: set inner border thickness in pixels (from 0 to 1024) (default 0)
        :param COLOR color: set the color of the unused area (default "black")
        :param INT overlap: set how many frames to overlap for each render (from 0 to INT_MAX) (default 0)
        :param INT init_padding: set how many frames to initially pad (from 0 to INT_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tile

        """
        filter_node = FilterNode(
            name="tile",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "layout": layout,
                        "nb_frames": nb_frames,
                        "margin": margin,
                        "padding": padding,
                        "color": color,
                        "overlap": overlap,
                        "init_padding": init_padding,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tinterlace(
        self,
        *,
        mode: INT
        | Literal[
            "merge", "drop_even", "drop_odd", "pad", "interleave_top", "interleave_bottom", "interlacex2", "mergex2"
        ]
        | Default = Default("merge"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Perform temporal field interlacing.

        Parameters:
        ----------

        :param INT mode: select interlace mode (from 0 to 7) (default merge)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tinterlace

        """
        filter_node = FilterNode(
            name="tinterlace",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tlut2(
        self,
        *,
        c0: STRING = Default("x"),
        c1: STRING = Default("x"),
        c2: STRING = Default("x"),
        c3: STRING = Default("x"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table from two successive frames.

        Parameters:
        ----------

        :param STRING c0: set component #0 expression (default "x")
        :param STRING c1: set component #1 expression (default "x")
        :param STRING c2: set component #2 expression (default "x")
        :param STRING c3: set component #3 expression (default "x")
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

        """
        filter_node = FilterNode(
            name="tlut2",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "c0": c0,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tmedian(
        self,
        *,
        radius: INT = Default("1"),
        planes: INT = Default("15"),
        percentile: FLOAT = Default("0.5"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick median pixels from successive frames.

        Parameters:
        ----------

        :param INT radius: set median filter radius (from 1 to 127) (default 1)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param FLOAT percentile: set percentile (from 0 to 1) (default 0.5)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmedian

        """
        filter_node = FilterNode(
            name="tmedian",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "radius": radius,
                        "planes": planes,
                        "percentile": percentile,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tmidequalizer(
        self,
        *,
        radius: INT = Default("5"),
        sigma: FLOAT = Default("0.5"),
        planes: INT = Default("15"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Temporal Midway Equalization.

        Parameters:
        ----------

        :param INT radius: set radius (from 1 to 127) (default 5)
        :param FLOAT sigma: set sigma (from 0 to 1) (default 0.5)
        :param INT planes: set planes (from 0 to 15) (default 15)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmidequalizer

        """
        filter_node = FilterNode(
            name="tmidequalizer",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "radius": radius,
                        "sigma": sigma,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tmix(
        self,
        *,
        frames: INT = Default("3"),
        weights: STRING = Default("1 1 1"),
        scale: FLOAT = Default("0"),
        planes: FLAGS = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Mix successive video frames.

        Parameters:
        ----------

        :param INT frames: set number of successive frames to mix (from 1 to 1024) (default 3)
        :param STRING weights: set weight for each frame (default "1 1 1")
        :param FLOAT scale: set scale (from 0 to 32767) (default 0)
        :param FLAGS planes: set what planes to filter (default F)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmix

        """
        filter_node = FilterNode(
            name="tmix",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "frames": frames,
                        "weights": weights,
                        "scale": scale,
                        "planes": planes,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tonemap(
        self,
        *,
        tonemap: INT
        | Literal["none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"]
        | Default = Default("none"),
        param: DOUBLE = Default("nan"),
        desat: DOUBLE = Default("2"),
        peak: DOUBLE = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Conversion to/from different dynamic ranges.

        Parameters:
        ----------

        :param INT tonemap: tonemap algorithm selection (from 0 to 6) (default none)
        :param DOUBLE param: tonemap parameter (from DBL_MIN to DBL_MAX) (default nan)
        :param DOUBLE desat: desaturation strength (from 0 to DBL_MAX) (default 2)
        :param DOUBLE peak: signal peak override (from 0 to DBL_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap

        """
        filter_node = FilterNode(
            name="tonemap",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "tonemap": tonemap,
                        "param": param,
                        "desat": desat,
                        "peak": peak,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tpad(
        self,
        *,
        start: INT = Default("0"),
        stop: INT = Default("0"),
        start_mode: INT | Literal["add", "clone"] | Default = Default("add"),
        stop_mode: INT | Literal["add", "clone"] | Default = Default("add"),
        start_duration: DURATION = Default("0"),
        stop_duration: DURATION = Default("0"),
        color: COLOR = Default("black"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Temporarily pad video frames.

        Parameters:
        ----------

        :param INT start: set the number of frames to delay input (from 0 to INT_MAX) (default 0)
        :param INT stop: set the number of frames to add after input finished (from -1 to INT_MAX) (default 0)
        :param INT start_mode: set the mode of added frames to start (from 0 to 1) (default add)
        :param INT stop_mode: set the mode of added frames to end (from 0 to 1) (default add)
        :param DURATION start_duration: set the duration to delay input (default 0)
        :param DURATION stop_duration: set the duration to pad input (default 0)
        :param COLOR color: set the color of the added frames (default "black")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tpad

        """
        filter_node = FilterNode(
            name="tpad",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "start": start,
                        "stop": stop,
                        "start_mode": start_mode,
                        "stop_mode": stop_mode,
                        "start_duration": start_duration,
                        "stop_duration": stop_duration,
                        "color": color,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def transpose(
        self,
        *,
        dir: INT | Literal["cclock_flip", "clock", "cclock", "clock_flip"] | Default = Default("cclock_flip"),
        passthrough: INT | Literal["none", "portrait", "landscape"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transpose input video.

        Parameters:
        ----------

        :param INT dir: set transpose direction (from 0 to 7) (default cclock_flip)
        :param INT passthrough: do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose

        """
        filter_node = FilterNode(
            name="transpose",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dir": dir,
                        "passthrough": passthrough,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def trim(
        self,
        *,
        start: DURATION = Default("INT64_MAX"),
        end: DURATION = Default("INT64_MAX"),
        start_pts: INT64 = Default("I64_MIN"),
        end_pts: INT64 = Default("I64_MIN"),
        duration: DURATION = Default("0"),
        start_frame: INT64 = Default("-1"),
        end_frame: INT64 = Default("I64_MAX"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick one continuous section from the input, drop the rest.

        Parameters:
        ----------

        :param DURATION start: Timestamp of the first frame that should be passed (default INT64_MAX)
        :param DURATION end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
        :param INT64 start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
        :param INT64 end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
        :param DURATION duration: Maximum duration of the output (default 0)
        :param INT64 start_frame: Number of the first frame that should be passed to the output (from -1 to I64_MAX) (default -1)
        :param INT64 end_frame: Number of the first frame that should be dropped again (from 0 to I64_MAX) (default I64_MAX)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#trim

        """
        filter_node = FilterNode(
            name="trim",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "start": start,
                        "end": end,
                        "start_pts": start_pts,
                        "end_pts": end_pts,
                        "duration": duration,
                        "start_frame": start_frame,
                        "end_frame": end_frame,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def unsharp(
        self,
        *,
        luma_msize_x: INT = Default("5"),
        luma_msize_y: INT = Default("5"),
        luma_amount: FLOAT = Default("1"),
        chroma_msize_x: INT = Default("5"),
        chroma_msize_y: INT = Default("5"),
        chroma_amount: FLOAT = Default("0"),
        alpha_msize_x: INT = Default("5"),
        alpha_msize_y: INT = Default("5"),
        alpha_amount: FLOAT = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Sharpen or blur the input video.

        Parameters:
        ----------

        :param INT luma_msize_x: set luma matrix horizontal size (from 3 to 23) (default 5)
        :param INT luma_msize_y: set luma matrix vertical size (from 3 to 23) (default 5)
        :param FLOAT luma_amount: set luma effect strength (from -2 to 5) (default 1)
        :param INT chroma_msize_x: set chroma matrix horizontal size (from 3 to 23) (default 5)
        :param INT chroma_msize_y: set chroma matrix vertical size (from 3 to 23) (default 5)
        :param FLOAT chroma_amount: set chroma effect strength (from -2 to 5) (default 0)
        :param INT alpha_msize_x: set alpha matrix horizontal size (from 3 to 23) (default 5)
        :param INT alpha_msize_y: set alpha matrix vertical size (from 3 to 23) (default 5)
        :param FLOAT alpha_amount: set alpha effect strength (from -2 to 5) (default 0)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#unsharp

        """
        filter_node = FilterNode(
            name="unsharp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "luma_msize_x": luma_msize_x,
                        "luma_msize_y": luma_msize_y,
                        "luma_amount": luma_amount,
                        "chroma_msize_x": chroma_msize_x,
                        "chroma_msize_y": chroma_msize_y,
                        "chroma_amount": chroma_amount,
                        "alpha_msize_x": alpha_msize_x,
                        "alpha_msize_y": alpha_msize_y,
                        "alpha_amount": alpha_amount,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def untile(self, *, layout: IMAGE_SIZE = Default("6x5"), **kwargs: Any) -> "VideoStream":
        """

        Untile a frame into a sequence of frames.

        Parameters:
        ----------

        :param IMAGE_SIZE layout: set grid size (default "6x5")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#untile

        """
        filter_node = FilterNode(
            name="untile",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "layout": layout,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def v360(
        self,
        *,
        input: INT
        | Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | Default = Default("e"),
        output: INT
        | Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "perspective",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | Default = Default("c3x2"),
        interp: INT
        | Literal[
            "near",
            "nearest",
            "line",
            "linear",
            "lagrange9",
            "cube",
            "cubic",
            "lanc",
            "lanczos",
            "sp16",
            "spline16",
            "gauss",
            "gaussian",
            "mitchell",
        ]
        | Default = Default("line"),
        w: INT = Default("0"),
        h: INT = Default("0"),
        in_stereo: INT | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        out_stereo: INT | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        in_forder: STRING = Default("rludfb"),
        out_forder: STRING = Default("rludfb"),
        in_frot: STRING = Default("000000"),
        out_frot: STRING = Default("000000"),
        in_pad: FLOAT = Default("0"),
        out_pad: FLOAT = Default("0"),
        fin_pad: INT = Default("0"),
        fout_pad: INT = Default("0"),
        yaw: FLOAT = Default("0"),
        pitch: FLOAT = Default("0"),
        roll: FLOAT = Default("0"),
        rorder: STRING = Default("ypr"),
        h_fov: FLOAT = Default("0"),
        v_fov: FLOAT = Default("0"),
        d_fov: FLOAT = Default("0"),
        h_flip: BOOLEAN = Default("false"),
        v_flip: BOOLEAN = Default("false"),
        d_flip: BOOLEAN = Default("false"),
        ih_flip: BOOLEAN = Default("false"),
        iv_flip: BOOLEAN = Default("false"),
        in_trans: BOOLEAN = Default("false"),
        out_trans: BOOLEAN = Default("false"),
        ih_fov: FLOAT = Default("0"),
        iv_fov: FLOAT = Default("0"),
        id_fov: FLOAT = Default("0"),
        h_offset: FLOAT = Default("0"),
        v_offset: FLOAT = Default("0"),
        alpha_mask: BOOLEAN = Default("false"),
        reset_rot: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert 360 projection of video.

        Parameters:
        ----------

        :param INT input: set input projection (from 0 to 24) (default e)
        :param INT output: set output projection (from 0 to 24) (default c3x2)
        :param INT interp: set interpolation method (from 0 to 7) (default line)
        :param INT w: output width (from 0 to 32767) (default 0)
        :param INT h: output height (from 0 to 32767) (default 0)
        :param INT in_stereo: input stereo format (from 0 to 2) (default 2d)
        :param INT out_stereo: output stereo format (from 0 to 2) (default 2d)
        :param STRING in_forder: input cubemap face order (default "rludfb")
        :param STRING out_forder: output cubemap face order (default "rludfb")
        :param STRING in_frot: input cubemap face rotation (default "000000")
        :param STRING out_frot: output cubemap face rotation (default "000000")
        :param FLOAT in_pad: percent input cubemap pads (from 0 to 0.1) (default 0)
        :param FLOAT out_pad: percent output cubemap pads (from 0 to 0.1) (default 0)
        :param INT fin_pad: fixed input cubemap pads (from 0 to 100) (default 0)
        :param INT fout_pad: fixed output cubemap pads (from 0 to 100) (default 0)
        :param FLOAT yaw: yaw rotation (from -180 to 180) (default 0)
        :param FLOAT pitch: pitch rotation (from -180 to 180) (default 0)
        :param FLOAT roll: roll rotation (from -180 to 180) (default 0)
        :param STRING rorder: rotation order (default "ypr")
        :param FLOAT h_fov: output horizontal field of view (from 0 to 360) (default 0)
        :param FLOAT v_fov: output vertical field of view (from 0 to 360) (default 0)
        :param FLOAT d_fov: output diagonal field of view (from 0 to 360) (default 0)
        :param BOOLEAN h_flip: flip out video horizontally (default false)
        :param BOOLEAN v_flip: flip out video vertically (default false)
        :param BOOLEAN d_flip: flip out video indepth (default false)
        :param BOOLEAN ih_flip: flip in video horizontally (default false)
        :param BOOLEAN iv_flip: flip in video vertically (default false)
        :param BOOLEAN in_trans: transpose video input (default false)
        :param BOOLEAN out_trans: transpose video output (default false)
        :param FLOAT ih_fov: input horizontal field of view (from 0 to 360) (default 0)
        :param FLOAT iv_fov: input vertical field of view (from 0 to 360) (default 0)
        :param FLOAT id_fov: input diagonal field of view (from 0 to 360) (default 0)
        :param FLOAT h_offset: output horizontal off-axis offset (from -1 to 1) (default 0)
        :param FLOAT v_offset: output vertical off-axis offset (from -1 to 1) (default 0)
        :param BOOLEAN alpha_mask: build mask in alpha plane (default false)
        :param BOOLEAN reset_rot: reset rotation (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#v360

        """
        filter_node = FilterNode(
            name="v360",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "input": input,
                        "output": output,
                        "interp": interp,
                        "w": w,
                        "h": h,
                        "in_stereo": in_stereo,
                        "out_stereo": out_stereo,
                        "in_forder": in_forder,
                        "out_forder": out_forder,
                        "in_frot": in_frot,
                        "out_frot": out_frot,
                        "in_pad": in_pad,
                        "out_pad": out_pad,
                        "fin_pad": fin_pad,
                        "fout_pad": fout_pad,
                        "yaw": yaw,
                        "pitch": pitch,
                        "roll": roll,
                        "rorder": rorder,
                        "h_fov": h_fov,
                        "v_fov": v_fov,
                        "d_fov": d_fov,
                        "h_flip": h_flip,
                        "v_flip": v_flip,
                        "d_flip": d_flip,
                        "ih_flip": ih_flip,
                        "iv_flip": iv_flip,
                        "in_trans": in_trans,
                        "out_trans": out_trans,
                        "ih_fov": ih_fov,
                        "iv_fov": iv_fov,
                        "id_fov": id_fov,
                        "h_offset": h_offset,
                        "v_offset": v_offset,
                        "alpha_mask": alpha_mask,
                        "reset_rot": reset_rot,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vaguedenoiser(
        self,
        *,
        threshold: FLOAT = Default("2"),
        method: INT | Literal["hard", "soft", "garrote"] | Default = Default("garrote"),
        nsteps: INT = Default("6"),
        percent: FLOAT = Default("85"),
        planes: INT = Default("15"),
        type: INT | Literal["universal", "bayes"] | Default = Default("universal"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a Wavelet based Denoiser.

        Parameters:
        ----------

        :param FLOAT threshold: set filtering strength (from 0 to DBL_MAX) (default 2)
        :param INT method: set filtering method (from 0 to 2) (default garrote)
        :param INT nsteps: set number of steps (from 1 to 32) (default 6)
        :param FLOAT percent: set percent of full denoising (from 0 to 100) (default 85)
        :param INT planes: set planes to filter (from 0 to 15) (default 15)
        :param INT type: set threshold type (from 0 to 1) (default universal)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vaguedenoiser

        """
        filter_node = FilterNode(
            name="vaguedenoiser",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "threshold": threshold,
                        "method": method,
                        "nsteps": nsteps,
                        "percent": percent,
                        "planes": planes,
                        "type": type,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def varblur(
        self,
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
        **kwargs: Any,
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
                self,
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

    def vectorscope(
        self,
        *,
        mode: INT
        | Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | Default = Default("gray"),
        x: INT = Default("1"),
        y: INT = Default("2"),
        intensity: FLOAT = Default("0.004"),
        envelope: INT | Literal["none", "instant", "peak", "instant"] | Default = Default("none"),
        graticule: INT | Literal["none", "green", "color", "invert"] | Default = Default("none"),
        opacity: FLOAT = Default("0.75"),
        flags: FLAGS | Literal["white", "black", "name"] | Default = Default("name"),
        bgopacity: FLOAT = Default("0.3"),
        lthreshold: FLOAT = Default("0"),
        hthreshold: FLOAT = Default("1"),
        colorspace: INT | Literal["auto", "601", "709"] | Default = Default("auto"),
        tint0: FLOAT = Default("0"),
        tint1: FLOAT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video vectorscope.

        Parameters:
        ----------

        :param INT mode: set vectorscope mode (from 0 to 5) (default gray)
        :param INT x: set color component on X axis (from 0 to 2) (default 1)
        :param INT y: set color component on Y axis (from 0 to 2) (default 2)
        :param FLOAT intensity: set intensity (from 0 to 1) (default 0.004)
        :param INT envelope: set envelope (from 0 to 3) (default none)
        :param INT graticule: set graticule (from 0 to 3) (default none)
        :param FLOAT opacity: set graticule opacity (from 0 to 1) (default 0.75)
        :param FLAGS flags: set graticule flags (default name)
        :param FLOAT bgopacity: set background opacity (from 0 to 1) (default 0.3)
        :param FLOAT lthreshold: set low threshold (from 0 to 1) (default 0)
        :param FLOAT hthreshold: set high threshold (from 0 to 1) (default 1)
        :param INT colorspace: set colorspace (from 0 to 2) (default auto)
        :param FLOAT tint0: set 1st tint (from -1 to 1) (default 0)
        :param FLOAT tint1: set 2nd tint (from -1 to 1) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vectorscope

        """
        filter_node = FilterNode(
            name="vectorscope",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "x": x,
                        "y": y,
                        "intensity": intensity,
                        "envelope": envelope,
                        "graticule": graticule,
                        "opacity": opacity,
                        "flags": flags,
                        "bgopacity": bgopacity,
                        "lthreshold": lthreshold,
                        "hthreshold": hthreshold,
                        "colorspace": colorspace,
                        "tint0": tint0,
                        "tint1": tint1,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vflip(self, *, enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Flip the input video vertically.

        Parameters:
        ----------

        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vflip

        """
        filter_node = FilterNode(
            name="vflip",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def vfrdet(self, **kwargs: Any) -> "VideoStream":
        """

        Variable frame rate detect filter.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#vfrdet

        """
        filter_node = FilterNode(
            name="vfrdet",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def vibrance(
        self,
        *,
        intensity: FLOAT = Default("0"),
        rbal: FLOAT = Default("1"),
        gbal: FLOAT = Default("1"),
        bbal: FLOAT = Default("1"),
        rlum: FLOAT = Default("0.072186"),
        glum: FLOAT = Default("0.715158"),
        blum: FLOAT = Default("0.212656"),
        alternate: BOOLEAN = Default("false"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Boost or alter saturation.

        Parameters:
        ----------

        :param FLOAT intensity: set the intensity value (from -2 to 2) (default 0)
        :param FLOAT rbal: set the red balance value (from -10 to 10) (default 1)
        :param FLOAT gbal: set the green balance value (from -10 to 10) (default 1)
        :param FLOAT bbal: set the blue balance value (from -10 to 10) (default 1)
        :param FLOAT rlum: set the red luma coefficient (from 0 to 1) (default 0.072186)
        :param FLOAT glum: set the green luma coefficient (from 0 to 1) (default 0.715158)
        :param FLOAT blum: set the blue luma coefficient (from 0 to 1) (default 0.212656)
        :param BOOLEAN alternate: use alternate colors (default false)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrance

        """
        filter_node = FilterNode(
            name="vibrance",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "intensity": intensity,
                        "rbal": rbal,
                        "gbal": gbal,
                        "bbal": bbal,
                        "rlum": rlum,
                        "glum": glum,
                        "blum": blum,
                        "alternate": alternate,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vidstabdetect(
        self,
        *,
        result: STRING = Default("transforms.trf"),
        shakiness: INT = Default("5"),
        accuracy: INT = Default("15"),
        stepsize: INT = Default("6"),
        mincontrast: DOUBLE = Default("0.25"),
        show: INT = Default("0"),
        tripod: INT = Default("0"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2).

        Parameters:
        ----------

        :param STRING result: path to the file used to write the transforms (default "transforms.trf")
        :param INT shakiness: how shaky is the video and how quick is the camera? 1: little (fast) 10: very strong/quick (slow) (from 1 to 10) (default 5)
        :param INT accuracy: (>=shakiness) 1: low 15: high (slow) (from 1 to 15) (default 15)
        :param INT stepsize: region around minimum is scanned with 1 pixel resolution (from 1 to 32) (default 6)
        :param DOUBLE mincontrast: below this contrast a field is discarded (0-1) (from 0 to 1) (default 0.25)
        :param INT show: 0: draw nothing; 1,2: show fields and transforms (from 0 to 2) (default 0)
        :param INT tripod: virtual tripod mode (if >0): motion is compared to a reference reference frame (frame # is the value) (from 0 to INT_MAX) (default 0)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vidstabdetect

        """
        filter_node = FilterNode(
            name="vidstabdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "result": result,
                        "shakiness": shakiness,
                        "accuracy": accuracy,
                        "stepsize": stepsize,
                        "mincontrast": mincontrast,
                        "show": show,
                        "tripod": tripod,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vidstabtransform(
        self,
        *,
        input: STRING = Default("transforms.trf"),
        smoothing: INT = Default("15"),
        optalgo: INT | Literal["opt", "gauss", "avg"] | Default = Default("opt"),
        maxshift: INT = Default("-1"),
        maxangle: DOUBLE = Default("-1"),
        crop: INT | Literal["keep", "black"] | Default = Default("keep"),
        invert: INT = Default("0"),
        relative: INT = Default("1"),
        zoom: DOUBLE = Default("0"),
        optzoom: INT = Default("1"),
        zoomspeed: DOUBLE = Default("0.25"),
        interpol: INT | Literal["no", "linear", "bilinear", "bicubic"] | Default = Default("bilinear"),
        tripod: BOOLEAN = Default("false"),
        debug: BOOLEAN = Default("false"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1).

        Parameters:
        ----------

        :param STRING input: set path to the file storing the transforms (default "transforms.trf")
        :param INT smoothing: set number of frames*2 + 1 used for lowpass filtering (from 0 to 1000) (default 15)
        :param INT optalgo: set camera path optimization algo (from 0 to 2) (default opt)
        :param INT maxshift: set maximal number of pixels to translate image (from -1 to 500) (default -1)
        :param DOUBLE maxangle: set maximal angle in rad to rotate image (from -1 to 3.14) (default -1)
        :param INT crop: set cropping mode (from 0 to 1) (default keep)
        :param INT invert: invert transforms (from 0 to 1) (default 0)
        :param INT relative: consider transforms as relative (from 0 to 1) (default 1)
        :param DOUBLE zoom: set percentage to zoom (>0: zoom in, <0: zoom out (from -100 to 100) (default 0)
        :param INT optzoom: set optimal zoom (0: nothing, 1: optimal static zoom, 2: optimal dynamic zoom) (from 0 to 2) (default 1)
        :param DOUBLE zoomspeed: for adative zoom: percent to zoom maximally each frame (from 0 to 5) (default 0.25)
        :param INT interpol: set type of interpolation (from 0 to 3) (default bilinear)
        :param BOOLEAN tripod: enable virtual tripod mode (same as relative=0:smoothing=0) (default false)
        :param BOOLEAN debug: enable debug mode and writer global motions information to file (default false)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vidstabtransform

        """
        filter_node = FilterNode(
            name="vidstabtransform",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "input": input,
                        "smoothing": smoothing,
                        "optalgo": optalgo,
                        "maxshift": maxshift,
                        "maxangle": maxangle,
                        "crop": crop,
                        "invert": invert,
                        "relative": relative,
                        "zoom": zoom,
                        "optzoom": optzoom,
                        "zoomspeed": zoomspeed,
                        "interpol": interpol,
                        "tripod": tripod,
                        "debug": debug,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vif(
        self,
        _reference: "VideoStream",
        *,
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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

    def vignette(
        self,
        *,
        angle: STRING = Default("PI/5"),
        x0: STRING = Default("w/2"),
        y0: STRING = Default("h/2"),
        mode: INT | Literal["forward", "backward"] | Default = Default("forward"),
        eval: INT | Literal["init", "frame"] | Default = Default("init"),
        dither: BOOLEAN = Default("true"),
        aspect: RATIONAL = Default("1/1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make or reverse a vignette effect.

        Parameters:
        ----------

        :param STRING angle: set lens angle (default "PI/5")
        :param STRING x0: set circle center position on x-axis (default "w/2")
        :param STRING y0: set circle center position on y-axis (default "h/2")
        :param INT mode: set forward/backward mode (from 0 to 1) (default forward)
        :param INT eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param BOOLEAN dither: set dithering (default true)
        :param RATIONAL aspect: set aspect ratio (from 0 to DBL_MAX) (default 1/1)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vignette

        """
        filter_node = FilterNode(
            name="vignette",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "angle": angle,
                        "x0": x0,
                        "y0": y0,
                        "mode": mode,
                        "eval": eval,
                        "dither": dither,
                        "aspect": aspect,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def vmafmotion(self, *, stats_file: STRING = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Calculate the VMAF Motion score.

        Parameters:
        ----------

        :param STRING stats_file: Set file where to store per-frame difference information

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vmafmotion

        """
        filter_node = FilterNode(
            name="vmafmotion",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "stats_file": stats_file,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def w3fdif(
        self,
        *,
        filter: INT | Literal["simple", "complex"] | Default = Default("complex"),
        mode: INT | Literal["frame", "field"] | Default = Default("field"),
        parity: INT | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: INT | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Martin Weston three field deinterlace.

        Parameters:
        ----------

        :param INT filter: specify the filter (from 0 to 1) (default complex)
        :param INT mode: specify the interlacing mode (from 0 to 1) (default field)
        :param INT parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param INT deint: specify which frames to deinterlace (from 0 to 1) (default all)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#w3fdif

        """
        filter_node = FilterNode(
            name="w3fdif",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filter": filter,
                        "mode": mode,
                        "parity": parity,
                        "deint": deint,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def waveform(
        self,
        *,
        mode: INT | Literal["row", "column"] | Default = Default("column"),
        intensity: FLOAT = Default("0.04"),
        mirror: BOOLEAN = Default("true"),
        display: INT | Literal["overlay", "stack", "parade"] | Default = Default("stack"),
        components: INT = Default("1"),
        envelope: INT | Literal["none", "instant", "peak", "instant"] | Default = Default("none"),
        filter: INT
        | Literal["lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"]
        | Default = Default("lowpass"),
        graticule: INT | Literal["none", "green", "orange", "invert"] | Default = Default("none"),
        opacity: FLOAT = Default("0.75"),
        flags: FLAGS | Literal["numbers", "dots"] | Default = Default("numbers"),
        scale: INT | Literal["digital", "millivolts", "ire"] | Default = Default("digital"),
        bgopacity: FLOAT = Default("0.75"),
        tint0: FLOAT = Default("0"),
        tint1: FLOAT = Default("0"),
        fitmode: INT | Literal["none", "size"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video waveform monitor.

        Parameters:
        ----------

        :param INT mode: set mode (from 0 to 1) (default column)
        :param FLOAT intensity: set intensity (from 0 to 1) (default 0.04)
        :param BOOLEAN mirror: set mirroring (default true)
        :param INT display: set display mode (from 0 to 2) (default stack)
        :param INT components: set components to display (from 1 to 15) (default 1)
        :param INT envelope: set envelope to display (from 0 to 3) (default none)
        :param INT filter: set filter (from 0 to 7) (default lowpass)
        :param INT graticule: set graticule (from 0 to 3) (default none)
        :param FLOAT opacity: set graticule opacity (from 0 to 1) (default 0.75)
        :param FLAGS flags: set graticule flags (default numbers)
        :param INT scale: set scale (from 0 to 2) (default digital)
        :param FLOAT bgopacity: set background opacity (from 0 to 1) (default 0.75)
        :param FLOAT tint0: set 1st tint (from -1 to 1) (default 0)
        :param FLOAT tint1: set 2nd tint (from -1 to 1) (default 0)
        :param INT fitmode: set fit mode (from 0 to 1) (default none)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#waveform

        """
        filter_node = FilterNode(
            name="waveform",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "intensity": intensity,
                        "mirror": mirror,
                        "display": display,
                        "components": components,
                        "envelope": envelope,
                        "filter": filter,
                        "graticule": graticule,
                        "opacity": opacity,
                        "flags": flags,
                        "scale": scale,
                        "bgopacity": bgopacity,
                        "tint0": tint0,
                        "tint1": tint1,
                        "fitmode": fitmode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def weave(
        self, *, first_field: INT | Literal["top", "t", "bottom", "b"] | Default = Default("top"), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into frames.

        Parameters:
        ----------

        :param INT first_field: set first field (from 0 to 1) (default top)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        filter_node = FilterNode(
            name="weave",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "first_field": first_field,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def xbr(self, *, n: INT = Default("3"), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using xBR algorithm.

        Parameters:
        ----------

        :param INT n: set scale factor (from 2 to 4) (default 3)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xbr

        """
        filter_node = FilterNode(
            name="xbr",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "n": n,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def xcorrelate(
        self,
        _secondary: "VideoStream",
        *,
        planes: INT = Default("7"),
        secondary: INT | Literal["first", "all"] | Default = Default("all"),
        eof_action: INT | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: BOOLEAN = Default("false"),
        repeatlast: BOOLEAN = Default("true"),
        ts_sync_mode: INT | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
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
                self,
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
        self,
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
        **kwargs: Any,
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
                self,
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

    def yadif(
        self,
        *,
        mode: INT
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("send_frame"),
        parity: INT | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: INT | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param INT mode: specify the interlacing mode (from 0 to 3) (default send_frame)
        :param INT parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param INT deint: specify which frames to deinterlace (from 0 to 1) (default all)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yadif

        """
        filter_node = FilterNode(
            name="yadif",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "parity": parity,
                        "deint": deint,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def yaepblur(
        self,
        *,
        radius: INT = Default("3"),
        planes: INT = Default("1"),
        sigma: INT = Default("128"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Yet another edge preserving blur filter.

        Parameters:
        ----------

        :param INT radius: set window radius (from 0 to INT_MAX) (default 3)
        :param INT planes: set planes to filter (from 0 to 15) (default 1)
        :param INT sigma: set blur strength (from 1 to INT_MAX) (default 128)
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yaepblur

        """
        filter_node = FilterNode(
            name="yaepblur",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "radius": radius,
                        "planes": planes,
                        "sigma": sigma,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def zmq(self, *, bind_address: STRING = Default("tcp://*:5555"), **kwargs: Any) -> "VideoStream":
        """

        Receive commands through ZMQ and broker them to filters.

        Parameters:
        ----------

        :param STRING bind_address: set bind address (default "tcp://*:5555")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zmq_002c-azmq

        """
        filter_node = FilterNode(
            name="zmq",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
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
        return filter_node.video(0)

    def zoompan(
        self,
        *,
        zoom: STRING = Default("1"),
        x: STRING = Default("0"),
        y: STRING = Default("0"),
        d: STRING = Default("90"),
        s: IMAGE_SIZE = Default("hd720"),
        fps: VIDEO_RATE = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Zoom & Pan effect.

        Parameters:
        ----------

        :param STRING zoom: set the zoom expression (default "1")
        :param STRING x: set the x expression (default "0")
        :param STRING y: set the y expression (default "0")
        :param STRING d: set the duration expression (default "90")
        :param IMAGE_SIZE s: set the output image size (default "hd720")
        :param VIDEO_RATE fps: set the output framerate (default "25")

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zoompan

        """
        filter_node = FilterNode(
            name="zoompan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "zoom": zoom,
                        "x": x,
                        "y": y,
                        "d": d,
                        "s": s,
                        "fps": fps,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def zscale(
        self,
        *,
        w: STRING = Default(None),
        h: STRING = Default(None),
        size: STRING = Default(None),
        dither: INT | Literal["none", "ordered", "random", "error_diffusion"] | Default = Default("none"),
        filter: INT
        | Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | Default = Default("bilinear"),
        out_range: INT | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default("input"),
        primaries: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "p22",
            "ebu3213",
        ]
        | Default = Default("input"),
        transfer: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "10",
            "12",
            "smpte2084",
            "4",
            "1",
            "b67",
        ]
        | Default = Default("input"),
        matrix: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "nc",
            "c",
            "ictcp",
        ]
        | Default = Default("input"),
        in_range: INT | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default("input"),
        primariesin: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "p22",
            "ebu3213",
        ]
        | Default = Default("input"),
        transferin: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "10",
            "12",
            "smpte2084",
            "4",
            "1",
            "b67",
        ]
        | Default = Default("input"),
        matrixin: INT
        | Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "nc",
            "c",
            "ictcp",
        ]
        | Default = Default("input"),
        chromal: INT
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default("input"),
        chromalin: INT
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default("input"),
        npl: DOUBLE = Default("nan"),
        agamma: BOOLEAN = Default("true"),
        param_a: DOUBLE = Default("nan"),
        param_b: DOUBLE = Default("nan"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply resizing, colorspace and bit depth conversion.

        Parameters:
        ----------

        :param STRING w: Output video width
        :param STRING h: Output video height
        :param STRING size: set video size
        :param INT dither: set dither type (from 0 to 3) (default none)
        :param INT filter: set filter type (from 0 to 5) (default bilinear)
        :param INT out_range: set color range (from -1 to 1) (default input)
        :param INT primaries: set color primaries (from -1 to INT_MAX) (default input)
        :param INT transfer: set transfer characteristic (from -1 to INT_MAX) (default input)
        :param INT matrix: set colorspace matrix (from -1 to INT_MAX) (default input)
        :param INT in_range: set input color range (from -1 to 1) (default input)
        :param INT primariesin: set input color primaries (from -1 to INT_MAX) (default input)
        :param INT transferin: set input transfer characteristic (from -1 to INT_MAX) (default input)
        :param INT matrixin: set input colorspace matrix (from -1 to INT_MAX) (default input)
        :param INT chromal: set output chroma location (from -1 to 5) (default input)
        :param INT chromalin: set input chroma location (from -1 to 5) (default input)
        :param DOUBLE npl: set nominal peak luminance (from 0 to DBL_MAX) (default nan)
        :param BOOLEAN agamma: allow approximate gamma (default true)
        :param DOUBLE param_a: parameter A, which is parameter "b" for bicubic, and the number of filter taps for lanczos (from -DBL_MAX to DBL_MAX) (default nan)
        :param DOUBLE param_b: parameter B, which is parameter "c" for bicubic (from -DBL_MAX to DBL_MAX) (default nan)

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zscale

        """
        filter_node = FilterNode(
            name="zscale",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "w": w,
                        "h": h,
                        "size": size,
                        "dither": dither,
                        "filter": filter,
                        "out_range": out_range,
                        "primaries": primaries,
                        "transfer": transfer,
                        "matrix": matrix,
                        "in_range": in_range,
                        "primariesin": primariesin,
                        "transferin": transferin,
                        "matrixin": matrixin,
                        "chromal": chromal,
                        "chromalin": chromalin,
                        "npl": npl,
                        "agamma": agamma,
                        "param_a": param_a,
                        "param_b": param_b,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)
