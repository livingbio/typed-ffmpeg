from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from ..base import FilterableStream, FilterNode
from ..schema import DefaultFloat, DefaultInt, DefaultStr, StreamType

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
        rate: str | DefaultStr = DefaultStr("25"),
        size: str | DefaultStr = DefaultStr("hd720"),
        fov: float | DefaultStr = DefaultStr("90.f"),
        roll: float | DefaultStr = DefaultStr("0.f"),
        pitch: float | DefaultStr = DefaultStr("0.f"),
        yaw: float | DefaultStr = DefaultStr("0.f"),
        xzoom: float | DefaultStr = DefaultStr("1.f"),
        yzoom: float | DefaultStr = DefaultStr("1.f"),
        zzoom: float | DefaultStr = DefaultStr("1.f"),
        xpos: float | DefaultStr = DefaultStr("0.f"),
        ypos: float | DefaultStr = DefaultStr("0.f"),
        zpos: float | DefaultStr = DefaultStr("0.f"),
        length: int | DefaultInt = DefaultInt(15),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.1 a3dscope
        Convert input audio to 3d scope video output.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str rate: Set frame rate, expressed as number of frames per second. Default value is "25".
        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is hd720.
        :param float fov: Set the camera field of view. Default is 90 degrees. Allowed range is from 40 to 150.
        :param float roll: Set the camera roll.
        :param float pitch: Set the camera pitch.
        :param float yaw: Set the camera yaw.
        :param float xzoom: Set the camera zoom on X-axis.
        :param float yzoom: Set the camera zoom on Y-axis.
        :param float zzoom: Set the camera zoom on Z-axis.
        :param float xpos: Set the camera position on X-axis.
        :param float ypos: Set the camera position on Y-axis.
        :param float zpos: Set the camera position on Z-axis.
        :param int length: Set the length of displayed audio waves in number of frames.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#a3dscope

        """
        filter_node = FilterNode(
            name="a3dscope",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "rate": rate,
                "size": size,
                "fov": fov,
                "roll": roll,
                "pitch": pitch,
                "yaw": yaw,
                "xzoom": xzoom,
                "yzoom": yzoom,
                "zzoom": zzoom,
                "xpos": xpos,
                "ypos": ypos,
                "zpos": zpos,
                "length": length,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def aap(
        self,
        _desired: "AudioStream",
        *,
        order: int | DefaultInt = DefaultInt(16),
        projection: int | DefaultInt = DefaultInt(2),
        mu: float | DefaultFloat = DefaultFloat(0.0001),
        delta: float | DefaultFloat = DefaultFloat(0.001),
        out_mode: int | DefaultStr = DefaultStr("OUT_MODE"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def abench(self, *, action: int | DefaultStr = DefaultStr("ACTION_START"), **kwargs: Any) -> "AudioStream":
        """

        18.8 bench, abench
        Benchmark part of a filtergraph.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int action: Start or stop a timer. Available values are: ‘start’ Get the current time, set it as frame metadata (using the key lavfi.bench.start_time), and forward the frame to the next filter. ‘stop’ Get the current time and fetch the lavfi.bench.start_time metadata from the input frame metadata to get the time difference. Time difference, average, maximum and minimum time (respectively t, avg, max and min) are then printed. The timestamps are expressed in seconds.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench

        """
        filter_node = FilterNode(
            name="abench",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "action": action,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def abitscope(
        self,
        *,
        rate: str | DefaultStr = DefaultStr("25"),
        size: str | DefaultStr = DefaultStr("1024x256"),
        colors: str | DefaultStr = DefaultStr("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        mode: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.2 abitscope
        Convert input audio to a video output, displaying the audio bit scope.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str rate: Set frame rate, expressed as number of frames per second. Default value is "25".
        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 1024x256.
        :param str colors: Specify list of colors separated by space or by ’|’ which will be used to draw channels. Unrecognized or missing colors will be replaced by white color.
        :param int mode: Set output mode. Can be bars or trace. Default is bars.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#abitscope

        """
        filter_node = FilterNode(
            name="abitscope",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "rate": rate,
                "size": size,
                "colors": colors,
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def acompressor(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(0),
        threshold: float | DefaultFloat = DefaultFloat(0.125),
        ratio: float | DefaultFloat = DefaultFloat(2.0),
        attack: float | DefaultFloat = DefaultFloat(20.0),
        release: float | DefaultFloat = DefaultFloat(250.0),
        makeup: float | DefaultFloat = DefaultFloat(1.0),
        knee: float | DefaultFloat = DefaultFloat(2.82843),
        link: int | DefaultInt = DefaultInt(0),
        detection: int | DefaultInt = DefaultInt(1),
        level_sc: float | DefaultFloat = DefaultFloat(1.0),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.2 acompressor
        A compressor is mainly used to reduce the dynamic range of a signal.
        Especially modern music is mostly compressed at a high ratio to
        improve the overall loudness. It’s done to get the highest attention
        of a listener, "fatten" the sound and bring more "power" to the track.
        If a signal is compressed too much it may sound dull or "dead"
        afterwards or it may start to "pump" (which could be a powerful effect
        but can also destroy a track completely).
        The right compression is the key to reach a professional sound and is
        the high art of mixing and mastering. Because of its complex settings
        it may take a long time to get the right feeling for this kind of effect.

        Compression is done by detecting the volume above a chosen level
        threshold and dividing it by the factor set with ratio.
        So if you set the threshold to -12dB and your signal reaches -6dB a ratio
        of 2:1 will result in a signal at -9dB. Because an exact manipulation of
        the signal would cause distortion of the waveform the reduction can be
        levelled over the time. This is done by setting "Attack" and "Release".
        attack determines how long the signal has to rise above the threshold
        before any reduction will occur and release sets the time the signal
        has to fall below the threshold to reduce the reduction again. Shorter signals
        than the chosen attack time will be left untouched.
        The overall reduction of the signal can be made up afterwards with the
        makeup setting. So compressing the peaks of a signal about 6dB and
        raising the makeup to this level results in a signal twice as loud than the
        source. To gain a softer entry in the compression the knee flattens the
        hard edge at the threshold in the range of the chosen decibels.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input gain. Default is 1. Range is between 0.015625 and 64.
        :param int mode: Set mode of compressor operation. Can be upward or downward. Default is downward.
        :param float threshold: If a signal of stream rises above this level it will affect the gain reduction. By default it is 0.125. Range is between 0.00097563 and 1.
        :param float ratio: Set a ratio by which the signal is reduced. 1:2 means that if the level rose 4dB above the threshold, it will be only 2dB above after the reduction. Default is 2. Range is between 1 and 20.
        :param float attack: Amount of milliseconds the signal has to rise above the threshold before gain reduction starts. Default is 20. Range is between 0.01 and 2000.
        :param float release: Amount of milliseconds the signal has to fall below the threshold before reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
        :param float makeup: Set the amount by how much signal will be amplified after processing. Default is 1. Range is from 1 to 64.
        :param float knee: Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.82843. Range is between 1 and 8.
        :param int link: Choose if the average level between all channels of input stream or the louder(maximum) channel of input stream affects the reduction. Default is average.
        :param int detection: Should the exact signal be taken in case of peak or an RMS one in case of rms. Default is rms which is mostly smoother.
        :param float level_sc: None
        :param float mix: How much to use compressed signal in output. Default is 1. Range is between 0 and 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acompressor

        """
        filter_node = FilterNode(
            name="acompressor",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def acontrast(self, *, contrast: float | DefaultFloat = DefaultFloat(33.0), **kwargs: Any) -> "AudioStream":
        """

        8.3 acontrast
        Simple audio dynamic range compression/expansion filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float contrast: Set contrast. Default is 33. Allowed range is between 0 and 100.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acontrast

        """
        filter_node = FilterNode(
            name="acontrast",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "contrast": contrast,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def acopy(self, **kwargs: Any) -> "AudioStream":
        """

        8.4 acopy
        Copy the input audio source unchanged to the output. This is mainly useful for
        testing purposes.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#acopy

        """
        filter_node = FilterNode(
            name="acopy",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def acrossfade(
        self,
        _crossfade1: "AudioStream",
        *,
        nb_samples: int | DefaultInt = DefaultInt(44100),
        duration: int | DefaultInt = DefaultInt(0),
        overlap: bool | DefaultInt = DefaultInt(1),
        curve1: int | DefaultStr = DefaultStr("TRI"),
        curve2: int | DefaultStr = DefaultStr("TRI"),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def acrossover(
        self,
        *,
        split: str | DefaultStr = DefaultStr("500"),
        order: int | DefaultInt = DefaultInt(1),
        level: float | DefaultFloat = DefaultFloat(1.0),
        gain: str | DefaultStr = DefaultStr("1.f"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> FilterNode:
        """

        8.6 acrossover
        Split audio stream into several bands.

        This filter splits audio stream into two or more frequency ranges.
        Summing all streams back will give flat output.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str split: Set split frequencies. Those must be positive and increasing.
        :param int order: Set filter order for each band split. This controls filter roll-off or steepness of filter transfer function. Available values are: ‘2nd’ 12 dB per octave. ‘4th’ 24 dB per octave. ‘6th’ 36 dB per octave. ‘8th’ 48 dB per octave. ‘10th’ 60 dB per octave. ‘12th’ 72 dB per octave. ‘14th’ 84 dB per octave. ‘16th’ 96 dB per octave. ‘18th’ 108 dB per octave. ‘20th’ 120 dB per octave. Default is 4th.
        :param float level: Set input gain level. Allowed range is from 0 to 1. Default value is 1.
        :param str gain: None
        :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format. Default value is auto.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossover

        """
        filter_node = FilterNode(
            name="acrossover",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] * len(re.split(r"[ |]+", split)),
            inputs=[
                self,
            ],
            kwargs={
                "split": split,
                "order": order,
                "level": level,
                "gain": gain,
                "precision": precision,
            }
            | kwargs,
        )

        return filter_node

    def acrusher(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        bits: float | DefaultFloat = DefaultFloat(8.0),
        mix: float | DefaultFloat = DefaultFloat(0.5),
        mode: int | DefaultInt = DefaultInt(0),
        dc: float | DefaultFloat = DefaultFloat(1.0),
        aa: float | DefaultFloat = DefaultFloat(0.5),
        samples: float | DefaultFloat = DefaultFloat(1.0),
        lfo: bool | DefaultInt = DefaultInt(0),
        lforange: float | DefaultFloat = DefaultFloat(20.0),
        lforate: float | DefaultFloat = DefaultFloat(0.3),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.7 acrusher
        Reduce audio bit resolution.

        This filter is bit crusher with enhanced functionality. A bit crusher
        is used to audibly reduce number of bits an audio signal is sampled
        with. This doesn’t change the bit depth at all, it just produces the
        effect. Material reduced in bit depth sounds more harsh and "digital".
        This filter is able to even round to continuous values instead of discrete
        bit depths.
        Additionally it has a D/C offset which results in different crushing of
        the lower and the upper half of the signal.
        An Anti-Aliasing setting is able to produce "softer" crushing sounds.

        Another feature of this filter is the logarithmic mode.
        This setting switches from linear distances between bits to logarithmic ones.
        The result is a much more "natural" sounding crusher which doesn’t gate low
        signals for example. The human ear has a logarithmic perception,
        so this kind of crushing is much more pleasant.
        Logarithmic crushing is also able to get anti-aliased.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set level in.
        :param float level_out: Set level out.
        :param float bits: Set bit reduction.
        :param float mix: Set mixing amount.
        :param int mode: Can be linear: lin or logarithmic: log.
        :param float dc: Set DC.
        :param float aa: Set anti-aliasing.
        :param float samples: Set sample reduction.
        :param bool lfo: Enable LFO. By default disabled.
        :param float lforange: Set LFO range.
        :param float lforate: Set LFO rate.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrusher

        """
        filter_node = FilterNode(
            name="acrusher",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def acue(
        self,
        *,
        cue: int | DefaultInt = DefaultInt(0),
        preroll: int | DefaultInt = DefaultInt(0),
        buffer: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.8 acue
        Delay audio filtering until a given wallclock timestamp. See the cue
        filter.

        Parameters:
        ----------

        :param int cue: None
        :param int preroll: None
        :param int buffer: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acue

        """
        filter_node = FilterNode(
            name="acue",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adeclick(
        self,
        *,
        window: float | DefaultFloat = DefaultFloat(55.0),
        overlap: float | DefaultFloat = DefaultFloat(75.0),
        arorder: float | DefaultFloat = DefaultFloat(2.0),
        threshold: float | DefaultFloat = DefaultFloat(2.0),
        burst: float | DefaultFloat = DefaultFloat(2.0),
        method: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.9 adeclick
        Remove impulsive noise from input audio.

        Samples detected as impulsive noise are replaced by interpolated samples using
        autoregressive modelling.

        Parameters:
        ----------

        :param float window: Set window size, in milliseconds. Allowed range is from 10 to 100. Default value is 55 milliseconds. This sets size of window which will be processed at once.
        :param float overlap: Set window overlap, in percentage of window size. Allowed range is from 50 to 95. Default value is 75 percent. Setting this to a very high value increases impulsive noise removal but makes whole process much slower.
        :param float arorder: Set autoregression order, in percentage of window size. Allowed range is from 0 to 25. Default value is 2 percent. This option also controls quality of interpolated samples using neighbour good samples.
        :param float threshold: Set threshold value. Allowed range is from 1 to 100. Default value is 2. This controls the strength of impulsive noise which is going to be removed. The lower value, the more samples will be detected as impulsive noise.
        :param float burst: Set burst fusion, in percentage of window size. Allowed range is 0 to 10. Default value is 2. If any two samples detected as noise are spaced less than this value then any sample between those two samples will be also detected as noise.
        :param int method: Set overlap method. It accepts the following values: add, a Select overlap-add method. Even not interpolated samples are slightly changed with this method. save, s Select overlap-save method. Not interpolated samples remain unchanged. Default value is a.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclick

        """
        filter_node = FilterNode(
            name="adeclick",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "burst": burst,
                "method": method,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adeclip(
        self,
        *,
        window: float | DefaultFloat = DefaultFloat(55.0),
        overlap: float | DefaultFloat = DefaultFloat(75.0),
        arorder: float | DefaultFloat = DefaultFloat(8.0),
        threshold: float | DefaultFloat = DefaultFloat(10.0),
        hsize: int | DefaultInt = DefaultInt(1000),
        method: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.10 adeclip
        Remove clipped samples from input audio.

        Samples detected as clipped are replaced by interpolated samples using
        autoregressive modelling.

        Parameters:
        ----------

        :param float window: Set window size, in milliseconds. Allowed range is from 10 to 100. Default value is 55 milliseconds. This sets size of window which will be processed at once.
        :param float overlap: Set window overlap, in percentage of window size. Allowed range is from 50 to 95. Default value is 75 percent.
        :param float arorder: Set autoregression order, in percentage of window size. Allowed range is from 0 to 25. Default value is 8 percent. This option also controls quality of interpolated samples using neighbour good samples.
        :param float threshold: Set threshold value. Allowed range is from 1 to 100. Default value is 10. Higher values make clip detection less aggressive.
        :param int hsize: Set size of histogram used to detect clips. Allowed range is from 100 to 9999. Default value is 1000. Higher values make clip detection less aggressive.
        :param int method: Set overlap method. It accepts the following values: add, a Select overlap-add method. Even not interpolated samples are slightly changed with this method. save, s Select overlap-save method. Not interpolated samples remain unchanged. Default value is a.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclip

        """
        filter_node = FilterNode(
            name="adeclip",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "hsize": hsize,
                "method": method,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adecorrelate(
        self, *, stages: int | DefaultInt = DefaultInt(6), seed: int | DefaultInt = DefaultInt(-1), **kwargs: Any
    ) -> "AudioStream":
        """

        8.11 adecorrelate
        Apply decorrelation to input audio stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int stages: Set decorrelation stages of filtering. Allowed range is from 1 to 16. Default value is 6.
        :param int seed: Set random seed used for setting delay in samples across channels.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adecorrelate

        """
        filter_node = FilterNode(
            name="adecorrelate",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "stages": stages,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adelay(self, *, delays: str, all: bool | DefaultInt = DefaultInt(0), **kwargs: Any) -> "AudioStream":
        """

        8.12 adelay
        Delay one or more audio channels.

        Samples in delayed channel are filled with silence.

        The filter accepts the following option:

        Parameters:
        ----------

        :param str delays: Set list of delays in milliseconds for each channel separated by ’|’. Unused delays will be silently ignored. If number of given delays is smaller than number of channels all remaining channels will not be delayed. If you want to delay exact number of samples, append ’S’ to number. If you want instead to delay in seconds, append ’s’ to number.
        :param bool all: Use last set delay for all remaining channels. By default is disabled. This option if enabled changes how option delays is interpreted.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adelay

        """
        filter_node = FilterNode(
            name="adelay",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "delays": delays,
                "all": all,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adenorm(
        self,
        *,
        level: float | DefaultFloat = DefaultFloat(-351.0),
        type: int | DefaultStr = DefaultStr("DC_TYPE"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.13 adenorm
        Remedy denormals in audio by adding extremely low-level noise.

        This filter shall be placed before any filter that can produce denormals.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param float level: Set level of added noise in dB. Default is -351. Allowed range is from -451 to -90.
        :param int type: Set type of added noise. dc Add DC signal. ac Add AC signal. square Add square signal. pulse Add pulse signal. Default is dc.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adenorm

        """
        filter_node = FilterNode(
            name="adenorm",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "level": level,
                "type": type,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aderivative(self, **kwargs: Any) -> "AudioStream":
        """

        8.14 aderivative, aintegral
        Compute derivative/integral of audio stream.

        Applying both filters one after another produces original audio.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        filter_node = FilterNode(
            name="aderivative",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def adrawgraph(
        self,
        *,
        m1: str | DefaultStr = DefaultStr(""),
        fg1: str | DefaultStr = DefaultStr("0xffff0000"),
        m2: str | DefaultStr = DefaultStr(""),
        fg2: str | DefaultStr = DefaultStr("0xff00ff00"),
        m3: str | DefaultStr = DefaultStr(""),
        fg3: str | DefaultStr = DefaultStr("0xffff00ff"),
        m4: str | DefaultStr = DefaultStr(""),
        fg4: str | DefaultStr = DefaultStr("0xffffff00"),
        bg: str | DefaultStr = DefaultStr("white"),
        min: float | DefaultFloat = DefaultFloat(-1.0),
        max: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(2),
        slide: int | DefaultInt = DefaultInt(0),
        size: str | DefaultStr = DefaultStr("900x256"),
        rate: str | DefaultStr = DefaultStr("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.3 adrawgraph
        Draw a graph using input audio metadata.

        See drawgraph

        Parameters:
        ----------

        :param str m1: None
        :param str fg1: None
        :param str m2: None
        :param str fg2: None
        :param str m3: None
        :param str fg3: None
        :param str m4: None
        :param str fg4: None
        :param str bg: None
        :param float min: None
        :param float max: None
        :param int mode: None
        :param int slide: None
        :param str size: None
        :param str rate: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adrawgraph

        """
        filter_node = FilterNode(
            name="adrawgraph",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def adrc(
        self,
        *,
        transfer: str | DefaultStr = DefaultStr("p"),
        attack: float | DefaultFloat = DefaultFloat(50.0),
        release: float | DefaultFloat = DefaultFloat(100.0),
        channels: str | DefaultStr = DefaultStr("all"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.15 adrc
        Apply spectral dynamic range controller filter to input audio stream.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param str transfer: Set the transfer expression. The expression can contain the following constants: ch current channel number sn current sample number nb_channels number of channels t timestamp expressed in seconds sr sample rate p current frequency power value, in dB f current frequency in Hz Default value is p.
        :param float attack: Set the attack in milliseconds. Default is 50 milliseconds. Allowed range is from 1 to 1000 milliseconds.
        :param float release: Set the release in milliseconds. Default is 100 milliseconds. Allowed range is from 5 to 2000 milliseconds.
        :param str channels: Set which channels to filter, by default all channels in audio stream are filtered.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adrc

        """
        filter_node = FilterNode(
            name="adrc",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "transfer": transfer,
                "attack": attack,
                "release": release,
                "channels": channels,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adynamicequalizer(
        self,
        *,
        threshold: float | DefaultFloat = DefaultFloat(0.0),
        dfrequency: float | DefaultFloat = DefaultFloat(1000.0),
        dqfactor: float | DefaultFloat = DefaultFloat(1.0),
        tfrequency: float | DefaultFloat = DefaultFloat(1000.0),
        tqfactor: float | DefaultFloat = DefaultFloat(1.0),
        attack: float | DefaultFloat = DefaultFloat(20.0),
        release: float | DefaultFloat = DefaultFloat(200.0),
        ratio: float | DefaultFloat = DefaultFloat(1.0),
        makeup: float | DefaultFloat = DefaultFloat(0.0),
        range: float | DefaultFloat = DefaultFloat(50.0),
        mode: int | DefaultInt = DefaultInt(0),
        dftype: int | DefaultInt = DefaultInt(0),
        tftype: int | DefaultInt = DefaultInt(0),
        auto: int | DefaultStr = DefaultStr("DET_OFF"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.16 adynamicequalizer
        Apply dynamic equalization to input audio stream.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param float threshold: Set the detection threshold used to trigger equalization. Threshold detection is using detection filter. Default value is 0. Allowed range is from 0 to 100.
        :param float dfrequency: Set the detection frequency in Hz used for detection filter used to trigger equalization. Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
        :param float dqfactor: Set the detection resonance factor for detection filter used to trigger equalization. Default value is 1. Allowed range is from 0.001 to 1000.
        :param float tfrequency: Set the target frequency of equalization filter. Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
        :param float tqfactor: Set the target resonance factor for target equalization filter. Default value is 1. Allowed range is from 0.001 to 1000.
        :param float attack: Set the amount of milliseconds the signal from detection has to rise above the detection threshold before equalization starts. Default is 20. Allowed range is between 1 and 2000.
        :param float release: Set the amount of milliseconds the signal from detection has to fall below the detection threshold before equalization ends. Default is 200. Allowed range is between 1 and 2000.
        :param float ratio: Set the ratio by which the equalization gain is raised. Default is 1. Allowed range is between 0 and 30.
        :param float makeup: Set the makeup offset by which the equalization gain is raised. Default is 0. Allowed range is between 0 and 100.
        :param float range: Set the max allowed cut/boost amount. Default is 50. Allowed range is from 1 to 200.
        :param int mode: Set the mode of filter operation, can be one of the following: ‘listen’ Output only isolated detection signal. ‘cutbelow’ Cut frequencies below detection threshold. ‘cutabove’ Cut frequencies above detection threshold. ‘boostbelow’ Boost frequencies below detection threshold. ‘boostabove’ Boost frequencies above detection threshold. Default mode is ‘cutbelow’.
        :param int dftype: Set the type of detection filter, can be one of the following: ‘bandpass’ ‘lowpass’ ‘highpass’ ‘peak’ Default type is ‘bandpass’.
        :param int tftype: Set the type of target filter, can be one of the following: ‘bell’ ‘lowshelf’ ‘highshelf’ Default type is ‘bell’.
        :param int auto: Automatically gather threshold from detection filter. By default is ‘disabled’. This option is useful to detect threshold in certain time frame of input audio stream, in such case option value is changed at runtime. Available values are: ‘disabled’ Disable using automatically gathered threshold value. ‘off’ Stop picking threshold value. ‘on’ Start picking threshold value. ‘adaptive’ Adaptively pick threshold value, by calculating sliding window entropy.
        :param int precision: Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer

        """
        filter_node = FilterNode(
            name="adynamicequalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
                "auto": auto,
                "precision": precision,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def adynamicsmooth(
        self,
        *,
        sensitivity: float | DefaultFloat = DefaultFloat(2.0),
        basefreq: float | DefaultFloat = DefaultFloat(22050.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.17 adynamicsmooth
        Apply dynamic smoothing to input audio stream.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param float sensitivity: Set an amount of sensitivity to frequency fluctations. Default is 2. Allowed range is from 0 to 1e+06.
        :param float basefreq: Set a base frequency for smoothing. Default value is 22050. Allowed range is from 2 to 1e+06.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth

        """
        filter_node = FilterNode(
            name="adynamicsmooth",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sensitivity": sensitivity,
                "basefreq": basefreq,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aecho(
        self,
        *,
        in_gain: float | DefaultFloat = DefaultFloat(0.6),
        out_gain: float | DefaultFloat = DefaultFloat(0.3),
        delays: str | DefaultStr = DefaultStr("1000"),
        decays: str | DefaultStr = DefaultStr("0.5"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.18 aecho
        Apply echoing to the input audio.

        Echoes are reflected sound and can occur naturally amongst mountains
        (and sometimes large buildings) when talking or shouting; digital echo
        effects emulate this behaviour and are often used to help fill out the
        sound of a single instrument or vocal. The time difference between the
        original signal and the reflection is the delay, and the
        loudness of the reflected signal is the decay.
        Multiple echoes can have different delays and decays.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param float in_gain: Set input gain of reflected signal. Default is 0.6.
        :param float out_gain: Set output gain of reflected signal. Default is 0.3.
        :param str delays: Set list of time intervals in milliseconds between original signal and reflections separated by ’|’. Allowed range for each delay is (0 - 90000.0]. Default is 1000.
        :param str decays: Set list of loudness of reflected signals separated by ’|’. Allowed range for each decay is (0 - 1.0]. Default is 0.5.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aecho

        """
        filter_node = FilterNode(
            name="aecho",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aemphasis(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(0),
        type: int | DefaultInt = DefaultInt(4),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.19 aemphasis
        Audio emphasis filter creates or restores material directly taken from LPs or
        emphased CDs with different filter curves. E.g. to store music on vinyl the
        signal has to be altered by a filter first to even out the disadvantages of
        this recording medium.
        Once the material is played back the inverse filter has to be applied to
        restore the distortion of the frequency response.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input gain.
        :param float level_out: Set output gain.
        :param int mode: Set filter mode. For restoring material use reproduction mode, otherwise use production mode. Default is reproduction mode.
        :param int type: Set filter type. Selects medium. Can be one of the following: col select Columbia. emi select EMI. bsi select BSI (78RPM). riaa select RIAA. cd select Compact Disc (CD). 50fm select 50µs (FM). 75fm select 75µs (FM). 50kf select 50µs (FM-KF). 75kf select 75µs (FM-KF).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aemphasis

        """
        filter_node = FilterNode(
            name="aemphasis",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "type": type,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aeval(self, *, exprs: str, channel_layout: str, **kwargs: Any) -> "AudioStream":
        """

        8.20 aeval
        Modify an audio signal according to the specified expressions.

        This filter accepts one or more expressions (one for each channel),
        which are evaluated and used to modify a corresponding audio signal.

        It accepts the following parameters:


        Each expression in exprs can contain the following constants and functions:


        Note: this filter is slow. For faster processing you should use a
        dedicated filter.

        Parameters:
        ----------

        :param str exprs: Set the ’|’-separated expressions list for each separate channel. If the number of input channels is greater than the number of expressions, the last specified expression is used for the remaining output channels.
        :param str channel_layout: Set output channel layout. If not specified, the channel layout is specified by the number of expressions. If set to ‘same’, it will use by default the same input channel layout.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aeval

        """
        filter_node = FilterNode(
            name="aeval",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "exprs": exprs,
                "channel_layout": channel_layout,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aexciter(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        amount: float | DefaultFloat = DefaultFloat(1.0),
        drive: float | DefaultFloat = DefaultFloat(8.5),
        blend: float | DefaultFloat = DefaultFloat(0.0),
        freq: float | DefaultFloat = DefaultFloat(7500.0),
        ceil: float | DefaultFloat = DefaultFloat(9999.0),
        listen: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.21 aexciter
        An exciter is used to produce high sound that is not present in the
        original signal. This is done by creating harmonic distortions of the
        signal which are restricted in range and added to the original signal.
        An Exciter raises the upper end of an audio signal without simply raising
        the higher frequencies like an equalizer would do to create a more
        "crisp" or "brilliant" sound.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input level prior processing of signal. Allowed range is from 0 to 64. Default value is 1.
        :param float level_out: Set output level after processing of signal. Allowed range is from 0 to 64. Default value is 1.
        :param float amount: Set the amount of harmonics added to original signal. Allowed range is from 0 to 64. Default value is 1.
        :param float drive: Set the amount of newly created harmonics. Allowed range is from 0.1 to 10. Default value is 8.5.
        :param float blend: Set the octave of newly created harmonics. Allowed range is from -10 to 10. Default value is 0.
        :param float freq: Set the lower frequency limit of producing harmonics in Hz. Allowed range is from 2000 to 12000 Hz. Default is 7500 Hz.
        :param float ceil: Set the upper frequency limit of producing harmonics. Allowed range is from 9999 to 20000 Hz. If value is lower than 10000 Hz no limit is applied.
        :param bool listen: Mute the original signal and output only added harmonics. By default is disabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aexciter

        """
        filter_node = FilterNode(
            name="aexciter",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "amount": amount,
                "drive": drive,
                "blend": blend,
                "freq": freq,
                "ceil": ceil,
                "listen": listen,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afade(
        self,
        *,
        type: int | DefaultInt = DefaultInt(0),
        start_sample: int | DefaultInt = DefaultInt(0),
        nb_samples: int | DefaultInt = DefaultInt(44100),
        start_time: int | DefaultInt = DefaultInt(0),
        duration: int | DefaultInt = DefaultInt(0),
        curve: int | DefaultStr = DefaultStr("TRI"),
        silence: float | DefaultFloat = DefaultFloat(0.0),
        unity: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.22 afade
        Apply fade-in/out effect to input audio.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param int type: Specify the effect type, can be either in for fade-in, or out for a fade-out effect. Default is in.
        :param int start_sample: Specify the number of the start sample for starting to apply the fade effect. Default is 0.
        :param int nb_samples: Specify the number of samples for which the fade effect has to last. At the end of the fade-in effect the output audio will have the same volume as the input audio, at the end of the fade-out transition the output audio will be silence. Default is 44100.
        :param int start_time: Specify the start time of the fade effect. Default is 0. The value must be specified as a time duration; see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. If set this option is used instead of start_sample.
        :param int duration: Specify the duration of the fade effect. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. At the end of the fade-in effect the output audio will have the same volume as the input audio, at the end of the fade-out transition the output audio will be silence. By default the duration is determined by nb_samples. If set this option is used instead of nb_samples.
        :param int curve: Set curve for fade transition. It accepts the following values: tri select triangular, linear slope (default) qsin select quarter of sine wave hsin select half of sine wave esin select exponential sine wave log select logarithmic ipar select inverted parabola qua select quadratic cub select cubic squ select square root cbr select cubic root par select parabola exp select exponential iqsin select inverted quarter of sine wave ihsin select inverted half of sine wave dese select double-exponential seat desi select double-exponential sigmoid losi select logistic sigmoid sinc select sine cardinal function isinc select inverted sine cardinal function quat select quartic quatr select quartic root qsin2 select squared quarter of sine wave hsin2 select squared half of sine wave nofade no fade applied
        :param float silence: Set the initial gain for fade-in or final gain for fade-out. Default value is 0.0.
        :param float unity: Set the initial gain for fade-out or final gain for fade-in. Default value is 1.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afade

        """
        filter_node = FilterNode(
            name="afade",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "type": type,
                "start_sample": start_sample,
                "nb_samples": nb_samples,
                "start_time": start_time,
                "duration": duration,
                "curve": curve,
                "silence": silence,
                "unity": unity,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afftdn(
        self,
        *,
        noise_reduction: float | DefaultFloat = DefaultFloat(12.0),
        noise_floor: float | DefaultFloat = DefaultFloat(-50.0),
        noise_type: int | DefaultStr = DefaultStr("WHITE_NOISE"),
        band_noise: str,
        residual_floor: float | DefaultFloat = DefaultFloat(-38.0),
        track_noise: bool | DefaultInt = DefaultInt(0),
        track_residual: bool | DefaultInt = DefaultInt(0),
        output_mode: int | DefaultStr = DefaultStr("OUT_MODE"),
        adaptivity: float | DefaultFloat = DefaultFloat(0.5),
        floor_offset: float | DefaultFloat = DefaultFloat(1.0),
        noise_link: int | DefaultStr = DefaultStr("MIN_LINK"),
        band_multiplier: float | DefaultFloat = DefaultFloat(1.25),
        sample_noise: int | DefaultStr = DefaultStr("SAMPLE_NONE"),
        gain_smooth: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.23 afftdn
        Denoise audio samples with FFT.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param float noise_reduction: Set the noise reduction in dB, allowed range is 0.01 to 97. Default value is 12 dB.
        :param float noise_floor: Set the noise floor in dB, allowed range is -80 to -20. Default value is -50 dB.
        :param int noise_type: Set the noise type. It accepts the following values: white, w Select white noise. vinyl, v Select vinyl noise. shellac, s Select shellac noise. custom, c Select custom noise, defined in bn option. Default value is white noise.
        :param str band_noise: Set custom band noise profile for every one of 15 bands. Bands are separated by ’ ’ or ’|’.
        :param float residual_floor: Set the residual floor in dB, allowed range is -80 to -20. Default value is -38 dB.
        :param bool track_noise: Enable noise floor tracking. By default is disabled. With this enabled, noise floor is automatically adjusted.
        :param bool track_residual: Enable residual tracking. By default is disabled.
        :param int output_mode: Set the output mode. It accepts the following values: input, i Pass input unchanged. output, o Pass noise filtered out. noise, n Pass only noise. Default value is output.
        :param float adaptivity: Set the adaptivity factor, used how fast to adapt gains adjustments per each frequency bin. Value 0 enables instant adaptation, while higher values react much slower. Allowed range is from 0 to 1. Default value is 0.5.
        :param float floor_offset: Set the noise floor offset factor. This option is used to adjust offset applied to measured noise floor. It is only effective when noise floor tracking is enabled. Allowed range is from -2.0 to 2.0. Default value is 1.0.
        :param int noise_link: Set the noise link used for multichannel audio. It accepts the following values: none Use unchanged channel’s noise floor. min Use measured min noise floor of all channels. max Use measured max noise floor of all channels. average Use measured average noise floor of all channels. Default value is min.
        :param float band_multiplier: Set the band multiplier factor, used how much to spread bands across frequency bins. Allowed range is from 0.2 to 5. Default value is 1.25.
        :param int sample_noise: Toggle capturing and measurement of noise profile from input audio. It accepts the following values: start, begin Start sample noise capture. stop, end Stop sample noise capture and measure new noise band profile. Default value is none.
        :param int gain_smooth: Set gain smooth spatial radius, used to smooth gains applied to each frequency bin. Useful to reduce random music noise artefacts. Higher values increases smoothing of gains. Allowed range is from 0 to 50. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftdn

        """
        filter_node = FilterNode(
            name="afftdn",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afftfilt(
        self,
        *,
        real: str | DefaultStr = DefaultStr("re"),
        imag: str | DefaultStr = DefaultStr("im"),
        win_size: int | DefaultInt = DefaultInt(4096),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        overlap: float | DefaultFloat = DefaultFloat(0.75),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.24 afftfilt
        Apply arbitrary expressions to samples in frequency domain.

        Parameters:
        ----------

        :param str real: Set frequency domain real expression for each separate channel separated by ’|’. Default is "re". If the number of input channels is greater than the number of expressions, the last specified expression is used for the remaining output channels.
        :param str imag: Set frequency domain imaginary expression for each separate channel separated by ’|’. Default is "im". Each expression in real and imag can contain the following constants and functions: sr sample rate b current frequency bin number nb number of available bins ch channel number of the current expression chs number of channels pts current frame pts re current real part of frequency bin of current channel im current imaginary part of frequency bin of current channel real(b, ch) Return the value of real part of frequency bin at location (bin,channel) imag(b, ch) Return the value of imaginary part of frequency bin at location (bin,channel)
        :param int win_size: Set window size. Allowed range is from 16 to 131072. Default is 4096
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        :param float overlap: Set window overlap. If set to 1, the recommended overlap for selected window function will be picked. Default is 0.75.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftfilt

        """
        filter_node = FilterNode(
            name="afftfilt",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "real": real,
                "imag": imag,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afifo(self, **kwargs: Any) -> "AudioStream":
        """

        11.96 fifo, afifo
        Buffer input images and send them when they are requested.

        It is mainly useful when auto-inserted by the libavfilter
        framework.

        It does not take parameters.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#fifo_002c-afifo

        """
        filter_node = FilterNode(
            name="afifo",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def aformat(self, *, sample_fmts: str, sample_rates: str, channel_layouts: str, **kwargs: Any) -> "AudioStream":
        """

        8.26 aformat
        Set output format constraints for the input audio. The framework will
        negotiate the most appropriate format to minimize conversions.

        It accepts the following parameters:

        If a parameter is omitted, all values are allowed.

        Force the output to either unsigned 8-bit or signed 16-bit stereo

        aformat=sample_fmts=u8|s16:channel_layouts=stereo

        Parameters:
        ----------

        :param str sample_fmts: A ’|’-separated list of requested sample formats.
        :param str sample_rates: A ’|’-separated list of requested sample rates.
        :param str channel_layouts: A ’|’-separated list of requested channel layouts. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aformat

        """
        filter_node = FilterNode(
            name="aformat",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sample_fmts": sample_fmts,
                "sample_rates": sample_rates,
                "channel_layouts": channel_layouts,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afreqshift(
        self,
        *,
        shift: float | DefaultFloat = DefaultFloat(0.0),
        level: float | DefaultFloat = DefaultFloat(1.0),
        order: int | DefaultInt = DefaultInt(8),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.27 afreqshift
        Apply frequency shift to input audio samples.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float shift: Specify frequency shift. Allowed range is -INT_MAX to INT_MAX. Default value is 0.0.
        :param float level: Set output gain applied to final output. Allowed range is from 0.0 to 1.0. Default value is 1.0.
        :param int order: Set filter order used for filtering. Allowed range is from 1 to 16. Default value is 8.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afreqshift

        """
        filter_node = FilterNode(
            name="afreqshift",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "shift": shift,
                "level": level,
                "order": order,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def afwtdn(
        self,
        *,
        sigma: float | DefaultFloat = DefaultFloat(0.0),
        levels: int | DefaultInt = DefaultInt(10),
        wavet: int | DefaultStr = DefaultStr("SYM10"),
        percent: float | DefaultFloat = DefaultFloat(85.0),
        profile: bool | DefaultInt = DefaultInt(0),
        adaptive: bool | DefaultInt = DefaultInt(0),
        samples: int | DefaultInt = DefaultInt(8192),
        softness: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.28 afwtdn
        Reduce broadband noise from input samples using Wavelets.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param float sigma: Set the noise sigma, allowed range is from 0 to 1. Default value is 0. This option controls strength of denoising applied to input samples. Most useful way to set this option is via decibels, eg. -45dB.
        :param int levels: Set the number of wavelet levels of decomposition. Allowed range is from 1 to 12. Default value is 10. Setting this too low make denoising performance very poor.
        :param int wavet: Set wavelet type for decomposition of input frame. They are sorted by number of coefficients, from lowest to highest. More coefficients means worse filtering speed, but overall better quality. Available wavelets are: ‘sym2’ ‘sym4’ ‘rbior68’ ‘deb10’ ‘sym10’ ‘coif5’ ‘bl3’
        :param float percent: Set percent of full denoising. Allowed range is from 0 to 100 percent. Default value is 85 percent or partial denoising.
        :param bool profile: If enabled, first input frame will be used as noise profile. If first frame samples contain non-noise performance will be very poor.
        :param bool adaptive: If enabled, input frames are analyzed for presence of noise. If noise is detected with high possibility then input frame profile will be used for processing following frames, until new noise frame is detected.
        :param int samples: Set size of single frame in number of samples. Allowed range is from 512 to 65536. Default frame size is 8192 samples.
        :param float softness: Set softness applied inside thresholding function. Allowed range is from 0 to 10. Default softness is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afwtdn

        """
        filter_node = FilterNode(
            name="afwtdn",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sigma": sigma,
                "levels": levels,
                "wavet": wavet,
                "percent": percent,
                "profile": profile,
                "adaptive": adaptive,
                "samples": samples,
                "softness": softness,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def agate(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(0),
        range: float | DefaultFloat = DefaultFloat(0.06125),
        threshold: float | DefaultFloat = DefaultFloat(0.125),
        ratio: float | DefaultFloat = DefaultFloat(2.0),
        attack: float | DefaultFloat = DefaultFloat(20.0),
        release: float | DefaultFloat = DefaultFloat(250.0),
        makeup: float | DefaultFloat = DefaultFloat(1.0),
        knee: float | DefaultFloat = DefaultFloat(2.828427125),
        detection: int | DefaultInt = DefaultInt(1),
        link: int | DefaultInt = DefaultInt(0),
        level_sc: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.29 agate
        A gate is mainly used to reduce lower parts of a signal. This kind of signal
        processing reduces disturbing noise between useful signals.

        Gating is done by detecting the volume below a chosen level threshold
        and dividing it by the factor set with ratio. The bottom of the noise
        floor is set via range. Because an exact manipulation of the signal
        would cause distortion of the waveform the reduction can be levelled over
        time. This is done by setting attack and release.

        attack determines how long the signal has to fall below the threshold
        before any reduction will occur and release sets the time the signal
        has to rise above the threshold to reduce the reduction again.
        Shorter signals than the chosen attack time will be left untouched.

        Parameters:
        ----------

        :param float level_in: Set input level before filtering. Default is 1. Allowed range is from 0.015625 to 64.
        :param int mode: Set the mode of operation. Can be upward or downward. Default is downward. If set to upward mode, higher parts of signal will be amplified, expanding dynamic range in upward direction. Otherwise, in case of downward lower parts of signal will be reduced.
        :param float range: Set the level of gain reduction when the signal is below the threshold. Default is 0.06125. Allowed range is from 0 to 1. Setting this to 0 disables reduction and then filter behaves like expander.
        :param float threshold: If a signal rises above this level the gain reduction is released. Default is 0.125. Allowed range is from 0 to 1.
        :param float ratio: Set a ratio by which the signal is reduced. Default is 2. Allowed range is from 1 to 9000.
        :param float attack: Amount of milliseconds the signal has to rise above the threshold before gain reduction stops. Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
        :param float release: Amount of milliseconds the signal has to fall below the threshold before the reduction is increased again. Default is 250 milliseconds. Allowed range is from 0.01 to 9000.
        :param float makeup: Set amount of amplification of signal after processing. Default is 1. Allowed range is from 1 to 64.
        :param float knee: Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.828427125. Allowed range is from 1 to 8.
        :param int detection: Choose if exact signal should be taken for detection or an RMS like one. Default is rms. Can be peak or rms.
        :param int link: Choose if the average level between all channels or the louder channel affects the reduction. Default is average. Can be average or maximum.
        :param float level_sc: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#agate

        """
        filter_node = FilterNode(
            name="agate",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def agraphmonitor(
        self,
        *,
        size: str | DefaultStr = DefaultStr("hd720"),
        opacity: float | DefaultFloat = DefaultFloat(0.9),
        mode: str | DefaultStr = DefaultStr(0),
        flags: str | DefaultStr = DefaultStr("FLAG_QUEUE"),
        rate: str | DefaultStr = DefaultStr("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.4 agraphmonitor
        See graphmonitor.

        Parameters:
        ----------

        :param str size: None
        :param float opacity: None
        :param str mode: None
        :param str flags: None
        :param str rate: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#agraphmonitor

        """
        filter_node = FilterNode(
            name="agraphmonitor",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "size": size,
                "opacity": opacity,
                "mode": mode,
                "flags": flags,
                "rate": rate,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def ahistogram(
        self,
        *,
        dmode: int | DefaultStr = DefaultStr("SINGLE"),
        rate: str | DefaultStr = DefaultStr("25"),
        size: str | DefaultStr = DefaultStr("hd720"),
        scale: int | DefaultStr = DefaultStr("LOG"),
        ascale: int | DefaultStr = DefaultStr("ALOG"),
        acount: int | DefaultInt = DefaultInt(1),
        rheight: float | DefaultFloat = DefaultFloat(0.1),
        slide: int | DefaultStr = DefaultStr("REPLACE"),
        hmode: int | DefaultStr = DefaultStr("ABS"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.5 ahistogram
        Convert input audio to a video output, displaying the volume histogram.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int dmode: Specify how histogram is calculated. It accepts the following values: ‘single’ Use single histogram for all channels. ‘separate’ Use separate histogram for each channel. Default is single.
        :param str rate: Set frame rate, expressed as number of frames per second. Default value is "25".
        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is hd720.
        :param int scale: Set display scale. It accepts the following values: ‘log’ logarithmic ‘sqrt’ square root ‘cbrt’ cubic root ‘lin’ linear ‘rlog’ reverse logarithmic Default is log.
        :param int ascale: Set amplitude scale. It accepts the following values: ‘log’ logarithmic ‘lin’ linear Default is log.
        :param int acount: Set how much frames to accumulate in histogram. Default is 1. Setting this to -1 accumulates all frames.
        :param float rheight: Set histogram ratio of window height.
        :param int slide: Set sonogram sliding. It accepts the following values: ‘replace’ replace old rows with new ones. ‘scroll’ scroll from top to bottom. Default is replace.
        :param int hmode: Set histogram mode. It accepts the following values: ‘abs’ Use absolute values of samples. ‘sign’ Use untouched values of samples. Default is abs.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ahistogram

        """
        filter_node = FilterNode(
            name="ahistogram",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def aiir(
        self,
        *,
        zeros: str | DefaultStr = DefaultStr("1+0i 1-0i"),
        poles: str | DefaultStr = DefaultStr("1+0i 1-0i"),
        gains: str | DefaultStr = DefaultStr("1|1"),
        dry: float | DefaultFloat = DefaultFloat(1.0),
        wet: float | DefaultFloat = DefaultFloat(1.0),
        format: int | DefaultInt = DefaultInt(1),
        process: int | DefaultInt = DefaultInt(1),
        precision: int | DefaultInt = DefaultInt(0),
        normalize: bool | DefaultInt = DefaultInt(1),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        response: bool | DefaultInt = DefaultInt(0),
        channel: int | DefaultInt = DefaultInt(0),
        size: str | DefaultStr = DefaultStr("hd720"),
        rate: str | DefaultStr = DefaultStr("25"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        8.30 aiir
        Apply an arbitrary Infinite Impulse Response filter.

        It accepts the following parameters:


        Coefficients in tf and sf format are separated by spaces and are in ascending
        order.

        Coefficients in zp format are separated by spaces and order of coefficients
        doesn’t matter. Coefficients in zp format are complex numbers with i
        imaginary unit.

        Different coefficients and gains can be provided for every channel, in such case
        use ’|’ to separate coefficients or gains. Last provided coefficients will be
        used for all remaining channels.

        Parameters:
        ----------

        :param str zeros: Set B/numerator/zeros/reflection coefficients.
        :param str poles: Set A/denominator/poles/ladder coefficients.
        :param str gains: Set channels gains.
        :param float dry: None
        :param float wet: None
        :param int format: Set coefficients format. ‘ll’ lattice-ladder function ‘sf’ analog transfer function ‘tf’ digital transfer function ‘zp’ Z-plane zeros/poles, cartesian (default) ‘pr’ Z-plane zeros/poles, polar radians ‘pd’ Z-plane zeros/poles, polar degrees ‘sp’ S-plane zeros/poles
        :param int process: Set type of processing. ‘d’ direct processing ‘s’ serial processing ‘p’ parallel processing
        :param int precision: Set filtering precision. ‘dbl’ double-precision floating-point (default) ‘flt’ single-precision floating-point ‘i32’ 32-bit integers ‘i16’ 16-bit integers
        :param bool normalize: Normalize filter coefficients, by default is enabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param bool response: Show IR frequency response, magnitude(magenta), phase(green) and group delay(yellow) in additional video stream. By default it is disabled.
        :param int channel: Set for which IR channel to display frequency response. By default is first channel displayed. This option is used only when response is enabled.
        :param str size: Set video stream size. This option is used only when response is enabled.
        :param str rate: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aiir

        """
        filter_node = FilterNode(
            name="aiir",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] + [StreamType.video] if response else [],
            inputs=[
                self,
            ],
            kwargs={
                "zeros": zeros,
                "poles": poles,
                "gains": gains,
                "dry": dry,
                "wet": wet,
                "format": format,
                "process": process,
                "precision": precision,
                "normalize": normalize,
                "mix": mix,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
            }
            | kwargs,
        )

        return filter_node

    def aintegral(self, **kwargs: Any) -> "AudioStream":
        """

        8.14 aderivative, aintegral
        Compute derivative/integral of audio stream.

        Applying both filters one after another produces original audio.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        filter_node = FilterNode(
            name="aintegral",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def alatency(self, **kwargs: Any) -> "AudioStream":
        """

        18.12 latency, alatency
        Measure filtering latency.

        Report previous filter filtering latency, delay in number of audio samples for audio filters
        or number of video frames for video filters.

        On end of input stream, filter will report min and max measured latency for previous running filter
        in filtergraph.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency

        """
        filter_node = FilterNode(
            name="alatency",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def alimiter(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        limit: float | DefaultFloat = DefaultFloat(1.0),
        attack: float | DefaultFloat = DefaultFloat(5.0),
        release: float | DefaultFloat = DefaultFloat(50.0),
        asc: bool | DefaultInt = DefaultInt(0),
        asc_level: float | DefaultFloat = DefaultFloat(0.5),
        level: bool | DefaultInt = DefaultInt(1),
        latency: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.31 alimiter
        The limiter prevents an input signal from rising over a desired threshold.
        This limiter uses lookahead technology to prevent your signal from distorting.
        It means that there is a small delay after the signal is processed. Keep in mind
        that the delay it produces is the attack time you set.

        The filter accepts the following options:


        Depending on picked setting it is recommended to upsample input 2x or 4x times
        with aresample before applying this filter.

        Parameters:
        ----------

        :param float level_in: Set input gain. Default is 1.
        :param float level_out: Set output gain. Default is 1.
        :param float limit: Don’t let signals above this level pass the limiter. Default is 1.
        :param float attack: The limiter will reach its attenuation level in this amount of time in milliseconds. Default is 5 milliseconds.
        :param float release: Come back from limiting to attenuation 1.0 in this amount of milliseconds. Default is 50 milliseconds.
        :param bool asc: When gain reduction is always needed ASC takes care of releasing to an average reduction level rather than reaching a reduction of 0 in the release time.
        :param float asc_level: Select how much the release time is affected by ASC, 0 means nearly no changes in release time while 1 produces higher release times.
        :param bool level: Auto level output signal. Default is enabled. This normalizes audio back to 0dB if enabled.
        :param bool latency: Compensate the delay introduced by using the lookahead buffer set with attack parameter. Also flush the valid audio data in the lookahead buffer when the stream hits EOF.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#alimiter

        """
        filter_node = FilterNode(
            name="alimiter",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "limit": limit,
                "attack": attack,
                "release": release,
                "asc": asc,
                "asc_level": asc_level,
                "level": level,
                "latency": latency,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def allpass(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.707),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        order: int | DefaultInt = DefaultInt(2),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.32 allpass
        Apply a two-pole all-pass filter with central frequency (in Hz)
        frequency, and filter-width width.
        An all-pass filter changes the audio’s frequency to phase relationship
        without changing its frequency to amplitude relationship.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set frequency in Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int order: Set the filter order, can be 1 or 2. Default is 2.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#allpass

        """
        filter_node = FilterNode(
            name="allpass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "order": order,
                "transform": transform,
                "precision": precision,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aloop(
        self,
        *,
        loop: int | DefaultInt = DefaultInt(0),
        size: int | DefaultInt = DefaultInt(0),
        start: int | DefaultInt = DefaultInt(0),
        time: int | DefaultStr = DefaultStr("9223372036854775807LL"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.33 aloop
        Loop audio samples.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int loop: Set the number of loops. Setting this value to -1 will result in infinite loops. Default is 0.
        :param int size: Set maximal number of samples. Default is 0.
        :param int start: Set first sample of loop. Default is 0.
        :param int time: Set the time of loop start in seconds. Only used if option named start is set to -1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aloop

        """
        filter_node = FilterNode(
            name="aloop",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def ametadata(
        self,
        *,
        mode: int | DefaultInt = DefaultInt(0),
        key: str,
        value: str,
        function: int | DefaultInt = DefaultInt(0),
        expr: str,
        file: str,
        direct: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        18.13 metadata, ametadata
        Manipulate frame metadata.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Set mode of operation of the filter. Can be one of the following: ‘select’ If both value and key is set, select frames which have such metadata. If only key is set, select every frame that has such key in metadata. ‘add’ Add new metadata key and value. If key is already available do nothing. ‘modify’ Modify value of already present key. ‘delete’ If value is set, delete only keys that have such value. Otherwise, delete key. If key is not set, delete all metadata values in the frame. ‘print’ Print key and its value if metadata was found. If key is not set print all metadata values available in frame.
        :param str key: Set key used with all modes. Must be set for all modes except print and delete.
        :param str value: Set metadata value which will be used. This option is mandatory for modify and add mode.
        :param int function: Which function to use when comparing metadata value and value. Can be one of following: ‘same_str’ Values are interpreted as strings, returns true if metadata value is same as value. ‘starts_with’ Values are interpreted as strings, returns true if metadata value starts with the value option string. ‘less’ Values are interpreted as floats, returns true if metadata value is less than value. ‘equal’ Values are interpreted as floats, returns true if value is equal with metadata value. ‘greater’ Values are interpreted as floats, returns true if metadata value is greater than value. ‘expr’ Values are interpreted as floats, returns true if expression from option expr evaluates to true. ‘ends_with’ Values are interpreted as strings, returns true if metadata value ends with the value option string.
        :param str expr: Set expression which is used when function is set to expr. The expression is evaluated through the eval API and can contain the following constants: VALUE1, FRAMEVAL Float representation of value from metadata key. VALUE2, USERVAL Float representation of value as supplied by user in value option.
        :param str file: If specified in print mode, output is written to the named file. Instead of plain filename any writable url can be specified. Filename “-” is a shorthand for standard output. If file option is not set, output is written to the log with AV_LOG_INFO loglevel.
        :param bool direct: Reduces buffering in print mode when output is written to a URL set using file.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#metadata_002c-ametadata

        """
        filter_node = FilterNode(
            name="ametadata",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def amultiply(self, _multiply1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
                _multiply1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def anequalizer(
        self,
        *,
        params: str | DefaultStr = DefaultStr(""),
        curves: bool | DefaultInt = DefaultInt(0),
        size: str | DefaultStr = DefaultStr("hd720"),
        mgain: float | DefaultFloat = DefaultFloat(60.0),
        fscale: int | DefaultInt = DefaultInt(1),
        colors: str | DefaultStr = DefaultStr("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        8.37 anequalizer
        High-order parametric multiband equalizer for each channel.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str params: This option string is in format: "cchn f=cf w=w g=g t=f | ..." Each equalizer band is separated by ’|’. chn Set channel number to which equalization will be applied. If input doesn’t have that channel the entry is ignored. f Set central frequency for band. If input doesn’t have that frequency the entry is ignored. w Set band width in Hertz. g Set band gain in dB. t Set filter type for band, optional, can be: ‘0’ Butterworth, this is default. ‘1’ Chebyshev type 1. ‘2’ Chebyshev type 2.
        :param bool curves: With this option activated frequency response of anequalizer is displayed in video stream.
        :param str size: Set video stream size. Only useful if curves option is activated.
        :param float mgain: Set max gain that will be displayed. Only useful if curves option is activated. Setting this to a reasonable value makes it possible to display gain which is derived from neighbour bands which are too close to each other and thus produce higher gain when both are activated.
        :param int fscale: Set frequency scale used to draw frequency response in video output. Can be linear or logarithmic. Default is logarithmic.
        :param str colors: Set color for each channel curve which is going to be displayed in video stream. This is list of color names separated by space or by ’|’. Unrecognised or missing colors will be replaced by white color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anequalizer

        """
        filter_node = FilterNode(
            name="anequalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] + [StreamType.video] if curves else [],
            inputs=[
                self,
            ],
            kwargs={
                "params": params,
                "curves": curves,
                "size": size,
                "mgain": mgain,
                "fscale": fscale,
                "colors": colors,
            }
            | kwargs,
        )

        return filter_node

    def anlmdn(
        self,
        *,
        strength: float | DefaultFloat = DefaultFloat(1e-05),
        patch: int | DefaultInt = DefaultInt(2000),
        research: int | DefaultInt = DefaultInt(6000),
        output: int | DefaultStr = DefaultStr("OUT_MODE"),
        smooth: float | DefaultFloat = DefaultFloat(11.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.38 anlmdn
        Reduce broadband noise in audio samples using Non-Local Means algorithm.

        Each sample is adjusted by looking for other samples with similar contexts. This
        context similarity is defined by comparing their surrounding patches of size
        p. Patches are searched in an area of r around the sample.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float strength: Set denoising strength. Allowed range is from 0.00001 to 10000. Default value is 0.00001.
        :param int patch: Set patch radius duration. Allowed range is from 1 to 100 milliseconds. Default value is 2 milliseconds.
        :param int research: Set research radius duration. Allowed range is from 2 to 300 milliseconds. Default value is 6 milliseconds.
        :param int output: Set the output mode. It accepts the following values: i Pass input unchanged. o Pass noise filtered out. n Pass only noise. Default value is o.
        :param float smooth: Set smooth factor. Default value is 11. Allowed range is from 1 to 1000.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmdn

        """
        filter_node = FilterNode(
            name="anlmdn",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "strength": strength,
                "patch": patch,
                "research": research,
                "output": output,
                "smooth": smooth,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def anlmf(
        self,
        _desired: "AudioStream",
        *,
        order: int | DefaultInt = DefaultInt(256),
        mu: float | DefaultFloat = DefaultFloat(0.75),
        eps: float | DefaultFloat = DefaultFloat(1.0),
        leakage: float | DefaultFloat = DefaultFloat(0.0),
        out_mode: int | DefaultStr = DefaultStr("OUT_MODE"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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
        self,
        _desired: "AudioStream",
        *,
        order: int | DefaultInt = DefaultInt(256),
        mu: float | DefaultFloat = DefaultFloat(0.75),
        eps: float | DefaultFloat = DefaultFloat(1.0),
        leakage: float | DefaultFloat = DefaultFloat(0.0),
        out_mode: int | DefaultStr = DefaultStr("OUT_MODE"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def anull(self, **kwargs: Any) -> "AudioStream":
        """

        8.40 anull
        Pass the audio source unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#anull

        """
        filter_node = FilterNode(
            name="anull",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def apad(
        self,
        *,
        packet_size: int | DefaultInt = DefaultInt(4096),
        pad_len: int | DefaultInt = DefaultInt(-1),
        whole_len: int | DefaultInt = DefaultInt(-1),
        pad_dur: int | DefaultInt = DefaultInt(-1),
        whole_dur: int | DefaultInt = DefaultInt(-1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.41 apad
        Pad the end of an audio stream with silence.

        This can be used together with ffmpeg -shortest to
        extend audio streams to the same length as the video stream.

        A description of the accepted options follows.


        If neither the pad_len nor the whole_len nor pad_dur
        nor whole_dur option is set, the filter will add silence to the end of
        the input stream indefinitely.

        Note that for ffmpeg 4.4 and earlier a zero pad_dur or
        whole_dur also caused the filter to add silence indefinitely.

        Parameters:
        ----------

        :param int packet_size: Set silence packet size. Default value is 4096.
        :param int pad_len: Set the number of samples of silence to add to the end. After the value is reached, the stream is terminated. This option is mutually exclusive with whole_len.
        :param int whole_len: Set the minimum total number of samples in the output audio stream. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with pad_len.
        :param int pad_dur: Specify the duration of samples of silence to add. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value.
        :param int whole_dur: Specify the minimum total duration in the output audio stream. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with pad_dur

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apad

        """
        filter_node = FilterNode(
            name="apad",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "packet_size": packet_size,
                "pad_len": pad_len,
                "whole_len": whole_len,
                "pad_dur": pad_dur,
                "whole_dur": whole_dur,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aperms(
        self,
        *,
        mode: int | DefaultStr = DefaultStr("MODE_NONE"),
        seed: int | DefaultInt = DefaultInt(-1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        18.14 perms, aperms
        Set read/write permissions for the output frames.

        These filters are mainly aimed at developers to test direct path in the
        following filter in the filtergraph.

        The filters accept the following options:


        Note: in case of auto-inserted filter between the permission filter and the
        following one, the permission might not be received as expected in that
        following filter. Inserting a format or aformat filter before the
        perms/aperms filter can avoid this problem.

        Parameters:
        ----------

        :param int mode: Select the permissions mode. It accepts the following values: ‘none’ Do nothing. This is the default. ‘ro’ Set all the output frames read-only. ‘rw’ Set all the output frames directly writable. ‘toggle’ Make the frame read-only if writable, and writable if read-only. ‘random’ Set each output frame read-only or writable randomly.
        :param int seed: Set the seed for the random mode, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to -1, the filter will try to use a good random seed on a best effort basis.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms

        """
        filter_node = FilterNode(
            name="aperms",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "mode": mode,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aphasemeter(
        self,
        *,
        rate: str | DefaultStr = DefaultStr("25"),
        size: str | DefaultStr = DefaultStr("800x400"),
        rc: int | DefaultInt = DefaultInt(2),
        gc: int | DefaultInt = DefaultInt(7),
        bc: int | DefaultInt = DefaultInt(1),
        mpc: str | DefaultStr = DefaultStr("none"),
        video: bool | DefaultInt = DefaultInt(1),
        phasing: bool | DefaultInt = DefaultInt(0),
        tolerance: float | DefaultFloat = DefaultFloat(0.0),
        angle: float | DefaultFloat = DefaultFloat(170.0),
        duration: int | DefaultInt = DefaultInt(2000000),
        **kwargs: Any,
    ) -> FilterNode:
        """

        18.6 aphasemeter
        Measures phase of input audio, which is exported as metadata lavfi.aphasemeter.phase,
        representing mean phase of current audio frame. A video output can also be produced and is
        enabled by default. The audio is passed through as first output.

        Audio will be rematrixed to stereo if it has a different channel layout. Phase value is in
        range [-1, 1] where -1 means left and right channels are completely out of phase
        and 1 means channels are in phase.

        The filter accepts the following options, all related to its video output:

        Parameters:
        ----------

        :param str rate: Set the output frame rate. Default value is 25.
        :param str size: Set the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 800x400.
        :param int rc: Specify the red, green, blue contrast. Default values are 2, 7 and 1. Allowed range is [0, 255].
        :param int gc: Specify the red, green, blue contrast. Default values are 2, 7 and 1. Allowed range is [0, 255].
        :param int bc: Specify the red, green, blue contrast. Default values are 2, 7 and 1. Allowed range is [0, 255].
        :param str mpc: Set color which will be used for drawing median phase. If color is none which is default, no median phase value will be drawn.
        :param bool video: Enable video output. Default is enabled.
        :param bool phasing: None
        :param float tolerance: None
        :param float angle: None
        :param int duration: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphasemeter

        """
        filter_node = FilterNode(
            name="aphasemeter",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] + ([StreamType.video] if video else []),
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )

        return filter_node

    def aphaser(
        self,
        *,
        in_gain: float | DefaultFloat = DefaultFloat(0.4),
        out_gain: float | DefaultFloat = DefaultFloat(0.74),
        delay: float | DefaultFloat = DefaultFloat(3.0),
        decay: float | DefaultFloat = DefaultFloat(0.4),
        speed: float | DefaultFloat = DefaultFloat(0.5),
        type: int | DefaultStr = DefaultStr("WAVE_TRI"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.42 aphaser
        Add a phasing effect to the input audio.

        A phaser filter creates series of peaks and troughs in the frequency spectrum.
        The position of the peaks and troughs are modulated so that they vary over time, creating a sweeping effect.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param float in_gain: Set input gain. Default is 0.4.
        :param float out_gain: Set output gain. Default is 0.74
        :param float delay: Set delay in milliseconds. Default is 3.0.
        :param float decay: Set decay. Default is 0.4.
        :param float speed: Set modulation speed in Hz. Default is 0.5.
        :param int type: Set modulation type. Default is triangular. It accepts the following values: ‘triangular, t’ ‘sinusoidal, s’

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaser

        """
        filter_node = FilterNode(
            name="aphaser",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delay": delay,
                "decay": decay,
                "speed": speed,
                "type": type,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aphaseshift(
        self,
        *,
        shift: float | DefaultFloat = DefaultFloat(0.0),
        level: float | DefaultFloat = DefaultFloat(1.0),
        order: int | DefaultInt = DefaultInt(8),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.43 aphaseshift
        Apply phase shift to input audio samples.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float shift: Specify phase shift. Allowed range is from -1.0 to 1.0. Default value is 0.0.
        :param float level: Set output gain applied to final output. Allowed range is from 0.0 to 1.0. Default value is 1.0.
        :param int order: Set filter order used for filtering. Allowed range is from 1 to 16. Default value is 8.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaseshift

        """
        filter_node = FilterNode(
            name="aphaseshift",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "shift": shift,
                "level": level,
                "order": order,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def apsnr(self, _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def apsyclip(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        clip: float | DefaultFloat = DefaultFloat(1.0),
        diff: bool | DefaultInt = DefaultInt(0),
        adaptive: float | DefaultFloat = DefaultFloat(0.5),
        iterations: int | DefaultInt = DefaultInt(10),
        level: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.45 apsyclip
        Apply Psychoacoustic clipper to input audio stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input gain. By default it is 1. Range is [0.015625 - 64].
        :param float level_out: Set output gain. By default it is 1. Range is [0.015625 - 64].
        :param float clip: Set the clipping start value. Default value is 0dBFS or 1.
        :param bool diff: Output only difference samples, useful to hear introduced distortions. By default is disabled.
        :param float adaptive: Set strength of adaptive distortion applied. Default value is 0.5. Allowed range is from 0 to 1.
        :param int iterations: Set number of iterations of psychoacoustic clipper. Allowed range is from 1 to 20. Default value is 10.
        :param bool level: Auto level output signal. Default is disabled. This normalizes audio back to 0dBFS if enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apsyclip

        """
        filter_node = FilterNode(
            name="apsyclip",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "clip": clip,
                "diff": diff,
                "adaptive": adaptive,
                "iterations": iterations,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def apulsator(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultStr = DefaultStr("SINE"),
        amount: float | DefaultFloat = DefaultFloat(1.0),
        offset_l: float | DefaultFloat = DefaultFloat(0.0),
        offset_r: float | DefaultFloat = DefaultFloat(0.5),
        width: float | DefaultFloat = DefaultFloat(1.0),
        timing: int | DefaultInt = DefaultInt(2),
        bpm: float | DefaultFloat = DefaultFloat(120.0),
        ms: int | DefaultInt = DefaultInt(500),
        hz: float | DefaultFloat = DefaultFloat(2.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.46 apulsator
        Audio pulsator is something between an autopanner and a tremolo.
        But it can produce funny stereo effects as well. Pulsator changes the volume
        of the left and right channel based on a LFO (low frequency oscillator) with
        different waveforms and shifted phases.
        This filter have the ability to define an offset between left and right
        channel. An offset of 0 means that both LFO shapes match each other.
        The left and right channel are altered equally - a conventional tremolo.
        An offset of 50% means that the shape of the right channel is exactly shifted
        in phase (or moved backwards about half of the frequency) - pulsator acts as
        an autopanner. At 1 both curves match again. Every setting in between moves the
        phase shift gapless between all stages and produces some "bypassing" sounds with
        sine and triangle waveforms. The more you set the offset near 1 (starting from
        the 0.5) the faster the signal passes from the left to the right speaker.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input gain. By default it is 1. Range is [0.015625 - 64].
        :param float level_out: Set output gain. By default it is 1. Range is [0.015625 - 64].
        :param int mode: Set waveform shape the LFO will use. Can be one of: sine, triangle, square, sawup or sawdown. Default is sine.
        :param float amount: Set modulation. Define how much of original signal is affected by the LFO.
        :param float offset_l: Set left channel offset. Default is 0. Allowed range is [0 - 1].
        :param float offset_r: Set right channel offset. Default is 0.5. Allowed range is [0 - 1].
        :param float width: Set pulse width. Default is 1. Allowed range is [0 - 2].
        :param int timing: Set possible timing mode. Can be one of: bpm, ms or hz. Default is hz.
        :param float bpm: Set bpm. Default is 120. Allowed range is [30 - 300]. Only used if timing is set to bpm.
        :param int ms: Set ms. Default is 500. Allowed range is [10 - 2000]. Only used if timing is set to ms.
        :param float hz: Set frequency in Hz. Default is 2. Allowed range is [0.01 - 100]. Only used if timing is set to hz.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apulsator

        """
        filter_node = FilterNode(
            name="apulsator",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def arealtime(
        self,
        *,
        limit: int | DefaultInt = DefaultInt(2000000),
        speed: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        18.15 realtime, arealtime
        Slow down filtering to match real time approximately.

        These filters will pause the filtering for a variable amount of time to
        match the output rate with the input timestamps.
        They are similar to the re option to ffmpeg.

        They accept the following options:

        Parameters:
        ----------

        :param int limit: Time limit for the pauses. Any pause longer than that will be considered a timestamp discontinuity and reset the timer. Default is 2 seconds.
        :param float speed: Speed factor for processing. The value must be a float larger than zero. Values larger than 1.0 will result in faster than realtime processing, smaller will slow processing down. The limit is automatically adapted accordingly. Default is 1.0. A processing speed faster than what is possible without these filters cannot be achieved.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime

        """
        filter_node = FilterNode(
            name="arealtime",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "limit": limit,
                "speed": speed,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aresample(self, *, sample_rate: int | DefaultInt = DefaultInt(0), **kwargs: Any) -> "AudioStream":
        """

        8.47 aresample
        Resample the input audio to the specified parameters, using the
        libswresample library. If none are specified then the filter will
        automatically convert between its input and output.

        This filter is also able to stretch/squeeze the audio data to make it match
        the timestamps or to inject silence / cut out audio to make it match the
        timestamps, do a combination of both or do neither.

        The filter accepts the syntax
        [sample_rate:]resampler_options, where sample_rate
        expresses a sample rate and resampler_options is a list of
        key=value pairs, separated by ":". See the
        (ffmpeg-resampler)"Resampler Options" section in the
        ffmpeg-resampler(1) manual
        for the complete list of supported options.

        Parameters:
        ----------

        :param int sample_rate: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aresample

        """
        filter_node = FilterNode(
            name="aresample",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sample_rate": sample_rate,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def areverse(self, **kwargs: Any) -> "AudioStream":
        """

        8.48 areverse
        Reverse an audio clip.

        Warning: This filter requires memory to buffer the entire clip, so trimming
        is suggested.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#areverse

        """
        filter_node = FilterNode(
            name="areverse",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def arls(
        self,
        _desired: "AudioStream",
        *,
        order: int | DefaultInt = DefaultInt(16),
        _lambda: float | DefaultStr = DefaultStr("1.f"),
        delta: float | DefaultStr = DefaultStr("2.f"),
        out_mode: int | DefaultStr = DefaultStr("OUT_MODE"),
        precision: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def arnndn(self, *, model: str, mix: float | DefaultFloat = DefaultFloat(1.0), **kwargs: Any) -> "AudioStream":
        """

        8.50 arnndn
        Reduce noise from speech using Recurrent Neural Networks.

        This filter accepts the following options:

        Parameters:
        ----------

        :param str model: Set train model file to load. This option is always required.
        :param float mix: Set how much to mix filtered samples into final output. Allowed range is from -1 to 1. Default value is 1. Negative values are special, they set how much to keep filtered noise in the final filter output. Set this option to -1 to hear actual noise removed from input signal.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#arnndn

        """
        filter_node = FilterNode(
            name="arnndn",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "model": model,
                "mix": mix,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asdr(self, _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def asegment(self, *, timestamps: str, samples: str, **kwargs: Any) -> FilterNode:
        """

        18.16 segment, asegment
        Split single input stream into multiple streams.

        This filter does opposite of concat filters.

        segment works on video frames, asegment on audio samples.

        This filter accepts the following options:


        In all cases, prefixing an each segment with ’+’ will make it relative to the
        previous segment.

        Parameters:
        ----------

        :param str timestamps: Timestamps of output segments separated by ’|’. The first segment will run from the beginning of the input stream. The last segment will run until the end of the input stream
        :param str samples: Exact frame/sample count to split the segments.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment

        """
        filter_node = FilterNode(
            name="asegment",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] * len((timestamps or samples).split("|")),
            inputs=[
                self,
            ],
            kwargs={
                "timestamps": timestamps,
                "samples": samples,
            }
            | kwargs,
        )

        return filter_node

    def aselect(
        self, *, expr: str | DefaultStr = DefaultStr("1"), outputs: int | DefaultInt = DefaultInt(1), **kwargs: Any
    ) -> FilterNode:
        """

        18.17 select, aselect
        Select frames to pass in output.

        This filter accepts the following options:


        The expression can contain the following constants:


        The default value of the select expression is "1".

        Parameters:
        ----------

        :param str expr: Set expression, which is evaluated for each input frame. If the expression is evaluated to zero, the frame is discarded. If the evaluation result is negative or NaN, the frame is sent to the first output; otherwise it is sent to the output with index ceil(val)-1, assuming that the input index starts from 0. For example a value of 1.2 corresponds to the output with index ceil(1.2)-1 = 2-1 = 1, that is the second output.
        :param int outputs: Set the number of outputs. The output to which to send the selected frame is based on the result of the evaluation. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect

        """
        filter_node = FilterNode(
            name="aselect",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] * outputs,
            inputs=[
                self,
            ],
            kwargs={
                "expr": expr,
                "outputs": outputs,
            }
            | kwargs,
        )

        return filter_node

    def asendcmd(self, *, commands: str, filename: str, **kwargs: Any) -> "AudioStream":
        """

        18.18 sendcmd, asendcmd
        Send commands to filters in the filtergraph.

        These filters read commands to be sent to other filters in the
        filtergraph.

        sendcmd must be inserted between two video filters,
        asendcmd must be inserted between two audio filters, but apart
        from that they act the same way.

        The specification of commands can be provided in the filter arguments
        with the commands option, or in a file specified by the
        filename option.

        These filters accept the following options:

        Parameters:
        ----------

        :param str commands: Set the commands to be read and sent to the other filters.
        :param str filename: Set the filename of the commands to be read and sent to the other filters.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd

        """
        filter_node = FilterNode(
            name="asendcmd",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "commands": commands,
                "filename": filename,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asetnsamples(
        self,
        *,
        nb_out_samples: int | DefaultInt = DefaultInt(1024),
        pad: bool | DefaultInt = DefaultInt(1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.52 asetnsamples
        Set the number of samples per each output audio frame.

        The last output packet may contain a different number of samples, as
        the filter will flush all the remaining samples when the input audio
        signals its end.

        The filter accepts the following options:


        For example, to set the number of per-frame samples to 1234 and
        disable padding for the last frame, use:

        asetnsamples=n=1234:p=0

        Parameters:
        ----------

        :param int nb_out_samples: Set the number of frames per each output audio frame. The number is intended as the number of samples per each channel. Default value is 1024.
        :param bool pad: If set to 1, the filter will pad the last audio frame with zeroes, so that the last frame will contain the same number of samples as the previous ones. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetnsamples

        """
        filter_node = FilterNode(
            name="asetnsamples",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "nb_out_samples": nb_out_samples,
                "pad": pad,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asetpts(self, *, expr: str | DefaultStr = DefaultStr("PTS"), **kwargs: Any) -> "AudioStream":
        """

        18.19 setpts, asetpts
        Change the PTS (presentation timestamp) of the input frames.

        setpts works on video frames, asetpts on audio frames.

        This filter accepts the following options:


        The expression is evaluated through the eval API and can contain the following
        constants:

        Parameters:
        ----------

        :param str expr: The expression which is evaluated for each frame to construct its timestamp.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts

        """
        filter_node = FilterNode(
            name="asetpts",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asetrate(self, *, sample_rate: int | DefaultInt = DefaultInt(44100), **kwargs: Any) -> "AudioStream":
        """

        8.53 asetrate
        Set the sample rate without altering the PCM data.
        This will result in a change of speed and pitch.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int sample_rate: Set the output sample rate. Default is 44100 Hz.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetrate

        """
        filter_node = FilterNode(
            name="asetrate",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sample_rate": sample_rate,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asettb(self, *, expr: str | DefaultStr = DefaultStr("intb"), **kwargs: Any) -> "AudioStream":
        """

        18.21 settb, asettb
        Set the timebase to use for the output frames timestamps.
        It is mainly useful for testing timebase configuration.

        It accepts the following parameters:


        The value for tb is an arithmetic expression representing a
        rational. The expression can contain the constants "AVTB" (the default
        timebase), "intb" (the input timebase) and "sr" (the sample rate,
        audio only). Default value is "intb".

        Parameters:
        ----------

        :param str expr: The expression which is evaluated into the output timebase.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb

        """
        filter_node = FilterNode(
            name="asettb",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def ashowinfo(self, **kwargs: Any) -> "AudioStream":
        """

        8.54 ashowinfo
        Show a line containing various information for each input audio frame.
        The input audio is not modified.

        The shown line contains a sequence of key/value pairs of the form
        key:value.

        The following values are shown in the output:

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#ashowinfo

        """
        filter_node = FilterNode(
            name="ashowinfo",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def asidedata(
        self, *, mode: int | DefaultInt = DefaultInt(0), type: int | DefaultInt = DefaultInt(-1), **kwargs: Any
    ) -> "AudioStream":
        """

        18.31 sidedata, asidedata
        Delete frame side data, or select frames based on it.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Set mode of operation of the filter. Can be one of the following: ‘select’ Select every frame with side data of type. ‘delete’ Delete side data of type. If type is not set, delete all side data in the frame.
        :param int type: Set side data type used with all modes. Must be set for select mode. For the list of frame side data types, refer to the AVFrameSideDataType enum in libavutil/frame.h. For example, to choose AV_FRAME_DATA_PANSCAN side data, you must specify PANSCAN.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata

        """
        filter_node = FilterNode(
            name="asidedata",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "mode": mode,
                "type": type,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asisdr(self, _input1: "AudioStream", **kwargs: Any) -> "AudioStream":
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def asoftclip(
        self,
        *,
        type: int | DefaultInt = DefaultInt(0),
        threshold: float | DefaultFloat = DefaultFloat(1.0),
        output: float | DefaultFloat = DefaultFloat(1.0),
        param: float | DefaultFloat = DefaultFloat(1.0),
        oversample: int | DefaultInt = DefaultInt(1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.56 asoftclip
        Apply audio soft clipping.

        Soft clipping is a type of distortion effect where the amplitude of a signal is saturated
        along a smooth curve, rather than the abrupt shape of hard-clipping.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int type: Set type of soft-clipping. It accepts the following values: hard tanh atan cubic exp alg quintic sin erf
        :param float threshold: Set threshold from where to start clipping. Default value is 0dB or 1.
        :param float output: Set gain applied to output. Default value is 0dB or 1.
        :param float param: Set additional parameter which controls sigmoid function.
        :param int oversample: Set oversampling factor.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asoftclip

        """
        filter_node = FilterNode(
            name="asoftclip",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "type": type,
                "threshold": threshold,
                "output": output,
                "param": param,
                "oversample": oversample,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def aspectralstats(
        self,
        *,
        win_size: int | DefaultInt = DefaultInt(2048),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        overlap: float | DefaultFloat = DefaultFloat(0.5),
        measure: str | DefaultStr = DefaultStr("(2147483647 *2U +1U)"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.57 aspectralstats
        Display frequency domain statistical information about the audio channels.
        Statistics are calculated and stored as metadata for each audio channel and for each audio frame.

        It accepts the following option:

        A list of each metadata key follows:

        Parameters:
        ----------

        :param int win_size: Set the window length in samples. Default value is 2048. Allowed range is from 32 to 65536.
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        :param float overlap: Set window overlap. Allowed range is from 0 to 1. Default value is 0.5.
        :param str measure: Select the parameters which are measured. The metadata keys can be used as flags, default is all which measures everything. none disables all measurement.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aspectralstats

        """
        filter_node = FilterNode(
            name="aspectralstats",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "measure": measure,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asplit(self, *, outputs: int | DefaultInt = DefaultInt(2), **kwargs: Any) -> FilterNode:
        """

        18.33 split, asplit
        Split input into several identical outputs.

        asplit works with audio input, split with video.

        The filter accepts a single parameter which specifies the number of outputs. If
        unspecified, it defaults to 2.

        Parameters:
        ----------

        :param int outputs: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit

        """
        filter_node = FilterNode(
            name="asplit",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio] * outputs,
            inputs=[
                self,
            ],
            kwargs={
                "outputs": outputs,
            }
            | kwargs,
        )

        return filter_node

    def asr(
        self,
        *,
        rate: int | DefaultInt = DefaultInt(16000),
        hmm: str,
        dict: str,
        lm: str,
        lmctl: str,
        lmname: str,
        logfn: str | DefaultStr = DefaultStr("/dev/null"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.58 asr
        Automatic Speech Recognition

        This filter uses PocketSphinx for speech recognition. To enable
        compilation of this filter, you need to configure FFmpeg with
        --enable-pocketsphinx.

        It accepts the following options:


        The filter exports recognized speech as the frame metadata lavfi.asr.text.

        Parameters:
        ----------

        :param int rate: Set sampling rate of input audio. Defaults is 16000. This need to match speech models, otherwise one will get poor results.
        :param str hmm: Set dictionary containing acoustic model files.
        :param str dict: Set pronunciation dictionary.
        :param str lm: Set language model file.
        :param str lmctl: Set language model set.
        :param str lmname: Set which language model to use.
        :param str logfn: Set output for log messages.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asr

        """
        filter_node = FilterNode(
            name="asr",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "rate": rate,
                "hmm": hmm,
                "dict": dict,
                "lm": lm,
                "lmctl": lmctl,
                "lmname": lmname,
                "logfn": logfn,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def astats(
        self,
        *,
        length: float | DefaultFloat = DefaultFloat(0.05),
        metadata: bool | DefaultInt = DefaultInt(0),
        reset: int | DefaultInt = DefaultInt(0),
        measure_perchannel: str | DefaultStr = DefaultStr("(2147483647 *2U +1U)"),
        measure_overall: str | DefaultStr = DefaultStr("(2147483647 *2U +1U)"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.59 astats
        Display time domain statistical information about the audio channels.
        Statistics are calculated and displayed for each audio channel and,
        where applicable, an overall figure is also given.

        It accepts the following option:

        A description of the measure keys follow:

        Parameters:
        ----------

        :param float length: Short window length in seconds, used for peak and trough RMS measurement. Default is 0.05 (50 milliseconds). Allowed range is [0 - 10].
        :param bool metadata: Set metadata injection. All the metadata keys are prefixed with lavfi.astats.X, where X is channel number starting from 1 or string Overall. Default is disabled. Available keys for each channel are: Bit_depth Crest_factor DC_offset Dynamic_range Entropy Flat_factor Max_difference Max_level Mean_difference Min_difference Min_level Noise_floor Noise_floor_count Number_of_Infs Number_of_NaNs Number_of_denormals Peak_count Abs_Peak_count Peak_level RMS_difference RMS_peak RMS_trough Zero_crossings Zero_crossings_rate and for Overall: Bit_depth DC_offset Entropy Flat_factor Max_difference Max_level Mean_difference Min_difference Min_level Noise_floor Noise_floor_count Number_of_Infs Number_of_NaNs Number_of_denormals Number_of_samples Peak_count Abs_Peak_count Peak_level RMS_difference RMS_level RMS_peak RMS_trough For example, a full key looks like lavfi.astats.1.DC_offset or lavfi.astats.Overall.Peak_count. Read below for the description of the keys.
        :param int reset: Set the number of frames over which cumulative stats are calculated before being reset. Default is disabled.
        :param str measure_perchannel: Select the parameters which are measured per channel. The metadata keys can be used as flags, default is all which measures everything. none disables all per channel measurement.
        :param str measure_overall: Select the parameters which are measured overall. The metadata keys can be used as flags, default is all which measures everything. none disables all overall measurement.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#astats

        """
        filter_node = FilterNode(
            name="astats",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "length": length,
                "metadata": metadata,
                "reset": reset,
                "measure_perchannel": measure_perchannel,
                "measure_overall": measure_overall,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asubboost(
        self,
        *,
        dry: float | DefaultFloat = DefaultFloat(1.0),
        wet: float | DefaultFloat = DefaultFloat(1.0),
        boost: float | DefaultFloat = DefaultFloat(2.0),
        decay: float | DefaultFloat = DefaultFloat(0.0),
        feedback: float | DefaultFloat = DefaultFloat(0.9),
        cutoff: float | DefaultFloat = DefaultFloat(100.0),
        slope: float | DefaultFloat = DefaultFloat(0.5),
        delay: float | DefaultFloat = DefaultFloat(20.0),
        channels: str | DefaultStr = DefaultStr("all"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.60 asubboost
        Boost subwoofer frequencies.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float dry: Set dry gain, how much of original signal is kept. Allowed range is from 0 to 1. Default value is 1.0.
        :param float wet: Set wet gain, how much of filtered signal is kept. Allowed range is from 0 to 1. Default value is 1.0.
        :param float boost: Set max boost factor. Allowed range is from 1 to 12. Default value is 2.
        :param float decay: Set delay line decay gain value. Allowed range is from 0 to 1. Default value is 0.0.
        :param float feedback: Set delay line feedback gain value. Allowed range is from 0 to 1. Default value is 0.9.
        :param float cutoff: Set cutoff frequency in Hertz. Allowed range is 50 to 900. Default value is 100.
        :param float slope: Set slope amount for cutoff frequency. Allowed range is 0.0001 to 1. Default value is 0.5.
        :param float delay: Set delay. Allowed range is from 1 to 100. Default value is 20.
        :param str channels: Set the channels to process. Default value is all available.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubboost

        """
        filter_node = FilterNode(
            name="asubboost",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "dry": dry,
                "wet": wet,
                "boost": boost,
                "decay": decay,
                "feedback": feedback,
                "cutoff": cutoff,
                "slope": slope,
                "delay": delay,
                "channels": channels,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asubcut(
        self,
        *,
        cutoff: float | DefaultFloat = DefaultFloat(20.0),
        order: int | DefaultInt = DefaultInt(10),
        level: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.61 asubcut
        Cut subwoofer frequencies.

        This filter allows to set custom, steeper
        roll off than highpass filter, and thus is able to more attenuate
        frequency content in stop-band.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float cutoff: Set cutoff frequency in Hertz. Allowed range is 2 to 200. Default value is 20.
        :param int order: Set filter order. Available values are from 3 to 20. Default value is 10.
        :param float level: Set input gain level. Allowed range is from 0 to 1. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubcut

        """
        filter_node = FilterNode(
            name="asubcut",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asupercut(
        self,
        *,
        cutoff: float | DefaultFloat = DefaultFloat(20000.0),
        order: int | DefaultInt = DefaultInt(10),
        level: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.62 asupercut
        Cut super frequencies.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float cutoff: Set cutoff frequency in Hertz. Allowed range is 20000 to 192000. Default value is 20000.
        :param int order: Set filter order. Available values are from 3 to 20. Default value is 10.
        :param float level: Set input gain level. Allowed range is from 0 to 1. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asupercut

        """
        filter_node = FilterNode(
            name="asupercut",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asuperpass(
        self,
        *,
        centerf: float | DefaultFloat = DefaultFloat(1000.0),
        order: int | DefaultInt = DefaultInt(4),
        qfactor: float | DefaultFloat = DefaultFloat(1.0),
        level: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.63 asuperpass
        Apply high order Butterworth band-pass filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float centerf: Set center frequency in Hertz. Allowed range is 2 to 999999. Default value is 1000.
        :param int order: Set filter order. Available values are from 4 to 20. Default value is 4.
        :param float qfactor: Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
        :param float level: Set input gain level. Allowed range is from 0 to 2. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperpass

        """
        filter_node = FilterNode(
            name="asuperpass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def asuperstop(
        self,
        *,
        centerf: float | DefaultFloat = DefaultFloat(1000.0),
        order: int | DefaultInt = DefaultInt(4),
        qfactor: float | DefaultFloat = DefaultFloat(1.0),
        level: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.64 asuperstop
        Apply high order Butterworth band-stop filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float centerf: Set center frequency in Hertz. Allowed range is 2 to 999999. Default value is 1000.
        :param int order: Set filter order. Available values are from 4 to 20. Default value is 4.
        :param float qfactor: Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
        :param float level: Set input gain level. Allowed range is from 0 to 2. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperstop

        """
        filter_node = FilterNode(
            name="asuperstop",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def atempo(self, *, tempo: float | DefaultFloat = DefaultFloat(1.0), **kwargs: Any) -> "AudioStream":
        """

        8.65 atempo
        Adjust audio tempo.

        The filter accepts exactly one parameter, the audio tempo. If not
        specified then the filter will assume nominal 1.0 tempo. Tempo must
        be in the [0.5, 100.0] range.

        Note that tempo greater than 2 will skip some samples rather than
        blend them in.  If for any reason this is a concern it is always
        possible to daisy-chain several instances of atempo to achieve the
        desired product tempo.

        Parameters:
        ----------

        :param float tempo: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atempo

        """
        filter_node = FilterNode(
            name="atempo",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "tempo": tempo,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def atilt(
        self,
        *,
        freq: float | DefaultFloat = DefaultFloat(10000.0),
        slope: float | DefaultFloat = DefaultFloat(0.0),
        width: float | DefaultFloat = DefaultFloat(1000.0),
        order: int | DefaultInt = DefaultInt(5),
        level: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.66 atilt
        Apply spectral tilt filter to audio stream.

        This filter apply any spectral roll-off slope over any specified frequency band.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float freq: Set central frequency of tilt in Hz. Default is 10000 Hz.
        :param float slope: Set slope direction of tilt. Default is 0. Allowed range is from -1 to 1.
        :param float width: Set width of tilt. Default is 1000. Allowed range is from 100 to 10000.
        :param int order: Set order of tilt filter.
        :param float level: Set input volume level. Allowed range is from 0 to 4. Default is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atilt

        """
        filter_node = FilterNode(
            name="atilt",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "freq": freq,
                "slope": slope,
                "width": width,
                "order": order,
                "level": level,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def atrim(
        self,
        *,
        start: int | DefaultStr = DefaultStr("9223372036854775807LL"),
        end: int | DefaultStr = DefaultStr("9223372036854775807LL"),
        start_pts: int | DefaultStr = DefaultStr("((int64_t)(0x8000000000000000ULL))"),
        end_pts: int | DefaultStr = DefaultStr("((int64_t)(0x8000000000000000ULL))"),
        duration: int | DefaultInt = DefaultInt(0),
        start_sample: int | DefaultInt = DefaultInt(-1),
        end_sample: int | DefaultStr = DefaultStr("9223372036854775807LL"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.67 atrim
        Trim the input so that the output contains one continuous subpart of the input.

        It accepts the following parameters:

        start, end, and duration are expressed as time
        duration specifications; see
        (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual.

        Note that the first two sets of the start/end options and the duration
        option look at the frame timestamp, while the _sample options simply count the
        samples that pass through the filter. So start/end_pts and start/end_sample will
        give different results when the timestamps are wrong, inexact or do not start at
        zero. Also note that this filter does not modify the timestamps. If you wish
        to have the output timestamps start at zero, insert the asetpts filter after the
        atrim filter.

        If multiple start or end options are set, this filter tries to be greedy and
        keep all samples that match at least one of the specified constraints. To keep
        only the part that matches all the constraints at once, chain multiple atrim
        filters.

        The defaults are such that all the input is kept. So it is possible to set e.g.
        just the end values to keep everything before the specified time.

        Examples:

         Drop everything except the second minute of input:

        ffmpeg -i INPUT -af atrim=60:120

         Keep only the first 1000 samples:

        ffmpeg -i INPUT -af atrim=end_sample=1000

        Parameters:
        ----------

        :param int start: None
        :param int end: None
        :param int start_pts: None
        :param int end_pts: None
        :param int duration: None
        :param int start_sample: None
        :param int end_sample: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atrim

        """
        filter_node = FilterNode(
            name="atrim",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "start": start,
                "end": end,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "start_sample": start_sample,
                "end_sample": end_sample,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def avectorscope(
        self,
        *,
        mode: int | DefaultStr = DefaultStr("LISSAJOUS"),
        rate: str | DefaultStr = DefaultStr("25"),
        size: str | DefaultStr = DefaultStr("400x400"),
        rc: int | DefaultInt = DefaultInt(40),
        gc: int | DefaultInt = DefaultInt(160),
        bc: int | DefaultInt = DefaultInt(80),
        ac: int | DefaultInt = DefaultInt(255),
        rf: int | DefaultInt = DefaultInt(15),
        gf: int | DefaultInt = DefaultInt(10),
        bf: int | DefaultInt = DefaultInt(5),
        af: int | DefaultInt = DefaultInt(5),
        zoom: float | DefaultFloat = DefaultFloat(1.0),
        draw: int | DefaultStr = DefaultStr("DOT"),
        scale: int | DefaultStr = DefaultStr("LIN"),
        swap: bool | DefaultInt = DefaultInt(1),
        mirror: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.7 avectorscope
        Convert input audio to a video output, representing the audio vector
        scope.

        The filter is used to measure the difference between channels of stereo
        audio stream. A monaural signal, consisting of identical left and right
        signal, results in straight vertical line. Any stereo separation is visible
        as a deviation from this line, creating a Lissajous figure.
        If the straight (or deviation from it) but horizontal line appears this
        indicates that the left and right channels are out of phase.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Set the vectorscope mode. Available values are: ‘lissajous’ Lissajous rotated by 45 degrees. ‘lissajous_xy’ Same as above but not rotated. ‘polar’ Shape resembling half of circle. Default value is ‘lissajous’.
        :param str rate: Set the output frame rate. Default value is 25.
        :param str size: Set the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 400x400.
        :param int rc: Specify the red, green, blue and alpha contrast. Default values are 40, 160, 80 and 255. Allowed range is [0, 255].
        :param int gc: Specify the red, green, blue and alpha contrast. Default values are 40, 160, 80 and 255. Allowed range is [0, 255].
        :param int bc: Specify the red, green, blue and alpha contrast. Default values are 40, 160, 80 and 255. Allowed range is [0, 255].
        :param int ac: Specify the red, green, blue and alpha contrast. Default values are 40, 160, 80 and 255. Allowed range is [0, 255].
        :param int rf: Specify the red, green, blue and alpha fade. Default values are 15, 10, 5 and 5. Allowed range is [0, 255].
        :param int gf: Specify the red, green, blue and alpha fade. Default values are 15, 10, 5 and 5. Allowed range is [0, 255].
        :param int bf: Specify the red, green, blue and alpha fade. Default values are 15, 10, 5 and 5. Allowed range is [0, 255].
        :param int af: Specify the red, green, blue and alpha fade. Default values are 15, 10, 5 and 5. Allowed range is [0, 255].
        :param float zoom: Set the zoom factor. Default value is 1. Allowed range is [0, 10]. Values lower than 1 will auto adjust zoom factor to maximal possible value.
        :param int draw: Set the vectorscope drawing mode. Available values are: ‘dot’ Draw dot for each sample. ‘line’ Draw line between previous and current sample. ‘aaline’ Draw anti-aliased line between previous and current sample. Default value is ‘dot’.
        :param int scale: Specify amplitude scale of audio samples. Available values are: ‘lin’ Linear. ‘sqrt’ Square root. ‘cbrt’ Cubic root. ‘log’ Logarithmic.
        :param bool swap: Swap left channel axis with right channel axis.
        :param int mirror: Mirror axis. ‘none’ No mirror. ‘x’ Mirror only x axis. ‘y’ Mirror only y axis. ‘xy’ Mirror both axis.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avectorscope

        """
        filter_node = FilterNode(
            name="avectorscope",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def axcorrelate(
        self,
        _axcorrelate1: "AudioStream",
        *,
        size: int | DefaultInt = DefaultInt(256),
        algo: int | DefaultInt = DefaultInt(2),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
                _axcorrelate1,
            ],
            kwargs={
                "size": size,
                "algo": algo,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def bandpass(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        csg: bool | DefaultInt = DefaultInt(0),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.69 bandpass
        Apply a two-pole Butterworth band-pass filter with central
        frequency frequency, and (3dB-point) band-width width.
        The csg option selects a constant skirt gain (peak gain = Q)
        instead of the default: constant 0dB peak gain.
        The filter roll off at 6dB per octave (20dB per decade).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency. Default is 3000.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units.
        :param bool csg: Constant skirt gain if set to 1. Defaults to 0.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandpass

        """
        filter_node = FilterNode(
            name="bandpass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def bandreject(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.70 bandreject
        Apply a two-pole Butterworth band-reject filter with central
        frequency frequency, and (3dB-point) band-width width.
        The filter roll off at 6dB per octave (20dB per decade).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency. Default is 3000.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandreject

        """
        filter_node = FilterNode(
            name="bandreject",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def bass(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(100.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.71 bass, lowshelf
        Boost or cut the bass (lower) frequencies of the audio using a two-pole
        shelving filter with a response similar to that of a standard
        hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Determine how steep is the filter’s shelf transition.
        :param float gain: Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        filter_node = FilterNode(
            name="bass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def biquad(
        self,
        *,
        a0: float | DefaultFloat = DefaultFloat(1.0),
        a1: float | DefaultFloat = DefaultFloat(0.0),
        a2: float | DefaultFloat = DefaultFloat(0.0),
        b0: float | DefaultFloat = DefaultFloat(0.0),
        b1: float | DefaultFloat = DefaultFloat(0.0),
        b2: float | DefaultFloat = DefaultFloat(0.0),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.72 biquad
        Apply a biquad IIR filter with the given coefficients.
        Where b0, b1, b2 and a0, a1, a2
        are the numerator and denominator coefficients respectively.
        and channels, c specify which channels to filter, by default all
        available are filtered.

        Parameters:
        ----------

        :param float a0: None
        :param float a1: None
        :param float a2: None
        :param float b0: None
        :param float b1: None
        :param float b2: None
        :param float mix: None
        :param str channels: None
        :param bool normalize: None
        :param int transform: None
        :param int precision: None
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#biquad

        """
        filter_node = FilterNode(
            name="biquad",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "a0": a0,
                "a1": a1,
                "a2": a2,
                "b0": b0,
                "b1": b1,
                "b2": b2,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "blocksize": blocksize,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def bs2b(
        self,
        *,
        profile: int | DefaultStr = DefaultStr("BS2B_DEFAULT_CLEVEL"),
        fcut: int | DefaultInt = DefaultInt(0),
        feed: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.73 bs2b
        Bauer stereo to binaural transformation, which improves headphone listening of
        stereo audio records.

        To enable compilation of this filter you need to configure FFmpeg with
        --enable-libbs2b.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int profile: Pre-defined crossfeed level. default Default level (fcut=700, feed=50). cmoy Chu Moy circuit (fcut=700, feed=60). jmeier Jan Meier circuit (fcut=650, feed=95).
        :param int fcut: Cut frequency (in Hz).
        :param int feed: Feed level (in Hz).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bs2b

        """
        filter_node = FilterNode(
            name="bs2b",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "profile": profile,
                "fcut": fcut,
                "feed": feed,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def channelmap(self, *, map: str, channel_layout: str, **kwargs: Any) -> "AudioStream":
        """

        8.74 channelmap
        Remap input channels to new locations.

        It accepts the following parameters:

        If no mapping is present, the filter will implicitly map input channels to
        output channels, preserving indices.

        Parameters:
        ----------

        :param str map: Map channels from input to output. The argument is a ’|’-separated list of mappings, each in the in_channel-out_channel or in_channel form. in_channel can be either the name of the input channel (e.g. FL for front left) or its index in the input channel layout. out_channel is the name of the output channel or its index in the output channel layout. If out_channel is not given then it is implicitly an index, starting with zero and increasing by one for each mapping.
        :param str channel_layout: The channel layout of the output stream.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelmap

        """
        filter_node = FilterNode(
            name="channelmap",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "map": map,
                "channel_layout": channel_layout,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def channelsplit(
        self,
        *,
        channel_layout: str | DefaultStr = DefaultStr("stereo"),
        channels: str | DefaultStr = DefaultStr("all"),
        **kwargs: Any,
    ) -> FilterNode:
        """

        8.75 channelsplit
        Split each channel from an input audio stream into a separate output stream.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str channel_layout: The channel layout of the input stream. The default is "stereo".
        :param str channels: A channel layout describing the channels to be extracted as separate output streams or "all" to extract each input channel as a separate stream. The default is "all". Choosing channels not present in channel layout in the input will result in an error.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelsplit

        """
        filter_node = FilterNode(
            name="channelsplit",
            input_typings=[StreamType.audio],
            output_typings=None,
            inputs=[
                self,
            ],
            kwargs={
                "channel_layout": channel_layout,
                "channels": channels,
            }
            | kwargs,
        )

        return filter_node

    def chorus(
        self,
        *,
        in_gain: float | DefaultFloat = DefaultFloat(0.4),
        out_gain: float | DefaultFloat = DefaultFloat(0.4),
        delays: str,
        decays: str,
        speeds: str,
        depths: str,
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.76 chorus
        Add a chorus effect to the audio.

        Can make a single vocal sound like a chorus, but can also be applied to instrumentation.

        Chorus resembles an echo effect with a short delay, but whereas with echo the delay is
        constant, with chorus, it is varied using using sinusoidal or triangular modulation.
        The modulation depth defines the range the modulated delay is played before or after
        the delay. Hence the delayed sound will sound slower or faster, that is the delayed
        sound tuned around the original one, like in a chorus where some vocals are slightly
        off key.

        It accepts the following parameters:

        Parameters:
        ----------

        :param float in_gain: Set input gain. Default is 0.4.
        :param float out_gain: Set output gain. Default is 0.4.
        :param str delays: Set delays. A typical delay is around 40ms to 60ms.
        :param str decays: Set decays.
        :param str speeds: Set speeds.
        :param str depths: Set depths.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chorus

        """
        filter_node = FilterNode(
            name="chorus",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
                "speeds": speeds,
                "depths": depths,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def compand(
        self,
        *,
        attacks: str | DefaultStr = DefaultStr("0"),
        decays: str | DefaultStr = DefaultStr("0.8"),
        points: str | DefaultStr = DefaultStr("-70/-70|-60/-20|1/0"),
        soft_knee: float | DefaultFloat = DefaultFloat(0.01),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        volume: float | DefaultFloat = DefaultFloat(0.0),
        delay: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.77 compand
        Compress or expand the audio’s dynamic range.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str attacks: A list of times in seconds for each channel over which the instantaneous level of the input signal is averaged to determine its volume. attacks refers to increase of volume and decays refers to decrease of volume. For most situations, the attack time (response to the audio getting louder) should be shorter than the decay time, because the human ear is more sensitive to sudden loud audio than sudden soft audio. A typical value for attack is 0.3 seconds and a typical value for decay is 0.8 seconds. If specified number of attacks & decays is lower than number of channels, the last set attack/decay will be used for all remaining channels.
        :param str decays: A list of times in seconds for each channel over which the instantaneous level of the input signal is averaged to determine its volume. attacks refers to increase of volume and decays refers to decrease of volume. For most situations, the attack time (response to the audio getting louder) should be shorter than the decay time, because the human ear is more sensitive to sudden loud audio than sudden soft audio. A typical value for attack is 0.3 seconds and a typical value for decay is 0.8 seconds. If specified number of attacks & decays is lower than number of channels, the last set attack/decay will be used for all remaining channels.
        :param str points: A list of points for the transfer function, specified in dB relative to the maximum possible signal amplitude. Each key points list must be defined using the following syntax: x0/y0|x1/y1|x2/y2|.... or x0/y0 x1/y1 x2/y2 .... The input values must be in strictly increasing order but the transfer function does not have to be monotonically rising. The point 0/0 is assumed but may be overridden (by 0/out-dBn). Typical values for the transfer function are -70/-70|-60/-20|1/0.
        :param float soft_knee: Set the curve radius in dB for all joints. It defaults to 0.01.
        :param float gain: Set the additional gain in dB to be applied at all points on the transfer function. This allows for easy adjustment of the overall gain. It defaults to 0.
        :param float volume: Set an initial volume, in dB, to be assumed for each channel when filtering starts. This permits the user to supply a nominal level initially, so that, for example, a very large gain is not applied to initial signal levels before the companding has begun to operate. A typical value for audio which is initially quiet is -90 dB. It defaults to 0.
        :param float delay: Set a delay, in seconds. The input audio is analyzed immediately, but audio is delayed before being fed to the volume adjuster. Specifying a delay approximately equal to the attack/decay times allows the filter to effectively operate in predictive rather than reactive mode. It defaults to 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compand

        """
        filter_node = FilterNode(
            name="compand",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "attacks": attacks,
                "decays": decays,
                "points": points,
                "soft-knee": soft_knee,
                "gain": gain,
                "volume": volume,
                "delay": delay,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def compensationdelay(
        self,
        *,
        mm: int | DefaultInt = DefaultInt(0),
        cm: int | DefaultInt = DefaultInt(0),
        m: int | DefaultInt = DefaultInt(0),
        dry: float | DefaultFloat = DefaultFloat(0.0),
        wet: float | DefaultFloat = DefaultFloat(1.0),
        temp: int | DefaultInt = DefaultInt(20),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.78 compensationdelay
        Compensation Delay Line is a metric based delay to compensate differing
        positions of microphones or speakers.

        For example, you have recorded guitar with two microphones placed in
        different locations. Because the front of sound wave has fixed speed in
        normal conditions, the phasing of microphones can vary and depends on
        their location and interposition. The best sound mix can be achieved when
        these microphones are in phase (synchronized). Note that a distance of
        ~30 cm between microphones makes one microphone capture the signal in
        antiphase to the other microphone. That makes the final mix sound moody.
        This filter helps to solve phasing problems by adding different delays
        to each microphone track and make them synchronized.

        The best result can be reached when you take one track as base and
        synchronize other tracks one by one with it.
        Remember that synchronization/delay tolerance depends on sample rate, too.
        Higher sample rates will give more tolerance.

        The filter accepts the following parameters:

        Parameters:
        ----------

        :param int mm: Set millimeters distance. This is compensation distance for fine tuning. Default is 0.
        :param int cm: Set cm distance. This is compensation distance for tightening distance setup. Default is 0.
        :param int m: Set meters distance. This is compensation distance for hard distance setup. Default is 0.
        :param float dry: Set dry amount. Amount of unprocessed (dry) signal. Default is 0.
        :param float wet: Set wet amount. Amount of processed (wet) signal. Default is 1.
        :param int temp: Set temperature in degrees Celsius. This is the temperature of the environment. Default is 20.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compensationdelay

        """
        filter_node = FilterNode(
            name="compensationdelay",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "mm": mm,
                "cm": cm,
                "m": m,
                "dry": dry,
                "wet": wet,
                "temp": temp,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def crossfeed(
        self,
        *,
        strength: float | DefaultFloat = DefaultFloat(0.2),
        range: float | DefaultFloat = DefaultFloat(0.5),
        slope: float | DefaultFloat = DefaultFloat(0.5),
        level_in: float | DefaultFloat = DefaultFloat(0.9),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        block_size: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.79 crossfeed
        Apply headphone crossfeed filter.

        Crossfeed is the process of blending the left and right channels of stereo
        audio recording.
        It is mainly used to reduce extreme stereo separation of low frequencies.

        The intent is to produce more speaker like sound to the listener.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float strength: Set strength of crossfeed. Default is 0.2. Allowed range is from 0 to 1. This sets gain of low shelf filter for side part of stereo image. Default is -6dB. Max allowed is -30db when strength is set to 1.
        :param float range: Set soundstage wideness. Default is 0.5. Allowed range is from 0 to 1. This sets cut off frequency of low shelf filter. Default is cut off near 1550 Hz. With range set to 1 cut off frequency is set to 2100 Hz.
        :param float slope: Set curve slope of low shelf filter. Default is 0.5. Allowed range is from 0.01 to 1.
        :param float level_in: Set input gain. Default is 0.9.
        :param float level_out: Set output gain. Default is 1.
        :param int block_size: Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crossfeed

        """
        filter_node = FilterNode(
            name="crossfeed",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "strength": strength,
                "range": range,
                "slope": slope,
                "level_in": level_in,
                "level_out": level_out,
                "block_size": block_size,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def crystalizer(
        self, *, i: float | DefaultFloat = DefaultFloat(2.0), c: bool | DefaultInt = DefaultInt(1), **kwargs: Any
    ) -> "AudioStream":
        """

        8.80 crystalizer
        Simple algorithm for audio noise sharpening.

        This filter linearly increases differences between each audio sample.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float i: Sets the intensity of effect (default: 2.0). Must be in range between -10.0 to 0 (unchanged sound) to 10.0 (maximum effect). To inverse filtering use negative value.
        :param bool c: Enable clipping. By default is enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crystalizer

        """
        filter_node = FilterNode(
            name="crystalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "i": i,
                "c": c,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def dcshift(
        self,
        *,
        shift: float | DefaultFloat = DefaultFloat(0.0),
        limitergain: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.81 dcshift
        Apply a DC shift to the audio.

        This can be useful to remove a DC offset (caused perhaps by a hardware problem
        in the recording chain) from the audio. The effect of a DC offset is reduced
        headroom and hence volume. The astats filter can be used to determine if
        a signal has a DC offset.

        Parameters:
        ----------

        :param float shift: Set the DC shift, allowed range is [-1, 1]. It indicates the amount to shift the audio.
        :param float limitergain: Optional. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is used to prevent clipping.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dcshift

        """
        filter_node = FilterNode(
            name="dcshift",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "shift": shift,
                "limitergain": limitergain,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def deesser(
        self,
        *,
        i: float | DefaultFloat = DefaultFloat(0.0),
        m: float | DefaultFloat = DefaultFloat(0.5),
        f: float | DefaultFloat = DefaultFloat(0.5),
        s: int | DefaultStr = DefaultStr("OUT_MODE"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.82 deesser
        Apply de-essing to the audio samples.

        Parameters:
        ----------

        :param float i: Set intensity for triggering de-essing. Allowed range is from 0 to 1. Default is 0.
        :param float m: Set amount of ducking on treble part of sound. Allowed range is from 0 to 1. Default is 0.5.
        :param float f: How much of original frequency content to keep when de-essing. Allowed range is from 0 to 1. Default is 0.5.
        :param int s: Set the output mode. It accepts the following values: i Pass input unchanged. o Pass ess filtered out. e Pass only ess. Default value is o.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deesser

        """
        filter_node = FilterNode(
            name="deesser",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "i": i,
                "m": m,
                "f": f,
                "s": s,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def dialoguenhance(
        self,
        *,
        original: float | DefaultFloat = DefaultFloat(1.0),
        enhance: float | DefaultFloat = DefaultFloat(1.0),
        voice: float | DefaultFloat = DefaultFloat(2.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.83 dialoguenhance
        Enhance dialogue in stereo audio.

        This filter accepts stereo input and produce surround (3.0) channels output.
        The newly produced front center channel have enhanced speech dialogue originally
        available in both stereo channels.
        This filter outputs front left and front right channels same as available in stereo input.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float original: Set the original center factor to keep in front center channel output. Allowed range is from 0 to 1. Default value is 1.
        :param float enhance: Set the dialogue enhance factor to put in front center channel output. Allowed range is from 0 to 3. Default value is 1.
        :param float voice: Set the voice detection factor. Allowed range is from 2 to 32. Default value is 2.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance

        """
        filter_node = FilterNode(
            name="dialoguenhance",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "original": original,
                "enhance": enhance,
                "voice": voice,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def drmeter(self, *, length: float | DefaultFloat = DefaultFloat(3.0), **kwargs: Any) -> "AudioStream":
        """

        8.84 drmeter
        Measure audio dynamic range.

        DR values of 14 and higher is found in very dynamic material. DR of 8 to 13
        is found in transition material. And anything less that 8 have very poor dynamics
        and is very compressed.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float length: Set window length in seconds used to split audio into segments of equal length. Default is 3 seconds.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drmeter

        """
        filter_node = FilterNode(
            name="drmeter",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "length": length,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def dynaudnorm(
        self,
        *,
        framelen: int | DefaultInt = DefaultInt(500),
        gausssize: int | DefaultInt = DefaultInt(31),
        peak: float | DefaultFloat = DefaultFloat(0.95),
        maxgain: float | DefaultFloat = DefaultFloat(10.0),
        targetrms: float | DefaultFloat = DefaultFloat(0.0),
        coupling: bool | DefaultInt = DefaultInt(1),
        correctdc: bool | DefaultInt = DefaultInt(0),
        altboundary: bool | DefaultInt = DefaultInt(0),
        compress: float | DefaultFloat = DefaultFloat(0.0),
        threshold: float | DefaultFloat = DefaultFloat(0.0),
        channels: str | DefaultStr = DefaultStr("all"),
        overlap: float | DefaultFloat = DefaultFloat(0.0),
        curve: str,
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.85 dynaudnorm
        Dynamic Audio Normalizer.

        This filter applies a certain amount of gain to the input audio in order
        to bring its peak magnitude to a target level (e.g. 0 dBFS). However, in
        contrast to more "simple" normalization algorithms, the Dynamic Audio
        Normalizer *dynamically* re-adjusts the gain factor to the input audio.
        This allows for applying extra gain to the "quiet" sections of the audio
        while avoiding distortions or clipping the "loud" sections. In other words:
        The Dynamic Audio Normalizer will "even out" the volume of quiet and loud
        sections, in the sense that the volume of each section is brought to the
        same target level. Note, however, that the Dynamic Audio Normalizer achieves
        this goal *without* applying "dynamic range compressing". It will retain 100%
        of the dynamic range *within* each section of the audio file.

        Parameters:
        ----------

        :param int framelen: None
        :param int gausssize: None
        :param float peak: None
        :param float maxgain: None
        :param float targetrms: None
        :param bool coupling: None
        :param bool correctdc: None
        :param bool altboundary: None
        :param float compress: None
        :param float threshold: None
        :param str channels: None
        :param float overlap: None
        :param str curve: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm

        """
        filter_node = FilterNode(
            name="dynaudnorm",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def earwax(self, **kwargs: Any) -> "AudioStream":
        """

        8.86 earwax
        Make audio easier to listen to on headphones.

        This filter adds ‘cues’ to 44.1kHz stereo (i.e. audio CD format) audio
        so that when listened to on headphones the stereo image is moved from
        inside your head (standard for headphones) to outside and in front of
        the listener (standard for speakers).

        Ported from SoX.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#earwax

        """
        filter_node = FilterNode(
            name="earwax",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)

    def ebur128(
        self,
        *,
        video: bool | DefaultInt = DefaultInt(0),
        size: str | DefaultStr = DefaultStr("640x480"),
        meter: int | DefaultInt = DefaultInt(9),
        framelog: int | DefaultInt = DefaultInt(-1),
        metadata: bool | DefaultInt = DefaultInt(0),
        peak: str | DefaultStr = DefaultStr("PEAK_MODE_NONE"),
        dualmono: bool | DefaultInt = DefaultInt(0),
        panlaw: float | DefaultFloat = DefaultFloat(-3.01029995663978),
        target: int | DefaultInt = DefaultInt(-23),
        gauge: int | DefaultInt = DefaultInt(0),
        scale: int | DefaultInt = DefaultInt(0),
        integrated: float | DefaultFloat = DefaultFloat(0.0),
        range: float | DefaultFloat = DefaultFloat(0.0),
        lra_low: float | DefaultFloat = DefaultFloat(0.0),
        lra_high: float | DefaultFloat = DefaultFloat(0.0),
        sample_peak: float | DefaultFloat = DefaultFloat(0.0),
        true_peak: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> FilterNode:
        """

        18.10 ebur128
        EBU R128 scanner filter. This filter takes an audio stream and analyzes its loudness
        level. By default, it logs a message at a frequency of 10Hz with the
        Momentary loudness (identified by M), Short-term loudness (S),
        Integrated loudness (I) and Loudness Range (LRA).

        The filter can only analyze streams which have
        sample format is double-precision floating point. The input stream will be converted to
        this specification, if needed. Users may need to insert aformat and/or aresample filters
        after this filter to obtain the original parameters.

        The filter also has a video output (see the video option) with a real
        time graph to observe the loudness evolution. The graphic contains the logged
        message mentioned above, so it is not printed anymore when this option is set,
        unless the verbose logging is set. The main graphing area contains the
        short-term loudness (3 seconds of analysis), and the gauge on the right is for
        the momentary loudness (400 milliseconds), but can optionally be configured
        to instead display short-term loudness (see gauge).

        The green area marks a  +/- 1LU target range around the target loudness
        (-23LUFS by default, unless modified through target).

        More information about the Loudness Recommendation EBU R128 on
        http://tech.ebu.ch/loudness.

        The filter accepts the following options:

        Parameters:
        ----------

        :param bool video: Activate the video output. The audio stream is passed unchanged whether this option is set or no. The video stream will be the first output stream if activated. Default is 0.
        :param str size: Set the video size. This option is for video only. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default and minimum resolution is 640x480.
        :param int meter: Set the EBU scale meter. Default is 9. Common values are 9 and 18, respectively for EBU scale meter +9 and EBU scale meter +18. Any other integer value between this range is allowed.
        :param int framelog: Force the frame logging level. Available values are: ‘quiet’ logging disabled ‘info’ information logging level ‘verbose’ verbose logging level By default, the logging level is set to info. If the video or the metadata options are set, it switches to verbose.
        :param bool metadata: Set metadata injection. If set to 1, the audio input will be segmented into 100ms output frames, each of them containing various loudness information in metadata. All the metadata keys are prefixed with lavfi.r128.. Default is 0.
        :param str peak: Set peak mode(s). Available modes can be cumulated (the option is a flag type). Possible values are: ‘none’ Disable any peak mode (default). ‘sample’ Enable sample-peak mode. Simple peak mode looking for the higher sample value. It logs a message for sample-peak (identified by SPK). ‘true’ Enable true-peak mode. If enabled, the peak lookup is done on an over-sampled version of the input stream for better peak accuracy. It logs a message for true-peak. (identified by TPK) and true-peak per frame (identified by FTPK). This mode requires a build with libswresample.
        :param bool dualmono: Treat mono input files as "dual mono". If a mono file is intended for playback on a stereo system, its EBU R128 measurement will be perceptually incorrect. If set to true, this option will compensate for this effect. Multi-channel input files are not affected by this option.
        :param float panlaw: Set a specific pan law to be used for the measurement of dual mono files. This parameter is optional, and has a default value of -3.01dB.
        :param int target: Set a specific target level (in LUFS) used as relative zero in the visualization. This parameter is optional and has a default value of -23LUFS as specified by EBU R128. However, material published online may prefer a level of -16LUFS (e.g. for use with podcasts or video platforms).
        :param int gauge: Set the value displayed by the gauge. Valid values are momentary and s shortterm. By default the momentary value will be used, but in certain scenarios it may be more useful to observe the short term value instead (e.g. live mixing).
        :param int scale: Sets the display scale for the loudness. Valid parameters are absolute (in LUFS) or relative (LU) relative to the target. This only affects the video output, not the summary or continuous log output.
        :param float integrated: Read-only exported value for measured integrated loudness, in LUFS.
        :param float range: Read-only exported value for measured loudness range, in LU.
        :param float lra_low: Read-only exported value for measured LRA low, in LUFS.
        :param float lra_high: Read-only exported value for measured LRA high, in LUFS.
        :param float sample_peak: Read-only exported value for measured sample peak, in dBFS.
        :param float true_peak: Read-only exported value for measured true peak, in dBFS.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ebur128

        """
        filter_node = FilterNode(
            name="ebur128",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video] if video else [] + [StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )

        return filter_node

    def equalizer(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(0.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(1.0),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.87 equalizer
        Apply a two-pole peaking equalisation (EQ) filter. With this
        filter, the signal-level at and around a selected frequency can
        be increased or decreased, whilst (unlike bandpass and bandreject
        filters) that at all other frequencies is unchanged.

        In order to produce complex equalisation curves, this filter can
        be given several times, each with a different central frequency.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency in Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units.
        :param float gain: Set the required gain or attenuation in dB. Beware of clipping when using a positive gain.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#equalizer

        """
        filter_node = FilterNode(
            name="equalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def extrastereo(
        self, *, m: float | DefaultFloat = DefaultFloat(2.5), c: bool | DefaultInt = DefaultInt(1), **kwargs: Any
    ) -> "AudioStream":
        """

        8.88 extrastereo
        Linearly increases the difference between left and right channels which
        adds some sort of "live" effect to playback.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float m: Sets the difference coefficient (default: 2.5). 0.0 means mono sound (average of both channels), with 1.0 sound will be unchanged, with -1.0 left and right channels will be swapped.
        :param bool c: Enable clipping. By default is enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extrastereo

        """
        filter_node = FilterNode(
            name="extrastereo",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "m": m,
                "c": c,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def firequalizer(
        self,
        *,
        gain: str | DefaultStr = DefaultStr("gain_interpolate(f)"),
        gain_entry: str,
        delay: float | DefaultFloat = DefaultFloat(0.01),
        accuracy: float | DefaultFloat = DefaultFloat(5.0),
        wfunc: int | DefaultStr = DefaultStr("WFUNC_HANN"),
        fixed: bool | DefaultInt = DefaultInt(0),
        multi: bool | DefaultInt = DefaultInt(0),
        zero_phase: bool | DefaultInt = DefaultInt(0),
        scale: int | DefaultStr = DefaultStr("SCALE_LINLOG"),
        dumpfile: str,
        dumpscale: int | DefaultStr = DefaultStr("SCALE_LINLOG"),
        fft2: bool | DefaultInt = DefaultInt(0),
        min_phase: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.89 firequalizer
        Apply FIR Equalization using arbitrary frequency response.

        The filter accepts the following option:

        Parameters:
        ----------

        :param str gain: Set gain curve equation (in dB). The expression can contain variables: f the evaluated frequency sr sample rate ch channel number, set to 0 when multichannels evaluation is disabled chid channel id, see libavutil/channel_layout.h, set to the first channel id when multichannels evaluation is disabled chs number of channels chlayout channel_layout, see libavutil/channel_layout.h and functions: gain_interpolate(f) interpolate gain on frequency f based on gain_entry cubic_interpolate(f) same as gain_interpolate, but smoother This option is also available as command. Default is gain_interpolate(f).
        :param str gain_entry: Set gain entry for gain_interpolate function. The expression can contain functions: entry(f, g) store gain entry at frequency f with value g This option is also available as command.
        :param float delay: Set filter delay in seconds. Higher value means more accurate. Default is 0.01.
        :param float accuracy: Set filter accuracy in Hz. Lower value means more accurate. Default is 5.
        :param int wfunc: Set window function. Acceptable values are: rectangular rectangular window, useful when gain curve is already smooth hann hann window (default) hamming hamming window blackman blackman window nuttall3 3-terms continuous 1st derivative nuttall window mnuttall3 minimum 3-terms discontinuous nuttall window nuttall 4-terms continuous 1st derivative nuttall window bnuttall minimum 4-terms discontinuous nuttall (blackman-nuttall) window bharris blackman-harris window tukey tukey window
        :param bool fixed: If enabled, use fixed number of audio samples. This improves speed when filtering with large delay. Default is disabled.
        :param bool multi: Enable multichannels evaluation on gain. Default is disabled.
        :param bool zero_phase: Enable zero phase mode by subtracting timestamp to compensate delay. Default is disabled.
        :param int scale: Set scale used by gain. Acceptable values are: linlin linear frequency, linear gain linlog linear frequency, logarithmic (in dB) gain (default) loglin logarithmic (in octave scale where 20 Hz is 0) frequency, linear gain loglog logarithmic frequency, logarithmic gain
        :param str dumpfile: Set file for dumping, suitable for gnuplot.
        :param int dumpscale: Set scale for dumpfile. Acceptable values are same with scale option. Default is linlog.
        :param bool fft2: Enable 2-channel convolution using complex FFT. This improves speed significantly. Default is disabled.
        :param bool min_phase: Enable minimum phase impulse response. Default is disabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#firequalizer

        """
        filter_node = FilterNode(
            name="firequalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def flanger(
        self,
        *,
        delay: float | DefaultFloat = DefaultFloat(0.0),
        depth: float | DefaultFloat = DefaultFloat(2.0),
        regen: float | DefaultFloat = DefaultFloat(0.0),
        width: float | DefaultFloat = DefaultFloat(71.0),
        speed: float | DefaultFloat = DefaultFloat(0.5),
        shape: int | DefaultStr = DefaultStr("WAVE_SIN"),
        phase: float | DefaultFloat = DefaultFloat(25.0),
        interp: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.90 flanger
        Apply a flanging effect to the audio.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float delay: Set base delay in milliseconds. Range from 0 to 30. Default value is 0.
        :param float depth: Set added sweep delay in milliseconds. Range from 0 to 10. Default value is 2.
        :param float regen: Set percentage regeneration (delayed signal feedback). Range from -95 to 95. Default value is 0.
        :param float width: Set percentage of delayed signal mixed with original. Range from 0 to 100. Default value is 71.
        :param float speed: Set sweeps per second (Hz). Range from 0.1 to 10. Default value is 0.5.
        :param int shape: Set swept wave shape, can be triangular or sinusoidal. Default value is sinusoidal.
        :param float phase: Set swept wave percentage-shift for multi channel. Range from 0 to 100. Default value is 25.
        :param int interp: Set delay-line interpolation, linear or quadratic. Default is linear.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#flanger

        """
        filter_node = FilterNode(
            name="flanger",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "delay": delay,
                "depth": depth,
                "regen": regen,
                "width": width,
                "speed": speed,
                "shape": shape,
                "phase": phase,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def haas(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        side_gain: float | DefaultFloat = DefaultFloat(1.0),
        middle_source: int | DefaultInt = DefaultInt(2),
        middle_phase: bool | DefaultInt = DefaultInt(0),
        left_delay: float | DefaultFloat = DefaultFloat(2.05),
        left_balance: float | DefaultFloat = DefaultFloat(-1.0),
        left_gain: float | DefaultFloat = DefaultFloat(1.0),
        left_phase: bool | DefaultInt = DefaultInt(0),
        right_delay: float | DefaultFloat = DefaultFloat(2.12),
        right_balance: float | DefaultFloat = DefaultFloat(1.0),
        right_gain: float | DefaultFloat = DefaultFloat(1.0),
        right_phase: bool | DefaultInt = DefaultInt(1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.91 haas
        Apply Haas effect to audio.

        Note that this makes most sense to apply on mono signals.
        With this filter applied to mono signals it give some directionality and
        stretches its stereo image.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input level. By default is 1, or 0dB
        :param float level_out: Set output level. By default is 1, or 0dB.
        :param float side_gain: Set gain applied to side part of signal. By default is 1.
        :param int middle_source: Set kind of middle source. Can be one of the following: ‘left’ Pick left channel. ‘right’ Pick right channel. ‘mid’ Pick middle part signal of stereo image. ‘side’ Pick side part signal of stereo image.
        :param bool middle_phase: Change middle phase. By default is disabled.
        :param float left_delay: Set left channel delay. By default is 2.05 milliseconds.
        :param float left_balance: Set left channel balance. By default is -1.
        :param float left_gain: Set left channel gain. By default is 1.
        :param bool left_phase: Change left phase. By default is disabled.
        :param float right_delay: Set right channel delay. By defaults is 2.12 milliseconds.
        :param float right_balance: Set right channel balance. By default is 1.
        :param float right_gain: Set right channel gain. By default is 1.
        :param bool right_phase: Change right phase. By default is enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#haas

        """
        filter_node = FilterNode(
            name="haas",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def hdcd(
        self,
        *,
        disable_autoconvert: bool | DefaultInt = DefaultInt(1),
        process_stereo: bool | DefaultInt = DefaultInt(1),
        cdt_ms: int | DefaultInt = DefaultInt(2000),
        force_pe: bool | DefaultInt = DefaultInt(0),
        analyze_mode: int | DefaultStr = DefaultStr("HDCD_ANA_OFF"),
        bits_per_sample: int | DefaultInt = DefaultInt(16),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.92 hdcd
        Decodes High Definition Compatible Digital (HDCD) data. A 16-bit PCM stream with
        embedded HDCD codes is expanded into a 20-bit PCM stream.

        The filter supports the Peak Extend and Low-level Gain Adjustment features
        of HDCD, and detects the Transient Filter flag.


        ffmpeg -i HDCD16.flac -af hdcd OUT24.flac

        When using the filter with wav, note the default encoding for wav is 16-bit,
        so the resulting 20-bit stream will be truncated back to 16-bit. Use something
        like -acodec pcm_s24le after the filter to get 24-bit PCM output.

        ffmpeg -i HDCD16.wav -af hdcd OUT16.wav
        ffmpeg -i HDCD16.wav -af hdcd -c:a pcm_s24le OUT24.wav

        The filter accepts the following options:

        Parameters:
        ----------

        :param bool disable_autoconvert: Disable any automatic format conversion or resampling in the filter graph.
        :param bool process_stereo: Process the stereo channels together. If target_gain does not match between channels, consider it invalid and use the last valid target_gain.
        :param int cdt_ms: Set the code detect timer period in ms.
        :param bool force_pe: Always extend peaks above -3dBFS even if PE isn’t signaled.
        :param int analyze_mode: Replace audio with a solid tone and adjust the amplitude to signal some specific aspect of the decoding process. The output file can be loaded in an audio editor alongside the original to aid analysis. analyze_mode=pe:force_pe=true can be used to see all samples above the PE level. Modes are: ‘0, off’ Disabled ‘1, lle’ Gain adjustment level at each sample ‘2, pe’ Samples where peak extend occurs ‘3, cdt’ Samples where the code detect timer is active ‘4, tgm’ Samples where the target gain does not match between channels
        :param int bits_per_sample: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hdcd

        """
        filter_node = FilterNode(
            name="hdcd",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "disable_autoconvert": disable_autoconvert,
                "process_stereo": process_stereo,
                "cdt_ms": cdt_ms,
                "force_pe": force_pe,
                "analyze_mode": analyze_mode,
                "bits_per_sample": bits_per_sample,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def highpass(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.707),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.94 highpass
        Apply a high-pass filter with 3dB point frequency.
        The filter can be either single-pole, or double-pole (the default).
        The filter roll off at 6dB per pole per octave (20dB per pole per decade).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set frequency in Hz. Default is 3000.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units. Applies only to double-pole filter. The default is 0.707q and gives a Butterworth response.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#highpass

        """
        filter_node = FilterNode(
            name="highpass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def highshelf(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.116 treble, highshelf
        Boost or cut treble (upper) frequencies of the audio using a two-pole
        shelving filter with a response similar to that of a standard
        hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Determine how steep is the filter’s shelf transition.
        :param float gain: Give the gain at whichever is the lower of ~22 kHz and the Nyquist frequency. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        filter_node = FilterNode(
            name="highshelf",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def loudnorm(
        self,
        *,
        I: float | DefaultFloat = DefaultFloat(-24.0),
        LRA: float | DefaultFloat = DefaultFloat(7.0),
        TP: float | DefaultFloat = DefaultFloat(-2.0),
        measured_I: float | DefaultFloat = DefaultFloat(0.0),
        measured_LRA: float | DefaultFloat = DefaultFloat(0.0),
        measured_TP: float | DefaultFloat = DefaultFloat(99.0),
        measured_thresh: float | DefaultFloat = DefaultFloat(-70.0),
        offset: float | DefaultFloat = DefaultFloat(0.0),
        linear: bool | DefaultInt = DefaultInt(1),
        dual_mono: bool | DefaultInt = DefaultInt(0),
        print_format: int | DefaultStr = DefaultStr("NONE"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.97 loudnorm
        EBU R128 loudness normalization. Includes both dynamic and linear normalization modes.
        Support for both single pass (livestreams, files) and double pass (files) modes.
        This algorithm can target IL, LRA, and maximum true peak. In dynamic mode, to accurately
        detect true peaks, the audio stream will be upsampled to 192 kHz.
        Use the -ar option or aresample filter to explicitly set an output sample rate.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float I: Set integrated loudness target. Range is -70.0 - -5.0. Default value is -24.0.
        :param float LRA: Set loudness range target. Range is 1.0 - 50.0. Default value is 7.0.
        :param float TP: Set maximum true peak. Range is -9.0 - +0.0. Default value is -2.0.
        :param float measured_I: Measured IL of input file. Range is -99.0 - +0.0.
        :param float measured_LRA: Measured LRA of input file. Range is 0.0 - 99.0.
        :param float measured_TP: Measured true peak of input file. Range is -99.0 - +99.0.
        :param float measured_thresh: Measured threshold of input file. Range is -99.0 - +0.0.
        :param float offset: Set offset gain. Gain is applied before the true-peak limiter. Range is -99.0 - +99.0. Default is +0.0.
        :param bool linear: Normalize by linearly scaling the source audio. measured_I, measured_LRA, measured_TP, and measured_thresh must all be specified. Target LRA shouldn’t be lower than source LRA and the change in integrated loudness shouldn’t result in a true peak which exceeds the target TP. If any of these conditions aren’t met, normalization mode will revert to dynamic. Options are true or false. Default is true.
        :param bool dual_mono: Treat mono input files as "dual-mono". If a mono file is intended for playback on a stereo system, its EBU R128 measurement will be perceptually incorrect. If set to true, this option will compensate for this effect. Multi-channel input files are not affected by this option. Options are true or false. Default is false.
        :param int print_format: Set print format for stats. Options are summary, json, or none. Default value is none.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#loudnorm

        """
        filter_node = FilterNode(
            name="loudnorm",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def lowpass(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(500.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.707),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.98 lowpass
        Apply a low-pass filter with 3dB point frequency.
        The filter can be either single-pole or double-pole (the default).
        The filter roll off at 6dB per pole per octave (20dB per pole per decade).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set frequency in Hz. Default is 500.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Specify the band-width of a filter in width_type units. Applies only to double-pole filter. The default is 0.707q and gives a Butterworth response.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lowpass

        """
        filter_node = FilterNode(
            name="lowpass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def lowshelf(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(100.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.71 bass, lowshelf
        Boost or cut the bass (lower) frequencies of the audio using a two-pole
        shelving filter with a response similar to that of a standard
        hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Determine how steep is the filter’s shelf transition.
        :param float gain: Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        filter_node = FilterNode(
            name="lowshelf",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def mcompand(
        self,
        *,
        args: str
        | DefaultStr = DefaultStr(
            "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000"
        ),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.100 mcompand
        Multiband Compress or expand the audio’s dynamic range.

        The input audio is divided into bands using 4th order Linkwitz-Riley IIRs.
        This is akin to the crossover of a loudspeaker, and results in flat frequency
        response when absent compander action.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str args: This option syntax is: attack,decay,[attack,decay..] soft-knee points crossover_frequency [delay [initial_volume [gain]]] | attack,decay ... For explanation of each item refer to compand filter documentation.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcompand

        """
        filter_node = FilterNode(
            name="mcompand",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "args": args,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def pan(self, *, args: str, **kwargs: Any) -> "AudioStream":
        """

        8.101 pan
        Mix channels with specific gain levels. The filter accepts the output
        channel layout followed by a set of channels definitions.

        This filter is also designed to efficiently remap the channels of an audio
        stream.

        The filter accepts parameters of the form:
        "l|outdef|outdef|..."


        If the ‘=’ in a channel specification is replaced by ‘<’, then the gains for
        that specification will be renormalized so that the total is 1, thus
        avoiding clipping noise.

        Parameters:
        ----------

        :param str args: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pan

        """
        filter_node = FilterNode(
            name="pan",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "args": args,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def replaygain(
        self,
        *,
        track_gain: float | DefaultFloat = DefaultFloat(0.0),
        track_peak: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.102 replaygain
        ReplayGain scanner filter. This filter takes an audio stream as an input and
        outputs it unchanged.
        At end of filtering it displays track_gain and track_peak.

        The filter accepts the following exported read-only options:

        Parameters:
        ----------

        :param float track_gain: Exported track gain in dB at end of stream.
        :param float track_peak: Exported track peak at end of stream.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#replaygain

        """
        filter_node = FilterNode(
            name="replaygain",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "track_gain": track_gain,
                "track_peak": track_peak,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def rubberband(
        self,
        *,
        tempo: float | DefaultFloat = DefaultFloat(1.0),
        pitch: float | DefaultFloat = DefaultFloat(1.0),
        transients: int | DefaultInt = DefaultInt(0),
        detector: int | DefaultInt = DefaultInt(0),
        phase: int | DefaultInt = DefaultInt(0),
        window: int | DefaultInt = DefaultInt(0),
        smoothing: int | DefaultInt = DefaultInt(0),
        formant: int | DefaultInt = DefaultInt(0),
        pitchq: int | DefaultInt = DefaultInt(0),
        channels: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.104 rubberband
        Apply time-stretching and pitch-shifting with librubberband.

        To enable compilation of this filter, you need to configure FFmpeg with
        --enable-librubberband.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float tempo: Set tempo scale factor.
        :param float pitch: Set pitch scale factor.
        :param int transients: Set transients detector. Possible values are: crisp mixed smooth
        :param int detector: Set detector. Possible values are: compound percussive soft
        :param int phase: Set phase. Possible values are: laminar independent
        :param int window: Set processing window size. Possible values are: standard short long
        :param int smoothing: Set smoothing. Possible values are: off on
        :param int formant: Enable formant preservation when shift pitching. Possible values are: shifted preserved
        :param int pitchq: Set pitch quality. Possible values are: quality speed consistency
        :param int channels: Set channels. Possible values are: apart together

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rubberband

        """
        filter_node = FilterNode(
            name="rubberband",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def showcqt(
        self,
        *,
        size: str | DefaultStr = DefaultStr("1920x1080"),
        fps: str | DefaultStr = DefaultStr("25"),
        bar_h: int | DefaultInt = DefaultInt(-1),
        axis_h: int | DefaultInt = DefaultInt(-1),
        sono_h: int | DefaultInt = DefaultInt(-1),
        fullhd: bool | DefaultInt = DefaultInt(1),
        sono_v: str | DefaultStr = DefaultStr("16"),
        bar_v: str | DefaultStr = DefaultStr("sono_v"),
        sono_g: float | DefaultFloat = DefaultFloat(3.0),
        bar_g: float | DefaultFloat = DefaultFloat(1.0),
        bar_t: float | DefaultFloat = DefaultFloat(1.0),
        timeclamp: float | DefaultFloat = DefaultFloat(0.17),
        attack: float | DefaultFloat = DefaultFloat(0.0),
        basefreq: float | DefaultFloat = DefaultFloat(20.015231264080075),
        endfreq: float | DefaultFloat = DefaultFloat(20495.596814417997),
        coeffclamp: float | DefaultFloat = DefaultFloat(1.0),
        tlength: str | DefaultStr = DefaultStr("384*tc/(384+tc*f)"),
        count: int | DefaultInt = DefaultInt(6),
        fcount: int | DefaultInt = DefaultInt(0),
        fontfile: str,
        font: str,
        fontcolor: str
        | DefaultStr = DefaultStr(
            'st(0, (midi(f)-59.5)/12);" "st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));" "r(1-ld(1)) + b(ld(1))'
        ),
        axisfile: str,
        axis: bool | DefaultInt = DefaultInt(1),
        csp: int | DefaultStr = DefaultStr("AVCOL_SPC_UNSPECIFIED"),
        cscheme: str | DefaultStr = DefaultStr("1|0.5|0|0|0.5|1"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.22 showcqt
        Convert input audio to a video output representing frequency spectrum
        logarithmically using Brown-Puckette constant Q transform algorithm with
        direct frequency domain coefficient calculation (but the transform itself
        is not really constant Q, instead the Q factor is actually variable/clamped),
        with musical tone scale, from E0 to D#10.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. It must be even. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 1920x1080.
        :param str fps: Set the output frame rate. Default value is 25.
        :param int bar_h: Set the bargraph height. It must be even. Default value is -1 which computes the bargraph height automatically.
        :param int axis_h: Set the axis height. It must be even. Default value is -1 which computes the axis height automatically.
        :param int sono_h: Set the sonogram height. It must be even. Default value is -1 which computes the sonogram height automatically.
        :param bool fullhd: Set the fullhd resolution. This option is deprecated, use size, s instead. Default value is 1.
        :param str sono_v: Specify the sonogram volume expression. It can contain variables: bar_v the bar_v evaluated expression frequency, freq, f the frequency where it is evaluated timeclamp, tc the value of timeclamp option and functions: a_weighting(f) A-weighting of equal loudness b_weighting(f) B-weighting of equal loudness c_weighting(f) C-weighting of equal loudness. Default value is 16.
        :param str bar_v: Specify the bargraph volume expression. It can contain variables: sono_v the sono_v evaluated expression frequency, freq, f the frequency where it is evaluated timeclamp, tc the value of timeclamp option and functions: a_weighting(f) A-weighting of equal loudness b_weighting(f) B-weighting of equal loudness c_weighting(f) C-weighting of equal loudness. Default value is sono_v.
        :param float sono_g: Specify the sonogram gamma. Lower gamma makes the spectrum more contrast, higher gamma makes the spectrum having more range. Default value is 3. Acceptable range is [1, 7].
        :param float bar_g: Specify the bargraph gamma. Default value is 1. Acceptable range is [1, 7].
        :param float bar_t: Specify the bargraph transparency level. Lower value makes the bargraph sharper. Default value is 1. Acceptable range is [0, 1].
        :param float timeclamp: Specify the transform timeclamp. At low frequency, there is trade-off between accuracy in time domain and frequency domain. If timeclamp is lower, event in time domain is represented more accurately (such as fast bass drum), otherwise event in frequency domain is represented more accurately (such as bass guitar). Acceptable range is [0.002, 1]. Default value is 0.17.
        :param float attack: Set attack time in seconds. The default is 0 (disabled). Otherwise, it limits future samples by applying asymmetric windowing in time domain, useful when low latency is required. Accepted range is [0, 1].
        :param float basefreq: Specify the transform base frequency. Default value is 20.01523126408007475, which is frequency 50 cents below E0. Acceptable range is [10, 100000].
        :param float endfreq: Specify the transform end frequency. Default value is 20495.59681441799654, which is frequency 50 cents above D#10. Acceptable range is [10, 100000].
        :param float coeffclamp: This option is deprecated and ignored.
        :param str tlength: Specify the transform length in time domain. Use this option to control accuracy trade-off between time domain and frequency domain at every frequency sample. It can contain variables: frequency, freq, f the frequency where it is evaluated timeclamp, tc the value of timeclamp option. Default value is 384*tc/(384+tc*f).
        :param int count: Specify the transform count for every video frame. Default value is 6. Acceptable range is [1, 30].
        :param int fcount: Specify the transform count for every single pixel. Default value is 0, which makes it computed automatically. Acceptable range is [0, 10].
        :param str fontfile: Specify font file for use with freetype to draw the axis. If not specified, use embedded font. Note that drawing with font file or embedded font is not implemented with custom basefreq and endfreq, use axisfile option instead.
        :param str font: Specify fontconfig pattern. This has lower priority than fontfile. The : in the pattern may be replaced by | to avoid unnecessary escaping.
        :param str fontcolor: Specify font color expression. This is arithmetic expression that should return integer value 0xRRGGBB. It can contain variables: frequency, freq, f the frequency where it is evaluated timeclamp, tc the value of timeclamp option and functions: midi(f) midi number of frequency f, some midi numbers: E0(16), C1(24), C2(36), A4(69) r(x), g(x), b(x) red, green, and blue value of intensity x. Default value is st(0, (midi(f)-59.5)/12); st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0)); r(1-ld(1)) + b(ld(1)).
        :param str axisfile: Specify image file to draw the axis. This option override fontfile and fontcolor option.
        :param bool axis: Enable/disable drawing text to the axis. If it is set to 0, drawing to the axis is disabled, ignoring fontfile and axisfile option. Default value is 1.
        :param int csp: Set colorspace. The accepted values are: ‘unspecified’ Unspecified (default) ‘bt709’ BT.709 ‘fcc’ FCC ‘bt470bg’ BT.470BG or BT.601-6 625 ‘smpte170m’ SMPTE-170M or BT.601-6 525 ‘smpte240m’ SMPTE-240M ‘bt2020ncl’ BT.2020 with non-constant luminance
        :param str cscheme: Set spectrogram color scheme. This is list of floating point values with format left_r|left_g|left_b|right_r|right_g|right_b. The default is 1|0.5|0|0|0.5|1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showcqt

        """
        filter_node = FilterNode(
            name="showcqt",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showcwt(
        self,
        *,
        size: str | DefaultStr = DefaultStr("640x512"),
        rate: str | DefaultStr = DefaultStr("25"),
        scale: int | DefaultInt = DefaultInt(0),
        iscale: int | DefaultInt = DefaultInt(0),
        min: float | DefaultFloat = DefaultFloat(20.0),
        max: float | DefaultFloat = DefaultFloat(20000.0),
        imin: float | DefaultFloat = DefaultFloat(0.0),
        imax: float | DefaultFloat = DefaultFloat(1.0),
        logb: float | DefaultFloat = DefaultFloat(0.0001),
        deviation: float | DefaultFloat = DefaultFloat(1.0),
        pps: int | DefaultInt = DefaultInt(64),
        mode: int | DefaultInt = DefaultInt(0),
        slide: int | DefaultInt = DefaultInt(0),
        direction: int | DefaultInt = DefaultInt(0),
        bar: float | DefaultFloat = DefaultFloat(0.0),
        rotation: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.23 showcwt
        Convert input audio to video output representing frequency spectrum
        using Continuous Wavelet Transform and Morlet wavelet.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 640x512.
        :param str rate: Set the output frame rate. Default value is 25.
        :param int scale: Set the frequency scale used. Allowed values are: linear log bark mel erbs sqrt cbrt qdrt fm Default value is linear.
        :param int iscale: Set the intensity scale used. Allowed values are: linear log sqrt cbrt qdrt Default value is log.
        :param float min: Set the minimum frequency that will be used in output. Default is 20 Hz.
        :param float max: Set the maximum frequency that will be used in output. Default is 20000 Hz. The real frequency upper limit depends on input audio’s sample rate and such will be enforced on this value when it is set to value greater than Nyquist frequency.
        :param float imin: Set the minimum intensity that will be used in output.
        :param float imax: Set the maximum intensity that will be used in output.
        :param float logb: Set the logarithmic basis for brightness strength when mapping calculated magnitude values to pixel values. Allowed range is from 0 to 1. Default value is 0.0001.
        :param float deviation: Set the frequency deviation. Lower values than 1 are more frequency oriented, while higher values than 1 are more time oriented. Allowed range is from 0 to 10. Default value is 1.
        :param int pps: Set the number of pixel output per each second in one row. Allowed range is from 1 to 1024. Default value is 64.
        :param int mode: Set the output visual mode. Allowed values are: magnitude Show magnitude. phase Show only phase. magphase Show combination of magnitude and phase. Magnitude is mapped to brightness and phase to color. channel Show unique color per channel magnitude. stereo Show unique color per stereo difference. Default value is magnitude.
        :param int slide: Set the output slide method. Allowed values are: replace scroll frame
        :param int direction: Set the direction method for output slide method. Allowed values are: lr Direction from left to right. rl Direction from right to left. ud Direction from up to down. du Direction from down to up.
        :param float bar: Set the ratio of bargraph display to display size. Default is 0.
        :param float rotation: Set color rotation, must be in [-1.0, 1.0] range. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showcwt

        """
        filter_node = FilterNode(
            name="showcwt",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showfreqs(
        self,
        *,
        size: str | DefaultStr = DefaultStr("1024x512"),
        rate: str | DefaultStr = DefaultStr("25"),
        mode: int | DefaultStr = DefaultStr("BAR"),
        ascale: int | DefaultStr = DefaultStr("AS_LOG"),
        fscale: int | DefaultStr = DefaultStr("FS_LINEAR"),
        win_size: int | DefaultInt = DefaultInt(2048),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        overlap: float | DefaultFloat = DefaultFloat(1.0),
        averaging: int | DefaultInt = DefaultInt(1),
        colors: str | DefaultStr = DefaultStr("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        cmode: int | DefaultStr = DefaultStr("COMBINED"),
        minamp: float | DefaultFloat = DefaultFloat(1e-06),
        data: int | DefaultStr = DefaultStr("MAGNITUDE"),
        channels: str | DefaultStr = DefaultStr("all"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.24 showfreqs
        Convert input audio to video output representing the audio power spectrum.
        Audio amplitude is on Y-axis while frequency is on X-axis.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify size of video. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default is 1024x512.
        :param str rate: Set video rate. Default is 25.
        :param int mode: Set display mode. This set how each frequency bin will be represented. It accepts the following values: ‘line’ ‘bar’ ‘dot’ Default is bar.
        :param int ascale: Set amplitude scale. It accepts the following values: ‘lin’ Linear scale. ‘sqrt’ Square root scale. ‘cbrt’ Cubic root scale. ‘log’ Logarithmic scale. Default is log.
        :param int fscale: Set frequency scale. It accepts the following values: ‘lin’ Linear scale. ‘log’ Logarithmic scale. ‘rlog’ Reverse logarithmic scale. Default is lin.
        :param int win_size: Set window size. Allowed range is from 16 to 65536. Default is 2048
        :param int win_func: Set windowing function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hanning.
        :param float overlap: Set window overlap. In range [0, 1]. Default is 1, which means optimal overlap for selected window function will be picked.
        :param int averaging: Set time averaging. Setting this to 0 will display current maximal peaks. Default is 1, which means time averaging is disabled.
        :param str colors: Specify list of colors separated by space or by ’|’ which will be used to draw channel frequencies. Unrecognized or missing colors will be replaced by white color.
        :param int cmode: Set channel display mode. It accepts the following values: ‘combined’ ‘separate’ Default is combined.
        :param float minamp: Set minimum amplitude used in log amplitude scaler.
        :param int data: Set data display mode. It accepts the following values: ‘magnitude’ ‘phase’ ‘delay’ Default is magnitude.
        :param str channels: Set channels to use when processing audio. By default all are processed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showfreqs

        """
        filter_node = FilterNode(
            name="showfreqs",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showspatial(
        self,
        *,
        size: str | DefaultStr = DefaultStr("512x512"),
        win_size: int | DefaultInt = DefaultInt(4096),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        rate: str | DefaultStr = DefaultStr("25"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.25 showspatial
        Convert stereo input audio to a video output, representing the spatial relationship
        between two channels.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 512x512.
        :param int win_size: Set window size. Allowed range is from 1024 to 65536. Default size is 4096.
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann’ ‘hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default value is hann.
        :param str rate: Set output framerate.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspatial

        """
        filter_node = FilterNode(
            name="showspatial",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "size": size,
                "win_size": win_size,
                "win_func": win_func,
                "rate": rate,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def showspectrum(
        self,
        *,
        size: str | DefaultStr = DefaultStr("640x512"),
        slide: int | DefaultInt = DefaultInt(0),
        mode: int | DefaultStr = DefaultStr("COMBINED"),
        color: int | DefaultStr = DefaultStr("CHANNEL"),
        scale: int | DefaultStr = DefaultStr("SQRT"),
        fscale: int | DefaultStr = DefaultStr("F_LINEAR"),
        saturation: float | DefaultFloat = DefaultFloat(1.0),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        orientation: int | DefaultStr = DefaultStr("VERTICAL"),
        overlap: float | DefaultFloat = DefaultFloat(0.0),
        gain: float | DefaultFloat = DefaultFloat(1.0),
        data: int | DefaultInt = DefaultInt(0),
        rotation: float | DefaultFloat = DefaultFloat(0.0),
        start: int | DefaultInt = DefaultInt(0),
        stop: int | DefaultInt = DefaultInt(0),
        fps: str | DefaultStr = DefaultStr("auto"),
        legend: bool | DefaultInt = DefaultInt(0),
        drange: float | DefaultFloat = DefaultFloat(120.0),
        limit: float | DefaultFloat = DefaultFloat(0.0),
        opacity: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.26 showspectrum
        Convert input audio to a video output, representing the audio frequency
        spectrum.

        The filter accepts the following options:


        The usage is very similar to the showwaves filter; see the examples in that
        section.

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 640x512.
        :param int slide: Specify how the spectrum should slide along the window. It accepts the following values: ‘replace’ the samples start again on the left when they reach the right ‘scroll’ the samples scroll from right to left ‘fullframe’ frames are only produced when the samples reach the right ‘rscroll’ the samples scroll from left to right ‘lreplace’ the samples start again on the right when they reach the left Default value is replace.
        :param int mode: Specify display mode. It accepts the following values: ‘combined’ all channels are displayed in the same row ‘separate’ all channels are displayed in separate rows Default value is ‘combined’.
        :param int color: Specify display color mode. It accepts the following values: ‘channel’ each channel is displayed in a separate color ‘intensity’ each channel is displayed using the same color scheme ‘rainbow’ each channel is displayed using the rainbow color scheme ‘moreland’ each channel is displayed using the moreland color scheme ‘nebulae’ each channel is displayed using the nebulae color scheme ‘fire’ each channel is displayed using the fire color scheme ‘fiery’ each channel is displayed using the fiery color scheme ‘fruit’ each channel is displayed using the fruit color scheme ‘cool’ each channel is displayed using the cool color scheme ‘magma’ each channel is displayed using the magma color scheme ‘green’ each channel is displayed using the green color scheme ‘viridis’ each channel is displayed using the viridis color scheme ‘plasma’ each channel is displayed using the plasma color scheme ‘cividis’ each channel is displayed using the cividis color scheme ‘terrain’ each channel is displayed using the terrain color scheme Default value is ‘channel’.
        :param int scale: Specify scale used for calculating intensity color values. It accepts the following values: ‘lin’ linear ‘sqrt’ square root, default ‘cbrt’ cubic root ‘log’ logarithmic ‘4thrt’ 4th root ‘5thrt’ 5th root Default value is ‘sqrt’.
        :param int fscale: Specify frequency scale. It accepts the following values: ‘lin’ linear ‘log’ logarithmic Default value is ‘lin’.
        :param float saturation: Set saturation modifier for displayed colors. Negative values provide alternative color scheme. 0 is no saturation at all. Saturation must be in [-10.0, 10.0] range. Default value is 1.
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann’ ‘hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default value is hann.
        :param int orientation: Set orientation of time vs frequency axis. Can be vertical or horizontal. Default is vertical.
        :param float overlap: Set ratio of overlap window. Default value is 0. When value is 1 overlap is set to recommended size for specific window function currently used.
        :param float gain: Set scale gain for calculating intensity color values. Default value is 1.
        :param int data: Set which data to display. Can be magnitude, default or phase, or unwrapped phase: uphase.
        :param float rotation: Set color rotation, must be in [-1.0, 1.0] range. Default value is 0.
        :param int start: Set start frequency from which to display spectrogram. Default is 0.
        :param int stop: Set stop frequency to which to display spectrogram. Default is 0.
        :param str fps: Set upper frame rate limit. Default is auto, unlimited.
        :param bool legend: Draw time and frequency axes and legends. Default is disabled.
        :param float drange: Set dynamic range used to calculate intensity color values. Default is 120 dBFS. Allowed range is from 10 to 200.
        :param float limit: Set upper limit of input audio samples volume in dBFS. Default is 0 dBFS. Allowed range is from -100 to 100.
        :param float opacity: Set opacity strength when using pixel format output with alpha component.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspectrum

        """
        filter_node = FilterNode(
            name="showspectrum",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showspectrumpic(
        self,
        *,
        size: str | DefaultStr = DefaultStr("4096x2048"),
        mode: int | DefaultStr = DefaultStr("COMBINED"),
        color: int | DefaultStr = DefaultStr("INTENSITY"),
        scale: int | DefaultStr = DefaultStr("LOG"),
        fscale: int | DefaultStr = DefaultStr("F_LINEAR"),
        saturation: float | DefaultFloat = DefaultFloat(1.0),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        orientation: int | DefaultStr = DefaultStr("VERTICAL"),
        gain: float | DefaultFloat = DefaultFloat(1.0),
        legend: bool | DefaultInt = DefaultInt(1),
        rotation: float | DefaultFloat = DefaultFloat(0.0),
        start: int | DefaultInt = DefaultInt(0),
        stop: int | DefaultInt = DefaultInt(0),
        drange: float | DefaultFloat = DefaultFloat(120.0),
        limit: float | DefaultFloat = DefaultFloat(0.0),
        opacity: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.27 showspectrumpic
        Convert input audio to a single video frame, representing the audio frequency
        spectrum.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 4096x2048.
        :param int mode: Specify display mode. It accepts the following values: ‘combined’ all channels are displayed in the same row ‘separate’ all channels are displayed in separate rows Default value is ‘combined’.
        :param int color: Specify display color mode. It accepts the following values: ‘channel’ each channel is displayed in a separate color ‘intensity’ each channel is displayed using the same color scheme ‘rainbow’ each channel is displayed using the rainbow color scheme ‘moreland’ each channel is displayed using the moreland color scheme ‘nebulae’ each channel is displayed using the nebulae color scheme ‘fire’ each channel is displayed using the fire color scheme ‘fiery’ each channel is displayed using the fiery color scheme ‘fruit’ each channel is displayed using the fruit color scheme ‘cool’ each channel is displayed using the cool color scheme ‘magma’ each channel is displayed using the magma color scheme ‘green’ each channel is displayed using the green color scheme ‘viridis’ each channel is displayed using the viridis color scheme ‘plasma’ each channel is displayed using the plasma color scheme ‘cividis’ each channel is displayed using the cividis color scheme ‘terrain’ each channel is displayed using the terrain color scheme Default value is ‘intensity’.
        :param int scale: Specify scale used for calculating intensity color values. It accepts the following values: ‘lin’ linear ‘sqrt’ square root, default ‘cbrt’ cubic root ‘log’ logarithmic ‘4thrt’ 4th root ‘5thrt’ 5th root Default value is ‘log’.
        :param int fscale: Specify frequency scale. It accepts the following values: ‘lin’ linear ‘log’ logarithmic Default value is ‘lin’.
        :param float saturation: Set saturation modifier for displayed colors. Negative values provide alternative color scheme. 0 is no saturation at all. Saturation must be in [-10.0, 10.0] range. Default value is 1.
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann’ ‘hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default value is hann.
        :param int orientation: Set orientation of time vs frequency axis. Can be vertical or horizontal. Default is vertical.
        :param float gain: Set scale gain for calculating intensity color values. Default value is 1.
        :param bool legend: Draw time and frequency axes and legends. Default is enabled.
        :param float rotation: Set color rotation, must be in [-1.0, 1.0] range. Default value is 0.
        :param int start: Set start frequency from which to display spectrogram. Default is 0.
        :param int stop: Set stop frequency to which to display spectrogram. Default is 0.
        :param float drange: Set dynamic range used to calculate intensity color values. Default is 120 dBFS. Allowed range is from 10 to 200.
        :param float limit: Set upper limit of input audio samples volume in dBFS. Default is 0 dBFS. Allowed range is from -100 to 100.
        :param float opacity: Set opacity strength when using pixel format output with alpha component.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showspectrumpic

        """
        filter_node = FilterNode(
            name="showspectrumpic",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showvolume(
        self,
        *,
        rate: str | DefaultStr = DefaultStr("25"),
        b: int | DefaultInt = DefaultInt(1),
        w: int | DefaultInt = DefaultInt(400),
        h: int | DefaultInt = DefaultInt(20),
        f: float | DefaultFloat = DefaultFloat(0.95),
        c: str | DefaultStr = DefaultStr("PEAK*255+floor((1-PEAK)*255)*256+0xff000000"),
        t: bool | DefaultInt = DefaultInt(1),
        v: bool | DefaultInt = DefaultInt(1),
        dm: float | DefaultFloat = DefaultFloat(0.0),
        dmc: str | DefaultStr = DefaultStr("orange"),
        o: int | DefaultInt = DefaultInt(0),
        s: int | DefaultInt = DefaultInt(0),
        p: float | DefaultFloat = DefaultFloat(0.0),
        m: int | DefaultInt = DefaultInt(0),
        ds: int | DefaultStr = DefaultStr("LINEAR"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.28 showvolume
        Convert input audio volume to a video output.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str rate: Set video rate.
        :param int b: Set border width, allowed range is [0, 5]. Default is 1.
        :param int w: Set channel width, allowed range is [80, 8192]. Default is 400.
        :param int h: Set channel height, allowed range is [1, 900]. Default is 20.
        :param float f: Set fade, allowed range is [0, 1]. Default is 0.95.
        :param str c: Set volume color expression. The expression can use the following variables: VOLUME Current max volume of channel in dB. PEAK Current peak. CHANNEL Current channel number, starting from 0.
        :param bool t: If set, displays channel names. Default is enabled.
        :param bool v: If set, displays volume values. Default is enabled.
        :param float dm: In second. If set to > 0., display a line for the max level in the previous seconds. default is disabled: 0.
        :param str dmc: The color of the max line. Use when dm option is set to > 0. default is: orange
        :param int o: Set orientation, can be horizontal: h or vertical: v, default is h.
        :param int s: Set step size, allowed range is [0, 5]. Default is 0, which means step is disabled.
        :param float p: Set background opacity, allowed range is [0, 1]. Default is 0.
        :param int m: Set metering mode, can be peak: p or rms: r, default is p.
        :param int ds: Set display scale, can be linear: lin or log: log, default is lin.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showvolume

        """
        filter_node = FilterNode(
            name="showvolume",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.video(0)

    def showwaves(
        self,
        *,
        size: str | DefaultStr = DefaultStr("600x240"),
        mode: int | DefaultStr = DefaultStr("MODE_POINT"),
        n: float | DefaultStr = DefaultStr(0),
        rate: str | DefaultStr = DefaultStr("25"),
        split_channels: bool | DefaultInt = DefaultInt(0),
        colors: str | DefaultStr = DefaultStr("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: int | DefaultInt = DefaultInt(0),
        draw: int | DefaultStr = DefaultStr("DRAW_SCALE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.29 showwaves
        Convert input audio to a video output, representing the samples waves.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 600x240.
        :param int mode: Set display mode. Available values are: ‘point’ Draw a point for each sample. ‘line’ Draw a vertical line for each sample. ‘p2p’ Draw a point for each sample and a line between them. ‘cline’ Draw a centered vertical line for each sample. Default value is point.
        :param float n: Set the number of samples which are printed on the same column. A larger value will decrease the frame rate. Must be a positive integer. This option can be set only if the value for rate is not explicitly specified.
        :param str rate: Set the (approximate) output frame rate. This is done by setting the option n. Default value is "25".
        :param bool split_channels: Set if channels should be drawn separately or overlap. Default value is 0.
        :param str colors: Set colors separated by ’|’ which are going to be used for drawing of each channel.
        :param int scale: Set amplitude scale. Available values are: ‘lin’ Linear. ‘log’ Logarithmic. ‘sqrt’ Square root. ‘cbrt’ Cubic root. Default is linear.
        :param int draw: Set the draw mode. This is mostly useful to set for high n. Available values are: ‘scale’ Scale pixel values for each drawn sample. ‘full’ Draw every sample directly. Default value is scale.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showwaves

        """
        filter_node = FilterNode(
            name="showwaves",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "size": size,
                "mode": mode,
                "n": n,
                "rate": rate,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def showwavespic(
        self,
        *,
        size: str | DefaultStr = DefaultStr("600x240"),
        split_channels: bool | DefaultInt = DefaultInt(0),
        colors: str | DefaultStr = DefaultStr("red|green|blue|yellow|orange|lime|pink|magenta|brown"),
        scale: int | DefaultInt = DefaultInt(0),
        draw: int | DefaultStr = DefaultStr("DRAW_SCALE"),
        filter: int | DefaultStr = DefaultStr("FILTER_AVERAGE"),
        **kwargs: Any,
    ) -> "VideoStream":
        """

        18.30 showwavespic
        Convert input audio to a single video frame, representing the samples waves.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str size: Specify the video size for the output. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Default value is 600x240.
        :param bool split_channels: Set if channels should be drawn separately or overlap. Default value is 0.
        :param str colors: Set colors separated by ’|’ which are going to be used for drawing of each channel.
        :param int scale: Set amplitude scale. Available values are: ‘lin’ Linear. ‘log’ Logarithmic. ‘sqrt’ Square root. ‘cbrt’ Cubic root. Default is linear.
        :param int draw: Set the draw mode. Available values are: ‘scale’ Scale pixel values for each drawn sample. ‘full’ Draw every sample directly. Default value is scale.
        :param int filter: Set the filter mode. Available values are: ‘average’ Use average samples values for each drawn sample. ‘peak’ Use peak samples values for each drawn sample. Default value is average.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showwavespic

        """
        filter_node = FilterNode(
            name="showwavespic",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.video],
            inputs=[
                self,
            ],
            kwargs={
                "size": size,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
                "filter": filter,
            }
            | kwargs,
        )
        return filter_node.video(0)

    def sidechaincompress(
        self,
        _sidechain: "AudioStream",
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(0),
        threshold: float | DefaultFloat = DefaultFloat(0.125),
        ratio: float | DefaultFloat = DefaultFloat(2.0),
        attack: float | DefaultFloat = DefaultFloat(20.0),
        release: float | DefaultFloat = DefaultFloat(250.0),
        makeup: float | DefaultFloat = DefaultFloat(1.0),
        knee: float | DefaultFloat = DefaultFloat(2.82843),
        link: int | DefaultInt = DefaultInt(0),
        detection: int | DefaultInt = DefaultInt(1),
        level_sc: float | DefaultFloat = DefaultFloat(1.0),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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
        self,
        _sidechain: "AudioStream",
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        mode: int | DefaultInt = DefaultInt(0),
        range: float | DefaultFloat = DefaultFloat(0.06125),
        threshold: float | DefaultFloat = DefaultFloat(0.125),
        ratio: float | DefaultFloat = DefaultFloat(2.0),
        attack: float | DefaultFloat = DefaultFloat(20.0),
        release: float | DefaultFloat = DefaultFloat(250.0),
        makeup: float | DefaultFloat = DefaultFloat(1.0),
        knee: float | DefaultFloat = DefaultFloat(2.828427125),
        detection: int | DefaultInt = DefaultInt(1),
        link: int | DefaultInt = DefaultInt(0),
        level_sc: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
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
            input_typings=[StreamType.audio, StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
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

    def silencedetect(
        self,
        *,
        n: float | DefaultFloat = DefaultFloat(0.001),
        d: int | DefaultInt = DefaultInt(2000000),
        mono: bool | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.107 silencedetect
        Detect silence in an audio stream.

        This filter logs a message when it detects that the input audio volume is less
        or equal to a noise tolerance value for a duration greater or equal to the
        minimum detected noise duration.

        The printed times and duration are expressed in seconds. The
        lavfi.silence_start or lavfi.silence_start.X metadata key
        is set on the first frame whose timestamp equals or exceeds the detection
        duration and it contains the timestamp of the first frame of the silence.

        The lavfi.silence_duration or lavfi.silence_duration.X
        and lavfi.silence_end or lavfi.silence_end.X metadata
        keys are set on the first frame after the silence. If mono is
        enabled, and each channel is evaluated separately, the .X
        suffixed keys are used, and X corresponds to the channel number.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float n: Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default is -60dB, or 0.001.
        :param int d: Set silence duration until notification (default is 2 seconds). See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax.
        :param bool mono: Process each channel separately, instead of combined. By default is disabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silencedetect

        """
        filter_node = FilterNode(
            name="silencedetect",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "n": n,
                "d": d,
                "mono": mono,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def silenceremove(
        self,
        *,
        start_periods: int | DefaultInt = DefaultInt(0),
        start_duration: int | DefaultInt = DefaultInt(0),
        start_threshold: float | DefaultFloat = DefaultFloat(0.0),
        start_silence: int | DefaultInt = DefaultInt(0),
        start_mode: int | DefaultStr = DefaultStr("T_ANY"),
        stop_periods: int | DefaultInt = DefaultInt(0),
        stop_duration: int | DefaultInt = DefaultInt(0),
        stop_threshold: float | DefaultFloat = DefaultFloat(0.0),
        stop_silence: int | DefaultInt = DefaultInt(0),
        stop_mode: int | DefaultStr = DefaultStr("T_ALL"),
        detection: int | DefaultStr = DefaultStr("D_RMS"),
        window: int | DefaultInt = DefaultInt(20000),
        timestamp: int | DefaultStr = DefaultStr("TS_WRITE"),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.108 silenceremove
        Remove silence from the beginning, middle or end of the audio.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int start_periods: This value is used to indicate if audio should be trimmed at beginning of the audio. A value of zero indicates no silence should be trimmed from the beginning. When specifying a non-zero value, it trims audio up until it finds non-silence. Normally, when trimming silence from beginning of audio the start_periods will be 1 but it can be increased to higher values to trim all audio up to specific count of non-silence periods. Default value is 0.
        :param int start_duration: Specify the amount of time that non-silence must be detected before it stops trimming audio. By increasing the duration, bursts of noises can be treated as silence and trimmed off. Default value is 0.
        :param float start_threshold: This indicates what sample value should be treated as silence. For digital audio, a value of 0 may be fine but for audio recorded from analog, you may wish to increase the value to account for background noise. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default value is 0.
        :param int start_silence: Specify max duration of silence at beginning that will be kept after trimming. Default is 0, which is equal to trimming all samples detected as silence.
        :param int start_mode: Specify mode of detection of silence end at start of multi-channel audio. Can be any or all. Default is any. With any, any sample from any channel that is detected as non-silence will trigger end of silence trimming at start of audio stream. With all, only if every sample from every channel is detected as non-silence will trigger end of silence trimming at start of audio stream, limited usage.
        :param int stop_periods: Set the count for trimming silence from the end of audio. When specifying a positive value, it trims audio after it finds specified silence period. To remove silence from the middle of a file, specify a stop_periods that is negative. This value is then treated as a positive value and is used to indicate the effect should restart processing as specified by stop_periods, making it suitable for removing periods of silence in the middle of the audio. Default value is 0.
        :param int stop_duration: Specify a duration of silence that must exist before audio is not copied any more. By specifying a higher duration, silence that is wanted can be left in the audio. Default value is 0.
        :param float stop_threshold: This is the same as start_threshold but for trimming silence from the end of audio. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default value is 0.
        :param int stop_silence: Specify max duration of silence at end that will be kept after trimming. Default is 0, which is equal to trimming all samples detected as silence.
        :param int stop_mode: Specify mode of detection of silence start after start of multi-channel audio. Can be any or all. Default is all. With any, any sample from any channel that is detected as silence will trigger start of silence trimming after start of audio stream, limited usage. With all, only if every sample from every channel is detected as silence will trigger start of silence trimming after start of audio stream.
        :param int detection: Set how is silence detected. avg Mean of absolute values of samples in moving window. rms Root squared mean of absolute values of samples in moving window. peak Maximum of absolute values of samples in moving window. median Median of absolute values of samples in moving window. ptp Absolute of max peak to min peak difference of samples in moving window. dev Standard deviation of values of samples in moving window. Default value is rms.
        :param int window: Set duration in number of seconds used to calculate size of window in number of samples for detecting silence. Using 0 will effectively disable any windowing and use only single sample per channel for silence detection. In that case it may be needed to also set start_silence and/or stop_silence to nonzero values with also start_duration and/or stop_duration to nonzero values. Default value is 0.02. Allowed range is from 0 to 10.
        :param int timestamp: Set processing mode of every audio frame output timestamp. write Full timestamps rewrite, keep only the start time for the first output frame. copy Non-dropped frames are left with same timestamp as input audio frame. Defaults value is write.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silenceremove

        """
        filter_node = FilterNode(
            name="silenceremove",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def sofalizer(
        self,
        *,
        sofa: str,
        gain: float | DefaultFloat = DefaultFloat(0.0),
        rotation: float | DefaultFloat = DefaultFloat(0.0),
        elevation: float | DefaultFloat = DefaultFloat(0.0),
        radius: float | DefaultFloat = DefaultFloat(1.0),
        type: int | DefaultInt = DefaultInt(1),
        speakers: str,
        lfegain: float | DefaultFloat = DefaultFloat(0.0),
        framesize: int | DefaultInt = DefaultInt(1024),
        normalize: bool | DefaultInt = DefaultInt(1),
        interpolate: bool | DefaultInt = DefaultInt(0),
        minphase: bool | DefaultInt = DefaultInt(0),
        anglestep: float | DefaultFloat = DefaultFloat(0.5),
        radstep: float | DefaultFloat = DefaultFloat(0.01),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.109 sofalizer
        SOFAlizer uses head-related transfer functions (HRTFs) to create virtual
        loudspeakers around the user for binaural listening via headphones (audio
        formats up to 9 channels supported).
        The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database).
        SOFAlizer is developed at the Acoustics Research Institute (ARI) of the
        Austrian Academy of Sciences.

        To enable compilation of this filter you need to configure FFmpeg with
        --enable-libmysofa.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str sofa: Set the SOFA file used for rendering.
        :param float gain: Set gain applied to audio. Value is in dB. Default is 0.
        :param float rotation: Set rotation of virtual loudspeakers in deg. Default is 0.
        :param float elevation: Set elevation of virtual speakers in deg. Default is 0.
        :param float radius: Set distance in meters between loudspeakers and the listener with near-field HRTFs. Default is 1.
        :param int type: Set processing type. Can be time or freq. time is processing audio in time domain which is slow. freq is processing audio in frequency domain which is fast. Default is freq.
        :param str speakers: Set custom positions of virtual loudspeakers. Syntax for this option is: <CH> <AZIM> <ELEV>[|<CH> <AZIM> <ELEV>|...]. Each virtual loudspeaker is described with short channel name following with azimuth and elevation in degrees. Each virtual loudspeaker description is separated by ’|’. For example to override front left and front right channel positions use: ’speakers=FL 45 15|FR 345 15’. Descriptions with unrecognised channel names are ignored.
        :param float lfegain: Set custom gain for LFE channels. Value is in dB. Default is 0.
        :param int framesize: Set custom frame size in number of samples. Default is 1024. Allowed range is from 1024 to 96000. Only used if option ‘type’ is set to freq.
        :param bool normalize: Should all IRs be normalized upon importing SOFA file. By default is enabled.
        :param bool interpolate: Should nearest IRs be interpolated with neighbor IRs if exact position does not match. By default is disabled.
        :param bool minphase: Minphase all IRs upon loading of SOFA file. By default is disabled.
        :param float anglestep: Set neighbor search angle step. Only used if option interpolate is enabled.
        :param float radstep: Set neighbor search radius step. Only used if option interpolate is enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sofalizer

        """
        filter_node = FilterNode(
            name="sofalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "sofa": sofa,
                "gain": gain,
                "rotation": rotation,
                "elevation": elevation,
                "radius": radius,
                "type": type,
                "speakers": speakers,
                "lfegain": lfegain,
                "framesize": framesize,
                "normalize": normalize,
                "interpolate": interpolate,
                "minphase": minphase,
                "anglestep": anglestep,
                "radstep": radstep,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def speechnorm(
        self,
        *,
        peak: float | DefaultFloat = DefaultFloat(0.95),
        expansion: float | DefaultFloat = DefaultFloat(2.0),
        compression: float | DefaultFloat = DefaultFloat(2.0),
        threshold: float | DefaultFloat = DefaultFloat(0.0),
        _raise: float | DefaultFloat = DefaultFloat(0.001),
        fall: float | DefaultFloat = DefaultFloat(0.001),
        channels: str | DefaultStr = DefaultStr("all"),
        invert: bool | DefaultInt = DefaultInt(0),
        link: bool | DefaultInt = DefaultInt(0),
        rms: float | DefaultFloat = DefaultFloat(0.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.110 speechnorm
        Speech Normalizer.

        This filter expands or compresses each half-cycle of audio samples
        (local set of samples all above or all below zero and between two nearest zero crossings) depending
        on threshold value, so audio reaches target peak value under conditions controlled by below options.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float peak: Set the expansion target peak value. This specifies the highest allowed absolute amplitude level for the normalized audio input. Default value is 0.95. Allowed range is from 0.0 to 1.0.
        :param float expansion: Set the maximum expansion factor. Allowed range is from 1.0 to 50.0. Default value is 2.0. This option controls maximum local half-cycle of samples expansion. The maximum expansion would be such that local peak value reaches target peak value but never to surpass it and that ratio between new and previous peak value does not surpass this option value.
        :param float compression: Set the maximum compression factor. Allowed range is from 1.0 to 50.0. Default value is 2.0. This option controls maximum local half-cycle of samples compression. This option is used only if threshold option is set to value greater than 0.0, then in such cases when local peak is lower or same as value set by threshold all samples belonging to that peak’s half-cycle will be compressed by current compression factor.
        :param float threshold: Set the threshold value. Default value is 0.0. Allowed range is from 0.0 to 1.0. This option specifies which half-cycles of samples will be compressed and which will be expanded. Any half-cycle samples with their local peak value below or same as this option value will be compressed by current compression factor, otherwise, if greater than threshold value they will be expanded with expansion factor so that it could reach peak target value but never surpass it.
        :param float _raise: Set the expansion raising amount per each half-cycle of samples. Default value is 0.001. Allowed range is from 0.0 to 1.0. This controls how fast expansion factor is raised per each new half-cycle until it reaches expansion value. Setting this options too high may lead to distortions.
        :param float fall: Set the compression raising amount per each half-cycle of samples. Default value is 0.001. Allowed range is from 0.0 to 1.0. This controls how fast compression factor is raised per each new half-cycle until it reaches compression value.
        :param str channels: Specify which channels to filter, by default all available channels are filtered.
        :param bool invert: Enable inverted filtering, by default is disabled. This inverts interpretation of threshold option. When enabled any half-cycle of samples with their local peak value below or same as threshold option will be expanded otherwise it will be compressed.
        :param bool link: Link channels when calculating gain applied to each filtered channel sample, by default is disabled. When disabled each filtered channel gain calculation is independent, otherwise when this option is enabled the minimum of all possible gains for each filtered channel is used.
        :param float rms: Set the expansion target RMS value. This specifies the highest allowed RMS level for the normalized audio input. Default value is 0.0, thus disabled. Allowed range is from 0.0 to 1.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#speechnorm

        """
        filter_node = FilterNode(
            name="speechnorm",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def stereotools(
        self,
        *,
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        balance_in: float | DefaultFloat = DefaultFloat(0.0),
        balance_out: float | DefaultFloat = DefaultFloat(0.0),
        softclip: bool | DefaultInt = DefaultInt(0),
        mutel: bool | DefaultInt = DefaultInt(0),
        muter: bool | DefaultInt = DefaultInt(0),
        phasel: bool | DefaultInt = DefaultInt(0),
        phaser: bool | DefaultInt = DefaultInt(0),
        mode: int | DefaultInt = DefaultInt(0),
        slev: float | DefaultFloat = DefaultFloat(1.0),
        sbal: float | DefaultFloat = DefaultFloat(0.0),
        mlev: float | DefaultFloat = DefaultFloat(1.0),
        mpan: float | DefaultFloat = DefaultFloat(0.0),
        base: float | DefaultFloat = DefaultFloat(0.0),
        delay: float | DefaultFloat = DefaultFloat(0.0),
        sclevel: float | DefaultFloat = DefaultFloat(1.0),
        phase: float | DefaultFloat = DefaultFloat(0.0),
        bmode_in: int | DefaultInt = DefaultInt(0),
        bmode_out: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.111 stereotools
        This filter has some handy utilities to manage stereo signals, for converting
        M/S stereo recordings to L/R signal while having control over the parameters
        or spreading the stereo image of master track.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float level_in: Set input level before filtering for both channels. Defaults is 1. Allowed range is from 0.015625 to 64.
        :param float level_out: Set output level after filtering for both channels. Defaults is 1. Allowed range is from 0.015625 to 64.
        :param float balance_in: Set input balance between both channels. Default is 0. Allowed range is from -1 to 1.
        :param float balance_out: Set output balance between both channels. Default is 0. Allowed range is from -1 to 1.
        :param bool softclip: Enable softclipping. Results in analog distortion instead of harsh digital 0dB clipping. Disabled by default.
        :param bool mutel: Mute the left channel. Disabled by default.
        :param bool muter: Mute the right channel. Disabled by default.
        :param bool phasel: Change the phase of the left channel. Disabled by default.
        :param bool phaser: Change the phase of the right channel. Disabled by default.
        :param int mode: Set stereo mode. Available values are: ‘lr>lr’ Left/Right to Left/Right, this is default. ‘lr>ms’ Left/Right to Mid/Side. ‘ms>lr’ Mid/Side to Left/Right. ‘lr>ll’ Left/Right to Left/Left. ‘lr>rr’ Left/Right to Right/Right. ‘lr>l+r’ Left/Right to Left + Right. ‘lr>rl’ Left/Right to Right/Left. ‘ms>ll’ Mid/Side to Left/Left. ‘ms>rr’ Mid/Side to Right/Right. ‘ms>rl’ Mid/Side to Right/Left. ‘lr>l-r’ Left/Right to Left - Right.
        :param float slev: Set level of side signal. Default is 1. Allowed range is from 0.015625 to 64.
        :param float sbal: Set balance of side signal. Default is 0. Allowed range is from -1 to 1.
        :param float mlev: Set level of the middle signal. Default is 1. Allowed range is from 0.015625 to 64.
        :param float mpan: Set middle signal pan. Default is 0. Allowed range is from -1 to 1.
        :param float base: Set stereo base between mono and inversed channels. Default is 0. Allowed range is from -1 to 1.
        :param float delay: Set delay in milliseconds how much to delay left from right channel and vice versa. Default is 0. Allowed range is from -20 to 20.
        :param float sclevel: Set S/C level. Default is 1. Allowed range is from 1 to 100.
        :param float phase: Set the stereo phase in degrees. Default is 0. Allowed range is from 0 to 360.
        :param int bmode_in: Set balance mode for balance_in/balance_out option. Can be one of the following: ‘balance’ Classic balance mode. Attenuate one channel at time. Gain is raised up to 1. ‘amplitude’ Similar as classic mode above but gain is raised up to 2. ‘power’ Equal power distribution, from -6dB to +6dB range.
        :param int bmode_out: Set balance mode for balance_in/balance_out option. Can be one of the following: ‘balance’ Classic balance mode. Attenuate one channel at time. Gain is raised up to 1. ‘amplitude’ Similar as classic mode above but gain is raised up to 2. ‘power’ Equal power distribution, from -6dB to +6dB range.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereotools

        """
        filter_node = FilterNode(
            name="stereotools",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def stereowiden(
        self,
        *,
        delay: float | DefaultFloat = DefaultFloat(20.0),
        feedback: float | DefaultFloat = DefaultFloat(0.3),
        crossfeed: float | DefaultFloat = DefaultFloat(0.3),
        drymix: float | DefaultFloat = DefaultFloat(0.8),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.112 stereowiden
        This filter enhance the stereo effect by suppressing signal common to both
        channels and by delaying the signal of left into right and vice versa,
        thereby widening the stereo effect.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float delay: Time in milliseconds of the delay of left signal into right and vice versa. Default is 20 milliseconds.
        :param float feedback: Amount of gain in delayed signal into right and vice versa. Gives a delay effect of left signal in right output and vice versa which gives widening effect. Default is 0.3.
        :param float crossfeed: Cross feed of left into right with inverted phase. This helps in suppressing the mono. If the value is 1 it will cancel all the signal common to both channels. Default is 0.3.
        :param float drymix: Set level of input signal of original channel. Default is 0.8.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereowiden

        """
        filter_node = FilterNode(
            name="stereowiden",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "delay": delay,
                "feedback": feedback,
                "crossfeed": crossfeed,
                "drymix": drymix,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def superequalizer(
        self,
        *,
        _1b: float | DefaultFloat = DefaultFloat(1.0),
        _2b: float | DefaultFloat = DefaultFloat(1.0),
        _3b: float | DefaultFloat = DefaultFloat(1.0),
        _4b: float | DefaultFloat = DefaultFloat(1.0),
        _5b: float | DefaultFloat = DefaultFloat(1.0),
        _6b: float | DefaultFloat = DefaultFloat(1.0),
        _7b: float | DefaultFloat = DefaultFloat(1.0),
        _8b: float | DefaultFloat = DefaultFloat(1.0),
        _9b: float | DefaultFloat = DefaultFloat(1.0),
        _10b: float | DefaultFloat = DefaultFloat(1.0),
        _11b: float | DefaultFloat = DefaultFloat(1.0),
        _12b: float | DefaultFloat = DefaultFloat(1.0),
        _13b: float | DefaultFloat = DefaultFloat(1.0),
        _14b: float | DefaultFloat = DefaultFloat(1.0),
        _15b: float | DefaultFloat = DefaultFloat(1.0),
        _16b: float | DefaultFloat = DefaultFloat(1.0),
        _17b: float | DefaultFloat = DefaultFloat(1.0),
        _18b: float | DefaultFloat = DefaultFloat(1.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.113 superequalizer
        Apply 18 band equalizer.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float _1b: Set 65Hz band gain.
        :param float _2b: Set 92Hz band gain.
        :param float _3b: Set 131Hz band gain.
        :param float _4b: Set 185Hz band gain.
        :param float _5b: Set 262Hz band gain.
        :param float _6b: Set 370Hz band gain.
        :param float _7b: Set 523Hz band gain.
        :param float _8b: Set 740Hz band gain.
        :param float _9b: Set 1047Hz band gain.
        :param float _10b: Set 1480Hz band gain.
        :param float _11b: Set 2093Hz band gain.
        :param float _12b: Set 2960Hz band gain.
        :param float _13b: Set 4186Hz band gain.
        :param float _14b: Set 5920Hz band gain.
        :param float _15b: Set 8372Hz band gain.
        :param float _16b: Set 11840Hz band gain.
        :param float _17b: Set 16744Hz band gain.
        :param float _18b: Set 20000Hz band gain.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#superequalizer

        """
        filter_node = FilterNode(
            name="superequalizer",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def surround(
        self,
        *,
        chl_out: str | DefaultStr = DefaultStr("5.1"),
        chl_in: str | DefaultStr = DefaultStr("stereo"),
        level_in: float | DefaultFloat = DefaultFloat(1.0),
        level_out: float | DefaultFloat = DefaultFloat(1.0),
        lfe: bool | DefaultInt = DefaultInt(1),
        lfe_low: int | DefaultInt = DefaultInt(128),
        lfe_high: int | DefaultInt = DefaultInt(256),
        lfe_mode: int | DefaultInt = DefaultInt(0),
        smooth: float | DefaultFloat = DefaultFloat(0.0),
        angle: float | DefaultFloat = DefaultFloat(90.0),
        focus: float | DefaultFloat = DefaultFloat(0.0),
        fc_in: float | DefaultFloat = DefaultFloat(1.0),
        fc_out: float | DefaultFloat = DefaultFloat(1.0),
        fl_in: float | DefaultFloat = DefaultFloat(1.0),
        fl_out: float | DefaultFloat = DefaultFloat(1.0),
        fr_in: float | DefaultFloat = DefaultFloat(1.0),
        fr_out: float | DefaultFloat = DefaultFloat(1.0),
        sl_in: float | DefaultFloat = DefaultFloat(1.0),
        sl_out: float | DefaultFloat = DefaultFloat(1.0),
        sr_in: float | DefaultFloat = DefaultFloat(1.0),
        sr_out: float | DefaultFloat = DefaultFloat(1.0),
        bl_in: float | DefaultFloat = DefaultFloat(1.0),
        bl_out: float | DefaultFloat = DefaultFloat(1.0),
        br_in: float | DefaultFloat = DefaultFloat(1.0),
        br_out: float | DefaultFloat = DefaultFloat(1.0),
        bc_in: float | DefaultFloat = DefaultFloat(1.0),
        bc_out: float | DefaultFloat = DefaultFloat(1.0),
        lfe_in: float | DefaultFloat = DefaultFloat(1.0),
        lfe_out: float | DefaultFloat = DefaultFloat(1.0),
        allx: float | DefaultFloat = DefaultFloat(-1.0),
        ally: float | DefaultFloat = DefaultFloat(-1.0),
        fcx: float | DefaultFloat = DefaultFloat(0.5),
        flx: float | DefaultFloat = DefaultFloat(0.5),
        frx: float | DefaultFloat = DefaultFloat(0.5),
        blx: float | DefaultFloat = DefaultFloat(0.5),
        brx: float | DefaultFloat = DefaultFloat(0.5),
        slx: float | DefaultFloat = DefaultFloat(0.5),
        srx: float | DefaultFloat = DefaultFloat(0.5),
        bcx: float | DefaultFloat = DefaultFloat(0.5),
        fcy: float | DefaultFloat = DefaultFloat(0.5),
        fly: float | DefaultFloat = DefaultFloat(0.5),
        fry: float | DefaultFloat = DefaultFloat(0.5),
        bly: float | DefaultFloat = DefaultFloat(0.5),
        bry: float | DefaultFloat = DefaultFloat(0.5),
        sly: float | DefaultFloat = DefaultFloat(0.5),
        sry: float | DefaultFloat = DefaultFloat(0.5),
        bcy: float | DefaultFloat = DefaultFloat(0.5),
        win_size: int | DefaultInt = DefaultInt(4096),
        win_func: int | DefaultStr = DefaultStr("WFUNC_HANNING"),
        overlap: float | DefaultFloat = DefaultFloat(0.5),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.114 surround
        Apply audio surround upmix filter.

        This filter allows to produce multichannel output from audio stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str chl_out: Set output channel layout. By default, this is 5.1. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.
        :param str chl_in: Set input channel layout. By default, this is stereo. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.
        :param float level_in: Set input volume level. By default, this is 1.
        :param float level_out: Set output volume level. By default, this is 1.
        :param bool lfe: Enable LFE channel output if output channel layout has it. By default, this is enabled.
        :param int lfe_low: Set LFE low cut off frequency. By default, this is 128 Hz.
        :param int lfe_high: Set LFE high cut off frequency. By default, this is 256 Hz.
        :param int lfe_mode: Set LFE mode, can be add or sub. Default is add. In add mode, LFE channel is created from input audio and added to output. In sub mode, LFE channel is created from input audio and added to output but also all non-LFE output channels are subtracted with output LFE channel.
        :param float smooth: Set temporal smoothness strength, used to gradually change factors when transforming stereo sound in time. Allowed range is from 0.0 to 1.0. Useful to improve output quality with focus option values greater than 0.0. Default is 0.0. Only values inside this range and without edges are effective.
        :param float angle: Set angle of stereo surround transform, Allowed range is from 0 to 360. Default is 90.
        :param float focus: Set focus of stereo surround transform, Allowed range is from -1 to 1. Default is 0.
        :param float fc_in: Set front center input volume. By default, this is 1.
        :param float fc_out: Set front center output volume. By default, this is 1.
        :param float fl_in: Set front left input volume. By default, this is 1.
        :param float fl_out: Set front left output volume. By default, this is 1.
        :param float fr_in: Set front right input volume. By default, this is 1.
        :param float fr_out: Set front right output volume. By default, this is 1.
        :param float sl_in: Set side left input volume. By default, this is 1.
        :param float sl_out: Set side left output volume. By default, this is 1.
        :param float sr_in: Set side right input volume. By default, this is 1.
        :param float sr_out: Set side right output volume. By default, this is 1.
        :param float bl_in: Set back left input volume. By default, this is 1.
        :param float bl_out: Set back left output volume. By default, this is 1.
        :param float br_in: Set back right input volume. By default, this is 1.
        :param float br_out: Set back right output volume. By default, this is 1.
        :param float bc_in: Set back center input volume. By default, this is 1.
        :param float bc_out: Set back center output volume. By default, this is 1.
        :param float lfe_in: Set LFE input volume. By default, this is 1.
        :param float lfe_out: Set LFE output volume. By default, this is 1.
        :param float allx: Set spread usage of stereo image across X axis for all channels. Allowed range is from -1 to 15. By default this value is negative -1, and thus unused.
        :param float ally: Set spread usage of stereo image across Y axis for all channels. Allowed range is from -1 to 15. By default this value is negative -1, and thus unused.
        :param float fcx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float flx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float frx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float blx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float brx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float slx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float srx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float bcx: Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float fcy: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float fly: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float fry: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float bly: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float bry: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float sly: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float sry: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param float bcy: Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        :param int win_size: Set window size. Allowed range is from 1024 to 65536. Default size is 4096.
        :param int win_func: Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        :param float overlap: Set window overlap. If set to 1, the recommended overlap for selected window function will be picked. Default is 0.5.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#surround

        """
        filter_node = FilterNode(
            name="surround",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node.audio(0)

    def tiltshelf(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.115 tiltshelf
        Boost or cut the lower frequencies and cut or boost higher frequencies
        of the audio using a two-pole shelving filter with a response similar to
        that of a standard hi-fi’s tone-controls.
        This is also known as shelving equalisation (EQ).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Determine how steep is the filter’s shelf transition.
        :param float gain: Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tiltshelf

        """
        filter_node = FilterNode(
            name="tiltshelf",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def treble(
        self,
        *,
        frequency: float | DefaultFloat = DefaultFloat(3000.0),
        width_type: int | DefaultStr = DefaultStr("QFACTOR"),
        width: float | DefaultFloat = DefaultFloat(0.5),
        gain: float | DefaultFloat = DefaultFloat(0.0),
        poles: int | DefaultInt = DefaultInt(2),
        mix: float | DefaultFloat = DefaultFloat(1.0),
        channels: str | DefaultStr = DefaultStr("all"),
        normalize: bool | DefaultInt = DefaultInt(0),
        transform: int | DefaultStr = DefaultStr("DI"),
        precision: int | DefaultInt = DefaultInt(-1),
        blocksize: int | DefaultInt = DefaultInt(0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.116 treble, highshelf
        Boost or cut treble (upper) frequencies of the audio using a two-pole
        shelving filter with a response similar to that of a standard
        hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).

        The filter accepts the following options:

        Parameters:
        ----------

        :param float frequency: Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        :param int width_type: Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        :param float width: Determine how steep is the filter’s shelf transition.
        :param float gain: Give the gain at whichever is the lower of ~22 kHz and the Nyquist frequency. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        :param int poles: Set number of poles. Default is 2.
        :param float mix: How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        :param str channels: Specify which channels to filter, by default all available are filtered.
        :param bool normalize: Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        :param int transform: Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        :param int precision: Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        :param int blocksize: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        filter_node = FilterNode(
            name="treble",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def tremolo(
        self, *, f: float | DefaultFloat = DefaultFloat(5.0), d: float | DefaultFloat = DefaultFloat(0.5), **kwargs: Any
    ) -> "AudioStream":
        """

        8.117 tremolo
        Sinusoidal amplitude modulation.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float f: Modulation frequency in Hertz. Modulation frequencies in the subharmonic range (20 Hz or lower) will result in a tremolo effect. This filter may also be used as a ring modulator by specifying a modulation frequency higher than 20 Hz. Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        :param float d: Depth of modulation as a percentage. Range is 0.0 - 1.0. Default value is 0.5.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tremolo

        """
        filter_node = FilterNode(
            name="tremolo",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "f": f,
                "d": d,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def vibrato(
        self, *, f: float | DefaultFloat = DefaultFloat(5.0), d: float | DefaultFloat = DefaultFloat(0.5), **kwargs: Any
    ) -> "AudioStream":
        """

        8.118 vibrato
        Sinusoidal phase modulation.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float f: Modulation frequency in Hertz. Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        :param float d: Depth of modulation as a percentage. Range is 0.0 - 1.0. Default value is 0.5.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrato

        """
        filter_node = FilterNode(
            name="vibrato",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "f": f,
                "d": d,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def virtualbass(
        self,
        *,
        cutoff: float | DefaultFloat = DefaultFloat(250.0),
        strength: float | DefaultFloat = DefaultFloat(3.0),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.119 virtualbass
        Apply audio Virtual Bass filter.

        This filter accepts stereo input and produce stereo with LFE (2.1) channels output.
        The newly produced LFE channel have enhanced virtual bass originally obtained from both stereo channels.
        This filter outputs front left and front right channels unchanged as available in stereo input.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float cutoff: Set the virtual bass cutoff frequency. Default value is 250 Hz. Allowed range is from 100 to 500 Hz.
        :param float strength: Set the virtual bass strength. Allowed range is from 0.5 to 3. Default value is 3.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#virtualbass

        """
        filter_node = FilterNode(
            name="virtualbass",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "strength": strength,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def volume(
        self,
        *,
        volume: str | DefaultStr = DefaultStr("1.0"),
        precision: int | DefaultStr = DefaultStr("PRECISION_FLOAT"),
        eval: int | DefaultStr = DefaultStr("EVAL_MODE_ONCE"),
        replaygain: int | DefaultStr = DefaultStr("REPLAYGAIN_DROP"),
        replaygain_preamp: float | DefaultFloat = DefaultFloat(0.0),
        replaygain_noclip: bool | DefaultInt = DefaultInt(1),
        **kwargs: Any,
    ) -> "AudioStream":
        """

        8.120 volume
        Adjust the input audio volume.

        It accepts the following parameters:

        The volume expression can contain the following parameters.


        Note that when eval is set to ‘once’ only the
        sample_rate and tb variables are available, all other
        variables will evaluate to NAN.

        Parameters:
        ----------

        :param str volume: Set audio volume expression. Output values are clipped to the maximum value. The output audio volume is given by the relation: output_volume = volume * input_volume The default value for volume is "1.0".
        :param int precision: This parameter represents the mathematical precision. It determines which input sample formats will be allowed, which affects the precision of the volume scaling. fixed 8-bit fixed-point; this limits input sample format to U8, S16, and S32. float 32-bit floating-point; this limits input sample format to FLT. (default) double 64-bit floating-point; this limits input sample format to DBL.
        :param int eval: Set when the volume expression is evaluated. It accepts the following values: ‘once’ only evaluate expression once during the filter initialization, or when the ‘volume’ command is sent ‘frame’ evaluate expression for each incoming frame Default value is ‘once’.
        :param int replaygain: Choose the behaviour on encountering ReplayGain side data in input frames. drop Remove ReplayGain side data, ignoring its contents (the default). ignore Ignore ReplayGain side data, but leave it in the frame. track Prefer the track gain, if present. album Prefer the album gain, if present.
        :param float replaygain_preamp: Pre-amplification gain in dB to apply to the selected replaygain gain. Default value for replaygain_preamp is 0.0.
        :param bool replaygain_noclip: Prevent clipping by limiting the gain applied. Default value for replaygain_noclip is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#volume

        """
        filter_node = FilterNode(
            name="volume",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={
                "volume": volume,
                "precision": precision,
                "eval": eval,
                "replaygain": replaygain,
                "replaygain_preamp": replaygain_preamp,
                "replaygain_noclip": replaygain_noclip,
            }
            | kwargs,
        )
        return filter_node.audio(0)

    def volumedetect(self, **kwargs: Any) -> "AudioStream":
        """

        8.121 volumedetect
        Detect the volume of the input video.

        The filter has no parameters. It supports only 16-bit signed integer samples,
        so the input will be converted when needed. Statistics about the volume will
        be printed in the log when the input stream end is reached.

        In particular it will show the mean volume (root mean square), maximum
        volume (on a per-sample basis), and the beginning of a histogram of the
        registered volume values (from the maximum value to a cumulated 1/1000 of
        the samples).

        All volumes are in decibels relative to the maximum PCM value.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#volumedetect

        """
        filter_node = FilterNode(
            name="volumedetect",
            input_typings=[StreamType.audio],
            output_typings=[StreamType.audio],
            inputs=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node.audio(0)
