from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from ..nodes.nodes import FilterableStream, FilterNode
from ..schema import Default, StreamType

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
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        w: str | float | int = Default("0"),
        h: str | float | int = Default("0"),
        qoffset: float | int | str = Default(-0.1),
        clear: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add region of interest to frame.

        Parameters:
        ----------

        :param str x: Region distance in pixels from the left edge of the frame.
        :param str y: Region distance in pixels from the top edge of the frame.
        :param str w: Region width in pixels.
        :param str h: Region height in pixels. The parameters x, y, w and h are expressions, and may contain the following variables: iw Width of the input frame. ih Height of the input frame.
        :param float qoffset: Quantisation offset to apply within the region. This must be a real value in the range -1 to +1. A value of zero indicates no quality change. A negative value asks for better quality (less quantisation), while a positive value asks for worse quality (greater quantisation). The range is calibrated so that the extreme values indicate the largest possible offset - if the rest of the frame is encoded with the worst possible quality, an offset of -1 indicates that this region should be encoded with the best possible quality anyway. Intermediate values are then interpolated in some codec-dependent way. For example, in 10-bit H.264 the quantisation parameter varies between -12 and 51. A typical qoffset value of -1/10 therefore indicates that this region should be encoded with a QP around one-tenth of the full range better than the rest of the frame. So, if most of the frame were to be encoded with a QP of around 30, this region would get a QP of around 24 (an offset of approximately -1/10 * (51 - -12) = -6.3). An extreme value of -1 would indicate that this region should be encoded with the best possible quality regardless of the treatment of the rest of the frame - that is, should be encoded at a QP of -12.
        :param bool clear: If set to true, remove any existing regions of interest marked on the frame before adding the new one.

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
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Copy the luma value of the second input into the alpha channel of the first input.

        Parameters:
        ----------

        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def amplify(
        self,
        *,
        radius: int | str = Default(2),
        factor: float | int | str = Default(2.0),
        threshold: float | int | str = Default(10.0),
        tolerance: float | int | str = Default(0.0),
        low: float | int | str = Default(65535.0),
        high: float | int | str = Default(65535.0),
        planes: str | float | int = Default(7),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Amplify changes between successive video frames.

        Parameters:
        ----------

        :param int radius: Set frame radius. Default is 2. Allowed range is from 1 to 63. For example radius of 3 will instruct filter to calculate average of 7 frames.
        :param float factor: Set factor to amplify difference. Default is 2. Allowed range is from 0 to 65535.
        :param float threshold: Set threshold for difference amplification. Any difference greater or equal to this value will not alter source pixel. Default is 10. Allowed range is from 0 to 65535.
        :param float tolerance: Set tolerance for difference amplification. Any difference lower to this value will not alter source pixel. Default is 0. Allowed range is from 0 to 65535.
        :param float low: Set lower limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will decrease source pixel value.
        :param float high: Set high limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will increase source pixel value.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.
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
        filename: str | float | int = Default("((void*)0)"),
        original_size: str | float | int = Default("((void*)0)"),
        fontsdir: str | float | int = Default("((void*)0)"),
        alpha: bool | int | str = Default(0),
        shaping: int | Literal["auto", "simple", "complex"] | Default = Default(-1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render ASS subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param str filename: set the filename of file to read
        :param str original_size: set the size of the original video (used to scale fonts)
        :param str fontsdir: set the directory containing the fonts to read
        :param bool alpha: enable processing of alpha channel
        :param int shaping: Set the shaping engine Available values are: ‘auto’ The default libass shaping engine, which is the best available. ‘simple’ Fast, font-agnostic shaper that can do only substitutions ‘complex’ Slower shaper using OpenType for substitutions and positioning The default is auto.

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
        _0a: float | int | str = Default(0.02),
        _0b: float | int | str = Default(0.04),
        _1a: float | int | str = Default(0.02),
        _1b: float | int | str = Default(0.04),
        _2a: float | int | str = Default(0.02),
        _2b: float | int | str = Default(0.04),
        s: int | str = Default(9),
        p: str | float | int = Default(7),
        a: int | Literal["p", "s"] | Default = Default("PARALLEL"),
        _0s: float | int | str = Default(32767.0),
        _1s: float | int | str = Default(32767.0),
        _2s: float | int | str = Default(32767.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an Adaptive Temporal Averaging Denoiser.

        Parameters:
        ----------

        :param float _0a: Set threshold A for 1st plane. Default is 0.02. Valid range is 0 to 0.3.
        :param float _0b: Set threshold B for 1st plane. Default is 0.04. Valid range is 0 to 5.
        :param float _1a: Set threshold A for 2nd plane. Default is 0.02. Valid range is 0 to 0.3.
        :param float _1b: Set threshold B for 2nd plane. Default is 0.04. Valid range is 0 to 5.
        :param float _2a: Set threshold A for 3rd plane. Default is 0.02. Valid range is 0 to 0.3.
        :param float _2b: Set threshold B for 3rd plane. Default is 0.04. Valid range is 0 to 5. Threshold A is designed to react on abrupt changes in the input signal and threshold B is designed to react on continuous changes in the input signal.
        :param int s: Set number of frames filter will use for averaging. Default is 9. Must be odd number in range [5, 129].
        :param str p: Set what planes of frame filter will use for averaging. Default is all.
        :param int a: Set what variant of algorithm filter will use for averaging. Default is p parallel. Alternatively can be set to s serial. Parallel can be faster then serial, while other way around is never true. Parallel will abort early on first change being greater then thresholds, while serial will continue processing other side of frames if they are equal or below thresholds.
        :param float _0s: Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.
        :param float _1s: Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.
        :param float _2s: Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.
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
        sizeX: int | str = Default(1),
        planes: int | str = Default("0xF"),
        sizeY: int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Average Blur filter.

        Parameters:
        ----------

        :param int sizeX: Set horizontal radius size.
        :param int planes: Set which planes to filter. By default all planes are filtered.
        :param int sizeY: Set vertical radius size, if zero it will be same as sizeX. Default is 0.
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

    def avgblur_opencl(
        self,
        *,
        sizeX: int | str = Default(1),
        planes: int | str = Default("0xF"),
        sizeY: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.1 avgblur_opencl

        Apply average blur filter.

        The filter accepts the following options:

        **sizeX**

            Set horizontal radius size. Range is [1, 1024] and default value is 1.

        **planes**

            Set which planes to filter. Default value is 0xf, by which all planes are processed.

        **sizeY**

            Set vertical radius size. Range is [1, 1024] and default value is 0. If zero, sizeX value will be used.



        Parameters:
        ----------

        :param int sizeX: Set horizontal radius size. Range is [1, 1024] and default value is 1.
        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.
        :param int sizeY: Set vertical radius size. Range is [1, 1024] and default value is 0. If zero, sizeX value will be used.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur_005fopencl

        """
        filter_node = FilterNode(
            name="avgblur_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sizeX": sizeX,
                        "planes": planes,
                        "sizeY": sizeY,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def avgblur_vulkan(
        self,
        *,
        sizeX: int | str = Default(3),
        sizeY: int | str = Default(3),
        planes: int | str = Default("0xF"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.1 avgblur_vulkan

        Apply an average blur filter, implemented on the GPU using Vulkan.

        The filter accepts the following options:

        **sizeX**

            Set horizontal radius size. Range is [1, 32] and default value is 3.

        **sizeY**

            Set vertical radius size. Range is [1, 32] and default value is 3.

        **planes**

            Set which planes to filter. Default value is 0xf, by which all planes are processed.



        Parameters:
        ----------

        :param int sizeX: Set horizontal radius size. Range is [1, 32] and default value is 3.
        :param int sizeY: Set vertical radius size. Range is [1, 32] and default value is 3.
        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur_005fvulkan

        """
        filter_node = FilterNode(
            name="avgblur_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sizeX": sizeX,
                        "sizeY": sizeY,
                        "planes": planes,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def backgroundkey(
        self,
        *,
        threshold: float | int | str = Default(0.08),
        similarity: float | int | str = Default(0.1),
        blend: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a static background into transparency.

        Parameters:
        ----------

        :param float threshold: Threshold for scene change detection.
        :param float similarity: Similarity percentage with the background.
        :param float blend: Set the blend amount for pixels that are not similar.
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

    def bbox(
        self, *, min_val: int | str = Default(16), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Compute bounding box for each frame.

        Parameters:
        ----------

        :param int min_val: Set the minimal luma value. Default is 16.
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
        self, *, action: int | Literal["start", "stop"] | Default = Default("ACTION_START"), **kwargs: Any
    ) -> "VideoStream":
        """

        Benchmark part of a filtergraph.

        Parameters:
        ----------

        :param int action: Start or stop a timer. Available values are: ‘start’ Get the current time, set it as frame metadata (using the key lavfi.bench.start_time), and forward the frame to the next filter. ‘stop’ Get the current time and fetch the lavfi.bench.start_time metadata from the input frame metadata to get the time difference. Time difference, average, maximum and minimum time (respectively t, avg, max and min) are then printed. The timestamps are expressed in seconds.

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
        sigmaS: float | int | str = Default(0.1),
        sigmaR: float | int | str = Default(0.1),
        planes: int | str = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Bilateral filter.

        Parameters:
        ----------

        :param float sigmaS: Set sigma of gaussian function to calculate spatial weight. Allowed range is 0 to 512. Default is 0.1.
        :param float sigmaR: Set sigma of gaussian function to calculate range weight. Allowed range is 0 to 1. Default is 0.1.
        :param int planes: Set planes to filter. Default is first only.
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

    def bilateral_cuda(
        self,
        *,
        sigmaS: float | int | str = Default(0.1),
        sigmaR: float | int | str = Default(0.1),
        window_size: int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.11 bilateral_cuda

        CUDA accelerated bilateral filter, an edge preserving filter. This filter is
        mathematically accurate thanks to the use of GPU acceleration. For best output
        quality, use one to one chroma subsampling, i.e. yuv444p format.

        The filter accepts the following options:

        **sigmaS**

            Set sigma of gaussian function to calculate spatial weight, also called sigma space. Allowed range is 0.1 to 512. Default is 0.1.

        **sigmaR**

            Set sigma of gaussian function to calculate color range weight, also called sigma color. Allowed range is 0.1 to 512. Default is 0.1.

        **window_size**

            Set window size of the bilateral function to determine the number of neighbours to loop on. If the number entered is even, one will be added automatically. Allowed range is 1 to 255. Default is 1.



        Parameters:
        ----------

        :param float sigmaS: Set sigma of gaussian function to calculate spatial weight, also called sigma space. Allowed range is 0.1 to 512. Default is 0.1.
        :param float sigmaR: Set sigma of gaussian function to calculate color range weight, also called sigma color. Allowed range is 0.1 to 512. Default is 0.1.
        :param int window_size: Set window size of the bilateral function to determine the number of neighbours to loop on. If the number entered is even, one will be added automatically. Allowed range is 1 to 255. Default is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral_005fcuda

        """
        filter_node = FilterNode(
            name="bilateral_cuda",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigmaS": sigmaS,
                        "sigmaR": sigmaR,
                        "window_size": window_size,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bitplanenoise(
        self,
        *,
        bitplane: int | str = Default(1),
        filter: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure bit plane noise.

        Parameters:
        ----------

        :param int bitplane: Set which plane to analyze. Default is 1.
        :param bool filter: Filter out noisy pixels from bitplane set above. Default is disabled.
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
        d: float | int | str = Default(2.0),
        picture_black_ratio_th: float | int | str = Default(0.98),
        pixel_black_th: float | int | str = Default(0.1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect video intervals that are (almost) black.

        Parameters:
        ----------

        :param float d: Set the minimum detected black duration expressed in seconds. It must be a non-negative floating point number. Default value is 2.0.
        :param float picture_black_ratio_th: Set the threshold for considering a picture "black". Express the minimum value for the ratio: nb_black_pixels / nb_pixels for which a picture is considered black. Default value is 0.98.
        :param float pixel_black_th: Set the threshold for considering a pixel "black". The threshold expresses the maximum pixel luma value for which a pixel is considered "black". The provided value is scaled according to the following equation: absolute_threshold = luma_minimum_value + pixel_black_th * luma_range_size luma_range_size and luma_minimum_value depend on the input video format, the range is [0-255] for YUV full-range formats and [16-235] for YUV non full-range formats. Default value is 0.10.

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
        self, *, amount: int | str = Default(98), threshold: int | str = Default(32), **kwargs: Any
    ) -> "VideoStream":
        """

        Detect frames that are (almost) black.

        Parameters:
        ----------

        :param int amount: The percentage of the pixels that have to be below the threshold; it defaults to 98.
        :param int threshold: The threshold below which a pixel value is considered black; it defaults to 32.

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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(-1),
        c0_expr: str | float | int = Default("((void*)0)"),
        c1_expr: str | float | int = Default("((void*)0)"),
        c2_expr: str | float | int = Default("((void*)0)"),
        c3_expr: str | float | int = Default("((void*)0)"),
        all_expr: str | float | int = Default("((void*)0)"),
        c0_opacity: float | int | str = Default(1.0),
        c1_opacity: float | int | str = Default(1.0),
        c2_opacity: float | int | str = Default(1.0),
        c3_opacity: float | int | str = Default(1.0),
        all_opacity: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blend two video frames into each other.

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
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def blend_vulkan(
        self,
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
        **kwargs: Any,
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

    def blockdetect(
        self,
        *,
        period_min: int | str = Default(3),
        period_max: int | str = Default(24),
        planes: int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blockdetect filter.

        Parameters:
        ----------

        :param int period_min: Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        :param int period_max: Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        :param int planes: Set planes to filter. Default is first only.

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
        high: float | int | str = Default("30/255."),
        low: float | int | str = Default("15/255."),
        radius: int | str = Default(50),
        block_pct: int | str = Default(80),
        block_width: int | str = Default(-1),
        block_height: int | str = Default(-1),
        planes: int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blurdetect filter.

        Parameters:
        ----------

        :param float high: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param float low: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param int radius: Define the radius to search around an edge pixel for local maxima.
        :param int block_pct: Determine blurriness only for the most significant blocks, given in percentage.
        :param int block_width: Determine blurriness for blocks of width block_width. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_height.
        :param int block_height: Determine blurriness for blocks of height block_height. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_width.
        :param int planes: Set planes to filter. Default is first only.

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
                        "block_height": block_height,
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
        luma_radius: str | float | int = Default("2"),
        luma_power: int | str = Default(2),
        chroma_radius: str | float | int = Default("((void*)0)"),
        chroma_power: int | str = Default(-1),
        alpha_radius: str | float | int = Default("((void*)0)"),
        alpha_power: int | str = Default(-1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input.

        Parameters:
        ----------

        :param str luma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int luma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str chroma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int chroma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str alpha_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int alpha_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
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

    def boxblur_opencl(
        self,
        *,
        luma_radius: str | float | int = Default("2"),
        luma_power: int | str = Default(2),
        chroma_radius: str | float | int = Default("((void*)0)"),
        chroma_power: int | str = Default(-1),
        alpha_radius: str | float | int = Default("((void*)0)"),
        alpha_power: int | str = Default(-1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.2 boxblur_opencl

        Apply a boxblur algorithm to the input video.

        It accepts the following parameters:

        **luma_radius, lr**

        **luma_power, lp**

        **chroma_radius, cr**

        **chroma_power, cp**

        **alpha_radius, ar**

        **alpha_power, ap**

        A description of the accepted options follows.

        **luma_radius, lr**

        **chroma_radius, cr**

        **alpha_radius, ar**

            Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.

        **luma_power, lp**

        **chroma_power, cp**

        **alpha_power, ap**

            Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.



        Parameters:
        ----------

        :param str luma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int luma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str chroma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int chroma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str alpha_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int alpha_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#boxblur_005fopencl

        """
        filter_node = FilterNode(
            name="boxblur_opencl",
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def bwdif(
        self,
        *,
        mode: int | Literal["send_frame", "send_field"] | Default = Default("YADIF_MODE_SEND_FIELD"),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default("YADIF_PARITY_AUTO"),
        deint: int | Literal["all", "interlaced"] | Default = Default("YADIF_DEINT_ALL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.
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

    def bwdif_cuda(
        self,
        *,
        mode: int
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("YADIF_MODE_SEND_FRAME"),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default("YADIF_PARITY_AUTO"),
        deint: int | Literal["all", "interlaced"] | Default = Default("YADIF_DEINT_ALL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.21 bwdif_cuda

        Deinterlace the input video using the bwdif algorithm, but implemented in CUDA
        so that it can work as part of a GPU accelerated pipeline with nvdec and/or
        nvenc.

        It accepts the following parameters:

        **mode**

            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.

        **parity**

            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.

        **deint**

            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif_005fcuda

        """
        filter_node = FilterNode(
            name="bwdif_cuda",
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

    def bwdif_vulkan(
        self,
        *,
        mode: int
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("YADIF_MODE_SEND_FRAME"),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default("YADIF_PARITY_AUTO"),
        deint: int | Literal["all", "interlaced"] | Default = Default("YADIF_DEINT_ALL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.3 bwdif_vulkan

        Deinterlacer using bwdif, the "Bob Weaver Deinterlacing Filter" algorithm,
        implemented on the GPU using Vulkan.

        It accepts the following parameters:

        **mode**

            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.

        **parity**

            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.

        **deint**

            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif_005fvulkan

        """
        filter_node = FilterNode(
            name="bwdif_vulkan",
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
        strength: float | int | str = Default(0.0),
        planes: str | float | int = Default(7),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Contrast Adaptive Sharpen.

        Parameters:
        ----------

        :param float strength: Set the sharpening strength. Default value is 0.
        :param str planes: Set planes to filter. Default value is to filter all planes except alpha plane.
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

    def ccrepack(self, **kwargs: Any) -> "VideoStream":
        """

        ### 11.22 ccrepack

        Repack CEA-708 closed captioning side data

        This filter fixes various issues seen with commerical encoders related to
        upstream malformed CEA-708 payloads, specifically incorrect number of tuples
        (wrong cc_count for the target FPS), and incorrect ordering of tuples (i.e.
        the CEA-608 tuples are not at the first entries in the payload).



        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#ccrepack

        """
        filter_node = FilterNode(
            name="ccrepack",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def chromaber_vulkan(
        self, *, dist_x: float | int | str = Default("0.0f"), dist_y: float | int | str = Default("0.0f"), **kwargs: Any
    ) -> "VideoStream":
        """

        ### 14.4 chromaber_vulkan

        Apply an effect that emulates chromatic aberration. Works best with RGB
        inputs, but provides a similar effect with YCbCr inputs too.

        **dist_x**

            Horizontal displacement multiplier. Each chroma pixel’s position will be multiplied by this amount, starting from the center of the image. Default is 0.

        **dist_y**

            Similarly, this sets the vertical displacement multiplier. Default is 0.



        Parameters:
        ----------

        :param float dist_x: Horizontal displacement multiplier. Each chroma pixel’s position will be multiplied by this amount, starting from the center of the image. Default is 0.
        :param float dist_y: Similarly, this sets the vertical displacement multiplier. Default is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromaber_005fvulkan

        """
        filter_node = FilterNode(
            name="chromaber_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "dist_x": dist_x,
                        "dist_y": dist_y,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromahold(
        self,
        *,
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        yuv: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray.

        Parameters:
        ----------

        :param str color: The color which will not be replaced with neutral chroma.
        :param float similarity: Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more preserved color.
        :param bool yuv: Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.
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
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        yuv: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param str color: The color which will be replaced with transparency.
        :param float similarity: Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.
        :param bool yuv: Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.
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

    def chromakey_cuda(
        self,
        *,
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        yuv: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.26 chromakey_cuda

        CUDA accelerated YUV colorspace color/chroma keying.

        This filter works like normal chromakey filter but operates on CUDA frames.
        for more details and parameters see chromakey.



        Parameters:
        ----------

        :param str color: set the chromakey key color
        :param float similarity: set the chromakey similarity value
        :param float blend: set the chromakey key blend value
        :param bool yuv: color parameter is in yuv instead of rgb

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey_005fcuda

        """
        filter_node = FilterNode(
            name="chromakey_cuda",
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def chromanr(
        self,
        *,
        thres: float | int | str = Default(30.0),
        sizew: int | str = Default(5),
        sizeh: int | str = Default(5),
        stepw: int | str = Default(1),
        steph: int | str = Default(1),
        threy: float | int | str = Default(200.0),
        threu: float | int | str = Default(200.0),
        threv: float | int | str = Default(200.0),
        distance: int | Literal["manhattan", "euclidean"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce chrominance noise.

        Parameters:
        ----------

        :param float thres: Set threshold for averaging chrominance values. Sum of absolute difference of Y, U and V pixel components of current pixel and neighbour pixels lower than this threshold will be used in averaging. Luma component is left unchanged and is copied to output. Default value is 30. Allowed range is from 1 to 200.
        :param int sizew: Set horizontal radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.
        :param int sizeh: Set vertical radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.
        :param int stepw: Set horizontal step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.
        :param int steph: Set vertical step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.
        :param float threy: Set Y threshold for averaging chrominance values. Set finer control for max allowed difference between Y components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        :param float threu: Set U threshold for averaging chrominance values. Set finer control for max allowed difference between U components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        :param float threv: Set V threshold for averaging chrominance values. Set finer control for max allowed difference between V components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        :param int distance: Set distance type used in calculations. ‘manhattan’ Absolute difference. ‘euclidean’ Difference squared. Default distance type is manhattan.
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
        cbh: int | str = Default(0),
        cbv: int | str = Default(0),
        crh: int | str = Default(0),
        crv: int | str = Default(0),
        edge: int | Literal["smear", "wrap"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift chroma.

        Parameters:
        ----------

        :param int cbh: Set amount to shift chroma-blue horizontally.
        :param int cbv: Set amount to shift chroma-blue vertically.
        :param int crh: Set amount to shift chroma-red horizontally.
        :param int crv: Set amount to shift chroma-red vertically.
        :param int edge: Set edge mode, can be smear, default, or warp.
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
        system: int
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
        | Default = Default("Rec709system"),
        cie: int | Literal["xyy", "ucs", "luv"] | Default = Default("XYY"),
        gamuts: str
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
        | Default = Default(0),
        size: int | str = Default(512),
        intensity: float | int | str = Default(0.001),
        contrast: float | int | str = Default(0.75),
        corrgamma: bool | int | str = Default(1),
        showwhite: bool | int | str = Default(0),
        gamma: float | int | str = Default(2.6),
        fill: bool | int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video CIE scope.

        Parameters:
        ----------

        :param int system: Set color system. ‘ntsc, 470m’ ‘ebu, 470bg’ ‘smpte’ ‘240m’ ‘apple’ ‘widergb’ ‘cie1931’ ‘rec709, hdtv’ ‘uhdtv, rec2020’ ‘dcip3’
        :param int cie: Set CIE system. ‘xyy’ ‘ucs’ ‘luv’
        :param str gamuts: Set what gamuts to draw. See system option for available values.
        :param int size: Set ciescope size, by default set to 512.
        :param float intensity: Set intensity used to map input pixel values to CIE diagram.
        :param float contrast: Set contrast used to draw tongue colors that are out of active color system gamut.
        :param bool corrgamma: Correct gamma displayed on scope, by default enabled.
        :param bool showwhite: Show white point on CIE diagram, by default disabled.
        :param float gamma: Set input gamma. Used only with XYZ input color space.
        :param bool fill: Fill with CIE colors. By default is enabled.

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
        mv: str | Literal["pf", "bf", "bb"] | Default = Default(0),
        qp: bool | int | str = Default(0),
        mv_type: str | Literal["fp", "bp"] | Default = Default(0),
        frame_type: str | Literal["if", "pf", "bf"] | Default = Default(0),
        block: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Visualize information about some codecs.

        Parameters:
        ----------

        :param str mv: Set motion vectors to visualize. Available flags for mv are: ‘pf’ forward predicted MVs of P-frames ‘bf’ forward predicted MVs of B-frames ‘bb’ backward predicted MVs of B-frames
        :param bool qp: Display quantization parameters using the chroma planes.
        :param str mv_type: Set motion vectors type to visualize. Includes MVs from all frames unless specified by frame_type option. Available flags for mv_type are: ‘fp’ forward predicted MVs ‘bp’ backward predicted MVs
        :param str frame_type: Set frame type to visualize motion vectors of. Available flags for frame_type are: ‘if’ intra-coded frames (I-frames) ‘pf’ predicted frames (P-frames) ‘bf’ bi-directionally predicted frames (B-frames)
        :param bool block: Display block partition structure using the luma plane.
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
        rs: float | int | str = Default(0.0),
        gs: float | int | str = Default(0.0),
        bs: float | int | str = Default(0.0),
        rm: float | int | str = Default(0.0),
        gm: float | int | str = Default(0.0),
        bm: float | int | str = Default(0.0),
        rh: float | int | str = Default(0.0),
        gh: float | int | str = Default(0.0),
        bh: float | int | str = Default(0.0),
        pl: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color balance.

        Parameters:
        ----------

        :param float rs: Adjust red, green and blue shadows (darkest pixels).
        :param float gs: Adjust red, green and blue shadows (darkest pixels).
        :param float bs: Adjust red, green and blue shadows (darkest pixels).
        :param float rm: Adjust red, green and blue midtones (medium pixels).
        :param float gm: Adjust red, green and blue midtones (medium pixels).
        :param float bm: Adjust red, green and blue midtones (medium pixels).
        :param float rh: Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float gh: Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float bh: Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param bool pl: Preserve lightness when changing color balance. Default is disabled.
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
        rr: float | int | str = Default(1.0),
        rg: float | int | str = Default(0.0),
        rb: float | int | str = Default(0.0),
        ra: float | int | str = Default(0.0),
        gr: float | int | str = Default(0.0),
        gg: float | int | str = Default(1.0),
        gb: float | int | str = Default(0.0),
        ga: float | int | str = Default(0.0),
        br: float | int | str = Default(0.0),
        bg: float | int | str = Default(0.0),
        bb: float | int | str = Default(1.0),
        ba: float | int | str = Default(0.0),
        ar: float | int | str = Default(0.0),
        ag: float | int | str = Default(0.0),
        ab: float | int | str = Default(0.0),
        aa: float | int | str = Default(1.0),
        pc: int | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default(0),
        pa: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors by mixing color channels.

        Parameters:
        ----------

        :param float rr: Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        :param float rg: Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        :param float rb: Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        :param float ra: Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        :param float gr: Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        :param float gg: Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        :param float gb: Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        :param float ga: Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        :param float br: Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        :param float bg: Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        :param float bb: Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        :param float ba: Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        :param float ar: Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        :param float ag: Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        :param float ab: Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        :param float aa: Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        :param int pc: Set preserve color mode. The accepted values are: ‘none’ Disable color preserving, this is default. ‘lum’ Preserve luminance. ‘max’ Preserve max value of RGB triplet. ‘avg’ Preserve average value of RGB triplet. ‘sum’ Preserve sum value of RGB triplet. ‘nrm’ Preserve normalized value of RGB triplet. ‘pwr’ Preserve power value of RGB triplet.
        :param float pa: Set the preserve color amount when changing colors. Allowed range is from [0.0, 1.0]. Default is 0.0, thus disabled.
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
        rc: float | int | str = Default(0.0),
        gm: float | int | str = Default(0.0),
        by: float | int | str = Default(0.0),
        rcw: float | int | str = Default(0.0),
        gmw: float | int | str = Default(0.0),
        byw: float | int | str = Default(0.0),
        pl: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color contrast between RGB components.

        Parameters:
        ----------

        :param float rc: Set the red-cyan contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float gm: Set the green-magenta contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float by: Set the blue-yellow contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float rcw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float gmw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float byw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float pl: Set the amount of preserving lightness. Default value is 0.0. Allowed range is from 0.0 to 1.0.
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
        rl: float | int | str = Default(0.0),
        bl: float | int | str = Default(0.0),
        rh: float | int | str = Default(0.0),
        bh: float | int | str = Default(0.0),
        saturation: float | int | str = Default(1.0),
        analyze: int | Literal["manual", "average", "minmax", "median"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color white balance selectively for blacks and whites.

        Parameters:
        ----------

        :param float rl: Set the red shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float bl: Set the blue shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float rh: Set the red highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float bh: Set the blue highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float saturation: Set the amount of saturation. Allowed range is from -3.0 to 3.0. Default value is 1.
        :param int analyze: If set to anything other than manual it will analyze every frame and use derived parameters for filtering output frame. Possible values are: ‘manual’ ‘average’ ‘minmax’ ‘median’ Default value is manual.
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
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color range into gray. Operates on RGB colors.

        Parameters:
        ----------

        :param str color: The color which will not be replaced with neutral gray.
        :param float similarity: Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels fully gray. Higher values result in more preserved color.
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
        hue: float | int | str = Default(0.0),
        saturation: float | int | str = Default(0.5),
        lightness: float | int | str = Default(0.5),
        mix: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Overlay a solid color on the video stream.

        Parameters:
        ----------

        :param float hue: Set the color hue. Allowed range is from 0 to 360. Default value is 0.
        :param float saturation: Set the color saturation. Allowed range is from 0 to 1. Default value is 0.5.
        :param float lightness: Set the color lightness. Allowed range is from 0 to 1. Default value is 0.5.
        :param float mix: Set the mix of source lightness. By default is set to 1.0. Allowed range is from 0.0 to 1.0.
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
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain color into transparency. Operates on RGB colors.

        Parameters:
        ----------

        :param str color: Set the color for which alpha will be set to 0 (full transparency). See (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default is black.
        :param float similarity: Set the radius from the key color within which other colors also have full transparency. The computed distance is related to the unit fractional distance in 3D space between the RGB values of the key color and the pixel’s color. Range is 0.01 to 1.0. 0.01 matches within a very small radius around the exact key color, while 1.0 matches everything. Default is 0.01.
        :param float blend: Set how the alpha value for pixels that fall outside the similarity radius is computed. 0.0 makes pixels either fully transparent or fully opaque. Higher values result in semi-transparent pixels, with greater transparency the more similar the pixel color is to the key color. Range is 0.0 to 1.0. Default is 0.0.
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

    def colorkey_opencl(
        self,
        *,
        color: str | float | int = Default("black"),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.3 colorkey_opencl

        RGB colorspace color keying.

        The filter accepts the following options:

        **color**

            The color which will be replaced with transparency.

        **similarity**

            Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.

        **blend**

            Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.



        Parameters:
        ----------

        :param str color: The color which will be replaced with transparency.
        :param float similarity: Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorkey_005fopencl

        """
        filter_node = FilterNode(
            name="colorkey_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color": color,
                        "similarity": similarity,
                        "blend": blend,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def colorlevels(
        self,
        *,
        rimin: float | int | str = Default(0.0),
        gimin: float | int | str = Default(0.0),
        bimin: float | int | str = Default(0.0),
        aimin: float | int | str = Default(0.0),
        rimax: float | int | str = Default(1.0),
        gimax: float | int | str = Default(1.0),
        bimax: float | int | str = Default(1.0),
        aimax: float | int | str = Default(1.0),
        romin: float | int | str = Default(0.0),
        gomin: float | int | str = Default(0.0),
        bomin: float | int | str = Default(0.0),
        aomin: float | int | str = Default(0.0),
        romax: float | int | str = Default(1.0),
        gomax: float | int | str = Default(1.0),
        bomax: float | int | str = Default(1.0),
        aomax: float | int | str = Default(1.0),
        preserve: int | Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the color levels.

        Parameters:
        ----------

        :param float rimin: Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float gimin: Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float bimin: Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float aimin: Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        :param float rimax: Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        :param float gimax: Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        :param float bimax: Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        :param float aimax: Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        :param float romin: Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        :param float gomin: Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        :param float bomin: Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        :param float aomin: Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        :param float romax: Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        :param float gomax: Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        :param float bomax: Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        :param float aomax: Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        :param int preserve: Set preserve color mode. The accepted values are: ‘none’ Disable color preserving, this is default. ‘lum’ Preserve luminance. ‘max’ Preserve max value of RGB triplet. ‘avg’ Preserve average value of RGB triplet. ‘sum’ Preserve sum value of RGB triplet. ‘nrm’ Preserve normalized value of RGB triplet. ‘pwr’ Preserve power value of RGB triplet.
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
        patch_size: str | float | int = Default("64x64"),
        nb_patches: int | str = Default(0),
        type: int | Literal["relative", "absolute"] | Default = Default(1),
        kernel: int | Literal["euclidean", "weuclidean"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply custom Color Maps to video stream.

        Parameters:
        ----------

        :param str patch_size: Set the source and target video stream patch size in pixels.
        :param int nb_patches: Set the max number of used patches from source and target video stream. Default value is number of patches available in additional video streams. Max allowed number of patches is 64.
        :param int type: Set the adjustments used for target colors. Can be relative or absolute. Defaults is absolute.
        :param int kernel: Set the kernel used to measure color differences between mapped colors. The accepted values are: ‘euclidean’ ‘weuclidean’ Default is euclidean.
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
        src: int
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("COLOR_MODE_NONE"),
        dst: int
        | Literal["bt709", "fcc", "bt601", "bt470", "bt470bg", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("COLOR_MODE_NONE"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert color matrix.

        Parameters:
        ----------

        :param int src: Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020
        :param int dst: Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020
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
        all: int
        | Literal["bt470m", "bt470bg", "bt601-6-525", "bt601-6-625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("CS_UNSPECIFIED"),
        space: int
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default("AVCOL_SPC_UNSPECIFIED"),
        range: int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        primaries: int
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
        | Default = Default("AVCOL_PRI_UNSPECIFIED"),
        trc: int
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
        | Default = Default("AVCOL_TRC_UNSPECIFIED"),
        format: int
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
        | Default = Default("AV_PIX_FMT_NONE"),
        fast: bool | int | str = Default(0),
        dither: int | Literal["none", "fsb"] | Default = Default("DITHER_NONE"),
        wpadapt: int | Literal["bradford", "vonkries", "identity"] | Default = Default("WP_ADAPT_BRADFORD"),
        iall: int
        | Literal["bt470m", "bt470bg", "bt601-6-525", "bt601-6-625", "bt709", "smpte170m", "smpte240m", "bt2020"]
        | Default = Default("CS_UNSPECIFIED"),
        ispace: int
        | Literal["bt709", "fcc", "bt470bg", "smpte170m", "smpte240m", "ycgco", "gbr", "bt2020nc", "bt2020ncl"]
        | Default = Default("AVCOL_SPC_UNSPECIFIED"),
        irange: int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        iprimaries: int
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
        | Default = Default("AVCOL_PRI_UNSPECIFIED"),
        itrc: int
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
        | Default = Default("AVCOL_TRC_UNSPECIFIED"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert between colorspaces.

        Parameters:
        ----------

        :param int all: Set all color properties together
        :param int space: Output colorspace
        :param int range: Output color range
        :param int primaries: Output color primaries
        :param int trc: Output transfer characteristics
        :param int format: Output pixel format
        :param bool fast: Ignore primary chromaticity and gamma correction
        :param int dither: Dithering mode
        :param int wpadapt: Whitepoint adaptation method
        :param int iall: Set all input color properties together
        :param int ispace: Input colorspace
        :param int irange: Input color range
        :param int iprimaries: Input color primaries
        :param int itrc: Input transfer characteristics
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

    def colorspace_cuda(
        self,
        *,
        range: int | Literal["tv", "mpeg", "pc", "jpeg"] | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.42 colorspace_cuda

        CUDA accelerated implementation of the colorspace filter.

        It is by no means feature complete compared to the software colorspace filter,
        and at the current time only supports color range conversion between jpeg/full
        and mpeg/limited range.

        The filter accepts the following options:

        **range**

            Specify output color range. The accepted values are: ‘tv’ TV (restricted) range ‘mpeg’ MPEG (restricted) range ‘pc’ PC (full) range ‘jpeg’ JPEG (full) range



        Parameters:
        ----------

        :param int range: Specify output color range. The accepted values are: ‘tv’ TV (restricted) range ‘mpeg’ MPEG (restricted) range ‘pc’ PC (full) range ‘jpeg’ JPEG (full) range

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace_005fcuda

        """
        filter_node = FilterNode(
            name="colorspace_cuda",
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

    def colortemperature(
        self,
        *,
        temperature: float | int | str = Default(6500.0),
        mix: float | int | str = Default(1.0),
        pl: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust color temperature of video.

        Parameters:
        ----------

        :param float temperature: Set the temperature in Kelvin. Allowed range is from 1000 to 40000. Default value is 6500 K.
        :param float mix: Set mixing with filtered output. Allowed range is from 0 to 1. Default value is 1.
        :param float pl: Set the amount of preserving lightness. Allowed range is from 0 to 1. Default value is 0.
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
        _0m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _1m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _2m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _3m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _0rdiv: float | int | str = Default(0.0),
        _1rdiv: float | int | str = Default(0.0),
        _2rdiv: float | int | str = Default(0.0),
        _3rdiv: float | int | str = Default(0.0),
        _0bias: float | int | str = Default(0.0),
        _1bias: float | int | str = Default(0.0),
        _2bias: float | int | str = Default(0.0),
        _3bias: float | int | str = Default(0.0),
        _0mode: int | Literal["square", "row", "column"] | Default = Default("MATRIX_SQUARE"),
        _1mode: int | Literal["square", "row", "column"] | Default = Default("MATRIX_SQUARE"),
        _2mode: int | Literal["square", "row", "column"] | Default = Default("MATRIX_SQUARE"),
        _3mode: int | Literal["square", "row", "column"] | Default = Default("MATRIX_SQUARE"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply convolution filter.

        Parameters:
        ----------

        :param str _0m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        :param str _1m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        :param str _2m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        :param str _3m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        :param float _0rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        :param float _1rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        :param float _2rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        :param float _3rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        :param float _0bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        :param float _1bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        :param float _2bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        :param float _3bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        :param int _0mode: Set matrix mode for each plane. Can be square, row or column. Default is square.
        :param int _1mode: Set matrix mode for each plane. Can be square, row or column. Default is square.
        :param int _2mode: Set matrix mode for each plane. Can be square, row or column. Default is square.
        :param int _3mode: Set matrix mode for each plane. Can be square, row or column. Default is square.
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

    def convolution_opencl(
        self,
        *,
        _0m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _1m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _2m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _3m: str | float | int = Default("0 0 0 0 1 0 0 0 0"),
        _0rdiv: float | int | str = Default(1.0),
        _1rdiv: float | int | str = Default(1.0),
        _2rdiv: float | int | str = Default(1.0),
        _3rdiv: float | int | str = Default(1.0),
        _0bias: float | int | str = Default(0.0),
        _1bias: float | int | str = Default(0.0),
        _2bias: float | int | str = Default(0.0),
        _3bias: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.4 convolution_opencl

        Apply convolution of 3x3, 5x5, 7x7 matrix.

        The filter accepts the following options:

        **0m**

        **1m**

        **2m**

        **3m**

            Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed numbers. Default value for each plane is 0 0 0 0 1 0 0 0 0.

        **0rdiv**

        **1rdiv**

        **2rdiv**

        **3rdiv**

            Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements. The option value must be a float number greater or equal to 0.0. Default value is 1.0.

        **0bias**

        **1bias**

        **2bias**

        **3bias**

            Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. The option value must be a float number greater or equal to 0.0. Default value is 0.0.



        Parameters:
        ----------

        :param str _0m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed numbers. Default value for each plane is 0 0 0 0 1 0 0 0 0.
        :param str _1m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed numbers. Default value for each plane is 0 0 0 0 1 0 0 0 0.
        :param str _2m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed numbers. Default value for each plane is 0 0 0 0 1 0 0 0 0.
        :param str _3m: Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed numbers. Default value for each plane is 0 0 0 0 1 0 0 0 0.
        :param float _0rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements. The option value must be a float number greater or equal to 0.0. Default value is 1.0.
        :param float _1rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements. The option value must be a float number greater or equal to 0.0. Default value is 1.0.
        :param float _2rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements. The option value must be a float number greater or equal to 0.0. Default value is 1.0.
        :param float _3rdiv: Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements. The option value must be a float number greater or equal to 0.0. Default value is 1.0.
        :param float _0bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. The option value must be a float number greater or equal to 0.0. Default value is 0.0.
        :param float _1bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. The option value must be a float number greater or equal to 0.0. Default value is 0.0.
        :param float _2bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. The option value must be a float number greater or equal to 0.0. Default value is 0.0.
        :param float _3bias: Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. The option value must be a float number greater or equal to 0.0. Default value is 0.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#convolution_005fopencl

        """
        filter_node = FilterNode(
            name="convolution_opencl",
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
        planes: int | str = Default(7),
        impulse: int | Literal["first", "all"] | Default = Default(1),
        noise: float | int | str = Default(1e-07),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convolve first video stream with second video stream.

        Parameters:
        ----------

        :param int planes: Set which planes to process.
        :param int impulse: Set which impulse video frames will be processed, can be first or all. Default is all.
        :param float noise: set noise
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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
        list_filters: bool | int | str = Default(0),
        list_generators: bool | int | str = Default(0),
        filter: str | float | int = Default("((void*)0)"),
        output_rect: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video filtering using CoreImage API.

        Parameters:
        ----------

        :param bool list_filters: List all available filters and generators along with all their respective options as well as possible minimum and maximum values along with the default values. list_filters=true
        :param bool list_generators: list available generators
        :param str filter: Specify all filters by their respective name and options. Use list_filters to determine all valid filter names and options. Numerical options are specified by a float value and are automatically clamped to their respective value range. Vector and color options have to be specified by a list of space separated float values. Character escaping has to be done. A special option name default is available to use default options for a filter. It is required to specify either default or at least one of the filter options. All omitted options are used with their default values. The syntax of the filter string is as follows: filter=<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...][#<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...]][#...]
        :param str output_rect: Specify a rectangle where the output of the filter chain is copied into the input image. It is given by a list of space separated float values: output_rect=x\ y\ width\ height If not given, the output rectangle equals the dimensions of the input image. The output rectangle is automatically cropped at the borders of the input image. Negative values are valid for each component. output_rect=25\ 25\ 100\ 100

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
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the correlation between two video streams.

        Parameters:
        ----------

        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def cover_rect(
        self,
        *,
        cover: str | float | int = Default("((void*)0)"),
        mode: int | Literal["cover", "blur"] | Default = Default("MODE_BLUR"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find and cover a user specified object.

        Parameters:
        ----------

        :param str cover: Filepath of the optional cover image, needs to be in yuv420.
        :param int mode: Set covering mode. It accepts the following values: ‘cover’ cover it by the supplied image ‘blur’ cover it by interpolating the surrounding pixels Default value is blur.

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
        out_w: str | float | int = Default("iw"),
        out_h: str | float | int = Default("ih"),
        x: str | float | int = Default("(in_w-out_w)/2"),
        y: str | float | int = Default("(in_h-out_h)/2"),
        keep_aspect: bool | int | str = Default(0),
        exact: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Crop the input video.

        Parameters:
        ----------

        :param str out_w: The width of the output video. It defaults to iw. This expression is evaluated only once during the filter configuration, or when the ‘w’ or ‘out_w’ command is sent.
        :param str out_h: The height of the output video. It defaults to ih. This expression is evaluated only once during the filter configuration, or when the ‘h’ or ‘out_h’ command is sent.
        :param str x: The horizontal position, in the input video, of the left edge of the output video. It defaults to (in_w-out_w)/2. This expression is evaluated per-frame.
        :param str y: The vertical position, in the input video, of the top edge of the output video. It defaults to (in_h-out_h)/2. This expression is evaluated per-frame.
        :param bool keep_aspect: If set to 1 will force the output display aspect ratio to be the same of the input, by changing the output sample aspect ratio. It defaults to 0.
        :param bool exact: Enable exact cropping. If enabled, subsampled videos will be cropped at exact width/height/x/y as specified and will not be rounded to nearest smaller value. It defaults to 0.

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
        limit: float | int | str = Default("24.0/255"),
        round: int | str = Default(16),
        reset: int | str = Default(0),
        skip: int | str = Default(2),
        max_outliers: int | str = Default(0),
        mode: int | Literal["black", "mvedges"] | Default = Default("MODE_BLACK"),
        high: float | int | str = Default("25/255."),
        low: float | int | str = Default("15/255."),
        mv_threshold: int | str = Default(8),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Auto-detect crop size.

        Parameters:
        ----------

        :param float limit: Set higher black value threshold, which can be optionally specified from nothing (0) to everything (255 for 8-bit based formats). An intensity value greater to the set value is considered non-black. It defaults to 24. You can also specify a value between 0.0 and 1.0 which will be scaled depending on the bitdepth of the pixel format.
        :param int round: The value which the width/height should be divisible by. It defaults to 16. The offset is automatically adjusted to center the video. Use 2 to get only even dimensions (needed for 4:2:2 video). 16 is best when encoding to most video codecs.
        :param int reset: Set the counter that determines after how many frames cropdetect will reset the previously detected largest video area and start over to detect the current optimal crop area. Default value is 0. This can be useful when channel logos distort the video area. 0 indicates ’never reset’, and returns the largest area encountered during playback.
        :param int skip: Set the number of initial frames for which evaluation is skipped. Default is 2. Range is 0 to INT_MAX.
        :param int max_outliers: Threshold count of outliers
        :param int mode: Depending on mode crop detection is based on either the mere black value of surrounding pixels or a combination of motion vectors and edge pixels. ‘black’ Detect black pixels surrounding the playing video. For fine control use option limit. ‘mvedges’ Detect the playing video by the motion vectors inside the video and scanning for edge pixels typically forming the border of a playing video.
        :param float high: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 5/255, and default value for high is 15/255.
        :param float low: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 5/255, and default value for high is 15/255.
        :param int mv_threshold: Set motion in pixel units as threshold for motion detection. It defaults to 8.
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
        cue: int | str = Default(0),
        preroll: int | str = Default(0),
        buffer: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Delay filtering to match a cue.

        Parameters:
        ----------

        :param int cue: The cue timestamp expressed in a UNIX timestamp in microseconds. Default is 0.
        :param int preroll: The duration of content to pass on as preroll expressed in seconds. Default is 0.
        :param int buffer: The maximum duration of content to buffer before waiting for the cue expressed in seconds. Default is 0.

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
        preset: int
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
        | Default = Default("PRESET_NONE"),
        master: str | float | int = Default("((void*)0)"),
        red: str | float | int = Default("((void*)0)"),
        green: str | float | int = Default("((void*)0)"),
        blue: str | float | int = Default("((void*)0)"),
        all: str | float | int = Default("((void*)0)"),
        psfile: str | float | int = Default("((void*)0)"),
        plot: str | float | int = Default("((void*)0)"),
        interp: int | Literal["natural", "pchip"] | Default = Default("INTERP_NATURAL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust components curves.

        Parameters:
        ----------

        :param int preset: Select one of the available color presets. This option can be used in addition to the r, g, b parameters; in this case, the later options takes priority on the preset values. Available presets are: ‘none’ ‘color_negative’ ‘cross_process’ ‘darker’ ‘increase_contrast’ ‘lighter’ ‘linear_contrast’ ‘medium_contrast’ ‘negative’ ‘strong_contrast’ ‘vintage’ Default is none.
        :param str master: Set the master key points. These points will define a second pass mapping. It is sometimes called a "luminance" or "value" mapping. It can be used with r, g, b or all since it acts like a post-processing LUT.
        :param str red: Set the key points for the red component.
        :param str green: Set the key points for the green component.
        :param str blue: Set the key points for the blue component.
        :param str all: Set the key points for all components (not including master). Can be used in addition to the other key points component options. In this case, the unset component(s) will fallback on this all setting.
        :param str psfile: Specify a Photoshop curves file (.acv) to import the settings from.
        :param str plot: Save Gnuplot script of the curves in specified file.
        :param int interp: Specify the kind of interpolation. Available algorithms are: ‘natural’ Natural cubic spline using a piece-wise cubic polynomial that is twice continuously differentiable. ‘pchip’ Monotonic cubic spline using a piecewise cubic Hermite interpolating polynomial (PCHIP).
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
        size: str | float | int = Default("hd720"),
        x: int | str = Default(0),
        y: int | str = Default(0),
        mode: int | Literal["mono", "color", "color2"] | Default = Default(0),
        axis: bool | int | str = Default(0),
        opacity: float | int | str = Default(0.75),
        format: int | Literal["hex", "dec"] | Default = Default(0),
        components: int | str = Default(15),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video data analysis.

        Parameters:
        ----------

        :param str size: Set output video size.
        :param int x: Set x offset from where to pick pixels.
        :param int y: Set y offset from where to pick pixels.
        :param int mode: Set scope mode, can be one of the following: ‘mono’ Draw hexadecimal pixel values with white color on black background. ‘color’ Draw hexadecimal pixel values with input video pixel color on black background. ‘color2’ Draw hexadecimal pixel values on color background picked from input video, the text color is picked in such way so its always visible.
        :param bool axis: Draw rows and columns numbers on left and top of video.
        :param float opacity: Set background opacity.
        :param int format: Set display number format. Can be hex, or dec. Default is hex.
        :param int components: Set pixel components to display. By default all pixel components are displayed.

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
        angle: float | int | str = Default(45.0),
        radius: float | int | str = Default(5.0),
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Directional Blur filter.

        Parameters:
        ----------

        :param float angle: Set angle of directional blur. Default is 45.
        :param float radius: Set radius of directional blur. Default is 5.
        :param int planes: Set which planes to filter. By default all planes are filtered.
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
        sigma: float | int | str = Default(0.0),
        overlap: int | str = Default(-1),
        expr: str | float | int = Default("((void*)0)"),
        n: int | str = Default(3),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise frames using 2D DCT.

        Parameters:
        ----------

        :param float sigma: Set the noise sigma constant. This sigma defines a hard threshold of 3 * sigma; every DCT coefficient (absolute value) below this threshold with be dropped. If you need a more advanced filtering, see expr. Default is 0.
        :param int overlap: Set number overlapping pixels for each block. Since the filter can be slow, you may want to reduce this value, at the cost of a less effective filter and the risk of various artefacts. If the overlapping value doesn’t permit processing the whole input width or height, a warning will be displayed and according borders won’t be denoised. Default value is blocksize-1, which is the best possible setting.
        :param str expr: Set the coefficient factor expression. For each coefficient of a DCT block, this expression will be evaluated as a multiplier value for the coefficient. If this is option is set, the sigma option will be ignored. The absolute value of the coefficient can be accessed through the c variable.
        :param int n: Set the blocksize using the number of bits. 1<<n defines the blocksize, which is the width and height of the processed blocks. The default value is 3 (8x8) and can be raised to 4 for a blocksize of 16x16. Note that changing this setting has huge consequences on the speed processing. Also, a larger block size does not necessarily means a better de-noising.
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
        _1thr: float | int | str = Default(0.02),
        _2thr: float | int | str = Default(0.02),
        _3thr: float | int | str = Default(0.02),
        _4thr: float | int | str = Default(0.02),
        range: int | str = Default(16),
        direction: float | int | str = Default("2*3.14159265358979323846264338327950288"),
        blur: bool | int | str = Default(1),
        coupling: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Debands video.

        Parameters:
        ----------

        :param float _1thr: Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        :param float _2thr: Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        :param float _3thr: Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        :param float _4thr: Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        :param int range: Banding detection range in pixels. Default is 16. If positive, random number in range 0 to set value will be used. If negative, exact absolute value will be used. The range defines square of four pixels around current pixel.
        :param float direction: Set direction in radians from which four pixel will be compared. If positive, random direction from 0 to set direction will be picked. If negative, exact of absolute value will be picked. For example direction 0, -PI or -2*PI radians will pick only pixels on same row and -PI/2 will pick only pixels on same column.
        :param bool blur: If enabled, current pixel is compared with average value of all four surrounding pixels. The default is enabled. If disabled current pixel is compared with all four surrounding pixels. The pixel is considered banded if only all four differences with surrounding pixels are less than threshold.
        :param bool coupling: If enabled, current pixel is changed if and only if all pixel components are banded, e.g. banding detection threshold is triggered for all color components. The default is disabled.
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
        filter: int | Literal["weak", "strong"] | Default = Default("STRONG"),
        block: int | str = Default(8),
        alpha: float | int | str = Default(0.098),
        beta: float | int | str = Default(0.05),
        gamma: float | int | str = Default(0.05),
        delta: float | int | str = Default(0.05),
        planes: int | str = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deblock video.

        Parameters:
        ----------

        :param int filter: Set filter type, can be weak or strong. Default is strong. This controls what kind of deblocking is applied.
        :param int block: Set size of block, allowed range is from 4 to 512. Default is 8.
        :param float alpha: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float beta: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float gamma: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float delta: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param int planes: Set planes to filter. Default is to filter all available planes.
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
        planes: int | str = Default(7),
        impulse: int | Literal["first", "all"] | Default = Default(1),
        noise: float | int | str = Default(1e-07),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deconvolve first video stream with second video stream.

        Parameters:
        ----------

        :param int planes: Set which planes to process.
        :param int impulse: Set which impulse video frames will be processed, can be first or all. Default is all.
        :param float noise: Set noise when doing divisions. Default is 0.0000001. Useful when width and height are not same and not power of 2 or if stream prior to convolving had noise.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def dedot(
        self,
        *,
        m: str | Literal["dotcrawl", "rainbows"] | Default = Default(3),
        lt: float | int | str = Default(0.079),
        tl: float | int | str = Default(0.079),
        tc: float | int | str = Default(0.058),
        ct: float | int | str = Default(0.019),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Reduce cross-luminance and cross-color.

        Parameters:
        ----------

        :param str m: Set mode of operation. Can be combination of dotcrawl for cross-luminance reduction and/or rainbows for cross-color reduction.
        :param float lt: Set spatial luma threshold. Lower values increases reduction of cross-luminance.
        :param float tl: Set tolerance for temporal luma. Higher values increases reduction of cross-luminance.
        :param float tc: Set tolerance for chroma temporal variation. Higher values increases reduction of cross-color.
        :param float ct: Set temporal chroma threshold. Lower values increases reduction of cross-color.
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
        threshold0: int | str = Default(65535),
        threshold1: int | str = Default(65535),
        threshold2: int | str = Default(65535),
        threshold3: int | str = Default(65535),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply deflate effect.

        Parameters:
        ----------

        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
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
        size: int | str = Default(5),
        mode: int | Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | Default = Default(0),
        bypass: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove temporal frame luminance variations.

        Parameters:
        ----------

        :param int size: Set moving-average filter size in frames. Default is 5. Allowed range is 2 - 129.
        :param int mode: Set averaging mode to smooth temporal luminance variations. Available values are: ‘am’ Arithmetic mean ‘gm’ Geometric mean ‘hm’ Harmonic mean ‘qm’ Quadratic mean ‘cm’ Cubic mean ‘pm’ Power mean ‘median’ Median
        :param bool bypass: Do not actually modify frame. Useful when one only wants metadata.

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

    def dejudder(self, *, cycle: int | str = Default(4), **kwargs: Any) -> "VideoStream":
        """

        Remove judder produced by pullup.

        Parameters:
        ----------

        :param int cycle: Specify the length of the window over which the judder repeats. Accepts any integer greater than 1. Useful values are: ‘4’ If the original was telecined from 24 to 30 fps (Film to NTSC). ‘5’ If the original was telecined from 25 to 30 fps (PAL to NTSC). ‘20’ If a mixture of the two. The default is ‘4’.

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
        x: str | float | int = Default("-1"),
        y: str | float | int = Default("-1"),
        w: str | float | int = Default("-1"),
        h: str | float | int = Default("-1"),
        show: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove logo from input video.

        Parameters:
        ----------

        :param str x: Specify the top left corner coordinates of the logo. They must be specified.
        :param str y: Specify the top left corner coordinates of the logo. They must be specified.
        :param str w: Specify the width and height of the logo to clear. They must be specified.
        :param str h: Specify the width and height of the logo to clear. They must be specified.
        :param bool show: When set to 1, a green rectangle is drawn on the screen to simplify finding the right x, y, w, and h parameters. The default value is 0. The rectangle is drawn on the outermost pixels which will be (partly) replaced with interpolated values. The values of the next pixels immediately outside this rectangle in each direction will be used to compute the interpolated pixel values inside the rectangle.
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
        filter_type: int | Literal["derain", "dehaze"] | Default = Default(0),
        dnn_backend: int | str = Default(1),
        model: str | float | int = Default("((void*)0)"),
        input: str | float | int = Default("x"),
        output: str | float | int = Default("y"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply derain filter to the input.

        Parameters:
        ----------

        :param int filter_type: Specify which filter to use. This option accepts the following values: ‘derain’ Derain filter. To conduct derain filter, you need to use a derain model. ‘dehaze’ Dehaze filter. To conduct dehaze filter, you need to use a dehaze model. Default value is ‘derain’.
        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow can load files for only its format.
        :param str input: input name of the model
        :param str output: output name of the model
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
        x: int | str = Default(-1),
        y: int | str = Default(-1),
        w: int | str = Default(-1),
        h: int | str = Default(-1),
        rx: int | str = Default(16),
        ry: int | str = Default(16),
        edge: int | Literal["blank", "original", "clamp", "mirror"] | Default = Default("FILL_MIRROR"),
        blocksize: int | str = Default(8),
        contrast: int | str = Default(125),
        search: int | Literal["exhaustive", "less"] | Default = Default("EXHAUSTIVE"),
        filename: str | float | int = Default("((void*)0)"),
        opencl: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Stabilize shaky video.

        Parameters:
        ----------

        :param int x: Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        :param int y: Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        :param int w: Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        :param int h: Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        :param int rx: Specify the maximum extent of movement in x and y directions in the range 0-64 pixels. Default 16.
        :param int ry: Specify the maximum extent of movement in x and y directions in the range 0-64 pixels. Default 16.
        :param int edge: Specify how to generate pixels to fill blanks at the edge of the frame. Available values are: ‘blank, 0’ Fill zeroes at blank locations ‘original, 1’ Original image at blank locations ‘clamp, 2’ Extruded edge value at blank locations ‘mirror, 3’ Mirrored edge at blank locations Default value is ‘mirror’.
        :param int blocksize: Specify the blocksize to use for motion search. Range 4-128 pixels, default 8.
        :param int contrast: Specify the contrast threshold for blocks. Only blocks with more than the specified contrast (difference between darkest and lightest pixels) will be considered. Range 1-255, default 125.
        :param int search: Specify the search strategy. Available values are: ‘exhaustive, 0’ Set exhaustive search ‘less, 1’ Set less exhaustive search. Default value is ‘exhaustive’.
        :param str filename: If set then a detailed log of the motion search is written to the specified file.
        :param bool opencl: ignored

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

    def deshake_opencl(
        self,
        *,
        tripod: bool | int | str = Default(0),
        debug: bool | int | str = Default(0),
        adaptive_crop: bool | int | str = Default(1),
        refine_features: bool | int | str = Default(1),
        smooth_strength: float | int | str = Default("0.0f"),
        smooth_window_multiplier: float | int | str = Default(2.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.6 deshake_opencl

        Feature-point based video stabilization filter.

        The filter accepts the following options:

        **tripod**

            Simulates a tripod by preventing any camera movement whatsoever from the original frame. Defaults to 0.

        **debug**

            Whether or not additional debug info should be displayed, both in the processed output and in the console. Note that in order to see console debug output you will also need to pass -v verbose to ffmpeg. Viewing point matches in the output video is only supported for RGB input. Defaults to 0.

        **adaptive_crop**

            Whether or not to do a tiny bit of cropping at the borders to cut down on the amount of mirrored pixels. Defaults to 1.

        **refine_features**

            Whether or not feature points should be refined at a sub-pixel level. This can be turned off for a slight performance gain at the cost of precision. Defaults to 1.

        **smooth_strength**

            The strength of the smoothing applied to the camera path from 0.0 to 1.0. 1.0 is the maximum smoothing strength while values less than that result in less smoothing. 0.0 causes the filter to adaptively choose a smoothing strength on a per-frame basis. Defaults to 0.0.

        **smooth_window_multiplier**

            Controls the size of the smoothing window (the number of frames buffered to determine motion information from). The size of the smoothing window is determined by multiplying the framerate of the video by this number. Acceptable values range from 0.1 to 10.0. Larger values increase the amount of motion data available for determining how to smooth the camera path, potentially improving smoothness, but also increase latency and memory usage. Defaults to 2.0.



        Parameters:
        ----------

        :param bool tripod: Simulates a tripod by preventing any camera movement whatsoever from the original frame. Defaults to 0.
        :param bool debug: Whether or not additional debug info should be displayed, both in the processed output and in the console. Note that in order to see console debug output you will also need to pass -v verbose to ffmpeg. Viewing point matches in the output video is only supported for RGB input. Defaults to 0.
        :param bool adaptive_crop: Whether or not to do a tiny bit of cropping at the borders to cut down on the amount of mirrored pixels. Defaults to 1.
        :param bool refine_features: Whether or not feature points should be refined at a sub-pixel level. This can be turned off for a slight performance gain at the cost of precision. Defaults to 1.
        :param float smooth_strength: The strength of the smoothing applied to the camera path from 0.0 to 1.0. 1.0 is the maximum smoothing strength while values less than that result in less smoothing. 0.0 causes the filter to adaptively choose a smoothing strength on a per-frame basis. Defaults to 0.0.
        :param float smooth_window_multiplier: Controls the size of the smoothing window (the number of frames buffered to determine motion information from). The size of the smoothing window is determined by multiplying the framerate of the video by this number. Acceptable values range from 0.1 to 10.0. Larger values increase the amount of motion data available for determining how to smooth the camera path, potentially improving smoothness, but also increase latency and memory usage. Defaults to 2.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deshake_005fopencl

        """
        filter_node = FilterNode(
            name="deshake_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "tripod": tripod,
                        "debug": debug,
                        "adaptive_crop": adaptive_crop,
                        "refine_features": refine_features,
                        "smooth_strength": smooth_strength,
                        "smooth_window_multiplier": smooth_window_multiplier,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def despill(
        self,
        *,
        type: int | Literal["green", "blue"] | Default = Default(0),
        mix: float | int | str = Default(0.5),
        expand: float | int | str = Default(0.0),
        red: float | int | str = Default(0.0),
        green: float | int | str = Default(-1.0),
        blue: float | int | str = Default(0.0),
        brightness: float | int | str = Default(0.0),
        alpha: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Despill video.

        Parameters:
        ----------

        :param int type: Set what type of despill to use.
        :param float mix: Set how spillmap will be generated.
        :param float expand: Set how much to get rid of still remaining spill.
        :param float red: Controls amount of red in spill area.
        :param float green: Controls amount of green in spill area. Should be -1 for greenscreen.
        :param float blue: Controls amount of blue in spill area. Should be -1 for bluescreen.
        :param float brightness: Controls brightness of spill area, preserving colors.
        :param bool alpha: Modify alpha from generated spillmap.
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
        first_field: int | Literal["top", "t", "bottom", "b"] | Default = Default(0),
        pattern: str | float | int = Default("23"),
        start_frame: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply an inverse telecine pattern.

        Parameters:
        ----------

        :param int first_field: ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        :param str pattern: A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.
        :param int start_frame: A number representing position of the first frame with respect to the telecine pattern. This is to be used if the stream is cut. The default value is 0.

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
        coordinates: int | str = Default(255),
        threshold0: int | str = Default(65535),
        threshold1: int | str = Default(65535),
        threshold2: int | str = Default(65535),
        threshold3: int | str = Default(65535),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply dilation effect.

        Parameters:
        ----------

        :param int coordinates: Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8
        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
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

    def dilation_opencl(
        self,
        *,
        threshold0: float | int | str = Default(65535.0),
        threshold1: float | int | str = Default(65535.0),
        threshold2: float | int | str = Default(65535.0),
        threshold3: float | int | str = Default(65535.0),
        coordinates: int | str = Default(255),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.7 dilation_opencl

        Apply dilation effect to the video.

        This filter replaces the pixel by the local(3x3) maximum.

        It accepts the following options:

        **threshold0**

        **threshold1**

        **threshold2**

        **threshold3**

            Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.

        **coordinates**

            Flag which specifies the pixel to refer to. Range is [0, 255] and default value is 255, i.e. all eight pixels are used. Flags to local 3x3 coordinates region centered on x: 1 2 3 4 x 5 6 7 8



        Parameters:
        ----------

        :param float threshold0: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold1: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold2: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold3: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param int coordinates: Flag which specifies the pixel to refer to. Range is [0, 255] and default value is 255, i.e. all eight pixels are used. Flags to local 3x3 coordinates region centered on x: 1 2 3 4 x 5 6 7 8

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dilation_005fopencl

        """
        filter_node = FilterNode(
            name="dilation_opencl",
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
                        "coordinates": coordinates,
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
        edge: int | Literal["blank", "smear", "wrap", "mirror"] | Default = Default("EDGE_SMEAR"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Displace pixels.

        Parameters:
        ----------

        :param int edge: Set displace behavior for pixels that are out of range. Available values are: ‘blank’ Missing pixels are replaced by black pixels. ‘smear’ Adjacent pixels will spread out to replace missing pixels. ‘wrap’ Out of range pixels are wrapped so they point to pixels of other side. ‘mirror’ Out of range pixels will be replaced with mirrored pixels. Default is ‘smear’.
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
        dnn_backend: int | str = Default("DNN_OV"),
        model: str | float | int = Default("((void*)0)"),
        input: str | float | int = Default("((void*)0)"),
        output: str | float | int = Default("((void*)0)"),
        backend_configs: str | float | int = Default("((void*)0)"),
        _async: bool | int | str = Default(1),
        confidence: float | int | str = Default(0.5),
        labels: str | float | int = Default("((void*)0)"),
        target: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN classify filter to the input.

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs for your system.
        :param bool _async: use DNN async inference (ignored, use backend_configs='async=1')
        :param float confidence: Set the confidence threshold (default: 0.5).
        :param str labels: Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0, and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        :param str target: which one to be classified

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
        dnn_backend: int | str = Default("DNN_OV"),
        model: str | float | int = Default("((void*)0)"),
        input: str | float | int = Default("((void*)0)"),
        output: str | float | int = Default("((void*)0)"),
        backend_configs: str | float | int = Default("((void*)0)"),
        _async: bool | int | str = Default(1),
        confidence: float | int | str = Default(0.5),
        labels: str | float | int = Default("((void*)0)"),
        model_type: int | Literal["ssd", "yolo", "yolov3", "yolov4"] | Default = Default("DDMT_SSD"),
        cell_w: int | str = Default(0),
        cell_h: int | str = Default(0),
        nb_classes: int | str = Default(0),
        anchors: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN detect filter to the input.

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async.
        :param bool _async: use DNN async inference (ignored, use backend_configs='async=1')
        :param float confidence: Set the confidence threshold (default: 0.5).
        :param str labels: Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0 (usually it is ’background’), and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        :param int model_type: DNN detection model type
        :param int cell_w: cell width
        :param int cell_h: cell height
        :param int nb_classes: The number of class
        :param str anchors: anchors, splited by '&'

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
                        "async": _async,
                        "confidence": confidence,
                        "labels": labels,
                        "model_type": model_type,
                        "cell_w": cell_w,
                        "cell_h": cell_h,
                        "nb_classes": nb_classes,
                        "anchors": anchors,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def dnn_processing(
        self,
        *,
        dnn_backend: int | str = Default("DNN_TF"),
        model: str | float | int = Default("((void*)0)"),
        input: str | float | int = Default("((void*)0)"),
        output: str | float | int = Default("((void*)0)"),
        backend_configs: str | float | int = Default("((void*)0)"),
        _async: bool | int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN processing filter to the input.

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow ‘openvino’ OpenVINO backend. To enable this backend you need to build and install the OpenVINO for C library (see https://github.com/openvinotoolkit/openvino/blob/master/build-instruction.md) and configure FFmpeg with --enable-libopenvino (–extra-cflags=-I... –extra-ldflags=-L... might be needed if the header files and libraries are not installed into system path)
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async. For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs of TensorFlow backend for your system.
        :param bool _async: use DNN async inference (ignored, use backend_configs='async=1')

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
                        "async": _async,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def doubleweave(
        self, *, first_field: int | Literal["top", "t", "bottom", "b"] | Default = Default(0), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into double number of frames.

        Parameters:
        ----------

        :param int first_field: Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.

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
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        width: str | float | int = Default("0"),
        height: str | float | int = Default("0"),
        color: str | float | int = Default("black"),
        thickness: str | float | int = Default("3"),
        replace: bool | int | str = Default(0),
        box_source: str | float | int = Default("((void*)0)"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored box on the input video.

        Parameters:
        ----------

        :param str x: The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        :param str y: The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        :param str width: The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        :param str height: The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        :param str color: Specify the color of the box to write. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the box edge color is the same as the video with inverted luma.
        :param str thickness: The expression which sets the thickness of the box edge. A value of fill will create a filled box. Default value is 3. See below for the list of accepted constants.
        :param bool replace: Applicable if the input has alpha. With value 1, the pixels of the painted box will overwrite the video’s color and alpha pixels. Default is 0, which composites the box onto the input, leaving the video’s alpha intact.
        :param str box_source: use datas from bounding box in side data
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
        m1: str | float | int = Default(""),
        fg1: str | float | int = Default("0xffff0000"),
        m2: str | float | int = Default(""),
        fg2: str | float | int = Default("0xff00ff00"),
        m3: str | float | int = Default(""),
        fg3: str | float | int = Default("0xffff00ff"),
        m4: str | float | int = Default(""),
        fg4: str | float | int = Default("0xffffff00"),
        bg: str | float | int = Default("white"),
        min: float | int | str = Default(-1.0),
        max: float | int | str = Default(1.0),
        mode: int | Literal["bar", "dot", "line"] | Default = Default(2),
        slide: int | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default(0),
        size: str | float | int = Default("900x256"),
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a graph using input video metadata.

        Parameters:
        ----------

        :param str m1: Set 1st frame metadata key from which metadata values will be used to draw a graph.
        :param str fg1: Set 1st foreground color expression.
        :param str m2: Set 2nd frame metadata key from which metadata values will be used to draw a graph.
        :param str fg2: Set 2nd foreground color expression.
        :param str m3: Set 3rd frame metadata key from which metadata values will be used to draw a graph.
        :param str fg3: Set 3rd foreground color expression.
        :param str m4: Set 4th frame metadata key from which metadata values will be used to draw a graph.
        :param str fg4: Set 4th foreground color expression.
        :param str bg: Set graph background color. Default is white.
        :param float min: Set minimal value of metadata value.
        :param float max: Set maximal value of metadata value.
        :param int mode: Set graph mode. Available values for mode is: ‘bar’ ‘dot’ ‘line’ Default is line.
        :param int slide: Set slide mode. Available values for slide is: ‘frame’ Draw new frame when right border is reached. ‘replace’ Replace old columns with new ones. ‘scroll’ Scroll from right to left. ‘rscroll’ Scroll from left to right. ‘picture’ Draw single picture. Default is frame.
        :param str size: Set size of graph video. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. The default value is 900x256.
        :param str rate: Set the output frame rate. Default value is 25. The foreground color expressions can use the following variables: MIN Minimal value of metadata value. MAX Maximal value of metadata value. VAL Current metadata key value. The color is defined as 0xAABBGGRR.

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
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        width: str | float | int = Default("0"),
        height: str | float | int = Default("0"),
        color: str | float | int = Default("black"),
        thickness: str | float | int = Default("1"),
        replace: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw a colored grid on the input video.

        Parameters:
        ----------

        :param str x: The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        :param str y: The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        :param str width: The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        :param str height: The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        :param str color: Specify the color of the grid. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the grid color is the same as the video with inverted luma.
        :param str thickness: The expression which sets the thickness of the grid line. Default value is 1. See below for the list of accepted constants.
        :param bool replace: Applicable if the input has alpha. With 1 the pixels of the painted grid will overwrite the video’s color and alpha pixels. Default is 0, which composites the grid onto the input, leaving the video’s alpha intact.
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
        fontfile: str | float | int = Default("((void*)0)"),
        text: str | float | int = Default("((void*)0)"),
        textfile: str | float | int = Default("((void*)0)"),
        fontcolor: str | float | int = Default("black"),
        fontcolor_expr: str | float | int = Default(""),
        boxcolor: str | float | int = Default("white"),
        bordercolor: str | float | int = Default("black"),
        shadowcolor: str | float | int = Default("black"),
        box: bool | int | str = Default(0),
        boxborderw: str | float | int = Default("0"),
        line_spacing: int | str = Default(0),
        fontsize: str | float | int = Default("((void*)0)"),
        text_align: str | float | int = Default(0),
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        boxw: int | str = Default(0),
        boxh: int | str = Default(0),
        shadowx: int | str = Default(0),
        shadowy: int | str = Default(0),
        borderw: int | str = Default(0),
        tabsize: int | str = Default(4),
        basetime: int | str = Default("((int64_t)(0x8000000000000000ULL))"),
        expansion: int | Literal["none", "normal", "strftime"] | Default = Default("EXP_NORMAL"),
        y_align: int | Literal["text", "baseline", "font"] | Default = Default("YA_TEXT"),
        timecode: str | float | int = Default("((void*)0)"),
        tc24hmax: bool | int | str = Default(0),
        timecode_rate: float | int | str = Default(0.0),
        reload: int | str = Default(0),
        alpha: str | float | int = Default("1"),
        fix_bounds: bool | int | str = Default(0),
        start_number: int | str = Default(0),
        text_source: str | float | int = Default("((void*)0)"),
        ft_load_flags: str | float | int = Default("FT_LOAD_DEFAULT"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Draw text on top of video frames using libfreetype library.

        Parameters:
        ----------

        :param str fontfile: set font file
        :param str text: set text
        :param str textfile: set text file
        :param str fontcolor: set foreground color
        :param str fontcolor_expr: set foreground color expression
        :param str boxcolor: set box color
        :param str bordercolor: set border color
        :param str shadowcolor: set shadow color
        :param bool box: set box
        :param str boxborderw: set box borders width
        :param int line_spacing: set line spacing in pixels
        :param str fontsize: set font size
        :param str text_align: set text alignment
        :param str x: set x expression
        :param str y: set y expression
        :param int boxw: set box width
        :param int boxh: set box height
        :param int shadowx: set shadow x offset
        :param int shadowy: set shadow y offset
        :param int borderw: set border width
        :param int tabsize: set tab size
        :param int basetime: set base time
        :param int expansion: set the expansion mode
        :param int y_align: set the y alignment
        :param str timecode: set initial timecode
        :param bool tc24hmax: set 24 hours max (timecode only)
        :param float timecode_rate: set rate (timecode only)
        :param int reload: reload text file at specified frame interval
        :param str alpha: apply alpha while rendering
        :param bool fix_bounds: check and fix text coords to avoid clipping
        :param int start_number: start frame number for n/frame_num variable
        :param str text_source: the source of text
        :param str ft_load_flags: set font loading flags for libfreetype
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
        high: float | int | str = Default("50/255."),
        low: float | int | str = Default("20/255."),
        mode: int | Literal["wires", "colormix", "canny"] | Default = Default("MODE_WIRES"),
        planes: str | Literal["y", "u", "v", "r", "g", "b"] | Default = Default(7),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Detect and draw edge.

        Parameters:
        ----------

        :param float high: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param float low: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param int mode: Define the drawing mode. ‘wires’ Draw white/gray wires on black background. ‘colormix’ Mix the colors to create a paint/cartoon effect. ‘canny’ Apply Canny edge detector on all selected planes. Default value is wires.
        :param str planes: Select planes for filtering. By default all available planes are filtered.
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
        codebook_length: int | str = Default(256),
        nb_steps: int | str = Default(1),
        seed: int | str = Default(-1),
        pal8: bool | int | str = Default(0),
        use_alpha: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply posterize effect, using the ELBG algorithm.

        Parameters:
        ----------

        :param int codebook_length: Set codebook length. The value must be a positive integer, and represents the number of distinct output colors. Default value is 256.
        :param int nb_steps: Set the maximum number of iterations to apply for computing the optimal mapping. The higher the value the better the result and the higher the computation time. Default value is 1.
        :param int seed: Set a random seed, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to -1, the filter will try to use a good random seed on a best effort basis.
        :param bool pal8: Set pal8 output pixel format. This option does not work with codebook length greater than 256. Default is disabled.
        :param bool use_alpha: Include alpha values in the quantization calculation. Allows creating palettized output images (e.g. PNG8) with multiple alpha smooth blending.

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
        mode: int | Literal["normal", "diff"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Measure video frames entropy.

        Parameters:
        ----------

        :param int mode: Can be either normal or diff. Default is normal. diff mode measures entropy of histogram delta values, absolute differences between neighbour histogram values.
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

    def epx(self, *, n: int | str = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using EPX algorithm.

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for 2xEPX, 3 for 3xEPX. Default is 3.

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
        contrast: str | float | int = Default("1.0"),
        brightness: str | float | int = Default("0.0"),
        saturation: str | float | int = Default("1.0"),
        gamma: str | float | int = Default("1.0"),
        gamma_r: str | float | int = Default("1.0"),
        gamma_g: str | float | int = Default("1.0"),
        gamma_b: str | float | int = Default("1.0"),
        gamma_weight: str | float | int = Default("1.0"),
        eval: int | str = Default("EVAL_MODE_INIT"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust brightness, contrast, gamma, and saturation.

        Parameters:
        ----------

        :param str contrast: Set the contrast expression. The value must be a float value in range -1000.0 to 1000.0. The default value is "1".
        :param str brightness: Set the brightness expression. The value must be a float value in range -1.0 to 1.0. The default value is "0".
        :param str saturation: Set the saturation expression. The value must be a float in range 0.0 to 3.0. The default value is "1".
        :param str gamma: Set the gamma expression. The value must be a float in range 0.1 to 10.0. The default value is "1".
        :param str gamma_r: Set the gamma expression for red. The value must be a float in range 0.1 to 10.0. The default value is "1".
        :param str gamma_g: Set the gamma expression for green. The value must be a float in range 0.1 to 10.0. The default value is "1".
        :param str gamma_b: Set the gamma expression for blue. The value must be a float in range 0.1 to 10.0. The default value is "1".
        :param str gamma_weight: Set the gamma weight expression. It can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting overamplified and just plain white. The value must be a float in range 0.0 to 1.0. A value of 0.0 turns the gamma correction all the way down while 1.0 leaves it at its full strength. Default is "1".
        :param int eval: Set when the expressions for brightness, contrast, saturation and gamma expressions are evaluated. It accepts the following values: ‘init’ only evaluate expressions once during the filter initialization or when a command is processed ‘frame’ evaluate expressions for each incoming frame Default value is ‘init’.
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
        coordinates: int | str = Default(255),
        threshold0: int | str = Default(65535),
        threshold1: int | str = Default(65535),
        threshold2: int | str = Default(65535),
        threshold3: int | str = Default(65535),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply erosion effect.

        Parameters:
        ----------

        :param int coordinates: Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8
        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
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

    def erosion_opencl(
        self,
        *,
        threshold0: float | int | str = Default(65535.0),
        threshold1: float | int | str = Default(65535.0),
        threshold2: float | int | str = Default(65535.0),
        threshold3: float | int | str = Default(65535.0),
        coordinates: int | str = Default(255),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.5 erosion_opencl

        Apply erosion effect to the video.

        This filter replaces the pixel by the local(3x3) minimum.

        It accepts the following options:

        **threshold0**

        **threshold1**

        **threshold2**

        **threshold3**

            Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.

        **coordinates**

            Flag which specifies the pixel to refer to. Range is [0, 255] and default value is 255, i.e. all eight pixels are used. Flags to local 3x3 coordinates region centered on x: 1 2 3 4 x 5 6 7 8



        Parameters:
        ----------

        :param float threshold0: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold1: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold2: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param float threshold3: Limit the maximum change for each plane. Range is [0, 65535] and default value is 65535. If 0, plane will remain unchanged.
        :param int coordinates: Flag which specifies the pixel to refer to. Range is [0, 255] and default value is 255, i.e. all eight pixels are used. Flags to local 3x3 coordinates region centered on x: 1 2 3 4 x 5 6 7 8

        Ref: https://ffmpeg.org/ffmpeg-filters.html#erosion_005fopencl

        """
        filter_node = FilterNode(
            name="erosion_opencl",
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
                        "coordinates": coordinates,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def estdif(
        self,
        *,
        mode: int | Literal["frame", "field"] | Default = Default(1),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default(-1),
        deint: int | Literal["all", "interlaced"] | Default = Default(0),
        rslope: int | str = Default(1),
        redge: int | str = Default(2),
        ecost: int | str = Default(2),
        mcost: int | str = Default(1),
        dcost: int | str = Default(1),
        interp: int | Literal["2p", "4p", "6p"] | Default = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Edge Slope Tracing deinterlace.

        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: frame Output one frame for each frame. field Output one frame for each field. The default value is field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: tff Assume the top field is first. bff Assume the bottom field is first. auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: all Deinterlace all frames. interlaced Only deinterlace frames marked as interlaced. The default value is all.
        :param int rslope: Specify the search radius for edge slope tracing. Default value is 1. Allowed range is from 1 to 15.
        :param int redge: Specify the search radius for best edge matching. Default value is 2. Allowed range is from 0 to 15.
        :param int ecost: Specify the edge cost for edge matching. Default value is 2. Allowed range is from 0 to 50.
        :param int mcost: Specify the middle cost for edge matching. Default value is 1. Allowed range is from 0 to 50.
        :param int dcost: Specify the distance cost for edge matching. Default value is 1. Allowed range is from 0 to 50.
        :param int interp: Specify the interpolation used. Default is 4-point interpolation. It accepts one of the following values: 2p Two-point interpolation. 4p Four-point interpolation. 6p Six-point interpolation.
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
        self,
        *,
        exposure: float | int | str = Default(0.0),
        black: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust exposure of the video stream.

        Parameters:
        ----------

        :param float exposure: Set the exposure correction in EV. Allowed range is from -3.0 to 3.0 EV Default value is 0 EV.
        :param float black: Set the black level correction. Allowed range is from -1.0 to 1.0. Default value is 0.
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
        self, *, planes: str | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default(1), **kwargs: Any
    ) -> FilterNode:
        """

        Extract planes as grayscale frames.

        Parameters:
        ----------

        :param str planes: Set plane(s) to extract. Available values for planes are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’ Choosing planes not available in the input will result in an error. That means you cannot select r, g, b planes with y, u, v planes at same time.

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
        type: int | str = Default(0),
        start_frame: int | str = Default(0),
        nb_frames: int | str = Default(25),
        alpha: bool | int | str = Default(0),
        start_time: int | str = Default("0."),
        duration: int | str = Default("0."),
        color: str | float | int = Default("black"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fade in/out input video.

        Parameters:
        ----------

        :param int type: The effect type can be either "in" for a fade-in, or "out" for a fade-out effect. Default is in.
        :param int start_frame: Specify the number of the frame to start applying the fade effect at. Default is 0.
        :param int nb_frames: The number of frames that the fade effect lasts. At the end of the fade-in effect, the output video will have the same intensity as the input video. At the end of the fade-out transition, the output video will be filled with the selected color. Default is 25.
        :param bool alpha: If set to 1, fade only alpha channel, if one exists on the input. Default value is 0.
        :param int start_time: Specify the timestamp (in seconds) of the frame to start to apply the fade effect. If both start_frame and start_time are specified, the fade will start at whichever comes last. Default is 0.
        :param int duration: The number of seconds for which the fade effect has to last. At the end of the fade-in effect the output video will have the same intensity as the input video, at the end of the fade-out transition the output video will be filled with the selected color. If both duration and nb_frames are specified, duration is used. Default is 0 (nb_frames is used by default).
        :param str color: Specify the color of the fade. Default is "black".
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
        self,
        _feedin: "VideoStream",
        *,
        x: int | str = Default(0),
        y: int | str = Default(0),
        w: int | str = Default(0),
        h: int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> tuple["VideoStream", "VideoStream",]:
        """

        Apply feedback video filter.

        Parameters:
        ----------

        :param int x: Set the top left crop position.
        :param int y: Set the top left crop position.
        :param int w: Set the crop size.
        :param int h: Set the crop size.
        :param str enable: timeline editing

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
                        "y": y,
                        "w": w,
                        "h": h,
                        "enable": enable,
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
        sigma: float | int | str = Default(1.0),
        amount: float | int | str = Default(1.0),
        block: int | str = Default(32),
        overlap: float | int | str = Default(0.5),
        method: int | Literal["wiener", "hard"] | Default = Default(0),
        prev: int | str = Default(0),
        next: int | str = Default(0),
        planes: int | str = Default(7),
        window: int
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
        | Default = Default("WFUNC_HANNING"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise frames using 3D FFT.

        Parameters:
        ----------

        :param float sigma: Set the noise sigma constant. This sets denoising strength. Default value is 1. Allowed range is from 0 to 30. Using very high sigma with low overlap may give blocking artifacts.
        :param float amount: Set amount of denoising. By default all detected noise is reduced. Default value is 1. Allowed range is from 0 to 1.
        :param int block: Set size of block in pixels, Default is 32, can be 8 to 256.
        :param float overlap: Set block overlap. Default is 0.5. Allowed range is from 0.2 to 0.8.
        :param int method: Set denoising method. Default is wiener, can also be hard.
        :param int prev: Set number of previous frames to use for denoising. By default is set to 0.
        :param int next: Set number of next frames to to use for denoising. By default is set to 0.
        :param int planes: Set planes which will be filtered, by default are all available filtered except alpha.
        :param int window: set window function
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
        dc_Y: int | str = Default(0),
        dc_U: int | str = Default(0),
        dc_V: int | str = Default(0),
        weight_Y: str | float | int = Default("1"),
        weight_U: str | float | int = Default("((void*)0)"),
        weight_V: str | float | int = Default("((void*)0)"),
        eval: int | str = Default("EVAL_MODE_INIT"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply arbitrary expressions to pixels in frequency domain.

        Parameters:
        ----------

        :param int dc_Y: Adjust the dc value (gain) of the luma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param int dc_U: Adjust the dc value (gain) of the 1st chroma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param int dc_V: Adjust the dc value (gain) of the 2nd chroma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param str weight_Y: Set the frequency domain weight expression for the luma plane.
        :param str weight_U: Set the frequency domain weight expression for the 1st chroma plane.
        :param str weight_V: Set the frequency domain weight expression for the 2nd chroma plane.
        :param int eval: Set when the expressions are evaluated. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization. ‘frame’ Evaluate expressions for each incoming frame. Default value is ‘init’. The filter accepts the following variables:
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

    def field(
        self, *, type: int | Literal["top", "bottom"] | Default = Default("FIELD_TYPE_TOP"), **kwargs: Any
    ) -> "VideoStream":
        """

        Extract a field from the input video.

        Parameters:
        ----------

        :param int type: Specify whether to extract the top (if the value is 0 or top) or the bottom field (if the value is 1 or bottom).

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
        hint: str | float | int = Default("((void*)0)"),
        mode: int | Literal["absolute", "relative", "pattern"] | Default = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Field matching using hints.

        Parameters:
        ----------

        :param str hint: Set file containing hints: absolute/relative frame numbers. There must be one line for each frame in a clip. Each line must contain two numbers separated by the comma, optionally followed by - or +. Numbers supplied on each line of file can not be out of [N-1,N+1] where N is current frame number for absolute mode or out of [-1, 1] range for relative mode. First number tells from which frame to pick up top field and second number tells from which frame to pick up bottom field. If optionally followed by + output frame will be marked as interlaced, else if followed by - output frame will be marked as progressive, else it will be marked same as input frame. If optionally followed by t output frame will use only top field, or in case of b it will use only bottom field. If line starts with # or ; that line is skipped.
        :param int mode: Can be item absolute or relative or pattern. Default is absolute. The pattern mode is same as relative mode, except at last entry of file if there are more frames to process than hint file is seek back to start.

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
        self, *, order: int | str = Default(1), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Set the field order.

        Parameters:
        ----------

        :param int order: The output field order. Valid values are tff for top field first or bff for bottom field first.
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
        left: int | str = Default(0),
        right: int | str = Default(0),
        top: int | str = Default(0),
        bottom: int | str = Default(0),
        mode: int
        | Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | Default = Default("FM_SMEAR"),
        color: str | float | int = Default("black"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill borders of the input video.

        Parameters:
        ----------

        :param int left: Number of pixels to fill from left border.
        :param int right: Number of pixels to fill from right border.
        :param int top: Number of pixels to fill from top border.
        :param int bottom: Number of pixels to fill from bottom border.
        :param int mode: Set fill mode. It accepts the following values: ‘smear’ fill pixels using outermost pixels ‘mirror’ fill pixels using mirroring (half sample symmetric) ‘fixed’ fill pixels with constant value ‘reflect’ fill pixels using reflecting (whole sample symmetric) ‘wrap’ fill pixels using wrapping ‘fade’ fade pixels to constant value ‘margins’ fill pixels at top and bottom with weighted averages pixels near borders Default is smear.
        :param str color: Set color for pixels in fixed or fade mode. Default is black.
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
        object: str | float | int = Default("((void*)0)"),
        threshold: float | int | str = Default(0.5),
        mipmaps: int | str = Default(3),
        xmin: int | str = Default(0),
        ymin: int | str = Default(0),
        xmax: int | str = Default(0),
        ymax: int | str = Default(0),
        discard: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find a user specified object.

        Parameters:
        ----------

        :param str object: Filepath of the object image, needs to be in gray8.
        :param float threshold: Detection threshold, expressed as a decimal number in the range 0-1. A threshold value of 0.01 means only exact matches, a threshold of 0.99 means almost everything matches. Default value is 0.5.
        :param int mipmaps: Number of mipmaps, default is 3.
        :param int xmin: Specifies the rectangle in which to search.
        :param int ymin: Specifies the rectangle in which to search.
        :param int xmax: Specifies the rectangle in which to search.
        :param int ymax: Specifies the rectangle in which to search.
        :param bool discard: Discard frames where object is not detected. Default is disabled.

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
                        "ymin": ymin,
                        "xmax": xmax,
                        "ymax": ymax,
                        "discard": discard,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def flip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        ### 14.8 flip_vulkan

        Flips an image along both the vertical and horizontal axis.



        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#flip_005fvulkan

        """
        filter_node = FilterNode(
            name="flip_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def floodfill(
        self,
        *,
        x: int | str = Default(0),
        y: int | str = Default(0),
        s0: int | str = Default(0),
        s1: int | str = Default(0),
        s2: int | str = Default(0),
        s3: int | str = Default(0),
        d0: int | str = Default(0),
        d1: int | str = Default(0),
        d2: int | str = Default(0),
        d3: int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Fill area with same color with another color.

        Parameters:
        ----------

        :param int x: Set pixel x coordinate.
        :param int y: Set pixel y coordinate.
        :param int s0: Set source #0 component value.
        :param int s1: Set source #1 component value.
        :param int s2: Set source #2 component value.
        :param int s3: Set source #3 component value.
        :param int d0: Set destination #0 component value.
        :param int d1: Set destination #1 component value.
        :param int d2: Set destination #2 component value.
        :param int d3: Set destination #3 component value.
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

    def format(self, *, pix_fmts: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Convert the input video to one of the specified pixel formats.

        Parameters:
        ----------

        :param str pix_fmts: A ’|’-separated list of pixel format names, such as "pix_fmts=yuv420p|monow|rgb24".

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
        fps: str | float | int = Default("25"),
        start_time: float | int | str = Default(1.7976931348623157e308),
        round: int | Literal["zero", "inf", "down", "up", "near"] | Default = Default("AV_ROUND_NEAR_INF"),
        eof_action: int | Literal["round", "pass"] | Default = Default("EOF_ACTION_ROUND"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force constant framerate.

        Parameters:
        ----------

        :param str fps: The desired output frame rate. It accepts expressions containing the following constants: ‘source_fps’ The input’s frame rate ‘ntsc’ NTSC frame rate of 30000/1001 ‘pal’ PAL frame rate of 25.0 ‘film’ Film frame rate of 24.0 ‘ntsc_film’ NTSC-film frame rate of 24000/1001 The default is 25.
        :param float start_time: Assume the first PTS should be the given value, in seconds. This allows for padding/trimming at the start of stream. By default, no assumption is made about the first frame’s expected PTS, so no padding or trimming is done. For example, this could be set to 0 to pad the beginning with duplicates of the first frame if a video stream starts after the audio stream or to trim any frames with a negative PTS.
        :param int round: Timestamp (PTS) rounding method. Possible values are: zero round towards 0 inf round away from 0 down round towards -infinity up round towards +infinity near round to nearest The default is near.
        :param int eof_action: Action performed when reading the last frame. Possible values are: round Use same timestamp rounding method as used for other frames. pass Pass through last frame if input duration has not been reached yet. The default is round.

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
        format: int
        | Literal["sbs", "tab", "frameseq", "lines", "columns"]
        | Default = Default("AV_STEREO3D_SIDEBYSIDE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate a frame packed stereoscopic video.

        Parameters:
        ----------

        :param int format: The desired packing format. Supported values are: sbs The views are next to each other (default). tab The views are on top of each other. lines The views are packed by line. columns The views are packed by column. frameseq The views are temporally interleaved.

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
        fps: str | float | int = Default("50"),
        interp_start: int | str = Default(15),
        interp_end: int | str = Default(240),
        scene: float | int | str = Default(8.2),
        flags: str | Literal["scene_change_detect", "scd"] | Default = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Upsamples or downsamples progressive source between specified frame rates.

        Parameters:
        ----------

        :param str fps: Specify the output frames per second. This option can also be specified as a value alone. The default is 50.
        :param int interp_start: Specify the start of a range where the output frame will be created as a linear interpolation of two frames. The range is [0-255], the default is 15.
        :param int interp_end: Specify the end of a range where the output frame will be created as a linear interpolation of two frames. The range is [0-255], the default is 240.
        :param float scene: Specify the level at which a scene change is detected as a value between 0 and 100 to indicate a new scene; a low value reflects a low probability for the current frame to introduce a new scene, while a higher value means the current frame is more likely to be one. The default is 8.2.
        :param str flags: Specify flags influencing the filter process. Available value for flags is: scene_change_detect, scd Enable scene change detection using the value of the option scene. This flag is enabled by default.

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

    def framestep(
        self, *, step: int | str = Default(1), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Select one frame every N frames.

        Parameters:
        ----------

        :param int step: Select frame after every step frames. Allowed values are positive integers higher than 0. Default value is 1.
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

    def freezedetect(
        self, *, n: float | int | str = Default(0.001), d: int | str = Default(2000000), **kwargs: Any
    ) -> "VideoStream":
        """

        Detects frozen video input.

        Parameters:
        ----------

        :param float n: Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or as a difference ratio between 0 and 1. Default is -60dB, or 0.001.
        :param int d: Set freeze duration until notification (default is 2 seconds).

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
        first: int | str = Default(0),
        last: int | str = Default(0),
        replace: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Freeze video frames.

        Parameters:
        ----------

        :param int first: Set number of first frame from which to start freeze.
        :param int last: Set number of last frame from which to end freeze.
        :param int replace: Set number of frame from 2nd input which will be used instead of replaced frames.

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
        filter_name: str | float | int = Default(None),
        filter_params: str | float | int = Default(None),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a frei0r effect.

        Parameters:
        ----------

        :param str filter_name: The name of the frei0r effect to load. If the environment variable FREI0R_PATH is defined, the frei0r effect is searched for in each of the directories specified by the colon-separated list in FREI0R_PATH. Otherwise, the standard frei0r paths are searched, in this order: HOME/.frei0r-1/lib/, /usr/local/lib/frei0r-1/, /usr/lib/frei0r-1/.
        :param str filter_params: A ’|’-separated list of parameters to pass to the frei0r effect.
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
        quality: int | str = Default(4),
        qp: int | str = Default(0),
        strength: int | str = Default(0),
        use_bframe_qp: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Fast Simple Post-processing filter.

        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 4-5. Default value is 4.
        :param int qp: Force a constant quantization parameter. It accepts an integer in range 0-63. If not set, the filter will use the QP from the video stream (if available).
        :param int strength: Set filter strength. It accepts an integer in range -15 to 32. Lower values mean more details but also more artifacts, while higher values make the image smoother but also blurrier. Default value is 0 − PSNR optimal.
        :param bool use_bframe_qp: Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).
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
        sigma: float | int | str = Default(0.5),
        steps: int | str = Default(1),
        planes: int | str = Default("0xF"),
        sigmaV: float | int | str = Default(-1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Gaussian Blur filter.

        Parameters:
        ----------

        :param float sigma: Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.
        :param int steps: Set number of steps for Gaussian approximation. Default is 1.
        :param int planes: Set which planes to filter. By default all planes are filtered.
        :param float sigmaV: Set vertical sigma, if negative it will be same as sigma. Default is -1.
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

    def gblur_vulkan(
        self,
        *,
        sigma: float | int | str = Default(0.5),
        sigmaV: float | int | str = Default(0.0),
        planes: int | str = Default("0xF"),
        size: int | str = Default(19),
        sizeV: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.9 gblur_vulkan

        Apply Gaussian blur filter on Vulkan frames.

        The filter accepts the following options:

        **sigma**

            Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.

        **sigmaV**

            Set vertical sigma, if negative it will be same as sigma. Default is -1.

        **planes**

            Set which planes to filter. By default all planes are filtered.

        **size**

            Set the kernel size along the horizontal axis. Default is 19.

        **sizeV**

            Set the kernel size along the vertical axis. Default is 0, which sets to use the same value as size.



        Parameters:
        ----------

        :param float sigma: Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.
        :param float sigmaV: Set vertical sigma, if negative it will be same as sigma. Default is -1.
        :param int planes: Set which planes to filter. By default all planes are filtered.
        :param int size: Set the kernel size along the horizontal axis. Default is 19.
        :param int sizeV: Set the kernel size along the vertical axis. Default is 0, which sets to use the same value as size.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gblur_005fvulkan

        """
        filter_node = FilterNode(
            name="gblur_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "sigma": sigma,
                        "sigmaV": sigmaV,
                        "planes": planes,
                        "size": size,
                        "sizeV": sizeV,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def geq(
        self,
        *,
        lum_expr: str | float | int = Default("((void*)0)"),
        cb_expr: str | float | int = Default("((void*)0)"),
        cr_expr: str | float | int = Default("((void*)0)"),
        alpha_expr: str | float | int = Default("((void*)0)"),
        red_expr: str | float | int = Default("((void*)0)"),
        green_expr: str | float | int = Default("((void*)0)"),
        blue_expr: str | float | int = Default("((void*)0)"),
        interpolation: int | Literal["nearest", "n", "bilinear", "b"] | Default = Default("INTERP_BILINEAR"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply generic equation to each pixel.

        Parameters:
        ----------

        :param str lum_expr: Set the luma expression.
        :param str cb_expr: Set the chrominance blue expression.
        :param str cr_expr: Set the chrominance red expression.
        :param str alpha_expr: Set the alpha expression.
        :param str red_expr: Set the red expression.
        :param str green_expr: Set the green expression.
        :param str blue_expr: Set the blue expression.
        :param int interpolation: set interpolation method
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
        strength: float | int | str = Default(1.2),
        radius: int | str = Default(16),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Debands video quickly using gradients.

        Parameters:
        ----------

        :param float strength: The maximum amount by which the filter will change any one pixel. This is also the threshold for detecting nearly flat regions. Acceptable values range from .51 to 64; the default value is 1.2. Out-of-range values will be clipped to the valid range.
        :param int radius: The neighborhood to fit the gradient to. A larger radius makes for smoother gradients, but also prevents the filter from modifying the pixels near detailed regions. Acceptable values are 8-32; the default value is 16. Out-of-range values will be clipped to the valid range.
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
        size: str | float | int = Default("hd720"),
        opacity: float | int | str = Default(0.9),
        mode: str | Literal["full", "compact", "nozero", "noeof", "nodisabled"] | Default = Default(0),
        flags: str
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
        | Default = Default("FLAG_QUEUE"),
        rate: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Show various filtergraph stats.

        Parameters:
        ----------

        :param str size: Set video output size. Default is hd720.
        :param float opacity: Set video opacity. Default is 0.9. Allowed range is from 0 to 1.
        :param str mode: Set output mode flags. Available values for flags are: ‘full’ No any filtering. Default. ‘compact’ Show only filters with queued frames. ‘nozero’ Show only filters with non-zero stats. ‘noeof’ Show only filters with non-eof stat. ‘nodisabled’ Show only filters that are enabled in timeline.
        :param str flags: Set flags which enable which stats are shown in video. Available values for flags are: ‘none’ All flags turned off. ‘all’ All flags turned on. ‘queue’ Display number of queued frames in each link. ‘frame_count_in’ Display number of frames taken from filter. ‘frame_count_out’ Display number of frames given out from filter. ‘frame_count_delta’ Display delta number of frames between above two values. ‘pts’ Display current filtered frame pts. ‘pts_delta’ Display pts delta between current and previous frame. ‘time’ Display current filtered frame time. ‘time_delta’ Display time delta between current and previous frame. ‘timebase’ Display time base for filter link. ‘format’ Display used format for filter link. ‘size’ Display video size or number of audio channels in case of audio used by filter link. ‘rate’ Display video frame rate or sample rate in case of audio used by filter link. ‘eof’ Display link output status. ‘sample_count_in’ Display number of samples taken from filter. ‘sample_count_out’ Display number of samples given out from filter. ‘sample_count_delta’ Display delta number of samples between above two values. ‘disabled’ Show the timeline filter status.
        :param str rate: Set upper limit for video rate of output stream, Default value is 25. This guarantee that output video frame rate will not be higher than this value.

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

    def grayworld(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
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
        difford: int | str = Default(1),
        minknorm: int | str = Default(1),
        sigma: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Estimates scene illumination by grey edge assumption.

        Parameters:
        ----------

        :param int difford: The order of differentiation to be applied on the scene. Must be chosen in the range [0,2] and default value is 1.
        :param int minknorm: The Minkowski parameter to be used for calculating the Minkowski distance. Must be chosen in the range [0,20] and default value is 1. Set to 0 for getting max value instead of calculating Minkowski distance.
        :param float sigma: The standard deviation of Gaussian blur to be applied on the scene. Must be chosen in the range [0,1024.0] and default value = 1. floor( sigma * break_off_sigma(3) ) can’t be equal to 0 if difford is greater than 0.
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
        clut: int | Literal["first", "all"] | Default = Default(1),
        interp: int
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("INTERPOLATE_TETRAHEDRAL"),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a Hald CLUT.

        Parameters:
        ----------

        :param int clut: Set which CLUT video frames will be processed from second input stream, can be first or all. Default is all.
        :param int interp: select interpolation mode
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def hflip(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
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

    def hflip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        ### 14.7 hflip_vulkan

        Flips an image horizontally.



        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#hflip_005fvulkan

        """
        filter_node = FilterNode(
            name="hflip_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
        )
        return filter_node.video(0)

    def histeq(
        self,
        *,
        strength: float | int | str = Default(0.2),
        intensity: float | int | str = Default(0.21),
        antibanding: int | Literal["none", "weak", "strong"] | Default = Default("HISTEQ_ANTIBANDING_NONE"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply global color histogram equalization.

        Parameters:
        ----------

        :param float strength: Determine the amount of equalization to be applied. As the strength is reduced, the distribution of pixel intensities more-and-more approaches that of the input frame. The value must be a float number in the range [0,1] and defaults to 0.200.
        :param float intensity: Set the maximum intensity that can generated and scale the output values appropriately. The strength should be set as desired and then the intensity can be limited if needed to avoid washing-out. The value must be a float number in the range [0,1] and defaults to 0.210.
        :param int antibanding: Set the antibanding level. If enabled the filter will randomly vary the luminance of output pixels by a small amount to avoid banding of the histogram. Possible values are none, weak or strong. It defaults to none.
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
        level_height: int | str = Default(200),
        scale_height: int | str = Default(12),
        display_mode: int | Literal["overlay", "parade", "stack"] | Default = Default(2),
        levels_mode: int | Literal["linear", "logarithmic"] | Default = Default(0),
        components: int | str = Default(7),
        fgopacity: float | int | str = Default(0.7),
        bgopacity: float | int | str = Default(0.5),
        colors_mode: int
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
        | Default = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and draw a histogram.

        Parameters:
        ----------

        :param int level_height: Set height of level. Default value is 200. Allowed range is [50, 2048].
        :param int scale_height: Set height of color scale. Default value is 12. Allowed range is [0, 40].
        :param int display_mode: Set display mode. It accepts the following values: ‘stack’ Per color component graphs are placed below each other. ‘parade’ Per color component graphs are placed side by side. ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. Default is stack.
        :param int levels_mode: Set mode. Can be either linear, or logarithmic. Default is linear.
        :param int components: Set what color components to display. Default is 7.
        :param float fgopacity: Set foreground opacity. Default is 0.7.
        :param float bgopacity: Set background opacity. Default is 0.5.
        :param int colors_mode: Set colors mode. It accepts the following values: ‘whiteonblack’ ‘blackonwhite’ ‘whiteongray’ ‘blackongray’ ‘coloronblack’ ‘coloronwhite’ ‘colorongray’ ‘blackoncolor’ ‘whiteoncolor’ ‘grayoncolor’ Default is whiteonblack.

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
        luma_spatial: float | int | str = Default(0.0),
        chroma_spatial: float | int | str = Default(0.0),
        luma_tmp: float | int | str = Default(0.0),
        chroma_tmp: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a High Quality 3D Denoiser.

        Parameters:
        ----------

        :param float luma_spatial: A non-negative floating point number which specifies spatial luma strength. It defaults to 4.0.
        :param float chroma_spatial: A non-negative floating point number which specifies spatial chroma strength. It defaults to 3.0*luma_spatial/4.0.
        :param float luma_tmp: A floating point number which specifies luma temporal strength. It defaults to 6.0*luma_spatial/4.0.
        :param float chroma_tmp: A floating point number which specifies chroma temporal strength. It defaults to luma_tmp*chroma_spatial/luma_spatial.
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

    def hqx(self, *, n: int | str = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for hq2x, 3 for hq3x and 4 for hq4x. Default is 3.

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
        hue: float | int | str = Default(0.0),
        sat: float | int | str = Default(0.0),
        val: float | int | str = Default(0.0),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into gray.

        Parameters:
        ----------

        :param float hue: Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        :param float sat: Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float val: Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float similarity: Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more gray pixels, with a higher gray pixel the more similar the pixels color is to the key color.
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
        hue: float | int | str = Default(0.0),
        sat: float | int | str = Default(0.0),
        val: float | int | str = Default(0.0),
        similarity: float | int | str = Default(0.01),
        blend: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain HSV range into transparency. Operates on YUV colors.

        Parameters:
        ----------

        :param float hue: Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        :param float sat: Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float val: Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float similarity: Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.
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
        h: str | float | int = Default("((void*)0)"),
        s: str | float | int = Default("1"),
        H: str | float | int = Default("((void*)0)"),
        b: str | float | int = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust the hue and saturation of the input video.

        Parameters:
        ----------

        :param str h: Specify the hue angle as a number of degrees. It accepts an expression, and defaults to "0".
        :param str s: Specify the saturation in the [-10,10] range. It accepts an expression and defaults to "1".
        :param str H: Specify the hue angle as a number of radians. It accepts an expression, and defaults to "0".
        :param str b: Specify the brightness in the [-10,10] range. It accepts an expression and defaults to "0".
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
        hue: float | int | str = Default(0.0),
        saturation: float | int | str = Default(0.0),
        intensity: float | int | str = Default(0.0),
        colors: str | Literal["r", "y", "g", "c", "b", "m", "a"] | Default = Default("0x3F"),
        strength: float | int | str = Default(1.0),
        rw: float | int | str = Default(0.333),
        gw: float | int | str = Default(0.334),
        bw: float | int | str = Default(0.333),
        lightness: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply hue-saturation-intensity adjustments.

        Parameters:
        ----------

        :param float hue: Set the hue shift in degrees to apply. Default is 0. Allowed range is from -180 to 180.
        :param float saturation: Set the saturation shift. Default is 0. Allowed range is from -1 to 1.
        :param float intensity: Set the intensity shift. Default is 0. Allowed range is from -1 to 1.
        :param str colors: Set which primary and complementary colors are going to be adjusted. This options is set by providing one or multiple values. This can select multiple colors at once. By default all colors are selected. ‘r’ Adjust reds. ‘y’ Adjust yellows. ‘g’ Adjust greens. ‘c’ Adjust cyans. ‘b’ Adjust blues. ‘m’ Adjust magentas. ‘a’ Adjust all colors.
        :param float strength: Set strength of filtering. Allowed range is from 0 to 100. Default value is 1.
        :param float rw: Set weight for each RGB component. Allowed range is from 0 to 1. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightess processing.
        :param float gw: Set weight for each RGB component. Allowed range is from 0 to 1. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightess processing.
        :param float bw: Set weight for each RGB component. Allowed range is from 0 to 1. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightess processing.
        :param bool lightness: Set preserving lightness, by default is disabled. Adjusting hues can change lightness from original RGB triplet, with this option enabled lightness is kept at same value.
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
        mode: str
        | Literal["read", "write", "overwrite", "direct"]
        | Default = Default("AV_HWFRAME_MAP_READ | AV_HWFRAME_MAP_WRITE"),
        derive_device: str | float | int = Default("((void*)0)"),
        reverse: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Map hardware frames

        Parameters:
        ----------

        :param str mode: Set the frame mapping mode. Some combination of: read The mapped frame should be readable. write The mapped frame should be writeable. overwrite The mapping will always overwrite the entire frame. This may improve performance in some cases, as the original contents of the frame need not be loaded. direct The mapping must not involve any copying. Indirect mappings to copies of frames are created in some cases where either direct mapping is not possible or it would have unexpected properties. Setting this flag ensures that the mapping is direct and will fail if that is not possible. Defaults to read+write if not specified.
        :param str derive_device: Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.
        :param int reverse: In a hardware to hardware mapping, map in reverse - create frames in the sink and map them back to the source. This may be necessary in some cases where a mapping in one direction is required but only the opposite direction is supported by the devices being used. This option is dangerous - it may break the preceding filter in undefined ways if there are any additional constraints on that filter’s output. Do not use it without fully understanding the implications of its use.

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

    def hwupload(self, *, derive_device: str | float | int = Default("((void*)0)"), **kwargs: Any) -> "VideoStream":
        """

        Upload a normal frame to a hardware frame

        Parameters:
        ----------

        :param str derive_device: Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.

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

    def hwupload_cuda(self, *, device: int | str = Default(0), **kwargs: Any) -> "VideoStream":
        """

        ### 11.124 hwupload_cuda

        Upload system memory frames to a CUDA device.

        It accepts the following optional parameters:

        **device**

            The number of the CUDA device to use



        Parameters:
        ----------

        :param int device: The number of the CUDA device to use

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload_005fcuda

        """
        filter_node = FilterNode(
            name="hwupload_cuda",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "device": device,
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
        planes: int | str = Default("0xF"),
        threshold: int | str = Default(0),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Grow first stream into second stream by connecting components.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
        :param int threshold: Set threshold which is used in filtering. If pixel component value is higher than this value filter algorithm for connecting components is activated. By default value is 0.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def iccdetect(self, *, force: bool | int | str = Default(1), **kwargs: Any) -> "VideoStream":
        """

        ### 11.132 iccdetect

        Detect the colorspace from an embedded ICC profile (if present), and update
        the frame’s tags accordingly.

        This filter accepts the following options:

        **force**

            If true, the frame’s existing colorspace tags will always be overridden by values detected from an ICC profile. Otherwise, they will only be assigned if they contain unknown. Enabled by default.



        Parameters:
        ----------

        :param bool force: If true, the frame’s existing colorspace tags will always be overridden by values detected from an ICC profile. Otherwise, they will only be assigned if they contain unknown. Enabled by default.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccdetect

        """
        filter_node = FilterNode(
            name="iccdetect",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "force": force,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def iccgen(
        self,
        *,
        color_primaries: int
        | Literal[
            "auto",
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
        | Default = Default(0),
        color_trc: int
        | Literal[
            "auto",
            "bt709",
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
        | Default = Default(0),
        force: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.133 iccgen

        Generate ICC profiles and attach them to frames.

        This filter accepts the following options:

        **color_primaries**

        **color_trc**

            Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.

        **force**

            If true, an ICC profile will be generated even if it would overwrite an already existing ICC profile. Disabled by default.



        Parameters:
        ----------

        :param int color_primaries: Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        :param int color_trc: Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        :param bool force: If true, an ICC profile will be generated even if it would overwrite an already existing ICC profile. Disabled by default.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccgen

        """
        filter_node = FilterNode(
            name="iccgen",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "color_primaries": color_primaries,
                        "color_trc": color_trc,
                        "force": force,
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
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the Identity between two video streams.

        Parameters:
        ----------

        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def idet(
        self,
        *,
        intl_thres: float | int | str = Default(1.04),
        prog_thres: float | int | str = Default(1.5),
        rep_thres: float | int | str = Default(3.0),
        half_life: float | int | str = Default(0.0),
        analyze_interlaced_flag: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Interlace detect Filter.

        Parameters:
        ----------

        :param float intl_thres: Set interlacing threshold.
        :param float prog_thres: Set progressive threshold.
        :param float rep_thres: Threshold for repeated field detection.
        :param float half_life: Number of frames after which a given frame’s contribution to the statistics is halved (i.e., it contributes only 0.5 to its classification). The default of 0 means that all frames seen are given full weight of 1.0 forever.
        :param int analyze_interlaced_flag: When this is not 0 then idet will use the specified number of frames to determine if the interlaced flag is accurate, it will not count undetermined frames. If the flag is found to be accurate it will be used without any further computations, if it is found to be inaccurate it will be cleared without any further computations. This allows inserting the idet filter as a low computational method to clean up the interlaced flag

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
        luma_mode: int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("MODE_NONE"),
        chroma_mode: int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("MODE_NONE"),
        alpha_mode: int | Literal["none", "interleave", "i", "deinterleave", "d"] | Default = Default("MODE_NONE"),
        luma_swap: bool | int | str = Default(0),
        chroma_swap: bool | int | str = Default(0),
        alpha_swap: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterleave or interleave fields.

        Parameters:
        ----------

        :param int luma_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param int chroma_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param int alpha_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param bool luma_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        :param bool chroma_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        :param bool alpha_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
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
        threshold0: int | str = Default(65535),
        threshold1: int | str = Default(65535),
        threshold2: int | str = Default(65535),
        threshold3: int | str = Default(65535),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply inflate effect.

        Parameters:
        ----------

        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
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
        scan: int | str = Default("MODE_TFF"),
        lowpass: int | Literal["off", "linear", "complex"] | Default = Default("VLPF_LIN"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert progressive video into interlaced.

        Parameters:
        ----------

        :param int scan: This determines whether the interlaced frame is taken from the even (tff - default) or odd (bff) lines of the progressive frame.
        :param int lowpass: Vertical lowpass filter to avoid twitter interlacing and reduce moire patterns. ‘0, off’ Disable vertical lowpass filter ‘1, linear’ Enable linear filter (default) ‘2, complex’ Enable complex filter. This will slightly less reduce twitter and moire but better retain detail and subjective sharpness impression.

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
        thresh: int | str = Default(10),
        map: bool | int | str = Default(0),
        order: bool | int | str = Default(0),
        sharp: bool | int | str = Default(0),
        twoway: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kernel deinterlacing to the input.

        Parameters:
        ----------

        :param int thresh: Set the threshold which affects the filter’s tolerance when determining if a pixel line must be processed. It must be an integer in the range [0,255] and defaults to 10. A value of 0 will result in applying the process on every pixels.
        :param bool map: Paint pixels exceeding the threshold value to white if set to 1. Default is 0.
        :param bool order: Set the fields order. Swap fields if set to 1, leave fields alone if 0. Default is 0.
        :param bool sharp: Enable additional sharpening if set to 1. Default is 0.
        :param bool twoway: Enable twoway sharpening if set to 1. Default is 0.

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
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply kirsch operator.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.
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
        decay: float | int | str = Default(0.95),
        planes: str | float | int = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Slowly update darker pixels.

        Parameters:
        ----------

        :param float decay: Set factor for decaying. Default is .95. Allowed range is from 0 to 1.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.
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

    def latency(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
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
        cx: float | int | str = Default(0.5),
        cy: float | int | str = Default(0.5),
        k1: float | int | str = Default(0.0),
        k2: float | int | str = Default(0.0),
        i: int | Literal["nearest", "bilinear"] | Default = Default(0),
        fc: str | float | int = Default("black@0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rectify the image by correcting for lens distortion.

        Parameters:
        ----------

        :param float cx: set relative center x
        :param float cy: set relative center y
        :param float k1: set quadratic distortion factor
        :param float k2: set double quadratic distortion factor
        :param int i: set interpolation type
        :param str fc: set the color of the unmapped pixels
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

    def lensfun(
        self,
        *,
        make: str | float | int = Default("((void*)0)"),
        model: str | float | int = Default("((void*)0)"),
        lens_model: str | float | int = Default("((void*)0)"),
        db_path: str | float | int = Default("((void*)0)"),
        mode: int
        | Literal["vignetting", "geometry", "subpixel", "vig_geo", "vig_subpixel", "distortion", "all"]
        | Default = Default("GEOMETRY_DISTORTION"),
        focal_length: float | int | str = Default(18.0),
        aperture: float | int | str = Default(3.5),
        focus_distance: float | int | str = Default("1000.0f"),
        scale: float | int | str = Default(0.0),
        target_geometry: int
        | Literal[
            "rectilinear",
            "fisheye",
            "panoramic",
            "equirectangular",
            "fisheye_orthographic",
            "fisheye_stereographic",
            "fisheye_equisolid",
            "fisheye_thoby",
        ]
        | Default = Default("LF_RECTILINEAR"),
        reverse: bool | int | str = Default(0),
        interpolation: int | Literal["nearest", "linear", "lanczos"] | Default = Default("LINEAR"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.143 lensfun

        Apply lens correction via the lensfun library
        (<http://lensfun.sourceforge.net/>).

        The `lensfun` filter requires the camera make, camera model, and lens model to
        apply the lens correction. The filter will load the lensfun database and query
        it to find the corresponding camera and lens entries in the database. As long
        as these entries can be found with the given options, the filter can perform
        corrections on frames. Note that incomplete strings will result in the filter
        choosing the best match with the given options, and the filter will output the
        chosen camera and lens models (logged with level "info"). You must provide the
        make, camera model, and lens model as they are required.

        To obtain a list of available makes and models, leave out one or both of
        `make` and `model` options. The filter will send the full list to the log with
        level `INFO`. The first column is the make and the second column is the model.
        To obtain a list of available lenses, set any values for make and model and
        leave out the `lens_model` option. The filter will send the full list of
        lenses in the log with level `INFO`. The ffmpeg tool will exit after the list
        is printed.

        The filter accepts the following options:

        **make**

            The make of the camera (for example, "Canon"). This option is required.

        **model**

            The model of the camera (for example, "Canon EOS 100D"). This option is required.

        **lens_model**

            The model of the lens (for example, "Canon EF-S 18-55mm f/3.5-5.6 IS STM"). This option is required.

        **db_path**

            The full path to the lens database folder. If not set, the filter will attempt to load the database from the install path when the library was built. Default is unset.

        **mode**

            The type of correction to apply. The following values are valid options: ‘vignetting’ Enables fixing lens vignetting. ‘geometry’ Enables fixing lens geometry. This is the default. ‘subpixel’ Enables fixing chromatic aberrations. ‘vig_geo’ Enables fixing lens vignetting and lens geometry. ‘vig_subpixel’ Enables fixing lens vignetting and chromatic aberrations. ‘distortion’ Enables fixing both lens geometry and chromatic aberrations. ‘all’ Enables all possible corrections.

        **focal_length**

            The focal length of the image/video (zoom; expected constant for video). For example, a 18–55mm lens has focal length range of [18–55], so a value in that range should be chosen when using that lens. Default 18.

        **aperture**

            The aperture of the image/video (expected constant for video). Note that aperture is only used for vignetting correction. Default 3.5.

        **focus_distance**

            The focus distance of the image/video (expected constant for video). Note that focus distance is only used for vignetting and only slightly affects the vignetting correction process. If unknown, leave it at the default value (which is 1000).

        **scale**

            The scale factor which is applied after transformation. After correction the video is no longer necessarily rectangular. This parameter controls how much of the resulting image is visible. The value 0 means that a value will be chosen automatically such that there is little or no unmapped area in the output image. 1.0 means that no additional scaling is done. Lower values may result in more of the corrected image being visible, while higher values may avoid unmapped areas in the output.

        **target_geometry**

            The target geometry of the output image/video. The following values are valid options: ‘rectilinear (default)’ ‘fisheye’ ‘panoramic’ ‘equirectangular’ ‘fisheye_orthographic’ ‘fisheye_stereographic’ ‘fisheye_equisolid’ ‘fisheye_thoby’

        **reverse**

            Apply the reverse of image correction (instead of correcting distortion, apply it).

        **interpolation**

            The type of interpolation used when correcting distortion. The following values are valid options: ‘nearest’ ‘linear (default)’ ‘lanczos’



        Parameters:
        ----------

        :param str make: The make of the camera (for example, "Canon"). This option is required.
        :param str model: The model of the camera (for example, "Canon EOS 100D"). This option is required.
        :param str lens_model: The model of the lens (for example, "Canon EF-S 18-55mm f/3.5-5.6 IS STM"). This option is required.
        :param str db_path: The full path to the lens database folder. If not set, the filter will attempt to load the database from the install path when the library was built. Default is unset.
        :param int mode: The type of correction to apply. The following values are valid options: ‘vignetting’ Enables fixing lens vignetting. ‘geometry’ Enables fixing lens geometry. This is the default. ‘subpixel’ Enables fixing chromatic aberrations. ‘vig_geo’ Enables fixing lens vignetting and lens geometry. ‘vig_subpixel’ Enables fixing lens vignetting and chromatic aberrations. ‘distortion’ Enables fixing both lens geometry and chromatic aberrations. ‘all’ Enables all possible corrections.
        :param float focal_length: The focal length of the image/video (zoom; expected constant for video). For example, a 18–55mm lens has focal length range of [18–55], so a value in that range should be chosen when using that lens. Default 18.
        :param float aperture: The aperture of the image/video (expected constant for video). Note that aperture is only used for vignetting correction. Default 3.5.
        :param float focus_distance: The focus distance of the image/video (expected constant for video). Note that focus distance is only used for vignetting and only slightly affects the vignetting correction process. If unknown, leave it at the default value (which is 1000).
        :param float scale: The scale factor which is applied after transformation. After correction the video is no longer necessarily rectangular. This parameter controls how much of the resulting image is visible. The value 0 means that a value will be chosen automatically such that there is little or no unmapped area in the output image. 1.0 means that no additional scaling is done. Lower values may result in more of the corrected image being visible, while higher values may avoid unmapped areas in the output.
        :param int target_geometry: The target geometry of the output image/video. The following values are valid options: ‘rectilinear (default)’ ‘fisheye’ ‘panoramic’ ‘equirectangular’ ‘fisheye_orthographic’ ‘fisheye_stereographic’ ‘fisheye_equisolid’ ‘fisheye_thoby’
        :param bool reverse: Apply the reverse of image correction (instead of correcting distortion, apply it).
        :param int interpolation: The type of interpolation used when correcting distortion. The following values are valid options: ‘nearest’ ‘linear (default)’ ‘lanczos’
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lensfun

        """
        filter_node = FilterNode(
            name="lensfun",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "make": make,
                        "model": model,
                        "lens_model": lens_model,
                        "db_path": db_path,
                        "mode": mode,
                        "focal_length": focal_length,
                        "aperture": aperture,
                        "focus_distance": focus_distance,
                        "scale": scale,
                        "target_geometry": target_geometry,
                        "reverse": reverse,
                        "interpolation": interpolation,
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
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the VMAF between two video streams.

        Parameters:
        ----------

        :param str log_path: Set the file path to be used to store log files.
        :param str log_fmt: Set the format of the log file (xml, json, csv, or sub).
        :param str pool: Set the pool method to be used for computing vmaf. Options are min, harmonic_mean or mean (default).
        :param int n_threads: Set number of threads to be used when initializing libvmaf. Default value: 0, no threads.
        :param int n_subsample: Set frame subsampling interval to be used.
        :param str model: A ‘|‘ delimited list of vmaf models. Each model can be configured with a number of parameters. Default value: "version=vmaf_v0.6.1"
        :param str feature: A ‘|‘ delimited list of features. Each feature can be configured with a number of parameters.
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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

    def libvmaf_cuda(
        self,
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
        **kwargs: Any,
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
                self,
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

    def limiter(
        self,
        *,
        min: int | str = Default(0),
        max: int | str = Default(65535),
        planes: int | str = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Limit pixels components to the specified range.

        Parameters:
        ----------

        :param int min: Lower bound. Defaults to the lowest allowed value for the input.
        :param int max: Upper bound. Defaults to the highest allowed value for the input.
        :param int planes: Specify which planes will be processed. Defaults to all available.
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
        self,
        *,
        loop: int | str = Default(0),
        size: int | str = Default(0),
        start: int | str = Default(0),
        time: int | str = Default("9223372036854775807LL"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Loop video frames.

        Parameters:
        ----------

        :param int loop: Set the number of loops. Setting this value to -1 will result in infinite loops. Default is 0.
        :param int size: Set maximal size in number of frames. Default is 0.
        :param int start: Set first frame of loop. Default is 0.
        :param int time: Set the time of loop start in seconds. Only used if option named start is set to -1.

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
                        "time": time,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def lumakey(
        self,
        *,
        threshold: float | int | str = Default(0.0),
        tolerance: float | int | str = Default(0.01),
        softness: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Turns a certain luma into transparency.

        Parameters:
        ----------

        :param float threshold: Set the luma which will be used as base for transparency. Default value is 0.
        :param float tolerance: Set the range of luma values to be keyed out. Default value is 0.01.
        :param float softness: Set the range of softness. Default value is 0. Use this to control gradual transition from zero to full transparency.
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
        c0: str | float | int = Default("clipval"),
        c1: str | float | int = Default("clipval"),
        c2: str | float | int = Default("clipval"),
        c3: str | float | int = Default("clipval"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB/YUV input video.

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component
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
        file: str | float | int = Default("((void*)0)"),
        interp: int
        | Literal["nearest", "linear", "cosine", "cubic", "spline"]
        | Default = Default("INTERPOLATE_1D_LINEAR"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 1D LUT.

        Parameters:
        ----------

        :param str file: Set the 1D LUT file name. Currently supported formats: ‘cube’ Iridas ‘csp’ cineSpace
        :param int interp: Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘linear’ Interpolate values using the linear interpolation. ‘cosine’ Interpolate values using the cosine interpolation. ‘cubic’ Interpolate values using the cubic interpolation. ‘spline’ Interpolate values using the spline interpolation.
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
        c0: str | float | int = Default("x"),
        c1: str | float | int = Default("x"),
        c2: str | float | int = Default("x"),
        c3: str | float | int = Default("x"),
        d: int | str = Default(0),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table from two video inputs.

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component
        :param int d: set output bit depth, only available for lut2 filter. By default is 0, which means bit depth is automatically picked from first input format.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def lut3d(
        self,
        *,
        file: str | float | int = Default("((void*)0)"),
        clut: int | Literal["first", "all"] | Default = Default(1),
        interp: int
        | Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | Default = Default("INTERPOLATE_TETRAHEDRAL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Adjust colors using a 3D LUT.

        Parameters:
        ----------

        :param str file: Set the 3D LUT file name. Currently supported formats: ‘3dl’ AfterEffects ‘cube’ Iridas ‘dat’ DaVinci ‘m3d’ Pandora ‘csp’ cineSpace
        :param int clut: when to process CLUT
        :param int interp: Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘trilinear’ Interpolate values using the 8 points defining a cube. ‘tetrahedral’ Interpolate values using a tetrahedron. ‘pyramid’ Interpolate values using a pyramid. ‘prism’ Interpolate values using a prism.
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
        c0: str | float | int = Default("clipval"),
        c1: str | float | int = Default("clipval"),
        c2: str | float | int = Default("clipval"),
        c3: str | float | int = Default("clipval"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the RGB input video.

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component
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
        c0: str | float | int = Default("clipval"),
        c1: str | float | int = Default("clipval"),
        c2: str | float | int = Default("clipval"),
        c3: str | float | int = Default("clipval"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table to the YUV input video.

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component
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
        undershoot: int | str = Default(0),
        overshoot: int | str = Default(0),
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Clamp first stream with second stream and third stream.

        Parameters:
        ----------

        :param int undershoot: Default value is 0.
        :param int overshoot: Default value is 0.
        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
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
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply filtering with maximum difference of two streams.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
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
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Merge first stream with second stream using third stream as mask.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
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
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply filtering with minimum difference of two streams.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
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
        threshold: int | str = Default(1),
        planes: int | str = Default("0xF"),
        mode: int | Literal["abs", "diff"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick pixels comparing absolute difference of two streams with threshold.

        Parameters:
        ----------

        :param int threshold: Set threshold used when picking pixels from absolute difference from two input video streams.
        :param int planes: Set which planes will be processed as bitmap, unprocessed planes will be copied from second stream. By default value 0xf, all planes will be processed.
        :param int mode: Set mode of filter operation. Can be abs or diff. Default is abs.
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
        low: int | str = Default(10),
        high: int | str = Default(10),
        planes: int | str = Default("0xF"),
        fill: int | str = Default(0),
        sum: int | str = Default(10),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Create Mask.

        Parameters:
        ----------

        :param int low: Set low threshold. Any pixel component lower or exact than this value will be set to 0.
        :param int high: Set high threshold. Any pixel component higher than this value will be set to max value allowed for current pixel format.
        :param int planes: Set planes to filter, by default all available planes are filtered.
        :param int fill: Fill all frame pixels with this value.
        :param int sum: Set max average pixel value for frame. If sum of all pixel components is higher that this average, output frame will be completely filled with value set by fill option. Typically useful for scene changes when used in combination with tblend filter.
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

    def mcdeint(
        self,
        *,
        mode: int | str = Default("MODE_FAST"),
        parity: int | Literal["tff", "bff"] | Default = Default("PARITY_BFF"),
        qp: int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.161 mcdeint

        Apply motion-compensation deinterlacing.

        It needs one field per frame as input and must thus be used together with
        yadif=1/3 or equivalent.

        This filter accepts the following options:

        **mode**

            Set the deinterlacing mode. It accepts one of the following values: ‘fast’ ‘medium’ ‘slow’ use iterative motion estimation ‘extra_slow’ like ‘slow’, but use multiple reference frames. Default value is ‘fast’.

        **parity**

            Set the picture field parity assumed for the input video. It must be one of the following values: ‘0, tff’ assume top field first ‘1, bff’ assume bottom field first Default value is ‘bff’.

        **qp**

            Set per-block quantization parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.



        Parameters:
        ----------

        :param int mode: Set the deinterlacing mode. It accepts one of the following values: ‘fast’ ‘medium’ ‘slow’ use iterative motion estimation ‘extra_slow’ like ‘slow’, but use multiple reference frames. Default value is ‘fast’.
        :param int parity: Set the picture field parity assumed for the input video. It must be one of the following values: ‘0, tff’ assume top field first ‘1, bff’ assume bottom field first Default value is ‘bff’.
        :param int qp: Set per-block quantization parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcdeint

        """
        filter_node = FilterNode(
            name="mcdeint",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "mode": mode,
                        "parity": parity,
                        "qp": qp,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def median(
        self,
        *,
        radius: int | str = Default(1),
        planes: int | str = Default("0xF"),
        radiusV: int | str = Default(0),
        percentile: float | int | str = Default(0.5),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Median filter.

        Parameters:
        ----------

        :param int radius: Set horizontal radius size. Default value is 1. Allowed range is integer from 1 to 127.
        :param int planes: Set which planes to process. Default is 15, which is all available planes.
        :param int radiusV: Set vertical radius size. Default value is 0. Allowed range is integer from 0 to 127. If it is 0, value will be picked from horizontal radius option.
        :param float percentile: Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.
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
        method: int | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"] | Default = Default(1),
        mb_size: int | str = Default(16),
        search_param: int | str = Default(7),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate motion vectors.

        Parameters:
        ----------

        :param int method: Specify the motion estimation method. Accepts one of the following values: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default value is ‘esa’.
        :param int mb_size: Macroblock size. Default 16.
        :param int search_param: Search parameter. Default 7.

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
        mode: int | Literal["select", "add", "modify", "delete", "print"] | Default = Default(0),
        key: str | float | int = Default("((void*)0)"),
        value: str | float | int = Default("((void*)0)"),
        function: int
        | Literal["same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"]
        | Default = Default(0),
        expr: str | float | int = Default("((void*)0)"),
        file: str | float | int = Default("((void*)0)"),
        direct: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Manipulate video frame metadata.

        Parameters:
        ----------

        :param int mode: Set mode of operation of the filter. Can be one of the following: ‘select’ If both value and key is set, select frames which have such metadata. If only key is set, select every frame that has such key in metadata. ‘add’ Add new metadata key and value. If key is already available do nothing. ‘modify’ Modify value of already present key. ‘delete’ If value is set, delete only keys that have such value. Otherwise, delete key. If key is not set, delete all metadata values in the frame. ‘print’ Print key and its value if metadata was found. If key is not set print all metadata values available in frame.
        :param str key: Set key used with all modes. Must be set for all modes except print and delete.
        :param str value: Set metadata value which will be used. This option is mandatory for modify and add mode.
        :param int function: Which function to use when comparing metadata value and value. Can be one of following: ‘same_str’ Values are interpreted as strings, returns true if metadata value is same as value. ‘starts_with’ Values are interpreted as strings, returns true if metadata value starts with the value option string. ‘less’ Values are interpreted as floats, returns true if metadata value is less than value. ‘equal’ Values are interpreted as floats, returns true if value is equal with metadata value. ‘greater’ Values are interpreted as floats, returns true if metadata value is greater than value. ‘expr’ Values are interpreted as floats, returns true if expression from option expr evaluates to true. ‘ends_with’ Values are interpreted as strings, returns true if metadata value ends with the value option string.
        :param str expr: Set expression which is used when function is set to expr. The expression is evaluated through the eval API and can contain the following constants: VALUE1, FRAMEVAL Float representation of value from metadata key. VALUE2, USERVAL Float representation of value as supplied by user in value option.
        :param str file: If specified in print mode, output is written to the named file. Instead of plain filename any writable url can be specified. Filename “-” is a shorthand for standard output. If file option is not set, output is written to the log with AV_LOG_INFO loglevel.
        :param bool direct: Reduces buffering in print mode when output is written to a URL set using file.
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
        self,
        _in1: "VideoStream",
        *,
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Midway Equalization.

        Parameters:
        ----------

        :param int planes: Set which planes to process. Default is 15, which is all available planes.
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
        fps: str | float | int = Default("60"),
        mi_mode: int | Literal["dup", "blend", "mci"] | Default = Default("MI_MODE_MCI"),
        mc_mode: int | Literal["obmc", "aobmc"] | Default = Default(0),
        me_mode: int | Literal["bidir", "bilat"] | Default = Default(1),
        me: int | Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"] | Default = Default(8),
        mb_size: int | str = Default(16),
        search_param: int | str = Default(32),
        vsbmc: int | str = Default(0),
        scd: int | Literal["none", "fdiff"] | Default = Default(1),
        scd_threshold: float | int | str = Default(10.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Frame rate conversion using Motion Interpolation.

        Parameters:
        ----------

        :param str fps: Specify the output frame rate. This can be rational e.g. 60000/1001. Frames are dropped if fps is lower than source fps. Default 60.
        :param int mi_mode: Motion interpolation mode. Following values are accepted: ‘dup’ Duplicate previous or next frame for interpolating new ones. ‘blend’ Blend source frames. Interpolated frame is mean of previous and next frames. ‘mci’ Motion compensated interpolation. Following options are effective when this mode is selected: ‘mc_mode’ Motion compensation mode. Following values are accepted: ‘obmc’ Overlapped block motion compensation. ‘aobmc’ Adaptive overlapped block motion compensation. Window weighting coefficients are controlled adaptively according to the reliabilities of the neighboring motion vectors to reduce oversmoothing. Default mode is ‘obmc’. ‘me_mode’ Motion estimation mode. Following values are accepted: ‘bidir’ Bidirectional motion estimation. Motion vectors are estimated for each source frame in both forward and backward directions. ‘bilat’ Bilateral motion estimation. Motion vectors are estimated directly for interpolated frame. Default mode is ‘bilat’. ‘me’ The algorithm to be used for motion estimation. Following values are accepted: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default algorithm is ‘epzs’. ‘mb_size’ Macroblock size. Default 16. ‘search_param’ Motion estimation search parameter. Default 32. ‘vsbmc’ Enable variable-size block motion compensation. Motion estimation is applied with smaller block sizes at object boundaries in order to make the them less blur. Default is 0 (disabled).
        :param int mc_mode: motion compensation mode
        :param int me_mode: motion estimation mode
        :param int me: motion estimation method
        :param int mb_size: macroblock size
        :param int search_param: search parameter
        :param int vsbmc: variable-size block motion compensation
        :param int scd: Scene change detection method. Scene change leads motion vectors to be in random direction. Scene change detection replace interpolated frames by duplicate ones. May not be needed for other modes. Following values are accepted: ‘none’ Disable scene change detection. ‘fdiff’ Frame difference. Corresponding pixel values are compared and if it satisfies scd_threshold scene change is detected. Default method is ‘fdiff’.
        :param float scd_threshold: Scene change detection threshold. Default is 10..

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
        cb: float | int | str = Default(0.0),
        cr: float | int | str = Default(0.0),
        size: float | int | str = Default(1.0),
        high: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert video to gray using custom color filter.

        Parameters:
        ----------

        :param float cb: Set the chroma blue spot. Allowed range is from -1 to 1. Default value is 0.
        :param float cr: Set the chroma red spot. Allowed range is from -1 to 1. Default value is 0.
        :param float size: Set the color filter size. Allowed range is from .1 to 10. Default value is 1.
        :param float high: Set the highlights strength. Allowed range is from 0 to 1. Default value is 0.
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
        mode: int
        | Literal["erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"]
        | Default = Default(0),
        planes: int | str = Default(7),
        structure: int | Literal["first", "all"] | Default = Default(1),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Morphological filter.

        Parameters:
        ----------

        :param int mode: Set morphological transform to apply, can be: ‘erode’ ‘dilate’ ‘open’ ‘close’ ‘gradient’ ‘tophat’ ‘blackhat’ Default is erode.
        :param int planes: Set planes to filter, by default all planes except alpha are filtered.
        :param int structure: Set which structure video frames will be processed from second input stream, can be first or all. Default is all.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def mpdecimate(
        self,
        *,
        max: int | str = Default(0),
        keep: int | str = Default(0),
        hi: int | str = Default("64*12"),
        lo: int | str = Default("64*5"),
        frac: float | int | str = Default(0.33),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove near-duplicate frames.

        Parameters:
        ----------

        :param int max: Set the maximum number of consecutive frames which can be dropped (if positive), or the minimum interval between dropped frames (if negative). If the value is 0, the frame is dropped disregarding the number of previous sequentially dropped frames. Default value is 0.
        :param int keep: Set the maximum number of consecutive similar frames to ignore before to start dropping them. If the value is 0, the frame is dropped disregarding the number of previous sequentially similar frames. Default value is 0.
        :param int hi: Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.
        :param int lo: Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.
        :param float frac: Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.

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
                        "keep": keep,
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
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the MSAD between two video streams.

        Parameters:
        ----------

        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def multiply(
        self,
        _factor: "VideoStream",
        *,
        scale: float | int | str = Default(1.0),
        offset: float | int | str = Default(0.5),
        planes: str | float | int = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Multiply first video stream with second video stream.

        Parameters:
        ----------

        :param float scale: Set the scale applied to second video stream. By default is 1. Allowed range is from 0 to 9.
        :param float offset: Set the offset applied to second video stream. By default is 0.5. Allowed range is from -1 to 1.
        :param str planes: Specify planes from input video stream that will be processed. By default all planes are processed.
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
        components: str | Literal["y", "u", "v", "r", "g", "b", "a"] | Default = Default("0x77"),
        negate_alpha: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Negate input video.

        Parameters:
        ----------

        :param str components: Set components to negate. Available values for components are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’
        :param bool negate_alpha: With value 1, it negates the alpha component, if present. Default value is 0.
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
        s: float | int | str = Default(1.0),
        p: int | str = Default("3*2+1"),
        pc: int | str = Default(0),
        r: int | str = Default("7*2+1"),
        rc: int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Non-local means denoiser.

        Parameters:
        ----------

        :param float s: Set denoising strength. Default is 1.0. Must be in range [1.0, 30.0].
        :param int p: Set patch size. Default is 7. Must be odd number in range [0, 99].
        :param int pc: Same as p but for chroma planes. The default value is 0 and means automatic.
        :param int r: Set research size. Default is 15. Must be odd number in range [0, 99].
        :param int rc: Same as r but for chroma planes. The default value is 0 and means automatic.
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

    def nlmeans_opencl(
        self,
        *,
        s: float | int | str = Default(1.0),
        p: int | str = Default("2*3+1"),
        pc: int | str = Default(0),
        r: int | str = Default("7*2+1"),
        rc: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.8 nlmeans_opencl

        Non-local Means denoise filter through OpenCL, this filter accepts same
        options as nlmeans.



        Parameters:
        ----------

        :param float s: denoising strength
        :param int p: patch size
        :param int pc: patch size for chroma planes
        :param int r: research window
        :param int rc: research window for chroma planes

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fopencl

        """
        filter_node = FilterNode(
            name="nlmeans_opencl",
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def nlmeans_vulkan(
        self,
        *,
        s: float | int | str = Default(1.0),
        p: int | str = Default("3*2+1"),
        r: int | str = Default("7*2+1"),
        t: int | str = Default(36),
        s1: float | int | str = Default(1.0),
        s2: float | int | str = Default(1.0),
        s3: float | int | str = Default(1.0),
        s4: float | int | str = Default(1.0),
        p1: int | str = Default(0),
        p2: int | str = Default(0),
        p3: int | str = Default(0),
        p4: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.10 nlmeans_vulkan

        Denoise frames using Non-Local Means algorithm, implemented on the GPU using
        Vulkan. Supports more pixel formats than nlmeans or nlmeans_opencl, including
        alpha channel support.

        The filter accepts the following options.

        **s**

            Set denoising strength for all components. Default is 1.0. Must be in range [1.0, 100.0].

        **p**

            Set patch size for all planes. Default is 7. Must be odd number in range [0, 99].

        **r**

            Set research size. Default is 15. Must be odd number in range [0, 99].

        **t**

            Set parallelism. Default is 36. Must be a number in the range [1, 168]. Larger values may speed up processing, at the cost of more VRAM. Lower values will slow it down, reducing VRAM usage. Only supported on GPUs with atomic float operations (RDNA3+, Ampere+).

        **s0**

        **s1**

        **s2**

        **s3**

            Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].

        **p0**

        **p1**

        **p2**

        **p3**

            Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].



        Parameters:
        ----------

        :param float s: Set denoising strength for all components. Default is 1.0. Must be in range [1.0, 100.0].
        :param int p: Set patch size for all planes. Default is 7. Must be odd number in range [0, 99].
        :param int r: Set research size. Default is 15. Must be odd number in range [0, 99].
        :param int t: Set parallelism. Default is 36. Must be a number in the range [1, 168]. Larger values may speed up processing, at the cost of more VRAM. Lower values will slow it down, reducing VRAM usage. Only supported on GPUs with atomic float operations (RDNA3+, Ampere+).
        :param float s1: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s2: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s3: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s4: denoising strength for component 4
        :param int p1: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p2: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p3: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p4: patch size for component 4

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fvulkan

        """
        filter_node = FilterNode(
            name="nlmeans_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def nnedi(
        self,
        *,
        weights: str | float | int = Default("nnedi3_weights.bin"),
        deint: int | Literal["all", "interlaced"] | Default = Default(0),
        field: int | Literal["af", "a", "t", "b", "tf", "bf"] | Default = Default(-1),
        planes: int | str = Default(7),
        nsize: int | Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"] | Default = Default(6),
        nns: int | Literal["n16", "n32", "n64", "n128", "n256"] | Default = Default(1),
        qual: int | Literal["fast", "slow"] | Default = Default(1),
        etype: int | Literal["a", "abs", "s", "mse"] | Default = Default(0),
        pscrn: int | Literal["none", "original", "new", "new2", "new3"] | Default = Default(2),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply neural network edge directed interpolation intra-only deinterlacer.

        Parameters:
        ----------

        :param str weights: Mandatory option, without binary file filter can not work. Currently file can be found here: https://github.com/dubhater/vapoursynth-nnedi3/blob/master/src/nnedi3_weights.bin
        :param int deint: Set which frames to deinterlace, by default it is all. Can be all or interlaced.
        :param int field: Set mode of operation. Can be one of the following: ‘af’ Use frame flags, both fields. ‘a’ Use frame flags, single field. ‘t’ Use top field only. ‘b’ Use bottom field only. ‘tf’ Use both fields, top first. ‘bf’ Use both fields, bottom first.
        :param int planes: Set which planes to process, by default filter process all frames.
        :param int nsize: Set size of local neighborhood around each pixel, used by the predictor neural network. Can be one of the following: ‘s8x6’ ‘s16x6’ ‘s32x6’ ‘s48x6’ ‘s8x4’ ‘s16x4’ ‘s32x4’
        :param int nns: Set the number of neurons in predictor neural network. Can be one of the following: ‘n16’ ‘n32’ ‘n64’ ‘n128’ ‘n256’
        :param int qual: Controls the number of different neural network predictions that are blended together to compute the final output value. Can be fast, default or slow.
        :param int etype: Set which set of weights to use in the predictor. Can be one of the following: ‘a, abs’ weights trained to minimize absolute error ‘s, mse’ weights trained to minimize squared error
        :param int pscrn: Controls whether or not the prescreener neural network is used to decide which pixels should be processed by the predictor neural network and which can be handled by simple cubic interpolation. The prescreener is trained to know whether cubic interpolation will be sufficient for a pixel or whether it should be predicted by the predictor nn. The computational complexity of the prescreener nn is much less than that of the predictor nn. Since most pixels can be handled by cubic interpolation, using the prescreener generally results in much faster processing. The prescreener is pretty accurate, so the difference between using it and not using it is almost always unnoticeable. Can be one of the following: ‘none’ ‘original’ ‘new’ ‘new2’ ‘new3’ Default is new.
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

    def noformat(self, *, pix_fmts: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
        """

        Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

        Parameters:
        ----------

        :param str pix_fmts: A ’|’-separated list of pixel format names, such as pix_fmts=yuv420p|monow|rgb24".

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
        all_seed: int | str = Default(-1),
        all_strength: int | str = Default(0),
        all_flags: str | Literal["a", "p", "t", "u"] | Default = Default(0),
        c0_seed: int | str = Default(-1),
        c0_strength: int | str = Default(0),
        c0_flags: str | Literal["a", "p", "t", "u"] | Default = Default(0),
        c1_seed: int | str = Default(-1),
        c1_strength: int | str = Default(0),
        c1_flags: str | Literal["a", "p", "t", "u"] | Default = Default(0),
        c2_seed: int | str = Default(-1),
        c2_strength: int | str = Default(0),
        c2_flags: str | Literal["a", "p", "t", "u"] | Default = Default(0),
        c3_seed: int | str = Default(-1),
        c3_strength: int | str = Default(0),
        c3_flags: str | Literal["a", "p", "t", "u"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Add noise.

        Parameters:
        ----------

        :param int all_seed: Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        :param int all_strength: Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        :param str all_flags: Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        :param int c0_seed: Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        :param int c0_strength: Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        :param str c0_flags: Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        :param int c1_seed: Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        :param int c1_strength: Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        :param str c1_flags: Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        :param int c2_seed: Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        :param int c2_strength: Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        :param str c2_flags: Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        :param int c3_seed: Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        :param int c3_strength: Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        :param str c3_flags: Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
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
        blackpt: str | float | int = Default("black"),
        whitept: str | float | int = Default("white"),
        smoothing: int | str = Default(0),
        independence: float | int | str = Default(1.0),
        strength: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Normalize RGB video.

        Parameters:
        ----------

        :param str blackpt: Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        :param str whitept: Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        :param int smoothing: The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).
        :param float independence: Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).
        :param float strength: Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).
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
        datapath: str | float | int = Default("((void*)0)"),
        language: str | float | int = Default("eng"),
        whitelist: str
        | float
        | int = Default(
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?\\\\\"\\'[]{}()<>|/\\\\\\\\=*&%$#@!~ "
        ),
        blacklist: str | float | int = Default(""),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Optical Character Recognition.

        Parameters:
        ----------

        :param str datapath: Set datapath to tesseract data. Default is to use whatever was set at installation.
        :param str language: Set language, default is "eng".
        :param str whitelist: Set character whitelist.
        :param str blacklist: Set character blacklist.

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

    def ocv(
        self,
        *,
        filter_name: str | float | int = Default(None),
        filter_params: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.181 ocv

        Apply a video transform using libopencv.

        To enable this filter, install the libopencv library and headers and configure
        FFmpeg with `--enable-libopencv`.

        It accepts the following parameters:

        **filter_name**

            The name of the libopencv filter to apply.

        **filter_params**

            The parameters to pass to the libopencv filter. If not specified, the default values are assumed.

        Refer to the official libopencv documentation for more precise information:
        <http://docs.opencv.org/master/modules/imgproc/doc/filtering.html>

        Several libopencv filters are supported; see the following subsections.



        Parameters:
        ----------

        :param str filter_name: The name of the libopencv filter to apply.
        :param str filter_params: The parameters to pass to the libopencv filter. If not specified, the default values are assumed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ocv

        """
        filter_node = FilterNode(
            name="ocv",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "filter_name": filter_name,
                        "filter_params": filter_params,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def oscilloscope(
        self,
        *,
        x: float | int | str = Default(0.5),
        y: float | int | str = Default(0.5),
        s: float | int | str = Default(0.8),
        t: float | int | str = Default(0.5),
        o: float | int | str = Default(0.8),
        tx: float | int | str = Default(0.5),
        ty: float | int | str = Default(0.9),
        tw: float | int | str = Default(0.8),
        th: float | int | str = Default(0.3),
        c: int | str = Default(7),
        g: bool | int | str = Default(1),
        st: bool | int | str = Default(1),
        sc: bool | int | str = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        2D Video Oscilloscope.

        Parameters:
        ----------

        :param float x: Set scope center x position.
        :param float y: Set scope center y position.
        :param float s: Set scope size, relative to frame diagonal.
        :param float t: Set scope tilt/rotation.
        :param float o: Set trace opacity.
        :param float tx: Set trace center x position.
        :param float ty: Set trace center y position.
        :param float tw: Set trace width, relative to width of frame.
        :param float th: Set trace height, relative to height of frame.
        :param int c: Set which components to trace. By default it traces first three components.
        :param bool g: Draw trace grid. By default is enabled.
        :param bool st: Draw some statistics. By default is enabled.
        :param bool sc: Draw scope. By default is enabled.
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
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("EOF_ACTION_REPEAT"),
        eval: int | str = Default("EVAL_MODE_FRAME"),
        shortest: bool | int | str = Default(0),
        format: int | str = Default("OVERLAY_FORMAT_YUV420"),
        repeatlast: bool | int | str = Default(1),
        alpha: int | str = Default(0),
        enable: str | float | int = Default(None),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Overlay a video source on top of the input.

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
        :param str enable: timeline editing
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
                        "ts_sync_mode": ts_sync_mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def overlay_cuda(
        self,
        _overlay: "VideoStream",
        *,
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        eof_action: int | Literal["repeat", "endall", "pass"] | Default = Default("EOF_ACTION_REPEAT"),
        eval: int | str = Default("EVAL_MODE_FRAME"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
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
                        "repeatlast": repeatlast,
                        "ts_sync_mode": ts_sync_mode,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def overlay_opencl(
        self, _overlay: "VideoStream", *, x: int | str = Default(0), y: int | str = Default(0), **kwargs: Any
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
                self,
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
        self,
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
        **kwargs: Any,
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
                self,
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
        self, _overlay: "VideoStream", *, x: int | str = Default(0), y: int | str = Default(0), **kwargs: Any
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
                self,
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

    def owdenoise(
        self,
        *,
        depth: int | str = Default(8),
        luma_strength: float | int | str = Default(1.0),
        chroma_strength: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Denoise using wavelets.

        Parameters:
        ----------

        :param int depth: Set depth. Larger depth values will denoise lower frequency components more, but slow down filtering. Must be an int in the range 8-16, default is 8.
        :param float luma_strength: Set luma strength. Must be a double value in the range 0-1000, default is 1.0.
        :param float chroma_strength: Set chroma strength. Must be a double value in the range 0-1000, default is 1.0.
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
        width: str | float | int = Default("iw"),
        height: str | float | int = Default("ih"),
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        color: str | float | int = Default("black"),
        eval: int | str = Default("EVAL_MODE_INIT"),
        aspect: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pad the input video.

        Parameters:
        ----------

        :param str width: Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        :param str height: Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        :param str x: Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        :param str y: Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        :param str color: Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".
        :param int eval: Specify when to evaluate width, height, x and y expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame. Default value is ‘init’.
        :param float aspect: Pad to aspect instead to a resolution.

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

    def pad_opencl(
        self,
        *,
        width: str | float | int = Default("iw"),
        height: str | float | int = Default("ih"),
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        color: str | float | int = Default("black"),
        aspect: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.10 pad_opencl

        Add paddings to the input image, and place the original input at the provided
        x, y coordinates.

        It accepts the following options:

        **width, w**

        **height, h**

            Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.

        **x**

        **y**

            Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.

        **color**

            Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.

        **aspect**

            Pad to an aspect instead to a resolution.

        The value for the width, height, x, and y options are expressions containing
        the following constants:

        **in_w**

        **in_h**

            The input video width and height.

        **iw**

        **ih**

            These are the same as in_w and in_h.

        **out_w**

        **out_h**

            The output width and height (the size of the padded area), as specified by the width and height expressions.

        **ow**

        **oh**

            These are the same as out_w and out_h.

        **x**

        **y**

            The x and y offsets as specified by the x and y expressions, or NAN if not yet specified.

        **a**

            same as iw / ih

        **sar**

            input sample aspect ratio

        **dar**

            input display aspect ratio, it is the same as (iw / ih) * sar



        Parameters:
        ----------

        :param str width: Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        :param str height: Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        :param str x: Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        :param str y: Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        :param str color: Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
        :param float aspect: Pad to an aspect instead to a resolution.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pad_005fopencl

        """
        filter_node = FilterNode(
            name="pad_opencl",
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
        max_colors: int | str = Default(256),
        reserve_transparent: bool | int | str = Default(1),
        transparency_color: str | float | int = Default("lime"),
        stats_mode: int | Literal["full", "diff", "single"] | Default = Default("STATS_MODE_ALL_FRAMES"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Find the optimal palette for a given stream.

        Parameters:
        ----------

        :param int max_colors: Set the maximum number of colors to quantize in the palette. Note: the palette will still contain 256 colors; the unused palette entries will be black.
        :param bool reserve_transparent: Create a palette of 255 colors maximum and reserve the last one for transparency. Reserving the transparency color is useful for GIF optimization. If not set, the maximum of colors in the palette will be 256. You probably want to disable this option for a standalone image. Set by default.
        :param str transparency_color: Set the color that will be used as background for transparency.
        :param int stats_mode: Set statistics mode. It accepts the following values: ‘full’ Compute full frame histograms. ‘diff’ Compute histograms only for the part that differs from previous frame. This might be relevant to give more importance to the moving part of your input if the background is static. ‘single’ Compute new histogram for each frame. Default value is full.

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
        dither: int
        | Literal["bayer", "heckbert", "floyd_steinberg", "sierra2", "sierra2_4a", "sierra3", "burkes", "atkinson"]
        | Default = Default("DITHERING_SIERRA2_4A"),
        bayer_scale: int | str = Default(2),
        diff_mode: int | Literal["rectangle"] | Default = Default("DIFF_MODE_NONE"),
        new: bool | int | str = Default(0),
        alpha_threshold: int | str = Default(128),
        debug_kdtree: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Use a palette to downsample an input video stream.

        Parameters:
        ----------

        :param int dither: Select dithering mode. Available algorithms are: ‘bayer’ Ordered 8x8 bayer dithering (deterministic) ‘heckbert’ Dithering as defined by Paul Heckbert in 1982 (simple error diffusion). Note: this dithering is sometimes considered "wrong" and is included as a reference. ‘floyd_steinberg’ Floyd and Steingberg dithering (error diffusion) ‘sierra2’ Frankie Sierra dithering v2 (error diffusion) ‘sierra2_4a’ Frankie Sierra dithering v2 "Lite" (error diffusion) ‘sierra3’ Frankie Sierra dithering v3 (error diffusion) ‘burkes’ Burkes dithering (error diffusion) ‘atkinson’ Atkinson dithering by Bill Atkinson at Apple Computer (error diffusion) ‘none’ Disable dithering. Default is sierra2_4a.
        :param int bayer_scale: When bayer dithering is selected, this option defines the scale of the pattern (how much the crosshatch pattern is visible). A low value means more visible pattern for less banding, and higher value means less visible pattern at the cost of more banding. The option must be an integer value in the range [0,5]. Default is 2.
        :param int diff_mode: If set, define the zone to process ‘rectangle’ Only the changing rectangle will be reprocessed. This is similar to GIF cropping/offsetting compression mechanism. This option can be useful for speed if only a part of the image is changing, and has use cases such as limiting the scope of the error diffusal dither to the rectangle that bounds the moving scene (it leads to more deterministic output if the scene doesn’t change much, and as a result less moving noise and better GIF compression). Default is none.
        :param bool new: Take new palette for each output frame.
        :param int alpha_threshold: Sets the alpha threshold for transparency. Alpha values above this threshold will be treated as completely opaque, and values below this threshold will be treated as completely transparent. The option must be an integer value in the range [0,255]. Default is 128.
        :param str debug_kdtree: save Graphviz graph of the kdtree in specified file

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
        mode: int | Literal["none", "ro", "rw", "toggle", "random"] | Default = Default("MODE_NONE"),
        seed: int | str = Default(-1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Set permissions for the output video frame.

        Parameters:
        ----------

        :param int mode: Select the permissions mode. It accepts the following values: ‘none’ Do nothing. This is the default. ‘ro’ Set all the output frames read-only. ‘rw’ Set all the output frames directly writable. ‘toggle’ Make the frame read-only if writable, and writable if read-only. ‘random’ Set each output frame read-only or writable randomly.
        :param int seed: Set the seed for the random mode, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to -1, the filter will try to use a good random seed on a best effort basis.
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
        x0: str | float | int = Default("0"),
        y0: str | float | int = Default("0"),
        x1: str | float | int = Default("W"),
        y1: str | float | int = Default("0"),
        x2: str | float | int = Default("0"),
        y2: str | float | int = Default("H"),
        x3: str | float | int = Default("W"),
        y3: str | float | int = Default("H"),
        interpolation: int | Literal["linear", "cubic"] | Default = Default(0),
        sense: int | Literal["source", "destination"] | Default = Default("PERSPECTIVE_SENSE_SOURCE"),
        eval: int | str = Default("EVAL_MODE_INIT"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Correct the perspective of video.

        Parameters:
        ----------

        :param str x0: set top left x coordinate
        :param str y0: set top left y coordinate
        :param str x1: set top right x coordinate
        :param str y1: set top right y coordinate
        :param str x2: set bottom left x coordinate
        :param str y2: set bottom left y coordinate
        :param str x3: set bottom right x coordinate
        :param str y3: set bottom right y coordinate
        :param int interpolation: set interpolation
        :param int sense: specify the sense of the coordinates
        :param int eval: specify when to evaluate expressions
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
        mode: int | Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"] | Default = Default("AUTO_ANALYZE"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Phase shift fields.

        Parameters:
        ----------

        :param int mode: set phase mode
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
        frames: int | str = Default(30),
        threshold: float | int | str = Default(1.0),
        skip: int | str = Default(1),
        bypass: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Filter out photosensitive epilepsy seizure-inducing flashes.

        Parameters:
        ----------

        :param int frames: Set how many frames to use when filtering. Default is 30.
        :param float threshold: Set detection threshold factor. Default is 1. Lower is stricter.
        :param int skip: Set how many pixels to skip when sampling frames. Default is 1. Allowed range is from 1 to 1024.
        :param bool bypass: Leave frames unchanged. Default is disabled.

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
        width: int | str = Default(16),
        height: int | str = Default(16),
        mode: int | Literal["avg", "min", "max"] | Default = Default(0),
        planes: str | float | int = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixelize video.

        Parameters:
        ----------

        :param int width: Set block dimensions that will be used for pixelization. Default value is 16.
        :param int height: Set block dimensions that will be used for pixelization. Default value is 16.
        :param int mode: Set the mode of pixelization used. Possible values are: ‘avg’ ‘min’ ‘max’ Default value is avg.
        :param str planes: Set what planes to filter. Default is to filter all planes.
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
        x: float | int | str = Default(0.5),
        y: float | int | str = Default(0.5),
        w: int | str = Default(7),
        h: int | str = Default(7),
        o: float | int | str = Default(0.5),
        wx: float | int | str = Default(-1.0),
        wy: float | int | str = Default(-1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pixel data analysis.

        Parameters:
        ----------

        :param float x: Set scope X position, relative offset on X axis.
        :param float y: Set scope Y position, relative offset on Y axis.
        :param int w: Set scope width.
        :param int h: Set scope height.
        :param float o: Set window opacity. This window also holds statistics about pixel area.
        :param float wx: Set window X position, relative offset on X axis.
        :param float wy: Set window Y position, relative offset on Y axis.
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

    def pp(
        self, *, subfilters: str | float | int = Default("de"), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Filter video using libpostproc.

        Parameters:
        ----------

        :param str subfilters: Set postprocessing subfilters string.
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
        qp: int | str = Default(0),
        mode: int | Literal["hard", "soft", "medium"] | Default = Default("MODE_MEDIUM"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Postprocessing 7 filter.

        Parameters:
        ----------

        :param int qp: Force a constant quantization parameter. It accepts an integer in range 0 to 63. If not set, the filter will use the QP from the video stream (if available).
        :param int mode: Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding. ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier). ‘medium’ Set medium thresholding (good results, default).
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
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply prewitt operator.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.
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

    def prewitt_opencl(
        self,
        *,
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.11 prewitt_opencl

        Apply the Prewitt operator (<https://en.wikipedia.org/wiki/Prewitt_operator>)
        to input video stream.

        The filter accepts the following option:

        **planes**

            Set which planes to filter. Default value is 0xf, by which all planes are processed.

        **scale**

            Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.

        **delta**

            Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.



        Parameters:
        ----------

        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.
        :param float scale: Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.
        :param float delta: Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#prewitt_005fopencl

        """
        filter_node = FilterNode(
            name="prewitt_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def pseudocolor(
        self,
        *,
        c0: str | float | int = Default("val"),
        c1: str | float | int = Default("val"),
        c2: str | float | int = Default("val"),
        c3: str | float | int = Default("val"),
        index: int | str = Default(0),
        preset: int
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
        | Default = Default(-1),
        opacity: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make pseudocolored video frames.

        Parameters:
        ----------

        :param str c0: set pixel first component expression
        :param str c1: set pixel second component expression
        :param str c2: set pixel third component expression
        :param str c3: set pixel fourth component expression, corresponds to the alpha component
        :param int index: set component to use as base for altering colors
        :param int preset: Pick one of built-in LUTs. By default is set to none. Available LUTs: ‘magma’ ‘inferno’ ‘plasma’ ‘viridis’ ‘turbo’ ‘cividis’ ‘range1’ ‘range2’ ‘shadows’ ‘highlights’ ‘solar’ ‘nominal’ ‘preferred’ ‘total’ ‘spectral’ ‘cool’ ‘heat’ ‘fiery’ ‘blues’ ‘green’ ‘helix’
        :param float opacity: Set opacity of output colors. Allowed range is from 0 to 1. Default value is set to 1.
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
        stats_file: str | float | int = Default("((void*)0)"),
        stats_version: int | str = Default(1),
        output_max: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the PSNR between two video streams.

        Parameters:
        ----------

        :param str stats_file: If specified the filter will use the named file to save the PSNR of each individual frame. When filename equals "-" the data is sent to standard output.
        :param int stats_version: Specifies which version of the stats file format to use. Details of each format are written below. Default value is 1.
        :param bool output_max: Add raw stats (max values) to the output log.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def pullup(
        self,
        *,
        jl: int | str = Default(1),
        jr: int | str = Default(1),
        jt: int | str = Default(4),
        jb: int | str = Default(4),
        sb: bool | int | str = Default(0),
        mp: int | Literal["y", "u", "v"] | Default = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pullup from field sequence to frames.

        Parameters:
        ----------

        :param int jl: These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        :param int jr: These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        :param int jt: These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        :param int jb: These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        :param bool sb: Set the strict breaks. Setting this option to 1 will reduce the chances of filter generating an occasional mismatched frame, but it may also cause an excessive number of frames to be dropped during high motion sequences. Conversely, setting it to -1 will make filter match fields more easily. This may help processing of video where there is slight blurring between the fields, but may also cause there to be interlaced frames in the output. Default value is 0.
        :param int mp: Set the metric plane to use. It accepts the following values: ‘l’ Use luma plane. ‘u’ Use chroma blue plane. ‘v’ Use chroma red plane. This option may be set to use chroma plane instead of the default luma plane for doing filter’s computations. This may improve accuracy on very clean source material, but more likely will decrease accuracy, especially if there is chroma noise (rainbow effect) or any grayscale video. The main purpose of setting mp to a chroma plane is to reduce CPU load and make pullup usable in realtime on slow machines.

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

    def qp(
        self, *, qp: str | float | int = Default("((void*)0)"), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Change video quantization parameters.

        Parameters:
        ----------

        :param str qp: Set expression for quantization parameter.
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

    def random(self, *, frames: int | str = Default(30), seed: int | str = Default(-1), **kwargs: Any) -> "VideoStream":
        """

        Return random frames.

        Parameters:
        ----------

        :param int frames: Set size in number of frames of internal cache, in range from 2 to 512. Default is 30.
        :param int seed: Set seed for random number generator, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to less than 0, the filter will try to use a good random seed on a best effort basis.

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
        scan_min: int | str = Default(0),
        scan_max: int | str = Default(29),
        spw: float | int | str = Default(0.27),
        chp: bool | int | str = Default(0),
        lp: bool | int | str = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

        Parameters:
        ----------

        :param int scan_min: Set the line to start scanning for EIA-608 data. Default is 0.
        :param int scan_max: Set the line to end scanning for EIA-608 data. Default is 29.
        :param float spw: Set the ratio of width reserved for sync code detection. Default is 0.27. Allowed range is [0.1 - 0.7].
        :param bool chp: Enable checking the parity bit. In the event of a parity error, the filter will output 0x00 for that character. Default is false.
        :param bool lp: Lowpass lines prior to further processing. Default is enabled.
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
        scan_max: int | str = Default(45),
        thr_b: float | int | str = Default(0.2),
        thr_w: float | int | str = Default(0.6),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Read vertical interval timecode and write it to frame metadata.

        Parameters:
        ----------

        :param int scan_max: Set the maximum number of lines to scan for VITC data. If the value is set to -1 the full video frame is scanned. Default is 45.
        :param float thr_b: Set the luma threshold for black. Accepts float numbers in the range [0.0,1.0], default value is 0.2. The value must be equal or less than thr_w.
        :param float thr_w: Set the luma threshold for white. Accepts float numbers in the range [0.0,1.0], default value is 0.6. The value must be equal or greater than thr_b.

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

    def realtime(
        self, *, limit: int | str = Default(2000000), speed: float | int | str = Default(1.0), **kwargs: Any
    ) -> "VideoStream":
        """

        Slow down filtering to match realtime.

        Parameters:
        ----------

        :param int limit: Time limit for the pauses. Any pause longer than that will be considered a timestamp discontinuity and reset the timer. Default is 2 seconds.
        :param float speed: Speed factor for processing. The value must be a float larger than zero. Values larger than 1.0 will result in faster than realtime processing, smaller will slow processing down. The limit is automatically adapted accordingly. Default is 1.0. A processing speed faster than what is possible without these filters cannot be achieved.

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
        format: int | str = Default(0),
        fill: str | float | int = Default("black"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remap pixels.

        Parameters:
        ----------

        :param int format: Specify pixel format of output from this filter. Can be color or gray. Default is color.
        :param str fill: Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.

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

    def remap_opencl(
        self,
        _xmap: "VideoStream",
        _ymap: "VideoStream",
        *,
        interp: int | Literal["near", "linear"] | Default = Default(1),
        fill: str | float | int = Default("black"),
        **kwargs: Any,
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
                self,
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

    def removegrain(
        self,
        *,
        m0: int | str = Default(0),
        m1: int | str = Default(0),
        m2: int | str = Default(0),
        m3: int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove grain.

        Parameters:
        ----------

        :param int m0: Set mode for the first plane.
        :param int m1: Set mode for the second plane.
        :param int m2: Set mode for the third plane.
        :param int m3: Set mode for the fourth plane.
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
        self,
        *,
        filename: str | float | int = Default("((void*)0)"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Remove a TV logo based on a mask image.

        Parameters:
        ----------

        :param str filename: Set the filter bitmap file, which can be any image format supported by libavformat. The width and height of the image file must match those of the video stream being processed.
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
        rh: int | str = Default(0),
        rv: int | str = Default(0),
        gh: int | str = Default(0),
        gv: int | str = Default(0),
        bh: int | str = Default(0),
        bv: int | str = Default(0),
        ah: int | str = Default(0),
        av: int | str = Default(0),
        edge: int | Literal["smear", "wrap"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shift RGBA.

        Parameters:
        ----------

        :param int rh: Set amount to shift red horizontally.
        :param int rv: Set amount to shift red vertically.
        :param int gh: Set amount to shift green horizontally.
        :param int gv: Set amount to shift green vertically.
        :param int bh: Set amount to shift blue horizontally.
        :param int bv: Set amount to shift blue vertically.
        :param int ah: Set amount to shift alpha horizontally.
        :param int av: Set amount to shift alpha vertically.
        :param int edge: Set edge mode, can be smear, default, or warp.
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
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply roberts cross operator.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.
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

    def roberts_opencl(
        self,
        *,
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.14 roberts_opencl

        Apply the Roberts cross operator
        (<https://en.wikipedia.org/wiki/Roberts_cross>) to input video stream.

        The filter accepts the following option:

        **planes**

            Set which planes to filter. Default value is 0xf, by which all planes are processed.

        **scale**

            Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.

        **delta**

            Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.



        Parameters:
        ----------

        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.
        :param float scale: Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.
        :param float delta: Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#roberts_005fopencl

        """
        filter_node = FilterNode(
            name="roberts_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def rotate(
        self,
        *,
        angle: str | float | int = Default("0"),
        out_w: str | float | int = Default("iw"),
        out_h: str | float | int = Default("ih"),
        fillcolor: str | float | int = Default("black"),
        bilinear: bool | int | str = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Rotate the input image.

        Parameters:
        ----------

        :param str angle: Set an expression for the angle by which to rotate the input video clockwise, expressed as a number of radians. A negative value will result in a counter-clockwise rotation. By default it is set to "0". This expression is evaluated for each frame.
        :param str out_w: Set the output width expression, default value is "iw". This expression is evaluated just once during configuration.
        :param str out_h: Set the output height expression, default value is "ih". This expression is evaluated just once during configuration.
        :param str fillcolor: Set the color used to fill the output area not covered by the rotated image. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".
        :param bool bilinear: Enable bilinear interpolation if set to 1, a value of 0 disables it. Default value is 1.
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
        luma_radius: float | int | str = Default(1.0),
        luma_pre_filter_radius: float | int | str = Default(1.0),
        luma_strength: float | int | str = Default(1.0),
        chroma_radius: float | int | str = Default("0.1 -1"),
        chroma_pre_filter_radius: float | int | str = Default("0.1 -1"),
        chroma_strength: float | int | str = Default("0.1 -1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply shape adaptive blur.

        Parameters:
        ----------

        :param float luma_radius: Set luma blur filter strength, must be a value in range 0.1-4.0, default value is 1.0. A greater value will result in a more blurred image, and in slower processing.
        :param float luma_pre_filter_radius: Set luma pre-filter radius, must be a value in the 0.1-2.0 range, default value is 1.0.
        :param float luma_strength: Set luma maximum difference between pixels to still be considered, must be a value in the 0.1-100.0 range, default value is 1.0.
        :param float chroma_radius: Set chroma blur filter strength, must be a value in range -0.9-4.0. A greater value will result in a more blurred image, and in slower processing.
        :param float chroma_pre_filter_radius: Set chroma pre-filter radius, must be a value in the -0.9-2.0 range.
        :param float chroma_strength: Set chroma maximum difference between pixels to still be considered, must be a value in the -0.9-100.0 range.
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
        w: str | float | int = Default(None),
        h: str | float | int = Default(None),
        flags: str | float | int = Default(""),
        interl: bool | int | str = Default(0),
        size: str | float | int = Default("((void*)0)"),
        in_color_matrix: int
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default(-1),
        out_color_matrix: int
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default("AVCOL_SPC_UNSPECIFIED"),
        in_range: int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        out_range: int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        in_v_chr_pos: int | str = Default(-513),
        in_h_chr_pos: int | str = Default(-513),
        out_v_chr_pos: int | str = Default(-513),
        out_h_chr_pos: int | str = Default(-513),
        force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
        force_divisible_by: int | str = Default(1),
        param0: float | int | str = Default(1.7976931348623157e308),
        param1: float | int | str = Default(1.7976931348623157e308),
        eval: int | str = Default("EVAL_MODE_INIT"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scale the input video size and/or convert the image format.

        Parameters:
        ----------

        :param str w: Output video width
        :param str h: Output video height
        :param str flags: Flags to pass to libswscale
        :param bool interl: set interlacing
        :param str size: set video size
        :param int in_color_matrix: set input YCbCr type
        :param int out_color_matrix: set output YCbCr type
        :param int in_range: set input color range
        :param int out_range: set output color range
        :param int in_v_chr_pos: input vertical chroma position in luma grid/256
        :param int in_h_chr_pos: input horizontal chroma position in luma grid/256
        :param int out_v_chr_pos: output vertical chroma position in luma grid/256
        :param int out_h_chr_pos: output horizontal chroma position in luma grid/256
        :param int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR
        :param int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used
        :param float param0: Scaler param 0
        :param float param1: Scaler param 1
        :param int eval: specify when to evaluate expressions

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
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scale2ref(
        self,
        _ref: "VideoStream",
        *,
        w: str | float | int = Default(None),
        h: str | float | int = Default(None),
        flags: str | float | int = Default(""),
        interl: bool | int | str = Default(0),
        size: str | float | int = Default("((void*)0)"),
        in_color_matrix: int
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default(-1),
        out_color_matrix: int
        | Literal["auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"]
        | Default = Default("AVCOL_SPC_UNSPECIFIED"),
        in_range: int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        out_range: int
        | Literal["auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"]
        | Default = Default("AVCOL_RANGE_UNSPECIFIED"),
        in_v_chr_pos: int | str = Default(-513),
        in_h_chr_pos: int | str = Default(-513),
        out_v_chr_pos: int | str = Default(-513),
        out_h_chr_pos: int | str = Default(-513),
        force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
        force_divisible_by: int | str = Default(1),
        param0: float | int | str = Default(1.7976931348623157e308),
        param1: float | int | str = Default(1.7976931348623157e308),
        eval: int | str = Default("EVAL_MODE_INIT"),
        **kwargs: Any,
    ) -> tuple["VideoStream", "VideoStream",]:
        """

        Scale the input video size and/or convert the image format to the given reference.

        Parameters:
        ----------

        :param str w: Output video width
        :param str h: Output video height
        :param str flags: Flags to pass to libswscale
        :param bool interl: set interlacing
        :param str size: set video size
        :param int in_color_matrix: set input YCbCr type
        :param int out_color_matrix: set output YCbCr type
        :param int in_range: set input color range
        :param int out_range: set output color range
        :param int in_v_chr_pos: input vertical chroma position in luma grid/256
        :param int in_h_chr_pos: input horizontal chroma position in luma grid/256
        :param int out_v_chr_pos: output vertical chroma position in luma grid/256
        :param int out_h_chr_pos: output horizontal chroma position in luma grid/256
        :param int force_original_aspect_ratio: decrease or increase w/h if necessary to keep the original AR
        :param int force_divisible_by: enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used
        :param float param0: Scaler param 0
        :param float param1: Scaler param 1
        :param int eval: specify when to evaluate expressions

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
                    | kwargs
                ).items()
            ),
        )
        return (
            filter_node.video(0),
            filter_node.video(1),
        )

    def scale2ref_npp(
        self,
        _ref: "VideoStream",
        *,
        w: str | float | int = Default(None),
        h: str | float | int = Default(None),
        format: str | float | int = Default("same"),
        s: str | float | int = Default("((void*)0)"),
        interp_algo: int
        | Literal[
            "nn", "linear", "cubic", "cubic2p_bspline", "cubic2p_catmullrom", "cubic2p_b05c03", "super", "lanczos"
        ]
        | Default = Default("NPPI_INTER_CUBIC"),
        force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
        force_divisible_by: int | str = Default(1),
        eval: int | Literal["init", "frame"] | Default = Default("EVAL_MODE_INIT"),
        **kwargs: Any,
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
                self,
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

    def scale_cuda(
        self,
        *,
        w: str | float | int = Default("iw"),
        h: str | float | int = Default("ih"),
        interp_algo: int
        | Literal["nearest", "bilinear", "bicubic", "lanczos"]
        | Default = Default("INTERP_ALGO_DEFAULT"),
        format: str | float | int = Default("AV_PIX_FMT_NONE"),
        passthrough: bool | int | str = Default(1),
        param: float | int | str = Default("999999.0f"),
        force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
        force_divisible_by: int | str = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.216 scale_cuda

        Scale (resize) and convert (pixel format) the input video, using accelerated
        CUDA kernels. Setting the output width and height works in the same way as for
        the scale filter.

        The filter accepts the following options:

        **w**

        **h**

            Set the output video dimension expression. Default value is the input dimension. Allows for the same expressions as the scale filter.

        **interp_algo**

            Sets the algorithm used for scaling: nearest Nearest neighbour Used by default if input parameters match the desired output. bilinear Bilinear bicubic Bicubic This is the default. lanczos Lanczos

        **format**

            Controls the output pixel format. By default, or if none is specified, the input pixel format is used. The filter does not support converting between YUV and RGB pixel formats.

        **passthrough**

            If set to 0, every frame is processed, even if no conversion is necessary. This mode can be useful to use the filter as a buffer for a downstream frame-consumer that exhausts the limited decoder frame pool. If set to 1, frames are passed through as-is if they match the desired output parameters. This is the default behaviour.

        **param**

            Algorithm-Specific parameter. Affects the curves of the bicubic algorithm.

        **force_original_aspect_ratio**

        **force_divisible_by**

            Work the same as the identical scale filter options.



        Parameters:
        ----------

        :param str w: Set the output video dimension expression. Default value is the input dimension. Allows for the same expressions as the scale filter.
        :param str h: Set the output video dimension expression. Default value is the input dimension. Allows for the same expressions as the scale filter.
        :param int interp_algo: Sets the algorithm used for scaling: nearest Nearest neighbour Used by default if input parameters match the desired output. bilinear Bilinear bicubic Bicubic This is the default. lanczos Lanczos
        :param str format: Controls the output pixel format. By default, or if none is specified, the input pixel format is used. The filter does not support converting between YUV and RGB pixel formats.
        :param bool passthrough: If set to 0, every frame is processed, even if no conversion is necessary. This mode can be useful to use the filter as a buffer for a downstream frame-consumer that exhausts the limited decoder frame pool. If set to 1, frames are passed through as-is if they match the desired output parameters. This is the default behaviour.
        :param float param: Algorithm-Specific parameter. Affects the curves of the bicubic algorithm.
        :param int force_original_aspect_ratio: Work the same as the identical scale filter options.
        :param int force_divisible_by: Work the same as the identical scale filter options.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fcuda

        """
        filter_node = FilterNode(
            name="scale_cuda",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "w": w,
                        "h": h,
                        "interp_algo": interp_algo,
                        "format": format,
                        "passthrough": passthrough,
                        "param": param,
                        "force_original_aspect_ratio": force_original_aspect_ratio,
                        "force_divisible_by": force_divisible_by,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scale_npp(
        self,
        *,
        w: str | float | int = Default(None),
        h: str | float | int = Default(None),
        format: str | float | int = Default("same"),
        s: str | float | int = Default("((void*)0)"),
        interp_algo: int
        | Literal[
            "nn", "linear", "cubic", "cubic2p_bspline", "cubic2p_catmullrom", "cubic2p_b05c03", "super", "lanczos"
        ]
        | Default = Default("NPPI_INTER_CUBIC"),
        force_original_aspect_ratio: int | Literal["disable", "decrease", "increase"] | Default = Default(0),
        force_divisible_by: int | str = Default(1),
        eval: int | Literal["init", "frame"] | Default = Default("EVAL_MODE_INIT"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.217 scale_npp

        Use the NVIDIA Performance Primitives (libnpp) to perform scaling and/or pixel
        format conversion on CUDA video frames. Setting the output width and height
        works in the same way as for the scale filter.

        The following additional options are accepted:

        **format**

            The pixel format of the output CUDA frames. If set to the string "same" (the default), the input format will be kept. Note that automatic format negotiation and conversion is not yet supported for hardware frames

        **interp_algo**

            The interpolation algorithm used for resizing. One of the following: nn Nearest neighbour. linear cubic cubic2p_bspline 2-parameter cubic (B=1, C=0) cubic2p_catmullrom 2-parameter cubic (B=0, C=1/2) cubic2p_b05c03 2-parameter cubic (B=1/2, C=3/10) super Supersampling lanczos

        **force_original_aspect_ratio**

            Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio. Possible values: ‘disable’ Scale the video as specified and disable this feature. ‘decrease’ The output video dimensions will automatically be decreased if needed. ‘increase’ The output video dimensions will automatically be increased if needed. One useful instance of this option is that when you know a specific device’s maximum allowed resolution, you can use this to limit the output video to that, while retaining the aspect ratio. For example, device A allows 1280x720 playback, and your video is 1920x800. Using this option (set it to decrease) and specifying 1280x720 to the command line makes the output 1280x533. Please note that this is a different thing than specifying -1 for w or h, you still need to specify the output resolution for this option to work.

        **force_divisible_by**

            Ensures that both the output dimensions, width and height, are divisible by the given integer when used together with force_original_aspect_ratio. This works similar to using -n in the w and h options. This option respects the value set for force_original_aspect_ratio, increasing or decreasing the resolution accordingly. The video’s aspect ratio may be slightly modified. This option can be handy if you need to have a video fit within or exceed a defined resolution using force_original_aspect_ratio but also have encoder restrictions on width or height divisibility.

        **eval**

            Specify when to evaluate width and height expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame.

        The values of the w and h options are expressions containing the following
        constants:

        **in_w**

        **in_h**

            The input width and height

        **iw**

        **ih**

            These are the same as in_w and in_h.

        **out_w**

        **out_h**

            The output (scaled) width and height

        **ow**

        **oh**

            These are the same as out_w and out_h

        **a**

            The same as iw / ih

        **sar**

            input sample aspect ratio

        **dar**

            The input display aspect ratio. Calculated from (iw / ih) * sar.

        **n**

            The (sequential) number of the input frame, starting from 0. Only available with eval=frame.

        **t**

            The presentation timestamp of the input frame, expressed as a number of seconds. Only available with eval=frame.

        **pos**

            The position (byte offset) of the frame in the input stream, or NaN if this information is unavailable and/or meaningless (for example in case of synthetic video). Only available with eval=frame. Deprecated, do not use.



        Parameters:
        ----------

        :param str w: Output video width
        :param str h: Output video height
        :param str format: The pixel format of the output CUDA frames. If set to the string "same" (the default), the input format will be kept. Note that automatic format negotiation and conversion is not yet supported for hardware frames
        :param str s: Output video size
        :param int interp_algo: The interpolation algorithm used for resizing. One of the following: nn Nearest neighbour. linear cubic cubic2p_bspline 2-parameter cubic (B=1, C=0) cubic2p_catmullrom 2-parameter cubic (B=0, C=1/2) cubic2p_b05c03 2-parameter cubic (B=1/2, C=3/10) super Supersampling lanczos
        :param int force_original_aspect_ratio: Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio. Possible values: ‘disable’ Scale the video as specified and disable this feature. ‘decrease’ The output video dimensions will automatically be decreased if needed. ‘increase’ The output video dimensions will automatically be increased if needed. One useful instance of this option is that when you know a specific device’s maximum allowed resolution, you can use this to limit the output video to that, while retaining the aspect ratio. For example, device A allows 1280x720 playback, and your video is 1920x800. Using this option (set it to decrease) and specifying 1280x720 to the command line makes the output 1280x533. Please note that this is a different thing than specifying -1 for w or h, you still need to specify the output resolution for this option to work.
        :param int force_divisible_by: Ensures that both the output dimensions, width and height, are divisible by the given integer when used together with force_original_aspect_ratio. This works similar to using -n in the w and h options. This option respects the value set for force_original_aspect_ratio, increasing or decreasing the resolution accordingly. The video’s aspect ratio may be slightly modified. This option can be handy if you need to have a video fit within or exceed a defined resolution using force_original_aspect_ratio but also have encoder restrictions on width or height divisibility.
        :param int eval: Specify when to evaluate width and height expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fnpp

        """
        filter_node = FilterNode(
            name="scale_npp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
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
        return filter_node.video(0)

    def scale_vt(
        self,
        *,
        w: str | float | int = Default("iw"),
        h: str | float | int = Default("ih"),
        color_matrix: str | float | int = Default("((void*)0)"),
        color_primaries: str | float | int = Default("((void*)0)"),
        color_transfer: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.220 scale_vt

        Scale and convert the color parameters using VTPixelTransferSession.

        The filter accepts the following options:

        **w**

        **h**

            Set the output video dimension expression. Default value is the input dimension.

        **color_matrix**

            Set the output colorspace matrix.

        **color_primaries**

            Set the output color primaries.

        **color_transfer**

            Set the output transfer characteristics.



        Parameters:
        ----------

        :param str w: Set the output video dimension expression. Default value is the input dimension.
        :param str h: Set the output video dimension expression. Default value is the input dimension.
        :param str color_matrix: Set the output colorspace matrix.
        :param str color_primaries: Set the output color primaries.
        :param str color_transfer: Set the output transfer characteristics.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fvt

        """
        filter_node = FilterNode(
            name="scale_vt",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "w": w,
                        "h": h,
                        "color_matrix": color_matrix,
                        "color_primaries": color_primaries,
                        "color_transfer": color_transfer,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def scdet(
        self, *, threshold: float | int | str = Default(10.0), sc_pass: bool | int | str = Default(0.0), **kwargs: Any
    ) -> "VideoStream":
        """

        Detect video scene change

        Parameters:
        ----------

        :param float threshold: Set the scene change detection threshold as a percentage of maximum change. Good values are in the [8.0, 14.0] range. The range for threshold is [0., 100.]. Default value is 10..
        :param bool sc_pass: Set the flag to pass scene change frames to the next filter. Default value is 0 You can enable it if you want to get snapshot of scene change frames only.

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
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply scharr operator.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.
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
        horizontal: float | int | str = Default(0.0),
        vertical: float | int | str = Default(0.0),
        hpos: float | int | str = Default(0.0),
        vpos: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Scroll input video.

        Parameters:
        ----------

        :param float horizontal: Set the horizontal scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        :param float vertical: Set the vertical scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        :param float hpos: Set the initial horizontal scrolling position. Default is 0. Allowed range is from 0 to 1.
        :param float vpos: Set the initial vertical scrolling position. Default is 0. Allowed range is from 0 to 1.
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
        self,
        *,
        timestamps: str | float | int = Default("((void*)0)"),
        frames: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        Segment video stream.

        Parameters:
        ----------

        :param str timestamps: Timestamps of output segments separated by ’|’. The first segment will run from the beginning of the input stream. The last segment will run until the end of the input stream
        :param str frames: Exact frame/sample count to split the segments.

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

    def select(
        self, *, expr: str | float | int = Default("1"), outputs: int | str = Default(1), **kwargs: Any
    ) -> FilterNode:
        """

        Select video frames to pass in output.

        Parameters:
        ----------

        :param str expr: Set expression, which is evaluated for each input frame. If the expression is evaluated to zero, the frame is discarded. If the evaluation result is negative or NaN, the frame is sent to the first output; otherwise it is sent to the output with index ceil(val)-1, assuming that the input index starts from 0. For example a value of 1.2 corresponds to the output with index ceil(1.2)-1 = 2-1 = 1, that is the second output.
        :param int outputs: Set the number of outputs. The output to which to send the selected frame is based on the result of the evaluation. Default value is 1.

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
        correction_method: int | Literal["absolute", "relative"] | Default = Default("CORRECTION_METHOD_ABSOLUTE"),
        reds: str | float | int = Default("((void*)0)"),
        yellows: str | float | int = Default("((void*)0)"),
        greens: str | float | int = Default("((void*)0)"),
        cyans: str | float | int = Default("((void*)0)"),
        blues: str | float | int = Default("((void*)0)"),
        magentas: str | float | int = Default("((void*)0)"),
        whites: str | float | int = Default("((void*)0)"),
        neutrals: str | float | int = Default("((void*)0)"),
        blacks: str | float | int = Default("((void*)0)"),
        psfile: str | float | int = Default("((void*)0)"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply CMYK adjustments to specific color ranges.

        Parameters:
        ----------

        :param int correction_method: Select color correction method. Available values are: ‘absolute’ Specified adjustments are applied "as-is" (added/subtracted to original pixel component value). ‘relative’ Specified adjustments are relative to the original component value. Default is absolute.
        :param str reds: Adjustments for red pixels (pixels where the red component is the maximum)
        :param str yellows: Adjustments for yellow pixels (pixels where the blue component is the minimum)
        :param str greens: Adjustments for green pixels (pixels where the green component is the maximum)
        :param str cyans: Adjustments for cyan pixels (pixels where the red component is the minimum)
        :param str blues: Adjustments for blue pixels (pixels where the blue component is the maximum)
        :param str magentas: Adjustments for magenta pixels (pixels where the green component is the minimum)
        :param str whites: Adjustments for white pixels (pixels where all components are greater than 128)
        :param str neutrals: Adjustments for all pixels except pure black and pure white
        :param str blacks: Adjustments for black pixels (pixels where all components are lesser than 128)
        :param str psfile: Specify a Photoshop selective color file (.asv) to import the settings from.
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
        self,
        *,
        commands: str | float | int = Default("((void*)0)"),
        filename: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Send commands to filters.

        Parameters:
        ----------

        :param str commands: Set the commands to be read and sent to the other filters.
        :param str filename: Set the filename of the commands to be read and sent to the other filters.

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

    def setdar(
        self, *, dar: str | float | int = Default("0"), max: int | str = Default(100), **kwargs: Any
    ) -> "VideoStream":
        """

        Set the frame display aspect ratio.

        Parameters:
        ----------

        :param str dar: Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        :param int max: Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.

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
        self, *, mode: int | Literal["auto", "bff", "tff", "prog"] | Default = Default("MODE_AUTO"), **kwargs: Any
    ) -> "VideoStream":
        """

        Force field for the output video frame.

        Parameters:
        ----------

        :param int mode: Available values are: ‘auto’ Keep the same field property. ‘bff’ Mark the frame as bottom-field-first. ‘tff’ Mark the frame as top-field-first. ‘prog’ Mark the frame as progressive.

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
        field_mode: int | Literal["auto", "bff", "tff", "prog"] | Default = Default("MODE_AUTO"),
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
        | Default = Default(-1),
        colorspace: int
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
        | Default = Default(-1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force field, or color property for the output video frame.

        Parameters:
        ----------

        :param int field_mode: Available values are: ‘auto’ Keep the same field property (default). ‘bff’ Mark the frame as bottom-field-first. ‘tff’ Mark the frame as top-field-first. ‘prog’ Mark the frame as progressive.
        :param int range: Available values are: ‘auto’ Keep the same color range property (default). ‘unspecified, unknown’ Mark the frame as unspecified color range. ‘limited, tv, mpeg’ Mark the frame as limited range. ‘full, pc, jpeg’ Mark the frame as full range.
        :param int color_primaries: Set the color primaries. Available values are: ‘auto’ Keep the same color primaries property (default). ‘bt709’ ‘unknown’ ‘bt470m’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘film’ ‘bt2020’ ‘smpte428’ ‘smpte431’ ‘smpte432’ ‘jedec-p22’
        :param int color_trc: Set the color transfer. Available values are: ‘auto’ Keep the same color trc property (default). ‘bt709’ ‘unknown’ ‘bt470m’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘linear’ ‘log100’ ‘log316’ ‘iec61966-2-4’ ‘bt1361e’ ‘iec61966-2-1’ ‘bt2020-10’ ‘bt2020-12’ ‘smpte2084’ ‘smpte428’ ‘arib-std-b67’
        :param int colorspace: Set the colorspace. Available values are: ‘auto’ Keep the same colorspace property (default). ‘gbr’ ‘bt709’ ‘unknown’ ‘fcc’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘ycgco’ ‘bt2020nc’ ‘bt2020c’ ‘smpte2085’ ‘chroma-derived-nc’ ‘chroma-derived-c’ ‘ictcp’

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

    def setpts(self, *, expr: str | float | int = Default("PTS"), **kwargs: Any) -> "VideoStream":
        """

        Set PTS for the output video frame.

        Parameters:
        ----------

        :param str expr: The expression which is evaluated for each frame to construct its timestamp.

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
        range: int
        | Literal["auto", "unspecified", "unknown", "limited", "tv", "mpeg", "full", "pc", "jpeg"]
        | Default = Default(-1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Force color range for the output video frame.

        Parameters:
        ----------

        :param int range: Available values are: ‘auto’ Keep the same color range property. ‘unspecified, unknown’ Set the color range as unspecified. ‘limited, tv, mpeg’ Set the color range as limited. ‘full, pc, jpeg’ Set the color range as full.

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

    def setsar(
        self, *, sar: str | float | int = Default("0"), max: int | str = Default(100), **kwargs: Any
    ) -> "VideoStream":
        """

        Set the pixel sample aspect ratio.

        Parameters:
        ----------

        :param str sar: Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        :param int max: Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.

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

    def settb(self, *, expr: str | float | int = Default("intb"), **kwargs: Any) -> "VideoStream":
        """

        Set timebase for the video output link.

        Parameters:
        ----------

        :param str expr: The expression which is evaluated into the output timebase.

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

    def sharpen_npp(
        self, *, border_type: int | Literal["replicate"] | Default = Default("NPP_BORDER_REPLICATE"), **kwargs: Any
    ) -> "VideoStream":
        """

        ### 11.229 sharpen_npp

        Use the NVIDIA Performance Primitives (libnpp) to perform image sharpening
        with border control.

        The following additional options are accepted:

        **border_type**

            Type of sampling to be used ad frame borders. One of the following: replicate Replicate pixel values.



        Parameters:
        ----------

        :param int border_type: Type of sampling to be used ad frame borders. One of the following: replicate Replicate pixel values.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sharpen_005fnpp

        """
        filter_node = FilterNode(
            name="sharpen_npp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "border_type": border_type,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def shear(
        self,
        *,
        shx: float | int | str = Default(0.0),
        shy: float | int | str = Default(0.0),
        fillcolor: str | float | int = Default("black"),
        interp: int | Literal["nearest", "bilinear"] | Default = Default(1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shear transform the input image.

        Parameters:
        ----------

        :param float shx: Shear factor in X-direction. Default value is 0. Allowed range is from -2 to 2.
        :param float shy: Shear factor in Y-direction. Default value is 0. Allowed range is from -2 to 2.
        :param str fillcolor: Set the color used to fill the output area not covered by the transformed video. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".
        :param int interp: Set interpolation type. Can be bilinear or nearest. Default is bilinear.
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

    def showinfo(self, *, checksum: bool | int | str = Default(1), **kwargs: Any) -> "VideoStream":
        """

        Show textual information for each video frame.

        Parameters:
        ----------

        :param bool checksum: Calculate checksums of each plane. By default enabled.

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

    def showpalette(self, *, s: int | str = Default(30), **kwargs: Any) -> "VideoStream":
        """

        Display frame palette.

        Parameters:
        ----------

        :param int s: Set the size of the box used to represent one palette color entry. Default is 30 (for a 30x30 pixel box).

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
        self, *, mapping: str | float | int = Default("0"), enable: str | float | int = Default(None), **kwargs: Any
    ) -> "VideoStream":
        """

        Shuffle video frames.

        Parameters:
        ----------

        :param str mapping: Set the destination indexes of input frames. This is space or ’|’ separated list of indexes that maps input frames to output frames. Number of indexes also sets maximal value that each index may have. ’-1’ index have special meaning and that is to drop frame.
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
        direction: int | Literal["forward", "inverse"] | Default = Default(0),
        mode: int | Literal["horizontal", "vertical", "block"] | Default = Default(0),
        width: int | str = Default(10),
        height: int | str = Default(10),
        seed: int | str = Default(-1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video pixels.

        Parameters:
        ----------

        :param int direction: Set shuffle direction. Can be forward or inverse direction. Default direction is forward.
        :param int mode: Set shuffle mode. Can be horizontal, vertical or block mode.
        :param int width: Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        :param int height: Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        :param int seed: Set random seed used with shuffling pixels. Mainly useful to set to be able to reverse filtering process to get original input. For example, to reverse forward shuffle you need to use same parameters and exact same seed and to set direction to inverse.
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
        map0: int | str = Default(0),
        map1: int | str = Default(1),
        map2: int | str = Default(2),
        map3: int | str = Default(3),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Shuffle video planes.

        Parameters:
        ----------

        :param int map0: The index of the input plane to be used as the first output plane.
        :param int map1: The index of the input plane to be used as the second output plane.
        :param int map2: The index of the input plane to be used as the third output plane.
        :param int map3: The index of the input plane to be used as the fourth output plane.
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
        mode: int | Literal["select", "delete"] | Default = Default(0),
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
        | Default = Default(-1),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Manipulate video frame side data.

        Parameters:
        ----------

        :param int mode: Set mode of operation of the filter. Can be one of the following: ‘select’ Select every frame with side data of type. ‘delete’ Delete side data of type. If type is not set, delete all side data in the frame.
        :param int type: Set side data type used with all modes. Must be set for select mode. For the list of frame side data types, refer to the AVFrameSideDataType enum in libavutil/frame.h. For example, to choose AV_FRAME_DATA_PANSCAN side data, you must specify PANSCAN.
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
        stat: str | Literal["tout", "vrep", "brng"] | Default = Default(0),
        out: int | Literal["tout", "vrep", "brng"] | Default = Default("FILTER_NONE"),
        c: str | float | int = Default("yellow"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Generate statistics from video analysis.

        Parameters:
        ----------

        :param str stat: stat specify an additional form of image analysis. out output video with the specified type of pixel highlighted. Both options accept the following values: ‘tout’ Identify temporal outliers pixels. A temporal outlier is a pixel unlike the neighboring pixels of the same field. Examples of temporal outliers include the results of video dropouts, head clogs, or tape tracking issues. ‘vrep’ Identify vertical line repetition. Vertical line repetition includes similar rows of pixels within a frame. In born-digital video vertical line repetition is common, but this pattern is uncommon in video digitized from an analog source. When it occurs in video that results from the digitization of an analog source it can indicate concealment from a dropout compensator. ‘brng’ Identify pixels that fall outside of legal broadcast range.
        :param int out: stat specify an additional form of image analysis. out output video with the specified type of pixel highlighted. Both options accept the following values: ‘tout’ Identify temporal outliers pixels. A temporal outlier is a pixel unlike the neighboring pixels of the same field. Examples of temporal outliers include the results of video dropouts, head clogs, or tape tracking issues. ‘vrep’ Identify vertical line repetition. Vertical line repetition includes similar rows of pixels within a frame. In born-digital video vertical line repetition is common, but this pattern is uncommon in video digitized from an analog source. When it occurs in video that results from the digitization of an analog source it can indicate concealment from a dropout compensator. ‘brng’ Identify pixels that fall outside of legal broadcast range.
        :param str c: Set the highlight color for the out option. The default color is yellow.

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

    def siti(self, *, print_summary: bool | int | str = Default(0), **kwargs: Any) -> "VideoStream":
        """

        Calculate spatial information (SI) and temporal information (TI).

        Parameters:
        ----------

        :param bool print_summary: If set to 1, Summary statistics will be printed to the console. Default 0.

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
        luma_radius: float | int | str = Default(1.0),
        luma_strength: float | int | str = Default(1.0),
        luma_threshold: int | str = Default(0),
        chroma_radius: float | int | str = Default("0.1 -1"),
        chroma_strength: float | int | str = Default("-1.0 -1"),
        chroma_threshold: int | str = Default("-30 -1"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blur the input video without impacting the outlines.

        Parameters:
        ----------

        :param float luma_radius: Set the luma radius. The option value must be a float number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is 1.0.
        :param float luma_strength: Set the luma strength. The option value must be a float number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is 1.0.
        :param int luma_threshold: Set the luma threshold used as a coefficient to determine whether a pixel should be blurred or not. The option value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is 0.
        :param float chroma_radius: Set the chroma radius. The option value must be a float number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is luma_radius.
        :param float chroma_strength: Set the chroma strength. The option value must be a float number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is luma_strength.
        :param int chroma_threshold: Set the chroma threshold used as a coefficient to determine whether a pixel should be blurred or not. The option value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is luma_threshold.
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
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply sobel operator.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.
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

    def sobel_opencl(
        self,
        *,
        planes: int | str = Default(15),
        scale: float | int | str = Default(1.0),
        delta: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.15 sobel_opencl

        Apply the Sobel operator (<https://en.wikipedia.org/wiki/Sobel_operator>) to
        input video stream.

        The filter accepts the following option:

        **planes**

            Set which planes to filter. Default value is 0xf, by which all planes are processed.

        **scale**

            Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.

        **delta**

            Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.



        Parameters:
        ----------

        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.
        :param float scale: Set value which will be multiplied with filtered result. Range is [0.0, 65535] and default value is 1.0.
        :param float delta: Set value which will be added to filtered result. Range is [-65535, 65535] and default value is 0.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sobel_005fopencl

        """
        filter_node = FilterNode(
            name="sobel_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "planes": planes,
                        "scale": scale,
                        "delta": delta,
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
        sample_rate: int | str = Default(44100),
        channels: int | str = Default(1),
        scale: int | Literal["lin", "log"] | Default = Default("LOG"),
        slide: int | Literal["replace", "scroll", "fullframe", "rscroll"] | Default = Default("FULLFRAME"),
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
        | Default = Default(0),
        overlap: float | int | str = Default(1.0),
        orientation: int | Literal["vertical", "horizontal"] | Default = Default("VERTICAL"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        Convert input spectrum videos to audio output.

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

    def split(self, *, outputs: int | str = Default(2), **kwargs: Any) -> FilterNode:
        """

        Pass on the input to N video outputs.

        Parameters:
        ----------

        :param int outputs: set number of outputs

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
        quality: int | str = Default(3),
        qp: int | str = Default(0),
        mode: int | Literal["hard", "soft"] | Default = Default("MODE_HARD"),
        use_bframe_qp: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a simple post processing filter.

        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-6. If set to 0, the filter will have no effect. A value of 6 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        :param int qp: Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        :param int mode: Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding (default). ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier).
        :param bool use_bframe_qp: Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).
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
        dnn_backend: int | str = Default(1),
        scale_factor: int | str = Default(2),
        model: str | float | int = Default("((void*)0)"),
        input: str | float | int = Default("x"),
        output: str | float | int = Default("y"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply DNN-based image super resolution to the input.

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        :param int scale_factor: Set scale factor for SRCNN model. Allowed values are 2, 3 and 4. Default value is 2. Scale factor is necessary for SRCNN model, because it accepts input upscaled using bicubic upscaling with proper scale factor.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        :param str input: input name of the model
        :param str output: output name of the model

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
        stats_file: str | float | int = Default("((void*)0)"),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the SSIM between two video streams.

        Parameters:
        ----------

        :param str stats_file: If specified the filter will use the named file to save the SSIM of each individual frame. When filename equals "-" the data is sent to standard output.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def stereo3d(
        self,
        *,
        _in: int
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
        | Default = Default("SIDE_BY_SIDE_LR"),
        out: int
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
        | Default = Default("ANAGLYPH_RC_DUBOIS"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert video stereoscopic 3D view.

        Parameters:
        ----------

        :param int _in: Set stereoscopic image format of input. Available values for input image formats are: ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first Default value is ‘sbsl’.
        :param int out: Set stereoscopic image format of output. ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘arbg’ anaglyph red/blue gray (red filter on left eye, blue filter on right eye) ‘argg’ anaglyph red/green gray (red filter on left eye, green filter on right eye) ‘arcg’ anaglyph red/cyan gray (red filter on left eye, cyan filter on right eye) ‘arch’ anaglyph red/cyan half colored (red filter on left eye, cyan filter on right eye) ‘arcc’ anaglyph red/cyan color (red filter on left eye, cyan filter on right eye) ‘arcd’ anaglyph red/cyan color optimized with the least squares projection of dubois (red filter on left eye, cyan filter on right eye) ‘agmg’ anaglyph green/magenta gray (green filter on left eye, magenta filter on right eye) ‘agmh’ anaglyph green/magenta half colored (green filter on left eye, magenta filter on right eye) ‘agmc’ anaglyph green/magenta colored (green filter on left eye, magenta filter on right eye) ‘agmd’ anaglyph green/magenta color optimized with the least squares projection of dubois (green filter on left eye, magenta filter on right eye) ‘aybg’ anaglyph yellow/blue gray (yellow filter on left eye, blue filter on right eye) ‘aybh’ anaglyph yellow/blue half colored (yellow filter on left eye, blue filter on right eye) ‘aybc’ anaglyph yellow/blue colored (yellow filter on left eye, blue filter on right eye) ‘aybd’ anaglyph yellow/blue color optimized with the least squares projection of dubois (yellow filter on left eye, blue filter on right eye) ‘ml’ mono output (left eye only) ‘mr’ mono output (right eye only) ‘chl’ checkerboard, left eye first ‘chr’ checkerboard, right eye first ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first ‘hdmi’ HDMI frame pack Default value is ‘arcd’.

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
        filename: str | float | int = Default("((void*)0)"),
        original_size: str | float | int = Default("((void*)0)"),
        fontsdir: str | float | int = Default("((void*)0)"),
        alpha: bool | int | str = Default(0),
        charenc: str | float | int = Default("((void*)0)"),
        stream_index: int | str = Default(-1),
        force_style: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Render text subtitles onto input video using the libass library.

        Parameters:
        ----------

        :param str filename: Set the filename of the subtitle file to read. It must be specified.
        :param str original_size: Specify the size of the original video, the video for which the ASS file was composed. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Due to a misdesign in ASS aspect ratio arithmetic, this is necessary to correctly scale the fonts if the aspect ratio has been changed.
        :param str fontsdir: Set a directory path containing fonts that can be used by the filter. These fonts will be used in addition to whatever the font provider uses.
        :param bool alpha: Process alpha channel, by default alpha channel is untouched.
        :param str charenc: Set subtitles input character encoding. subtitles filter only. Only useful if not UTF-8.
        :param int stream_index: Set subtitles stream index. subtitles filter only.
        :param str force_style: Override default style or script info parameters of the subtitles. It accepts a string containing ASS style format KEY=VALUE couples separated by ",".

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
        w: str | float | int = Default("w/2"),
        h: str | float | int = Default("h/2"),
        x1: str | float | int = Default("w/2"),
        y1: str | float | int = Default("h/2"),
        x2: str | float | int = Default("0"),
        y2: str | float | int = Default("0"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Swap 2 rectangular objects in video.

        Parameters:
        ----------

        :param str w: Set object width.
        :param str h: Set object height.
        :param str x1: Set 1st rect x coordinate.
        :param str y1: Set 1st rect y coordinate.
        :param str x2: Set 2nd rect x coordinate.
        :param str y2: Set 2nd rect y coordinate. All expressions are evaluated once for each frame.
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

    def swapuv(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(0),
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
        | Default = Default(-1),
        c0_expr: str | float | int = Default("((void*)0)"),
        c1_expr: str | float | int = Default("((void*)0)"),
        c2_expr: str | float | int = Default("((void*)0)"),
        c3_expr: str | float | int = Default("((void*)0)"),
        all_expr: str | float | int = Default("((void*)0)"),
        c0_opacity: float | int | str = Default(1.0),
        c1_opacity: float | int | str = Default(1.0),
        c2_opacity: float | int | str = Default(1.0),
        c3_opacity: float | int | str = Default(1.0),
        all_opacity: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Blend successive frames.

        Parameters:
        ----------

        :param int c0_mode: set component #0 blend mode
        :param int c1_mode: set component #1 blend mode
        :param int c2_mode: set component #2 blend mode
        :param int c3_mode: set component #3 blend mode
        :param int all_mode: set blend mode for all components
        :param str c0_expr: set color component #0 expression
        :param str c1_expr: set color component #1 expression
        :param str c2_expr: set color component #2 expression
        :param str c3_expr: set color component #3 expression
        :param str all_expr: set expression for all color components
        :param float c0_opacity: set color component #0 opacity
        :param float c1_opacity: set color component #1 opacity
        :param float c2_opacity: set color component #2 opacity
        :param float c3_opacity: set color component #3 opacity
        :param float all_opacity: set opacity for all color components
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
        first_field: int | Literal["top", "t", "bottom", "b"] | Default = Default(0),
        pattern: str | float | int = Default("23"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a telecine pattern.

        Parameters:
        ----------

        :param int first_field: ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        :param str pattern: A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.

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
        width: int | str = Default(0),
        display_mode: int | Literal["overlay", "parade", "stack"] | Default = Default(2),
        levels_mode: int | Literal["linear", "logarithmic"] | Default = Default(0),
        components: int | str = Default(7),
        bgopacity: float | int | str = Default(0.9),
        envelope: bool | int | str = Default(0),
        ecolor: str | float | int = Default("gold"),
        slide: int | Literal["frame", "replace", "scroll", "rscroll", "picture"] | Default = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and draw a temporal histogram.

        Parameters:
        ----------

        :param int width: Set width of single color component output. Default value is 0. Value of 0 means width will be picked from input video. This also set number of passed histograms to keep. Allowed range is [0, 8192].
        :param int display_mode: Set display mode. It accepts the following values: ‘stack’ Per color component graphs are placed below each other. ‘parade’ Per color component graphs are placed side by side. ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. Default is stack.
        :param int levels_mode: Set mode. Can be either linear, or logarithmic. Default is linear.
        :param int components: Set what color components to display. Default is 7.
        :param float bgopacity: Set background opacity. Default is 0.9.
        :param bool envelope: Show envelope. Default is disabled.
        :param str ecolor: Set envelope color. Default is gold.
        :param int slide: Set slide mode. Available values for slide is: ‘frame’ Draw new frame when right border is reached. ‘replace’ Replace old columns with new ones. ‘scroll’ Scroll from right to left. ‘rscroll’ Scroll from left to right. ‘picture’ Draw single picture. Default is replace.

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
        planes: int | str = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Threshold first video stream using other video streams.

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
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
        n: int | str = Default(100),
        log: int | Literal["quiet", "info", "verbose"] | Default = Default(32),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Select the most representative frame in a given sequence of consecutive frames.

        Parameters:
        ----------

        :param int n: Set the frames batch size to analyze; in a set of n frames, the filter will pick one of them, and then handle the next batch of n frames until the end. Default is 100.
        :param int log: Set the log level to display picked frame stats. Default is info.
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
        layout: str | float | int = Default("6x5"),
        nb_frames: int | str = Default(0),
        margin: int | str = Default(0),
        padding: int | str = Default(0),
        color: str | float | int = Default("black"),
        overlap: int | str = Default(0),
        init_padding: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Tile several successive frames together.

        Parameters:
        ----------

        :param str layout: Set the grid size in the form COLUMNSxROWS. Range is up to UINT_MAX cells. Default is 6x5.
        :param int nb_frames: Set the maximum number of frames to render in the given area. It must be less than or equal to wxh. The default value is 0, meaning all the area will be used.
        :param int margin: Set the outer border margin in pixels. Range is 0 to 1024. Default is 0.
        :param int padding: Set the inner border thickness (i.e. the number of pixels between frames). For more advanced padding options (such as having different values for the edges), refer to the pad video filter. Range is 0 to 1024. Default is 0.
        :param str color: Specify the color of the unused area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".
        :param int overlap: Set the number of frames to overlap when tiling several successive frames together. The value must be between 0 and nb_frames - 1. Default is 0.
        :param int init_padding: Set the number of frames to initially be empty before displaying first output frame. This controls how soon will one get first output frame. The value must be between 0 and nb_frames - 1. Default is 0.

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

    def tiltandshift(
        self,
        *,
        tilt: int | str = Default(1),
        start: int | Literal["none", "frame", "black"] | Default = Default("TILT_NONE"),
        end: int | Literal["none", "frame", "black"] | Default = Default("TILT_NONE"),
        hold: int | str = Default(0),
        pad: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.256 tiltandshift

        What happens when you invert time and space?

        Normally a video is composed of several frames that represent a different
        instant of time and shows a scence that evolves in the space captured by the
        frame. This filter is the antipode of that concept, taking inspiration by tilt
        and shift photography.

        A filtered frame contains the whole timeline of events composing the sequence,
        and this is obtained by placing a slice of pixels from each frame into a
        single one. However, since there are no infinite-width frames, this is done up
        the width of the input frame, and a video is recomposed by shifting away one
        column for each subsequent frame. In order to map space to time, the filter
        tilts each input frame as well, so that motion is preseved. This is
        accomplished by progressively selecting a different column from each input
        frame.

        The end result is a sort of inverted parralax, so that far away objects move
        much faster that the ones in the front. The ideal conditions for this video
        effect are when there is either very little motion and the backgroud is
        static, or when there is a lot of motion and a very wide depth of field (eg.
        wide panorama, while moving on a train).

        The filter accepts the following parameters:

        **tilt**

            Tilt video while shifting (default). When unset, video will be sliding a static image, composed of the first column of each frame.

        **start**

            What to do at the start of filtering (see below).

        **end**

            What to do at the end of filtering (see below).

        **hold**

            How many columns should pass through before start of filtering.

        **pad**

            How many columns should be inserted before end of filtering.

        Normally the filter shifts and tils from the very first frame, and stops when
        the last one is received. However, before filtering starts, normal video may
        be preseved, so that the effect is slowly shifted in its place. Similarly, the
        last video frame may be reconstructed at the end. Alternatively it is possible
        to just start and end with black.

        **‘none’**

            Filtering is starts immediately and ends when the last frame is received.

        **‘frame’**

            The first frames or the very last frame are kept intact during processing.

        **‘black’**

            Black is padded at the beginning or at the end of filtering.



        Parameters:
        ----------

        :param int tilt: Tilt video while shifting (default). When unset, video will be sliding a static image, composed of the first column of each frame.
        :param int start: What to do at the start of filtering (see below).
        :param int end: What to do at the end of filtering (see below).
        :param int hold: How many columns should pass through before start of filtering.
        :param int pad: How many columns should be inserted before end of filtering.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tiltandshift

        """
        filter_node = FilterNode(
            name="tiltandshift",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "tilt": tilt,
                        "start": start,
                        "end": end,
                        "hold": hold,
                        "pad": pad,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tinterlace(
        self,
        *,
        mode: int
        | Literal[
            "merge", "drop_even", "drop_odd", "pad", "interleave_top", "interleave_bottom", "interlacex2", "mergex2"
        ]
        | Default = Default("MODE_MERGE"),
        flags: str
        | Literal["low_pass_filter", "vlpf", "complex_filter", "cvlpf", "exact_tb", "bypass_il"]
        | Default = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Perform temporal field interlacing.

        Parameters:
        ----------

        :param int mode: Specify the mode of the interlacing. This option can also be specified as a value alone. See below for a list of values for this option. Available values are: ‘merge, 0’ Move odd frames into the upper field, even into the lower field, generating a double height frame at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 22222 44444 11111 33333 22222 44444 11111 33333 22222 44444 11111 33333 22222 44444 ‘drop_even, 1’ Only output odd frames, even frames are dropped, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 11111 33333 11111 33333 11111 33333 ‘drop_odd, 2’ Only output even frames, odd frames are dropped, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 22222 44444 22222 44444 22222 44444 22222 44444 ‘pad, 3’ Expand each frame to full height, but pad alternate lines with black, generating a frame with double height at the same input frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 ‘interleave_top, 4’ Interleave the upper field from odd frames with the lower field from even frames, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- Output: 11111 33333 22222 44444 11111 33333 22222 44444 ‘interleave_bottom, 5’ Interleave the lower field from odd frames with the upper field from even frames, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 Output: 22222 44444 11111 33333 22222 44444 11111 33333 ‘interlacex2, 6’ Double frame rate with unchanged height. Frames are inserted each containing the second temporal field from the previous input frame and the first temporal field from the next input frame. This mode relies on the top_field_first flag. Useful for interlaced video displays with no field synchronisation. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 22222 22222 33333 33333 44444 44444 11111 11111 22222 22222 33333 33333 44444 11111 22222 22222 33333 33333 44444 44444 11111 11111 22222 22222 33333 33333 44444 ‘mergex2, 7’ Move odd frames into the upper field, even into the lower field, generating a double height frame at same frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 Numeric values are deprecated but are accepted for backward compatibility reasons. Default mode is merge.
        :param str flags: Specify flags influencing the filter process. Available value for flags is: low_pass_filter, vlpf Enable linear vertical low-pass filtering in the filter. Vertical low-pass filtering is required when creating an interlaced destination from a progressive source which contains high-frequency vertical detail. Filtering will reduce interlace ’twitter’ and Moire patterning. complex_filter, cvlpf Enable complex vertical low-pass filtering. This will slightly less reduce interlace ’twitter’ and Moire patterning but better retain detail and subjective sharpness impression. bypass_il Bypass already interlaced frames, only adjust the frame rate. Vertical low-pass filtering and bypassing already interlaced frames can only be enabled for mode interleave_top and interleave_bottom.

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
                        "flags": flags,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tlut2(
        self,
        *,
        c0: str | float | int = Default("x"),
        c1: str | float | int = Default("x"),
        c2: str | float | int = Default("x"),
        c3: str | float | int = Default("x"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Compute and apply a lookup table from two successive frames.

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component
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
        radius: int | str = Default(1),
        planes: int | str = Default(15),
        percentile: float | int | str = Default(0.5),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick median pixels from successive frames.

        Parameters:
        ----------

        :param int radius: Set radius of median filter. Default is 1. Allowed range is from 1 to 127.
        :param int planes: Set which planes to filter. Default value is 15, by which all planes are processed.
        :param float percentile: Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.
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
        radius: int | str = Default(5),
        sigma: float | int | str = Default(0.5),
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Temporal Midway Equalization.

        Parameters:
        ----------

        :param int radius: Set filtering radius. Default is 5. Allowed range is from 1 to 127.
        :param float sigma: Set filtering sigma. Default is 0.5. This controls strength of filtering. Setting this option to 0 effectively does nothing.
        :param int planes: Set which planes to process. Default is 15, which is all available planes.
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
        frames: int | str = Default(3),
        weights: str | float | int = Default("1 1 1"),
        scale: float | int | str = Default(0.0),
        planes: str | float | int = Default(15),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Mix successive video frames.

        Parameters:
        ----------

        :param int frames: The number of successive frames to mix. If unspecified, it defaults to 3.
        :param str weights: Specify weight of each input video frame. Each weight is separated by space. If number of weights is smaller than number of frames last specified weight will be used for all remaining unset weights.
        :param float scale: Specify scale, if it is set it will be multiplied with sum of each weight multiplied with pixel values to give final destination pixel value. By default scale is auto scaled to sum of weights.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.
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
        tonemap: int
        | Literal["none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"]
        | Default = Default("TONEMAP_NONE"),
        param: float | int | str = Default('__builtin_nanf("0x7fc00000")'),
        desat: float | int | str = Default(2.0),
        peak: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Conversion to/from different dynamic ranges.

        Parameters:
        ----------

        :param int tonemap: tonemap algorithm selection
        :param float param: tonemap parameter
        :param float desat: desaturation strength
        :param float peak: signal peak override

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

    def tonemap_opencl(
        self,
        *,
        tonemap: int
        | Literal["none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"]
        | Default = Default("TONEMAP_NONE"),
        transfer: int | Literal["bt709", "bt2020"] | Default = Default("AVCOL_TRC_BT709"),
        matrix: int | Literal["bt709", "bt2020"] | Default = Default(-1),
        primaries: int | Literal["bt709", "bt2020"] | Default = Default(-1),
        range: int | Literal["tv", "pc", "limited", "full"] | Default = Default(-1),
        format: str | float | int = Default("AV_PIX_FMT_NONE"),
        peak: float | int | str = Default(0.0),
        param: float | int | str = Default('__builtin_nanf("0x7fc00000")'),
        desat: float | int | str = Default(0.5),
        threshold: float | int | str = Default(0.2),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.16 tonemap_opencl

        Perform HDR(PQ/HLG) to SDR conversion with tone-mapping.

        It accepts the following parameters:

        **tonemap**

            Specify the tone-mapping operator to be used. Same as tonemap option in tonemap.

        **param**

            Tune the tone mapping algorithm. same as param option in tonemap.

        **desat**

            Apply desaturation for highlights that exceed this level of brightness. The higher the parameter, the more color information will be preserved. This setting helps prevent unnaturally blown-out colors for super-highlights, by (smoothly) turning into white instead. This makes images feel more natural, at the cost of reducing information about out-of-range colors. The default value is 0.5, and the algorithm here is a little different from the cpu version tonemap currently. A setting of 0.0 disables this option.

        **threshold**

            The tonemapping algorithm parameters is fine-tuned per each scene. And a threshold is used to detect whether the scene has changed or not. If the distance between the current frame average brightness and the current running average exceeds a threshold value, we would re-calculate scene average and peak brightness. The default value is 0.2.

        **format**

            Specify the output pixel format. Currently supported formats are: p010 nv12

        **range, r**

            Set the output color range. Possible values are: tv/mpeg pc/jpeg Default is same as input.

        **primaries, p**

            Set the output color primaries. Possible values are: bt709 bt2020 Default is same as input.

        **transfer, t**

            Set the output transfer characteristics. Possible values are: bt709 bt2020 Default is bt709.

        **matrix, m**

            Set the output colorspace matrix. Possible value are: bt709 bt2020 Default is same as input.



        Parameters:
        ----------

        :param int tonemap: Specify the tone-mapping operator to be used. Same as tonemap option in tonemap.
        :param int transfer: Set the output transfer characteristics. Possible values are: bt709 bt2020 Default is bt709.
        :param int matrix: Set the output colorspace matrix. Possible value are: bt709 bt2020 Default is same as input.
        :param int primaries: Set the output color primaries. Possible values are: bt709 bt2020 Default is same as input.
        :param int range: Set the output color range. Possible values are: tv/mpeg pc/jpeg Default is same as input.
        :param str format: Specify the output pixel format. Currently supported formats are: p010 nv12
        :param float peak: signal peak override
        :param float param: Tune the tone mapping algorithm. same as param option in tonemap.
        :param float desat: Apply desaturation for highlights that exceed this level of brightness. The higher the parameter, the more color information will be preserved. This setting helps prevent unnaturally blown-out colors for super-highlights, by (smoothly) turning into white instead. This makes images feel more natural, at the cost of reducing information about out-of-range colors. The default value is 0.5, and the algorithm here is a little different from the cpu version tonemap currently. A setting of 0.0 disables this option.
        :param float threshold: The tonemapping algorithm parameters is fine-tuned per each scene. And a threshold is used to detect whether the scene has changed or not. If the distance between the current frame average brightness and the current running average exceeds a threshold value, we would re-calculate scene average and peak brightness. The default value is 0.2.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap_005fopencl

        """
        filter_node = FilterNode(
            name="tonemap_opencl",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tonemap_vaapi(
        self,
        *,
        format: str | float | int = Default(None),
        matrix: str | float | int = Default("((void*)0)"),
        primaries: str | float | int = Default("((void*)0)"),
        transfer: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 13.2 tonemap_vaapi

        Perform HDR(High Dynamic Range) to SDR(Standard Dynamic Range) conversion with
        tone-mapping. It maps the dynamic range of HDR10 content to the SDR content.
        It currently only accepts HDR10 as input.

        It accepts the following parameters:

        **format**

            Specify the output pixel format. Currently supported formats are: p010 nv12 Default is nv12.

        **primaries, p**

            Set the output color primaries. Default is same as input.

        **transfer, t**

            Set the output transfer characteristics. Default is bt709.

        **matrix, m**

            Set the output colorspace matrix. Default is same as input.



        Parameters:
        ----------

        :param str format: Specify the output pixel format. Currently supported formats are: p010 nv12 Default is nv12.
        :param str matrix: Set the output colorspace matrix. Default is same as input.
        :param str primaries: Set the output color primaries. Default is same as input.
        :param str transfer: Set the output transfer characteristics. Default is bt709.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap_005fvaapi

        """
        filter_node = FilterNode(
            name="tonemap_vaapi",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "format": format,
                        "matrix": matrix,
                        "primaries": primaries,
                        "transfer": transfer,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def tpad(
        self,
        *,
        start: int | str = Default(0),
        stop: int | str = Default(0),
        start_mode: int | Literal["add", "clone"] | Default = Default("MODE_ADD"),
        stop_mode: int | Literal["add", "clone"] | Default = Default("MODE_ADD"),
        start_duration: int | str = Default(0),
        stop_duration: int | str = Default(0),
        color: str | float | int = Default("black"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Temporarily pad video frames.

        Parameters:
        ----------

        :param int start: Specify number of delay frames before input video stream. Default is 0.
        :param int stop: Specify number of padding frames after input video stream. Set to -1 to pad indefinitely. Default is 0.
        :param int start_mode: Set kind of frames added to beginning of stream. Can be either add or clone. With add frames of solid-color are added. With clone frames are clones of first frame. Default is add.
        :param int stop_mode: Set kind of frames added to end of stream. Can be either add or clone. With add frames of solid-color are added. With clone frames are clones of last frame. Default is add.
        :param int start_duration: Specify the duration of the start/stop delay. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. These options override start and stop. Default is 0.
        :param int stop_duration: Specify the duration of the start/stop delay. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. These options override start and stop. Default is 0.
        :param str color: Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".

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
        dir: int | str = Default("TRANSPOSE_CCLOCK_FLIP"),
        passthrough: int | Literal["none", "portrait", "landscape"] | Default = Default("TRANSPOSE_PT_TYPE_NONE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transpose input video.

        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘0, 4, cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip (default), that is: L.R L.l . . -> . . l.r R.r ‘1, 5, clock’ Rotate by 90 degrees clockwise, that is: L.R l.L . . -> . . l.r r.R ‘2, 6, cclock’ Rotate by 90 degrees counterclockwise, that is: L.R R.r . . -> . . l.r L.l ‘3, 7, clock_flip’ Rotate by 90 degrees clockwise and vertically flip, that is: L.R r.R . . -> . . l.r l.L For values between 4-7, the transposition is only done if the input video geometry is portrait and not landscape. These values are deprecated, the passthrough option should be used instead. Numerical values are deprecated, and should be dropped in favor of symbolic constants.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height). Default value is none.

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

    def transpose_npp(
        self,
        *,
        dir: int
        | Literal["cclock_flip", "clock", "cclock", "clock_flip"]
        | Default = Default("NPP_TRANSPOSE_CCLOCK_FLIP"),
        passthrough: int | Literal["none", "landscape", "portrait"] | Default = Default("NPP_TRANSPOSE_PT_TYPE_NONE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.264 transpose_npp

        Transpose rows with columns in the input video and optionally flip it. For
        more in depth examples see the transpose video filter, which shares mostly the
        same options.

        It accepts the following parameters:

        **dir**

            Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.

        **passthrough**

            Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).



        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fnpp

        """
        filter_node = FilterNode(
            name="transpose_npp",
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

    def transpose_vt(
        self,
        *,
        dir: int | str = Default("TRANSPOSE_CCLOCK_FLIP"),
        passthrough: int | Literal["none", "portrait", "landscape"] | Default = Default("TRANSPOSE_PT_TYPE_NONE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.12 transpose_vt

        Transpose rows with columns in the input video and optionally flip it. For
        more in depth examples see the transpose video filter, which shares mostly the
        same options.

        It accepts the following parameters:

        **dir**

            Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip. ‘hflip’ Flip the input video horizontally. ‘vflip’ Flip the input video vertically.

        **passthrough**

            Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).



        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip. ‘hflip’ Flip the input video horizontally. ‘vflip’ Flip the input video vertically.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvt

        """
        filter_node = FilterNode(
            name="transpose_vt",
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

    def transpose_vulkan(
        self,
        *,
        dir: int | str = Default("TRANSPOSE_CCLOCK_FLIP"),
        passthrough: int | Literal["none", "portrait", "landscape"] | Default = Default("TRANSPOSE_PT_TYPE_NONE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 14.13 transpose_vulkan

        Transpose rows with columns in the input video and optionally flip it. For
        more in depth examples see the transpose video filter, which shares mostly the
        same options.

        It accepts the following parameters:

        **dir**

            Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.

        **passthrough**

            Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).



        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvulkan

        """
        filter_node = FilterNode(
            name="transpose_vulkan",
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
        start: int | str = Default("9223372036854775807LL"),
        end: int | str = Default("9223372036854775807LL"),
        start_pts: int | str = Default("((int64_t)(0x8000000000000000ULL))"),
        end_pts: int | str = Default("((int64_t)(0x8000000000000000ULL))"),
        duration: int | str = Default(0),
        start_frame: int | str = Default(-1),
        end_frame: int | str = Default("9223372036854775807LL"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Pick one continuous section from the input, drop the rest.

        Parameters:
        ----------

        :param int start: Timestamp of the first frame that should be passed
        :param int end: Timestamp of the first frame that should be dropped again
        :param int start_pts: Timestamp of the first frame that should be passed
        :param int end_pts: Timestamp of the first frame that should be dropped again
        :param int duration: Maximum duration of the output
        :param int start_frame: Number of the first frame that should be passed to the output
        :param int end_frame: Number of the first frame that should be dropped again

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
        luma_msize_x: int | str = Default(5),
        luma_msize_y: int | str = Default(5),
        luma_amount: float | int | str = Default(1.0),
        chroma_msize_x: int | str = Default(5),
        chroma_msize_y: int | str = Default(5),
        chroma_amount: float | int | str = Default(0.0),
        alpha_msize_x: int | str = Default(5),
        alpha_msize_y: int | str = Default(5),
        alpha_amount: float | int | str = Default(0.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Sharpen or blur the input video.

        Parameters:
        ----------

        :param int luma_msize_x: Set the luma matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        :param int luma_msize_y: Set the luma matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        :param float luma_amount: Set the luma effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 1.0.
        :param int chroma_msize_x: Set the chroma matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        :param int chroma_msize_y: Set the chroma matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        :param float chroma_amount: Set the chroma effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 0.0.
        :param int alpha_msize_x: Set the alpha matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        :param int alpha_msize_y: Set the alpha matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        :param float alpha_amount: Set the alpha effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 0.0.
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

    def unsharp_opencl(
        self,
        *,
        luma_msize_x: float | int | str = Default(5.0),
        luma_msize_y: float | int | str = Default(5.0),
        luma_amount: float | int | str = Default(1.0),
        chroma_msize_x: float | int | str = Default(5.0),
        chroma_msize_y: float | int | str = Default(5.0),
        chroma_amount: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 12.17 unsharp_opencl

        Sharpen or blur the input video.

        It accepts the following parameters:

        **luma_msize_x, lx**

            Set the luma matrix horizontal size. Range is [1, 23] and default value is 5.

        **luma_msize_y, ly**

            Set the luma matrix vertical size. Range is [1, 23] and default value is 5.

        **luma_amount, la**

            Set the luma effect strength. Range is [-10, 10] and default value is 1.0. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect.

        **chroma_msize_x, cx**

            Set the chroma matrix horizontal size. Range is [1, 23] and default value is 5.

        **chroma_msize_y, cy**

            Set the chroma matrix vertical size. Range is [1, 23] and default value is 5.

        **chroma_amount, ca**

            Set the chroma effect strength. Range is [-10, 10] and default value is 0.0. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect.

        All parameters are optional and default to the equivalent of the string
        ’5:5:1.0:5:5:0.0’.



        Parameters:
        ----------

        :param float luma_msize_x: Set the luma matrix horizontal size. Range is [1, 23] and default value is 5.
        :param float luma_msize_y: Set the luma matrix vertical size. Range is [1, 23] and default value is 5.
        :param float luma_amount: Set the luma effect strength. Range is [-10, 10] and default value is 1.0. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect.
        :param float chroma_msize_x: Set the chroma matrix horizontal size. Range is [1, 23] and default value is 5.
        :param float chroma_msize_y: Set the chroma matrix vertical size. Range is [1, 23] and default value is 5.
        :param float chroma_amount: Set the chroma effect strength. Range is [-10, 10] and default value is 0.0. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#unsharp_005fopencl

        """
        filter_node = FilterNode(
            name="unsharp_opencl",
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
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def untile(self, *, layout: str | float | int = Default("6x5"), **kwargs: Any) -> "VideoStream":
        """

        Untile a frame into a sequence of frames.

        Parameters:
        ----------

        :param str layout: Set the grid size (i.e. the number of lines and columns). For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.

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

    def uspp(
        self,
        *,
        quality: int | str = Default(3),
        qp: int | str = Default(0),
        use_bframe_qp: bool | int | str = Default(0),
        codec: str | float | int = Default("snow"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.269 uspp

        Apply ultra slow/simple postprocessing filter that compresses and decompresses
        the image at several (or - in the case of quality level `8` - all) shifts and
        average the results.

        The way this differs from the behavior of spp is that uspp actually encodes &
        decodes each case with libavcodec Snow, whereas spp uses a simplified intra
        only 8x8 DCT similar to MJPEG.

        This filter is only available in ffmpeg version 4.4 or earlier.

        The filter accepts the following options:

        **quality**

            Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-8. If set to 0, the filter will have no effect. A value of 8 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.

        **qp**

            Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).

        **codec**

            Use specified codec instead of snow.



        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-8. If set to 0, the filter will have no effect. A value of 8 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        :param int qp: Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        :param bool use_bframe_qp: use B-frames' QP
        :param str codec: Use specified codec instead of snow.
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#uspp

        """
        filter_node = FilterNode(
            name="uspp",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(
                (
                    {
                        "quality": quality,
                        "qp": qp,
                        "use_bframe_qp": use_bframe_qp,
                        "codec": codec,
                        "enable": enable,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def v360(
        self,
        *,
        input: int
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
        | Default = Default("EQUIRECTANGULAR"),
        output: int
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
        | Default = Default("CUBEMAP_3_2"),
        interp: int
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
        | Default = Default("BILINEAR"),
        w: int | str = Default(0),
        h: int | str = Default(0),
        in_stereo: int | Literal["2d", "sbs", "tb"] | Default = Default("STEREO_2D"),
        out_stereo: int | Literal["2d", "sbs", "tb"] | Default = Default("STEREO_2D"),
        in_forder: str | float | int = Default("rludfb"),
        out_forder: str | float | int = Default("rludfb"),
        in_frot: str | float | int = Default("000000"),
        out_frot: str | float | int = Default("000000"),
        in_pad: float | int | str = Default("0.f"),
        out_pad: float | int | str = Default("0.f"),
        fin_pad: int | str = Default(0),
        fout_pad: int | str = Default(0),
        yaw: float | int | str = Default("0.f"),
        pitch: float | int | str = Default("0.f"),
        roll: float | int | str = Default("0.f"),
        rorder: str | float | int = Default("ypr"),
        h_fov: float | int | str = Default("0.f"),
        v_fov: float | int | str = Default("0.f"),
        d_fov: float | int | str = Default("0.f"),
        h_flip: bool | int | str = Default(0),
        v_flip: bool | int | str = Default(0),
        d_flip: bool | int | str = Default(0),
        ih_flip: bool | int | str = Default(0),
        iv_flip: bool | int | str = Default(0),
        in_trans: bool | int | str = Default(0),
        out_trans: bool | int | str = Default(0),
        ih_fov: float | int | str = Default("0.f"),
        iv_fov: float | int | str = Default("0.f"),
        id_fov: float | int | str = Default("0.f"),
        h_offset: float | int | str = Default("0.f"),
        v_offset: float | int | str = Default("0.f"),
        alpha_mask: bool | int | str = Default(0),
        reset_rot: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Convert 360 projection of video.

        Parameters:
        ----------

        :param int input: Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        :param int output: Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        :param int interp: Set interpolation method. Note: more complex interpolation methods require much more memory to run. Available methods: ‘near’ ‘nearest’ Nearest neighbour. ‘line’ ‘linear’ Bilinear interpolation. ‘lagrange9’ Lagrange9 interpolation. ‘cube’ ‘cubic’ Bicubic interpolation. ‘lanc’ ‘lanczos’ Lanczos interpolation. ‘sp16’ ‘spline16’ Spline16 interpolation. ‘gauss’ ‘gaussian’ Gaussian interpolation. ‘mitchell’ Mitchell interpolation. Default value is ‘line’.
        :param int w: Set the output video resolution. Default resolution depends on formats.
        :param int h: Set the output video resolution. Default resolution depends on formats.
        :param int in_stereo: Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        :param int out_stereo: Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        :param str in_forder: input cubemap face order
        :param str out_forder: output cubemap face order
        :param str in_frot: input cubemap face rotation
        :param str out_frot: output cubemap face rotation
        :param float in_pad: percent input cubemap pads
        :param float out_pad: percent output cubemap pads
        :param int fin_pad: fixed input cubemap pads
        :param int fout_pad: fixed output cubemap pads
        :param float yaw: Set rotation for the output video. Values in degrees.
        :param float pitch: Set rotation for the output video. Values in degrees.
        :param float roll: Set rotation for the output video. Values in degrees.
        :param str rorder: Set rotation order for the output video. Choose one item for each position. ‘y, Y’ yaw ‘p, P’ pitch ‘r, R’ roll Default value is ‘ypr’.
        :param float h_fov: output horizontal field of view
        :param float v_fov: output vertical field of view
        :param float d_fov: output diagonal field of view
        :param bool h_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool v_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool d_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool ih_flip: Set if input video is flipped horizontally/vertically. Boolean values.
        :param bool iv_flip: Set if input video is flipped horizontally/vertically. Boolean values.
        :param bool in_trans: Set if input video is transposed. Boolean value, by default disabled.
        :param bool out_trans: Set if output video needs to be transposed. Boolean value, by default disabled.
        :param float ih_fov: input horizontal field of view
        :param float iv_fov: input vertical field of view
        :param float id_fov: input diagonal field of view
        :param float h_offset: Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        :param float v_offset: Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        :param bool alpha_mask: Build mask in alpha plane for all unmapped pixels by marking them fully transparent. Boolean value, by default disabled.
        :param bool reset_rot: Reset rotation of output video. Boolean value, by default disabled.

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
        threshold: float | int | str = Default(2.0),
        method: int | Literal["hard", "soft", "garrote"] | Default = Default(2),
        nsteps: int | str = Default(6),
        percent: float | int | str = Default(85.0),
        planes: int | str = Default(15),
        type: int | Literal["universal", "bayes"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply a Wavelet based Denoiser.

        Parameters:
        ----------

        :param float threshold: The filtering strength. The higher, the more filtered the video will be. Hard thresholding can use a higher threshold than soft thresholding before the video looks overfiltered. Default value is 2.
        :param int method: The filtering method the filter will use. It accepts the following values: ‘hard’ All values under the threshold will be zeroed. ‘soft’ All values under the threshold will be zeroed. All values above will be reduced by the threshold. ‘garrote’ Scales or nullifies coefficients - intermediary between (more) soft and (less) hard thresholding. Default is garrote.
        :param int nsteps: Number of times, the wavelet will decompose the picture. Picture can’t be decomposed beyond a particular point (typically, 8 for a 640x480 frame - as 2^9 = 512 > 480). Valid values are integers between 1 and 32. Default value is 6.
        :param float percent: Partial of full denoising (limited coefficients shrinking), from 0 to 100. Default value is 85.
        :param int planes: A list of the planes to process. By default all planes are processed.
        :param int type: The threshold type the filter will use. It accepts the following values: ‘universal’ Threshold used is same for all decompositions. ‘bayes’ Threshold used depends also on each decomposition coefficients. Default is universal.
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
        min_r: int | str = Default(0),
        max_r: int | str = Default(8),
        planes: int | str = Default("0xF"),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Variable Blur filter.

        Parameters:
        ----------

        :param int min_r: Set min allowed radius. Allowed range is from 0 to 254. Default is 0.
        :param int max_r: Set max allowed radius. Allowed range is from 1 to 255. Default is 8.
        :param int planes: Set which planes to process. By default, all are used.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def vectorscope(
        self,
        *,
        mode: int | Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"] | Default = Default(0),
        x: int | str = Default(1),
        y: int | str = Default(2),
        intensity: float | int | str = Default(0.004),
        envelope: int | Literal["none", "instant", "peak", "peak+instant"] | Default = Default(0),
        graticule: int | Literal["none", "green", "color", "invert"] | Default = Default("GRAT_NONE"),
        opacity: float | int | str = Default(0.75),
        flags: str | Literal["white", "black", "name"] | Default = Default(4),
        bgopacity: float | int | str = Default(0.3),
        lthreshold: float | int | str = Default(0.0),
        hthreshold: float | int | str = Default(1.0),
        colorspace: int | Literal["auto", "601", "709"] | Default = Default(0),
        tint0: float | int | str = Default(0.0),
        tint1: float | int | str = Default(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video vectorscope.

        Parameters:
        ----------

        :param int mode: Set vectorscope mode. It accepts the following values: ‘gray’ ‘tint’ Gray values are displayed on graph, higher brightness means more pixels have same component color value on location in graph. This is the default mode. ‘color’ Gray values are displayed on graph. Surrounding pixels values which are not present in video frame are drawn in gradient of 2 color components which are set by option x and y. The 3rd color component is static. ‘color2’ Actual color components values present in video frame are displayed on graph. ‘color3’ Similar as color2 but higher frequency of same values x and y on graph increases value of another color component, which is luminance by default values of x and y. ‘color4’ Actual colors present in video frame are displayed on graph. If two different colors map to same position on graph then color with higher value of component not present in graph is picked. ‘color5’ Gray values are displayed on graph. Similar to color but with 3rd color component picked from radial gradient.
        :param int x: Set which color component will be represented on X-axis. Default is 1.
        :param int y: Set which color component will be represented on Y-axis. Default is 2.
        :param float intensity: Set intensity, used by modes: gray, color, color3 and color5 for increasing brightness of color component which represents frequency of (X, Y) location in graph.
        :param int envelope: ‘none’ No envelope, this is default. ‘instant’ Instant envelope, even darkest single pixel will be clearly highlighted. ‘peak’ Hold maximum and minimum values presented in graph over time. This way you can still spot out of range values without constantly looking at vectorscope. ‘peak+instant’ Peak and instant envelope combined together.
        :param int graticule: Set what kind of graticule to draw. ‘none’ ‘green’ ‘color’ ‘invert’
        :param float opacity: Set graticule opacity.
        :param str flags: Set graticule flags. ‘white’ Draw graticule for white point. ‘black’ Draw graticule for black point. ‘name’ Draw color points short names.
        :param float bgopacity: Set background opacity.
        :param float lthreshold: Set low threshold for color component not represented on X or Y axis. Values lower than this value will be ignored. Default is 0. Note this value is multiplied with actual max possible value one pixel component can have. So for 8-bit input and low threshold value of 0.1 actual threshold is 0.1 * 255 = 25.
        :param float hthreshold: Set high threshold for color component not represented on X or Y axis. Values higher than this value will be ignored. Default is 1. Note this value is multiplied with actual max possible value one pixel component can have. So for 8-bit input and high threshold value of 0.9 actual threshold is 0.9 * 255 = 230.
        :param int colorspace: Set what kind of colorspace to use when drawing graticule. ‘auto’ ‘601’ ‘709’ Default is auto.
        :param float tint0: Set color tint for gray/tint vectorscope mode. By default both options are zero. This means no tint, and output will remain gray.
        :param float tint1: Set color tint for gray/tint vectorscope mode. By default both options are zero. This means no tint, and output will remain gray.

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

    def vflip(self, *, enable: str | float | int = Default(None), **kwargs: Any) -> "VideoStream":
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

    def vflip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        ### 14.6 vflip_vulkan

        Flips an image vertically.



        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#vflip_005fvulkan

        """
        filter_node = FilterNode(
            name="vflip_vulkan",
            input_typings=tuple([StreamType.video]),
            output_typings=tuple([StreamType.video]),
            inputs=(self,),
            kwargs=tuple(({} | kwargs).items()),
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
        intensity: float | int | str = Default(0.0),
        rbal: float | int | str = Default(1.0),
        gbal: float | int | str = Default(1.0),
        bbal: float | int | str = Default(1.0),
        rlum: float | int | str = Default(0.072186),
        glum: float | int | str = Default(0.715158),
        blum: float | int | str = Default(0.212656),
        alternate: bool | int | str = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Boost or alter saturation.

        Parameters:
        ----------

        :param float intensity: Set strength of boost if positive value or strength of alter if negative value. Default is 0. Allowed range is from -2 to 2.
        :param float rbal: Set the red balance. Default is 1. Allowed range is from -10 to 10.
        :param float gbal: Set the green balance. Default is 1. Allowed range is from -10 to 10.
        :param float bbal: Set the blue balance. Default is 1. Allowed range is from -10 to 10.
        :param float rlum: Set the red luma coefficient.
        :param float glum: Set the green luma coefficient.
        :param float blum: Set the blue luma coefficient.
        :param bool alternate: If intensity is negative and this is set to 1, colors will change, otherwise colors will be less saturated, more towards gray.
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
        result: str | float | int = Default("transforms.trf"),
        shakiness: int | str = Default(5),
        accuracy: int | str = Default(15),
        stepsize: int | str = Default(6),
        mincontrast: float | int | str = Default(0.25),
        show: int | str = Default(0),
        tripod: int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2).

        Parameters:
        ----------

        :param str result: Set the path to the file used to write the transforms information. Default value is transforms.trf.
        :param int shakiness: Set how shaky the video is and how quick the camera is. It accepts an integer in the range 1-10, a value of 1 means little shakiness, a value of 10 means strong shakiness. Default value is 5.
        :param int accuracy: Set the accuracy of the detection process. It must be a value in the range 1-15. A value of 1 means low accuracy, a value of 15 means high accuracy. Default value is 15.
        :param int stepsize: Set stepsize of the search process. The region around minimum is scanned with 1 pixel resolution. Default value is 6.
        :param float mincontrast: Set minimum contrast. Below this value a local measurement field is discarded. Must be a floating point value in the range 0-1. Default value is 0.3.
        :param int show: Show fields and transforms in the resulting frames. It accepts an integer in the range 0-2. Default value is 0, which disables any visualization.
        :param int tripod: Set reference frame number for tripod mode. If enabled, the motion of the frames is compared to a reference frame in the filtered stream, identified by the specified number. The idea is to compensate all movements in a more-or-less static scene and keep the camera view absolutely still. If set to 0, it is disabled. The frames are counted starting from 1.

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
        input: str | float | int = Default("transforms.trf"),
        smoothing: int | str = Default(15),
        optalgo: int | Literal["opt", "gauss", "avg"] | Default = Default("VSOptimalL1"),
        maxshift: int | str = Default(-1),
        maxangle: float | int | str = Default(-1.0),
        crop: int | Literal["keep", "black"] | Default = Default(0),
        invert: int | str = Default(0),
        relative: int | str = Default(1),
        zoom: float | int | str = Default(0.0),
        optzoom: int | str = Default(1),
        zoomspeed: float | int | str = Default(0.25),
        interpol: int | Literal["no", "linear", "bilinear", "bicubic"] | Default = Default(2),
        tripod: bool | int | str = Default(0),
        debug: bool | int | str = Default(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1).

        Parameters:
        ----------

        :param str input: set path to the file storing the transforms
        :param int smoothing: set number of frames*2 + 1 used for lowpass filtering
        :param int optalgo: set camera path optimization algo
        :param int maxshift: set maximal number of pixels to translate image
        :param float maxangle: set maximal angle in rad to rotate image
        :param int crop: set cropping mode
        :param int invert: invert transforms
        :param int relative: consider transforms as relative
        :param float zoom: set percentage to zoom (>0: zoom in, <0: zoom out
        :param int optzoom: set optimal zoom (0: nothing, 1: optimal static zoom, 2: optimal dynamic zoom)
        :param float zoomspeed: for adative zoom: percent to zoom maximally each frame
        :param int interpol: set type of interpolation
        :param bool tripod: enable virtual tripod mode (same as relative=0:smoothing=0)
        :param bool debug: enable debug mode and writer global motions information to file

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
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Calculate the VIF between two video streams.

        Parameters:
        ----------

        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def vignette(
        self,
        *,
        angle: str | float | int = Default("PI/5"),
        x0: str | float | int = Default("w/2"),
        y0: str | float | int = Default("h/2"),
        mode: int | Literal["forward", "backward"] | Default = Default(0),
        eval: int | str = Default("EVAL_MODE_INIT"),
        dither: bool | int | str = Default(1),
        aspect: float | int | str = Default(1.0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Make or reverse a vignette effect.

        Parameters:
        ----------

        :param str angle: Set lens angle expression as a number of radians. The value is clipped in the [0,PI/2] range. Default value: "PI/5"
        :param str x0: Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        :param str y0: Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        :param int mode: Set forward/backward mode. Available modes are: ‘forward’ The larger the distance from the central point, the darker the image becomes. ‘backward’ The larger the distance from the central point, the brighter the image becomes. This can be used to reverse a vignette effect, though there is no automatic detection to extract the lens angle and other settings (yet). It can also be used to create a burning effect. Default value is ‘forward’.
        :param int eval: Set evaluation mode for the expressions (angle, x0, y0). It accepts the following values: ‘init’ Evaluate expressions only once during the filter initialization. ‘frame’ Evaluate expressions for each incoming frame. This is way slower than the ‘init’ mode since it requires all the scalers to be re-computed, but it allows advanced dynamic expressions. Default value is ‘init’.
        :param bool dither: Set dithering to reduce the circular banding effects. Default is 1 (enabled).
        :param float aspect: Set vignette aspect. This setting allows one to adjust the shape of the vignette. Setting this value to the SAR of the input will make a rectangular vignetting following the dimensions of the video. Default is 1/1.
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

    def vmafmotion(self, *, stats_file: str | float | int = Default("((void*)0)"), **kwargs: Any) -> "VideoStream":
        """

        Calculate the VMAF Motion score.

        Parameters:
        ----------

        :param str stats_file: If specified, the filter will use the named file to save the motion score of each frame with respect to the previous frame. When filename equals "-" the data is sent to standard output.

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
        filter: int | Literal["simple", "complex"] | Default = Default(1),
        mode: int | Literal["frame", "field"] | Default = Default(1),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default(-1),
        deint: int | Literal["all", "interlaced"] | Default = Default(0),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Martin Weston three field deinterlace.

        Parameters:
        ----------

        :param int filter: Set the interlacing filter coefficients. Accepts one of the following values: ‘simple’ Simple filter coefficient set. ‘complex’ More-complex filter coefficient set. Default value is ‘complex’.
        :param int mode: The interlacing mode to adopt. It accepts one of the following values: frame Output one frame for each frame. field Output one frame for each field. The default value is field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: tff Assume the top field is first. bff Assume the bottom field is first. auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: ‘all’ Deinterlace all frames, ‘interlaced’ Only deinterlace frames marked as interlaced. Default value is ‘all’.
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
        mode: int | Literal["row", "column"] | Default = Default(1),
        intensity: float | int | str = Default(0.04),
        mirror: bool | int | str = Default(1),
        display: int | Literal["overlay", "stack", "parade"] | Default = Default("STACK"),
        components: int | str = Default(1),
        envelope: int | Literal["none", "instant", "peak", "peak+instant"] | Default = Default(0),
        filter: int
        | Literal["lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"]
        | Default = Default(0),
        graticule: int | Literal["none", "green", "orange", "invert"] | Default = Default(0),
        opacity: float | int | str = Default(0.75),
        flags: str | Literal["numbers", "dots"] | Default = Default(1),
        scale: int | Literal["digital", "millivolts", "ire"] | Default = Default(0),
        bgopacity: float | int | str = Default(0.75),
        tint0: float | int | str = Default(0.0),
        tint1: float | int | str = Default(0.0),
        fitmode: int | Literal["none", "size"] | Default = Default(0),
        input: int | Literal["all", "first"] | Default = Default(1),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Video waveform monitor.

        Parameters:
        ----------

        :param int mode: Can be either row, or column. Default is column. In row mode, the graph on the left side represents color component value 0 and the right side represents value = 255. In column mode, the top side represents color component value = 0 and bottom side represents value = 255.
        :param float intensity: Set intensity. Smaller values are useful to find out how many values of the same luminance are distributed across input rows/columns. Default value is 0.04. Allowed range is [0, 1].
        :param bool mirror: Set mirroring mode. 0 means unmirrored, 1 means mirrored. In mirrored mode, higher values will be represented on the left side for row mode and at the top for column mode. Default is 1 (mirrored).
        :param int display: Set display mode. It accepts the following values: ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. This display mode makes it easier to spot relative differences or similarities in overlapping areas of the color components that are supposed to be identical, such as neutral whites, grays, or blacks. ‘stack’ Display separate graph for the color components side by side in row mode or one below the other in column mode. ‘parade’ Display separate graph for the color components side by side in column mode or one below the other in row mode. Using this display mode makes it easy to spot color casts in the highlights and shadows of an image, by comparing the contours of the top and the bottom graphs of each waveform. Since whites, grays, and blacks are characterized by exactly equal amounts of red, green, and blue, neutral areas of the picture should display three waveforms of roughly equal width/height. If not, the correction is easy to perform by making level adjustments the three waveforms. Default is stack.
        :param int components: Set which color components to display. Default is 1, which means only luma or red color component if input is in RGB colorspace. If is set for example to 7 it will display all 3 (if) available color components.
        :param int envelope: ‘none’ No envelope, this is default. ‘instant’ Instant envelope, minimum and maximum values presented in graph will be easily visible even with small step value. ‘peak’ Hold minimum and maximum values presented in graph across time. This way you can still spot out of range values without constantly looking at waveforms. ‘peak+instant’ Peak and instant envelope combined together.
        :param int filter: ‘lowpass’ No filtering, this is default. ‘flat’ Luma and chroma combined together. ‘aflat’ Similar as above, but shows difference between blue and red chroma. ‘xflat’ Similar as above, but use different colors. ‘yflat’ Similar as above, but again with different colors. ‘chroma’ Displays only chroma. ‘color’ Displays actual color value on waveform. ‘acolor’ Similar as above, but with luma showing frequency of chroma values.
        :param int graticule: Set which graticule to display. ‘none’ Do not display graticule. ‘green’ Display green graticule showing legal broadcast ranges. ‘orange’ Display orange graticule showing legal broadcast ranges. ‘invert’ Display invert graticule showing legal broadcast ranges.
        :param float opacity: Set graticule opacity.
        :param str flags: Set graticule flags. ‘numbers’ Draw numbers above lines. By default enabled. ‘dots’ Draw dots instead of lines.
        :param int scale: Set scale used for displaying graticule. ‘digital’ ‘millivolts’ ‘ire’ Default is digital.
        :param float bgopacity: Set background opacity.
        :param float tint0: Set tint for output. Only used with lowpass filter and when display is not overlay and input pixel formats are not RGB.
        :param float tint1: Set tint for output. Only used with lowpass filter and when display is not overlay and input pixel formats are not RGB.
        :param int fitmode: Set sample aspect ratio of video output frames. Can be used to configure waveform so it is not streched too much in one of directions. ‘none’ Set sample aspect ration to 1/1. ‘size’ Set sample aspect ratio to match input size of video Default is ‘none’.
        :param int input: Set input formats for filter to pick from. Can be ‘all’, for selecting from all available formats, or ‘first’, for selecting first available format. Default is ‘first’.

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
                        "input": input,
                    }
                    | kwargs
                ).items()
            ),
        )
        return filter_node.video(0)

    def weave(
        self, *, first_field: int | Literal["top", "t", "bottom", "b"] | Default = Default(0), **kwargs: Any
    ) -> "VideoStream":
        """

        Weave input video fields into frames.

        Parameters:
        ----------

        :param int first_field: Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.

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

    def xbr(self, *, n: int | str = Default(3), **kwargs: Any) -> "VideoStream":
        """

        Scale the input using xBR algorithm.

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for 2xBR, 3 for 3xBR and 4 for 4xBR. Default is 3.

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
        planes: int | str = Default(7),
        secondary: int | Literal["first", "all"] | Default = Default(1),
        enable: str | float | int = Default(None),
        eof_action: str | Literal["repeat", "endall", "pass"] | Default = Default("repeat"),
        shortest: bool | int | str = Default(0),
        repeatlast: bool | int | str = Default(1),
        ts_sync_mode: str | Literal["default", "nearest"] | Default = Default("default"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Cross-correlate first video stream with second video stream.

        Parameters:
        ----------

        :param int planes: Set which planes to process.
        :param int secondary: Set which secondary video frames will be processed from second input video stream, can be first or all. Default is all.
        :param str enable: timeline editing
        :param str eof_action: The action to take when EOF is encountered on the secondary input; it accepts one of the following values
        :param bool shortest: Force the output to terminate when the shortest input terminates.
        :param bool repeatlast: force the filter to extend the last frame of secondary streams until the end of the primary stream.
        :param str ts_sync_mode: How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:

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
                        "enable": enable,
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

    def xfade(
        self,
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
        | Default = Default("FADE"),
        duration: int | str = Default(1000000),
        offset: int | str = Default(0),
        expr: str | float | int = Default("((void*)0)"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Cross fade one video with another video.

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

    def xfade_opencl(
        self,
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
        **kwargs: Any,
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
                self,
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

    def yadif(
        self,
        *,
        mode: int
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("YADIF_MODE_SEND_FRAME"),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default("YADIF_PARITY_AUTO"),
        deint: int | Literal["all", "interlaced"] | Default = Default("YADIF_DEINT_ALL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Deinterlace the input image.

        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. 2, send_frame_nospatial Like send_frame, but it skips the spatial interlacing check. 3, send_field_nospatial Like send_field, but it skips the spatial interlacing check. The default value is send_frame.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.
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

    def yadif_cuda(
        self,
        *,
        mode: int
        | Literal["send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"]
        | Default = Default("YADIF_MODE_SEND_FRAME"),
        parity: int | Literal["tff", "bff", "auto"] | Default = Default("YADIF_PARITY_AUTO"),
        deint: int | Literal["all", "interlaced"] | Default = Default("YADIF_DEINT_ALL"),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        ### 11.292 yadif_cuda

        Deinterlace the input video using the yadif algorithm, but implemented in CUDA
        so that it can work as part of a GPU accelerated pipeline with nvdec and/or
        nvenc.

        It accepts the following parameters:

        **mode**

            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. 2, send_frame_nospatial Like send_frame, but it skips the spatial interlacing check. 3, send_field_nospatial Like send_field, but it skips the spatial interlacing check. The default value is send_frame.

        **parity**

            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.

        **deint**

            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. 2, send_frame_nospatial Like send_frame, but it skips the spatial interlacing check. 3, send_field_nospatial Like send_field, but it skips the spatial interlacing check. The default value is send_frame.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.
        :param str enable: timeline editing

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yadif_005fcuda

        """
        filter_node = FilterNode(
            name="yadif_cuda",
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
        radius: int | str = Default(3),
        planes: int | str = Default(1),
        sigma: int | str = Default(128),
        enable: str | float | int = Default(None),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Yet another edge preserving blur filter.

        Parameters:
        ----------

        :param int radius: Set the window radius. Default value is 3.
        :param int planes: Set which planes to filter. Default is only the first plane.
        :param int sigma: Set blur strength. Default value is 128.
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

    def zmq(self, *, bind_address: str | float | int = Default("tcp://*:5555"), **kwargs: Any) -> "VideoStream":
        """

        Receive commands through ZMQ and broker them to filters.

        Parameters:
        ----------

        :param str bind_address: set bind address

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
        zoom: str | float | int = Default("1"),
        x: str | float | int = Default("0"),
        y: str | float | int = Default("0"),
        d: str | float | int = Default("90"),
        s: str | float | int = Default("hd720"),
        fps: str | float | int = Default("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply Zoom & Pan effect.

        Parameters:
        ----------

        :param str zoom: Set the zoom expression. Range is 1-10. Default is 1.
        :param str x: Set the x and y expression. Default is 0.
        :param str y: Set the x and y expression. Default is 0.
        :param str d: Set the duration expression in number of frames. This sets for how many number of frames effect will last for single input image. Default is 90.
        :param str s: Set the output image size, default is ’hd720’.
        :param str fps: Set the output frame rate, default is ’25’.

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
        w: str | float | int = Default(None),
        h: str | float | int = Default(None),
        size: str | float | int = Default("((void*)0)"),
        dither: int | Literal["none", "ordered", "random", "error_diffusion"] | Default = Default(0),
        filter: int
        | Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | Default = Default("ZIMG_RESIZE_BILINEAR"),
        out_range: int | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default(-1),
        primaries: int
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
        | Default = Default(-1),
        transfer: int
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
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | Default = Default(-1),
        matrix: int
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
        | Default = Default(-1),
        in_range: int | Literal["input", "limited", "full", "unknown", "tv", "pc"] | Default = Default(-1),
        primariesin: int
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
        | Default = Default(-1),
        transferin: int
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
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | Default = Default(-1),
        matrixin: int
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
        | Default = Default(-1),
        chromal: int
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default(-1),
        chromalin: int
        | Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | Default = Default(-1),
        npl: float | int | str = Default('__builtin_nanf("0x7fc00000")'),
        agamma: bool | int | str = Default(1),
        param_a: float | int | str = Default('__builtin_nanf("0x7fc00000")'),
        param_b: float | int | str = Default('__builtin_nanf("0x7fc00000")'),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        Apply resizing, colorspace and bit depth conversion.

        Parameters:
        ----------

        :param str w: Output video width
        :param str h: Output video height
        :param str size: set video size
        :param int dither: set dither type
        :param int filter: set filter type
        :param int out_range: set color range
        :param int primaries: set color primaries
        :param int transfer: set transfer characteristic
        :param int matrix: set colorspace matrix
        :param int in_range: set input color range
        :param int primariesin: set input color primaries
        :param int transferin: set input transfer characteristic
        :param int matrixin: set input colorspace matrix
        :param int chromal: set output chroma location
        :param int chromalin: set input chroma location
        :param float npl: set nominal peak luminance
        :param bool agamma: allow approximate gamma
        :param float param_a: parameter A, which is parameter \"b\" for bicubic, and the number of filter taps for lanczos
        :param float param_b: parameter B, which is parameter \"c\" for bicubic

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
