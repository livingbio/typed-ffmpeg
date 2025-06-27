# NOTE: this file is auto-generated, do not modify
"""Video stream."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from ..common.schema import FFMpegFilterDef
from ..dag.factory import filter_node_factory
from ..dag.nodes import (
    FilterableStream,
    FilterNode,
)
from ..options.framesync import FFMpegFrameSyncOption
from ..options.timeline import FFMpegTimelineOption
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
    Pix_fmt,
    Rational,
    String,
    Video_rate,
)
from ..utils.frozendict import merge

if TYPE_CHECKING:
    from .audio import AudioStream


class VideoStream(FilterableStream):
    """Video stream."""

    def addroi(
        self,
        *,
        x: String = Default("0"),
        y: String = Default("0"),
        w: String = Default("0"),
        h: String = Default("0"),
        qoffset: Rational = Default("-1/10"),
        clear: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Add region of interest to frame.

        Args:
            x: Region distance from left edge of frame. (default "0")
            y: Region distance from top edge of frame. (default "0")
            w: Region width. (default "0")
            h: Region height. (default "0")
            qoffset: Quantisation offset to apply in the region. (from -1 to 1) (default -1/10)
            clear: Remove any existing regions of interest before adding the new one. (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#addroi)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="addroi", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "qoffset": qoffset,
                    "clear": clear,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def alphaextract(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Extract an alpha channel as a grayscale image component.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#alphaextract)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="alphaextract", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def alphamerge(
        self,
        _alpha: VideoStream,
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Copy the luma value of the second input into the alpha channel of the first input.

        Args:
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#alphamerge)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="alphamerge",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _alpha,
            **merge(
                {},
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def amplify(
        self,
        *,
        radius: Int = Default("2"),
        factor: Float = Default("2"),
        threshold: Float = Default("10"),
        tolerance: Float = Default("0"),
        low: Float = Default("65535"),
        high: Float = Default("65535"),
        planes: Flags = Default("7"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Amplify changes between successive video frames.

        Args:
            radius: set radius (from 1 to 63) (default 2)
            factor: set factor (from 0 to 65535) (default 2)
            threshold: set threshold (from 0 to 65535) (default 10)
            tolerance: set tolerance (from 0 to 65535) (default 0)
            low: set low limit for amplification (from 0 to 65535) (default 65535)
            high: set high limit for amplification (from 0 to 65535) (default 65535)
            planes: set what planes to filter (default 7)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#amplify)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="amplify", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "radius": radius,
                    "factor": factor,
                    "threshold": threshold,
                    "tolerance": tolerance,
                    "low": low,
                    "high": high,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def ass(
        self,
        *,
        filename: String = Default(None),
        original_size: Image_size = Default(None),
        fontsdir: String = Default(None),
        alpha: Boolean = Default("false"),
        shaping: Int | Literal["auto", "simple", "complex"] | Default = Default("auto"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Render ASS subtitles onto input video using the libass library.

        Args:
            filename: set the filename of file to read
            original_size: set the size of the original video (used to scale fonts)
            fontsdir: set the directory containing the fonts to read
            alpha: enable processing of alpha channel (default false)
            shaping: set shaping engine (from -1 to 1) (default auto)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ass)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ass", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filename": filename,
                    "original_size": original_size,
                    "fontsdir": fontsdir,
                    "alpha": alpha,
                    "shaping": shaping,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def atadenoise(
        self,
        *,
        _0a: Float = Default("0.02"),
        _0b: Float = Default("0.04"),
        _1a: Float = Default("0.02"),
        _1b: Float = Default("0.04"),
        _2a: Float = Default("0.02"),
        _2b: Float = Default("0.04"),
        s: Int = Default("9"),
        p: Flags = Default("7"),
        a: Int | Literal["p", "s"] | Default = Default("p"),
        _0s: Float = Default("32767"),
        _1s: Float = Default("32767"),
        _2s: Float = Default("32767"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply an Adaptive Temporal Averaging Denoiser.

        Args:
            _0a: set threshold A for 1st plane (from 0 to 0.3) (default 0.02)
            _0b: set threshold B for 1st plane (from 0 to 5) (default 0.04)
            _1a: set threshold A for 2nd plane (from 0 to 0.3) (default 0.02)
            _1b: set threshold B for 2nd plane (from 0 to 5) (default 0.04)
            _2a: set threshold A for 3rd plane (from 0 to 0.3) (default 0.02)
            _2b: set threshold B for 3rd plane (from 0 to 5) (default 0.04)
            s: set how many frames to use (from 5 to 129) (default 9)
            p: set what planes to filter (default 7)
            a: set variant of algorithm (from 0 to 1) (default p)
            _0s: set sigma for 1st plane (from 0 to 32767) (default 32767)
            _1s: set sigma for 2nd plane (from 0 to 32767) (default 32767)
            _2s: set sigma for 3rd plane (from 0 to 32767) (default 32767)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#atadenoise)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="atadenoise", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def avgblur(
        self,
        *,
        sizeX: Int = Default("1"),
        planes: Int = Default("15"),
        sizeY: Int = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Average Blur filter.

        Args:
            sizeX: set horizontal size (from 1 to 1024) (default 1)
            planes: set planes to filter (from 0 to 15) (default 15)
            sizeY: set vertical size (from 0 to 1024) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#avgblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="avgblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sizeX": sizeX,
                    "planes": planes,
                    "sizeY": sizeY,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def avgblur_opencl(
        self,
        *,
        sizeX: Int = Default("1"),
        planes: Int = Default("15"),
        sizeY: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply average blur filter.

        Args:
            sizeX: set horizontal size (from 1 to 1024) (default 1)
            planes: set planes to filter (from 0 to 15) (default 15)
            sizeY: set vertical size (from 0 to 1024) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#avgblur_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="avgblur_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "sizeX": sizeX,
                    "planes": planes,
                    "sizeY": sizeY,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def avgblur_vulkan(
        self,
        *,
        sizeX: Int = Default("3"),
        sizeY: Int = Default("3"),
        planes: Int = Default("15"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply avgblur mask to input video.

        Args:
            sizeX: Set horizontal radius (from 1 to 32) (default 3)
            sizeY: Set vertical radius (from 1 to 32) (default 3)
            planes: Set planes to filter (bitmask) (from 0 to 15) (default 15)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#avgblur_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="avgblur_vulkan",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "sizeX": sizeX,
                    "sizeY": sizeY,
                    "planes": planes,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def backgroundkey(
        self,
        *,
        threshold: Float = Default("0.08"),
        similarity: Float = Default("0.1"),
        blend: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a static background into transparency.

        Args:
            threshold: set the scene change threshold (from 0 to 1) (default 0.08)
            similarity: set the similarity (from 0 to 1) (default 0.1)
            blend: set the blend value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#backgroundkey)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="backgroundkey",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "threshold": threshold,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def bbox(
        self,
        *,
        min_val: Int = Default("16"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute bounding box for each frame.

        Args:
            min_val: set minimum luminance value for bounding box (from 0 to 65535) (default 16)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bbox)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bbox", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "min_val": min_val,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def bench(
        self,
        *,
        action: Int | Literal["start", "stop"] | Default = Default("start"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Benchmark part of a filtergraph.

        Args:
            action: set action (from 0 to 1) (default start)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bench", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "action": action,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def bilateral(
        self,
        *,
        sigmaS: Float = Default("0.1"),
        sigmaR: Float = Default("0.1"),
        planes: Int = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Bilateral filter.

        Args:
            sigmaS: set spatial sigma (from 0 to 512) (default 0.1)
            sigmaR: set range sigma (from 0 to 1) (default 0.1)
            planes: set planes to filter (from 0 to 15) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bilateral)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bilateral", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sigmaS": sigmaS,
                    "sigmaR": sigmaR,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def bitplanenoise(
        self,
        *,
        bitplane: Int = Default("1"),
        filter: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Measure bit plane noise.

        Args:
            bitplane: set bit plane to use for measuring noise (from 1 to 16) (default 1)
            filter: show noisy pixels (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bitplanenoise)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bitplanenoise",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "bitplane": bitplane,
                    "filter": filter,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def blackdetect(
        self,
        *,
        d: Double = Default("2"),
        picture_black_ratio_th: Double = Default("0.98"),
        pixel_black_th: Double = Default("0.1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Detect video intervals that are (almost) black.

        Args:
            d: set minimum detected black duration in seconds (from 0 to DBL_MAX) (default 2)
            picture_black_ratio_th: set the picture black ratio threshold (from 0 to 1) (default 0.98)
            pixel_black_th: set the pixel black threshold (from 0 to 1) (default 0.1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blackdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blackdetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "d": d,
                    "picture_black_ratio_th": picture_black_ratio_th,
                    "pixel_black_th": pixel_black_th,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def blackframe(
        self,
        *,
        amount: Int = Default("98"),
        threshold: Int = Default("32"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Detect frames that are (almost) black.

        Args:
            amount: percentage of the pixels that have to be below the threshold for the frame to be considered black (from 0 to 100) (default 98)
            threshold: threshold below which a pixel value is considered black (from 0 to 255) (default 32)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blackframe)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blackframe", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "amount": amount,
                    "threshold": threshold,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def blend(
        self,
        _bottom: VideoStream,
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
        | Default = Default("-1"),
        c0_expr: String = Default(None),
        c1_expr: String = Default(None),
        c2_expr: String = Default(None),
        c3_expr: String = Default(None),
        all_expr: String = Default(None),
        c0_opacity: Double = Default("1"),
        c1_opacity: Double = Default("1"),
        c2_opacity: Double = Default("1"),
        c3_opacity: Double = Default("1"),
        all_opacity: Double = Default("1"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blend two video frames into each other.

        Args:
            c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
            c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
            c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
            c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
            all_mode: set blend mode for all components (from -1 to 39) (default -1)
            c0_expr: set color component #0 expression
            c1_expr: set color component #1 expression
            c2_expr: set color component #2 expression
            c3_expr: set color component #3 expression
            all_expr: set expression for all color components
            c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
            c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
            c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
            c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
            all_opacity: set opacity for all color components (from 0 to 1) (default 1)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blend)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blend",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _bottom,
            **merge(
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
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def blend_vulkan(
        self,
        _bottom: VideoStream,
        *,
        c0_mode: Int | Literal["normal", "multiply"] | Default = Default("normal"),
        c1_mode: Int | Literal["normal", "multiply"] | Default = Default("normal"),
        c2_mode: Int | Literal["normal", "multiply"] | Default = Default("normal"),
        c3_mode: Int | Literal["normal", "multiply"] | Default = Default("normal"),
        all_mode: Int | Literal["normal", "multiply"] | Default = Default("-1"),
        c0_opacity: Double = Default("1"),
        c1_opacity: Double = Default("1"),
        c2_opacity: Double = Default("1"),
        c3_opacity: Double = Default("1"),
        all_opacity: Double = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blend two video frames in Vulkan.

        Args:
            c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
            c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
            c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
            c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
            all_mode: set blend mode for all components (from -1 to 39) (default -1)
            c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
            c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
            c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
            c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
            all_opacity: set opacity for all color components (from 0 to 1) (default 1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blend_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blend_vulkan",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _bottom,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def blockdetect(
        self,
        *,
        period_min: Int = Default("3"),
        period_max: Int = Default("24"),
        planes: Int = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blockdetect filter.

        Args:
            period_min: Minimum period to search for (from 2 to 32) (default 3)
            period_max: Maximum period to search for (from 2 to 64) (default 24)
            planes: set planes to filter (from 0 to 15) (default 1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blockdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blockdetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "period_min": period_min,
                    "period_max": period_max,
                    "planes": planes,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def blurdetect(
        self,
        *,
        high: Float = Default("0.117647"),
        low: Float = Default("0.0588235"),
        radius: Int = Default("50"),
        block_pct: Int = Default("80"),
        block_width: Int = Default("-1"),
        planes: Int = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blurdetect filter.

        Args:
            high: set high threshold (from 0 to 1) (default 0.117647)
            low: set low threshold (from 0 to 1) (default 0.0588235)
            radius: search radius for maxima detection (from 1 to 100) (default 50)
            block_pct: block pooling threshold when calculating blurriness (from 1 to 100) (default 80)
            block_width: block size for block-based abbreviation of blurriness (from -1 to INT_MAX) (default -1)
            planes: set planes to filter (from 0 to 15) (default 1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#blurdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="blurdetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "high": high,
                    "low": low,
                    "radius": radius,
                    "block_pct": block_pct,
                    "block_width": block_width,
                    "planes": planes,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def boxblur(
        self,
        *,
        luma_radius: String = Default("2"),
        luma_power: Int = Default("2"),
        chroma_radius: String = Default(None),
        chroma_power: Int = Default("-1"),
        alpha_radius: String = Default(None),
        alpha_power: Int = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blur the input.

        Args:
            luma_radius: Radius of the luma blurring box (default "2")
            luma_power: How many times should the boxblur be applied to luma (from 0 to INT_MAX) (default 2)
            chroma_radius: Radius of the chroma blurring box
            chroma_power: How many times should the boxblur be applied to chroma (from -1 to INT_MAX) (default -1)
            alpha_radius: Radius of the alpha blurring box
            alpha_power: How many times should the boxblur be applied to alpha (from -1 to INT_MAX) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#boxblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="boxblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "luma_radius": luma_radius,
                    "luma_power": luma_power,
                    "chroma_radius": chroma_radius,
                    "chroma_power": chroma_power,
                    "alpha_radius": alpha_radius,
                    "alpha_power": alpha_power,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def boxblur_opencl(
        self,
        *,
        luma_radius: String = Default("2"),
        luma_power: Int = Default("2"),
        chroma_radius: String = Default(None),
        chroma_power: Int = Default("-1"),
        alpha_radius: String = Default(None),
        alpha_power: Int = Default("-1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply boxblur filter to input video.

        Args:
            luma_radius: Radius of the luma blurring box (default "2")
            luma_power: How many times should the boxblur be applied to luma (from 0 to INT_MAX) (default 2)
            chroma_radius: Radius of the chroma blurring box
            chroma_power: How many times should the boxblur be applied to chroma (from -1 to INT_MAX) (default -1)
            alpha_radius: Radius of the alpha blurring box
            alpha_power: How many times should the boxblur be applied to alpha (from -1 to INT_MAX) (default -1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#boxblur_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="boxblur_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "luma_radius": luma_radius,
                    "luma_power": luma_power,
                    "chroma_radius": chroma_radius,
                    "chroma_power": chroma_power,
                    "alpha_radius": alpha_radius,
                    "alpha_power": alpha_power,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def bwdif(
        self,
        *,
        mode: Int | Literal["send_frame", "send_field"] | Default = Default(
            "send_field"
        ),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deinterlace the input image.

        Args:
            mode: specify the interlacing mode (from 0 to 1) (default send_field)
            parity: specify the assumed picture field parity (from -1 to 1) (default auto)
            deint: specify which frames to deinterlace (from 0 to 1) (default all)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bwdif)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bwdif", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "parity": parity,
                    "deint": deint,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def bwdif_vulkan(
        self,
        *,
        mode: Int
        | Literal[
            "send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"
        ]
        | Default = Default("send_frame"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deinterlace Vulkan frames via bwdif.

        Args:
            mode: specify the interlacing mode (from 0 to 3) (default send_frame)
            parity: specify the assumed picture field parity (from -1 to 1) (default auto)
            deint: specify which frames to deinterlace (from 0 to 1) (default all)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#bwdif_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="bwdif_vulkan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "parity": parity,
                    "deint": deint,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def cas(
        self,
        *,
        strength: Float = Default("0"),
        planes: Flags = Default("7"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Contrast Adaptive Sharpen.

        Args:
            strength: set the sharpening strength (from 0 to 1) (default 0)
            planes: set what planes to filter (default 7)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#cas)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="cas", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "strength": strength,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def ccrepack(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Repack CEA-708 closed caption metadata.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ccrepack)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ccrepack", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def chromaber_vulkan(
        self,
        *,
        dist_x: Float = Default("0"),
        dist_y: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Offset chroma of input video (chromatic aberration).

        Args:
            dist_x: Set horizontal distortion amount (from -10 to 10) (default 0)
            dist_y: Set vertical distortion amount (from -10 to 10) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chromaber_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chromaber_vulkan",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "dist_x": dist_x,
                    "dist_y": dist_y,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def chromahold(
        self,
        *,
        color: Color = Default("black"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        yuv: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain color range into gray.

        Args:
            color: set the chromahold key color (default "black")
            similarity: set the chromahold similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the chromahold blend value (from 0 to 1) (default 0)
            yuv: color parameter is in yuv instead of rgb (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chromahold)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chromahold", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "color": color,
                    "similarity": similarity,
                    "blend": blend,
                    "yuv": yuv,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def chromakey(
        self,
        *,
        color: Color = Default("black"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        yuv: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain color into transparency. Operates on YUV colors.

        Args:
            color: set the chromakey key color (default "black")
            similarity: set the chromakey similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the chromakey key blend value (from 0 to 1) (default 0)
            yuv: color parameter is in yuv instead of rgb (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chromakey)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chromakey", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "color": color,
                    "similarity": similarity,
                    "blend": blend,
                    "yuv": yuv,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def chromanr(
        self,
        *,
        thres: Float = Default("30"),
        sizew: Int = Default("5"),
        sizeh: Int = Default("5"),
        stepw: Int = Default("1"),
        steph: Int = Default("1"),
        threy: Float = Default("200"),
        threu: Float = Default("200"),
        threv: Float = Default("200"),
        distance: Int | Literal["manhattan", "euclidean"] | Default = Default(
            "manhattan"
        ),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Reduce chrominance noise.

        Args:
            thres: set y+u+v threshold (from 1 to 200) (default 30)
            sizew: set horizontal patch size (from 1 to 100) (default 5)
            sizeh: set vertical patch size (from 1 to 100) (default 5)
            stepw: set horizontal step (from 1 to 50) (default 1)
            steph: set vertical step (from 1 to 50) (default 1)
            threy: set y threshold (from 1 to 200) (default 200)
            threu: set u threshold (from 1 to 200) (default 200)
            threv: set v threshold (from 1 to 200) (default 200)
            distance: set distance type (from 0 to 1) (default manhattan)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chromanr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chromanr", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def chromashift(
        self,
        *,
        cbh: Int = Default("0"),
        cbv: Int = Default("0"),
        crh: Int = Default("0"),
        crv: Int = Default("0"),
        edge: Int | Literal["smear", "wrap"] | Default = Default("smear"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shift chroma.

        Args:
            cbh: shift chroma-blue horizontally (from -255 to 255) (default 0)
            cbv: shift chroma-blue vertically (from -255 to 255) (default 0)
            crh: shift chroma-red horizontally (from -255 to 255) (default 0)
            crv: shift chroma-red vertically (from -255 to 255) (default 0)
            edge: set edge operation (from 0 to 1) (default smear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#chromashift)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="chromashift", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "cbh": cbh,
                    "cbv": cbv,
                    "crh": crh,
                    "crv": crv,
                    "edge": edge,
                },
                extra_options,
                timeline_options,
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
        size: Int = Default("512"),
        intensity: Float = Default("0.001"),
        contrast: Float = Default("0.75"),
        corrgamma: Boolean = Default("true"),
        showwhite: Boolean = Default("false"),
        gamma: Double = Default("2.6"),
        fill: Boolean = Default("true"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Video CIE scope.

        Args:
            system: set color system (from 0 to 9) (default hdtv)
            cie: set cie system (from 0 to 2) (default xyy)
            gamuts: set what gamuts to draw (default 0)
            size: set ciescope size (from 256 to 8192) (default 512)
            intensity: set ciescope intensity (from 0 to 1) (default 0.001)
            contrast: (from 0 to 1) (default 0.75)
            corrgamma: (default true)
            showwhite: (default false)
            gamma: (from 0.1 to 6) (default 2.6)
            fill: fill with CIE colors (default true)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ciescope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ciescope", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def codecview(
        self,
        *,
        mv: Flags | Literal["pf", "bf", "bb"] | Default = Default("0"),
        qp: Boolean = Default("false"),
        mv_type: Flags | Literal["fp", "bp"] | Default = Default("0"),
        frame_type: Flags | Literal["if", "pf", "bf"] | Default = Default("0"),
        block: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Visualize information about some codecs.

        Args:
            mv: set motion vectors to visualize (default 0)
            qp: (default false)
            mv_type: set motion vectors type (default 0)
            frame_type: set frame types to visualize motion vectors of (default 0)
            block: set block partitioning structure to visualize (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#codecview)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="codecview", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mv": mv,
                    "qp": qp,
                    "mv_type": mv_type,
                    "frame_type": frame_type,
                    "block": block,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorbalance(
        self,
        *,
        rs: Float = Default("0"),
        gs: Float = Default("0"),
        bs: Float = Default("0"),
        rm: Float = Default("0"),
        gm: Float = Default("0"),
        bm: Float = Default("0"),
        rh: Float = Default("0"),
        gh: Float = Default("0"),
        bh: Float = Default("0"),
        pl: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust the color balance.

        Args:
            rs: set red shadows (from -1 to 1) (default 0)
            gs: set green shadows (from -1 to 1) (default 0)
            bs: set blue shadows (from -1 to 1) (default 0)
            rm: set red midtones (from -1 to 1) (default 0)
            gm: set green midtones (from -1 to 1) (default 0)
            bm: set blue midtones (from -1 to 1) (default 0)
            rh: set red highlights (from -1 to 1) (default 0)
            gh: set green highlights (from -1 to 1) (default 0)
            bh: set blue highlights (from -1 to 1) (default 0)
            pl: preserve lightness (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorbalance)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorbalance", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorchannelmixer(
        self,
        *,
        rr: Double = Default("1"),
        rg: Double = Default("0"),
        rb: Double = Default("0"),
        ra: Double = Default("0"),
        gr: Double = Default("0"),
        gg: Double = Default("1"),
        gb: Double = Default("0"),
        ga: Double = Default("0"),
        br: Double = Default("0"),
        bg: Double = Default("0"),
        bb: Double = Default("1"),
        ba: Double = Default("0"),
        ar: Double = Default("0"),
        ag: Double = Default("0"),
        ab: Double = Default("0"),
        aa: Double = Default("1"),
        pc: Int
        | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"]
        | Default = Default("none"),
        pa: Double = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust colors by mixing color channels.

        Args:
            rr: set the red gain for the red channel (from -2 to 2) (default 1)
            rg: set the green gain for the red channel (from -2 to 2) (default 0)
            rb: set the blue gain for the red channel (from -2 to 2) (default 0)
            ra: set the alpha gain for the red channel (from -2 to 2) (default 0)
            gr: set the red gain for the green channel (from -2 to 2) (default 0)
            gg: set the green gain for the green channel (from -2 to 2) (default 1)
            gb: set the blue gain for the green channel (from -2 to 2) (default 0)
            ga: set the alpha gain for the green channel (from -2 to 2) (default 0)
            br: set the red gain for the blue channel (from -2 to 2) (default 0)
            bg: set the green gain for the blue channel (from -2 to 2) (default 0)
            bb: set the blue gain for the blue channel (from -2 to 2) (default 1)
            ba: set the alpha gain for the blue channel (from -2 to 2) (default 0)
            ar: set the red gain for the alpha channel (from -2 to 2) (default 0)
            ag: set the green gain for the alpha channel (from -2 to 2) (default 0)
            ab: set the blue gain for the alpha channel (from -2 to 2) (default 0)
            aa: set the alpha gain for the alpha channel (from -2 to 2) (default 1)
            pc: set the preserve color mode (from 0 to 6) (default none)
            pa: set the preserve color amount (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorchannelmixer",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorcontrast(
        self,
        *,
        rc: Float = Default("0"),
        gm: Float = Default("0"),
        by: Float = Default("0"),
        rcw: Float = Default("0"),
        gmw: Float = Default("0"),
        byw: Float = Default("0"),
        pl: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust color contrast between RGB components.

        Args:
            rc: set the red-cyan contrast (from -1 to 1) (default 0)
            gm: set the green-magenta contrast (from -1 to 1) (default 0)
            by: set the blue-yellow contrast (from -1 to 1) (default 0)
            rcw: set the red-cyan weight (from 0 to 1) (default 0)
            gmw: set the green-magenta weight (from 0 to 1) (default 0)
            byw: set the blue-yellow weight (from 0 to 1) (default 0)
            pl: set the amount of preserving lightness (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorcontrast)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorcontrast",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "rc": rc,
                    "gm": gm,
                    "by": by,
                    "rcw": rcw,
                    "gmw": gmw,
                    "byw": byw,
                    "pl": pl,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorcorrect(
        self,
        *,
        rl: Float = Default("0"),
        bl: Float = Default("0"),
        rh: Float = Default("0"),
        bh: Float = Default("0"),
        saturation: Float = Default("1"),
        analyze: Int
        | Literal["manual", "average", "minmax", "median"]
        | Default = Default("manual"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust color white balance selectively for blacks and whites.

        Args:
            rl: set the red shadow spot (from -1 to 1) (default 0)
            bl: set the blue shadow spot (from -1 to 1) (default 0)
            rh: set the red highlight spot (from -1 to 1) (default 0)
            bh: set the blue highlight spot (from -1 to 1) (default 0)
            saturation: set the amount of saturation (from -3 to 3) (default 1)
            analyze: set the analyze mode (from 0 to 3) (default manual)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorcorrect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorcorrect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "rl": rl,
                    "bl": bl,
                    "rh": rh,
                    "bh": bh,
                    "saturation": saturation,
                    "analyze": analyze,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorhold(
        self,
        *,
        color: Color = Default("black"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain color range into gray. Operates on RGB colors.

        Args:
            color: set the colorhold key color (default "black")
            similarity: set the colorhold similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the colorhold blend value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorhold)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorhold", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "color": color,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorize(
        self,
        *,
        hue: Float = Default("0"),
        saturation: Float = Default("0.5"),
        lightness: Float = Default("0.5"),
        mix: Float = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Overlay a solid color on the video stream.

        Args:
            hue: set the hue (from 0 to 360) (default 0)
            saturation: set the saturation (from 0 to 1) (default 0.5)
            lightness: set the lightness (from 0 to 1) (default 0.5)
            mix: set the mix of source lightness (from 0 to 1) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorize)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorize", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "hue": hue,
                    "saturation": saturation,
                    "lightness": lightness,
                    "mix": mix,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorkey(
        self,
        *,
        color: Color = Default("black"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain color into transparency. Operates on RGB colors.

        Args:
            color: set the colorkey key color (default "black")
            similarity: set the colorkey similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the colorkey key blend value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorkey)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorkey", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "color": color,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorkey_opencl(
        self,
        *,
        color: Color = Default("black"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain color into transparency. Operates on RGB colors.

        Args:
            color: set the colorkey key color (default "black")
            similarity: set the colorkey similarity value (from 0.01 to 1) (default 0.01)
            blend: set the colorkey key blend value (from 0 to 1) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorkey_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorkey_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "color": color,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def colorlevels(
        self,
        *,
        rimin: Double = Default("0"),
        gimin: Double = Default("0"),
        bimin: Double = Default("0"),
        aimin: Double = Default("0"),
        rimax: Double = Default("1"),
        gimax: Double = Default("1"),
        bimax: Double = Default("1"),
        aimax: Double = Default("1"),
        romin: Double = Default("0"),
        gomin: Double = Default("0"),
        bomin: Double = Default("0"),
        aomin: Double = Default("0"),
        romax: Double = Default("1"),
        gomax: Double = Default("1"),
        bomax: Double = Default("1"),
        aomax: Double = Default("1"),
        preserve: Int
        | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"]
        | Default = Default("none"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust the color levels.

        Args:
            rimin: set input red black point (from -1 to 1) (default 0)
            gimin: set input green black point (from -1 to 1) (default 0)
            bimin: set input blue black point (from -1 to 1) (default 0)
            aimin: set input alpha black point (from -1 to 1) (default 0)
            rimax: set input red white point (from -1 to 1) (default 1)
            gimax: set input green white point (from -1 to 1) (default 1)
            bimax: set input blue white point (from -1 to 1) (default 1)
            aimax: set input alpha white point (from -1 to 1) (default 1)
            romin: set output red black point (from 0 to 1) (default 0)
            gomin: set output green black point (from 0 to 1) (default 0)
            bomin: set output blue black point (from 0 to 1) (default 0)
            aomin: set output alpha black point (from 0 to 1) (default 0)
            romax: set output red white point (from 0 to 1) (default 1)
            gomax: set output green white point (from 0 to 1) (default 1)
            bomax: set output blue white point (from 0 to 1) (default 1)
            aomax: set output alpha white point (from 0 to 1) (default 1)
            preserve: set preserve color mode (from 0 to 6) (default none)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorlevels)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorlevels", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colormap(
        self,
        _source: VideoStream,
        _target: VideoStream,
        *,
        patch_size: Image_size = Default("64x64"),
        nb_patches: Int = Default("0"),
        type: Int | Literal["relative", "absolute"] | Default = Default("absolute"),
        kernel: Int | Literal["euclidean", "weuclidean"] | Default = Default(
            "euclidean"
        ),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply custom Color Maps to video stream.

        Args:
            patch_size: set patch size (default "64x64")
            nb_patches: set number of patches (from 0 to 64) (default 0)
            type: set the target type used (from 0 to 1) (default absolute)
            kernel: set the kernel used for measuring color difference (from 0 to 1) (default euclidean)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colormap)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colormap",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _source,
            _target,
            **merge(
                {
                    "patch_size": patch_size,
                    "nb_patches": nb_patches,
                    "type": type,
                    "kernel": kernel,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colormatrix(
        self,
        *,
        src: Int
        | Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | Default = Default("-1"),
        dst: Int
        | Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | Default = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert color matrix.

        Args:
            src: set source color matrix (from -1 to 4) (default -1)
            dst: set destination color matrix (from -1 to 4) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colormatrix)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colormatrix", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "src": src,
                    "dst": dst,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colorspace(
        self,
        *,
        all: Int
        | Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | Default = Default("0"),
        space: Int
        | Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | Default = Default("2"),
        range: Int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("0"),
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
            "jedec-p22",
            "ebu3213",
        ]
        | Default = Default("2"),
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
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | Default = Default("2"),
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
        | Default = Default("-1"),
        fast: Boolean = Default("false"),
        dither: Int | Literal["none", "fsb"] | Default = Default("none"),
        wpadapt: Int | Literal["bradford", "vonkries", "identity"] | Default = Default(
            "bradford"
        ),
        iall: Int
        | Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | Default = Default("0"),
        ispace: Int
        | Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | Default = Default("2"),
        irange: Int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("0"),
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
            "jedec-p22",
            "ebu3213",
        ]
        | Default = Default("2"),
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
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | Default = Default("2"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert between colorspaces.

        Args:
            all: Set all color properties together (from 0 to 8) (default 0)
            space: Output colorspace (from 0 to 14) (default 2)
            range: Output color range (from 0 to 2) (default 0)
            primaries: Output color primaries (from 0 to 22) (default 2)
            trc: Output transfer characteristics (from 0 to 18) (default 2)
            format: Output pixel format (from -1 to 162) (default -1)
            fast: Ignore primary chromaticity and gamma correction (default false)
            dither: Dithering mode (from 0 to 1) (default none)
            wpadapt: Whitepoint adaptation method (from 0 to 2) (default bradford)
            iall: Set all input color properties together (from 0 to 8) (default 0)
            ispace: Input colorspace (from 0 to 22) (default 2)
            irange: Input color range (from 0 to 2) (default 0)
            iprimaries: Input color primaries (from 0 to 22) (default 2)
            itrc: Input transfer characteristics (from 0 to 18) (default 2)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colorspace)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colorspace", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def colortemperature(
        self,
        *,
        temperature: Float = Default("6500"),
        mix: Float = Default("1"),
        pl: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust color temperature of video.

        Args:
            temperature: set the temperature in Kelvin (from 1000 to 40000) (default 6500)
            mix: set the mix with filtered output (from 0 to 1) (default 1)
            pl: set the amount of preserving lightness (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#colortemperature)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="colortemperature",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "temperature": temperature,
                    "mix": mix,
                    "pl": pl,
                },
                extra_options,
                timeline_options,
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
        _0rdiv: Float = Default("0"),
        _1rdiv: Float = Default("0"),
        _2rdiv: Float = Default("0"),
        _3rdiv: Float = Default("0"),
        _0bias: Float = Default("0"),
        _1bias: Float = Default("0"),
        _2bias: Float = Default("0"),
        _3bias: Float = Default("0"),
        _0mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _1mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _2mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        _3mode: Int | Literal["square", "row", "column"] | Default = Default("square"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply convolution filter.

        Args:
            _0m: set matrix for 1st plane (default "0 0 0 0 1 0 0 0 0")
            _1m: set matrix for 2nd plane (default "0 0 0 0 1 0 0 0 0")
            _2m: set matrix for 3rd plane (default "0 0 0 0 1 0 0 0 0")
            _3m: set matrix for 4th plane (default "0 0 0 0 1 0 0 0 0")
            _0rdiv: set rdiv for 1st plane (from 0 to INT_MAX) (default 0)
            _1rdiv: set rdiv for 2nd plane (from 0 to INT_MAX) (default 0)
            _2rdiv: set rdiv for 3rd plane (from 0 to INT_MAX) (default 0)
            _3rdiv: set rdiv for 4th plane (from 0 to INT_MAX) (default 0)
            _0bias: set bias for 1st plane (from 0 to INT_MAX) (default 0)
            _1bias: set bias for 2nd plane (from 0 to INT_MAX) (default 0)
            _2bias: set bias for 3rd plane (from 0 to INT_MAX) (default 0)
            _3bias: set bias for 4th plane (from 0 to INT_MAX) (default 0)
            _0mode: set matrix mode for 1st plane (from 0 to 2) (default square)
            _1mode: set matrix mode for 2nd plane (from 0 to 2) (default square)
            _2mode: set matrix mode for 3rd plane (from 0 to 2) (default square)
            _3mode: set matrix mode for 4th plane (from 0 to 2) (default square)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#convolution)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="convolution", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def convolution_opencl(
        self,
        *,
        _0m: String = Default("0 0 0 0 1 0 0 0 0"),
        _2m: String = Default("0 0 0 0 1 0 0 0 0"),
        _3m: String = Default("0 0 0 0 1 0 0 0 0"),
        _0rdiv: Float = Default("1"),
        _1rdiv: Float = Default("1"),
        _2rdiv: Float = Default("1"),
        _3rdiv: Float = Default("1"),
        _0bias: Float = Default("0"),
        _1bias: Float = Default("0"),
        _2bias: Float = Default("0"),
        _3bias: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply convolution mask to input video.

        Args:
            _0m: set matrix for 2nd plane (default "0 0 0 0 1 0 0 0 0")
            _2m: set matrix for 3rd plane (default "0 0 0 0 1 0 0 0 0")
            _3m: set matrix for 4th plane (default "0 0 0 0 1 0 0 0 0")
            _0rdiv: set rdiv for 1nd plane (from 0 to INT_MAX) (default 1)
            _1rdiv: set rdiv for 2nd plane (from 0 to INT_MAX) (default 1)
            _2rdiv: set rdiv for 3rd plane (from 0 to INT_MAX) (default 1)
            _3rdiv: set rdiv for 4th plane (from 0 to INT_MAX) (default 1)
            _0bias: set bias for 1st plane (from 0 to INT_MAX) (default 0)
            _1bias: set bias for 2nd plane (from 0 to INT_MAX) (default 0)
            _2bias: set bias for 3rd plane (from 0 to INT_MAX) (default 0)
            _3bias: set bias for 4th plane (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#convolution_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="convolution_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "0m": _0m,
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def convolve(
        self,
        _impulse: VideoStream,
        *,
        planes: Int = Default("7"),
        impulse: Int | Literal["first", "all"] | Default = Default("all"),
        noise: Float = Default("1e-07"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convolve first video stream with second video stream.

        Args:
            planes: set planes to convolve (from 0 to 15) (default 7)
            impulse: when to process impulses (from 0 to 1) (default all)
            noise: set noise (from 0 to 1) (default 1e-07)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#convolve)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="convolve",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _impulse,
            **merge(
                {
                    "planes": planes,
                    "impulse": impulse,
                    "noise": noise,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def copy(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Copy the input video unchanged to the output.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#copy)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="copy", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def corr(
        self,
        _reference: VideoStream,
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the correlation between two video streams.

        Args:
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#corr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="corr", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _reference,
            **merge(
                {},
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def cover_rect(
        self,
        *,
        cover: String = Default(None),
        mode: Int | Literal["cover", "blur"] | Default = Default("blur"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Find and cover a user specified object.

        Args:
            cover: cover bitmap filename
            mode: set removal mode (from 0 to 1) (default blur)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#cover_005frect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="cover_rect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "cover": cover,
                    "mode": mode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def crop(
        self,
        *,
        out_w: String = Default("iw"),
        out_h: String = Default("ih"),
        x: String = Default("(in_w-out_w)/2"),
        y: String = Default("(in_h-out_h)/2"),
        keep_aspect: Boolean = Default("false"),
        exact: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Crop the input video.

        Args:
            out_w: set the width crop area expression (default "iw")
            out_h: set the height crop area expression (default "ih")
            x: set the x crop area expression (default "(in_w-out_w)/2")
            y: set the y crop area expression (default "(in_h-out_h)/2")
            keep_aspect: keep aspect ratio (default false)
            exact: do exact cropping (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#crop)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="crop", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "out_w": out_w,
                    "out_h": out_h,
                    "x": x,
                    "y": y,
                    "keep_aspect": keep_aspect,
                    "exact": exact,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def cropdetect(
        self,
        *,
        limit: Float = Default("0.0941176"),
        round: Int = Default("16"),
        reset: Int = Default("0"),
        skip: Int = Default("2"),
        reset_count: Int = Default("0"),
        max_outliers: Int = Default("0"),
        mode: Int | Literal["black", "mvedges"] | Default = Default("black"),
        high: Float = Default("0.0980392"),
        low: Float = Default("0.0588235"),
        mv_threshold: Int = Default("8"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Auto-detect crop size.

        Args:
            limit: Threshold below which the pixel is considered black (from 0 to 65535) (default 0.0941176)
            round: Value by which the width/height should be divisible (from 0 to INT_MAX) (default 16)
            reset: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
            skip: Number of initial frames to skip (from 0 to INT_MAX) (default 2)
            reset_count: Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
            max_outliers: Threshold count of outliers (from 0 to INT_MAX) (default 0)
            mode: set mode (from 0 to 1) (default black)
            high: Set high threshold for edge detection (from 0 to 1) (default 0.0980392)
            low: Set low threshold for edge detection (from 0 to 1) (default 0.0588235)
            mv_threshold: motion vector threshold when estimating video window size (from 0 to 100) (default 8)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#cropdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="cropdetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def cue(
        self,
        *,
        cue: Int64 = Default("0"),
        preroll: Duration = Default("0"),
        buffer: Duration = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Delay filtering to match a cue.

        Args:
            cue: cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
            preroll: preroll duration in seconds (default 0)
            buffer: buffer duration in seconds (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#cue)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="cue", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "cue": cue,
                    "preroll": preroll,
                    "buffer": buffer,
                },
                extra_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust components curves.

        Args:
            preset: select a color curves preset (from 0 to 10) (default none)
            master: set master points coordinates
            red: set red points coordinates
            green: set green points coordinates
            blue: set blue points coordinates
            all: set points coordinates for all components
            psfile: set Photoshop curves file name
            plot: save Gnuplot script of the curves in specified file
            interp: specify the kind of interpolation (from 0 to 1) (default natural)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#curves)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="curves", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def datascope(
        self,
        *,
        size: Image_size = Default("hd720"),
        x: Int = Default("0"),
        y: Int = Default("0"),
        mode: Int | Literal["mono", "color", "color2"] | Default = Default("mono"),
        axis: Boolean = Default("false"),
        opacity: Float = Default("0.75"),
        format: Int | Literal["hex", "dec"] | Default = Default("hex"),
        components: Int = Default("15"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Video data analysis.

        Args:
            size: set output size (default "hd720")
            x: set x offset (from 0 to INT_MAX) (default 0)
            y: set y offset (from 0 to INT_MAX) (default 0)
            mode: set scope mode (from 0 to 2) (default mono)
            axis: draw column/row numbers (default false)
            opacity: set background opacity (from 0 to 1) (default 0.75)
            format: set display number format (from 0 to 1) (default hex)
            components: set components to display (from 1 to 15) (default 15)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#datascope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="datascope", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "size": size,
                    "x": x,
                    "y": y,
                    "mode": mode,
                    "axis": axis,
                    "opacity": opacity,
                    "format": format,
                    "components": components,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def dblur(
        self,
        *,
        angle: Float = Default("45"),
        radius: Float = Default("5"),
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Directional Blur filter.

        Args:
            angle: set angle (from 0 to 360) (default 45)
            radius: set radius (from 0 to 8192) (default 5)
            planes: set planes to filter (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "angle": angle,
                    "radius": radius,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def dctdnoiz(
        self,
        *,
        sigma: Float = Default("0"),
        overlap: Int = Default("-1"),
        expr: String = Default(None),
        n: Int = Default("3"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Denoise frames using 2D DCT.

        Args:
            sigma: set noise sigma constant (from 0 to 999) (default 0)
            overlap: set number of block overlapping pixels (from -1 to 15) (default -1)
            expr: set coefficient factor expression
            n: set the block size, expressed in bits (from 3 to 4) (default 3)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dctdnoiz)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dctdnoiz", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sigma": sigma,
                    "overlap": overlap,
                    "expr": expr,
                    "n": n,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deband(
        self,
        *,
        _1thr: Float = Default("0.02"),
        _2thr: Float = Default("0.02"),
        _3thr: Float = Default("0.02"),
        _4thr: Float = Default("0.02"),
        range: Int = Default("16"),
        direction: Float = Default("6.28319"),
        blur: Boolean = Default("true"),
        coupling: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Debands video.

        Args:
            _1thr: set 1st plane threshold (from 3e-05 to 0.5) (default 0.02)
            _2thr: set 2nd plane threshold (from 3e-05 to 0.5) (default 0.02)
            _3thr: set 3rd plane threshold (from 3e-05 to 0.5) (default 0.02)
            _4thr: set 4th plane threshold (from 3e-05 to 0.5) (default 0.02)
            range: set range (from INT_MIN to INT_MAX) (default 16)
            direction: set direction (from -6.28319 to 6.28319) (default 6.28319)
            blur: set blur (default true)
            coupling: set plane coupling (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deband)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deband", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "1thr": _1thr,
                    "2thr": _2thr,
                    "3thr": _3thr,
                    "4thr": _4thr,
                    "range": range,
                    "direction": direction,
                    "blur": blur,
                    "coupling": coupling,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deblock(
        self,
        *,
        filter: Int | Literal["weak", "strong"] | Default = Default("strong"),
        block: Int = Default("8"),
        alpha: Float = Default("0.098"),
        beta: Float = Default("0.05"),
        gamma: Float = Default("0.05"),
        delta: Float = Default("0.05"),
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deblock video.

        Args:
            filter: set type of filter (from 0 to 1) (default strong)
            block: set size of block (from 4 to 512) (default 8)
            alpha: set 1st detection threshold (from 0 to 1) (default 0.098)
            beta: set 2nd detection threshold (from 0 to 1) (default 0.05)
            gamma: set 3rd detection threshold (from 0 to 1) (default 0.05)
            delta: set 4th detection threshold (from 0 to 1) (default 0.05)
            planes: set planes to filter (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deblock)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deblock", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filter": filter,
                    "block": block,
                    "alpha": alpha,
                    "beta": beta,
                    "gamma": gamma,
                    "delta": delta,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deconvolve(
        self,
        _impulse: VideoStream,
        *,
        planes: Int = Default("7"),
        impulse: Int | Literal["first", "all"] | Default = Default("all"),
        noise: Float = Default("1e-07"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deconvolve first video stream with second video stream.

        Args:
            planes: set planes to deconvolve (from 0 to 15) (default 7)
            impulse: when to process impulses (from 0 to 1) (default all)
            noise: set noise (from 0 to 1) (default 1e-07)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deconvolve)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deconvolve",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _impulse,
            **merge(
                {
                    "planes": planes,
                    "impulse": impulse,
                    "noise": noise,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def dedot(
        self,
        *,
        m: Flags | Literal["dotcrawl", "rainbows"] | Default = Default(
            "dotcrawl+rainbows"
        ),
        lt: Float = Default("0.079"),
        tl: Float = Default("0.079"),
        tc: Float = Default("0.058"),
        ct: Float = Default("0.019"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Reduce cross-luminance and cross-color.

        Args:
            m: set filtering mode (default dotcrawl+rainbows)
            lt: set spatial luma threshold (from 0 to 1) (default 0.079)
            tl: set tolerance for temporal luma (from 0 to 1) (default 0.079)
            tc: set tolerance for chroma temporal variation (from 0 to 1) (default 0.058)
            ct: set temporal chroma threshold (from 0 to 1) (default 0.019)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dedot)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dedot", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "m": m,
                    "lt": lt,
                    "tl": tl,
                    "tc": tc,
                    "ct": ct,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deflate(
        self,
        *,
        threshold0: Int = Default("65535"),
        threshold1: Int = Default("65535"),
        threshold2: Int = Default("65535"),
        threshold3: Int = Default("65535"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply deflate effect.

        Args:
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deflate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deflate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deflicker(
        self,
        *,
        size: Int = Default("5"),
        mode: Int
        | Literal["am", "gm", "hm", "qm", "cm", "pm", "median"]
        | Default = Default("am"),
        bypass: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove temporal frame luminance variations.

        Args:
            size: set how many frames to use (from 2 to 129) (default 5)
            mode: set how to smooth luminance (from 0 to 6) (default am)
            bypass: leave frames unchanged (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deflicker)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deflicker", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "size": size,
                    "mode": mode,
                    "bypass": bypass,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def dejudder(
        self,
        *,
        cycle: Int = Default("4"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove judder produced by pullup.

        Args:
            cycle: set the length of the cycle to use for dejuddering (from 2 to 240) (default 4)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dejudder)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dejudder", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "cycle": cycle,
                },
                extra_options,
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
        show: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove logo from input video.

        Args:
            x: set logo x position (default "-1")
            y: set logo y position (default "-1")
            w: set logo width (default "-1")
            h: set logo height (default "-1")
            show: show delogo area (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#delogo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="delogo", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "show": show,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def derain(
        self,
        *,
        filter_type: Int | Literal["derain", "dehaze"] | Default = Default("derain"),
        dnn_backend: Int = Default("1"),
        model: String = Default(None),
        input: String = Default("x"),
        output: String = Default("y"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply derain filter to the input.

        Args:
            filter_type: filter type(derain/dehaze) (from 0 to 1) (default derain)
            dnn_backend: DNN backend (from 0 to 1) (default 1)
            model: path to model file
            input: input name of the model (default "x")
            output: output name of the model (default "y")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#derain)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="derain", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filter_type": filter_type,
                    "dnn_backend": dnn_backend,
                    "model": model,
                    "input": input,
                    "output": output,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def deshake(
        self,
        *,
        x: Int = Default("-1"),
        y: Int = Default("-1"),
        w: Int = Default("-1"),
        h: Int = Default("-1"),
        rx: Int = Default("16"),
        ry: Int = Default("16"),
        edge: Int | Literal["blank", "original", "clamp", "mirror"] | Default = Default(
            "mirror"
        ),
        blocksize: Int = Default("8"),
        contrast: Int = Default("125"),
        search: Int | Literal["exhaustive", "less"] | Default = Default("exhaustive"),
        filename: String = Default(None),
        opencl: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Stabilize shaky video.

        Args:
            x: set x for the rectangular search area (from -1 to INT_MAX) (default -1)
            y: set y for the rectangular search area (from -1 to INT_MAX) (default -1)
            w: set width for the rectangular search area (from -1 to INT_MAX) (default -1)
            h: set height for the rectangular search area (from -1 to INT_MAX) (default -1)
            rx: set x for the rectangular search area (from 0 to 64) (default 16)
            ry: set y for the rectangular search area (from 0 to 64) (default 16)
            edge: set edge mode (from 0 to 3) (default mirror)
            blocksize: set motion search blocksize (from 4 to 128) (default 8)
            contrast: set contrast threshold for blocks (from 1 to 255) (default 125)
            search: set search strategy (from 0 to 1) (default exhaustive)
            filename: set motion search detailed log file name
            opencl: ignored (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deshake)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deshake", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def deshake_opencl(
        self,
        *,
        tripod: Boolean = Default("false"),
        debug: Boolean = Default("false"),
        adaptive_crop: Boolean = Default("true"),
        refine_features: Boolean = Default("true"),
        smooth_strength: Float = Default("0"),
        smooth_window_multiplier: Float = Default("2"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Feature-point based video stabilization filter.

        Args:
            tripod: simulates a tripod by preventing any camera movement whatsoever from the original frame (default false)
            debug: turn on additional debugging information (default false)
            adaptive_crop: attempt to subtly crop borders to reduce mirrored content (default true)
            refine_features: refine feature point locations at a sub-pixel level (default true)
            smooth_strength: smoothing strength (0 attempts to adaptively determine optimal strength) (from 0 to 1) (default 0)
            smooth_window_multiplier: multiplier for number of frames to buffer for motion data (from 0.1 to 10) (default 2)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#deshake_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="deshake_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "tripod": tripod,
                    "debug": debug,
                    "adaptive_crop": adaptive_crop,
                    "refine_features": refine_features,
                    "smooth_strength": smooth_strength,
                    "smooth_window_multiplier": smooth_window_multiplier,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def despill(
        self,
        *,
        type: Int | Literal["green", "blue"] | Default = Default("green"),
        mix: Float = Default("0.5"),
        expand: Float = Default("0"),
        red: Float = Default("0"),
        green: Float = Default("-1"),
        blue: Float = Default("0"),
        brightness: Float = Default("0"),
        alpha: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Despill video.

        Args:
            type: set the screen type (from 0 to 1) (default green)
            mix: set the spillmap mix (from 0 to 1) (default 0.5)
            expand: set the spillmap expand (from 0 to 1) (default 0)
            red: set red scale (from -100 to 100) (default 0)
            green: set green scale (from -100 to 100) (default -1)
            blue: set blue scale (from -100 to 100) (default 0)
            brightness: set brightness (from -10 to 10) (default 0)
            alpha: change alpha component (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#despill)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="despill", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "type": type,
                    "mix": mix,
                    "expand": expand,
                    "red": red,
                    "green": green,
                    "blue": blue,
                    "brightness": brightness,
                    "alpha": alpha,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def detelecine(
        self,
        *,
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default(
            "top"
        ),
        pattern: String = Default("23"),
        start_frame: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply an inverse telecine pattern.

        Args:
            first_field: select first field (from 0 to 1) (default top)
            pattern: pattern that describe for how many fields a frame is to be displayed (default "23")
            start_frame: position of first frame with respect to the pattern if stream is cut (from 0 to 13) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#detelecine)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="detelecine", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "first_field": first_field,
                    "pattern": pattern,
                    "start_frame": start_frame,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def dilation(
        self,
        *,
        coordinates: Int = Default("255"),
        threshold0: Int = Default("65535"),
        threshold1: Int = Default("65535"),
        threshold2: Int = Default("65535"),
        threshold3: Int = Default("65535"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply dilation effect.

        Args:
            coordinates: set coordinates (from 0 to 255) (default 255)
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dilation)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dilation", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "coordinates": coordinates,
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def dilation_opencl(
        self,
        *,
        threshold0: Float = Default("65535"),
        threshold1: Float = Default("65535"),
        threshold2: Float = Default("65535"),
        threshold3: Float = Default("65535"),
        coordinates: Int = Default("255"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply dilation effect.

        Args:
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            coordinates: set coordinates (from 0 to 255) (default 255)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dilation_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dilation_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                    "coordinates": coordinates,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def displace(
        self,
        _xmap: VideoStream,
        _ymap: VideoStream,
        *,
        edge: Int | Literal["blank", "smear", "wrap", "mirror"] | Default = Default(
            "smear"
        ),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Displace pixels.

        Args:
            edge: set edge mode (from 0 to 3) (default smear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#displace)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="displace",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _xmap,
            _ymap,
            **merge(
                {
                    "edge": edge,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def dnn_classify(
        self,
        *,
        dnn_backend: Int = Default("2"),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default("true"),
        confidence: Float = Default("0.5"),
        labels: String = Default(None),
        target: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply DNN classify filter to the input.

        Args:
            dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
            model: path to model file
            input: input name of the model
            output: output name of the model
            backend_configs: backend configs
            options: backend configs (deprecated, use backend_configs)
            _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
            confidence: threshold of confidence (from 0 to 1) (default 0.5)
            labels: path to labels file
            target: which one to be classified
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dnn_005fclassify)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dnn_classify", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def dnn_detect(
        self,
        *,
        dnn_backend: Int = Default("2"),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default("true"),
        confidence: Float = Default("0.5"),
        labels: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply DNN detect filter to the input.

        Args:
            dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 2)
            model: path to model file
            input: input name of the model
            output: output name of the model
            backend_configs: backend configs
            options: backend configs (deprecated, use backend_configs)
            _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
            confidence: threshold of confidence (from 0 to 1) (default 0.5)
            labels: path to labels file
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dnn_005fdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dnn_detect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def dnn_processing(
        self,
        *,
        dnn_backend: Int = Default("1"),
        model: String = Default(None),
        input: String = Default(None),
        output: String = Default(None),
        backend_configs: String = Default(None),
        options: String = Default(None),
        _async: Boolean = Default("true"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply DNN processing filter to the input.

        Args:
            dnn_backend: DNN backend (from INT_MIN to INT_MAX) (default 1)
            model: path to model file
            input: input name of the model
            output: output name of the model
            backend_configs: backend configs
            options: backend configs (deprecated, use backend_configs)
            _async: use DNN async inference (ignored, use backend_configs='async=1') (default true)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#dnn_005fprocessing)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="dnn_processing",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "dnn_backend": dnn_backend,
                    "model": model,
                    "input": input,
                    "output": output,
                    "backend_configs": backend_configs,
                    "options": options,
                    "async": _async,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def doubleweave(
        self,
        *,
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default(
            "top"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Weave input video fields into double number of frames.

        Args:
            first_field: set first field (from 0 to 1) (default top)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="doubleweave", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "first_field": first_field,
                },
                extra_options,
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
        replace: Boolean = Default("false"),
        box_source: String = Default(None),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Draw a colored box on the input video.

        Args:
            x: set horizontal position of the left box edge (default "0")
            y: set vertical position of the top box edge (default "0")
            width: set width of the box (default "0")
            height: set height of the box (default "0")
            color: set color of the box (default "black")
            thickness: set the box thickness (default "3")
            replace: replace color & alpha (default false)
            box_source: use datas from bounding box in side data
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#drawbox)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="drawbox", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "color": color,
                    "thickness": thickness,
                    "replace": replace,
                    "box_source": box_source,
                },
                extra_options,
                timeline_options,
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
        min: Float = Default("-1"),
        max: Float = Default("1"),
        mode: Int | Literal["bar", "dot", "line"] | Default = Default("line"),
        slide: Int
        | Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | Default = Default("frame"),
        size: Image_size = Default("900x256"),
        rate: Video_rate = Default("25"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Draw a graph using input video metadata.

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
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#drawgraph)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="drawgraph", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
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
        replace: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Draw a colored grid on the input video.

        Args:
            x: set horizontal offset (default "0")
            y: set vertical offset (default "0")
            width: set width of grid cell (default "0")
            height: set height of grid cell (default "0")
            color: set color of the grid (default "black")
            thickness: set grid line thickness (default "1")
            replace: replace color & alpha (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#drawgrid)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="drawgrid", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "color": color,
                    "thickness": thickness,
                    "replace": replace,
                },
                extra_options,
                timeline_options,
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
        box: Boolean = Default("false"),
        boxborderw: String = Default("0"),
        line_spacing: Int = Default("0"),
        fontsize: String = Default(None),
        text_align: Flags
        | Literal[
            "left",
            "L",
            "right",
            "R",
            "center",
            "C",
            "top",
            "T",
            "bottom",
            "B",
            "middle",
            "M",
        ]
        | Default = Default("0"),
        x: String = Default("0"),
        y: String = Default("0"),
        boxw: Int = Default("0"),
        boxh: Int = Default("0"),
        shadowx: Int = Default("0"),
        shadowy: Int = Default("0"),
        borderw: Int = Default("0"),
        tabsize: Int = Default("4"),
        basetime: Int64 = Default("I64_MIN"),
        font: String = Default("Sans"),
        expansion: Int | Literal["none", "normal", "strftime"] | Default = Default(
            "normal"
        ),
        y_align: Int | Literal["text", "baseline", "font"] | Default = Default("text"),
        timecode: String = Default(None),
        tc24hmax: Boolean = Default("false"),
        timecode_rate: Rational = Default("0/1"),
        reload: Int = Default("0"),
        alpha: String = Default("1"),
        fix_bounds: Boolean = Default("false"),
        start_number: Int = Default("0"),
        text_source: String = Default(None),
        text_shaping: Boolean = Default("true"),
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Draw text on top of video frames using libfreetype library.

        Args:
            fontfile: set font file
            text: set text
            textfile: set text file
            fontcolor: set foreground color (default "black")
            fontcolor_expr: set foreground color expression (default "")
            boxcolor: set box color (default "white")
            bordercolor: set border color (default "black")
            shadowcolor: set shadow color (default "black")
            box: set box (default false)
            boxborderw: set box borders width (default "0")
            line_spacing: set line spacing in pixels (from INT_MIN to INT_MAX) (default 0)
            fontsize: set font size
            text_align: set text alignment (default 0)
            x: set x expression (default "0")
            y: set y expression (default "0")
            boxw: set box width (from 0 to INT_MAX) (default 0)
            boxh: set box height (from 0 to INT_MAX) (default 0)
            shadowx: set shadow x offset (from INT_MIN to INT_MAX) (default 0)
            shadowy: set shadow y offset (from INT_MIN to INT_MAX) (default 0)
            borderw: set border width (from INT_MIN to INT_MAX) (default 0)
            tabsize: set tab size (from 0 to INT_MAX) (default 4)
            basetime: set base time (from I64_MIN to I64_MAX) (default I64_MIN)
            font: Font name (default "Sans")
            expansion: set the expansion mode (from 0 to 2) (default normal)
            y_align: set the y alignment (from 0 to 2) (default text)
            timecode: set initial timecode
            tc24hmax: set 24 hours max (timecode only) (default false)
            timecode_rate: set rate (timecode only) (from 0 to INT_MAX) (default 0/1)
            reload: reload text file at specified frame interval (from 0 to INT_MAX) (default 0)
            alpha: apply alpha while rendering (default "1")
            fix_bounds: check and fix text coords to avoid clipping (default false)
            start_number: start frame number for n/frame_num variable (from 0 to INT_MAX) (default 0)
            text_source: the source of text
            text_shaping: attempt to shape text before drawing (default true)
            ft_load_flags: set font loading flags for libfreetype (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#drawtext)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="drawtext", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                    "text_align": text_align,
                    "x": x,
                    "y": y,
                    "boxw": boxw,
                    "boxh": boxh,
                    "shadowx": shadowx,
                    "shadowy": shadowy,
                    "borderw": borderw,
                    "tabsize": tabsize,
                    "basetime": basetime,
                    "font": font,
                    "expansion": expansion,
                    "y_align": y_align,
                    "timecode": timecode,
                    "tc24hmax": tc24hmax,
                    "timecode_rate": timecode_rate,
                    "reload": reload,
                    "alpha": alpha,
                    "fix_bounds": fix_bounds,
                    "start_number": start_number,
                    "text_source": text_source,
                    "text_shaping": text_shaping,
                    "ft_load_flags": ft_load_flags,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def edgedetect(
        self,
        *,
        high: Double = Default("0.196078"),
        low: Double = Default("0.0784314"),
        mode: Int | Literal["wires", "colormix", "canny"] | Default = Default("wires"),
        planes: Flags | Literal["y", "u", "v", "r", "g", "b"] | Default = Default(
            "y+u+v+r+g+b"
        ),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Detect and draw edge.

        Args:
            high: set high threshold (from 0 to 1) (default 0.196078)
            low: set low threshold (from 0 to 1) (default 0.0784314)
            mode: set mode (from 0 to 2) (default wires)
            planes: set planes to filter (default y+u+v+r+g+b)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#edgedetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="edgedetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "high": high,
                    "low": low,
                    "mode": mode,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def elbg(
        self,
        *,
        codebook_length: Int = Default("256"),
        nb_steps: Int = Default("1"),
        seed: Int64 = Default("-1"),
        pal8: Boolean = Default("false"),
        use_alpha: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply posterize effect, using the ELBG algorithm.

        Args:
            codebook_length: set codebook length (from 1 to INT_MAX) (default 256)
            nb_steps: set max number of steps used to compute the mapping (from 1 to INT_MAX) (default 1)
            seed: set the random seed (from -1 to UINT32_MAX) (default -1)
            pal8: set the pal8 output (default false)
            use_alpha: use alpha channel for mapping (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#elbg)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="elbg", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "codebook_length": codebook_length,
                    "nb_steps": nb_steps,
                    "seed": seed,
                    "pal8": pal8,
                    "use_alpha": use_alpha,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def entropy(
        self,
        *,
        mode: Int | Literal["normal", "diff"] | Default = Default("normal"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Measure video frames entropy.

        Args:
            mode: set kind of histogram entropy measurement (from 0 to 1) (default normal)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#entropy)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="entropy", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def epx(
        self,
        *,
        n: Int = Default("3"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scale the input using EPX algorithm.

        Args:
            n: set scale factor (from 2 to 3) (default 3)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#epx)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="epx", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "n": n,
                },
                extra_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust brightness, contrast, gamma, and saturation.

        Args:
            contrast: set the contrast adjustment, negative values give a negative image (default "1.0")
            brightness: set the brightness adjustment (default "0.0")
            saturation: set the saturation adjustment (default "1.0")
            gamma: set the initial gamma value (default "1.0")
            gamma_r: gamma value for red (default "1.0")
            gamma_g: gamma value for green (default "1.0")
            gamma_b: gamma value for blue (default "1.0")
            gamma_weight: set the gamma weight which reduces the effect of gamma on bright areas (default "1.0")
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#eq)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="eq", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def erosion(
        self,
        *,
        coordinates: Int = Default("255"),
        threshold0: Int = Default("65535"),
        threshold1: Int = Default("65535"),
        threshold2: Int = Default("65535"),
        threshold3: Int = Default("65535"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply erosion effect.

        Args:
            coordinates: set coordinates (from 0 to 255) (default 255)
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#erosion)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="erosion", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "coordinates": coordinates,
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def erosion_opencl(
        self,
        *,
        threshold0: Float = Default("65535"),
        threshold1: Float = Default("65535"),
        threshold2: Float = Default("65535"),
        threshold3: Float = Default("65535"),
        coordinates: Int = Default("255"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply erosion effect.

        Args:
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            coordinates: set coordinates (from 0 to 255) (default 255)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#erosion_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="erosion_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                    "coordinates": coordinates,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def estdif(
        self,
        *,
        mode: Int | Literal["frame", "field"] | Default = Default("field"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        rslope: Int = Default("1"),
        redge: Int = Default("2"),
        ecost: Int = Default("2"),
        mcost: Int = Default("1"),
        dcost: Int = Default("1"),
        interp: Int | Literal["2p", "4p", "6p"] | Default = Default("4p"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Edge Slope Tracing deinterlace.

        Args:
            mode: specify the mode (from 0 to 1) (default field)
            parity: specify the assumed picture field parity (from -1 to 1) (default auto)
            deint: specify which frames to deinterlace (from 0 to 1) (default all)
            rslope: specify the search radius for edge slope tracing (from 1 to 15) (default 1)
            redge: specify the search radius for best edge matching (from 0 to 15) (default 2)
            ecost: specify the edge cost for edge matching (from 0 to 50) (default 2)
            mcost: specify the middle cost for edge matching (from 0 to 50) (default 1)
            dcost: specify the distance cost for edge matching (from 0 to 50) (default 1)
            interp: specify the type of interpolation (from 0 to 2) (default 4p)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#estdif)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="estdif", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def exposure(
        self,
        *,
        exposure: Float = Default("0"),
        black: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust exposure of the video stream.

        Args:
            exposure: set the exposure correction (from -3 to 3) (default 0)
            black: set the black level correction (from -1 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#exposure)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="exposure", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "exposure": exposure,
                    "black": black,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def extractplanes(
        self,
        *,
        planes: Flags | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default(
            "r"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> FilterNode:
        """

        Extract planes as grayscale frames.

        Args:
            planes: set planes (default r)
            extra_options: Extra options for the filter

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#extractplanes)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="extractplanes",
                typings_input=("video",),
                typings_output="[StreamType.video] * len(planes.split('+'))",
            ),
            self,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
            ),
        )

        return filter_node

    def fade(
        self,
        *,
        type: Int | Literal["in", "out"] | Default = Default("in"),
        start_frame: Int = Default("0"),
        nb_frames: Int = Default("25"),
        alpha: Boolean = Default("false"),
        start_time: Duration = Default("0"),
        duration: Duration = Default("0"),
        color: Color = Default("black"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Fade in/out input video.

        Args:
            type: set the fade direction (from 0 to 1) (default in)
            start_frame: Number of the first frame to which to apply the effect. (from 0 to INT_MAX) (default 0)
            nb_frames: Number of frames to which the effect should be applied. (from 1 to INT_MAX) (default 25)
            alpha: fade alpha if it is available on the input (default false)
            start_time: Number of seconds of the beginning of the effect. (default 0)
            duration: Duration of the effect in seconds. (default 0)
            color: set color (default "black")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fade)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fade", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "type": type,
                    "start_frame": start_frame,
                    "nb_frames": nb_frames,
                    "alpha": alpha,
                    "start_time": start_time,
                    "duration": duration,
                    "color": color,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def feedback(
        self,
        _feedin: VideoStream,
        *,
        x: Int = Default("0"),
        w: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> tuple[
        VideoStream,
        VideoStream,
    ]:
        """

        Apply feedback video filter.

        Args:
            x: set top left crop position (from 0 to INT_MAX) (default 0)
            w: set crop size (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream
            feedout: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#feedback)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="feedback",
                typings_input=("video", "video"),
                typings_output=("video", "video"),
            ),
            self,
            _feedin,
            **merge(
                {
                    "x": x,
                    "w": w,
                },
                extra_options,
            ),
        )
        return (
            filter_node.video(0),
            filter_node.video(1),
        )

    def fftdnoiz(
        self,
        *,
        sigma: Float = Default("1"),
        amount: Float = Default("1"),
        block: Int = Default("32"),
        overlap: Float = Default("0.5"),
        method: Int | Literal["wiener", "hard"] | Default = Default("wiener"),
        prev: Int = Default("0"),
        next: Int = Default("0"),
        planes: Int = Default("7"),
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Denoise frames using 3D FFT.

        Args:
            sigma: set denoise strength (from 0 to 100) (default 1)
            amount: set amount of denoising (from 0.01 to 1) (default 1)
            block: set block size (from 8 to 256) (default 32)
            overlap: set block overlap (from 0.2 to 0.8) (default 0.5)
            method: set method of denoising (from 0 to 1) (default wiener)
            prev: set number of previous frames for temporal denoising (from 0 to 1) (default 0)
            next: set number of next frames for temporal denoising (from 0 to 1) (default 0)
            planes: set planes to filter (from 0 to 15) (default 7)
            window: set window function (from 0 to 20) (default hann)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fftdnoiz", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def fftfilt(
        self,
        *,
        dc_Y: Int = Default("0"),
        dc_U: Int = Default("0"),
        dc_V: Int = Default("0"),
        weight_Y: String = Default("1"),
        weight_U: String = Default(None),
        weight_V: String = Default(None),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply arbitrary expressions to pixels in frequency domain.

        Args:
            dc_Y: adjust gain in Y plane (from 0 to 1000) (default 0)
            dc_U: adjust gain in U plane (from 0 to 1000) (default 0)
            dc_V: adjust gain in V plane (from 0 to 1000) (default 0)
            weight_Y: set luminance expression in Y plane (default "1")
            weight_U: set chrominance expression in U plane
            weight_V: set chrominance expression in V plane
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fftfilt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fftfilt", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "dc_Y": dc_Y,
                    "dc_U": dc_U,
                    "dc_V": dc_V,
                    "weight_Y": weight_Y,
                    "weight_U": weight_U,
                    "weight_V": weight_V,
                    "eval": eval,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def field(
        self,
        *,
        type: Int | Literal["top", "bottom"] | Default = Default("top"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Extract a field from the input video.

        Args:
            type: set field type (top or bottom) (from 0 to 1) (default top)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#field)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="field", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "type": type,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def fieldhint(
        self,
        *,
        hint: String = Default(None),
        mode: Int | Literal["absolute", "relative", "pattern"] | Default = Default(
            "absolute"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Field matching using hints.

        Args:
            hint: set hint file
            mode: set hint mode (from 0 to 2) (default absolute)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fieldhint)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fieldhint", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "hint": hint,
                    "mode": mode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def fieldorder(
        self,
        *,
        order: Int | Literal["bff", "tff"] | Default = Default("tff"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set the field order.

        Args:
            order: output field order (from 0 to 1) (default tff)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fieldorder)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fieldorder", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "order": order,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def fillborders(
        self,
        *,
        left: Int = Default("0"),
        right: Int = Default("0"),
        top: Int = Default("0"),
        bottom: Int = Default("0"),
        mode: Int
        | Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | Default = Default("smear"),
        color: Color = Default("black"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Fill borders of the input video.

        Args:
            left: set the left fill border (from 0 to INT_MAX) (default 0)
            right: set the right fill border (from 0 to INT_MAX) (default 0)
            top: set the top fill border (from 0 to INT_MAX) (default 0)
            bottom: set the bottom fill border (from 0 to INT_MAX) (default 0)
            mode: set the fill borders mode (from 0 to 6) (default smear)
            color: set the color for the fixed/fade mode (default "black")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fillborders)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fillborders", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "left": left,
                    "right": right,
                    "top": top,
                    "bottom": bottom,
                    "mode": mode,
                    "color": color,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def find_rect(
        self,
        *,
        object: String = Default(None),
        threshold: Float = Default("0.5"),
        mipmaps: Int = Default("3"),
        xmin: Int = Default("0"),
        discard: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Find a user specified object.

        Args:
            object: object bitmap filename
            threshold: set threshold (from 0 to 1) (default 0.5)
            mipmaps: set mipmaps (from 1 to 5) (default 3)
            xmin: (from 0 to INT_MAX) (default 0)
            discard: (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#find_005frect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="find_rect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "object": object,
                    "threshold": threshold,
                    "mipmaps": mipmaps,
                    "xmin": xmin,
                    "discard": discard,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def flip_vulkan(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Flip both horizontally and vertically.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#flip_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="flip_vulkan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def floodfill(
        self,
        *,
        x: Int = Default("0"),
        y: Int = Default("0"),
        s0: Int = Default("0"),
        s1: Int = Default("0"),
        s2: Int = Default("0"),
        s3: Int = Default("0"),
        d0: Int = Default("0"),
        d1: Int = Default("0"),
        d2: Int = Default("0"),
        d3: Int = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Fill area with same color with another color.

        Args:
            x: set pixel x coordinate (from 0 to 65535) (default 0)
            y: set pixel y coordinate (from 0 to 65535) (default 0)
            s0: set source #0 component value (from -1 to 65535) (default 0)
            s1: set source #1 component value (from -1 to 65535) (default 0)
            s2: set source #2 component value (from -1 to 65535) (default 0)
            s3: set source #3 component value (from -1 to 65535) (default 0)
            d0: set destination #0 component value (from 0 to 65535) (default 0)
            d1: set destination #1 component value (from 0 to 65535) (default 0)
            d2: set destination #2 component value (from 0 to 65535) (default 0)
            d3: set destination #3 component value (from 0 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#floodfill)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="floodfill", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def format(
        self,
        *,
        pix_fmts: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert the input video to one of the specified pixel formats.

        Args:
            pix_fmts: A '|'-separated list of pixel formats
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#format)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="format", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "pix_fmts": pix_fmts,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def fps(
        self,
        *,
        fps: String = Default("25"),
        start_time: Double = Default("DBL_MAX"),
        round: Int | Literal["zero", "inf", "down", "up", "near"] | Default = Default(
            "near"
        ),
        eof_action: Int | Literal["round", "pass"] | Default = Default("round"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Force constant framerate.

        Args:
            fps: A string describing desired output framerate (default "25")
            start_time: Assume the first PTS should be this value. (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
            round: set rounding method for timestamps (from 0 to 5) (default near)
            eof_action: action performed for last frame (from 0 to 1) (default round)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fps)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fps", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "fps": fps,
                    "start_time": start_time,
                    "round": round,
                    "eof_action": eof_action,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def framepack(
        self,
        _right: VideoStream,
        *,
        format: Int
        | Literal["sbs", "tab", "frameseq", "lines", "columns"]
        | Default = Default("sbs"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Generate a frame packed stereoscopic video.

        Args:
            format: Frame pack output format (from 0 to INT_MAX) (default sbs)
            extra_options: Extra options for the filter

        Returns:
            packed: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#framepack)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="framepack",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _right,
            **merge(
                {
                    "format": format,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def framerate(
        self,
        *,
        fps: Video_rate = Default("50"),
        interp_start: Int = Default("15"),
        interp_end: Int = Default("240"),
        scene: Double = Default("8.2"),
        flags: Flags | Literal["scene_change_detect", "scd"] | Default = Default(
            "scene_change_detect+scd"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Upsamples or downsamples progressive source between specified frame rates.

        Args:
            fps: required output frames per second rate (default "50")
            interp_start: point to start linear interpolation (from 0 to 255) (default 15)
            interp_end: point to end linear interpolation (from 0 to 255) (default 240)
            scene: scene change level (from 0 to 100) (default 8.2)
            flags: set flags (default scene_change_detect+scd)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#framerate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="framerate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "fps": fps,
                    "interp_start": interp_start,
                    "interp_end": interp_end,
                    "scene": scene,
                    "flags": flags,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def framestep(
        self,
        *,
        step: Int = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Select one frame every N frames.

        Args:
            step: set frame step (from 1 to INT_MAX) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#framestep)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="framestep", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "step": step,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def freezedetect(
        self,
        *,
        n: Double = Default("0.001"),
        d: Duration = Default("2"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Detects frozen video input.

        Args:
            n: set noise tolerance (from 0 to 1) (default 0.001)
            d: set minimum duration in seconds (default 2)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#freezedetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="freezedetect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "n": n,
                    "d": d,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def freezeframes(
        self,
        _replace: VideoStream,
        *,
        first: Int64 = Default("0"),
        last: Int64 = Default("0"),
        replace: Int64 = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Freeze video frames.

        Args:
            first: set first frame to freeze (from 0 to I64_MAX) (default 0)
            last: set last frame to freeze (from 0 to I64_MAX) (default 0)
            replace: set frame to replace (from 0 to I64_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#freezeframes)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="freezeframes",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _replace,
            **merge(
                {
                    "first": first,
                    "last": last,
                    "replace": replace,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def frei0r(
        self,
        *,
        filter_name: String = Default(None),
        filter_params: String = Default(None),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply a frei0r effect.

        Args:
            filter_name:
            filter_params:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#frei0r)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="frei0r", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filter_name": filter_name,
                    "filter_params": filter_params,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def fspp(
        self,
        *,
        quality: Int = Default("4"),
        qp: Int = Default("0"),
        strength: Int = Default("0"),
        use_bframe_qp: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Fast Simple Post-processing filter.

        Args:
            quality: set quality (from 4 to 5) (default 4)
            qp: force a constant quantizer parameter (from 0 to 64) (default 0)
            strength: set filter strength (from -15 to 32) (default 0)
            use_bframe_qp: use B-frames' QP (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#fspp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="fspp", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "quality": quality,
                    "qp": qp,
                    "strength": strength,
                    "use_bframe_qp": use_bframe_qp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def gblur(
        self,
        *,
        sigma: Float = Default("0.5"),
        steps: Int = Default("1"),
        planes: Int = Default("15"),
        sigmaV: Float = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Gaussian Blur filter.

        Args:
            sigma: set sigma (from 0 to 1024) (default 0.5)
            steps: set number of steps (from 1 to 6) (default 1)
            planes: set planes to filter (from 0 to 15) (default 15)
            sigmaV: set vertical sigma (from -1 to 1024) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#gblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="gblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sigma": sigma,
                    "steps": steps,
                    "planes": planes,
                    "sigmaV": sigmaV,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def gblur_vulkan(
        self,
        *,
        sigma: Float = Default("0.5"),
        sigmaV: Float = Default("0"),
        planes: Int = Default("15"),
        size: Int = Default("19"),
        sizeV: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Gaussian Blur in Vulkan.

        Args:
            sigma: Set sigma (from 0.01 to 1024) (default 0.5)
            sigmaV: Set vertical sigma (from 0 to 1024) (default 0)
            planes: Set planes to filter (from 0 to 15) (default 15)
            size: Set kernel size (from 1 to 127) (default 19)
            sizeV: Set vertical kernel size (from 0 to 127) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#gblur_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="gblur_vulkan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sigma": sigma,
                    "sigmaV": sigmaV,
                    "planes": planes,
                    "size": size,
                    "sizeV": sizeV,
                },
                extra_options,
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
        interpolation: Int
        | Literal["nearest", "n", "bilinear", "b"]
        | Default = Default("bilinear"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply generic equation to each pixel.

        Args:
            lum_expr: set luminance expression
            cb_expr: set chroma blue expression
            cr_expr: set chroma red expression
            alpha_expr: set alpha expression
            red_expr: set red expression
            green_expr: set green expression
            blue_expr: set blue expression
            interpolation: set interpolation method (from 0 to 1) (default bilinear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#geq)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="geq", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "lum_expr": lum_expr,
                    "cb_expr": cb_expr,
                    "cr_expr": cr_expr,
                    "alpha_expr": alpha_expr,
                    "red_expr": red_expr,
                    "green_expr": green_expr,
                    "blue_expr": blue_expr,
                    "interpolation": interpolation,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def gradfun(
        self,
        *,
        strength: Float = Default("1.2"),
        radius: Int = Default("16"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Debands video quickly using gradients.

        Args:
            strength: The maximum amount by which the filter will change any one pixel. (from 0.51 to 64) (default 1.2)
            radius: The neighborhood to fit the gradient to. (from 4 to 32) (default 16)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#gradfun)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="gradfun", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "strength": strength,
                    "radius": radius,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def graphmonitor(
        self,
        *,
        size: Image_size = Default("hd720"),
        opacity: Float = Default("0.9"),
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
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Show various filtergraph stats.

        Args:
            size: set monitor size (default "hd720")
            opacity: set video opacity (from 0 to 1) (default 0.9)
            mode: set mode (default 0)
            flags: set flags (default all+queue)
            rate: set video rate (default "25")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#graphmonitor)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="graphmonitor", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "size": size,
                    "opacity": opacity,
                    "mode": mode,
                    "flags": flags,
                    "rate": rate,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def grayworld(
        self,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust white balance using LAB gray world algorithm.

        Args:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#grayworld)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="grayworld", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def greyedge(
        self,
        *,
        difford: Int = Default("1"),
        minknorm: Int = Default("1"),
        sigma: Double = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Estimates scene illumination by grey edge assumption.

        Args:
            difford: set differentiation order (from 0 to 2) (default 1)
            minknorm: set Minkowski norm (from 0 to 20) (default 1)
            sigma: set sigma (from 0 to 1024) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#greyedge)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="greyedge", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "difford": difford,
                    "minknorm": minknorm,
                    "sigma": sigma,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def haldclut(
        self,
        _clut: VideoStream,
        *,
        clut: Int | Literal["first", "all"] | Default = Default("all"),
        interp: Int
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("tetrahedral"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust colors using a Hald CLUT.

        Args:
            clut: when to process CLUT (from 0 to 1) (default all)
            interp: select interpolation mode (from 0 to 4) (default tetrahedral)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#haldclut)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="haldclut",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _clut,
            **merge(
                {
                    "clut": clut,
                    "interp": interp,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def hflip(
        self,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Horizontally flip the input video.

        Args:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hflip)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hflip", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def hflip_vulkan(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Horizontally flip the input video in Vulkan.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hflip_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hflip_vulkan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def histeq(
        self,
        *,
        strength: Float = Default("0.2"),
        intensity: Float = Default("0.21"),
        antibanding: Int | Literal["none", "weak", "strong"] | Default = Default(
            "none"
        ),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply global color histogram equalization.

        Args:
            strength: set the strength (from 0 to 1) (default 0.2)
            intensity: set the intensity (from 0 to 1) (default 0.21)
            antibanding: set the antibanding level (from 0 to 2) (default none)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#histeq)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="histeq", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "strength": strength,
                    "intensity": intensity,
                    "antibanding": antibanding,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def histogram(
        self,
        *,
        level_height: Int = Default("200"),
        scale_height: Int = Default("12"),
        display_mode: Int | Literal["overlay", "parade", "stack"] | Default = Default(
            "stack"
        ),
        levels_mode: Int | Literal["linear", "logarithmic"] | Default = Default(
            "linear"
        ),
        components: Int = Default("7"),
        fgopacity: Float = Default("0.7"),
        bgopacity: Float = Default("0.5"),
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
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and draw a histogram.

        Args:
            level_height: set level height (from 50 to 2048) (default 200)
            scale_height: set scale height (from 0 to 40) (default 12)
            display_mode: set display mode (from 0 to 2) (default stack)
            levels_mode: set levels mode (from 0 to 1) (default linear)
            components: set color components to display (from 1 to 15) (default 7)
            fgopacity: set foreground opacity (from 0 to 1) (default 0.7)
            bgopacity: set background opacity (from 0 to 1) (default 0.5)
            colors_mode: set colors mode (from 0 to 9) (default whiteonblack)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#histogram)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="histogram", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "level_height": level_height,
                    "scale_height": scale_height,
                    "display_mode": display_mode,
                    "levels_mode": levels_mode,
                    "components": components,
                    "fgopacity": fgopacity,
                    "bgopacity": bgopacity,
                    "colors_mode": colors_mode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hqdn3d(
        self,
        *,
        luma_spatial: Double = Default("0"),
        chroma_spatial: Double = Default("0"),
        luma_tmp: Double = Default("0"),
        chroma_tmp: Double = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply a High Quality 3D Denoiser.

        Args:
            luma_spatial: spatial luma strength (from 0 to DBL_MAX) (default 0)
            chroma_spatial: spatial chroma strength (from 0 to DBL_MAX) (default 0)
            luma_tmp: temporal luma strength (from 0 to DBL_MAX) (default 0)
            chroma_tmp: temporal chroma strength (from 0 to DBL_MAX) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hqdn3d)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hqdn3d", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "luma_spatial": luma_spatial,
                    "chroma_spatial": chroma_spatial,
                    "luma_tmp": luma_tmp,
                    "chroma_tmp": chroma_tmp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def hqx(
        self,
        *,
        n: Int = Default("3"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

        Args:
            n: set scale factor (from 2 to 4) (default 3)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hqx)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hqx", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "n": n,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hsvhold(
        self,
        *,
        hue: Float = Default("0"),
        sat: Float = Default("0"),
        val: Float = Default("0"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain HSV range into gray.

        Args:
            hue: set the hue value (from -360 to 360) (default 0)
            sat: set the saturation value (from -1 to 1) (default 0)
            val: set the value value (from -1 to 1) (default 0)
            similarity: set the hsvhold similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the hsvhold blend value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hsvhold)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hsvhold", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "hue": hue,
                    "sat": sat,
                    "val": val,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def hsvkey(
        self,
        *,
        hue: Float = Default("0"),
        sat: Float = Default("0"),
        val: Float = Default("0"),
        similarity: Float = Default("0.01"),
        blend: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain HSV range into transparency. Operates on YUV colors.

        Args:
            hue: set the hue value (from -360 to 360) (default 0)
            sat: set the saturation value (from -1 to 1) (default 0)
            val: set the value value (from -1 to 1) (default 0)
            similarity: set the hsvkey similarity value (from 1e-05 to 1) (default 0.01)
            blend: set the hsvkey blend value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hsvkey)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hsvkey", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "hue": hue,
                    "sat": sat,
                    "val": val,
                    "similarity": similarity,
                    "blend": blend,
                },
                extra_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust the hue and saturation of the input video.

        Args:
            h: set the hue angle degrees expression
            s: set the saturation expression (default "1")
            H: set the hue angle radians expression
            b: set the brightness expression (default "0")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hue)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hue", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "h": h,
                    "s": s,
                    "H": H,
                    "b": b,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def huesaturation(
        self,
        *,
        hue: Float = Default("0"),
        saturation: Float = Default("0"),
        intensity: Float = Default("0"),
        colors: Flags | Literal["r", "y", "g", "c", "b", "m", "a"] | Default = Default(
            "r+y+g+c+b+m+a"
        ),
        strength: Float = Default("1"),
        rw: Float = Default("0.333"),
        gw: Float = Default("0.334"),
        bw: Float = Default("0.333"),
        lightness: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply hue-saturation-intensity adjustments.

        Args:
            hue: set the hue shift (from -180 to 180) (default 0)
            saturation: set the saturation shift (from -1 to 1) (default 0)
            intensity: set the intensity shift (from -1 to 1) (default 0)
            colors: set colors range (default r+y+g+c+b+m+a)
            strength: set the filtering strength (from 0 to 100) (default 1)
            rw: set the red weight (from 0 to 1) (default 0.333)
            gw: set the green weight (from 0 to 1) (default 0.334)
            bw: set the blue weight (from 0 to 1) (default 0.333)
            lightness: set the preserve lightness (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#huesaturation)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="huesaturation",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def hwdownload(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Download a hardware frame to a normal frame.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hwdownload)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hwdownload", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hwmap(
        self,
        *,
        mode: Flags
        | Literal["read", "write", "overwrite", "direct"]
        | Default = Default("read+write"),
        derive_device: String = Default(None),
        reverse: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Map hardware frames.

        Args:
            mode: Frame mapping mode (default read+write)
            derive_device: Derive a new device of this type
            reverse: Map in reverse (create and allocate in the sink) (from 0 to 1) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hwmap)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hwmap", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "derive_device": derive_device,
                    "reverse": reverse,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hwupload(
        self,
        *,
        derive_device: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Upload a normal frame to a hardware frame.

        Args:
            derive_device: Derive a new device of this type
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hwupload)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hwupload", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "derive_device": derive_device,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hwupload_cuda(
        self,
        *,
        device: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Upload a system memory frame to a CUDA device.

        Args:
            device: Number of the device to use (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hwupload_005fcuda)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hwupload_cuda",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "device": device,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def hysteresis(
        self,
        _alt: VideoStream,
        *,
        planes: Int = Default("15"),
        threshold: Int = Default("0"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Grow first stream into second stream by connecting components.

        Args:
            planes: set planes (from 0 to 15) (default 15)
            threshold: set threshold (from 0 to 65535) (default 0)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#hysteresis)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="hysteresis",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _alt,
            **merge(
                {
                    "planes": planes,
                    "threshold": threshold,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def identity(
        self,
        _reference: VideoStream,
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the Identity between two video streams.

        Args:
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#identity)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="identity",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _reference,
            **merge(
                {},
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def idet(
        self,
        *,
        intl_thres: Float = Default("1.04"),
        prog_thres: Float = Default("1.5"),
        rep_thres: Float = Default("3"),
        half_life: Float = Default("0"),
        analyze_interlaced_flag: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Interlace detect Filter.

        Args:
            intl_thres: set interlacing threshold (from -1 to FLT_MAX) (default 1.04)
            prog_thres: set progressive threshold (from -1 to FLT_MAX) (default 1.5)
            rep_thres: set repeat threshold (from -1 to FLT_MAX) (default 3)
            half_life: half life of cumulative statistics (from -1 to INT_MAX) (default 0)
            analyze_interlaced_flag: set number of frames to use to determine if the interlace flag is accurate (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#idet)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="idet", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "intl_thres": intl_thres,
                    "prog_thres": prog_thres,
                    "rep_thres": rep_thres,
                    "half_life": half_life,
                    "analyze_interlaced_flag": analyze_interlaced_flag,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def il(
        self,
        *,
        luma_mode: Int
        | Literal["none", "interleave", "i", "deinterleave", "d"]
        | Default = Default("none"),
        chroma_mode: Int
        | Literal["none", "interleave", "i", "deinterleave", "d"]
        | Default = Default("none"),
        alpha_mode: Int
        | Literal["none", "interleave", "i", "deinterleave", "d"]
        | Default = Default("none"),
        luma_swap: Boolean = Default("false"),
        chroma_swap: Boolean = Default("false"),
        alpha_swap: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deinterleave or interleave fields.

        Args:
            luma_mode: select luma mode (from 0 to 2) (default none)
            chroma_mode: select chroma mode (from 0 to 2) (default none)
            alpha_mode: select alpha mode (from 0 to 2) (default none)
            luma_swap: swap luma fields (default false)
            chroma_swap: swap chroma fields (default false)
            alpha_swap: swap alpha fields (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#il)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="il", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "luma_mode": luma_mode,
                    "chroma_mode": chroma_mode,
                    "alpha_mode": alpha_mode,
                    "luma_swap": luma_swap,
                    "chroma_swap": chroma_swap,
                    "alpha_swap": alpha_swap,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def inflate(
        self,
        *,
        threshold0: Int = Default("65535"),
        threshold1: Int = Default("65535"),
        threshold2: Int = Default("65535"),
        threshold3: Int = Default("65535"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply inflate effect.

        Args:
            threshold0: set threshold for 1st plane (from 0 to 65535) (default 65535)
            threshold1: set threshold for 2nd plane (from 0 to 65535) (default 65535)
            threshold2: set threshold for 3rd plane (from 0 to 65535) (default 65535)
            threshold3: set threshold for 4th plane (from 0 to 65535) (default 65535)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#inflate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="inflate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "threshold0": threshold0,
                    "threshold1": threshold1,
                    "threshold2": threshold2,
                    "threshold3": threshold3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def interlace(
        self,
        *,
        scan: Int | Literal["tff", "bff"] | Default = Default("tff"),
        lowpass: Int | Literal["off", "linear", "complex"] | Default = Default(
            "linear"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert progressive video into interlaced.

        Args:
            scan: scanning mode (from 0 to 1) (default tff)
            lowpass: set vertical low-pass filter (from 0 to 2) (default linear)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#interlace_002c-interlace_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="interlace", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "scan": scan,
                    "lowpass": lowpass,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def kerndeint(
        self,
        *,
        thresh: Int = Default("10"),
        map: Boolean = Default("false"),
        order: Boolean = Default("false"),
        sharp: Boolean = Default("false"),
        twoway: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply kernel deinterlacing to the input.

        Args:
            thresh: set the threshold (from 0 to 255) (default 10)
            map: set the map (default false)
            order: set the order (default false)
            sharp: set sharpening (default false)
            twoway: set twoway (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#kerndeint)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="kerndeint", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "thresh": thresh,
                    "map": map,
                    "order": order,
                    "sharp": sharp,
                    "twoway": twoway,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def kirsch(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply kirsch operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#kirsch)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="kirsch", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def lagfun(
        self,
        *,
        decay: Float = Default("0.95"),
        planes: Flags = Default("F"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Slowly update darker pixels.

        Args:
            decay: set decay (from 0 to 1) (default 0.95)
            planes: set what planes to filter (default F)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lagfun)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lagfun", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "decay": decay,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def latency(
        self,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Report video filtering latency.

        Args:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="latency", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def lenscorrection(
        self,
        *,
        cx: Double = Default("0.5"),
        cy: Double = Default("0.5"),
        k1: Double = Default("0"),
        k2: Double = Default("0"),
        i: Int | Literal["nearest", "bilinear"] | Default = Default("nearest"),
        fc: Color = Default("black@0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Rectify the image by correcting for lens distortion.

        Args:
            cx: set relative center x (from 0 to 1) (default 0.5)
            cy: set relative center y (from 0 to 1) (default 0.5)
            k1: set quadratic distortion factor (from -1 to 1) (default 0)
            k2: set double quadratic distortion factor (from -1 to 1) (default 0)
            i: set interpolation type (from 0 to 64) (default nearest)
            fc: set the color of the unmapped pixels (default "black@0")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lenscorrection)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lenscorrection",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "cx": cx,
                    "cy": cy,
                    "k1": k1,
                    "k2": k2,
                    "i": i,
                    "fc": fc,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def limiter(
        self,
        *,
        min: Int = Default("0"),
        max: Int = Default("65535"),
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Limit pixels components to the specified range.

        Args:
            min: set min value (from 0 to 65535) (default 0)
            max: set max value (from 0 to 65535) (default 65535)
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#limiter)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="limiter", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "min": min,
                    "max": max,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def loop(
        self,
        *,
        loop: Int = Default("0"),
        size: Int64 = Default("0"),
        start: Int64 = Default("0"),
        time: Duration = Default("INT64_MAX"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Loop video frames.

        Args:
            loop: number of loops (from -1 to INT_MAX) (default 0)
            size: max number of frames to loop (from 0 to 32767) (default 0)
            start: set the loop start frame (from -1 to I64_MAX) (default 0)
            time: set the loop start time (default INT64_MAX)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#loop)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="loop", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "loop": loop,
                    "size": size,
                    "start": start,
                    "time": time,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def lumakey(
        self,
        *,
        threshold: Double = Default("0"),
        tolerance: Double = Default("0.01"),
        softness: Double = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Turns a certain luma into transparency.

        Args:
            threshold: set the threshold value (from 0 to 1) (default 0)
            tolerance: set the tolerance value (from 0 to 1) (default 0.01)
            softness: set the softness value (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lumakey)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lumakey", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "threshold": threshold,
                    "tolerance": tolerance,
                    "softness": softness,
                },
                extra_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and apply a lookup table to the RGB/YUV input video.

        Args:
            c0: set component #0 expression (default "clipval")
            c1: set component #1 expression (default "clipval")
            c2: set component #2 expression (default "clipval")
            c3: set component #3 expression (default "clipval")
            y: set Y expression (default "clipval")
            u: set U expression (default "clipval")
            v: set V expression (default "clipval")
            r: set R expression (default "clipval")
            g: set G expression (default "clipval")
            b: set B expression (default "clipval")
            a: set A expression (default "clipval")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lut", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def lut1d(
        self,
        *,
        file: String = Default(None),
        interp: Int
        | Literal["nearest", "linear", "cosine", "cubic", "spline"]
        | Default = Default("linear"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust colors using a 1D LUT.

        Args:
            file: set 1D LUT file name
            interp: select interpolation mode (from 0 to 4) (default linear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut1d)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lut1d", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "file": file,
                    "interp": interp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def lut2(
        self,
        _srcy: VideoStream,
        *,
        c0: String = Default("x"),
        c1: String = Default("x"),
        c2: String = Default("x"),
        c3: String = Default("x"),
        d: Int = Default("0"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and apply a lookup table from two video inputs.

        Args:
            c0: set component #0 expression (default "x")
            c1: set component #1 expression (default "x")
            c2: set component #2 expression (default "x")
            c3: set component #3 expression (default "x")
            d: set output depth (from 0 to 16) (default 0)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lut2", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _srcy,
            **merge(
                {
                    "c0": c0,
                    "c1": c1,
                    "c2": c2,
                    "c3": c3,
                    "d": d,
                },
                extra_options,
                framesync_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Adjust colors using a 3D LUT.

        Args:
            file: set 3D LUT file name
            clut: when to process CLUT (from 0 to 1) (default all)
            interp: select interpolation mode (from 0 to 4) (default tetrahedral)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut3d)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lut3d", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "file": file,
                    "clut": clut,
                    "interp": interp,
                },
                extra_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and apply a lookup table to the RGB input video.

        Args:
            c0: set component #0 expression (default "clipval")
            c1: set component #1 expression (default "clipval")
            c2: set component #2 expression (default "clipval")
            c3: set component #3 expression (default "clipval")
            y: set Y expression (default "clipval")
            u: set U expression (default "clipval")
            v: set V expression (default "clipval")
            r: set R expression (default "clipval")
            g: set G expression (default "clipval")
            b: set B expression (default "clipval")
            a: set A expression (default "clipval")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lutrgb", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and apply a lookup table to the YUV input video.

        Args:
            c0: set component #0 expression (default "clipval")
            c1: set component #1 expression (default "clipval")
            c2: set component #2 expression (default "clipval")
            c3: set component #3 expression (default "clipval")
            y: set Y expression (default "clipval")
            u: set U expression (default "clipval")
            v: set V expression (default "clipval")
            r: set R expression (default "clipval")
            g: set G expression (default "clipval")
            b: set B expression (default "clipval")
            a: set A expression (default "clipval")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="lutyuv", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskedclamp(
        self,
        _dark: VideoStream,
        _bright: VideoStream,
        *,
        undershoot: Int = Default("0"),
        overshoot: Int = Default("0"),
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Clamp first stream with second stream and third stream.

        Args:
            undershoot: set undershoot (from 0 to 65535) (default 0)
            overshoot: set overshoot (from 0 to 65535) (default 0)
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskedclamp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskedclamp",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _dark,
            _bright,
            **merge(
                {
                    "undershoot": undershoot,
                    "overshoot": overshoot,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskedmax(
        self,
        _filter1: VideoStream,
        _filter2: VideoStream,
        *,
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply filtering with maximum difference of two streams.

        Args:
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskedmax)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskedmax",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _filter1,
            _filter2,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskedmerge(
        self,
        _overlay: VideoStream,
        _mask: VideoStream,
        *,
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Merge first stream with second stream using third stream as mask.

        Args:
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskedmerge)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskedmerge",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _overlay,
            _mask,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskedmin(
        self,
        _filter1: VideoStream,
        _filter2: VideoStream,
        *,
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply filtering with minimum difference of two streams.

        Args:
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskedmin)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskedmin",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _filter1,
            _filter2,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskedthreshold(
        self,
        _reference: VideoStream,
        *,
        threshold: Int = Default("1"),
        planes: Int = Default("15"),
        mode: Int | Literal["abs", "diff"] | Default = Default("abs"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pick pixels comparing absolute difference of two streams with threshold.

        Args:
            threshold: set threshold (from 0 to 65535) (default 1)
            planes: set planes (from 0 to 15) (default 15)
            mode: set mode (from 0 to 1) (default abs)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskedthreshold)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskedthreshold",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _reference,
            **merge(
                {
                    "threshold": threshold,
                    "planes": planes,
                    "mode": mode,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def maskfun(
        self,
        *,
        low: Int = Default("10"),
        high: Int = Default("10"),
        planes: Int = Default("15"),
        fill: Int = Default("0"),
        sum: Int = Default("10"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Create Mask.

        Args:
            low: set low threshold (from 0 to 65535) (default 10)
            high: set high threshold (from 0 to 65535) (default 10)
            planes: set planes (from 0 to 15) (default 15)
            fill: set fill value (from 0 to 65535) (default 0)
            sum: set sum value (from 0 to 65535) (default 10)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#maskfun)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="maskfun", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "low": low,
                    "high": high,
                    "planes": planes,
                    "fill": fill,
                    "sum": sum,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def mcdeint(
        self,
        *,
        mode: Int | Literal["fast", "medium", "slow", "extra_slow"] | Default = Default(
            "fast"
        ),
        parity: Int | Literal["tff", "bff"] | Default = Default("bff"),
        qp: Int = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply motion compensating deinterlacing.

        Args:
            mode: set mode (from 0 to 3) (default fast)
            parity: set the assumed picture field parity (from -1 to 1) (default bff)
            qp: set qp (from INT_MIN to INT_MAX) (default 1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mcdeint)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="mcdeint", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "parity": parity,
                    "qp": qp,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def median(
        self,
        *,
        radius: Int = Default("1"),
        planes: Int = Default("15"),
        radiusV: Int = Default("0"),
        percentile: Float = Default("0.5"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Median filter.

        Args:
            radius: set median radius (from 1 to 127) (default 1)
            planes: set planes to filter (from 0 to 15) (default 15)
            radiusV: set median vertical radius (from 0 to 127) (default 0)
            percentile: set median percentile (from 0 to 1) (default 0.5)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#median)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="median", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "radius": radius,
                    "planes": planes,
                    "radiusV": radiusV,
                    "percentile": percentile,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def mestimate(
        self,
        *,
        method: Int
        | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | Default = Default("esa"),
        mb_size: Int = Default("16"),
        search_param: Int = Default("7"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Generate motion vectors.

        Args:
            method: motion estimation method (from 1 to 9) (default esa)
            mb_size: macroblock size (from 8 to INT_MAX) (default 16)
            search_param: search parameter (from 4 to INT_MAX) (default 7)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mestimate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="mestimate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "method": method,
                    "mb_size": mb_size,
                    "search_param": search_param,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def metadata(
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
        direct: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Manipulate video frame metadata.

        Args:
            mode: set a mode of operation (from 0 to 4) (default select)
            key: set metadata key
            value: set metadata value
            function: function for comparing values (from 0 to 6) (default same_str)
            expr: set expression for expr function
            file: set file where to print metadata information
            direct: reduce buffering when printing to user-set file or pipe (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#metadata_002c-ametadata)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="metadata", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "key": key,
                    "value": value,
                    "function": function,
                    "expr": expr,
                    "file": file,
                    "direct": direct,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def midequalizer(
        self,
        _in1: VideoStream,
        *,
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Midway Equalization.

        Args:
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#midequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="midequalizer",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _in1,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
                timeline_options,
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
        mb_size: Int = Default("16"),
        search_param: Int = Default("32"),
        vsbmc: Int = Default("0"),
        scd: Int | Literal["none", "fdiff"] | Default = Default("fdiff"),
        scd_threshold: Double = Default("10"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Frame rate conversion using Motion Interpolation.

        Args:
            fps: output's frame rate (default "60")
            mi_mode: motion interpolation mode (from 0 to 2) (default mci)
            mc_mode: motion compensation mode (from 0 to 1) (default obmc)
            me_mode: motion estimation mode (from 0 to 1) (default bilat)
            me: motion estimation method (from 1 to 9) (default epzs)
            mb_size: macroblock size (from 4 to 16) (default 16)
            search_param: search parameter (from 4 to INT_MAX) (default 32)
            vsbmc: variable-size block motion compensation (from 0 to 1) (default 0)
            scd: scene change detection method (from 0 to 1) (default fdiff)
            scd_threshold: scene change threshold (from 0 to 100) (default 10)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#minterpolate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="minterpolate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def monochrome(
        self,
        *,
        cb: Float = Default("0"),
        cr: Float = Default("0"),
        size: Float = Default("1"),
        high: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert video to gray using custom color filter.

        Args:
            cb: set the chroma blue spot (from -1 to 1) (default 0)
            cr: set the chroma red spot (from -1 to 1) (default 0)
            size: set the color filter size (from 0.1 to 10) (default 1)
            high: set the highlights strength (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#monochrome)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="monochrome", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "cb": cb,
                    "cr": cr,
                    "size": size,
                    "high": high,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def morpho(
        self,
        _structure: VideoStream,
        *,
        mode: Int
        | Literal["erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"]
        | Default = Default("erode"),
        planes: Int = Default("7"),
        structure: Int | Literal["first", "all"] | Default = Default("all"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Morphological filter.

        Args:
            mode: set morphological transform (from 0 to 6) (default erode)
            planes: set planes to filter (from 0 to 15) (default 7)
            structure: when to process structures (from 0 to 1) (default all)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#morpho)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="morpho",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _structure,
            **merge(
                {
                    "mode": mode,
                    "planes": planes,
                    "structure": structure,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def mpdecimate(
        self,
        *,
        max: Int = Default("0"),
        keep: Int = Default("0"),
        hi: Int = Default("768"),
        lo: Int = Default("320"),
        frac: Float = Default("0.33"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove near-duplicate frames.

        Args:
            max: set the maximum number of consecutive dropped frames (positive), or the minimum interval between dropped frames (negative) (from INT_MIN to INT_MAX) (default 0)
            keep: set the number of similar consecutive frames to be kept before starting to drop similar frames (from 0 to INT_MAX) (default 0)
            hi: set high dropping threshold (from INT_MIN to INT_MAX) (default 768)
            lo: set low dropping threshold (from INT_MIN to INT_MAX) (default 320)
            frac: set fraction dropping threshold (from 0 to 1) (default 0.33)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#mpdecimate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="mpdecimate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "max": max,
                    "keep": keep,
                    "hi": hi,
                    "lo": lo,
                    "frac": frac,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def msad(
        self,
        _reference: VideoStream,
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the MSAD between two video streams.

        Args:
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#msad)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="msad", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _reference,
            **merge(
                {},
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def multiply(
        self,
        _factor: VideoStream,
        *,
        scale: Float = Default("1"),
        offset: Float = Default("0.5"),
        planes: Flags = Default("F"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Multiply first video stream with second video stream.

        Args:
            scale: set scale (from 0 to 9) (default 1)
            offset: set offset (from -1 to 1) (default 0.5)
            planes: set planes (default F)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#multiply)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="multiply",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _factor,
            **merge(
                {
                    "scale": scale,
                    "offset": offset,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def negate(
        self,
        *,
        components: Flags
        | Literal["y", "u", "v", "r", "g", "b", "a"]
        | Default = Default("y+u+v+r+g+b"),
        negate_alpha: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Negate input video.

        Args:
            components: set components to negate (default y+u+v+r+g+b)
            negate_alpha: (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#negate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="negate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "components": components,
                    "negate_alpha": negate_alpha,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def nlmeans(
        self,
        *,
        s: Double = Default("1"),
        p: Int = Default("7"),
        pc: Int = Default("0"),
        r: Int = Default("15"),
        rc: Int = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Non-local means denoiser.

        Args:
            s: denoising strength (from 1 to 30) (default 1)
            p: patch size (from 0 to 99) (default 7)
            pc: patch size for chroma planes (from 0 to 99) (default 0)
            r: research window (from 0 to 99) (default 15)
            rc: research window for chroma planes (from 0 to 99) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#nlmeans)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="nlmeans", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "s": s,
                    "p": p,
                    "pc": pc,
                    "r": r,
                    "rc": rc,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def nlmeans_opencl(
        self,
        *,
        s: Double = Default("1"),
        p: Int = Default("7"),
        pc: Int = Default("0"),
        r: Int = Default("15"),
        rc: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Non-local means denoiser through OpenCL.

        Args:
            s: denoising strength (from 1 to 30) (default 1)
            p: patch size (from 0 to 99) (default 7)
            pc: patch size for chroma planes (from 0 to 99) (default 0)
            r: research window (from 0 to 99) (default 15)
            rc: research window for chroma planes (from 0 to 99) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="nlmeans_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "s": s,
                    "p": p,
                    "pc": pc,
                    "r": r,
                    "rc": rc,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def nlmeans_vulkan(
        self,
        *,
        s: Double = Default("1"),
        p: Int = Default("7"),
        r: Int = Default("15"),
        t: Int = Default("36"),
        s1: Double = Default("1"),
        s2: Double = Default("1"),
        s3: Double = Default("1"),
        s4: Double = Default("1"),
        p1: Int = Default("0"),
        p2: Int = Default("0"),
        p3: Int = Default("0"),
        p4: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Non-local means denoiser (Vulkan).

        Args:
            s: denoising strength for all components (from 1 to 100) (default 1)
            p: patch size for all components (from 0 to 99) (default 7)
            r: research window radius (from 0 to 99) (default 15)
            t: parallelism (from 1 to 168) (default 36)
            s1: denoising strength for component 1 (from 1 to 100) (default 1)
            s2: denoising strength for component 2 (from 1 to 100) (default 1)
            s3: denoising strength for component 3 (from 1 to 100) (default 1)
            s4: denoising strength for component 4 (from 1 to 100) (default 1)
            p1: patch size for component 1 (from 0 to 99) (default 0)
            p2: patch size for component 2 (from 0 to 99) (default 0)
            p3: patch size for component 3 (from 0 to 99) (default 0)
            p4: patch size for component 4 (from 0 to 99) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="nlmeans_vulkan",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "s": s,
                    "p": p,
                    "r": r,
                    "t": t,
                    "s1": s1,
                    "s2": s2,
                    "s3": s3,
                    "s4": s4,
                    "p1": p1,
                    "p2": p2,
                    "p3": p3,
                    "p4": p4,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def nnedi(
        self,
        *,
        weights: String = Default("nnedi3_weights.bin"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        field: Int | Literal["af", "a", "t", "b", "tf", "bf"] | Default = Default("a"),
        planes: Int = Default("7"),
        nsize: Int
        | Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"]
        | Default = Default("s32x4"),
        nns: Int | Literal["n16", "n32", "n64", "n128", "n256"] | Default = Default(
            "n32"
        ),
        qual: Int | Literal["fast", "slow"] | Default = Default("fast"),
        etype: Int | Literal["a", "abs", "s", "mse"] | Default = Default("a"),
        pscrn: Int
        | Literal["none", "original", "new", "new2", "new3"]
        | Default = Default("new"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply neural network edge directed interpolation intra-only deinterlacer.

        Args:
            weights: set weights file (default "nnedi3_weights.bin")
            deint: set which frames to deinterlace (from 0 to 1) (default all)
            field: set mode of operation (from -2 to 3) (default a)
            planes: set which planes to process (from 0 to 15) (default 7)
            nsize: set size of local neighborhood around each pixel, used by the predictor neural network (from 0 to 6) (default s32x4)
            nns: set number of neurons in predictor neural network (from 0 to 4) (default n32)
            qual: set quality (from 1 to 2) (default fast)
            etype: set which set of weights to use in the predictor (from 0 to 1) (default a)
            pscrn: set prescreening (from 0 to 4) (default new)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#nnedi)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="nnedi", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def noformat(
        self,
        *,
        pix_fmts: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

        Args:
            pix_fmts: A '|'-separated list of pixel formats
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#noformat)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="noformat", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "pix_fmts": pix_fmts,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def noise(
        self,
        *,
        all_seed: Int = Default("-1"),
        all_strength: Int = Default("0"),
        all_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c0_seed: Int = Default("-1"),
        c0_strength: Int = Default("0"),
        c0_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c1_seed: Int = Default("-1"),
        c1_strength: Int = Default("0"),
        c1_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c2_seed: Int = Default("-1"),
        c2_strength: Int = Default("0"),
        c2_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        c3_seed: Int = Default("-1"),
        c3_strength: Int = Default("0"),
        c3_flags: Flags | Literal["a", "p", "t", "u"] | Default = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Add noise.

        Args:
            all_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
            all_strength: set component #0 strength (from 0 to 100) (default 0)
            all_flags: set component #0 flags (default 0)
            c0_seed: set component #0 noise seed (from -1 to INT_MAX) (default -1)
            c0_strength: set component #0 strength (from 0 to 100) (default 0)
            c0_flags: set component #0 flags (default 0)
            c1_seed: set component #1 noise seed (from -1 to INT_MAX) (default -1)
            c1_strength: set component #1 strength (from 0 to 100) (default 0)
            c1_flags: set component #1 flags (default 0)
            c2_seed: set component #2 noise seed (from -1 to INT_MAX) (default -1)
            c2_strength: set component #2 strength (from 0 to 100) (default 0)
            c2_flags: set component #2 flags (default 0)
            c3_seed: set component #3 noise seed (from -1 to INT_MAX) (default -1)
            c3_strength: set component #3 strength (from 0 to 100) (default 0)
            c3_flags: set component #3 flags (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#noise)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="noise", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def normalize(
        self,
        *,
        blackpt: Color = Default("black"),
        whitept: Color = Default("white"),
        smoothing: Int = Default("0"),
        independence: Float = Default("1"),
        strength: Float = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Normalize RGB video.

        Args:
            blackpt: output color to which darkest input color is mapped (default "black")
            whitept: output color to which brightest input color is mapped (default "white")
            smoothing: amount of temporal smoothing of the input range, to reduce flicker (from 0 to 2.68435e+08) (default 0)
            independence: proportion of independent to linked channel normalization (from 0 to 1) (default 1)
            strength: strength of filter, from no effect to full normalization (from 0 to 1) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#normalize)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="normalize", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "blackpt": blackpt,
                    "whitept": whitept,
                    "smoothing": smoothing,
                    "independence": independence,
                    "strength": strength,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def null(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pass the source unchanged to the output.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#null)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="null", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def oscilloscope(
        self,
        *,
        x: Float = Default("0.5"),
        y: Float = Default("0.5"),
        s: Float = Default("0.8"),
        t: Float = Default("0.5"),
        o: Float = Default("0.8"),
        tx: Float = Default("0.5"),
        ty: Float = Default("0.9"),
        tw: Float = Default("0.8"),
        th: Float = Default("0.3"),
        c: Int = Default("7"),
        g: Boolean = Default("true"),
        st: Boolean = Default("true"),
        sc: Boolean = Default("true"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        2D Video Oscilloscope.

        Args:
            x: set scope x position (from 0 to 1) (default 0.5)
            y: set scope y position (from 0 to 1) (default 0.5)
            s: set scope size (from 0 to 1) (default 0.8)
            t: set scope tilt (from 0 to 1) (default 0.5)
            o: set trace opacity (from 0 to 1) (default 0.8)
            tx: set trace x position (from 0 to 1) (default 0.5)
            ty: set trace y position (from 0 to 1) (default 0.9)
            tw: set trace width (from 0.1 to 1) (default 0.8)
            th: set trace height (from 0.1 to 1) (default 0.3)
            c: set components to trace (from 0 to 15) (default 7)
            g: draw trace grid (default true)
            st: draw statistics (default true)
            sc: draw scope (default true)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#oscilloscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="oscilloscope", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def overlay(
        self,
        _overlay: VideoStream,
        *,
        x: String = Default("0"),
        y: String = Default("0"),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default(
            "repeat"
        ),
        eval: Int | Literal["init", "frame"] | Default = Default("frame"),
        shortest: Boolean = Default("false"),
        format: Int
        | Literal[
            "yuv420",
            "yuv420p10",
            "yuv422",
            "yuv422p10",
            "yuv444",
            "yuv444p10",
            "rgb",
            "gbrp",
            "auto",
        ]
        | Default = Default("yuv420"),
        repeatlast: Boolean = Default("true"),
        alpha: Int | Literal["straight", "premultiplied"] | Default = Default(
            "straight"
        ),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Overlay a video source on top of the input.

        Args:
            x: set the x expression (default "0")
            y: set the y expression (default "0")
            eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
            eval: specify when to evaluate expressions (from 0 to 1) (default frame)
            shortest: force termination when the shortest input terminates (default false)
            format: set output format (from 0 to 8) (default yuv420)
            repeatlast: repeat overlay of the last overlay frame (default true)
            alpha: alpha format (from 0 to 1) (default straight)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#overlay)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="overlay",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _overlay,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "eof_action": eof_action,
                    "eval": eval,
                    "shortest": shortest,
                    "format": format,
                    "repeatlast": repeatlast,
                    "alpha": alpha,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def overlay_opencl(
        self,
        _overlay: VideoStream,
        *,
        x: Int = Default("0"),
        y: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Overlay one video on top of another.

        Args:
            x: Overlay x position (from 0 to INT_MAX) (default 0)
            y: Overlay y position (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#overlay_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="overlay_opencl",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _overlay,
            **merge(
                {
                    "x": x,
                    "y": y,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def overlay_vaapi(
        self,
        _overlay: VideoStream,
        *,
        x: String = Default("0"),
        y: String = Default("0"),
        w: String = Default("overlay_iw"),
        h: String = Default("overlay_ih*w/overlay_iw"),
        alpha: Float = Default("1"),
        eof_action: Int | Literal["repeat", "endall", "pass"] | Default = Default(
            "repeat"
        ),
        shortest: Boolean = Default("false"),
        repeatlast: Boolean = Default("true"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Overlay one video on top of another.

        Args:
            x: Overlay x position (default "0")
            y: Overlay y position (default "0")
            w: Overlay width (default "overlay_iw")
            h: Overlay height (default "overlay_ih*w/overlay_iw")
            alpha: Overlay global alpha (from 0 to 1) (default 1)
            eof_action: Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
            shortest: force termination when the shortest input terminates (default false)
            repeatlast: repeat overlay of the last overlay frame (default true)
            framesync_options: Framesync options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvaapi)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="overlay_vaapi",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _overlay,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "alpha": alpha,
                    "eof_action": eof_action,
                    "shortest": shortest,
                    "repeatlast": repeatlast,
                },
                extra_options,
                framesync_options,
            ),
        )
        return filter_node.video(0)

    def overlay_vulkan(
        self,
        _overlay: VideoStream,
        *,
        x: Int = Default("0"),
        y: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Overlay a source on top of another.

        Args:
            x: Set horizontal offset (from 0 to INT_MAX) (default 0)
            y: Set vertical offset (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#overlay_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="overlay_vulkan",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _overlay,
            **merge(
                {
                    "x": x,
                    "y": y,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def owdenoise(
        self,
        *,
        depth: Int = Default("8"),
        luma_strength: Double = Default("1"),
        chroma_strength: Double = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Denoise using wavelets.

        Args:
            depth: set depth (from 8 to 16) (default 8)
            luma_strength: set luma strength (from 0 to 1000) (default 1)
            chroma_strength: set chroma strength (from 0 to 1000) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#owdenoise)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="owdenoise", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "depth": depth,
                    "luma_strength": luma_strength,
                    "chroma_strength": chroma_strength,
                },
                extra_options,
                timeline_options,
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
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pad the input video.

        Args:
            width: set the pad area width expression (default "iw")
            height: set the pad area height expression (default "ih")
            x: set the x offset expression for the input image position (default "0")
            y: set the y offset expression for the input image position (default "0")
            color: set the color of the padded area border (default "black")
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            aspect: pad to fit an aspect instead of a resolution (from 0 to DBL_MAX) (default 0/1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pad)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pad", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "width": width,
                    "height": height,
                    "x": x,
                    "y": y,
                    "color": color,
                    "eval": eval,
                    "aspect": aspect,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def pad_opencl(
        self,
        *,
        width: String = Default("iw"),
        height: String = Default("ih"),
        x: String = Default("0"),
        y: String = Default("0"),
        color: Color = Default("black"),
        aspect: Rational = Default("0/1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pad the input video.

        Args:
            width: set the pad area width (default "iw")
            height: set the pad area height (default "ih")
            x: set the x offset for the input image position (default "0")
            y: set the y offset for the input image position (default "0")
            color: set the color of the padded area border (default "black")
            aspect: pad to fit an aspect instead of a resolution (from 0 to 32767) (default 0/1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pad_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pad_opencl", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "width": width,
                    "height": height,
                    "x": x,
                    "y": y,
                    "color": color,
                    "aspect": aspect,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def palettegen(
        self,
        *,
        max_colors: Int = Default("256"),
        reserve_transparent: Boolean = Default("true"),
        transparency_color: Color = Default("lime"),
        stats_mode: Int | Literal["full", "diff", "single"] | Default = Default("full"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Find the optimal palette for a given stream.

        Args:
            max_colors: set the maximum number of colors to use in the palette (from 2 to 256) (default 256)
            reserve_transparent: reserve a palette entry for transparency (default true)
            transparency_color: set a background color for transparency (default "lime")
            stats_mode: set statistics mode (from 0 to 2) (default full)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#palettegen)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="palettegen", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "max_colors": max_colors,
                    "reserve_transparent": reserve_transparent,
                    "transparency_color": transparency_color,
                    "stats_mode": stats_mode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def paletteuse(
        self,
        _palette: VideoStream,
        *,
        dither: Int
        | Literal[
            "bayer",
            "heckbert",
            "floyd_steinberg",
            "sierra2",
            "sierra2_4a",
            "sierra3",
            "burkes",
            "atkinson",
        ]
        | Default = Default("sierra2_4a"),
        bayer_scale: Int = Default("2"),
        diff_mode: Int | Literal["rectangle"] | Default = Default("0"),
        new: Boolean = Default("false"),
        alpha_threshold: Int = Default("128"),
        debug_kdtree: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Use a palette to downsample an input video stream.

        Args:
            dither: select dithering mode (from 0 to 8) (default sierra2_4a)
            bayer_scale: set scale for bayer dithering (from 0 to 5) (default 2)
            diff_mode: set frame difference mode (from 0 to 1) (default 0)
            new: take new palette for each output frame (default false)
            alpha_threshold: set the alpha threshold for transparency (from 0 to 255) (default 128)
            debug_kdtree: save Graphviz graph of the kdtree in specified file
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#paletteuse)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="paletteuse",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _palette,
            **merge(
                {
                    "dither": dither,
                    "bayer_scale": bayer_scale,
                    "diff_mode": diff_mode,
                    "new": new,
                    "alpha_threshold": alpha_threshold,
                    "debug_kdtree": debug_kdtree,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def perms(
        self,
        *,
        mode: Int | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default(
            "none"
        ),
        seed: Int64 = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set permissions for the output video frame.

        Args:
            mode: select permissions mode (from 0 to 4) (default none)
            seed: set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="perms", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "seed": seed,
                },
                extra_options,
                timeline_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Correct the perspective of video.

        Args:
            x0: set top left x coordinate (default "0")
            y0: set top left y coordinate (default "0")
            x1: set top right x coordinate (default "W")
            y1: set top right y coordinate (default "0")
            x2: set bottom left x coordinate (default "0")
            y2: set bottom left y coordinate (default "H")
            x3: set bottom right x coordinate (default "W")
            y3: set bottom right y coordinate (default "H")
            interpolation: set interpolation (from 0 to 1) (default linear)
            sense: specify the sense of the coordinates (from 0 to 1) (default source)
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#perspective)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="perspective", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def phase(
        self,
        *,
        mode: Int
        | Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"]
        | Default = Default("A"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Phase shift fields.

        Args:
            mode: set phase mode (from 0 to 8) (default A)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#phase)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="phase", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def photosensitivity(
        self,
        *,
        frames: Int = Default("30"),
        threshold: Float = Default("1"),
        skip: Int = Default("1"),
        bypass: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Filter out photosensitive epilepsy seizure-inducing flashes.

        Args:
            frames: set how many frames to use (from 2 to 240) (default 30)
            threshold: set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX) (default 1)
            skip: set pixels to skip when sampling frames (from 1 to 1024) (default 1)
            bypass: leave frames unchanged (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#photosensitivity)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="photosensitivity",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "frames": frames,
                    "threshold": threshold,
                    "skip": skip,
                    "bypass": bypass,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def pixdesctest(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Test pixel format definitions.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pixdesctest)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pixdesctest", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def pixelize(
        self,
        *,
        width: Int = Default("16"),
        height: Int = Default("16"),
        mode: Int | Literal["avg", "min", "max"] | Default = Default("avg"),
        planes: Flags = Default("F"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pixelize video.

        Args:
            width: set block width (from 1 to 1024) (default 16)
            height: set block height (from 1 to 1024) (default 16)
            mode: set the pixelize mode (from 0 to 2) (default avg)
            planes: set what planes to filter (default F)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pixelize)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pixelize", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "width": width,
                    "height": height,
                    "mode": mode,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def pixscope(
        self,
        *,
        x: Float = Default("0.5"),
        y: Float = Default("0.5"),
        w: Int = Default("7"),
        h: Int = Default("7"),
        o: Float = Default("0.5"),
        wx: Float = Default("-1"),
        wy: Float = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pixel data analysis.

        Args:
            x: set scope x offset (from 0 to 1) (default 0.5)
            y: set scope y offset (from 0 to 1) (default 0.5)
            w: set scope width (from 1 to 80) (default 7)
            h: set scope height (from 1 to 80) (default 7)
            o: set window opacity (from 0 to 1) (default 0.5)
            wx: set window x offset (from -1 to 1) (default -1)
            wy: set window y offset (from -1 to 1) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pixscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pixscope", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "o": o,
                    "wx": wx,
                    "wy": wy,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def pp7(
        self,
        *,
        qp: Int = Default("0"),
        mode: Int | Literal["hard", "soft", "medium"] | Default = Default("medium"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Postprocessing 7 filter.

        Args:
            qp: force a constant quantizer parameter (from 0 to 64) (default 0)
            mode: set thresholding mode (from 0 to 2) (default medium)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pp7)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pp7", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "qp": qp,
                    "mode": mode,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def prewitt(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply prewitt operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#prewitt)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="prewitt", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def prewitt_opencl(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply prewitt operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#prewitt_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="prewitt_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
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
        index: Int = Default("0"),
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
            "cool",
            "heat",
            "fiery",
            "blues",
            "green",
            "helix",
        ]
        | Default = Default("none"),
        opacity: Float = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Make pseudocolored video frames.

        Args:
            c0: set component #0 expression (default "val")
            c1: set component #1 expression (default "val")
            c2: set component #2 expression (default "val")
            c3: set component #3 expression (default "val")
            index: set component as base (from 0 to 3) (default 0)
            preset: set preset (from -1 to 20) (default none)
            opacity: set pseudocolor opacity (from 0 to 1) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pseudocolor)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pseudocolor", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "c0": c0,
                    "c1": c1,
                    "c2": c2,
                    "c3": c3,
                    "index": index,
                    "preset": preset,
                    "opacity": opacity,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def psnr(
        self,
        _reference: VideoStream,
        *,
        stats_file: String = Default(None),
        stats_version: Int = Default("1"),
        output_max: Boolean = Default("false"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the PSNR between two video streams.

        Args:
            stats_file: Set file where to store per-frame difference information
            stats_version: Set the format version for the stats file. (from 1 to 2) (default 1)
            output_max: Add raw stats (max values) to the output log. (default false)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#psnr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="psnr", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _reference,
            **merge(
                {
                    "stats_file": stats_file,
                    "stats_version": stats_version,
                    "output_max": output_max,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def pullup(
        self,
        *,
        jl: Int = Default("1"),
        jr: Int = Default("1"),
        jt: Int = Default("4"),
        jb: Int = Default("4"),
        sb: Boolean = Default("false"),
        mp: Int | Literal["y", "u", "v"] | Default = Default("y"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pullup from field sequence to frames.

        Args:
            jl: set left junk size (from 0 to INT_MAX) (default 1)
            jr: set right junk size (from 0 to INT_MAX) (default 1)
            jt: set top junk size (from 1 to INT_MAX) (default 4)
            jb: set bottom junk size (from 1 to INT_MAX) (default 4)
            sb: set strict breaks (default false)
            mp: set metric plane (from 0 to 2) (default y)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#pullup)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="pullup", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "jl": jl,
                    "jr": jr,
                    "jt": jt,
                    "jb": jb,
                    "sb": sb,
                    "mp": mp,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def qp(
        self,
        *,
        qp: String = Default(None),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Change video quantization parameters.

        Args:
            qp: set qp expression
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#qp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="qp", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "qp": qp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def random(
        self,
        *,
        frames: Int = Default("30"),
        seed: Int64 = Default("-1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Return random frames.

        Args:
            frames: set number of frames in cache (from 2 to 512) (default 30)
            seed: set the seed (from -1 to UINT32_MAX) (default -1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#random)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="random", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "frames": frames,
                    "seed": seed,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def readeia608(
        self,
        *,
        scan_min: Int = Default("0"),
        scan_max: Int = Default("29"),
        spw: Float = Default("0.27"),
        chp: Boolean = Default("false"),
        lp: Boolean = Default("true"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

        Args:
            scan_min: set from which line to scan for codes (from 0 to INT_MAX) (default 0)
            scan_max: set to which line to scan for codes (from 0 to INT_MAX) (default 29)
            spw: set ratio of width reserved for sync code detection (from 0.1 to 0.7) (default 0.27)
            chp: check and apply parity bit (default false)
            lp: lowpass line prior to processing (default true)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#readeia608)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="readeia608", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "scan_min": scan_min,
                    "scan_max": scan_max,
                    "spw": spw,
                    "chp": chp,
                    "lp": lp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def readvitc(
        self,
        *,
        scan_max: Int = Default("45"),
        thr_b: Double = Default("0.2"),
        thr_w: Double = Default("0.6"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Read vertical interval timecode and write it to frame metadata.

        Args:
            scan_max: maximum line numbers to scan for VITC data (from -1 to INT_MAX) (default 45)
            thr_b: black color threshold (from 0 to 1) (default 0.2)
            thr_w: white color threshold (from 0 to 1) (default 0.6)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#readvitc)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="readvitc", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "scan_max": scan_max,
                    "thr_b": thr_b,
                    "thr_w": thr_w,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def realtime(
        self,
        *,
        limit: Duration = Default("2"),
        speed: Double = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Slow down filtering to match realtime.

        Args:
            limit: sleep time limit (default 2)
            speed: speed factor (from DBL_MIN to DBL_MAX) (default 1)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="realtime", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "limit": limit,
                    "speed": speed,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def remap(
        self,
        _xmap: VideoStream,
        _ymap: VideoStream,
        *,
        format: Int | Literal["color", "gray"] | Default = Default("color"),
        fill: Color = Default("black"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remap pixels.

        Args:
            format: set output format (from 0 to 1) (default color)
            fill: set the color of the unmapped pixels (default "black")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#remap)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="remap",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _xmap,
            _ymap,
            **merge(
                {
                    "format": format,
                    "fill": fill,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def remap_opencl(
        self,
        _xmap: VideoStream,
        _ymap: VideoStream,
        *,
        interp: Int | Literal["near", "linear"] | Default = Default("linear"),
        fill: Color = Default("black"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remap pixels using OpenCL.

        Args:
            interp: set interpolation method (from 0 to 1) (default linear)
            fill: set the color of the unmapped pixels (default "black")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#remap_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="remap_opencl",
                typings_input=("video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _xmap,
            _ymap,
            **merge(
                {
                    "interp": interp,
                    "fill": fill,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def removegrain(
        self,
        *,
        m0: Int = Default("0"),
        m1: Int = Default("0"),
        m2: Int = Default("0"),
        m3: Int = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove grain.

        Args:
            m0: set mode for 1st plane (from 0 to 24) (default 0)
            m1: set mode for 2nd plane (from 0 to 24) (default 0)
            m2: set mode for 3rd plane (from 0 to 24) (default 0)
            m3: set mode for 4th plane (from 0 to 24) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#removegrain)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="removegrain", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "m0": m0,
                    "m1": m1,
                    "m2": m2,
                    "m3": m3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def removelogo(
        self,
        *,
        filename: String = Default(None),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Remove a TV logo based on a mask image.

        Args:
            filename: set bitmap filename
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#removelogo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="removelogo", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filename": filename,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def repeatfields(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Hard repeat fields based on MPEG repeat field flag.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#repeatfields)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="repeatfields", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def reverse(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Reverse a clip.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#reverse)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="reverse", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def rgbashift(
        self,
        *,
        rh: Int = Default("0"),
        rv: Int = Default("0"),
        gh: Int = Default("0"),
        gv: Int = Default("0"),
        bh: Int = Default("0"),
        bv: Int = Default("0"),
        ah: Int = Default("0"),
        av: Int = Default("0"),
        edge: Int | Literal["smear", "wrap"] | Default = Default("smear"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shift RGBA.

        Args:
            rh: shift red horizontally (from -255 to 255) (default 0)
            rv: shift red vertically (from -255 to 255) (default 0)
            gh: shift green horizontally (from -255 to 255) (default 0)
            gv: shift green vertically (from -255 to 255) (default 0)
            bh: shift blue horizontally (from -255 to 255) (default 0)
            bv: shift blue vertically (from -255 to 255) (default 0)
            ah: shift alpha horizontally (from -255 to 255) (default 0)
            av: shift alpha vertically (from -255 to 255) (default 0)
            edge: set edge operation (from 0 to 1) (default smear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#rgbashift)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="rgbashift", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def roberts(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply roberts cross operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#roberts)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="roberts", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def roberts_opencl(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply roberts operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#roberts_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="roberts_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
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
        bilinear: Boolean = Default("true"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Rotate the input image.

        Args:
            angle: set angle (in radians) (default "0")
            out_w: set output width expression (default "iw")
            out_h: set output height expression (default "ih")
            fillcolor: set background fill color (default "black")
            bilinear: use bilinear interpolation (default true)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#rotate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="rotate", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "angle": angle,
                    "out_w": out_w,
                    "out_h": out_h,
                    "fillcolor": fillcolor,
                    "bilinear": bilinear,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def sab(
        self,
        *,
        luma_radius: Float = Default("1"),
        luma_pre_filter_radius: Float = Default("1"),
        luma_strength: Float = Default("1"),
        chroma_radius: Float = Default("-0.9"),
        chroma_pre_filter_radius: Float = Default("-0.9"),
        chroma_strength: Float = Default("-0.9"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply shape adaptive blur.

        Args:
            luma_radius: set luma radius (from 0.1 to 4) (default 1)
            luma_pre_filter_radius: set luma pre-filter radius (from 0.1 to 2) (default 1)
            luma_strength: set luma strength (from 0.1 to 100) (default 1)
            chroma_radius: set chroma radius (from -0.9 to 4) (default -0.9)
            chroma_pre_filter_radius: set chroma pre-filter radius (from -0.9 to 2) (default -0.9)
            chroma_strength: set chroma strength (from -0.9 to 100) (default -0.9)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sab)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sab", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "luma_radius": luma_radius,
                    "luma_pre_filter_radius": luma_pre_filter_radius,
                    "luma_strength": luma_strength,
                    "chroma_radius": chroma_radius,
                    "chroma_pre_filter_radius": chroma_pre_filter_radius,
                    "chroma_strength": chroma_strength,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def scale(
        self,
        *,
        w: String = Default(None),
        h: String = Default(None),
        flags: String = Default(""),
        interl: Boolean = Default("false"),
        in_color_matrix: String
        | Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | Default = Default("auto"),
        out_color_matrix: String
        | Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | Default = Default(None),
        in_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        out_range: Int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("auto"),
        in_v_chr_pos: Int = Default("-513"),
        in_h_chr_pos: Int = Default("-513"),
        out_v_chr_pos: Int = Default("-513"),
        out_h_chr_pos: Int = Default("-513"),
        force_original_aspect_ratio: Int
        | Literal["disable", "decrease", "increase"]
        | Default = Default("disable"),
        force_divisible_by: Int = Default("1"),
        param0: Double = Default("DBL_MAX"),
        param1: Double = Default("DBL_MAX"),
        eval: Int | Literal["init", "frame"] | Default = Default("init"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scale the input video size and/or convert the image format.

        Args:
            w: Output video width
            h: Output video height
            flags: Flags to pass to libswscale (default "")
            interl: set interlacing (default false)
            in_color_matrix: set input YCbCr type (default "auto")
            out_color_matrix: set output YCbCr type
            in_range: set input color range (from 0 to 2) (default auto)
            out_range: set output color range (from 0 to 2) (default auto)
            in_v_chr_pos: input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
            in_h_chr_pos: input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
            out_v_chr_pos: output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
            out_h_chr_pos: output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
            force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
            force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
            param0: Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
            param1: Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#scale)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="scale", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def scdet(
        self,
        *,
        threshold: Double = Default("10"),
        sc_pass: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Detect video scene change.

        Args:
            threshold: set scene change detect threshold (from 0 to 100) (default 10)
            sc_pass: Set the flag to pass scene change frames (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#scdet)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="scdet", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "threshold": threshold,
                    "sc_pass": sc_pass,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def scharr(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply scharr operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#scharr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="scharr", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def scroll(
        self,
        *,
        horizontal: Float = Default("0"),
        vertical: Float = Default("0"),
        hpos: Float = Default("0"),
        vpos: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scroll input video.

        Args:
            horizontal: set the horizontal scrolling speed (from -1 to 1) (default 0)
            vertical: set the vertical scrolling speed (from -1 to 1) (default 0)
            hpos: set initial horizontal position (from 0 to 1) (default 0)
            vpos: set initial vertical position (from 0 to 1) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#scroll)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="scroll", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "horizontal": horizontal,
                    "vertical": vertical,
                    "hpos": hpos,
                    "vpos": vpos,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def segment(
        self,
        *,
        timestamps: String = Default(None),
        frames: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> FilterNode:
        """

        Segment video stream.

        Args:
            timestamps: timestamps of input at which to split input
            frames: frames at which to split input
            extra_options: Extra options for the filter

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="segment",
                typings_input=("video",),
                typings_output="[StreamType.video] * len((str(timestamps or frames)).split('|'))",
            ),
            self,
            **merge(
                {
                    "timestamps": timestamps,
                    "frames": frames,
                },
                extra_options,
            ),
        )

        return filter_node

    def select(
        self,
        *,
        expr: String = Default("1"),
        outputs: Int = Default("1"),
        extra_options: dict[str, Any] | None = None,
    ) -> FilterNode:
        """

        Select video frames to pass in output.

        Args:
            expr: set an expression to use for selecting frames (default "1")
            outputs: set the number of outputs (from 1 to INT_MAX) (default 1)
            extra_options: Extra options for the filter

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="select",
                typings_input=("video",),
                typings_output="[StreamType.video] * int(outputs)",
            ),
            self,
            **merge(
                {
                    "expr": expr,
                    "outputs": outputs,
                },
                extra_options,
            ),
        )

        return filter_node

    def selectivecolor(
        self,
        *,
        correction_method: Int | Literal["absolute", "relative"] | Default = Default(
            "absolute"
        ),
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply CMYK adjustments to specific color ranges.

        Args:
            correction_method: select correction method (from 0 to 1) (default absolute)
            reds: adjust red regions
            yellows: adjust yellow regions
            greens: adjust green regions
            cyans: adjust cyan regions
            blues: adjust blue regions
            magentas: adjust magenta regions
            whites: adjust white regions
            neutrals: adjust neutral regions
            blacks: adjust black regions
            psfile: set Photoshop selectivecolor file name
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#selectivecolor)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="selectivecolor",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def sendcmd(
        self,
        *,
        commands: String = Default(None),
        filename: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Send commands to filters.

        Args:
            commands: set commands
            filename: set commands file
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sendcmd", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "commands": commands,
                    "filename": filename,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def separatefields(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Split input video frames into fields.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#separatefields)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="separatefields",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setdar(
        self,
        *,
        dar: String = Default("0"),
        max: Int = Default("100"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set the frame display aspect ratio.

        Args:
            dar: set display aspect ratio (default "0")
            max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setdar", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "dar": dar,
                    "max": max,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setfield(
        self,
        *,
        mode: Int | Literal["auto", "bff", "tff", "prog"] | Default = Default("auto"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Force field for the output video frame.

        Args:
            mode: select interlace mode (from -1 to 2) (default auto)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setfield)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setfield", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setparams(
        self,
        *,
        field_mode: Int | Literal["auto", "bff", "tff", "prog"] | Default = Default(
            "auto"
        ),
        range: Int
        | Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
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
            "jedec-p22",
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
            "iec61966-2-4",
            "bt1361e",
            "iec61966-2-1",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
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
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | Default = Default("auto"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Force field, or color property for the output video frame.

        Args:
            field_mode: select interlace mode (from -1 to 2) (default auto)
            range: select color range (from -1 to 2) (default auto)
            color_primaries: select color primaries (from -1 to 22) (default auto)
            color_trc: select color transfer (from -1 to 18) (default auto)
            colorspace: select colorspace (from -1 to 14) (default auto)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setparams)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setparams", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "field_mode": field_mode,
                    "range": range,
                    "color_primaries": color_primaries,
                    "color_trc": color_trc,
                    "colorspace": colorspace,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setpts(
        self,
        *,
        expr: String = Default("PTS"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set PTS for the output video frame.

        Args:
            expr: Expression determining the frame timestamp (default "PTS")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setpts", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "expr": expr,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setrange(
        self,
        *,
        range: Int
        | Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
        | Default = Default("auto"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Force color range for the output video frame.

        Args:
            range: select color range (from -1 to 2) (default auto)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setrange)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setrange", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "range": range,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def setsar(
        self,
        *,
        sar: String = Default("0"),
        max: Int = Default("100"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set the pixel sample aspect ratio.

        Args:
            sar: set sample (pixel) aspect ratio (default "0")
            max: set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="setsar", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "sar": sar,
                    "max": max,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def settb(
        self,
        *,
        expr: String = Default("intb"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Set timebase for the video output link.

        Args:
            expr: set expression determining the output timebase (default "intb")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="settb", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "expr": expr,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def shear(
        self,
        *,
        shx: Float = Default("0"),
        shy: Float = Default("0"),
        fillcolor: String = Default("black"),
        interp: Int | Literal["nearest", "bilinear"] | Default = Default("bilinear"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shear transform the input image.

        Args:
            shx: set x shear factor (from -2 to 2) (default 0)
            shy: set y shear factor (from -2 to 2) (default 0)
            fillcolor: set background fill color (default "black")
            interp: set interpolation (from 0 to 1) (default bilinear)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#shear)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="shear", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "shx": shx,
                    "shy": shy,
                    "fillcolor": fillcolor,
                    "interp": interp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def showinfo(
        self,
        *,
        checksum: Boolean = Default("true"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Show textual information for each video frame.

        Args:
            checksum: calculate checksums (default true)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showinfo)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showinfo", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "checksum": checksum,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def showpalette(
        self,
        *,
        s: Int = Default("30"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Display frame palette.

        Args:
            s: set pixel box size (from 1 to 100) (default 30)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#showpalette)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="showpalette", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "s": s,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def shuffleframes(
        self,
        *,
        mapping: String = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shuffle video frames.

        Args:
            mapping: set destination indexes of input frames (default "0")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#shuffleframes)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="shuffleframes",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "mapping": mapping,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def shufflepixels(
        self,
        *,
        direction: Int | Literal["forward", "inverse"] | Default = Default("forward"),
        mode: Int | Literal["horizontal", "vertical", "block"] | Default = Default(
            "horizontal"
        ),
        width: Int = Default("10"),
        height: Int = Default("10"),
        seed: Int64 = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shuffle video pixels.

        Args:
            direction: set shuffle direction (from 0 to 1) (default forward)
            mode: set shuffle mode (from 0 to 2) (default horizontal)
            width: set block width (from 1 to 8000) (default 10)
            height: set block height (from 1 to 8000) (default 10)
            seed: set random seed (from -1 to UINT32_MAX) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#shufflepixels)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="shufflepixels",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "direction": direction,
                    "mode": mode,
                    "width": width,
                    "height": height,
                    "seed": seed,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def shuffleplanes(
        self,
        *,
        map0: Int = Default("0"),
        map1: Int = Default("1"),
        map2: Int = Default("2"),
        map3: Int = Default("3"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Shuffle video planes.

        Args:
            map0: Index of the input plane to be used as the first output plane (from 0 to 3) (default 0)
            map1: Index of the input plane to be used as the second output plane (from 0 to 3) (default 1)
            map2: Index of the input plane to be used as the third output plane (from 0 to 3) (default 2)
            map3: Index of the input plane to be used as the fourth output plane (from 0 to 3) (default 3)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#shuffleplanes)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="shuffleplanes",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "map0": map0,
                    "map1": map1,
                    "map2": map2,
                    "map3": map3,
                },
                extra_options,
                timeline_options,
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
        | Default = Default("-1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Manipulate video frame side data.

        Args:
            mode: set a mode of operation (from 0 to 1) (default select)
            type: set side data type (from -1 to INT_MAX) (default -1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sidedata", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "type": type,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def signalstats(
        self,
        *,
        stat: Flags | Literal["tout", "vrep", "brng"] | Default = Default("0"),
        out: Int | Literal["tout", "vrep", "brng"] | Default = Default("-1"),
        c: Color = Default("yellow"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Generate statistics from video analysis.

        Args:
            stat: set statistics filters (default 0)
            out: set video filter (from -1 to 2) (default -1)
            c: set highlight color (default "yellow")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#signalstats)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="signalstats", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "stat": stat,
                    "out": out,
                    "c": c,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def siti(
        self,
        *,
        print_summary: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate spatial information (SI) and temporal information (TI).

        Args:
            print_summary: Print summary showing average values (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#siti)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="siti", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "print_summary": print_summary,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def smartblur(
        self,
        *,
        luma_radius: Float = Default("1"),
        luma_strength: Float = Default("1"),
        luma_threshold: Int = Default("0"),
        chroma_radius: Float = Default("-0.9"),
        chroma_strength: Float = Default("-2"),
        chroma_threshold: Int = Default("-31"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blur the input video without impacting the outlines.

        Args:
            luma_radius: set luma radius (from 0.1 to 5) (default 1)
            luma_strength: set luma strength (from -1 to 1) (default 1)
            luma_threshold: set luma threshold (from -30 to 30) (default 0)
            chroma_radius: set chroma radius (from -0.9 to 5) (default -0.9)
            chroma_strength: set chroma strength (from -2 to 1) (default -2)
            chroma_threshold: set chroma threshold (from -31 to 30) (default -31)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#smartblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="smartblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "luma_radius": luma_radius,
                    "luma_strength": luma_strength,
                    "luma_threshold": luma_threshold,
                    "chroma_radius": chroma_radius,
                    "chroma_strength": chroma_strength,
                    "chroma_threshold": chroma_threshold,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def sobel(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply sobel operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sobel)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sobel", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def sobel_opencl(
        self,
        *,
        planes: Int = Default("15"),
        scale: Float = Default("1"),
        delta: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply sobel operator.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            scale: set scale (from 0 to 65535) (default 1)
            delta: set delta (from -65535 to 65535) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sobel_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sobel_opencl", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "planes": planes,
                    "scale": scale,
                    "delta": delta,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def spectrumsynth(
        self,
        _phase: VideoStream,
        *,
        sample_rate: Int = Default("44100"),
        channels: Int = Default("1"),
        scale: Int | Literal["lin", "log"] | Default = Default("log"),
        slide: Int
        | Literal["replace", "scroll", "fullframe", "rscroll"]
        | Default = Default("fullframe"),
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
        overlap: Float = Default("1"),
        orientation: Int | Literal["vertical", "horizontal"] | Default = Default(
            "vertical"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> AudioStream:
        """

        Convert input spectrum videos to audio output.

        Args:
            sample_rate: set sample rate (from 15 to INT_MAX) (default 44100)
            channels: set channels (from 1 to 8) (default 1)
            scale: set input amplitude scale (from 0 to 1) (default log)
            slide: set input sliding mode (from 0 to 3) (default fullframe)
            win_func: set window function (from 0 to 20) (default rect)
            overlap: set window overlap (from 0 to 1) (default 1)
            orientation: set orientation (from 0 to 1) (default vertical)
            extra_options: Extra options for the filter

        Returns:
            default: the audio stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#spectrumsynth)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="spectrumsynth",
                typings_input=("video", "video"),
                typings_output=("audio",),
            ),
            self,
            _phase,
            **merge(
                {
                    "sample_rate": sample_rate,
                    "channels": channels,
                    "scale": scale,
                    "slide": slide,
                    "win_func": win_func,
                    "overlap": overlap,
                    "orientation": orientation,
                },
                extra_options,
            ),
        )
        return filter_node.audio(0)

    def split(
        self,
        *,
        outputs: Int = Default("2"),
        extra_options: dict[str, Any] | None = None,
    ) -> FilterNode:
        """

        Pass on the input to N video outputs.

        Args:
            outputs: set number of outputs (from 1 to INT_MAX) (default 2)
            extra_options: Extra options for the filter

        Returns:
            filter_node: the filter node


        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="split",
                typings_input=("video",),
                typings_output="[StreamType.video] * int(outputs)",
            ),
            self,
            **merge(
                {
                    "outputs": outputs,
                },
                extra_options,
            ),
        )

        return filter_node

    def spp(
        self,
        *,
        quality: Int = Default("3"),
        qp: Int = Default("0"),
        mode: Int | Literal["hard", "soft"] | Default = Default("hard"),
        use_bframe_qp: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply a simple post processing filter.

        Args:
            quality: set quality (from 0 to 6) (default 3)
            qp: force a constant quantizer parameter (from 0 to 63) (default 0)
            mode: set thresholding mode (from 0 to 1) (default hard)
            use_bframe_qp: use B-frames' QP (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#spp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="spp", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "quality": quality,
                    "qp": qp,
                    "mode": mode,
                    "use_bframe_qp": use_bframe_qp,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def sr(
        self,
        *,
        dnn_backend: Int = Default("1"),
        scale_factor: Int = Default("2"),
        model: String = Default(None),
        input: String = Default("x"),
        output: String = Default("y"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply DNN-based image super resolution to the input.

        Args:
            dnn_backend: DNN backend used for model execution (from 0 to 1) (default 1)
            scale_factor: scale factor for SRCNN model (from 2 to 4) (default 2)
            model: path to model file specifying network architecture and its parameters
            input: input name of the model (default "x")
            output: output name of the model (default "y")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#sr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="sr", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "dnn_backend": dnn_backend,
                    "scale_factor": scale_factor,
                    "model": model,
                    "input": input,
                    "output": output,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def ssim(
        self,
        _reference: VideoStream,
        *,
        stats_file: String = Default(None),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the SSIM between two video streams.

        Args:
            stats_file: Set file where to store per-frame difference information
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#ssim)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="ssim", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _reference,
            **merge(
                {
                    "stats_file": stats_file,
                },
                extra_options,
                framesync_options,
                timeline_options,
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
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert video stereoscopic 3D view.

        Args:
            _in: set input format (from 16 to 32) (default sbsl)
            out: set output format (from 0 to 32) (default arcd)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#stereo3d)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="stereo3d", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "in": _in,
                    "out": out,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def subtitles(
        self,
        *,
        filename: String = Default(None),
        original_size: Image_size = Default(None),
        fontsdir: String = Default(None),
        alpha: Boolean = Default("false"),
        charenc: String = Default(None),
        stream_index: Int = Default("-1"),
        force_style: String = Default(None),
        wrap_unicode: Boolean = Default("auto"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Render text subtitles onto input video using the libass library.

        Args:
            filename: set the filename of file to read
            original_size: set the size of the original video (used to scale fonts)
            fontsdir: set the directory containing the fonts to read
            alpha: enable processing of alpha channel (default false)
            charenc: set input character encoding
            stream_index: set stream index (from -1 to INT_MAX) (default -1)
            force_style: force subtitle style
            wrap_unicode: break lines according to the Unicode Line Breaking Algorithm (default auto)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#subtitles)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="subtitles", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filename": filename,
                    "original_size": original_size,
                    "fontsdir": fontsdir,
                    "alpha": alpha,
                    "charenc": charenc,
                    "stream_index": stream_index,
                    "force_style": force_style,
                    "wrap_unicode": wrap_unicode,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def super2xsai(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scale the input by 2x using the Super2xSaI pixel art algorithm.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#super2xsai)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="super2xsai", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Swap 2 rectangular objects in video.

        Args:
            w: set rect width (default "w/2")
            h: set rect height (default "h/2")
            x1: set 1st rect x top left coordinate (default "w/2")
            y1: set 1st rect y top left coordinate (default "h/2")
            x2: set 2nd rect x top left coordinate (default "0")
            y2: set 2nd rect y top left coordinate (default "0")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#swaprect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="swaprect", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "w": w,
                    "h": h,
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def swapuv(
        self,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Swap U and V components.

        Args:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#swapuv)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="swapuv", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
                timeline_options,
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
        | Default = Default("-1"),
        c0_expr: String = Default(None),
        c1_expr: String = Default(None),
        c2_expr: String = Default(None),
        c3_expr: String = Default(None),
        all_expr: String = Default(None),
        c0_opacity: Double = Default("1"),
        c1_opacity: Double = Default("1"),
        c2_opacity: Double = Default("1"),
        c3_opacity: Double = Default("1"),
        all_opacity: Double = Default("1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Blend successive frames.

        Args:
            c0_mode: set component #0 blend mode (from 0 to 39) (default normal)
            c1_mode: set component #1 blend mode (from 0 to 39) (default normal)
            c2_mode: set component #2 blend mode (from 0 to 39) (default normal)
            c3_mode: set component #3 blend mode (from 0 to 39) (default normal)
            all_mode: set blend mode for all components (from -1 to 39) (default -1)
            c0_expr: set color component #0 expression
            c1_expr: set color component #1 expression
            c2_expr: set color component #2 expression
            c3_expr: set color component #3 expression
            all_expr: set expression for all color components
            c0_opacity: set color component #0 opacity (from 0 to 1) (default 1)
            c1_opacity: set color component #1 opacity (from 0 to 1) (default 1)
            c2_opacity: set color component #2 opacity (from 0 to 1) (default 1)
            c3_opacity: set color component #3 opacity (from 0 to 1) (default 1)
            all_opacity: set opacity for all color components (from 0 to 1) (default 1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tblend)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tblend", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def telecine(
        self,
        *,
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default(
            "top"
        ),
        pattern: String = Default("23"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply a telecine pattern.

        Args:
            first_field: select first field (from 0 to 1) (default top)
            pattern: pattern that describe for how many fields a frame is to be displayed (default "23")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#telecine)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="telecine", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "first_field": first_field,
                    "pattern": pattern,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def thistogram(
        self,
        *,
        width: Int = Default("0"),
        display_mode: Int | Literal["overlay", "parade", "stack"] | Default = Default(
            "stack"
        ),
        levels_mode: Int | Literal["linear", "logarithmic"] | Default = Default(
            "linear"
        ),
        components: Int = Default("7"),
        bgopacity: Float = Default("0.9"),
        envelope: Boolean = Default("false"),
        ecolor: Color = Default("gold"),
        slide: Int
        | Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | Default = Default("replace"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and draw a temporal histogram.

        Args:
            width: set width (from 0 to 8192) (default 0)
            display_mode: set display mode (from 0 to 2) (default stack)
            levels_mode: set levels mode (from 0 to 1) (default linear)
            components: set color components to display (from 1 to 15) (default 7)
            bgopacity: set background opacity (from 0 to 1) (default 0.9)
            envelope: display envelope (default false)
            ecolor: set envelope color (default "gold")
            slide: set slide mode (from 0 to 4) (default replace)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#thistogram)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="thistogram", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "width": width,
                    "display_mode": display_mode,
                    "levels_mode": levels_mode,
                    "components": components,
                    "bgopacity": bgopacity,
                    "envelope": envelope,
                    "ecolor": ecolor,
                    "slide": slide,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def threshold(
        self,
        _threshold: VideoStream,
        _min: VideoStream,
        _max: VideoStream,
        *,
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Threshold first video stream using other video streams.

        Args:
            planes: set planes to filter (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#threshold)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="threshold",
                typings_input=("video", "video", "video", "video"),
                typings_output=("video",),
            ),
            self,
            _threshold,
            _min,
            _max,
            **merge(
                {
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def thumbnail(
        self,
        *,
        n: Int = Default("100"),
        log: Int | Literal["quiet", "info", "verbose"] | Default = Default("info"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Select the most representative frame in a given sequence of consecutive frames.

        Args:
            n: set the frames batch size (from 2 to INT_MAX) (default 100)
            log: force stats logging level (from INT_MIN to INT_MAX) (default info)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#thumbnail)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="thumbnail", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "n": n,
                    "log": log,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def tile(
        self,
        *,
        layout: Image_size = Default("6x5"),
        nb_frames: Int = Default("0"),
        margin: Int = Default("0"),
        padding: Int = Default("0"),
        color: Color = Default("black"),
        overlap: Int = Default("0"),
        init_padding: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Tile several successive frames together.

        Args:
            layout: set grid size (default "6x5")
            nb_frames: set maximum number of frame to render (from 0 to INT_MAX) (default 0)
            margin: set outer border margin in pixels (from 0 to 1024) (default 0)
            padding: set inner border thickness in pixels (from 0 to 1024) (default 0)
            color: set the color of the unused area (default "black")
            overlap: set how many frames to overlap for each render (from 0 to INT_MAX) (default 0)
            init_padding: set how many frames to initially pad (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tile)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tile", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "layout": layout,
                    "nb_frames": nb_frames,
                    "margin": margin,
                    "padding": padding,
                    "color": color,
                    "overlap": overlap,
                    "init_padding": init_padding,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def tinterlace(
        self,
        *,
        mode: Int
        | Literal[
            "merge",
            "drop_even",
            "drop_odd",
            "pad",
            "interleave_top",
            "interleave_bottom",
            "interlacex2",
            "mergex2",
        ]
        | Default = Default("merge"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Perform temporal field interlacing.

        Args:
            mode: select interlace mode (from 0 to 7) (default merge)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tinterlace)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tinterlace", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                },
                extra_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Compute and apply a lookup table from two successive frames.

        Args:
            c0: set component #0 expression (default "x")
            c1: set component #1 expression (default "x")
            c2: set component #2 expression (default "x")
            c3: set component #3 expression (default "x")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tlut2", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "c0": c0,
                    "c1": c1,
                    "c2": c2,
                    "c3": c3,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def tmedian(
        self,
        *,
        radius: Int = Default("1"),
        planes: Int = Default("15"),
        percentile: Float = Default("0.5"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pick median pixels from successive frames.

        Args:
            radius: set median filter radius (from 1 to 127) (default 1)
            planes: set planes to filter (from 0 to 15) (default 15)
            percentile: set percentile (from 0 to 1) (default 0.5)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tmedian)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tmedian", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "radius": radius,
                    "planes": planes,
                    "percentile": percentile,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def tmidequalizer(
        self,
        *,
        radius: Int = Default("5"),
        sigma: Float = Default("0.5"),
        planes: Int = Default("15"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Temporal Midway Equalization.

        Args:
            radius: set radius (from 1 to 127) (default 5)
            sigma: set sigma (from 0 to 1) (default 0.5)
            planes: set planes (from 0 to 15) (default 15)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tmidequalizer)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tmidequalizer",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "radius": radius,
                    "sigma": sigma,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def tmix(
        self,
        *,
        frames: Int = Default("3"),
        weights: String = Default("1 1 1"),
        scale: Float = Default("0"),
        planes: Flags = Default("F"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Mix successive video frames.

        Args:
            frames: set number of successive frames to mix (from 1 to 1024) (default 3)
            weights: set weight for each frame (default "1 1 1")
            scale: set scale (from 0 to 32767) (default 0)
            planes: set what planes to filter (default F)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tmix)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tmix", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "frames": frames,
                    "weights": weights,
                    "scale": scale,
                    "planes": planes,
                },
                extra_options,
                timeline_options,
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
        desat: Double = Default("2"),
        peak: Double = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Conversion to/from different dynamic ranges.

        Args:
            tonemap: tonemap algorithm selection (from 0 to 6) (default none)
            param: tonemap parameter (from DBL_MIN to DBL_MAX) (default nan)
            desat: desaturation strength (from 0 to DBL_MAX) (default 2)
            peak: signal peak override (from 0 to DBL_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tonemap)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tonemap", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "tonemap": tonemap,
                    "param": param,
                    "desat": desat,
                    "peak": peak,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def tonemap_opencl(
        self,
        *,
        tonemap: Int
        | Literal["none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"]
        | Default = Default("none"),
        transfer: Int | Literal["bt709", "bt2020"] | Default = Default("bt709"),
        matrix: Int | Literal["bt709", "bt2020"] | Default = Default("-1"),
        primaries: Int | Literal["bt709", "bt2020"] | Default = Default("-1"),
        range: Int | Literal["tv", "pc", "limited", "full"] | Default = Default("-1"),
        format: Pix_fmt = Default("none"),
        peak: Double = Default("0"),
        param: Double = Default("nan"),
        desat: Double = Default("0.5"),
        threshold: Double = Default("0.2"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Perform HDR to SDR conversion with tonemapping.

        Args:
            tonemap: tonemap algorithm selection (from 0 to 6) (default none)
            transfer: set transfer characteristic (from -1 to INT_MAX) (default bt709)
            matrix: set colorspace matrix (from -1 to INT_MAX) (default -1)
            primaries: set color primaries (from -1 to INT_MAX) (default -1)
            range: set color range (from -1 to INT_MAX) (default -1)
            format: output pixel format (default none)
            peak: signal peak override (from 0 to DBL_MAX) (default 0)
            param: tonemap parameter (from DBL_MIN to DBL_MAX) (default nan)
            desat: desaturation parameter (from 0 to DBL_MAX) (default 0.5)
            threshold: scene detection threshold (from 0 to DBL_MAX) (default 0.2)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tonemap_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tonemap_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "tonemap": tonemap,
                    "transfer": transfer,
                    "matrix": matrix,
                    "primaries": primaries,
                    "range": range,
                    "format": format,
                    "peak": peak,
                    "param": param,
                    "desat": desat,
                    "threshold": threshold,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def tonemap_vaapi(
        self,
        *,
        format: String = Default(None),
        matrix: String = Default(None),
        primaries: String = Default(None),
        transfer: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        VAAPI VPP for tone-mapping.

        Args:
            format: Output pixel format set
            matrix: Output color matrix coefficient set
            primaries: Output color primaries set
            transfer: Output color transfer characteristics set
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tonemap_005fvaapi)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tonemap_vaapi",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "format": format,
                    "matrix": matrix,
                    "primaries": primaries,
                    "transfer": transfer,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def tpad(
        self,
        *,
        start: Int = Default("0"),
        stop: Int = Default("0"),
        start_mode: Int | Literal["add", "clone"] | Default = Default("add"),
        stop_mode: Int | Literal["add", "clone"] | Default = Default("add"),
        start_duration: Duration = Default("0"),
        stop_duration: Duration = Default("0"),
        color: Color = Default("black"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Temporarily pad video frames.

        Args:
            start: set the number of frames to delay input (from 0 to INT_MAX) (default 0)
            stop: set the number of frames to add after input finished (from -1 to INT_MAX) (default 0)
            start_mode: set the mode of added frames to start (from 0 to 1) (default add)
            stop_mode: set the mode of added frames to end (from 0 to 1) (default add)
            start_duration: set the duration to delay input (default 0)
            stop_duration: set the duration to pad input (default 0)
            color: set the color of the added frames (default "black")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#tpad)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="tpad", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "start": start,
                    "stop": stop,
                    "start_mode": start_mode,
                    "stop_mode": stop_mode,
                    "start_duration": start_duration,
                    "stop_duration": stop_duration,
                    "color": color,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def transpose(
        self,
        *,
        dir: Int
        | Literal["cclock_flip", "clock", "cclock", "clock_flip"]
        | Default = Default("cclock_flip"),
        passthrough: Int | Literal["none", "portrait", "landscape"] | Default = Default(
            "none"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Transpose input video.

        Args:
            dir: set transpose direction (from 0 to 7) (default cclock_flip)
            passthrough: do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#transpose)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="transpose", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "dir": dir,
                    "passthrough": passthrough,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def transpose_vulkan(
        self,
        *,
        dir: Int
        | Literal["cclock_flip", "clock", "cclock", "clock_flip"]
        | Default = Default("cclock_flip"),
        passthrough: Int | Literal["none", "portrait", "landscape"] | Default = Default(
            "none"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Transpose Vulkan Filter.

        Args:
            dir: set transpose direction (from 0 to 7) (default cclock_flip)
            passthrough: do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="transpose_vulkan",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "dir": dir,
                    "passthrough": passthrough,
                },
                extra_options,
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
        duration: Duration = Default("0"),
        start_frame: Int64 = Default("-1"),
        end_frame: Int64 = Default("I64_MAX"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Pick one continuous section from the input, drop the rest.

        Args:
            start: Timestamp of the first frame that should be passed (default INT64_MAX)
            end: Timestamp of the first frame that should be dropped again (default INT64_MAX)
            start_pts: Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
            end_pts: Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
            duration: Maximum duration of the output (default 0)
            start_frame: Number of the first frame that should be passed to the output (from -1 to I64_MAX) (default -1)
            end_frame: Number of the first frame that should be dropped again (from 0 to I64_MAX) (default I64_MAX)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#trim)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="trim", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "start": start,
                    "end": end,
                    "start_pts": start_pts,
                    "end_pts": end_pts,
                    "duration": duration,
                    "start_frame": start_frame,
                    "end_frame": end_frame,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def unsharp(
        self,
        *,
        luma_msize_x: Int = Default("5"),
        luma_msize_y: Int = Default("5"),
        luma_amount: Float = Default("1"),
        chroma_msize_x: Int = Default("5"),
        chroma_msize_y: Int = Default("5"),
        chroma_amount: Float = Default("0"),
        alpha_msize_x: Int = Default("5"),
        alpha_msize_y: Int = Default("5"),
        alpha_amount: Float = Default("0"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Sharpen or blur the input video.

        Args:
            luma_msize_x: set luma matrix horizontal size (from 3 to 23) (default 5)
            luma_msize_y: set luma matrix vertical size (from 3 to 23) (default 5)
            luma_amount: set luma effect strength (from -2 to 5) (default 1)
            chroma_msize_x: set chroma matrix horizontal size (from 3 to 23) (default 5)
            chroma_msize_y: set chroma matrix vertical size (from 3 to 23) (default 5)
            chroma_amount: set chroma effect strength (from -2 to 5) (default 0)
            alpha_msize_x: set alpha matrix horizontal size (from 3 to 23) (default 5)
            alpha_msize_y: set alpha matrix vertical size (from 3 to 23) (default 5)
            alpha_amount: set alpha effect strength (from -2 to 5) (default 0)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#unsharp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="unsharp", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def unsharp_opencl(
        self,
        *,
        luma_msize_x: Float = Default("5"),
        luma_msize_y: Float = Default("5"),
        luma_amount: Float = Default("1"),
        chroma_msize_x: Float = Default("5"),
        chroma_msize_y: Float = Default("5"),
        chroma_amount: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply unsharp mask to input video.

        Args:
            luma_msize_x: Set luma mask horizontal diameter (pixels) (from 1 to 23) (default 5)
            luma_msize_y: Set luma mask vertical diameter (pixels) (from 1 to 23) (default 5)
            luma_amount: Set luma amount (multiplier) (from -10 to 10) (default 1)
            chroma_msize_x: Set chroma mask horizontal diameter (pixels after subsampling) (from 1 to 23) (default 5)
            chroma_msize_y: Set chroma mask vertical diameter (pixels after subsampling) (from 1 to 23) (default 5)
            chroma_amount: Set chroma amount (multiplier) (from -10 to 10) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#unsharp_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="unsharp_opencl",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "luma_msize_x": luma_msize_x,
                    "luma_msize_y": luma_msize_y,
                    "luma_amount": luma_amount,
                    "chroma_msize_x": chroma_msize_x,
                    "chroma_msize_y": chroma_msize_y,
                    "chroma_amount": chroma_amount,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def untile(
        self,
        *,
        layout: Image_size = Default("6x5"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Untile a frame into a sequence of frames.

        Args:
            layout: set grid size (default "6x5")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#untile)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="untile", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "layout": layout,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def uspp(
        self,
        *,
        quality: Int = Default("3"),
        qp: Int = Default("0"),
        use_bframe_qp: Boolean = Default("false"),
        codec: String = Default("snow"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Ultra Simple / Slow Post-processing filter.

        Args:
            quality: set quality (from 0 to 8) (default 3)
            qp: force a constant quantizer parameter (from 0 to 63) (default 0)
            use_bframe_qp: use B-frames' QP (default false)
            codec: Codec name (default "snow")
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#uspp)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="uspp", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "quality": quality,
                    "qp": qp,
                    "use_bframe_qp": use_bframe_qp,
                    "codec": codec,
                },
                extra_options,
                timeline_options,
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
        w: Int = Default("0"),
        h: Int = Default("0"),
        in_stereo: Int | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        out_stereo: Int | Literal["2d", "sbs", "tb"] | Default = Default("2d"),
        in_forder: String = Default("rludfb"),
        out_forder: String = Default("rludfb"),
        in_frot: String = Default("000000"),
        out_frot: String = Default("000000"),
        in_pad: Float = Default("0"),
        out_pad: Float = Default("0"),
        fin_pad: Int = Default("0"),
        fout_pad: Int = Default("0"),
        yaw: Float = Default("0"),
        pitch: Float = Default("0"),
        roll: Float = Default("0"),
        rorder: String = Default("ypr"),
        h_fov: Float = Default("0"),
        v_fov: Float = Default("0"),
        d_fov: Float = Default("0"),
        h_flip: Boolean = Default("false"),
        v_flip: Boolean = Default("false"),
        d_flip: Boolean = Default("false"),
        ih_flip: Boolean = Default("false"),
        iv_flip: Boolean = Default("false"),
        in_trans: Boolean = Default("false"),
        out_trans: Boolean = Default("false"),
        ih_fov: Float = Default("0"),
        iv_fov: Float = Default("0"),
        id_fov: Float = Default("0"),
        h_offset: Float = Default("0"),
        v_offset: Float = Default("0"),
        alpha_mask: Boolean = Default("false"),
        reset_rot: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Convert 360 projection of video.

        Args:
            input: set input projection (from 0 to 24) (default e)
            output: set output projection (from 0 to 24) (default c3x2)
            interp: set interpolation method (from 0 to 7) (default line)
            w: output width (from 0 to 32767) (default 0)
            h: output height (from 0 to 32767) (default 0)
            in_stereo: input stereo format (from 0 to 2) (default 2d)
            out_stereo: output stereo format (from 0 to 2) (default 2d)
            in_forder: input cubemap face order (default "rludfb")
            out_forder: output cubemap face order (default "rludfb")
            in_frot: input cubemap face rotation (default "000000")
            out_frot: output cubemap face rotation (default "000000")
            in_pad: percent input cubemap pads (from 0 to 0.1) (default 0)
            out_pad: percent output cubemap pads (from 0 to 0.1) (default 0)
            fin_pad: fixed input cubemap pads (from 0 to 100) (default 0)
            fout_pad: fixed output cubemap pads (from 0 to 100) (default 0)
            yaw: yaw rotation (from -180 to 180) (default 0)
            pitch: pitch rotation (from -180 to 180) (default 0)
            roll: roll rotation (from -180 to 180) (default 0)
            rorder: rotation order (default "ypr")
            h_fov: output horizontal field of view (from 0 to 360) (default 0)
            v_fov: output vertical field of view (from 0 to 360) (default 0)
            d_fov: output diagonal field of view (from 0 to 360) (default 0)
            h_flip: flip out video horizontally (default false)
            v_flip: flip out video vertically (default false)
            d_flip: flip out video indepth (default false)
            ih_flip: flip in video horizontally (default false)
            iv_flip: flip in video vertically (default false)
            in_trans: transpose video input (default false)
            out_trans: transpose video output (default false)
            ih_fov: input horizontal field of view (from 0 to 360) (default 0)
            iv_fov: input vertical field of view (from 0 to 360) (default 0)
            id_fov: input diagonal field of view (from 0 to 360) (default 0)
            h_offset: output horizontal off-axis offset (from -1 to 1) (default 0)
            v_offset: output vertical off-axis offset (from -1 to 1) (default 0)
            alpha_mask: build mask in alpha plane (default false)
            reset_rot: reset rotation (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#v360)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="v360", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vaguedenoiser(
        self,
        *,
        threshold: Float = Default("2"),
        method: Int | Literal["hard", "soft", "garrote"] | Default = Default("garrote"),
        nsteps: Int = Default("6"),
        percent: Float = Default("85"),
        planes: Int = Default("15"),
        type: Int | Literal["universal", "bayes"] | Default = Default("universal"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply a Wavelet based Denoiser.

        Args:
            threshold: set filtering strength (from 0 to DBL_MAX) (default 2)
            method: set filtering method (from 0 to 2) (default garrote)
            nsteps: set number of steps (from 1 to 32) (default 6)
            percent: set percent of full denoising (from 0 to 100) (default 85)
            planes: set planes to filter (from 0 to 15) (default 15)
            type: set threshold type (from 0 to 1) (default universal)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vaguedenoiser)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vaguedenoiser",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "threshold": threshold,
                    "method": method,
                    "nsteps": nsteps,
                    "percent": percent,
                    "planes": planes,
                    "type": type,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def varblur(
        self,
        _radius: VideoStream,
        *,
        min_r: Int = Default("0"),
        max_r: Int = Default("8"),
        planes: Int = Default("15"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Variable Blur filter.

        Args:
            min_r: set min blur radius (from 0 to 254) (default 0)
            max_r: set max blur radius (from 1 to 255) (default 8)
            planes: set planes to filter (from 0 to 15) (default 15)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#varblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="varblur",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _radius,
            **merge(
                {
                    "min_r": min_r,
                    "max_r": max_r,
                    "planes": planes,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def vectorscope(
        self,
        *,
        mode: Int
        | Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | Default = Default("gray"),
        x: Int = Default("1"),
        y: Int = Default("2"),
        intensity: Float = Default("0.004"),
        envelope: Int
        | Literal["none", "instant", "peak", "peak+instant"]
        | Default = Default("none"),
        graticule: Int
        | Literal["none", "green", "color", "invert"]
        | Default = Default("none"),
        opacity: Float = Default("0.75"),
        flags: Flags | Literal["white", "black", "name"] | Default = Default("name"),
        bgopacity: Float = Default("0.3"),
        lthreshold: Float = Default("0"),
        hthreshold: Float = Default("1"),
        colorspace: Int | Literal["auto", "601", "709"] | Default = Default("auto"),
        tint0: Float = Default("0"),
        tint1: Float = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Video vectorscope.

        Args:
            mode: set vectorscope mode (from 0 to 5) (default gray)
            x: set color component on X axis (from 0 to 2) (default 1)
            y: set color component on Y axis (from 0 to 2) (default 2)
            intensity: set intensity (from 0 to 1) (default 0.004)
            envelope: set envelope (from 0 to 3) (default none)
            graticule: set graticule (from 0 to 3) (default none)
            opacity: set graticule opacity (from 0 to 1) (default 0.75)
            flags: set graticule flags (default name)
            bgopacity: set background opacity (from 0 to 1) (default 0.3)
            lthreshold: set low threshold (from 0 to 1) (default 0)
            hthreshold: set high threshold (from 0 to 1) (default 1)
            colorspace: set colorspace (from 0 to 2) (default auto)
            tint0: set 1st tint (from -1 to 1) (default 0)
            tint1: set 2nd tint (from -1 to 1) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vectorscope)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vectorscope", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vflip(
        self,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Flip the input video vertically.

        Args:
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vflip)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vflip", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def vflip_vulkan(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Vertically flip the input video in Vulkan.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vflip_005fvulkan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vflip_vulkan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vfrdet(
        self,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Variable frame rate detect filter.

        Args:
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vfrdet)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vfrdet", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {},
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vibrance(
        self,
        *,
        intensity: Float = Default("0"),
        rbal: Float = Default("1"),
        gbal: Float = Default("1"),
        bbal: Float = Default("1"),
        rlum: Float = Default("0.072186"),
        glum: Float = Default("0.715158"),
        blum: Float = Default("0.212656"),
        alternate: Boolean = Default("false"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Boost or alter saturation.

        Args:
            intensity: set the intensity value (from -2 to 2) (default 0)
            rbal: set the red balance value (from -10 to 10) (default 1)
            gbal: set the green balance value (from -10 to 10) (default 1)
            bbal: set the blue balance value (from -10 to 10) (default 1)
            rlum: set the red luma coefficient (from 0 to 1) (default 0.072186)
            glum: set the green luma coefficient (from 0 to 1) (default 0.715158)
            blum: set the blue luma coefficient (from 0 to 1) (default 0.212656)
            alternate: use alternate colors (default false)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vibrance)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vibrance", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "intensity": intensity,
                    "rbal": rbal,
                    "gbal": gbal,
                    "bbal": bbal,
                    "rlum": rlum,
                    "glum": glum,
                    "blum": blum,
                    "alternate": alternate,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def vidstabdetect(
        self,
        *,
        result: String = Default("transforms.trf"),
        shakiness: Int = Default("5"),
        accuracy: Int = Default("15"),
        stepsize: Int = Default("6"),
        mincontrast: Double = Default("0.25"),
        show: Int = Default("0"),
        tripod: Int = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2).

        Args:
            result: path to the file used to write the transforms (default "transforms.trf")
            shakiness: how shaky is the video and how quick is the camera? 1: little (fast) 10: very strong/quick (slow) (from 1 to 10) (default 5)
            accuracy: (>=shakiness) 1: low 15: high (slow) (from 1 to 15) (default 15)
            stepsize: region around minimum is scanned with 1 pixel resolution (from 1 to 32) (default 6)
            mincontrast: below this contrast a field is discarded (0-1) (from 0 to 1) (default 0.25)
            show: 0: draw nothing; 1,2: show fields and transforms (from 0 to 2) (default 0)
            tripod: virtual tripod mode (if >0): motion is compared to a reference reference frame (frame # is the value) (from 0 to INT_MAX) (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vidstabdetect)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vidstabdetect",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
                {
                    "result": result,
                    "shakiness": shakiness,
                    "accuracy": accuracy,
                    "stepsize": stepsize,
                    "mincontrast": mincontrast,
                    "show": show,
                    "tripod": tripod,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vidstabtransform(
        self,
        *,
        input: String = Default("transforms.trf"),
        smoothing: Int = Default("15"),
        optalgo: Int | Literal["opt", "gauss", "avg"] | Default = Default("opt"),
        maxshift: Int = Default("-1"),
        maxangle: Double = Default("-1"),
        crop: Int | Literal["keep", "black"] | Default = Default("keep"),
        invert: Int = Default("0"),
        relative: Int = Default("1"),
        zoom: Double = Default("0"),
        optzoom: Int = Default("1"),
        zoomspeed: Double = Default("0.25"),
        interpol: Int
        | Literal["no", "linear", "bilinear", "bicubic"]
        | Default = Default("bilinear"),
        tripod: Boolean = Default("false"),
        debug: Boolean = Default("false"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1).

        Args:
            input: set path to the file storing the transforms (default "transforms.trf")
            smoothing: set number of frames*2 + 1 used for lowpass filtering (from 0 to 1000) (default 15)
            optalgo: set camera path optimization algo (from 0 to 2) (default opt)
            maxshift: set maximal number of pixels to translate image (from -1 to 500) (default -1)
            maxangle: set maximal angle in rad to rotate image (from -1 to 3.14) (default -1)
            crop: set cropping mode (from 0 to 1) (default keep)
            invert: invert transforms (from 0 to 1) (default 0)
            relative: consider transforms as relative (from 0 to 1) (default 1)
            zoom: set percentage to zoom (>0: zoom in, <0: zoom out (from -100 to 100) (default 0)
            optzoom: set optimal zoom (0: nothing, 1: optimal static zoom, 2: optimal dynamic zoom) (from 0 to 2) (default 1)
            zoomspeed: for adative zoom: percent to zoom maximally each frame (from 0 to 5) (default 0.25)
            interpol: set type of interpolation (from 0 to 3) (default bilinear)
            tripod: enable virtual tripod mode (same as relative=0:smoothing=0) (default false)
            debug: enable debug mode and writer global motions information to file (default false)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vidstabtransform)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vidstabtransform",
                typings_input=("video",),
                typings_output=("video",),
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def vif(
        self,
        _reference: VideoStream,
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the VIF between two video streams.

        Args:
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vif)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vif", typings_input=("video", "video"), typings_output=("video",)
            ),
            self,
            _reference,
            **merge(
                {},
                extra_options,
                framesync_options,
                timeline_options,
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
        dither: Boolean = Default("true"),
        aspect: Rational = Default("1/1"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Make or reverse a vignette effect.

        Args:
            angle: set lens angle (default "PI/5")
            x0: set circle center position on x-axis (default "w/2")
            y0: set circle center position on y-axis (default "h/2")
            mode: set forward/backward mode (from 0 to 1) (default forward)
            eval: specify when to evaluate expressions (from 0 to 1) (default init)
            dither: set dithering (default true)
            aspect: set aspect ratio (from 0 to DBL_MAX) (default 1/1)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vignette)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vignette", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "angle": angle,
                    "x0": x0,
                    "y0": y0,
                    "mode": mode,
                    "eval": eval,
                    "dither": dither,
                    "aspect": aspect,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def vmafmotion(
        self,
        *,
        stats_file: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Calculate the VMAF Motion score.

        Args:
            stats_file: Set file where to store per-frame difference information
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#vmafmotion)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="vmafmotion", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "stats_file": stats_file,
                },
                extra_options,
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
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Martin Weston three field deinterlace.

        Args:
            filter: specify the filter (from 0 to 1) (default complex)
            mode: specify the interlacing mode (from 0 to 1) (default field)
            parity: specify the assumed picture field parity (from -1 to 1) (default auto)
            deint: specify which frames to deinterlace (from 0 to 1) (default all)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#w3fdif)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="w3fdif", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "filter": filter,
                    "mode": mode,
                    "parity": parity,
                    "deint": deint,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def waveform(
        self,
        *,
        mode: Int | Literal["row", "column"] | Default = Default("column"),
        intensity: Float = Default("0.04"),
        mirror: Boolean = Default("true"),
        display: Int | Literal["overlay", "stack", "parade"] | Default = Default(
            "stack"
        ),
        components: Int = Default("1"),
        envelope: Int
        | Literal["none", "instant", "peak", "peak+instant"]
        | Default = Default("none"),
        filter: Int
        | Literal[
            "lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"
        ]
        | Default = Default("lowpass"),
        graticule: Int
        | Literal["none", "green", "orange", "invert"]
        | Default = Default("none"),
        opacity: Float = Default("0.75"),
        flags: Flags | Literal["numbers", "dots"] | Default = Default("numbers"),
        scale: Int | Literal["digital", "millivolts", "ire"] | Default = Default(
            "digital"
        ),
        bgopacity: Float = Default("0.75"),
        tint0: Float = Default("0"),
        tint1: Float = Default("0"),
        fitmode: Int | Literal["none", "size"] | Default = Default("none"),
        input: Int | Literal["all", "first"] | Default = Default("first"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Video waveform monitor.

        Args:
            mode: set mode (from 0 to 1) (default column)
            intensity: set intensity (from 0 to 1) (default 0.04)
            mirror: set mirroring (default true)
            display: set display mode (from 0 to 2) (default stack)
            components: set components to display (from 1 to 15) (default 1)
            envelope: set envelope to display (from 0 to 3) (default none)
            filter: set filter (from 0 to 7) (default lowpass)
            graticule: set graticule (from 0 to 3) (default none)
            opacity: set graticule opacity (from 0 to 1) (default 0.75)
            flags: set graticule flags (default numbers)
            scale: set scale (from 0 to 2) (default digital)
            bgopacity: set background opacity (from 0 to 1) (default 0.75)
            tint0: set 1st tint (from -1 to 1) (default 0)
            tint1: set 2nd tint (from -1 to 1) (default 0)
            fitmode: set fit mode (from 0 to 1) (default none)
            input: set input formats selection (from 0 to 1) (default first)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#waveform)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="waveform", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                    "input": input,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def weave(
        self,
        *,
        first_field: Int | Literal["top", "t", "bottom", "b"] | Default = Default(
            "top"
        ),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Weave input video fields into frames.

        Args:
            first_field: set first field (from 0 to 1) (default top)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="weave", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "first_field": first_field,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def xbr(
        self,
        *,
        n: Int = Default("3"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Scale the input using xBR algorithm.

        Args:
            n: set scale factor (from 2 to 4) (default 3)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xbr)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="xbr", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "n": n,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def xcorrelate(
        self,
        _secondary: VideoStream,
        *,
        planes: Int = Default("7"),
        secondary: Int | Literal["first", "all"] | Default = Default("all"),
        framesync_options: FFMpegFrameSyncOption | None = None,
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Cross-correlate first video stream with second video stream.

        Args:
            planes: set planes to cross-correlate (from 0 to 15) (default 7)
            secondary: when to process secondary frame (from 0 to 1) (default all)
            framesync_options: Framesync options
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xcorrelate)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="xcorrelate",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _secondary,
            **merge(
                {
                    "planes": planes,
                    "secondary": secondary,
                },
                extra_options,
                framesync_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def xfade(
        self,
        _xfade: VideoStream,
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
            "hlwind",
            "hrwind",
            "vuwind",
            "vdwind",
            "coverleft",
            "coverright",
            "coverup",
            "coverdown",
            "revealleft",
            "revealright",
            "revealup",
            "revealdown",
        ]
        | Default = Default("fade"),
        duration: Duration = Default("1"),
        offset: Duration = Default("0"),
        expr: String = Default(None),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Cross fade one video with another video.

        Args:
            transition: set cross fade transition (from -1 to 57) (default fade)
            duration: set cross fade duration (default 1)
            offset: set cross fade start relative to first input stream (default 0)
            expr: set expression for custom transition
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xfade)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="xfade",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _xfade,
            **merge(
                {
                    "transition": transition,
                    "duration": duration,
                    "offset": offset,
                    "expr": expr,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def xfade_opencl(
        self,
        _xfade: VideoStream,
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
        ]
        | Default = Default("fade"),
        source: String = Default(None),
        kernel: String = Default(None),
        duration: Duration = Default("1"),
        offset: Duration = Default("0"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Cross fade one video with another video.

        Args:
            transition: set cross fade transition (from 0 to 9) (default fade)
            source: set OpenCL program source file for custom transition
            kernel: set kernel name in program file for custom transition
            duration: set cross fade duration (default 1)
            offset: set cross fade start relative to first input stream (default 0)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#xfade_005fopencl)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="xfade_opencl",
                typings_input=("video", "video"),
                typings_output=("video",),
            ),
            self,
            _xfade,
            **merge(
                {
                    "transition": transition,
                    "source": source,
                    "kernel": kernel,
                    "duration": duration,
                    "offset": offset,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def yadif(
        self,
        *,
        mode: Int
        | Literal[
            "send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"
        ]
        | Default = Default("send_frame"),
        parity: Int | Literal["tff", "bff", "auto"] | Default = Default("auto"),
        deint: Int | Literal["all", "interlaced"] | Default = Default("all"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Deinterlace the input image.

        Args:
            mode: specify the interlacing mode (from 0 to 3) (default send_frame)
            parity: specify the assumed picture field parity (from -1 to 1) (default auto)
            deint: specify which frames to deinterlace (from 0 to 1) (default all)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#yadif)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="yadif", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "mode": mode,
                    "parity": parity,
                    "deint": deint,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def yaepblur(
        self,
        *,
        radius: Int = Default("3"),
        planes: Int = Default("1"),
        sigma: Int = Default("128"),
        timeline_options: FFMpegTimelineOption | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Yet another edge preserving blur filter.

        Args:
            radius: set window radius (from 0 to INT_MAX) (default 3)
            planes: set planes to filter (from 0 to 15) (default 1)
            sigma: set blur strength (from 1 to INT_MAX) (default 128)
            timeline_options: Timeline options
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#yaepblur)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="yaepblur", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "radius": radius,
                    "planes": planes,
                    "sigma": sigma,
                },
                extra_options,
                timeline_options,
            ),
        )
        return filter_node.video(0)

    def zmq(
        self,
        *,
        bind_address: String = Default("tcp://*:5555"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Receive commands through ZMQ and broker them to filters.

        Args:
            bind_address: set bind address (default "tcp://*:5555")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#zmq_002c-azmq)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="zmq", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "bind_address": bind_address,
                },
                extra_options,
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
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply Zoom & Pan effect.

        Args:
            zoom: set the zoom expression (default "1")
            x: set the x expression (default "0")
            y: set the y expression (default "0")
            d: set the duration expression (default "90")
            s: set the output image size (default "hd720")
            fps: set the output framerate (default "25")
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#zoompan)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="zoompan", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
                {
                    "zoom": zoom,
                    "x": x,
                    "y": y,
                    "d": d,
                    "s": s,
                    "fps": fps,
                },
                extra_options,
            ),
        )
        return filter_node.video(0)

    def zscale(
        self,
        *,
        w: String = Default(None),
        h: String = Default(None),
        size: String = Default(None),
        dither: Int
        | Literal["none", "ordered", "random", "error_diffusion"]
        | Default = Default("none"),
        filter: Int
        | Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | Default = Default("bilinear"),
        out_range: Int
        | Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | Default = Default("input"),
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
            "jedec-p22",
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
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
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
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | Default = Default("input"),
        in_range: Int
        | Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | Default = Default("input"),
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
            "jedec-p22",
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
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
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
            "chroma-derived-nc",
            "chroma-derived-c",
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
        agamma: Boolean = Default("true"),
        param_a: Double = Default("nan"),
        param_b: Double = Default("nan"),
        extra_options: dict[str, Any] | None = None,
    ) -> VideoStream:
        """

        Apply resizing, colorspace and bit depth conversion.

        Args:
            w: Output video width
            h: Output video height
            size: set video size
            dither: set dither type (from 0 to 3) (default none)
            filter: set filter type (from 0 to 5) (default bilinear)
            out_range: set color range (from -1 to 1) (default input)
            primaries: set color primaries (from -1 to INT_MAX) (default input)
            transfer: set transfer characteristic (from -1 to INT_MAX) (default input)
            matrix: set colorspace matrix (from -1 to INT_MAX) (default input)
            in_range: set input color range (from -1 to 1) (default input)
            primariesin: set input color primaries (from -1 to INT_MAX) (default input)
            transferin: set input transfer characteristic (from -1 to INT_MAX) (default input)
            matrixin: set input colorspace matrix (from -1 to INT_MAX) (default input)
            chromal: set output chroma location (from -1 to 5) (default input)
            chromalin: set input chroma location (from -1 to 5) (default input)
            npl: set nominal peak luminance (from 0 to DBL_MAX) (default nan)
            agamma: allow approximate gamma (default true)
            param_a: parameter A, which is parameter "b" for bicubic, and the number of filter taps for lanczos (from -DBL_MAX to DBL_MAX) (default nan)
            param_b: parameter B, which is parameter "c" for bicubic (from -DBL_MAX to DBL_MAX) (default nan)
            extra_options: Extra options for the filter

        Returns:
            default: the video stream

        References:
            [FFmpeg Documentation](https://ffmpeg.org/ffmpeg-filters.html#zscale)

        """
        filter_node = filter_node_factory(
            FFMpegFilterDef(
                name="zscale", typings_input=("video",), typings_output=("video",)
            ),
            self,
            **merge(
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
                },
                extra_options,
            ),
        )
        return filter_node.video(0)
