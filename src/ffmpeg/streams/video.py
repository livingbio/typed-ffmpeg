from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from ..nodes.nodes import FilterableStream, FilterNode
from ..schema import (
    Boolean,
    Color,
    Default,
    Double,
    Duration,
    Flags,
    Float,
    Image_size,
    Int,
    Int64,
    Rational,
    StreamType,
    String,
    Video_rate,
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
        x: String = Default("0"),
        y: String = Default("0"),
        w: String = Default("0"),
        h: String = Default("0"),
        qoffset: Rational = Default("-1/10"),
        clear: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add region of interest to frame.

        Parameters:
        ----------

        :param String x: Region distance from left edge of frame. (default "0")
        :param String y: Region distance from top edge of frame. (default "0")
        :param String w: Region width. (default "0")
        :param String h: Region height. (default "0")
        :param Rational qoffset: Quantisation offset to apply in the region. (from -1 to 1) (default -1/10)
        :param Boolean clear: Remove any existing regions of interest before adding the new one. (default false)

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
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Copy the luma value of the second input into the alpha channel of the first input.

        Parameters:
        ----------

        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        radius: Int = Default(2),
        factor: Float = Default(2.0),
        threshold: Float = Default(10.0),
        tolerance: Float = Default(0.0),
        low: Float = Default(65535.0),
        high: Float = Default(65535.0),
        planes: Flags = Default("7"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Amplify changes between successive video frames.

        Parameters:
        ----------

        :param Int radius: set radius (from 1 to 63) (default 2)
        :param Float factor: set factor (from 0 to 65535) (default 2)
        :param Float threshold: set threshold (from 0 to 65535) (default 10)
        :param Float tolerance: set tolerance (from 0 to 65535) (default 0)
        :param Float low: set low limit for amplification (from 0 to 65535) (default 65535)
        :param Float high: set high limit for amplification (from 0 to 65535) (default 65535)
        :param Flags planes: set what planes to filter (default 7)
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
        filename: String = Default(None),
        original_size: Image_size = Default(None),
        fontsdir: String = Default(None),
        alpha: Boolean = Default(False),
        shaping: Int | Literal["auto", "simple", "complex"] | Default = Default("auto"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render ASS subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param String filename: set the filename of file to read
        :param Image_size original_size: set the size of the original video (used to scale fonts)
        :param String fontsdir: set the directory containing the fonts to read
        :param Boolean alpha: enable processing of alpha channel (default false)
        :param Int shaping: set shaping engine (from -1 to 1) (default auto)

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
        _0a: Float = Default(0.02),
        _0b: Float = Default(0.04),
        _1a: Float = Default(0.02),
        _1b: Float = Default(0.04),
        _2a: Float = Default(0.02),
        _2b: Float = Default(0.04),
        s: Int = Default(9),
        p: Flags = Default("7"),
        a: Int | Literal["p", "s"] | Default = Default("p"),
        _0s: Float = Default(32767.0),
        _1s: Float = Default(32767.0),
        _2s: Float = Default(32767.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an Adaptive Temporal Averaging Denoiser.

        Parameters:
        ----------

        :param Float _0a: set threshold A for 1st plane (from 0 to 0.3) (default 0.02)
        :param Float _0b: set threshold B for 1st plane (from 0 to 5) (default 0.04)
        :param Float _1a: set threshold A for 2nd plane (from 0 to 0.3) (default 0.02)
        :param Float _1b: set threshold B for 2nd plane (from 0 to 5) (default 0.04)
        :param Float _2a: set threshold A for 3rd plane (from 0 to 0.3) (default 0.02)
        :param Float _2b: set threshold B for 3rd plane (from 0 to 5) (default 0.04)
        :param Int s: set how many frames to use (from 5 to 129) (default 9)
        :param Flags p: set what planes to filter (default 7)
        :param Int a: set variant of algorithm (from 0 to 1) (default p)
        :param Float _0s: set sigma for 1st plane (from 0 to 32767) (default 32767)
        :param Float _1s: set sigma for 2nd plane (from 0 to 32767) (default 32767)
        :param Float _2s: set sigma for 3rd plane (from 0 to 32767) (default 32767)
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
        sizeX: Int = Default(1),
        planes: Int = Default(15),
        sizeY: Int = Default(0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Average Blur filter.

        Parameters:
        ----------

        :param Int sizeX: set horizontal size (from 1 to 1024) (default 1)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Int sizeY: set vertical size (from 0 to 1024) (default 0)
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
        threshold: Float = Default(0.08),
        similarity: Float = Default(0.1),
        blend: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a static background into transparency.

        Parameters:
        ----------

        :param Float threshold: set the scene change threshold (from 0 to 1) (default 0.08)
        :param Float similarity: set the similarity (from 0 to 1) (default 0.1)
        :param Float blend: set the blend value (from 0 to 1) (default 0)
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

    def bbox(self, *, min_val: Int = Default(16), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Compute bounding box for each frame.

        Parameters:
        ----------

        :param Int min_val: set minimum luminance value for bounding box (from 0 to 65535) (default 16)
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
        self, *, action: Int | Literal["start", "stop"] | Default = Default("start"), **kwargs: Any
    ) -> "VideoStream":
        """

        Benchmark part of a filtergraph.

        Parameters:
        ----------

        :param Int action: set action (from 0 to 1) (default start)

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
        sigmaS: Float = Default(0.1),
        sigmaR: Float = Default(0.1),
        planes: Int = Default(1),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Bilateral filter.

        Parameters:
        ----------

        :param Float sigmaS: set spatial sigma (from 0 to 512) (default 0.1)
        :param Float sigmaR: set range sigma (from 0 to 1) (default 0.1)
        :param Int planes: set planes to filter (from 0 to 15) (default 1)
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
        bitplane: Int = Default(1),
        filter: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure bit plane noise.

        Parameters:
        ----------

        :param Int bitplane: set bit plane to use for measuring noise (from 1 to 16) (default 1)
        :param Boolean filter: show noisy pixels (default false)
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
        d: Double = Default(2.0),
        picture_black_ratio_th: Double = Default(0.98),
        pixel_black_th: Double = Default(0.1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect video intervals that are (almost) black.

        Parameters:
        ----------

        :param Double d: set minimum detected black duration in seconds (from 0 to DBL_MAX) (default 2)
        :param Double picture_black_ratio_th: set the picture black ratio threshold (from 0 to 1) (default 0.98)
        :param Double pixel_black_th: set the pixel black threshold (from 0 to 1) (default 0.1)

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

    def blackframe(self, *, amount: Int = Default(98), threshold: Int = Default(32), **kwargs: Any) -> "VideoStream":
        """

        Detect frames that are (almost) black.

        Parameters:
        ----------

        :param Int amount: percentage of the pixels that have to be below the threshold for the frame to be considered black (from 0 to 100) (default 98)
        :param Int threshold: threshold below which a pixel value is considered black (from 0 to 255) (default 32)

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
        c0_mode: Int
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
        c1_mode: Int
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
        c2_mode: Int
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
        c3_mode: Int
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
        all_mode: Int
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
        | Default = Default(-1),
        c0_expr: String = Default(None),
        c1_expr: String = Default(None),
        c2_expr: String = Default(None),
        c3_expr: String = Default(None),
        all_expr: String = Default(None),
        c0_opacity: Double = Default(1.0),
        c1_opacity: Double = Default(1.0),
        c2_opacity: Double = Default(1.0),
        c3_opacity: Double = Default(1.0),
        all_opacity: Double = Default(1.0),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blend two video frames into each other.

        Parameters:
        ----------

        :param Int c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
        :param Int c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
        :param Int c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
        :param Int c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
        :param Int all_mode: set blend mode for all components (from -1 to 39) (default -1)
        :param String c0_expr: set color component #0 expression
        :param String c1_expr: set color component #1 expression
        :param String c2_expr: set color component #2 expression
        :param String c3_expr: set color component #3 expression
        :param String all_expr: set expression for all color components
        :param Double c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
        :param Double c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
        :param Double c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
        :param Double c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
        :param Double all_opacity: set opacity for all color components (from 0 to 1) (default 1)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        self, *, period_min: Int = Default(3), period_max: Int = Default(24), planes: Int = Default(1), **kwargs: Any
    ) -> "VideoStream":
        """

        Blockdetect filter.

        Parameters:
        ----------

        :param Int period_min: Minimum period to search for (from 2 to 32) (default 3)
        :param Int period_max: Maximum period to search for (from 2 to 64) (default 24)
        :param Int planes: set planes to filter (from 0 to 15) (default 1)

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
        high: Float = Default(0.117647),
        low: Float = Default(0.0588235),
        radius: Int = Default(50),
        block_pct: Int = Default(80),
        block_width: Int = Default(-1),
        planes: Int = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blurdetect filter.

        Parameters:
        ----------

        :param Float high: set high threshold (from 0 to 1) (default 0.117647)
        :param Float low: set low threshold (from 0 to 1) (default 0.0588235)
        :param Int radius: search radius for maxima detection (from 1 to 100) (default 50)
        :param Int block_pct: block pooling threshold when calculating blurriness (from 1 to 100) (default 80)
        :param Int block_width: block size for block-based abbreviation of blurriness (from -1 to INT_MAX) (default -1)
        :param Int planes: set planes to filter (from 0 to 15) (default 1)

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
        luma_radius: String = Default("2"),
        luma_power: Int = Default(2),
        chroma_radius: String = Default(None),
        chroma_power: Int = Default(-1),
        alpha_radius: String = Default(None),
        alpha_power: Int = Default(-1),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input.

        Parameters:
        ----------

        :param String luma_radius: Radius of the luma blurring box (default "2")
        :param Int luma_power: How many times should the boxblur be applied to luma (from 0 to INT_MAX) (default 2)
        :param String chroma_radius: Radius of the chroma blurring box
        :param Int chroma_power: How many times should the boxblur be applied to chroma (from -1 to INT_MAX) (default -1)
        :param String alpha_radius: Radius of the alpha blurring box
        :param Int alpha_power: How many times should the boxblur be applied to alpha (from -1 to INT_MAX) (default -1)
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
        mode: Int | Literal["send_frame", "send_field"] | Default = Default("send_field"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param Int mode: specify the interlacing mode (from 0 to 1) (default send_field)
        :param Int parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param Int deint: specify which frames to deinterlace (from 0 to 1) (default all)
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
        strength: Float = Default(0.0),
        planes: Flags = Default("7"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Contrast Adaptive Sharpen.

        Parameters:
        ----------

        :param Float strength: set the sharpening strength (from 0 to 1) (default 0)
        :param Flags planes: set what planes to filter (default 7)
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
        color: Color = Default("black"),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        yuv: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray.

        Parameters:
        ----------

        :param Color color: set the chromahold key color (default "black")
        :param Float similarity: set the chromahold similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the chromahold blend value (from 0 to 1) (default 0)
        :param Boolean yuv: color parameter is in yuv instead of rgb (default false)
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
        color: Color = Default("black"),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        yuv: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param Color color: set the chromakey key color (default "black")
        :param Float similarity: set the chromakey similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the chromakey key blend value (from 0 to 1) (default 0)
        :param Boolean yuv: color parameter is in yuv instead of rgb (default false)
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
        thres: Float = Default(30.0),
        sizew: Int = Default(5),
        sizeh: Int = Default(5),
        stepw: Int = Default(1),
        steph: Int = Default(1),
        threy: Float = Default(200.0),
        threu: Float = Default(200.0),
        threv: Float = Default(200.0),
        distance: Int | Literal["manhattan", "euclidean"] | Default = Default("manhattan"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce chrominance noise.

        Parameters:
        ----------

        :param Float thres: set y+u+v threshold (from 1 to 200) (default 30)
        :param Int sizew: set horizontal patch size (from 1 to 100) (default 5)
        :param Int sizeh: set vertical patch size (from 1 to 100) (default 5)
        :param Int stepw: set horizontal step (from 1 to 50) (default 1)
        :param Int steph: set vertical step (from 1 to 50) (default 1)
        :param Float threy: set y threshold (from 1 to 200) (default 200)
        :param Float threu: set u threshold (from 1 to 200) (default 200)
        :param Float threv: set v threshold (from 1 to 200) (default 200)
        :param Int distance: set distance type (from 0 to 1) (default manhattan)
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
        cbh: Int = Default(0),
        cbv: Int = Default(0),
        crh: Int = Default(0),
        crv: Int = Default(0),
        edge: Int | Literal["smear", "wrap"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift chroma.

        Parameters:
        ----------

        :param Int cbh: shift chroma-blue horizontally (from -255 to 255) (default 0)
        :param Int cbv: shift chroma-blue vertically (from -255 to 255) (default 0)
        :param Int crh: shift chroma-red horizontally (from -255 to 255) (default 0)
        :param Int crv: shift chroma-red vertically (from -255 to 255) (default 0)
        :param Int edge: set edge operation (from 0 to 1) (default smear)
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
        system: Int
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
        cie: Int | Literal["xyy", "ucs", "luv"] | Default = Default("xyy"),
        gamuts: Flags
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
        size: Int = Default(512),
        intensity: Float = Default(0.001),
        contrast: Float = Default(0.75),
        corrgamma: Boolean = Default(True),
        showwhite: Boolean = Default(False),
        gamma: Double = Default(2.6),
        fill: Boolean = Default(True),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video CIE scope.

        Parameters:
        ----------

        :param Int system: set color system (from 0 to 9) (default hdtv)
        :param Int cie: set cie system (from 0 to 2) (default xyy)
        :param Flags gamuts: set what gamuts to draw (default 0)
        :param Int size: set ciescope size (from 256 to 8192) (default 512)
        :param Float intensity: set ciescope intensity (from 0 to 1) (default 0.001)
        :param Float contrast: (from 0 to 1) (default 0.75)
        :param Boolean corrgamma: (default true)
        :param Boolean showwhite: (default false)
        :param Double gamma: (from 0.1 to 6) (default 2.6)
        :param Boolean fill: fill with CIE colors (default true)

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
        mv: Flags | Literal["pf", "bf", "bb"] | Default = Default("0"),
        qp: Boolean = Default(False),
        mv_type: Flags | Literal["fp", "bp"] | Default = Default("0"),
        frame_type: Flags | Literal["if", "pf", "bf"] | Default = Default("0"),
        block: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Visualize information about some codecs.

        Parameters:
        ----------

        :param Flags mv: set motion vectors to visualize (default 0)
        :param Boolean qp: (default false)
        :param Flags mv_type: set motion vectors type (default 0)
        :param Flags frame_type: set frame types to visualize motion vectors of (default 0)
        :param Boolean block: set block partitioning structure to visualize (default false)
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
        rs: Float = Default(0.0),
        gs: Float = Default(0.0),
        bs: Float = Default(0.0),
        rm: Float = Default(0.0),
        gm: Float = Default(0.0),
        bm: Float = Default(0.0),
        rh: Float = Default(0.0),
        gh: Float = Default(0.0),
        bh: Float = Default(0.0),
        pl: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color balance.

        Parameters:
        ----------

        :param Float rs: set red shadows (from -1 to 1) (default 0)
        :param Float gs: set green shadows (from -1 to 1) (default 0)
        :param Float bs: set blue shadows (from -1 to 1) (default 0)
        :param Float rm: set red midtones (from -1 to 1) (default 0)
        :param Float gm: set green midtones (from -1 to 1) (default 0)
        :param Float bm: set blue midtones (from -1 to 1) (default 0)
        :param Float rh: set red highlights (from -1 to 1) (default 0)
        :param Float gh: set green highlights (from -1 to 1) (default 0)
        :param Float bh: set blue highlights (from -1 to 1) (default 0)
        :param Boolean pl: preserve lightness (default false)
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
        rr: Double = Default(1.0),
        rg: Double = Default(0.0),
        rb: Double = Default(0.0),
        ra: Double = Default(0.0),
        gr: Double = Default(0.0),
        gg: Double = Default(1.0),
        gb: Double = Default(0.0),
        ga: Double = Default(0.0),
        br: Double = Default(0.0),
        bg: Double = Default(0.0),
        bb: Double = Default(1.0),
        ba: Double = Default(0.0),
        ar: Double = Default(0.0),
        ag: Double = Default(0.0),
        ab: Double = Default(0.0),
        aa: Double = Default(1.0),
        pc: Int | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default("none"),
        pa: Double = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors by mixing color channels.

        Parameters:
        ----------

        :param Double rr: set the red gain for the red channel (from -2 to 2) (default 1)
        :param Double rg: set the green gain for the red channel (from -2 to 2) (default 0)
        :param Double rb: set the blue gain for the red channel (from -2 to 2) (default 0)
        :param Double ra: set the alpha gain for the red channel (from -2 to 2) (default 0)
        :param Double gr: set the red gain for the green channel (from -2 to 2) (default 0)
        :param Double gg: set the green gain for the green channel (from -2 to 2) (default 1)
        :param Double gb: set the blue gain for the green channel (from -2 to 2) (default 0)
        :param Double ga: set the alpha gain for the green channel (from -2 to 2) (default 0)
        :param Double br: set the red gain for the blue channel (from -2 to 2) (default 0)
        :param Double bg: set the green gain for the blue channel (from -2 to 2) (default 0)
        :param Double bb: set the blue gain for the blue channel (from -2 to 2) (default 1)
        :param Double ba: set the alpha gain for the blue channel (from -2 to 2) (default 0)
        :param Double ar: set the red gain for the alpha channel (from -2 to 2) (default 0)
        :param Double ag: set the green gain for the alpha channel (from -2 to 2) (default 0)
        :param Double ab: set the blue gain for the alpha channel (from -2 to 2) (default 0)
        :param Double aa: set the alpha gain for the alpha channel (from -2 to 2) (default 1)
        :param Int pc: set the preserve color mode (from 0 to 6) (default none)
        :param Double pa: set the preserve color amount (from 0 to 1) (default 0)
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
        rc: Float = Default(0.0),
        gm: Float = Default(0.0),
        by: Float = Default(0.0),
        rcw: Float = Default(0.0),
        gmw: Float = Default(0.0),
        byw: Float = Default(0.0),
        pl: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color contrast between RGB components.

        Parameters:
        ----------

        :param Float rc: set the red-cyan contrast (from -1 to 1) (default 0)
        :param Float gm: set the green-magenta contrast (from -1 to 1) (default 0)
        :param Float by: set the blue-yellow contrast (from -1 to 1) (default 0)
        :param Float rcw: set the red-cyan weight (from 0 to 1) (default 0)
        :param Float gmw: set the green-magenta weight (from 0 to 1) (default 0)
        :param Float byw: set the blue-yellow weight (from 0 to 1) (default 0)
        :param Float pl: set the amount of preserving lightness (from 0 to 1) (default 0)
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
        rl: Float = Default(0.0),
        bl: Float = Default(0.0),
        rh: Float = Default(0.0),
        bh: Float = Default(0.0),
        saturation: Float = Default(1.0),
        analyze: Int | Literal["manual", "average", "minmax", "median"] | Default = Default("manual"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color white balance selectively for blacks and whites.

        Parameters:
        ----------

        :param Float rl: set the red shadow spot (from -1 to 1) (default 0)
        :param Float bl: set the blue shadow spot (from -1 to 1) (default 0)
        :param Float rh: set the red highlight spot (from -1 to 1) (default 0)
        :param Float bh: set the blue highlight spot (from -1 to 1) (default 0)
        :param Float saturation: set the amount of saturation (from -3 to 3) (default 1)
        :param Int analyze: set the analyze mode (from 0 to 3) (default manual)
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
        color: Color = Default("black"),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray. Operates on RGB colors.

        Parameters:
        ----------

        :param Color color: set the colorhold key color (default "black")
        :param Float similarity: set the colorhold similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the colorhold blend value (from 0 to 1) (default 0)
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
        hue: Float = Default(0.0),
        saturation: Float = Default(0.5),
        lightness: Float = Default(0.5),
        mix: Float = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Overlay a solid color on the video stream.

        Parameters:
        ----------

        :param Float hue: set the hue (from 0 to 360) (default 0)
        :param Float saturation: set the saturation (from 0 to 1) (default 0.5)
        :param Float lightness: set the lightness (from 0 to 1) (default 0.5)
        :param Float mix: set the mix of source lightness (from 0 to 1) (default 1)
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
        color: Color = Default("black"),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on RGB colors.

        Parameters:
        ----------

        :param Color color: set the colorkey key color (default "black")
        :param Float similarity: set the colorkey similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the colorkey key blend value (from 0 to 1) (default 0)
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
        rimin: Double = Default(0.0),
        gimin: Double = Default(0.0),
        bimin: Double = Default(0.0),
        aimin: Double = Default(0.0),
        rimax: Double = Default(1.0),
        gimax: Double = Default(1.0),
        bimax: Double = Default(1.0),
        aimax: Double = Default(1.0),
        romin: Double = Default(0.0),
        gomin: Double = Default(0.0),
        bomin: Double = Default(0.0),
        aomin: Double = Default(0.0),
        romax: Double = Default(1.0),
        gomax: Double = Default(1.0),
        bomax: Double = Default(1.0),
        aomax: Double = Default(1.0),
        preserve: Int | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default("none"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color levels.

        Parameters:
        ----------

        :param Double rimin: set input red black point (from -1 to 1) (default 0)
        :param Double gimin: set input green black point (from -1 to 1) (default 0)
        :param Double bimin: set input blue black point (from -1 to 1) (default 0)
        :param Double aimin: set input alpha black point (from -1 to 1) (default 0)
        :param Double rimax: set input red white point (from -1 to 1) (default 1)
        :param Double gimax: set input green white point (from -1 to 1) (default 1)
        :param Double bimax: set input blue white point (from -1 to 1) (default 1)
        :param Double aimax: set input alpha white point (from -1 to 1) (default 1)
        :param Double romin: set output red black point (from 0 to 1) (default 0)
        :param Double gomin: set output green black point (from 0 to 1) (default 0)
        :param Double bomin: set output blue black point (from 0 to 1) (default 0)
        :param Double aomin: set output alpha black point (from 0 to 1) (default 0)
        :param Double romax: set output red white point (from 0 to 1) (default 1)
        :param Double gomax: set output green white point (from 0 to 1) (default 1)
        :param Double bomax: set output blue white point (from 0 to 1) (default 1)
        :param Double aomax: set output alpha white point (from 0 to 1) (default 1)
        :param Int preserve: set preserve color mode (from 0 to 6) (default none)
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
        patch_size: Image_size = Default("64x64"),
        nb_patches: Int = Default(0),
        type: Int | Literal["relative", "absolute"] | Default = Default("absolute"),
        kernel: Int | Literal["euclidean", "weuclidean"] | Default = Default("euclidean"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply custom Color Maps to video stream.

        Parameters:
        ----------

        :param Image_size patch_size: set patch size (default "64x64")
        :param Int nb_patches: set number of patches (from 0 to 64) (default 0)
        :param Int type: set the target type used (from 0 to 1) (default absolute)
        :param Int kernel: set the kernel used for measuring color difference (from 0 to 1) (default euclidean)
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
        src: Int
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default(-1),
        dst: Int
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default(-1),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert color matrix.

        Parameters:
        ----------

        :param Int src: set source color matrix (from -1 to 4) (default -1)
        :param Int dst: set destination color matrix (from -1 to 4) (default -1)
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
        all: Int
        | Literal["bt470m", "bt470bg", "525", "625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default(0),
        space: Int
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default(2),
        range: Int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default(0),
        primaries: Int
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
        | Default = Default(2),
        trc: Int
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
        | Default = Default(2),
        format: Int
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
        | Default = Default(-1),
        fast: Boolean = Default(False),
        dither: Int | Literal["none", "fsb"] | Default = Default("none"),
        wpadapt: Int | Literal["bradford", "vonkries", "identity"] | Default = Default("bradford"),
        iall: Int
        | Literal["bt470m", "bt470bg", "525", "625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default(0),
        ispace: Int
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default(2),
        irange: Int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default(0),
        iprimaries: Int
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
        | Default = Default(2),
        itrc: Int
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
        | Default = Default(2),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert between colorspaces.

        Parameters:
        ----------

        :param Int all: Set all color properties together (from 0 to 8) (default 0)
        :param Int space: Output colorspace (from 0 to 14) (default 2)
        :param Int range: Output color range (from 0 to 2) (default 0)
        :param Int primaries: Output color primaries (from 0 to 22) (default 2)
        :param Int trc: Output transfer characteristics (from 0 to 18) (default 2)
        :param Int format: Output pixel format (from -1 to 162) (default -1)
        :param Boolean fast: Ignore primary chromaticity and gamma correction (default false)
        :param Int dither: Dithering mode (from 0 to 1) (default none)
        :param Int wpadapt: Whitepoint adaptation method (from 0 to 2) (default bradford)
        :param Int iall: Set all input color properties together (from 0 to 8) (default 0)
        :param Int ispace: Input colorspace (from 0 to 22) (default 2)
        :param Int irange: Input color range (from 0 to 2) (default 0)
        :param Int iprimaries: Input color primaries (from 0 to 22) (default 2)
        :param Int itrc: Input transfer characteristics (from 0 to 18) (default 2)
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
        temperature: Float = Default(6500.0),
        mix: Float = Default(1.0),
        pl: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color temperature of video.

        Parameters:
        ----------

        :param Float temperature: set the temperature in Kelvin (from 1000 to 40000) (default 6500)
        :param Float mix: set the mix with filtered output (from 0 to 1) (default 1)
        :param Float pl: set the amount of preserving lightness (from 0 to 1) (default 0)
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
        _0m: String = Default("0 0 0 0 1 0 0 0 0"),
        _1m: String = Default("0 0 0 0 1 0 0 0 0"),
        _2m: String = Default("0 0 0 0 1 0 0 0 0"),
        _3m: String = Default("0 0 0 0 1 0 0 0 0"),
        _0rdiv: Float = Default(0.0),
        _1rdiv: Float = Default(0.0),
        _2rdiv: Float = Default(0.0),
        _3rdiv: Float = Default(0.0),
        _0bias: Float = Default(0.0),
        _1bias: Float = Default(0.0),
        _2bias: Float = Default(0.0),
        _3bias: Float = Default(0.0),
        _0mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _1mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _2mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _3mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply convolution filter.

        Parameters:
        ----------

        :param String _0m: set matrix for 1st plane (default "0 0 0 0 1 0 0 0 0")
        :param String _1m: set matrix for 2nd plane (default "0 0 0 0 1 0 0 0 0")
        :param String _2m: set matrix for 3rd plane (default "0 0 0 0 1 0 0 0 0")
        :param String _3m: set matrix for 4th plane (default "0 0 0 0 1 0 0 0 0")
        :param Float _0rdiv: set rdiv for 1st plane (from 0 to INT_MAX) (default 0)
        :param Float _1rdiv: set rdiv for 2nd plane (from 0 to INT_MAX) (default 0)
        :param Float _2rdiv: set rdiv for 3rd plane (from 0 to INT_MAX) (default 0)
        :param Float _3rdiv: set rdiv for 4th plane (from 0 to INT_MAX) (default 0)
        :param Float _0bias: set bias for 1st plane (from 0 to INT_MAX) (default 0)
        :param Float _1bias: set bias for 2nd plane (from 0 to INT_MAX) (default 0)
        :param Float _2bias: set bias for 3rd plane (from 0 to INT_MAX) (default 0)
        :param Float _3bias: set bias for 4th plane (from 0 to INT_MAX) (default 0)
        :param Int _0mode: set matrix mode for 1st plane (from 0 to 2) (default square)
        :param Int _1mode: set matrix mode for 2nd plane (from 0 to 2) (default square)
        :param Int _2mode: set matrix mode for 3rd plane (from 0 to 2) (default square)
        :param Int _3mode: set matrix mode for 4th plane (from 0 to 2) (default square)
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
        planes: Int = Default(7),
        impulse: Int | Literal["first", "all"] | Default = Default("all"),
        noise: Float = Default(1e-07),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convolve first video stream with second video stream.

        Parameters:
        ----------

        :param Int planes: set planes to convolve (from 0 to 15) (default 7)
        :param Int impulse: when to process impulses (from 0 to 1) (default all)
        :param Float noise: set noise (from 0 to 1) (default 1e-07)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        list_filters: Boolean = Default(False),
        list_generators: Boolean = Default(False),
        filter: String = Default(None),
        output_rect: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video filtering using CoreImage API.

        Parameters:
        ----------

        :param Boolean list_filters: list available filters (default false)
        :param Boolean list_generators: list available generators (default false)
        :param String filter: names and options of filters to apply
        :param String output_rect: output rectangle within output image

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
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the correlation between two video streams.

        Parameters:
        ----------

        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        cover: String = Default(None),
        mode: Int | Literal["cover", "blur"] | Default = Default("blur"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find and cover a user specified object.

        Parameters:
        ----------

        :param String cover: cover bitmap filename
        :param Int mode: set removal mode (from 0 to 1) (default blur)

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
        out_w: String = Default("iw"),
        out_h: String = Default("ih"),
        x: String = Default("(in_w-out_w"),
        y: String = Default("(in_h-out_h"),
        keep_aspect: Boolean = Default(False),
        exact: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Crop the input video.

        Parameters:
        ----------

        :param String out_w: set the width crop area expression (default "iw")
        :param String out_h: set the height crop area expression (default "ih")
        :param String x: set the x crop area expression (default "(in_w-out_w)/2")
        :param String y: set the y crop area expression (default "(in_h-out_h)/2")
        :param Boolean keep_aspect: keep aspect ratio (default false)
        :param Boolean exact: do exact cropping (default false)

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
        limit: Float = Default(0.0941176),
        round: Int = Default(16),
        reset: Int = Default(0),
        skip: Int = Default(2),
        reset_count: Int = Default(0),
        max_outliers: Int = Default(0),
        mode: Int | Literal["black", "mvedges"] | Default = Default("black"),
        high: Float = Default(0.0980392),
        low: Float = Default(0.0588235),
        mv_threshold: Int = Default(8),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Auto-detect crop size.

        Parameters:
        ----------

        :param Float limit: Threshold below which the pixel is considered black (from 0 to 65535) (default 0.0941176)
        :param Int round: Value by which the width/height should be divisible (from 0 to INT_MAX) (default 16)
        :param Int reset: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
        :param Int skip: Number of initial frames to skip (from 0 to INT_MAX) (default 2)
        :param Int reset_count: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
        :param Int max_outliers: Threshold count of outliers (from 0 to INT_MAX) (default 0)
        :param Int mode: set mode (from 0 to 1) (default black)
        :param Float high: Set high threshold for edge detection (from 0 to 1) (default 0.0980392)
        :param Float low: Set low threshold for edge detection (from 0 to 1) (default 0.0588235)
        :param Int mv_threshold: motion vector threshold when estimating video window size (from 0 to 100) (default 8)
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
        cue: Int64 = Default(0),
        preroll: Duration = Default(0.0),
        buffer: Duration = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Delay filtering to match a cue.

        Parameters:
        ----------

        :param Int64 cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
        :param Duration preroll: preroll duration in seconds (default 0)
        :param Duration buffer: buffer duration in seconds (default 0)

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
        preset: Int
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
        master: String = Default(None),
        red: String = Default(None),
        green: String = Default(None),
        blue: String = Default(None),
        all: String = Default(None),
        psfile: String = Default(None),
        plot: String = Default(None),
        interp: Int | Literal["natural", "pchip"] | Default = Default("natural"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust components curves.

        Parameters:
        ----------

        :param Int preset: select a color curves preset (from 0 to 10) (default none)
        :param String master: set master points coordinates
        :param String red: set red points coordinates
        :param String green: set green points coordinates
        :param String blue: set blue points coordinates
        :param String all: set points coordinates for all components
        :param String psfile: set Photoshop curves file name
        :param String plot: save Gnuplot script of the curves in specified file
        :param Int interp: specify the kind of interpolation (from 0 to 1) (default natural)
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
        size: Image_size = Default("hd720"),
        x: Int = Default(0),
        y: Int = Default(0),
        mode: Int | Literal["mono", "color", "color2"] | Default = Default("mono"),
        axis: Boolean = Default(False),
        opacity: Float = Default(0.75),
        format: Int | Literal["hex", "dec"] | Default = Default("hex"),
        components: Int = Default(15),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video data analysis.

        Parameters:
        ----------

        :param Image_size size: set output size (default "hd720")
        :param Int x: set x offset (from 0 to INT_MAX) (default 0)
        :param Int y: set y offset (from 0 to INT_MAX) (default 0)
        :param Int mode: set scope mode (from 0 to 2) (default mono)
        :param Boolean axis: draw column/row numbers (default false)
        :param Float opacity: set background opacity (from 0 to 1) (default 0.75)
        :param Int format: set display number format (from 0 to 1) (default hex)
        :param Int components: set components to display (from 1 to 15) (default 15)

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
        angle: Float = Default(45.0),
        radius: Float = Default(5.0),
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Directional Blur filter.

        Parameters:
        ----------

        :param Float angle: set angle (from 0 to 360) (default 45)
        :param Float radius: set radius (from 0 to 8192) (default 5)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
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
        sigma: Float = Default(0.0),
        overlap: Int = Default(-1),
        expr: String = Default(None),
        n: Int = Default(3),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise frames using 2D DCT.

        Parameters:
        ----------

        :param Float sigma: set noise sigma constant (from 0 to 999) (default 0)
        :param Int overlap: set number of block overlapping pixels (from -1 to 15) (default -1)
        :param String expr: set coefficient factor expression
        :param Int n: set the block size, expressed in bits (from 3 to 4) (default 3)
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
        _1thr: Float = Default(0.02),
        _2thr: Float = Default(0.02),
        _3thr: Float = Default(0.02),
        _4thr: Float = Default(0.02),
        range: Int = Default(16),
        direction: Float = Default(6.28319),
        blur: Boolean = Default(True),
        coupling: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Debands video.

        Parameters:
        ----------

        :param Float _1thr: set 1st plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param Float _2thr: set 2nd plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param Float _3thr: set 3rd plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param Float _4thr: set 4th plane threshold (from 3e-05 to 0.5) (default 0.02)
        :param Int range: set range (from INT_MIN to INT_MAX) (default 16)
        :param Float direction: set direction (from -6.28319 to 6.28319) (default 6.28319)
        :param Boolean blur: set blur (default true)
        :param Boolean coupling: set plane coupling (default false)
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
        filter: Int | Literal["weak", "strong"] | Default = Default("strong"),
        block: Int = Default(8),
        alpha: Float = Default(0.098),
        beta: Float = Default(0.05),
        gamma: Float = Default(0.05),
        delta: Float = Default(0.05),
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deblock video.

        Parameters:
        ----------

        :param Int filter: set type of filter (from 0 to 1) (default strong)
        :param Int block: set size of block (from 4 to 512) (default 8)
        :param Float alpha: set 1st detection threshold (from 0 to 1) (default 0.098)
        :param Float beta: set 2nd detection threshold (from 0 to 1) (default 0.05)
        :param Float gamma: set 3rd detection threshold (from 0 to 1) (default 0.05)
        :param Float delta: set 4th detection threshold (from 0 to 1) (default 0.05)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
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
        planes: Int = Default(7),
        impulse: Int | Literal["first", "all"] | Default = Default("all"),
        noise: Float = Default(1e-07),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deconvolve first video stream with second video stream.

        Parameters:
        ----------

        :param Int planes: set planes to deconvolve (from 0 to 15) (default 7)
        :param Int impulse: when to process impulses (from 0 to 1) (default all)
        :param Float noise: set noise (from 0 to 1) (default 1e-07)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        m: Flags | Literal["dotcrawl", "rainbows"] | Default = Default("dotcrawl+rainbows"),
        lt: Float = Default(0.079),
        tl: Float = Default(0.079),
        tc: Float = Default(0.058),
        ct: Float = Default(0.019),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce cross-luminance and cross-color.

        Parameters:
        ----------

        :param Flags m: set filtering mode (default dotcrawl+rainbows)
        :param Float lt: set spatial luma threshold (from 0 to 1) (default 0.079)
        :param Float tl: set tolerance for temporal luma (from 0 to 1) (default 0.079)
        :param Float tc: set tolerance for chroma temporal variation (from 0 to 1) (default 0.058)
        :param Float ct: set temporal chroma threshold (from 0 to 1) (default 0.019)
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
        threshold0: Int = Default(65535),
        threshold1: Int = Default(65535),
        threshold2: Int = Default(65535),
        threshold3: Int = Default(65535),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply deflate effect.

        Parameters:
        ----------

        :param Int threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param Int threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param Int threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param Int threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
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
        size: Int = Default(5),
        mode: Int | Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | Default = Default("am"),
        bypass: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove temporal frame luminance variations.

        Parameters:
        ----------

        :param Int size: set how many frames to use (from 2 to 129) (default 5)
        :param Int mode: set how to smooth luminance (from 0 to 6) (default am)
        :param Boolean bypass: leave frames unchanged (default false)

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

    def dejudder(self, *, cycle: Int = Default(4), **kwargs: Any) -> "VideoStream":
        """

        Remove judder produced by pullup.

        Parameters:
        ----------

        :param Int cycle: set the length of the cycle to use for dejuddering (from 2 to 240) (default 4)

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
        x: String = Default("-1"),
        y: String = Default("-1"),
        w: String = Default("-1"),
        h: String = Default("-1"),
        show: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove logo from input video.

        Parameters:
        ----------

        :param String x: set logo x position (default "-1")
        :param String y: set logo y position (default "-1")
        :param String w: set logo width (default "-1")
        :param String h: set logo height (default "-1")
        :param Boolean show: show delogo area (default false)
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
        filter_type: Int | Literal["derain", "dehaze"] | Default = Default("derain"),
        dnn_backend: Int | Literal["native"] | Default = Default("native"),
        model: String = Default(None),
        input: String = Default("x"),
        output: String = Default("y"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply derain filter to the input.

        Parameters:
        ----------

        :param Int filter_type: filter type(derain/dehaze) (from 0 to 1) (default derain)
        :param Int dnn_backend: DNN backend (from 0 to 1) (default native)
        :param String model: path to model file
        :param String input: input name of the model (default "x")
        :param String output: output name of the model (default "y")
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
        x: Int = Default(-1),
        y: Int = Default(-1),
        w: Int = Default(-1),
        h: Int = Default(-1),
        rx: Int = Default(16),
        ry: Int = Default(16),
        edge: Int | Literal["blank", "original", "clamp", "mirror"] | Default = Default("mirror"),
        blocksize: Int = Default(8),
        contrast: Int = Default(125),
        search: Int | Literal["exhaustive", "less"] | Default = Default("exhaustive"),
        filename: String = Default(None),
        opencl: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Stabilize shaky video.

        Parameters:
        ----------

        :param Int x: set x for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param Int y: set y for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param Int w: set width for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param Int h: set height for the rectangular search area (from -1 to INT_MAX) (default -1)
        :param Int rx: set x for the rectangular search area (from 0 to 64) (default 16)
        :param Int ry: set y for the rectangular search area (from 0 to 64) (default 16)
        :param Int edge: set edge mode (from 0 to 3) (default mirror)
        :param Int blocksize: set motion search blocksize (from 4 to 128) (default 8)
        :param Int contrast: set contrast threshold for blocks (from 1 to 255) (default 125)
        :param Int search: set search strategy (from 0 to 1) (default exhaustive)
        :param String filename: set motion search detailed log file name
        :param Boolean opencl: ignored (default false)

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
        type: Int | Literal["green", "blue"] | Default = Default("green"),
        mix: Float = Default(0.5),
        expand: Float = Default(0.0),
        red: Float = Default(0.0),
        green: Float = Default(-1.0),
        blue: Float = Default(0.0),
        brightness: Float = Default(0.0),
        alpha: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Despill video.

        Parameters:
        ----------

        :param Int type: set the screen type (from 0 to 1) (default green)
        :param Float mix: set the spillmap mix (from 0 to 1) (default 0.5)
        :param Float expand: set the spillmap expand (from 0 to 1) (default 0)
        :param Float red: set red scale (from -100 to 100) (default 0)
        :param Float green: set green scale (from -100 to 100) (default -1)
        :param Float blue: set blue scale (from -100 to 100) (default 0)
        :param Float brightness: set brightness (from -10 to 10) (default 0)
        :param Boolean alpha: change alpha component (default false)
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
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default("top"),
        pattern: String = Default("23"),
        start_frame: Int = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an inverse telecine pattern.

        Parameters:
        ----------

        :param Int first_field: select first field (from 0 to 1) (default top)
        :param String pattern: pattern that describe for how many fields a frame is to be displayed (default "23")
        :param Int start_frame: position of first frame with respect to the pattern if stream is cut (from 0 to 13) (default 0)

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
        coordinates: Int = Default(255),
        threshold0: Int = Default(65535),
        threshold1: Int = Default(65535),
        threshold2: Int = Default(65535),
        threshold3: Int = Default(65535),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply dilation effect.

        Parameters:
        ----------

        :param Int coordinates: set coordinates (from 0 to 255) (default 255)
        :param Int threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param Int threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param Int threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param Int threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
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
        edge: Int | Literal["blank", "smear", "wrap", "mirror"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Displace pixels.

        Parameters:
        ----------

        :param Int edge: set edge mode (from 0 to 3) (default smear)
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
        dnn_backend: Int = Default(2),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default(True),
        confidence: Float = Default(0.5),
        labels: String = Default(None),
        target: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN classify filter to the input.

        Parameters:
        ----------

        :param Int dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
        :param String model: path to model file
        :param String input: input name of the model
        :param String output: output name of the model
        :param String backend_configs: backend configs
        :param String options: backend configs (deprecated, use backend_configs)
        :param Boolean _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
        :param Float confidence: threshold of confidence (from 0 to 1) (default 0.5)
        :param String labels: path to labels file
        :param String target: which one to be classified

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
        dnn_backend: Int = Default(2),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default(True),
        confidence: Float = Default(0.5),
        labels: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN detect filter to the input.

        Parameters:
        ----------

        :param Int dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
        :param String model: path to model file
        :param String input: input name of the model
        :param String output: output name of the model
        :param String backend_configs: backend configs
        :param String options: backend configs (deprecated, use backend_configs)
        :param Boolean _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
        :param Float confidence: threshold of confidence (from 0 to 1) (default 0.5)
        :param String labels: path to labels file

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
        dnn_backend: Int | Literal["native"] | Default = Default("native"),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default(True),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN processing filter to the input.

        Parameters:
        ----------

        :param Int dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default native)
        :param String model: path to model file
        :param String input: input name of the model
        :param String output: output name of the model
        :param String backend_configs: backend configs
        :param String options: backend configs (deprecated, use backend_configs)
        :param Boolean _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)

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
        self, *, first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default("top"), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into double number of frames.

        Parameters:
        ----------

        :param Int first_field: set first field (from 0 to 1) (default top)

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
        x: String = Default("0"),
        y: String = Default("0"),
        width: String = Default("0"),
        height: String = Default("0"),
        color: String = Default("black"),
        thickness: String = Default("3"),
        replace: Boolean = Default(False),
        box_source: String = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored box on the input video.

        Parameters:
        ----------

        :param String x: set horizontal position of the left box edge (default "0")
        :param String y: set vertical position of the top box edge (default "0")
        :param String width: set width of the box (default "0")
        :param String height: set height of the box (default "0")
        :param String color: set color of the box (default "black")
        :param String thickness: set the box thickness (default "3")
        :param Boolean replace: replace color & alpha (default false)
        :param String box_source: use datas from bounding box in side data
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
        slide: Int | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default("frame"),
        size: Image_size = Default("900x256"),
        rate: Video_rate = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a graph using input video metadata.

        Parameters:
        ----------

        :param String m1: set 1st metadata key (default "")
        :param String fg1: set 1st foreground color expression (default "0xffff0000")
        :param String m2: set 2nd metadata key (default "")
        :param String fg2: set 2nd foreground color expression (default "0xff00ff00")
        :param String m3: set 3rd metadata key (default "")
        :param String fg3: set 3rd foreground color expression (default "0xffff00ff")
        :param String m4: set 4th metadata key (default "")
        :param String fg4: set 4th foreground color expression (default "0xffffff00")
        :param Color bg: set background color (default "white")
        :param Float min: set minimal value (from INT_MIN to INT_MAX) (default -1)
        :param Float max: set maximal value (from INT_MIN to INT_MAX) (default 1)
        :param Int mode: set graph mode (from 0 to 2) (default line)
        :param Int slide: set slide mode (from 0 to 4) (default frame)
        :param Image_size size: set graph size (default "900x256")
        :param Video_rate rate: set video rate (default "25")

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
        x: String = Default("0"),
        y: String = Default("0"),
        width: String = Default("0"),
        height: String = Default("0"),
        color: String = Default("black"),
        thickness: String = Default("1"),
        replace: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored grid on the input video.

        Parameters:
        ----------

        :param String x: set horizontal offset (default "0")
        :param String y: set vertical offset (default "0")
        :param String width: set width of grid cell (default "0")
        :param String height: set height of grid cell (default "0")
        :param String color: set color of the grid (default "black")
        :param String thickness: set grid line thickness (default "1")
        :param Boolean replace: replace color & alpha (default false)
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
        fontfile: String = Default(None),
        text: String = Default(None),
        textfile: String = Default(None),
        fontcolor: Color = Default("black"),
        fontcolor_expr: String = Default(""),
        boxcolor: Color = Default("white"),
        bordercolor: Color = Default("black"),
        shadowcolor: Color = Default("black"),
        box: Boolean = Default(False),
        boxborderw: Int = Default(0),
        line_spacing: Int = Default(0),
        fontsize: String = Default(None),
        x: String = Default("0"),
        y: String = Default("0"),
        shadowx: Int = Default(0),
        shadowy: Int = Default(0),
        borderw: Int = Default(0),
        tabsize: Int = Default(4),
        basetime: Int64 = Default("I64_MIN"),
        font: String = Default("Sans"),
        expansion: Int | Literal["none", "normal", "strftime"] | Default = Default("normal"),
        timecode: String = Default(None),
        tc24hmax: Boolean = Default(False),
        timecode_rate: Rational = Default("0/1"),
        reload: Int = Default(0),
        alpha: String = Default("1"),
        fix_bounds: Boolean = Default(False),
        start_number: Int = Default(0),
        text_source: String = Default(None),
        ft_load_flags: Flags
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

        :param String fontfile: set font file
        :param String text: set text
        :param String textfile: set text file
        :param Color fontcolor: set foreground color (default "black")
        :param String fontcolor_expr: set foreground color expression (default "")
        :param Color boxcolor: set box color (default "white")
        :param Color bordercolor: set border color (default "black")
        :param Color shadowcolor: set shadow color (default "black")
        :param Boolean box: set box (default false)
        :param Int boxborderw: set box border width (from INT_MIN to INT_MAX) (default 0)
        :param Int line_spacing: set line spacing in pixels (from INT_MIN to INT_MAX) (default 0)
        :param String fontsize: set font size
        :param String x: set x expression (default "0")
        :param String y: set y expression (default "0")
        :param Int shadowx: set shadow x offset (from INT_MIN to INT_MAX) (default 0)
        :param Int shadowy: set shadow y offset (from INT_MIN to INT_MAX) (default 0)
        :param Int borderw: set border width (from INT_MIN to INT_MAX) (default 0)
        :param Int tabsize: set tab size (from 0 to INT_MAX) (default 4)
        :param Int64 basetime: set base time (from I64_MIN to I64_MAX) (default I64_MIN)
        :param String font: Font name (default "Sans")
        :param Int expansion: set the expansion mode (from 0 to 2) (default normal)
        :param String timecode: set initial timecode
        :param Boolean tc24hmax: set 24 hours max (timecode only) (default false)
        :param Rational timecode_rate: set rate (timecode only) (from 0 to INT_MAX) (default 0/1)
        :param Int reload: reload text file at specified frame interval (from 0 to INT_MAX) (default 0)
        :param String alpha: apply alpha while rendering (default "1")
        :param Boolean fix_bounds: check and fix text coords to avoid clipping (default false)
        :param Int start_number: start frame number for n/frame_num variable (from 0 to INT_MAX) (default 0)
        :param String text_source: the source of text
        :param Flags ft_load_flags: set font loading flags for libfreetype (default 0)
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
        high: Double = Default(0.196078),
        low: Double = Default(0.0784314),
        mode: Int | Literal["wires", "colormix", "canny"] | Default = Default("wires"),
        planes: Flags | Literal["y", "u", "v", "r", "g", "b"] | Default = Default("y+u+v+r+g+b"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect and draw edge.

        Parameters:
        ----------

        :param Double high: set high threshold (from 0 to 1) (default 0.196078)
        :param Double low: set low threshold (from 0 to 1) (default 0.0784314)
        :param Int mode: set mode (from 0 to 2) (default wires)
        :param Flags planes: set planes to filter (default y+u+v+r+g+b)
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
        codebook_length: Int = Default(256),
        nb_steps: Int = Default(1),
        seed: Int64 = Default(-1),
        pal8: Boolean = Default(False),
        use_alpha: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply posterize effect, using the ELBG algorithm.

        Parameters:
        ----------

        :param Int codebook_length: set codebook length (from 1 to INT_MAX) (default 256)
        :param Int nb_steps: set max number of steps used to compute the mapping (from 1 to INT_MAX) (default 1)
        :param Int64 seed: set the random seed (from -1 to UINT32_MAX) (default -1)
        :param Boolean pal8: set the pal8 output (default false)
        :param Boolean use_alpha: use alpha channel for mapping (default false)

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
        mode: Int | Literal["normal", "diff"] | Default = Default("normal"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure video frames entropy.

        Parameters:
        ----------

        :param Int mode: set kind of histogram entropy measurement (from 0 to 1) (default normal)
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

    def epx(self, *, n: Int = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using EPX algorithm.

        Parameters:
        ----------

        :param Int n: set scale factor (from 2 to 3) (default 3)

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
        contrast: String = Default("1.0"),
        brightness: String = Default("0.0"),
        saturation: String = Default("1.0"),
        gamma: String = Default("1.0"),
        gamma_r: String = Default("1.0"),
        gamma_g: String = Default("1.0"),
        gamma_b: String = Default("1.0"),
        gamma_weight: String = Default("1.0"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust brightness, contrast, gamma, and saturation.

        Parameters:
        ----------

        :param String contrast: set the contrast adjustment, negative values give a negative image (default "1.0")
        :param String brightness: set the brightness adjustment (default "0.0")
        :param String saturation: set the saturation adjustment (default "1.0")
        :param String gamma: set the initial gamma value (default "1.0")
        :param String gamma_r: gamma value for red (default "1.0")
        :param String gamma_g: gamma value for green (default "1.0")
        :param String gamma_b: gamma value for blue (default "1.0")
        :param String gamma_weight: set the gamma weight which reduces the effect of gamma on bright areas (default "1.0")
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)
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
        coordinates: Int = Default(255),
        threshold0: Int = Default(65535),
        threshold1: Int = Default(65535),
        threshold2: Int = Default(65535),
        threshold3: Int = Default(65535),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply erosion effect.

        Parameters:
        ----------

        :param Int coordinates: set coordinates (from 0 to 255) (default 255)
        :param Int threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param Int threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param Int threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param Int threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
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
        mode: Int | Literal["frame", "field"] | Default = Default("field"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        rslope: Int = Default(1),
        redge: Int = Default(2),
        ecost: Float = Default(1.0),
        mcost: Float = Default(0.5),
        dcost: Float = Default(0.5),
        interp: Int | Literal["2p", "4p", "6p"] | Default = Default("4p"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Edge Slope Tracing deinterlace.

        Parameters:
        ----------

        :param Int mode: specify the mode (from 0 to 1) (default field)
        :param Int parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param Int deint: specify which frames to deinterlace (from 0 to 1) (default all)
        :param Int rslope: specify the search radius for edge slope tracing (from 1 to 15) (default 1)
        :param Int redge: specify the search radius for best edge matching (from 0 to 15) (default 2)
        :param Float ecost: specify the edge cost for edge matching (from 0 to 9) (default 1)
        :param Float mcost: specify the middle cost for edge matching (from 0 to 1) (default 0.5)
        :param Float dcost: specify the distance cost for edge matching (from 0 to 1) (default 0.5)
        :param Int interp: specify the type of interpolation (from 0 to 2) (default 4p)
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
        self, *, exposure: Float = Default(0.0), black: Float = Default(0.0), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Adjust exposure of the video stream.

        Parameters:
        ----------

        :param Float exposure: set the exposure correction (from -3 to 3) (default 0)
        :param Float black: set the black level correction (from -1 to 1) (default 0)
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
        self, *, planes: Flags | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default("r"), **kwargs: Any
    ) -> FilterNode:
        """

        Extract planes as grayscale frames.

        Parameters:
        ----------

        :param Flags planes: set planes (default r)

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
        type: Int | Literal["in", "out"] | Default = Default("in"),
        start_frame: Int = Default(0),
        nb_frames: Int = Default(25),
        alpha: Boolean = Default(False),
        start_time: Duration = Default(0.0),
        duration: Duration = Default(0.0),
        color: Color = Default("black"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fade in/out input video.

        Parameters:
        ----------

        :param Int type: set the fade direction (from 0 to 1) (default in)
        :param Int start_frame: Number of the first frame to which to apply the effect. (from 0 to INT_MAX) (default 0)
        :param Int nb_frames: Number of frames to which the effect should be applied. (from 1 to INT_MAX) (default 25)
        :param Boolean alpha: fade alpha if it is available on the input (default false)
        :param Duration start_time: Number of seconds of the beginning of the effect. (default 0)
        :param Duration duration: Duration of the effect in seconds. (default 0)
        :param Color color: set color (default "black")
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
        self, _feedin: "VideoStream", *, x: Int = Default(0), w: Int = Default(0), **kwargs: Any
    ) -> tuple["AudioStream", "AudioStream",]:
        """

        Apply feedback video filter.

        Parameters:
        ----------

        :param Int x: set top left crop position (from 0 to INT_MAX) (default 0)
        :param Int w: set crop size (from 0 to INT_MAX) (default 0)

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
            filter_node.audio(0),
            filter_node.audio(1),
        )

    def fftdnoiz(
        self,
        *,
        sigma: Float = Default(1.0),
        amount: Float = Default(1.0),
        block: Int = Default(32),
        overlap: Float = Default(0.5),
        method: Int | Literal["wiener", "hard"] | Default = Default("wiener"),
        prev: Int = Default(0),
        next: Int = Default(0),
        planes: Int = Default(7),
        window: Int
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

        :param Float sigma: set denoise strength (from 0 to 100) (default 1)
        :param Float amount: set amount of denoising (from 0.01 to 1) (default 1)
        :param Int block: set block size (from 8 to 256) (default 32)
        :param Float overlap: set block overlap (from 0.2 to 0.8) (default 0.5)
        :param Int method: set method of denoising (from 0 to 1) (default wiener)
        :param Int prev: set number of previous frames for temporal denoising (from 0 to 1) (default 0)
        :param Int next: set number of next frames for temporal denoising (from 0 to 1) (default 0)
        :param Int planes: set planes to filter (from 0 to 15) (default 7)
        :param Int window: set window function (from 0 to 20) (default hann)
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
        dc_Y: Int = Default(0),
        dc_U: Int = Default(0),
        dc_V: Int = Default(0),
        weight_Y: String = Default("1"),
        weight_U: String = Default(None),
        weight_V: String = Default(None),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply arbitrary expressions to pixels in frequency domain.

        Parameters:
        ----------

        :param Int dc_Y: adjust gain in Y plane (from 0 to 1000) (default 0)
        :param Int dc_U: adjust gain in U plane (from 0 to 1000) (default 0)
        :param Int dc_V: adjust gain in V plane (from 0 to 1000) (default 0)
        :param String weight_Y: set luminance expression in Y plane (default "1")
        :param String weight_U: set chrominance expression in U plane
        :param String weight_V: set chrominance expression in V plane
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)
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

    def field(self, *, type: Int | Literal["top", "bottom"] | Default = Default("top"), **kwargs: Any) -> "VideoStream":
        """

        Extract a field from the input video.

        Parameters:
        ----------

        :param Int type: set field type (top or bottom) (from 0 to 1) (default top)

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
        hint: String = Default(None),
        mode: Int | Literal["absolute", "relative", "pattern"] | Default = Default("absolute"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Field matching using hints.

        Parameters:
        ----------

        :param String hint: set hint file
        :param Int mode: set hint mode (from 0 to 2) (default absolute)

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
        order: Int | Literal["bff", "tff"] | Default = Default("tff"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Set the field order.

        Parameters:
        ----------

        :param Int order: output field order (from 0 to 1) (default tff)
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
        left: Int = Default(0),
        right: Int = Default(0),
        top: Int = Default(0),
        bottom: Int = Default(0),
        mode: Int
        | Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | Default = Default("smear"),
        color: Color = Default("black"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill borders of the input video.

        Parameters:
        ----------

        :param Int left: set the left fill border (from 0 to INT_MAX) (default 0)
        :param Int right: set the right fill border (from 0 to INT_MAX) (default 0)
        :param Int top: set the top fill border (from 0 to INT_MAX) (default 0)
        :param Int bottom: set the bottom fill border (from 0 to INT_MAX) (default 0)
        :param Int mode: set the fill borders mode (from 0 to 6) (default smear)
        :param Color color: set the color for the fixed/fade mode (default "black")
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
        object: String = Default(None),
        threshold: Float = Default(0.5),
        mipmaps: Int = Default(3),
        xmin: Int = Default(0),
        discard: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find a user specified object.

        Parameters:
        ----------

        :param String object: object bitmap filename
        :param Float threshold: set threshold (from 0 to 1) (default 0.5)
        :param Int mipmaps: set mipmaps (from 1 to 5) (default 3)
        :param Int xmin: (from 0 to INT_MAX) (default 0)
        :param Boolean discard: (default false)

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
        x: Int = Default(0),
        y: Int = Default(0),
        s0: Int = Default(0),
        s1: Int = Default(0),
        s2: Int = Default(0),
        s3: Int = Default(0),
        d0: Int = Default(0),
        d1: Int = Default(0),
        d2: Int = Default(0),
        d3: Int = Default(0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill area with same color with another color.

        Parameters:
        ----------

        :param Int x: set pixel x coordinate (from 0 to 65535) (default 0)
        :param Int y: set pixel y coordinate (from 0 to 65535) (default 0)
        :param Int s0: set source #0 component value (from -1 to 65535) (default 0)
        :param Int s1: set source #1 component value (from -1 to 65535) (default 0)
        :param Int s2: set source #2 component value (from -1 to 65535) (default 0)
        :param Int s3: set source #3 component value (from -1 to 65535) (default 0)
        :param Int d0: set destination #0 component value (from 0 to 65535) (default 0)
        :param Int d1: set destination #1 component value (from 0 to 65535) (default 0)
        :param Int d2: set destination #2 component value (from 0 to 65535) (default 0)
        :param Int d3: set destination #3 component value (from 0 to 65535) (default 0)
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

    def format(self, *, pix_fmts: String = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Convert the input video to one of the specified pixel formats.

        Parameters:
        ----------

        :param String pix_fmts: A '|'-separated list of pixel formats

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
        fps: String = Default("25"),
        start_time: Double = Default("DBL_MAX"),
        round: Int | Literal["zero", "inf", "down", "up", "near"] | Default = Default("near"),
        eof_action: Int | Literal["round", "pass"] | Default = Default("round"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force constant framerate.

        Parameters:
        ----------

        :param String fps: A string describing desired output framerate (default "25")
        :param Double start_time: Assume the first PTS should be this value. (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param Int round: set rounding method for timestamps (from 0 to 5) (default near)
        :param Int eof_action: action performed for last frame (from 0 to 1) (default round)

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
        format: Int | Literal["sbs", "tab", "frameseq", "lines", "columns"] | Default = Default("sbs"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate a frame packed stereoscopic video.

        Parameters:
        ----------

        :param Int format: Frame pack output format (from 0 to INT_MAX) (default sbs)

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
        fps: Video_rate = Default("50"),
        interp_start: Int = Default(15),
        interp_end: Int = Default(240),
        scene: Double = Default(8.2),
        flags: Flags | Literal["scene_change_detect", "scd"] | Default = Default("scene_change_detect+scd"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Upsamples or downsamples progressive source between specified frame rates.

        Parameters:
        ----------

        :param Video_rate fps: required output frames per second rate (default "50")
        :param Int interp_start: point to start linear interpolation (from 0 to 255) (default 15)
        :param Int interp_end: point to end linear interpolation (from 0 to 255) (default 240)
        :param Double scene: scene change level (from 0 to 100) (default 8.2)
        :param Flags flags: set flags (default scene_change_detect+scd)

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

    def framestep(self, *, step: Int = Default(1), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Select one frame every N frames.

        Parameters:
        ----------

        :param Int step: set frame step (from 1 to INT_MAX) (default 1)
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

    def freezedetect(self, *, n: Double = Default(0.001), d: Duration = Default(2.0), **kwargs: Any) -> "VideoStream":
        """

        Detects frozen video input.

        Parameters:
        ----------

        :param Double n: set noise tolerance (from 0 to 1) (default 0.001)
        :param Duration d: set minimum duration in seconds (default 2)

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
        first: Int64 = Default(0),
        last: Int64 = Default(0),
        replace: Int64 = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Freeze video frames.

        Parameters:
        ----------

        :param Int64 first: set first frame to freeze (from 0 to I64_MAX) (default 0)
        :param Int64 last: set last frame to freeze (from 0 to I64_MAX) (default 0)
        :param Int64 replace: set frame to replace (from 0 to I64_MAX) (default 0)

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
        filter_name: String = Default(None),
        filter_params: String = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a frei0r effect.

        Parameters:
        ----------

        :param String filter_name:
        :param String filter_params:
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
        quality: Int = Default(4),
        qp: Int = Default(0),
        strength: Int = Default(0),
        use_bframe_qp: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Fast Simple Post-processing filter.

        Parameters:
        ----------

        :param Int quality: set quality (from 4 to 5) (default 4)
        :param Int qp: force a constant quantizer parameter (from 0 to 64) (default 0)
        :param Int strength: set filter strength (from -15 to 32) (default 0)
        :param Boolean use_bframe_qp: use B-frames' QP (default false)
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
        sigma: Float = Default(0.5),
        steps: Int = Default(1),
        planes: Int = Default(15),
        sigmaV: Float = Default(-1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Gaussian Blur filter.

        Parameters:
        ----------

        :param Float sigma: set sigma (from 0 to 1024) (default 0.5)
        :param Int steps: set number of steps (from 1 to 6) (default 1)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float sigmaV: set vertical sigma (from -1 to 1024) (default -1)
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
        lum_expr: String = Default(None),
        cb_expr: String = Default(None),
        cr_expr: String = Default(None),
        alpha_expr: String = Default(None),
        red_expr: String = Default(None),
        green_expr: String = Default(None),
        blue_expr: String = Default(None),
        interpolation: Int | Literal["nearest", "n", "bilinear", "b"] | Default = Default("bilinear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply generic equation to each pixel.

        Parameters:
        ----------

        :param String lum_expr: set luminance expression
        :param String cb_expr: set chroma blue expression
        :param String cr_expr: set chroma red expression
        :param String alpha_expr: set alpha expression
        :param String red_expr: set red expression
        :param String green_expr: set green expression
        :param String blue_expr: set blue expression
        :param Int interpolation: set interpolation method (from 0 to 1) (default bilinear)
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
        self, *, strength: Float = Default(1.2), radius: Int = Default(16), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Debands video quickly using gradients.

        Parameters:
        ----------

        :param Float strength: The maximum amount by which the filter will change any one pixel. (from 0.51 to 64) (default 1.2)
        :param Int radius: The neighborhood to fit the gradient to. (from 4 to 32) (default 16)
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
        size: Image_size = Default("hd720"),
        opacity: Float = Default(0.9),
        mode: Int | Literal["full", "compact"] | Default = Default("full"),
        flags: Flags
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
        rate: Video_rate = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Show various filtergraph stats.

        Parameters:
        ----------

        :param Image_size size: set monitor size (default "hd720")
        :param Float opacity: set video opacity (from 0 to 1) (default 0.9)
        :param Int mode: set mode (from 0 to 1) (default full)
        :param Flags flags: set flags (default queue)
        :param Video_rate rate: set video rate (default "25")

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
        difford: Int = Default(1),
        minknorm: Int = Default(1),
        sigma: Double = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Estimates scene illumination by grey edge assumption.

        Parameters:
        ----------

        :param Int difford: set differentiation order (from 0 to 2) (default 1)
        :param Int minknorm: set Minkowski norm (from 0 to 20) (default 1)
        :param Double sigma: set sigma (from 0 to 1024) (default 1)
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
        clut: Int | Literal["first", "all"] | Default = Default("all"),
        interp: Int
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("tetrahedral"),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a Hald CLUT.

        Parameters:
        ----------

        :param Int clut: when to process CLUT (from 0 to 1) (default all)
        :param Int interp: select interpolation mode (from 0 to 4) (default tetrahedral)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        strength: Float = Default(0.2),
        intensity: Float = Default(0.21),
        antibanding: Int | Literal["none", "weak", "strong"] | Default = Default("none"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply global color histogram equalization.

        Parameters:
        ----------

        :param Float strength: set the strength (from 0 to 1) (default 0.2)
        :param Float intensity: set the intensity (from 0 to 1) (default 0.21)
        :param Int antibanding: set the antibanding level (from 0 to 2) (default none)
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
        level_height: Int = Default(200),
        scale_height: Int = Default(12),
        display_mode: Int | Literal["overlay", "parade", "stack"] | Default = Default("stack"),
        levels_mode: Int | Literal["linear", "logarithmic"] | Default = Default("linear"),
        components: Int = Default(7),
        fgopacity: Float = Default(0.7),
        bgopacity: Float = Default(0.5),
        colors_mode: Int
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

        :param Int level_height: set level height (from 50 to 2048) (default 200)
        :param Int scale_height: set scale height (from 0 to 40) (default 12)
        :param Int display_mode: set display mode (from 0 to 2) (default stack)
        :param Int levels_mode: set levels mode (from 0 to 1) (default linear)
        :param Int components: set color components to display (from 1 to 15) (default 7)
        :param Float fgopacity: set foreground opacity (from 0 to 1) (default 0.7)
        :param Float bgopacity: set background opacity (from 0 to 1) (default 0.5)
        :param Int colors_mode: set colors mode (from 0 to 9) (default whiteonblack)

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
        luma_spatial: Double = Default(0.0),
        chroma_spatial: Double = Default(0.0),
        luma_tmp: Double = Default(0.0),
        chroma_tmp: Double = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a High Quality 3D Denoiser.

        Parameters:
        ----------

        :param Double luma_spatial: spatial luma strength (from 0 to DBL_MAX) (default 0)
        :param Double chroma_spatial: spatial chroma strength (from 0 to DBL_MAX) (default 0)
        :param Double luma_tmp: temporal luma strength (from 0 to DBL_MAX) (default 0)
        :param Double chroma_tmp: temporal chroma strength (from 0 to DBL_MAX) (default 0)
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

    def hqx(self, *, n: Int = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

        Parameters:
        ----------

        :param Int n: set scale factor (from 2 to 4) (default 3)

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
        hue: Float = Default(0.0),
        sat: Float = Default(0.0),
        val: Float = Default(0.0),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into gray.

        Parameters:
        ----------

        :param Float hue: set the hue value (from -360 to 360) (default 0)
        :param Float sat: set the saturation value (from -1 to 1) (default 0)
        :param Float val: set the value value (from -1 to 1) (default 0)
        :param Float similarity: set the hsvhold similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the hsvhold blend value (from 0 to 1) (default 0)
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
        hue: Float = Default(0.0),
        sat: Float = Default(0.0),
        val: Float = Default(0.0),
        similarity: Float = Default(0.01),
        blend: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param Float hue: set the hue value (from -360 to 360) (default 0)
        :param Float sat: set the saturation value (from -1 to 1) (default 0)
        :param Float val: set the value value (from -1 to 1) (default 0)
        :param Float similarity: set the hsvkey similarity value (from 1e-05 to 1) (default 0.01)
        :param Float blend: set the hsvkey blend value (from 0 to 1) (default 0)
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
        h: String = Default(None),
        s: String = Default("1"),
        H: String = Default(None),
        b: String = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the hue and saturation of the input video.

        Parameters:
        ----------

        :param String h: set the hue angle degrees expression
        :param String s: set the saturation expression (default "1")
        :param String H: set the hue angle radians expression
        :param String b: set the brightness expression (default "0")
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
        hue: Float = Default(0.0),
        saturation: Float = Default(0.0),
        intensity: Float = Default(0.0),
        colors: Flags | Literal["r", "y", "g", "c", "b", "m", "a"] | Default = Default("r+y+g+c+b+m+a"),
        strength: Float = Default(1.0),
        rw: Float = Default(0.333),
        gw: Float = Default(0.334),
        bw: Float = Default(0.333),
        lightness: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply hue-saturation-intensity adjustments.

        Parameters:
        ----------

        :param Float hue: set the hue shift (from -180 to 180) (default 0)
        :param Float saturation: set the saturation shift (from -1 to 1) (default 0)
        :param Float intensity: set the intensity shift (from -1 to 1) (default 0)
        :param Flags colors: set colors range (default r+y+g+c+b+m+a)
        :param Float strength: set the filtering strength (from 0 to 100) (default 1)
        :param Float rw: set the red weight (from 0 to 1) (default 0.333)
        :param Float gw: set the green weight (from 0 to 1) (default 0.334)
        :param Float bw: set the blue weight (from 0 to 1) (default 0.333)
        :param Boolean lightness: set the preserve lightness (default false)
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
        mode: Flags | Literal["read", "write", "overwrite", "direct"] | Default = Default("read+write"),
        derive_device: String = Default(None),
        reverse: Int = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Map hardware frames

        Parameters:
        ----------

        :param Flags mode: Frame mapping mode (default read+write)
        :param String derive_device: Derive a new device of this type
        :param Int reverse: Map in reverse (create and allocate in the sink) (from 0 to 1) (default 0)

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

    def hwupload(self, *, derive_device: String = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Upload a normal frame to a hardware frame

        Parameters:
        ----------

        :param String derive_device: Derive a new device of this type

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
        planes: Int = Default(15),
        threshold: Int = Default(0),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Grow first stream into second stream by connecting components.

        Parameters:
        ----------

        :param Int planes: set planes (from 0 to 15) (default 15)
        :param Int threshold: set threshold (from 0 to 65535) (default 0)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the Identity between two video streams.

        Parameters:
        ----------

        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        intl_thres: Float = Default(1.04),
        prog_thres: Float = Default(1.5),
        rep_thres: Float = Default(3.0),
        half_life: Float = Default(0.0),
        analyze_interlaced_flag: Int = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Interlace detect Filter.

        Parameters:
        ----------

        :param Float intl_thres: set interlacing threshold (from -1 to FLT_MAX) (default 1.04)
        :param Float prog_thres: set progressive threshold (from -1 to FLT_MAX) (default 1.5)
        :param Float rep_thres: set repeat threshold (from -1 to FLT_MAX) (default 3)
        :param Float half_life: half life of cumulative statistics (from -1 to INT_MAX) (default 0)
        :param Int analyze_interlaced_flag: set number of frames to use to determine if the interlace flag is accurate (from 0 to INT_MAX) (default 0)

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
        luma_mode: Int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        chroma_mode: Int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        alpha_mode: Int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("none"),
        luma_swap: Boolean = Default(False),
        chroma_swap: Boolean = Default(False),
        alpha_swap: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterleave or interleave fields.

        Parameters:
        ----------

        :param Int luma_mode: select luma mode (from 0 to 2) (default none)
        :param Int chroma_mode: select chroma mode (from 0 to 2) (default none)
        :param Int alpha_mode: select alpha mode (from 0 to 2) (default none)
        :param Boolean luma_swap: swap luma fields (default false)
        :param Boolean chroma_swap: swap chroma fields (default false)
        :param Boolean alpha_swap: swap alpha fields (default false)
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
        threshold0: Int = Default(65535),
        threshold1: Int = Default(65535),
        threshold2: Int = Default(65535),
        threshold3: Int = Default(65535),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply inflate effect.

        Parameters:
        ----------

        :param Int threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
        :param Int threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
        :param Int threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
        :param Int threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
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
        scan: Int | Literal["tff", "bff"] | Default = Default("tff"),
        lowpass: Int | Literal["off", "linear", "complex"] | Default = Default("linear"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert progressive video into interlaced.

        Parameters:
        ----------

        :param Int scan: scanning mode (from 0 to 1) (default tff)
        :param Int lowpass: set vertical low-pass filter (from 0 to 2) (default linear)

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
        thresh: Int = Default(10),
        map: Boolean = Default(False),
        order: Boolean = Default(False),
        sharp: Boolean = Default(False),
        twoway: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kernel deinterlacing to the input.

        Parameters:
        ----------

        :param Int thresh: set the threshold (from 0 to 255) (default 10)
        :param Boolean map: set the map (default false)
        :param Boolean order: set the order (default false)
        :param Boolean sharp: set sharpening (default false)
        :param Boolean twoway: set twoway (default false)

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
        planes: Int = Default(15),
        scale: Float = Default(1.0),
        delta: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kirsch operator.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float scale: set scale (from 0 to 65535) (default 1)
        :param Float delta: set delta (from -65535 to 65535) (default 0)
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
        self, *, decay: Float = Default(0.95), planes: Flags = Default("F"), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Slowly update darker pixels.

        Parameters:
        ----------

        :param Float decay: set decay (from 0 to 1) (default 0.95)
        :param Flags planes: set what planes to filter (default F)
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
        cx: Double = Default(0.5),
        cy: Double = Default(0.5),
        k1: Double = Default(0.0),
        k2: Double = Default(0.0),
        i: Int | Literal["nearest", "bilinear"] | Default = Default("nearest"),
        fc: Color = Default("black@0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rectify the image by correcting for lens distortion.

        Parameters:
        ----------

        :param Double cx: set relative center x (from 0 to 1) (default 0.5)
        :param Double cy: set relative center y (from 0 to 1) (default 0.5)
        :param Double k1: set quadratic distortion factor (from -1 to 1) (default 0)
        :param Double k2: set double quadratic distortion factor (from -1 to 1) (default 0)
        :param Int i: set interpolation type (from 0 to 64) (default nearest)
        :param Color fc: set the color of the unmapped pixels (default "black@0")
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
        model_path: String = Default(None),
        log_path: String = Default(None),
        log_fmt: String = Default("xml"),
        enable_transform: Boolean = Default(False),
        psnr: Boolean = Default(False),
        ssim: Boolean = Default(False),
        ms_ssim: Boolean = Default(False),
        pool: String = Default(None),
        n_threads: Int = Default(0),
        n_subsample: Int = Default(1),
        enable_conf_interval: Boolean = Default(False),
        model: String = Default("version=vmaf_v0.6.1"),
        feature: String = Default(None),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the VMAF between two video streams.

        Parameters:
        ----------

        :param String model_path: use model='path=...'.
        :param String log_path: Set the file path to be used to write log.
        :param String log_fmt: Set the format of the log (csv, json, xml, or sub). (default "xml")
        :param Boolean enable_transform: use model='enable_transform=true'. (default false)
        :param Boolean psnr: use feature='name=psnr'. (default false)
        :param Boolean ssim: use feature='name=float_ssim'. (default false)
        :param Boolean ms_ssim: use feature='name=float_ms_ssim'. (default false)
        :param String pool: Set the pool method to be used for computing vmaf.
        :param Int n_threads: Set number of threads to be used when computing vmaf. (from 0 to UINT32_MAX) (default 0)
        :param Int n_subsample: Set interval for frame subsampling used when computing vmaf. (from 1 to UINT32_MAX) (default 1)
        :param Boolean enable_conf_interval: model='enable_conf_interval=true'. (default false)
        :param String model: Set the model to be used for computing vmaf. (default "version=vmaf_v0.6.1")
        :param String feature: Set the feature to be used for computing vmaf.
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)

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
        min: Int = Default(0),
        max: Int = Default(65535),
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Limit pixels components to the specified range.

        Parameters:
        ----------

        :param Int min: set min value (from 0 to 65535) (default 0)
        :param Int max: set max value (from 0 to 65535) (default 65535)
        :param Int planes: set planes (from 0 to 15) (default 15)
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
        self, *, loop: Int = Default(0), size: Int64 = Default(0), start: Int64 = Default(0), **kwargs: Any
    ) -> "VideoStream":
        """

        Loop video frames.

        Parameters:
        ----------

        :param Int loop: number of loops (from -1 to INT_MAX) (default 0)
        :param Int64 size: max number of frames to loop (from 0 to 32767) (default 0)
        :param Int64 start: set the loop start frame (from 0 to I64_MAX) (default 0)

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
        threshold: Double = Default(0.0),
        tolerance: Double = Default(0.01),
        softness: Double = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain luma into transparency.

        Parameters:
        ----------

        :param Double threshold: set the threshold value (from 0 to 1) (default 0)
        :param Double tolerance: set the tolerance value (from 0 to 1) (default 0.01)
        :param Double softness: set the softness value (from 0 to 1) (default 0)
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
        c0: String = Default("clipval"),
        c1: String = Default("clipval"),
        c2: String = Default("clipval"),
        c3: String = Default("clipval"),
        y: String = Default("clipval"),
        u: String = Default("clipval"),
        v: String = Default("clipval"),
        r: String = Default("clipval"),
        g: String = Default("clipval"),
        b: String = Default("clipval"),
        a: String = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB/YUV input video.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "clipval")
        :param String c1: set component #1 expression (default "clipval")
        :param String c2: set component #2 expression (default "clipval")
        :param String c3: set component #3 expression (default "clipval")
        :param String y: set Y expression (default "clipval")
        :param String u: set U expression (default "clipval")
        :param String v: set V expression (default "clipval")
        :param String r: set R expression (default "clipval")
        :param String g: set G expression (default "clipval")
        :param String b: set B expression (default "clipval")
        :param String a: set A expression (default "clipval")
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
        file: String = Default(None),
        interp: Int | Literal["nearest", "linear", "cosine", "cubic", "spline"] | Default = Default("linear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 1D LUT.

        Parameters:
        ----------

        :param String file: set 1D LUT file name
        :param Int interp: select interpolation mode (from 0 to 4) (default linear)
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
        c0: String = Default("x"),
        c1: String = Default("x"),
        c2: String = Default("x"),
        c3: String = Default("x"),
        d: Int = Default(0),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table from two video inputs.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "x")
        :param String c1: set component #1 expression (default "x")
        :param String c2: set component #2 expression (default "x")
        :param String c3: set component #3 expression (default "x")
        :param Int d: set output depth (from 0 to 16) (default 0)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        file: String = Default(None),
        clut: Int | Literal["first", "all"] | Default = Default("all"),
        interp: Int
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("tetrahedral"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 3D LUT.

        Parameters:
        ----------

        :param String file: set 3D LUT file name
        :param Int clut: when to process CLUT (from 0 to 1) (default all)
        :param Int interp: select interpolation mode (from 0 to 4) (default tetrahedral)
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
        c0: String = Default("clipval"),
        c1: String = Default("clipval"),
        c2: String = Default("clipval"),
        c3: String = Default("clipval"),
        y: String = Default("clipval"),
        u: String = Default("clipval"),
        v: String = Default("clipval"),
        r: String = Default("clipval"),
        g: String = Default("clipval"),
        b: String = Default("clipval"),
        a: String = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB input video.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "clipval")
        :param String c1: set component #1 expression (default "clipval")
        :param String c2: set component #2 expression (default "clipval")
        :param String c3: set component #3 expression (default "clipval")
        :param String y: set Y expression (default "clipval")
        :param String u: set U expression (default "clipval")
        :param String v: set V expression (default "clipval")
        :param String r: set R expression (default "clipval")
        :param String g: set G expression (default "clipval")
        :param String b: set B expression (default "clipval")
        :param String a: set A expression (default "clipval")
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
        c0: String = Default("clipval"),
        c1: String = Default("clipval"),
        c2: String = Default("clipval"),
        c3: String = Default("clipval"),
        y: String = Default("clipval"),
        u: String = Default("clipval"),
        v: String = Default("clipval"),
        r: String = Default("clipval"),
        g: String = Default("clipval"),
        b: String = Default("clipval"),
        a: String = Default("clipval"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the YUV input video.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "clipval")
        :param String c1: set component #1 expression (default "clipval")
        :param String c2: set component #2 expression (default "clipval")
        :param String c3: set component #3 expression (default "clipval")
        :param String y: set Y expression (default "clipval")
        :param String u: set U expression (default "clipval")
        :param String v: set V expression (default "clipval")
        :param String r: set R expression (default "clipval")
        :param String g: set G expression (default "clipval")
        :param String b: set B expression (default "clipval")
        :param String a: set A expression (default "clipval")
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
        undershoot: Int = Default(0),
        overshoot: Int = Default(0),
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Clamp first stream with second stream and third stream.

        Parameters:
        ----------

        :param Int undershoot: set undershoot (from 0 to 65535) (default 0)
        :param Int overshoot: set overshoot (from 0 to 65535) (default 0)
        :param Int planes: set planes (from 0 to 15) (default 15)
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
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply filtering with maximum difference of two streams.

        Parameters:
        ----------

        :param Int planes: set planes (from 0 to 15) (default 15)
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
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Merge first stream with second stream using third stream as mask.

        Parameters:
        ----------

        :param Int planes: set planes (from 0 to 15) (default 15)
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
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply filtering with minimum difference of two streams.

        Parameters:
        ----------

        :param Int planes: set planes (from 0 to 15) (default 15)
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
        threshold: Int = Default(1),
        planes: Int = Default(15),
        mode: Int | Literal["abs", "diff"] | Default = Default("abs"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick pixels comparing absolute difference of two streams with threshold.

        Parameters:
        ----------

        :param Int threshold: set threshold (from 0 to 65535) (default 1)
        :param Int planes: set planes (from 0 to 15) (default 15)
        :param Int mode: set mode (from 0 to 1) (default abs)
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
        low: Int = Default(10),
        high: Int = Default(10),
        planes: Int = Default(15),
        fill: Int = Default(0),
        sum: Int = Default(10),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Create Mask.

        Parameters:
        ----------

        :param Int low: set low threshold (from 0 to 65535) (default 10)
        :param Int high: set high threshold (from 0 to 65535) (default 10)
        :param Int planes: set planes (from 0 to 15) (default 15)
        :param Int fill: set fill value (from 0 to 65535) (default 0)
        :param Int sum: set sum value (from 0 to 65535) (default 10)
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
        radius: Int = Default(1),
        planes: Int = Default(15),
        radiusV: Int = Default(0),
        percentile: Float = Default(0.5),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Median filter.

        Parameters:
        ----------

        :param Int radius: set median radius (from 1 to 127) (default 1)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Int radiusV: set median vertical radius (from 0 to 127) (default 0)
        :param Float percentile: set median percentile (from 0 to 1) (default 0.5)
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
        method: Int
        | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | Default = Default("esa"),
        mb_size: Int = Default(16),
        search_param: Int = Default(7),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate motion vectors.

        Parameters:
        ----------

        :param Int method: motion estimation method (from 1 to 9) (default esa)
        :param Int mb_size: macroblock size (from 8 to INT_MAX) (default 16)
        :param Int search_param: search parameter (from 4 to INT_MAX) (default 7)

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
        mode: Int | Literal["select", "add", "modify", "delete", "print"] | Default = Default("select"),
        key: String = Default(None),
        value: String = Default(None),
        function: Int
        | Literal["same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"]
        | Default = Default("same_str"),
        expr: String = Default(None),
        file: String = Default(None),
        direct: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Manipulate video frame metadata.

        Parameters:
        ----------

        :param Int mode: set a mode of operation (from 0 to 4) (default select)
        :param String key: set metadata key
        :param String value: set metadata value
        :param Int function: function for comparing values (from 0 to 6) (default same_str)
        :param String expr: set expression for expr function
        :param String file: set file where to print metadata information
        :param Boolean direct: reduce buffering when printing to user-set file or pipe (default false)
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
        self, _in1: "VideoStream", *, planes: Int = Default(15), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Apply Midway Equalization.

        Parameters:
        ----------

        :param Int planes: set planes (from 0 to 15) (default 15)
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
        fps: Video_rate = Default("60"),
        mi_mode: Int | Literal["dup", "blend", "mci"] | Default = Default("mci"),
        mc_mode: Int | Literal["obmc", "aobmc"] | Default = Default("obmc"),
        me_mode: Int | Literal["bidir", "bilat"] | Default = Default("bilat"),
        me: Int
        | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | Default = Default("epzs"),
        mb_size: Int = Default(16),
        search_param: Int = Default(32),
        vsbmc: Int = Default(0),
        scd: Int | Literal["none", "fdiff"] | Default = Default("fdiff"),
        scd_threshold: Double = Default(10.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Frame rate conversion using Motion Interpolation.

        Parameters:
        ----------

        :param Video_rate fps: output's frame rate (default "60")
        :param Int mi_mode: motion interpolation mode (from 0 to 2) (default mci)
        :param Int mc_mode: motion compensation mode (from 0 to 1) (default obmc)
        :param Int me_mode: motion estimation mode (from 0 to 1) (default bilat)
        :param Int me: motion estimation method (from 1 to 9) (default epzs)
        :param Int mb_size: macroblock size (from 4 to 16) (default 16)
        :param Int search_param: search parameter (from 4 to INT_MAX) (default 32)
        :param Int vsbmc: variable-size block motion compensation (from 0 to 1) (default 0)
        :param Int scd: scene change detection method (from 0 to 1) (default fdiff)
        :param Double scd_threshold: scene change threshold (from 0 to 100) (default 10)

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
        cb: Float = Default(0.0),
        cr: Float = Default(0.0),
        size: Float = Default(1.0),
        high: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert video to gray using custom color filter.

        Parameters:
        ----------

        :param Float cb: set the chroma blue spot (from -1 to 1) (default 0)
        :param Float cr: set the chroma red spot (from -1 to 1) (default 0)
        :param Float size: set the color filter size (from 0.1 to 10) (default 1)
        :param Float high: set the highlights strength (from 0 to 1) (default 0)
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
        mode: Int
        | Literal["erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"]
        | Default = Default("erode"),
        planes: Int = Default(7),
        structure: Int | Literal["first", "all"] | Default = Default("all"),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Morphological filter.

        Parameters:
        ----------

        :param Int mode: set morphological transform (from 0 to 6) (default erode)
        :param Int planes: set planes to filter (from 0 to 15) (default 7)
        :param Int structure: when to process structures (from 0 to 1) (default all)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        max: Int = Default(0),
        hi: Int = Default(768),
        lo: Int = Default(320),
        frac: Float = Default(0.33),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove near-duplicate frames.

        Parameters:
        ----------

        :param Int max: set the maximum number of consecutive dropped frames (positive), or the minimum interval between dropped frames (negative) (from INT_MIN to INT_MAX) (default 0)
        :param Int hi: set high dropping threshold (from INT_MIN to INT_MAX) (default 768)
        :param Int lo: set low dropping threshold (from INT_MIN to INT_MAX) (default 320)
        :param Float frac: set fraction dropping threshold (from 0 to 1) (default 0.33)

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
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the MSAD between two video streams.

        Parameters:
        ----------

        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        scale: Float = Default(1.0),
        offset: Float = Default(0.5),
        planes: Flags = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Multiply first video stream with second video stream.

        Parameters:
        ----------

        :param Float scale: set scale (from 0 to 9) (default 1)
        :param Float offset: set offset (from -1 to 1) (default 0.5)
        :param Flags planes: set planes (default F)
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
        components: Flags | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default("y+u+v+r+g+b"),
        negate_alpha: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Negate input video.

        Parameters:
        ----------

        :param Flags components: set components to negate (default y+u+v+r+g+b)
        :param Boolean negate_alpha: (default false)
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
        s: Double = Default(1.0),
        p: Int = Default(7),
        pc: Int = Default(0),
        r: Int = Default(15),
        rc: Int = Default(0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Non-local means denoiser.

        Parameters:
        ----------

        :param Double s: denoising strength (from 1 to 30) (default 1)
        :param Int p: patch size (from 0 to 99) (default 7)
        :param Int pc: patch size for chroma planes (from 0 to 99) (default 0)
        :param Int r: research window (from 0 to 99) (default 15)
        :param Int rc: research window for chroma planes (from 0 to 99) (default 0)
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
        weights: String = Default("nnedi3_weights.bin"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        field: Int | Literal["af", "a", "t", "b", "tf", "bf"] | Default = Default("a"),
        planes: Int = Default(7),
        nsize: Int | Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"] | Default = Default("s32x4"),
        nns: Int | Literal["n16", "n32", "n64", "n128", "n256"] | Default = Default("n32"),
        qual: Int | Literal["fast", "slow"] | Default = Default("fast"),
        etype: Int | Literal["a", "abs", "s", "mse"] | Default = Default("a"),
        pscrn: Int | Literal["none", "original", "new", "new2", "new3"] | Default = Default("new"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply neural network edge directed interpolation intra-only deinterlacer.

        Parameters:
        ----------

        :param String weights: set weights file (default "nnedi3_weights.bin")
        :param Int deint: set which frames to deinterlace (from 0 to 1) (default all)
        :param Int field: set mode of operation (from -2 to 3) (default a)
        :param Int planes: set which planes to process (from 0 to 15) (default 7)
        :param Int nsize: set size of local neighborhood around each pixel, used by the predictor neural network (from 0 to 6) (default s32x4)
        :param Int nns: set number of neurons in predictor neural network (from 0 to 4) (default n32)
        :param Int qual: set quality (from 1 to 2) (default fast)
        :param Int etype: set which set of weights to use in the predictor (from 0 to 1) (default a)
        :param Int pscrn: set prescreening (from 0 to 4) (default new)
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

    def noformat(self, *, pix_fmts: String = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

        Parameters:
        ----------

        :param String pix_fmts: A '|'-separated list of pixel formats

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
        all_seed: Int = Default(-1),
        all_strength: Int = Default(0),
        all_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c0_seed: Int = Default(-1),
        c0_strength: Int = Default(0),
        c0_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c1_seed: Int = Default(-1),
        c1_strength: Int = Default(0),
        c1_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c2_seed: Int = Default(-1),
        c2_strength: Int = Default(0),
        c2_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c3_seed: Int = Default(-1),
        c3_strength: Int = Default(0),
        c3_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add noise.

        Parameters:
        ----------

        :param Int all_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
        :param Int all_strength: set component #0 strength (from 0 to 100) (default 0)
        :param Flags all_flags: set component #0 flags (default 0)
        :param Int c0_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
        :param Int c0_strength: set component #0 strength (from 0 to 100) (default 0)
        :param Flags c0_flags: set component #0 flags (default 0)
        :param Int c1_seed: set component #1 noise seed (from -1 to INT_MAX) (default -1)
        :param Int c1_strength: set component #1 strength (from 0 to 100) (default 0)
        :param Flags c1_flags: set component #1 flags (default 0)
        :param Int c2_seed: set component #2 noise seed (from -1 to INT_MAX) (default -1)
        :param Int c2_strength: set component #2 strength (from 0 to 100) (default 0)
        :param Flags c2_flags: set component #2 flags (default 0)
        :param Int c3_seed: set component #3 noise seed (from -1 to INT_MAX) (default -1)
        :param Int c3_strength: set component #3 strength (from 0 to 100) (default 0)
        :param Flags c3_flags: set component #3 flags (default 0)
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
        blackpt: Color = Default("black"),
        whitept: Color = Default("white"),
        smoothing: Int = Default(0),
        independence: Float = Default(1.0),
        strength: Float = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Normalize RGB video.

        Parameters:
        ----------

        :param Color blackpt: output color to which darkest input color is mapped (default "black")
        :param Color whitept: output color to which brightest input color is mapped (default "white")
        :param Int smoothing: amount of temporal smoothing of the input range, to reduce flicker (from 0 to 2.68435e+08) (default 0)
        :param Float independence: proportion of independent to linked channel normalization (from 0 to 1) (default 1)
        :param Float strength: strength of filter, from no effect to full normalization (from 0 to 1) (default 1)
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
        datapath: String = Default(None),
        language: String = Default("eng"),
        whitelist: String = Default("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?\"'[]{}("),
        blacklist: String = Default(""),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Optical Character Recognition.

        Parameters:
        ----------

        :param String datapath: set datapath
        :param String language: set language (default "eng")
        :param String whitelist: set character whitelist (default "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?"'[]{}()|/\=*&%$#@!~ ")
        :param String blacklist: set character blacklist (default "")

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
        x: Float = Default(0.5),
        y: Float = Default(0.5),
        s: Float = Default(0.8),
        t: Float = Default(0.5),
        o: Float = Default(0.8),
        tx: Float = Default(0.5),
        ty: Float = Default(0.9),
        tw: Float = Default(0.8),
        th: Float = Default(0.3),
        c: Int = Default(7),
        g: Boolean = Default(True),
        st: Boolean = Default(True),
        sc: Boolean = Default(True),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        2D Video Oscilloscope.

        Parameters:
        ----------

        :param Float x: set scope x position (from 0 to 1) (default 0.5)
        :param Float y: set scope y position (from 0 to 1) (default 0.5)
        :param Float s: set scope size (from 0 to 1) (default 0.8)
        :param Float t: set scope tilt (from 0 to 1) (default 0.5)
        :param Float o: set trace opacity (from 0 to 1) (default 0.8)
        :param Float tx: set trace x position (from 0 to 1) (default 0.5)
        :param Float ty: set trace y position (from 0 to 1) (default 0.9)
        :param Float tw: set trace width (from 0.1 to 1) (default 0.8)
        :param Float th: set trace height (from 0.1 to 1) (default 0.3)
        :param Int c: set components to trace (from 0 to 15) (default 7)
        :param Boolean g: draw trace grid (default true)
        :param Boolean st: draw statistics (default true)
        :param Boolean sc: draw scope (default true)
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
        x: String = Default("0"),
        y: String = Default("0"),
        eof_action: Int | Literal["repeat", "endall", "pass", "repeat", "endall", "pass"] | Default = Default("repeat"),
        eval: Int | Literal["init", "frame"] | Default = Default("frame"),
        shortest: Boolean = Default(False),
        format: Int
        | Literal["yuv420", "yuv420p10", "yuv422", "yuv422p10", "yuv444", "rgb", "gbrp", "auto"]
        | Default = Default("yuv420"),
        repeatlast: Boolean = Default(True),
        alpha: Int | Literal["straight", "premultiplied"] | Default = Default("straight"),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Overlay a video source on top of the input.

        Parameters:
        ----------

        :param String x: set the x expression (default "0")
        :param String y: set the y expression (default "0")
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default frame)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Int format: set output format (from 0 to 7) (default yuv420)
        :param Boolean repeatlast: repeat overlay of the last overlay frame (default true)
        :param Int alpha: alpha format (from 0 to 1) (default straight)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        depth: Int = Default(8),
        luma_strength: Double = Default(1.0),
        chroma_strength: Double = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise using wavelets.

        Parameters:
        ----------

        :param Int depth: set depth (from 8 to 16) (default 8)
        :param Double luma_strength: set luma strength (from 0 to 1000) (default 1)
        :param Double chroma_strength: set chroma strength (from 0 to 1000) (default 1)
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
        width: String = Default("iw"),
        height: String = Default("ih"),
        x: String = Default("0"),
        y: String = Default("0"),
        color: Color = Default("black"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        aspect: Rational = Default("0/1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pad the input video.

        Parameters:
        ----------

        :param String width: set the pad area width expression (default "iw")
        :param String height: set the pad area height expression (default "ih")
        :param String x: set the x offset expression for the input image position (default "0")
        :param String y: set the y offset expression for the input image position (default "0")
        :param Color color: set the color of the padded area border (default "black")
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param Rational aspect: pad to fit an aspect instead of a resolution (from 0 to DBL_MAX) (default 0/1)

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
        max_colors: Int = Default(256),
        reserve_transparent: Boolean = Default(True),
        transparency_color: Color = Default("lime"),
        stats_mode: Int | Literal["full", "diff", "single"] | Default = Default("full"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find the optimal palette for a given stream.

        Parameters:
        ----------

        :param Int max_colors: set the maximum number of colors to use in the palette (from 2 to 256) (default 256)
        :param Boolean reserve_transparent: reserve a palette entry for transparency (default true)
        :param Color transparency_color: set a background color for transparency (default "lime")
        :param Int stats_mode: set statistics mode (from 0 to 2) (default full)

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
        dither: Int
        | Literal["bayer", "heckbert", "floyd_steinberg", "sierra2", "sierra2_4a", "sierra3", "burkes", "atkinson"]
        | Default = Default("sierra2_4a"),
        bayer_scale: Int = Default(2),
        diff_mode: Int | Literal["rectangle"] | Default = Default(0),
        new: Boolean = Default(False),
        alpha_threshold: Int = Default(128),
        debug_kdtree: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Use a palette to downsample an input video stream.

        Parameters:
        ----------

        :param Int dither: select dithering mode (from 0 to 8) (default sierra2_4a)
        :param Int bayer_scale: set scale for bayer dithering (from 0 to 5) (default 2)
        :param Int diff_mode: set frame difference mode (from 0 to 1) (default 0)
        :param Boolean new: take new palette for each output frame (default false)
        :param Int alpha_threshold: set the alpha threshold for transparency (from 0 to 255) (default 128)
        :param String debug_kdtree: save Graphviz graph of the kdtree in specified file

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
        mode: Int | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default("none"),
        seed: Int64 = Default(-1),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Set permissions for the output video frame.

        Parameters:
        ----------

        :param Int mode: select permissions mode (from 0 to 4) (default none)
        :param Int64 seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
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
        x0: String = Default("0"),
        y0: String = Default("0"),
        x1: String = Default("W"),
        y1: String = Default("0"),
        x2: String = Default("0"),
        y2: String = Default("H"),
        x3: String = Default("W"),
        y3: String = Default("H"),
        interpolation: Int | Literal["linear", "cubic"] | Default = Default("linear"),
        sense: Int | Literal["source", "destination"] | Default = Default("source"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Correct the perspective of video.

        Parameters:
        ----------

        :param String x0: set top left x coordinate (default "0")
        :param String y0: set top left y coordinate (default "0")
        :param String x1: set top right x coordinate (default "W")
        :param String y1: set top right y coordinate (default "0")
        :param String x2: set bottom left x coordinate (default "0")
        :param String y2: set bottom left y coordinate (default "H")
        :param String x3: set bottom right x coordinate (default "W")
        :param String y3: set bottom right y coordinate (default "H")
        :param Int interpolation: set interpolation (from 0 to 1) (default linear)
        :param Int sense: specify the sense of the coordinates (from 0 to 1) (default source)
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)
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
        mode: Int | Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"] | Default = Default("A"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Phase shift fields.

        Parameters:
        ----------

        :param Int mode: set phase mode (from 0 to 8) (default A)
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
        frames: Int = Default(30),
        threshold: Float = Default(1.0),
        skip: Int = Default(1),
        bypass: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Filter out photosensitive epilepsy seizure-inducing flashes.

        Parameters:
        ----------

        :param Int frames: set how many frames to use (from 2 to 240) (default 30)
        :param Float threshold: set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX) (default 1)
        :param Int skip: set pixels to skip when sampling frames (from 1 to 1024) (default 1)
        :param Boolean bypass: leave frames unchanged (default false)

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
        width: Int = Default(16),
        height: Int = Default(16),
        mode: Int | Literal["avg", "min", "max"] | Default = Default("avg"),
        planes: Flags = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixelize video.

        Parameters:
        ----------

        :param Int width: set block width (from 1 to 1024) (default 16)
        :param Int height: set block height (from 1 to 1024) (default 16)
        :param Int mode: set the pixelize mode (from 0 to 2) (default avg)
        :param Flags planes: set what planes to filter (default F)
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
        x: Float = Default(0.5),
        y: Float = Default(0.5),
        w: Int = Default(7),
        h: Int = Default(7),
        o: Float = Default(0.5),
        wx: Float = Default(-1.0),
        wy: Float = Default(-1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixel data analysis.

        Parameters:
        ----------

        :param Float x: set scope x offset (from 0 to 1) (default 0.5)
        :param Float y: set scope y offset (from 0 to 1) (default 0.5)
        :param Int w: set scope width (from 1 to 80) (default 7)
        :param Int h: set scope height (from 1 to 80) (default 7)
        :param Float o: set window opacity (from 0 to 1) (default 0.5)
        :param Float wx: set window x offset (from -1 to 1) (default -1)
        :param Float wy: set window y offset (from -1 to 1) (default -1)
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

    def pp(self, *, subfilters: String = Default("de"), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Filter video using libpostproc.

        Parameters:
        ----------

        :param String subfilters: set postprocess subfilters (default "de")
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
        qp: Int = Default(0),
        mode: Int | Literal["hard", "soft", "medium"] | Default = Default("medium"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Postprocessing 7 filter.

        Parameters:
        ----------

        :param Int qp: force a constant quantizer parameter (from 0 to 64) (default 0)
        :param Int mode: set thresholding mode (from 0 to 2) (default medium)
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
        planes: Int = Default(15),
        scale: Float = Default(1.0),
        delta: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply prewitt operator.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float scale: set scale (from 0 to 65535) (default 1)
        :param Float delta: set delta (from -65535 to 65535) (default 0)
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
        c0: String = Default("val"),
        c1: String = Default("val"),
        c2: String = Default("val"),
        c3: String = Default("val"),
        index: Int = Default(0),
        preset: Int
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
        opacity: Float = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make pseudocolored video frames.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "val")
        :param String c1: set component #1 expression (default "val")
        :param String c2: set component #2 expression (default "val")
        :param String c3: set component #3 expression (default "val")
        :param Int index: set component as base (from 0 to 3) (default 0)
        :param Int preset: set preset (from -1 to 14) (default none)
        :param Float opacity: set pseudocolor opacity (from 0 to 1) (default 1)
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
        stats_file: String = Default(None),
        stats_version: Int = Default(1),
        output_max: Boolean = Default(False),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the PSNR between two video streams.

        Parameters:
        ----------

        :param String stats_file: Set file where to store per-frame difference information
        :param Int stats_version: Set the format version for the stats file. (from 1 to 2) (default 1)
        :param Boolean output_max: Add raw stats (max values) to the output log. (default false)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        jl: Int = Default(1),
        jr: Int = Default(1),
        jt: Int = Default(4),
        jb: Int = Default(4),
        sb: Boolean = Default(False),
        mp: Int | Literal["y", "u", "v"] | Default = Default("y"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pullup from field sequence to frames.

        Parameters:
        ----------

        :param Int jl: set left junk size (from 0 to INT_MAX) (default 1)
        :param Int jr: set right junk size (from 0 to INT_MAX) (default 1)
        :param Int jt: set top junk size (from 1 to INT_MAX) (default 4)
        :param Int jb: set bottom junk size (from 1 to INT_MAX) (default 4)
        :param Boolean sb: set strict breaks (default false)
        :param Int mp: set metric plane (from 0 to 2) (default y)

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

    def qp(self, *, qp: String = Default(None), enable: str = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Change video quantization parameters.

        Parameters:
        ----------

        :param String qp: set qp expression
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

    def random(self, *, frames: Int = Default(30), seed: Int64 = Default(-1), **kwargs: Any) -> "VideoStream":
        """

        Return random frames.

        Parameters:
        ----------

        :param Int frames: set number of frames in cache (from 2 to 512) (default 30)
        :param Int64 seed: set the seed (from -1 to UINT32_MAX) (default -1)

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
        scan_min: Int = Default(0),
        scan_max: Int = Default(29),
        spw: Float = Default(0.27),
        chp: Boolean = Default(False),
        lp: Boolean = Default(True),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

        Parameters:
        ----------

        :param Int scan_min: set from which line to scan for codes (from 0 to INT_MAX) (default 0)
        :param Int scan_max: set to which line to scan for codes (from 0 to INT_MAX) (default 29)
        :param Float spw: set ratio of width reserved for sync code detection (from 0.1 to 0.7) (default 0.27)
        :param Boolean chp: check and apply parity bit (default false)
        :param Boolean lp: lowpass line prior to processing (default true)
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
        self, *, scan_max: Int = Default(45), thr_b: Double = Default(0.2), thr_w: Double = Default(0.6), **kwargs: Any
    ) -> "VideoStream":
        """

        Read vertical interval timecode and write it to frame metadata.

        Parameters:
        ----------

        :param Int scan_max: maximum line numbers to scan for VITC data (from -1 to INT_MAX) (default 45)
        :param Double thr_b: black color threshold (from 0 to 1) (default 0.2)
        :param Double thr_w: white color threshold (from 0 to 1) (default 0.6)

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

    def realtime(self, *, limit: Duration = Default(2.0), speed: Double = Default(1.0), **kwargs: Any) -> "VideoStream":
        """

        Slow down filtering to match realtime.

        Parameters:
        ----------

        :param Duration limit: sleep time limit (default 2)
        :param Double speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)

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
        format: Int | Literal["color", "gray"] | Default = Default("color"),
        fill: Color = Default("black"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remap pixels.

        Parameters:
        ----------

        :param Int format: set output format (from 0 to 1) (default color)
        :param Color fill: set the color of the unmapped pixels (default "black")

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
        m0: Int = Default(0),
        m1: Int = Default(0),
        m2: Int = Default(0),
        m3: Int = Default(0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove grain.

        Parameters:
        ----------

        :param Int m0: set mode for 1st plane (from 0 to 24) (default 0)
        :param Int m1: set mode for 2nd plane (from 0 to 24) (default 0)
        :param Int m2: set mode for 3rd plane (from 0 to 24) (default 0)
        :param Int m3: set mode for 4th plane (from 0 to 24) (default 0)
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
        self, *, filename: String = Default(None), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Remove a TV logo based on a mask image.

        Parameters:
        ----------

        :param String filename: set bitmap filename
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
        rh: Int = Default(0),
        rv: Int = Default(0),
        gh: Int = Default(0),
        gv: Int = Default(0),
        bh: Int = Default(0),
        bv: Int = Default(0),
        ah: Int = Default(0),
        av: Int = Default(0),
        edge: Int | Literal["smear", "wrap"] | Default = Default("smear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift RGBA.

        Parameters:
        ----------

        :param Int rh: shift red horizontally (from -255 to 255) (default 0)
        :param Int rv: shift red vertically (from -255 to 255) (default 0)
        :param Int gh: shift green horizontally (from -255 to 255) (default 0)
        :param Int gv: shift green vertically (from -255 to 255) (default 0)
        :param Int bh: shift blue horizontally (from -255 to 255) (default 0)
        :param Int bv: shift blue vertically (from -255 to 255) (default 0)
        :param Int ah: shift alpha horizontally (from -255 to 255) (default 0)
        :param Int av: shift alpha vertically (from -255 to 255) (default 0)
        :param Int edge: set edge operation (from 0 to 1) (default smear)
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
        planes: Int = Default(15),
        scale: Float = Default(1.0),
        delta: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply roberts cross operator.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float scale: set scale (from 0 to 65535) (default 1)
        :param Float delta: set delta (from -65535 to 65535) (default 0)
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
        angle: String = Default("0"),
        out_w: String = Default("iw"),
        out_h: String = Default("ih"),
        fillcolor: String = Default("black"),
        bilinear: Boolean = Default(True),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rotate the input image.

        Parameters:
        ----------

        :param String angle: set angle (in radians) (default "0")
        :param String out_w: set output width expression (default "iw")
        :param String out_h: set output height expression (default "ih")
        :param String fillcolor: set background fill color (default "black")
        :param Boolean bilinear: use bilinear interpolation (default true)
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
        luma_radius: Float = Default(1.0),
        luma_pre_filter_radius: Float = Default(1.0),
        luma_strength: Float = Default(1.0),
        chroma_radius: Float = Default(-0.9),
        chroma_pre_filter_radius: Float = Default(-0.9),
        chroma_strength: Float = Default(-0.9),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply shape adaptive blur.

        Parameters:
        ----------

        :param Float luma_radius: set luma radius (from 0.1 to 4) (default 1)
        :param Float luma_pre_filter_radius: set luma pre-filter radius (from 0.1 to 2) (default 1)
        :param Float luma_strength: set luma strength (from 0.1 to 100) (default 1)
        :param Float chroma_radius: set chroma radius (from -0.9 to 4) (default -0.9)
        :param Float chroma_pre_filter_radius: set chroma pre-filter radius (from -0.9 to 2) (default -0.9)
        :param Float chroma_strength: set chroma strength (from -0.9 to 100) (default -0.9)
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
        w: String = Default(None),
        h: String = Default(None),
        flags: String = Default(""),
        interl: Boolean = Default(False),
        in_color_matrix: String
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default("auto"),
        out_color_matrix: String
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default(None),
        in_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        out_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        in_v_chr_pos: Int = Default(-513),
        in_h_chr_pos: Int = Default(-513),
        out_v_chr_pos: Int = Default(-513),
        out_h_chr_pos: Int = Default(-513),
        force_original_aspect_ratio: Int | Literal["disable", "decrease", "increase"] | Default = Default("disable"),
        force_divisible_by: Int = Default(1),
        param0: Double = Default("DBL_MAX"),
        param1: Double = Default("DBL_MAX"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scale the input video size and/or convert the image format.

        Parameters:
        ----------

        :param String w: Output video width
        :param String h: Output video height
        :param String flags: Flags to pass to libswscale (default "")
        :param Boolean interl: set interlacing (default false)
        :param String in_color_matrix: set input YCbCr type (default "auto")
        :param String out_color_matrix: set output YCbCr type
        :param Int in_range: set input color range (from 0 to 2) (default auto)
        :param Int out_range: set output color range (from 0 to 2) (default auto)
        :param Int in_v_chr_pos: input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int in_h_chr_pos: input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int out_v_chr_pos: output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int out_h_chr_pos: output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
        :param Int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
        :param Double param0: Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param Double param1: Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)

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
        w: String = Default(None),
        h: String = Default(None),
        flags: String = Default(""),
        interl: Boolean = Default(False),
        in_color_matrix: String
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default("auto"),
        out_color_matrix: String
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default(None),
        in_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        out_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        in_v_chr_pos: Int = Default(-513),
        in_h_chr_pos: Int = Default(-513),
        out_v_chr_pos: Int = Default(-513),
        out_h_chr_pos: Int = Default(-513),
        force_original_aspect_ratio: Int | Literal["disable", "decrease", "increase"] | Default = Default("disable"),
        force_divisible_by: Int = Default(1),
        param0: Double = Default("DBL_MAX"),
        param1: Double = Default("DBL_MAX"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        **kwargs: Any,
    ) -> tuple["AudioStream", "AudioStream",]:
        """

        Scale the input video size and/or convert the image format to the given reference.

        Parameters:
        ----------

        :param String w: Output video width
        :param String h: Output video height
        :param String flags: Flags to pass to libswscale (default "")
        :param Boolean interl: set interlacing (default false)
        :param String in_color_matrix: set input YCbCr type (default "auto")
        :param String out_color_matrix: set output YCbCr type
        :param Int in_range: set input color range (from 0 to 2) (default auto)
        :param Int out_range: set output color range (from 0 to 2) (default auto)
        :param Int in_v_chr_pos: input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int in_h_chr_pos: input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int out_v_chr_pos: output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int out_h_chr_pos: output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
        :param Int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
        :param Int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
        :param Double param0: Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param Double param1: Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)

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
            filter_node.audio(0),
            filter_node.audio(1),
        )

    def scdet(
        self, *, threshold: Double = Default(10.0), sc_pass: Boolean = Default(False), **kwargs: Any
    ) -> "VideoStream":
        """

        Detect video scene change

        Parameters:
        ----------

        :param Double threshold: set scene change detect threshold (from 0 to 100) (default 10)
        :param Boolean sc_pass: Set the flag to pass scene change frames (default false)

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
        planes: Int = Default(15),
        scale: Float = Default(1.0),
        delta: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply scharr operator.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float scale: set scale (from 0 to 65535) (default 1)
        :param Float delta: set delta (from -65535 to 65535) (default 0)
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
        horizontal: Float = Default(0.0),
        vertical: Float = Default(0.0),
        hpos: Float = Default(0.0),
        vpos: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scroll input video.

        Parameters:
        ----------

        :param Float horizontal: set the horizontal scrolling speed (from -1 to 1) (default 0)
        :param Float vertical: set the vertical scrolling speed (from -1 to 1) (default 0)
        :param Float hpos: set initial horizontal position (from 0 to 1) (default 0)
        :param Float vpos: set initial vertical position (from 0 to 1) (default 0)
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
        self, *, timestamps: String = Default(None), frames: String = Default(None), **kwargs: Any
    ) -> FilterNode:
        """

        Segment video stream.

        Parameters:
        ----------

        :param String timestamps: timestamps of input at which to split input
        :param String frames: frames at which to split input

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

    def select(self, *, expr: String = Default("1"), outputs: Int = Default(1), **kwargs: Any) -> FilterNode:
        """

        Select video frames to pass in output.

        Parameters:
        ----------

        :param String expr: set an expression to use for selecting frames (default "1")
        :param Int outputs: set the number of outputs (from 1 to INT_MAX) (default 1)

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
        correction_method: Int | Literal["absolute", "relative"] | Default = Default("absolute"),
        reds: String = Default(None),
        yellows: String = Default(None),
        greens: String = Default(None),
        cyans: String = Default(None),
        blues: String = Default(None),
        magentas: String = Default(None),
        whites: String = Default(None),
        neutrals: String = Default(None),
        blacks: String = Default(None),
        psfile: String = Default(None),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply CMYK adjustments to specific color ranges.

        Parameters:
        ----------

        :param Int correction_method: select correction method (from 0 to 1) (default absolute)
        :param String reds: adjust red regions
        :param String yellows: adjust yellow regions
        :param String greens: adjust green regions
        :param String cyans: adjust cyan regions
        :param String blues: adjust blue regions
        :param String magentas: adjust magenta regions
        :param String whites: adjust white regions
        :param String neutrals: adjust neutral regions
        :param String blacks: adjust black regions
        :param String psfile: set Photoshop selectivecolor file name
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
        self, *, commands: String = Default(None), filename: String = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Send commands to filters.

        Parameters:
        ----------

        :param String commands: set commands
        :param String filename: set commands file

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

    def setdar(self, *, dar: String = Default("0"), max: Int = Default(100), **kwargs: Any) -> "VideoStream":
        """

        Set the frame display aspect ratio.

        Parameters:
        ----------

        :param String dar: set display aspect ratio (default "0")
        :param Int max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)

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
        self, *, mode: Int | Literal["auto", "bff", "tff", "prog"] | Default = Default("auto"), **kwargs: Any
    ) -> "VideoStream":
        """

        Force field for the output video frame.

        Parameters:
        ----------

        :param Int mode: select interlace mode (from -1 to 2) (default auto)

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
        field_mode: Int | Literal["auto", "bff", "tff", "prog"] | Default = Default("auto"),
        range: Int
        | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
        | Default = Default("auto"),
        color_primaries: Int
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
        color_trc: Int
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
        colorspace: Int
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

        :param Int field_mode: select interlace mode (from -1 to 2) (default auto)
        :param Int range: select color range (from -1 to 2) (default auto)
        :param Int color_primaries: select color primaries (from -1 to 22) (default auto)
        :param Int color_trc: select color transfer (from -1 to 18) (default auto)
        :param Int colorspace: select colorspace (from -1 to 14) (default auto)

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

    def setpts(self, *, expr: String = Default("PTS"), **kwargs: Any) -> "VideoStream":
        """

        Set PTS for the output video frame.

        Parameters:
        ----------

        :param String expr: Expression determining the frame timestamp (default "PTS")

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
        range: Int
        | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
        | Default = Default("auto"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force color range for the output video frame.

        Parameters:
        ----------

        :param Int range: select color range (from -1 to 2) (default auto)

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

    def setsar(self, *, sar: String = Default("0"), max: Int = Default(100), **kwargs: Any) -> "VideoStream":
        """

        Set the pixel sample aspect ratio.

        Parameters:
        ----------

        :param String sar: set sample (pixel) aspect ratio (default "0")
        :param Int max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)

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

    def settb(self, *, expr: String = Default("intb"), **kwargs: Any) -> "VideoStream":
        """

        Set timebase for the video output link.

        Parameters:
        ----------

        :param String expr: set expression determining the output timebase (default "intb")

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
        shx: Float = Default(0.0),
        shy: Float = Default(0.0),
        fillcolor: String = Default("black"),
        interp: Int | Literal["nearest", "bilinear"] | Default = Default("bilinear"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shear transform the input image.

        Parameters:
        ----------

        :param Float shx: set x shear factor (from -2 to 2) (default 0)
        :param Float shy: set y shear factor (from -2 to 2) (default 0)
        :param String fillcolor: set background fill color (default "black")
        :param Int interp: set interpolation (from 0 to 1) (default bilinear)
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

    def showinfo(self, *, checksum: Boolean = Default(True), **kwargs: Any) -> "VideoStream":
        """

        Show textual information for each video frame.

        Parameters:
        ----------

        :param Boolean checksum: calculate checksums (default true)

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

    def showpalette(self, *, s: Int = Default(30), **kwargs: Any) -> "VideoStream":
        """

        Display frame palette.

        Parameters:
        ----------

        :param Int s: set pixel box size (from 1 to 100) (default 30)

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
        self, *, mapping: String = Default("0"), enable: str = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Shuffle video frames.

        Parameters:
        ----------

        :param String mapping: set destination indexes of input frames (default "0")
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
        direction: Int | Literal["forward", "inverse"] | Default = Default("forward"),
        mode: Int | Literal["horizontal", "vertical", "block"] | Default = Default("horizontal"),
        width: Int = Default(10),
        height: Int = Default(10),
        seed: Int64 = Default(-1),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video pixels.

        Parameters:
        ----------

        :param Int direction: set shuffle direction (from 0 to 1) (default forward)
        :param Int mode: set shuffle mode (from 0 to 2) (default horizontal)
        :param Int width: set block width (from 1 to 8000) (default 10)
        :param Int height: set block height (from 1 to 8000) (default 10)
        :param Int64 seed: set random seed (from -1 to UINT32_MAX) (default -1)
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
        map0: Int = Default(0),
        map1: Int = Default(1),
        map2: Int = Default(2),
        map3: Int = Default(3),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video planes.

        Parameters:
        ----------

        :param Int map0: Index of the input plane to be used as the first output plane (from 0 to 3) (default 0)
        :param Int map1: Index of the input plane to be used as the second output plane (from 0 to 3) (default 1)
        :param Int map2: Index of the input plane to be used as the third output plane (from 0 to 3) (default 2)
        :param Int map3: Index of the input plane to be used as the fourth output plane (from 0 to 3) (default 3)
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
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Manipulate video frame side data.

        Parameters:
        ----------

        :param Int mode: set a mode of operation (from 0 to 1) (default select)
        :param Int type: set side data type (from -1 to INT_MAX) (default -1)
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
        stat: Flags | Literal["tout", "vrep", "brng"] | Default = Default("0"),
        out: Int | Literal["tout", "vrep", "brng"] | Default = Default(-1),
        c: Color = Default("yellow"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate statistics from video analysis.

        Parameters:
        ----------

        :param Flags stat: set statistics filters (default 0)
        :param Int out: set video filter (from -1 to 2) (default -1)
        :param Color c: set highlight color (default "yellow")

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

    def siti(self, *, print_summary: Boolean = Default(False), **kwargs: Any) -> "VideoStream":
        """

        Calculate spatial information (SI) and temporal information (TI).

        Parameters:
        ----------

        :param Boolean print_summary: Print summary showing average values (default false)

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
        luma_radius: Float = Default(1.0),
        luma_strength: Float = Default(1.0),
        luma_threshold: Int = Default(0),
        chroma_radius: Float = Default(-0.9),
        chroma_strength: Float = Default(-2.0),
        chroma_threshold: Int = Default(-31),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input video without impacting the outlines.

        Parameters:
        ----------

        :param Float luma_radius: set luma radius (from 0.1 to 5) (default 1)
        :param Float luma_strength: set luma strength (from -1 to 1) (default 1)
        :param Int luma_threshold: set luma threshold (from -30 to 30) (default 0)
        :param Float chroma_radius: set chroma radius (from -0.9 to 5) (default -0.9)
        :param Float chroma_strength: set chroma strength (from -2 to 1) (default -2)
        :param Int chroma_threshold: set chroma threshold (from -31 to 30) (default -31)
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
        planes: Int = Default(15),
        scale: Float = Default(1.0),
        delta: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply sobel operator.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float scale: set scale (from 0 to 65535) (default 1)
        :param Float delta: set delta (from -65535 to 65535) (default 0)
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
        sample_rate: Int = Default(44100),
        channels: Int = Default(1),
        scale: Int | Literal["lin", "log"] | Default = Default("log"),
        slide: Int | Literal["replace", "scroll", "fullframe", "rscroll"] | Default = Default("fullframe"),
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
        | Default = Default("rect"),
        overlap: Float = Default(1.0),
        orientation: Int | Literal["vertical", "horizontal"] | Default = Default("vertical"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Convert input spectrum videos to audio output.

        Parameters:
        ----------

        :param Int sample_rate: set sample rate (from 15 to INT_MAX) (default 44100)
        :param Int channels: set channels (from 1 to 8) (default 1)
        :param Int scale: set input amplitude scale (from 0 to 1) (default log)
        :param Int slide: set input sliding mode (from 0 to 3) (default fullframe)
        :param Int win_func: set window function (from 0 to 20) (default rect)
        :param Float overlap: set window overlap (from 0 to 1) (default 1)
        :param Int orientation: set orientation (from 0 to 1) (default vertical)

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

    def split(self, *, outputs: Int = Default(2), **kwargs: Any) -> FilterNode:
        """

        Pass on the input to N video outputs.

        Parameters:
        ----------

        :param Int outputs: set number of outputs (from 1 to INT_MAX) (default 2)

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
        quality: Int = Default(3),
        qp: Int = Default(0),
        mode: Int | Literal["hard", "soft"] | Default = Default("hard"),
        use_bframe_qp: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a simple post processing filter.

        Parameters:
        ----------

        :param Int quality: set quality (from 0 to 6) (default 3)
        :param Int qp: force a constant quantizer parameter (from 0 to 63) (default 0)
        :param Int mode: set thresholding mode (from 0 to 1) (default hard)
        :param Boolean use_bframe_qp: use B-frames' QP (default false)
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
        dnn_backend: Int | Literal["native"] | Default = Default("native"),
        scale_factor: Int = Default(2),
        model: String = Default(None),
        input: String = Default("x"),
        output: String = Default("y"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN-based image super resolution to the input.

        Parameters:
        ----------

        :param Int dnn_backend: DNN backend used for model execution (from 0 to 1) (default native)
        :param Int scale_factor: scale factor for SRCNN model (from 2 to 4) (default 2)
        :param String model: path to model file specifying network architecture and its parameters
        :param String input: input name of the model (default "x")
        :param String output: output name of the model (default "y")

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
        stats_file: String = Default(None),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the SSIM between two video streams.

        Parameters:
        ----------

        :param String stats_file: Set file where to store per-frame difference information
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        _in: Int
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
        out: Int
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

        :param Int _in: set input format (from 16 to 32) (default sbsl)
        :param Int out: set output format (from 0 to 32) (default arcd)

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
        filename: String = Default(None),
        original_size: Image_size = Default(None),
        fontsdir: String = Default(None),
        alpha: Boolean = Default(False),
        charenc: String = Default(None),
        stream_index: Int = Default(-1),
        force_style: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render text subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param String filename: set the filename of file to read
        :param Image_size original_size: set the size of the original video (used to scale fonts)
        :param String fontsdir: set the directory containing the fonts to read
        :param Boolean alpha: enable processing of alpha channel (default false)
        :param String charenc: set input character encoding
        :param Int stream_index: set stream index (from -1 to INT_MAX) (default -1)
        :param String force_style: force subtitle style

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
        w: String = Default("w/2"),
        h: String = Default("h/2"),
        x1: String = Default("w/2"),
        y1: String = Default("h/2"),
        x2: String = Default("0"),
        y2: String = Default("0"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Swap 2 rectangular objects in video.

        Parameters:
        ----------

        :param String w: set rect width (default "w/2")
        :param String h: set rect height (default "h/2")
        :param String x1: set 1st rect x top left coordinate (default "w/2")
        :param String y1: set 1st rect y top left coordinate (default "h/2")
        :param String x2: set 2nd rect x top left coordinate (default "0")
        :param String y2: set 2nd rect y top left coordinate (default "0")
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
        c0_mode: Int
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
        c1_mode: Int
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
        c2_mode: Int
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
        c3_mode: Int
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
        all_mode: Int
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
        | Default = Default(-1),
        c0_expr: String = Default(None),
        c1_expr: String = Default(None),
        c2_expr: String = Default(None),
        c3_expr: String = Default(None),
        all_expr: String = Default(None),
        c0_opacity: Double = Default(1.0),
        c1_opacity: Double = Default(1.0),
        c2_opacity: Double = Default(1.0),
        c3_opacity: Double = Default(1.0),
        all_opacity: Double = Default(1.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blend successive frames.

        Parameters:
        ----------

        :param Int c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
        :param Int c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
        :param Int c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
        :param Int c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
        :param Int all_mode: set blend mode for all components (from -1 to 39) (default -1)
        :param String c0_expr: set color component #0 expression
        :param String c1_expr: set color component #1 expression
        :param String c2_expr: set color component #2 expression
        :param String c3_expr: set color component #3 expression
        :param String all_expr: set expression for all color components
        :param Double c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
        :param Double c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
        :param Double c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
        :param Double c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
        :param Double all_opacity: set opacity for all color components (from 0 to 1) (default 1)
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
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default("top"),
        pattern: String = Default("23"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a telecine pattern.

        Parameters:
        ----------

        :param Int first_field: select first field (from 0 to 1) (default top)
        :param String pattern: pattern that describe for how many fields a frame is to be displayed (default "23")

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
        width: Int = Default(0),
        display_mode: Int | Literal["overlay", "parade", "stack"] | Default = Default("stack"),
        levels_mode: Int | Literal["linear", "logarithmic"] | Default = Default("linear"),
        components: Int = Default(7),
        bgopacity: Float = Default(0.9),
        envelope: Boolean = Default(False),
        ecolor: Color = Default("gold"),
        slide: Int | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default("replace"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and draw a temporal histogram.

        Parameters:
        ----------

        :param Int width: set width (from 0 to 8192) (default 0)
        :param Int display_mode: set display mode (from 0 to 2) (default stack)
        :param Int levels_mode: set levels mode (from 0 to 1) (default linear)
        :param Int components: set color components to display (from 1 to 15) (default 7)
        :param Float bgopacity: set background opacity (from 0 to 1) (default 0.9)
        :param Boolean envelope: display envelope (default false)
        :param Color ecolor: set envelope color (default "gold")
        :param Int slide: set slide mode (from 0 to 4) (default replace)

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
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Threshold first video stream using other video streams.

        Parameters:
        ----------

        :param Int planes: set planes to filter (from 0 to 15) (default 15)
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
        n: Int = Default(100),
        log: Int | Literal["quiet", "info", "verbose"] | Default = Default("info"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Select the most representative frame in a given sequence of consecutive frames.

        Parameters:
        ----------

        :param Int n: set the frames batch size (from 2 to INT_MAX) (default 100)
        :param Int log: force stats logging level (from INT_MIN to INT_MAX) (default info)
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
        layout: Image_size = Default("6x5"),
        nb_frames: Int = Default(0),
        margin: Int = Default(0),
        padding: Int = Default(0),
        color: Color = Default("black"),
        overlap: Int = Default(0),
        init_padding: Int = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Tile several successive frames together.

        Parameters:
        ----------

        :param Image_size layout: set grid size (default "6x5")
        :param Int nb_frames: set maximum number of frame to render (from 0 to INT_MAX) (default 0)
        :param Int margin: set outer border margin in pixels (from 0 to 1024) (default 0)
        :param Int padding: set inner border thickness in pixels (from 0 to 1024) (default 0)
        :param Color color: set the color of the unused area (default "black")
        :param Int overlap: set how many frames to overlap for each render (from 0 to INT_MAX) (default 0)
        :param Int init_padding: set how many frames to initially pad (from 0 to INT_MAX) (default 0)

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
        mode: Int
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

        :param Int mode: select interlace mode (from 0 to 7) (default merge)

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
        c0: String = Default("x"),
        c1: String = Default("x"),
        c2: String = Default("x"),
        c3: String = Default("x"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table from two successive frames.

        Parameters:
        ----------

        :param String c0: set component #0 expression (default "x")
        :param String c1: set component #1 expression (default "x")
        :param String c2: set component #2 expression (default "x")
        :param String c3: set component #3 expression (default "x")
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
        radius: Int = Default(1),
        planes: Int = Default(15),
        percentile: Float = Default(0.5),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick median pixels from successive frames.

        Parameters:
        ----------

        :param Int radius: set median filter radius (from 1 to 127) (default 1)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Float percentile: set percentile (from 0 to 1) (default 0.5)
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
        radius: Int = Default(5),
        sigma: Float = Default(0.5),
        planes: Int = Default(15),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Temporal Midway Equalization.

        Parameters:
        ----------

        :param Int radius: set radius (from 1 to 127) (default 5)
        :param Float sigma: set sigma (from 0 to 1) (default 0.5)
        :param Int planes: set planes (from 0 to 15) (default 15)
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
        frames: Int = Default(3),
        weights: String = Default("1 1 1"),
        scale: Float = Default(0.0),
        planes: Flags = Default("F"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Mix successive video frames.

        Parameters:
        ----------

        :param Int frames: set number of successive frames to mix (from 1 to 1024) (default 3)
        :param String weights: set weight for each frame (default "1 1 1")
        :param Float scale: set scale (from 0 to 32767) (default 0)
        :param Flags planes: set what planes to filter (default F)
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
        tonemap: Int
        | Literal["none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"]
        | Default = Default("none"),
        param: Double = Default("nan"),
        desat: Double = Default(2.0),
        peak: Double = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Conversion to/from different dynamic ranges.

        Parameters:
        ----------

        :param Int tonemap: tonemap algorithm selection (from 0 to 6) (default none)
        :param Double param: tonemap parameter (from DBL_MIN to DBL_MAX) (default nan)
        :param Double desat: desaturation strength (from 0 to DBL_MAX) (default 2)
        :param Double peak: signal peak override (from 0 to DBL_MAX) (default 0)

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
        start: Int = Default(0),
        stop: Int = Default(0),
        start_mode: Int | Literal["add", "clone"] | Default = Default("add"),
        stop_mode: Int | Literal["add", "clone"] | Default = Default("add"),
        start_duration: Duration = Default(0.0),
        stop_duration: Duration = Default(0.0),
        color: Color = Default("black"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Temporarily pad video frames.

        Parameters:
        ----------

        :param Int start: set the number of frames to delay input (from 0 to INT_MAX) (default 0)
        :param Int stop: set the number of frames to add after input finished (from -1 to INT_MAX) (default 0)
        :param Int start_mode: set the mode of added frames to start (from 0 to 1) (default add)
        :param Int stop_mode: set the mode of added frames to end (from 0 to 1) (default add)
        :param Duration start_duration: set the duration to delay input (default 0)
        :param Duration stop_duration: set the duration to pad input (default 0)
        :param Color color: set the color of the added frames (default "black")

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
        dir: Int | Literal["cclock_flip", "clock", "cclock", "clock_flip"] | Default = Default("cclock_flip"),
        passthrough: Int | Literal["none", "portrait", "landscape"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transpose input video.

        Parameters:
        ----------

        :param Int dir: set transpose direction (from 0 to 7) (default cclock_flip)
        :param Int passthrough: do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)

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
        start: Duration = Default("INT64_MAX"),
        end: Duration = Default("INT64_MAX"),
        start_pts: Int64 = Default("I64_MIN"),
        end_pts: Int64 = Default("I64_MIN"),
        duration: Duration = Default(0.0),
        start_frame: Int64 = Default(-1),
        end_frame: Int64 = Default("I64_MAX"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick one continuous section from the input, drop the rest.

        Parameters:
        ----------

        :param Duration start: Timestamp of the first frame that should be passed (default INT64_MAX)
        :param Duration end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
        :param Int64 start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
        :param Int64 end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
        :param Duration duration: Maximum duration of the output (default 0)
        :param Int64 start_frame: Number of the first frame that should be passed to the output (from -1 to I64_MAX) (default -1)
        :param Int64 end_frame: Number of the first frame that should be dropped again (from 0 to I64_MAX) (default I64_MAX)

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
        luma_msize_x: Int = Default(5),
        luma_msize_y: Int = Default(5),
        luma_amount: Float = Default(1.0),
        chroma_msize_x: Int = Default(5),
        chroma_msize_y: Int = Default(5),
        chroma_amount: Float = Default(0.0),
        alpha_msize_x: Int = Default(5),
        alpha_msize_y: Int = Default(5),
        alpha_amount: Float = Default(0.0),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Sharpen or blur the input video.

        Parameters:
        ----------

        :param Int luma_msize_x: set luma matrix horizontal size (from 3 to 23) (default 5)
        :param Int luma_msize_y: set luma matrix vertical size (from 3 to 23) (default 5)
        :param Float luma_amount: set luma effect strength (from -2 to 5) (default 1)
        :param Int chroma_msize_x: set chroma matrix horizontal size (from 3 to 23) (default 5)
        :param Int chroma_msize_y: set chroma matrix vertical size (from 3 to 23) (default 5)
        :param Float chroma_amount: set chroma effect strength (from -2 to 5) (default 0)
        :param Int alpha_msize_x: set alpha matrix horizontal size (from 3 to 23) (default 5)
        :param Int alpha_msize_y: set alpha matrix vertical size (from 3 to 23) (default 5)
        :param Float alpha_amount: set alpha effect strength (from -2 to 5) (default 0)
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

    def untile(self, *, layout: Image_size = Default("6x5"), **kwargs: Any) -> "VideoStream":
        """

        Untile a frame into a sequence of frames.

        Parameters:
        ----------

        :param Image_size layout: set grid size (default "6x5")

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
        input: Int
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
        output: Int
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
        interp: Int
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
        w: Int = Default(0),
        h: Int = Default(0),
        in_stereo: Int | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        out_stereo: Int | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        in_forder: String = Default("rludfb"),
        out_forder: String = Default("rludfb"),
        in_frot: String = Default("000000"),
        out_frot: String = Default("000000"),
        in_pad: Float = Default(0.0),
        out_pad: Float = Default(0.0),
        fin_pad: Int = Default(0),
        fout_pad: Int = Default(0),
        yaw: Float = Default(0.0),
        pitch: Float = Default(0.0),
        roll: Float = Default(0.0),
        rorder: String = Default("ypr"),
        h_fov: Float = Default(0.0),
        v_fov: Float = Default(0.0),
        d_fov: Float = Default(0.0),
        h_flip: Boolean = Default(False),
        v_flip: Boolean = Default(False),
        d_flip: Boolean = Default(False),
        ih_flip: Boolean = Default(False),
        iv_flip: Boolean = Default(False),
        in_trans: Boolean = Default(False),
        out_trans: Boolean = Default(False),
        ih_fov: Float = Default(0.0),
        iv_fov: Float = Default(0.0),
        id_fov: Float = Default(0.0),
        h_offset: Float = Default(0.0),
        v_offset: Float = Default(0.0),
        alpha_mask: Boolean = Default(False),
        reset_rot: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert 360 projection of video.

        Parameters:
        ----------

        :param Int input: set input projection (from 0 to 24) (default e)
        :param Int output: set output projection (from 0 to 24) (default c3x2)
        :param Int interp: set interpolation method (from 0 to 7) (default line)
        :param Int w: output width (from 0 to 32767) (default 0)
        :param Int h: output height (from 0 to 32767) (default 0)
        :param Int in_stereo: input stereo format (from 0 to 2) (default 2d)
        :param Int out_stereo: output stereo format (from 0 to 2) (default 2d)
        :param String in_forder: input cubemap face order (default "rludfb")
        :param String out_forder: output cubemap face order (default "rludfb")
        :param String in_frot: input cubemap face rotation (default "000000")
        :param String out_frot: output cubemap face rotation (default "000000")
        :param Float in_pad: percent input cubemap pads (from 0 to 0.1) (default 0)
        :param Float out_pad: percent output cubemap pads (from 0 to 0.1) (default 0)
        :param Int fin_pad: fixed input cubemap pads (from 0 to 100) (default 0)
        :param Int fout_pad: fixed output cubemap pads (from 0 to 100) (default 0)
        :param Float yaw: yaw rotation (from -180 to 180) (default 0)
        :param Float pitch: pitch rotation (from -180 to 180) (default 0)
        :param Float roll: roll rotation (from -180 to 180) (default 0)
        :param String rorder: rotation order (default "ypr")
        :param Float h_fov: output horizontal field of view (from 0 to 360) (default 0)
        :param Float v_fov: output vertical field of view (from 0 to 360) (default 0)
        :param Float d_fov: output diagonal field of view (from 0 to 360) (default 0)
        :param Boolean h_flip: flip out video horizontally (default false)
        :param Boolean v_flip: flip out video vertically (default false)
        :param Boolean d_flip: flip out video indepth (default false)
        :param Boolean ih_flip: flip in video horizontally (default false)
        :param Boolean iv_flip: flip in video vertically (default false)
        :param Boolean in_trans: transpose video input (default false)
        :param Boolean out_trans: transpose video output (default false)
        :param Float ih_fov: input horizontal field of view (from 0 to 360) (default 0)
        :param Float iv_fov: input vertical field of view (from 0 to 360) (default 0)
        :param Float id_fov: input diagonal field of view (from 0 to 360) (default 0)
        :param Float h_offset: output horizontal off-axis offset (from -1 to 1) (default 0)
        :param Float v_offset: output vertical off-axis offset (from -1 to 1) (default 0)
        :param Boolean alpha_mask: build mask in alpha plane (default false)
        :param Boolean reset_rot: reset rotation (default false)

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
        threshold: Float = Default(2.0),
        method: Int | Literal["hard", "soft", "garrote"] | Default = Default("garrote"),
        nsteps: Int = Default(6),
        percent: Float = Default(85.0),
        planes: Int = Default(15),
        type: Int | Literal["universal", "bayes"] | Default = Default("universal"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a Wavelet based Denoiser.

        Parameters:
        ----------

        :param Float threshold: set filtering strength (from 0 to DBL_MAX) (default 2)
        :param Int method: set filtering method (from 0 to 2) (default garrote)
        :param Int nsteps: set number of steps (from 1 to 32) (default 6)
        :param Float percent: set percent of full denoising (from 0 to 100) (default 85)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Int type: set threshold type (from 0 to 1) (default universal)
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
        min_r: Int = Default(0),
        max_r: Int = Default(8),
        planes: Int = Default(15),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Variable Blur filter.

        Parameters:
        ----------

        :param Int min_r: set min blur radius (from 0 to 254) (default 0)
        :param Int max_r: set max blur radius (from 1 to 255) (default 8)
        :param Int planes: set planes to filter (from 0 to 15) (default 15)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        mode: Int
        | Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | Default = Default("gray"),
        x: Int = Default(1),
        y: Int = Default(2),
        intensity: Float = Default(0.004),
        envelope: Int | Literal["none", "instant", "peak", "instant"] | Default = Default("none"),
        graticule: Int | Literal["none", "green", "color", "invert"] | Default = Default("none"),
        opacity: Float = Default(0.75),
        flags: Flags | Literal["white", "black", "name"] | Default = Default("name"),
        bgopacity: Float = Default(0.3),
        lthreshold: Float = Default(0.0),
        hthreshold: Float = Default(1.0),
        colorspace: Int | Literal["auto", "601", "709"] | Default = Default("auto"),
        tint0: Float = Default(0.0),
        tint1: Float = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video vectorscope.

        Parameters:
        ----------

        :param Int mode: set vectorscope mode (from 0 to 5) (default gray)
        :param Int x: set color component on X axis (from 0 to 2) (default 1)
        :param Int y: set color component on Y axis (from 0 to 2) (default 2)
        :param Float intensity: set intensity (from 0 to 1) (default 0.004)
        :param Int envelope: set envelope (from 0 to 3) (default none)
        :param Int graticule: set graticule (from 0 to 3) (default none)
        :param Float opacity: set graticule opacity (from 0 to 1) (default 0.75)
        :param Flags flags: set graticule flags (default name)
        :param Float bgopacity: set background opacity (from 0 to 1) (default 0.3)
        :param Float lthreshold: set low threshold (from 0 to 1) (default 0)
        :param Float hthreshold: set high threshold (from 0 to 1) (default 1)
        :param Int colorspace: set colorspace (from 0 to 2) (default auto)
        :param Float tint0: set 1st tint (from -1 to 1) (default 0)
        :param Float tint1: set 2nd tint (from -1 to 1) (default 0)

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
        intensity: Float = Default(0.0),
        rbal: Float = Default(1.0),
        gbal: Float = Default(1.0),
        bbal: Float = Default(1.0),
        rlum: Float = Default(0.072186),
        glum: Float = Default(0.715158),
        blum: Float = Default(0.212656),
        alternate: Boolean = Default(False),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Boost or alter saturation.

        Parameters:
        ----------

        :param Float intensity: set the intensity value (from -2 to 2) (default 0)
        :param Float rbal: set the red balance value (from -10 to 10) (default 1)
        :param Float gbal: set the green balance value (from -10 to 10) (default 1)
        :param Float bbal: set the blue balance value (from -10 to 10) (default 1)
        :param Float rlum: set the red luma coefficient (from 0 to 1) (default 0.072186)
        :param Float glum: set the green luma coefficient (from 0 to 1) (default 0.715158)
        :param Float blum: set the blue luma coefficient (from 0 to 1) (default 0.212656)
        :param Boolean alternate: use alternate colors (default false)
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
        result: String = Default("transforms.trf"),
        shakiness: Int = Default(5),
        accuracy: Int = Default(15),
        stepsize: Int = Default(6),
        mincontrast: Double = Default(0.25),
        show: Int = Default(0),
        tripod: Int = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2).

        Parameters:
        ----------

        :param String result: path to the file used to write the transforms (default "transforms.trf")
        :param Int shakiness: how shaky is the video and how quick is the camera? 1: little (fast) 10: very strong/quick (slow) (from 1 to 10) (default 5)
        :param Int accuracy: (>=shakiness) 1: low 15: high (slow) (from 1 to 15) (default 15)
        :param Int stepsize: region around minimum is scanned with 1 pixel resolution (from 1 to 32) (default 6)
        :param Double mincontrast: below this contrast a field is discarded (0-1) (from 0 to 1) (default 0.25)
        :param Int show: 0: draw nothing; 1,2: show fields and transforms (from 0 to 2) (default 0)
        :param Int tripod: virtual tripod mode (if >0): motion is compared to a reference reference frame (frame # is the value) (from 0 to INT_MAX) (default 0)

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
        input: String = Default("transforms.trf"),
        smoothing: Int = Default(15),
        optalgo: Int | Literal["opt", "gauss", "avg"] | Default = Default("opt"),
        maxshift: Int = Default(-1),
        maxangle: Double = Default(-1.0),
        crop: Int | Literal["keep", "black"] | Default = Default("keep"),
        invert: Int = Default(0),
        relative: Int = Default(1),
        zoom: Double = Default(0.0),
        optzoom: Int = Default(1),
        zoomspeed: Double = Default(0.25),
        interpol: Int | Literal["no", "linear", "bilinear", "bicubic"] | Default = Default("bilinear"),
        tripod: Boolean = Default(False),
        debug: Boolean = Default(False),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1).

        Parameters:
        ----------

        :param String input: set path to the file storing the transforms (default "transforms.trf")
        :param Int smoothing: set number of frames*2 + 1 used for lowpass filtering (from 0 to 1000) (default 15)
        :param Int optalgo: set camera path optimization algo (from 0 to 2) (default opt)
        :param Int maxshift: set maximal number of pixels to translate image (from -1 to 500) (default -1)
        :param Double maxangle: set maximal angle in rad to rotate image (from -1 to 3.14) (default -1)
        :param Int crop: set cropping mode (from 0 to 1) (default keep)
        :param Int invert: invert transforms (from 0 to 1) (default 0)
        :param Int relative: consider transforms as relative (from 0 to 1) (default 1)
        :param Double zoom: set percentage to zoom (>0: zoom in, <0: zoom out (from -100 to 100) (default 0)
        :param Int optzoom: set optimal zoom (0: nothing, 1: optimal static zoom, 2: optimal dynamic zoom) (from 0 to 2) (default 1)
        :param Double zoomspeed: for adative zoom: percent to zoom maximally each frame (from 0 to 5) (default 0.25)
        :param Int interpol: set type of interpolation (from 0 to 3) (default bilinear)
        :param Boolean tripod: enable virtual tripod mode (same as relative=0:smoothing=0) (default false)
        :param Boolean debug: enable debug mode and writer global motions information to file (default false)

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
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the VIF between two video streams.

        Parameters:
        ----------

        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        angle: String = Default("PI/5"),
        x0: String = Default("w/2"),
        y0: String = Default("h/2"),
        mode: Int | Literal["forward", "backward"] | Default = Default("forward"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        dither: Boolean = Default(True),
        aspect: Rational = Default("1/1"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make or reverse a vignette effect.

        Parameters:
        ----------

        :param String angle: set lens angle (default "PI/5")
        :param String x0: set circle center position on x-axis (default "w/2")
        :param String y0: set circle center position on y-axis (default "h/2")
        :param Int mode: set forward/backward mode (from 0 to 1) (default forward)
        :param Int eval: specify when to evaluate expressions (from 0 to 1) (default init)
        :param Boolean dither: set dithering (default true)
        :param Rational aspect: set aspect ratio (from 0 to DBL_MAX) (default 1/1)
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

    def vmafmotion(self, *, stats_file: String = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Calculate the VMAF Motion score.

        Parameters:
        ----------

        :param String stats_file: Set file where to store per-frame difference information

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
        filter: Int | Literal["simple", "complex"] | Default = Default("complex"),
        mode: Int | Literal["frame", "field"] | Default = Default("field"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Martin Weston three field deinterlace.

        Parameters:
        ----------

        :param Int filter: specify the filter (from 0 to 1) (default complex)
        :param Int mode: specify the interlacing mode (from 0 to 1) (default field)
        :param Int parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param Int deint: specify which frames to deinterlace (from 0 to 1) (default all)
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
        mode: Int | Literal["row", "column"] | Default = Default("column"),
        intensity: Float = Default(0.04),
        mirror: Boolean = Default(True),
        display: Int | Literal["overlay", "stack", "parade"] | Default = Default("stack"),
        components: Int = Default(1),
        envelope: Int | Literal["none", "instant", "peak", "instant"] | Default = Default("none"),
        filter: Int
        | Literal["lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"]
        | Default = Default("lowpass"),
        graticule: Int | Literal["none", "green", "orange", "invert"] | Default = Default("none"),
        opacity: Float = Default(0.75),
        flags: Flags | Literal["numbers", "dots"] | Default = Default("numbers"),
        scale: Int | Literal["digital", "millivolts", "ire"] | Default = Default("digital"),
        bgopacity: Float = Default(0.75),
        tint0: Float = Default(0.0),
        tint1: Float = Default(0.0),
        fitmode: Int | Literal["none", "size"] | Default = Default("none"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video waveform monitor.

        Parameters:
        ----------

        :param Int mode: set mode (from 0 to 1) (default column)
        :param Float intensity: set intensity (from 0 to 1) (default 0.04)
        :param Boolean mirror: set mirroring (default true)
        :param Int display: set display mode (from 0 to 2) (default stack)
        :param Int components: set components to display (from 1 to 15) (default 1)
        :param Int envelope: set envelope to display (from 0 to 3) (default none)
        :param Int filter: set filter (from 0 to 7) (default lowpass)
        :param Int graticule: set graticule (from 0 to 3) (default none)
        :param Float opacity: set graticule opacity (from 0 to 1) (default 0.75)
        :param Flags flags: set graticule flags (default numbers)
        :param Int scale: set scale (from 0 to 2) (default digital)
        :param Float bgopacity: set background opacity (from 0 to 1) (default 0.75)
        :param Float tint0: set 1st tint (from -1 to 1) (default 0)
        :param Float tint1: set 2nd tint (from -1 to 1) (default 0)
        :param Int fitmode: set fit mode (from 0 to 1) (default none)

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
        self, *, first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default("top"), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into frames.

        Parameters:
        ----------

        :param Int first_field: set first field (from 0 to 1) (default top)

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

    def xbr(self, *, n: Int = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using xBR algorithm.

        Parameters:
        ----------

        :param Int n: set scale factor (from 2 to 4) (default 3)

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
        planes: Int = Default(7),
        secondary: Int | Literal["first", "all"] | Default = Default("all"),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: Boolean = Default(False),
        repeatlast: Boolean = Default(True),
        ts_sync_mode: Int | Literal["default", "nearest"] | Default = Default("default"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Cross-correlate first video stream with second video stream.

        Parameters:
        ----------

        :param Int planes: set planes to cross-correlate (from 0 to 15) (default 7)
        :param Int secondary: when to process secondary frame (from 0 to 1) (default all)
        :param Int eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
        :param Boolean shortest: force termination when the shortest input terminates (default false)
        :param Boolean repeatlast: extend last frame of secondary streams beyond EOF (default true)
        :param Int ts_sync_mode: How strictly to sync streams based on secondary input timestamps (from 0 to 1) (default default)
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
        transition: Int
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
        duration: Duration = Default(1.0),
        offset: Duration = Default(0.0),
        expr: String = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Cross fade one video with another video.

        Parameters:
        ----------

        :param Int transition: set cross fade transition (from -1 to 45) (default fade)
        :param Duration duration: set cross fade duration (default 1)
        :param Duration offset: set cross fade start relative to first input stream (default 0)
        :param String expr: set expression for custom transition

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
        mode: Int
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("send_frame"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param Int mode: specify the interlacing mode (from 0 to 3) (default send_frame)
        :param Int parity: specify the assumed picture field parity (from -1 to 1) (default auto)
        :param Int deint: specify which frames to deinterlace (from 0 to 1) (default all)
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
        radius: Int = Default(3),
        planes: Int = Default(1),
        sigma: Int = Default(128),
        enable: str = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Yet another edge preserving blur filter.

        Parameters:
        ----------

        :param Int radius: set window radius (from 0 to INT_MAX) (default 3)
        :param Int planes: set planes to filter (from 0 to 15) (default 1)
        :param Int sigma: set blur strength (from 1 to INT_MAX) (default 128)
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

    def zmq(self, *, bind_address: String = Default("tcp://*:5555"), **kwargs: Any) -> "VideoStream":
        """

        Receive commands through ZMQ and broker them to filters.

        Parameters:
        ----------

        :param String bind_address: set bind address (default "tcp://*:5555")

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
        zoom: String = Default("1"),
        x: String = Default("0"),
        y: String = Default("0"),
        d: String = Default("90"),
        s: Image_size = Default("hd720"),
        fps: Video_rate = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Zoom & Pan effect.

        Parameters:
        ----------

        :param String zoom: set the zoom expression (default "1")
        :param String x: set the x expression (default "0")
        :param String y: set the y expression (default "0")
        :param String d: set the duration expression (default "90")
        :param Image_size s: set the output image size (default "hd720")
        :param Video_rate fps: set the output framerate (default "25")

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
        w: String = Default(None),
        h: String = Default(None),
        size: String = Default(None),
        dither: Int | Literal["none", "ordered", "random", "error_diffusion"] | Default = Default("none"),
        filter: Int
        | Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | Default = Default("bilinear"),
        out_range: Int | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default("input"),
        primaries: Int
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
        transfer: Int
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
        matrix: Int
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
        in_range: Int | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default("input"),
        primariesin: Int
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
        transferin: Int
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
        matrixin: Int
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
        chromal: Int
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default("input"),
        chromalin: Int
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default("input"),
        npl: Double = Default("nan"),
        agamma: Boolean = Default(True),
        param_a: Double = Default("nan"),
        param_b: Double = Default("nan"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply resizing, colorspace and bit depth conversion.

        Parameters:
        ----------

        :param String w: Output video width
        :param String h: Output video height
        :param String size: set video size
        :param Int dither: set dither type (from 0 to 3) (default none)
        :param Int filter: set filter type (from 0 to 5) (default bilinear)
        :param Int out_range: set color range (from -1 to 1) (default input)
        :param Int primaries: set color primaries (from -1 to INT_MAX) (default input)
        :param Int transfer: set transfer characteristic (from -1 to INT_MAX) (default input)
        :param Int matrix: set colorspace matrix (from -1 to INT_MAX) (default input)
        :param Int in_range: set input color range (from -1 to 1) (default input)
        :param Int primariesin: set input color primaries (from -1 to INT_MAX) (default input)
        :param Int transferin: set input transfer characteristic (from -1 to INT_MAX) (default input)
        :param Int matrixin: set input colorspace matrix (from -1 to INT_MAX) (default input)
        :param Int chromal: set output chroma location (from -1 to 5) (default input)
        :param Int chromalin: set input chroma location (from -1 to 5) (default input)
        :param Double npl: set nominal peak luminance (from 0 to DBL_MAX) (default nan)
        :param Boolean agamma: allow approximate gamma (default true)
        :param Double param_a: parameter A, which is parameter "b" for bicubic, and the number of filter taps for lanczos (from -DBL_MAX to DBL_MAX) (default nan)
        :param Double param_b: parameter B, which is parameter "c" for bicubic (from -DBL_MAX to DBL_MAX) (default nan)

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
