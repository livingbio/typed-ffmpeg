from typing import Any

from pydantic import BaseModel


class Stream(BaseModel):
    ...


class FilterNode(BaseModel):
    streams: list[Stream]
    name: str
    kwargs: dict[str, str | int | float | bool | None] = {}

    def _vs(self, index: int) -> "VideoStream":
        return VideoStream()

    def _as(self, index: int) -> "AudioStream":
        return AudioStream()


class AudioStream(Stream):
    def a3dscope(
        self,
        *,
        rate: str = None,
        size: str = None,
        fov: float = None,
        roll: float = None,
        pitch: float = None,
        yaw: float = None,
        xzoom: float = None,
        yzoom: float = None,
        zzoom: float = None,
        xpos: float = None,
        ypos: float = None,
        zpos: float = None,
        length: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def aap(
        self,
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
        return filter_node._as(0)

    def abench(self, *, action: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "action": action,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def abitscope(
        self, *, rate: str = None, size: str = None, colors: str = None, mode: int = None, **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def acompressor(
        self,
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
            streams=[
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
        return filter_node._as(0)

    def acontrast(self, *, contrast: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "contrast": contrast,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def acrossfade(
        self,
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
        return filter_node._as(0)

    def acrossover(
        self,
        *,
        split: str = None,
        order: int = None,
        level: float = None,
        gain: str = None,
        precision: int = None,
        **kwargs: Any
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
            streams=[
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
        level_in: float = None,
        level_out: float = None,
        bits: float = None,
        mix: float = None,
        mode: int = None,
        dc: float = None,
        aa: float = None,
        samples: float = None,
        lfo: bool = None,
        lforange: float = None,
        lforate: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def acue(self, *, cue: int = None, preroll: int = None, buffer: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def adeclick(
        self,
        *,
        window: float = None,
        overlap: float = None,
        arorder: float = None,
        threshold: float = None,
        burst: float = None,
        method: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def adeclip(
        self,
        *,
        window: float = None,
        overlap: float = None,
        arorder: float = None,
        threshold: float = None,
        hsize: int = None,
        method: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def adecorrelate(self, *, stages: int = None, seed: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "stages": stages,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def adelay(self, *, delays: str, all: bool = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "delays": delays,
                "all": all,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def adenorm(self, *, level: float = None, type: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "level": level,
                "type": type,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def adrawgraph(
        self,
        *,
        m1: str = None,
        fg1: str = None,
        m2: str = None,
        fg2: str = None,
        m3: str = None,
        fg3: str = None,
        m4: str = None,
        fg4: str = None,
        bg: str = None,
        min: float = None,
        max: float = None,
        mode: int = None,
        slide: int = None,
        size: str = None,
        rate: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def adrc(
        self, *, transfer: str = None, attack: float = None, release: float = None, channels: str = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def adynamicequalizer(
        self,
        *,
        threshold: float = None,
        dfrequency: float = None,
        dqfactor: float = None,
        tfrequency: float = None,
        tqfactor: float = None,
        attack: float = None,
        release: float = None,
        ratio: float = None,
        makeup: float = None,
        range: float = None,
        mode: int = None,
        dftype: int = None,
        tftype: int = None,
        auto: int = None,
        precision: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def adynamicsmooth(self, *, sensitivity: float = None, basefreq: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "sensitivity": sensitivity,
                "basefreq": basefreq,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def aecho(
        self, *, in_gain: float = None, out_gain: float = None, delays: str = None, decays: str = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def aemphasis(
        self, *, level_in: float = None, level_out: float = None, mode: int = None, type: int = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={
                "exprs": exprs,
                "channel_layout": channel_layout,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def aexciter(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        amount: float = None,
        drive: float = None,
        blend: float = None,
        freq: float = None,
        ceil: float = None,
        listen: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def afade(
        self,
        *,
        type: int = None,
        start_sample: int = None,
        nb_samples: int = None,
        start_time: int = None,
        duration: int = None,
        curve: int = None,
        silence: float = None,
        unity: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def afftdn(
        self,
        *,
        noise_reduction: float = None,
        noise_floor: float = None,
        noise_type: int = None,
        band_noise: str,
        residual_floor: float = None,
        track_noise: bool = None,
        track_residual: bool = None,
        output_mode: int = None,
        adaptivity: float = None,
        floor_offset: float = None,
        noise_link: int = None,
        band_multiplier: float = None,
        sample_noise: int = None,
        gain_smooth: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def afftfilt(
        self,
        *,
        real: str = None,
        imag: str = None,
        win_size: int = None,
        win_func: int = None,
        overlap: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def afir(
        self,
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
                self,
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={
                "sample_fmts": sample_fmts,
                "sample_rates": sample_rates,
                "channel_layouts": channel_layouts,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def afreqshift(
        self, *, shift: float = None, level: float = None, order: int = None, **kwargs: Any
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
            streams=[
                self,
            ],
            kwargs={
                "shift": shift,
                "level": level,
                "order": order,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def afwtdn(
        self,
        *,
        sigma: float = None,
        levels: int = None,
        wavet: int = None,
        percent: float = None,
        profile: bool = None,
        adaptive: bool = None,
        samples: int = None,
        softness: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def agate(
        self,
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
            streams=[
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
        return filter_node._as(0)

    def agraphmonitor(
        self,
        *,
        size: str = None,
        opacity: float = None,
        mode: str = None,
        flags: str = None,
        rate: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def ahistogram(
        self,
        *,
        dmode: int = None,
        rate: str = None,
        size: str = None,
        scale: int = None,
        ascale: int = None,
        acount: int = None,
        rheight: float = None,
        slide: int = None,
        hmode: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def aiir(
        self,
        *,
        zeros: str = None,
        poles: str = None,
        gains: str = None,
        dry: float = None,
        wet: float = None,
        format: int = None,
        process: int = None,
        precision: int = None,
        normalize: bool = None,
        mix: float = None,
        response: bool = None,
        channel: int = None,
        size: str = None,
        rate: str = None,
        **kwargs: Any
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
            streams=[
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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def ainterleave(
        self, *streams: "AudioStream", nb_inputs: int = None, duration: int = None, **kwargs: Any
    ) -> "AudioStream":
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
                self,
                *streams,
            ],
            kwargs={
                "nb_inputs": nb_inputs,
                "duration": duration,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def alimiter(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        limit: float = None,
        attack: float = None,
        release: float = None,
        asc: bool = None,
        asc_level: float = None,
        level: bool = None,
        latency: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def allpass(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        order: int = None,
        transform: int = None,
        precision: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def aloop(
        self, *, loop: int = None, size: int = None, start: int = None, time: int = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def amerge(self, *streams: "AudioStream", inputs: int = None, **kwargs: Any) -> "AudioStream":
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def ametadata(
        self,
        *,
        mode: int = None,
        key: str,
        value: str,
        function: int = None,
        expr: str,
        file: str,
        direct: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def amix(
        self,
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
                self,
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
        return filter_node._as(0)

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
            streams=[
                self,
                _multiply1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def anequalizer(
        self,
        *,
        params: str = None,
        curves: bool = None,
        size: str = None,
        mgain: float = None,
        fscale: int = None,
        colors: str = None,
        **kwargs: Any
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
            streams=[
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
        strength: float = None,
        patch: int = None,
        research: int = None,
        output: int = None,
        smooth: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def anlmf(
        self,
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
        return filter_node._as(0)

    def anlms(
        self,
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def apad(
        self,
        *,
        packet_size: int = None,
        pad_len: int = None,
        whole_len: int = None,
        pad_dur: int = None,
        whole_dur: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def aperms(self, *, mode: int = None, seed: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def aphasemeter(
        self,
        *,
        rate: str = None,
        size: str = None,
        rc: int = None,
        gc: int = None,
        bc: int = None,
        mpc: str = None,
        video: bool = None,
        phasing: bool = None,
        tolerance: float = None,
        angle: float = None,
        duration: int = None,
        **kwargs: Any
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
            streams=[
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
        in_gain: float = None,
        out_gain: float = None,
        delay: float = None,
        decay: float = None,
        speed: float = None,
        type: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def aphaseshift(
        self, *, shift: float = None, level: float = None, order: int = None, **kwargs: Any
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
            streams=[
                self,
            ],
            kwargs={
                "shift": shift,
                "level": level,
                "order": order,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def apsyclip(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        clip: float = None,
        diff: bool = None,
        adaptive: float = None,
        iterations: int = None,
        level: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def apulsator(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        mode: int = None,
        amount: float = None,
        offset_l: float = None,
        offset_r: float = None,
        width: float = None,
        timing: int = None,
        bpm: float = None,
        ms: int = None,
        hz: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def arealtime(self, *, limit: int = None, speed: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "limit": limit,
                "speed": speed,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def aresample(self, *, sample_rate: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "sample_rate": sample_rate,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def arls(
        self,
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
        return filter_node._as(0)

    def arnndn(self, *, model: str, mix: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "model": model,
                "mix": mix,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={
                "timestamps": timestamps,
                "samples": samples,
            }
            | kwargs,
        )

        return filter_node

    def aselect(self, *, expr: str = None, outputs: int = None, **kwargs: Any) -> FilterNode:
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
            streams=[
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
            streams=[
                self,
            ],
            kwargs={
                "commands": commands,
                "filename": filename,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asetnsamples(self, *, nb_out_samples: int = None, pad: bool = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "nb_out_samples": nb_out_samples,
                "pad": pad,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asetpts(self, *, expr: str = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asetrate(self, *, sample_rate: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "sample_rate": sample_rate,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asettb(self, *, expr: str = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def asidedata(self, *, mode: int = None, type: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "type": type,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
                _input1,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def asoftclip(
        self,
        *,
        type: int = None,
        threshold: float = None,
        output: float = None,
        param: float = None,
        oversample: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def aspectralstats(
        self, *, win_size: int = None, win_func: int = None, overlap: float = None, measure: str = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def asplit(self, *, outputs: int = None, **kwargs: Any) -> FilterNode:
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
            streams=[
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
        rate: int = None,
        hmm: str,
        dict: str,
        lm: str,
        lmctl: str,
        lmname: str,
        logfn: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def astats(
        self,
        *,
        length: float = None,
        metadata: bool = None,
        reset: int = None,
        measure_perchannel: str = None,
        measure_overall: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def astreamselect(self, *streams: "AudioStream", inputs: int = None, map: str, **kwargs: Any) -> FilterNode:
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "map": map,
            }
            | kwargs,
        )

        return filter_node

    def asubboost(
        self,
        *,
        dry: float = None,
        wet: float = None,
        boost: float = None,
        decay: float = None,
        feedback: float = None,
        cutoff: float = None,
        slope: float = None,
        delay: float = None,
        channels: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def asubcut(self, *, cutoff: float = None, order: int = None, level: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asupercut(
        self, *, cutoff: float = None, order: int = None, level: float = None, **kwargs: Any
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
            streams=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def asuperpass(
        self, *, centerf: float = None, order: int = None, qfactor: float = None, level: float = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def asuperstop(
        self, *, centerf: float = None, order: int = None, qfactor: float = None, level: float = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def atempo(self, *, tempo: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "tempo": tempo,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def atilt(
        self,
        *,
        freq: float = None,
        slope: float = None,
        width: float = None,
        order: int = None,
        level: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def atrim(
        self,
        *,
        start: int = None,
        end: int = None,
        start_pts: int = None,
        end_pts: int = None,
        duration: int = None,
        start_sample: int = None,
        end_sample: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def avectorscope(
        self,
        *,
        mode: int = None,
        rate: str = None,
        size: str = None,
        rc: int = None,
        gc: int = None,
        bc: int = None,
        ac: int = None,
        rf: int = None,
        gf: int = None,
        bf: int = None,
        af: int = None,
        zoom: float = None,
        draw: int = None,
        scale: int = None,
        swap: bool = None,
        mirror: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def axcorrelate(
        self, _axcorrelate1: "AudioStream", *, size: int = None, algo: int = None, **kwargs: Any
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
                self,
                _axcorrelate1,
            ],
            kwargs={
                "size": size,
                "algo": algo,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def bandpass(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        csg: bool = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def bandreject(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def bass(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def biquad(
        self,
        *,
        a0: float = None,
        a1: float = None,
        a2: float = None,
        b0: float = None,
        b1: float = None,
        b2: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def bs2b(self, *, profile: int = None, fcut: int = None, feed: int = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "profile": profile,
                "fcut": fcut,
                "feed": feed,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={
                "map": map,
                "channel_layout": channel_layout,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def channelsplit(self, *, channel_layout: str = None, channels: str = None, **kwargs: Any) -> FilterNode:
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
            streams=[
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
        in_gain: float = None,
        out_gain: float = None,
        delays: str,
        decays: str,
        speeds: str,
        depths: str,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def compand(
        self,
        *,
        attacks: str = None,
        decays: str = None,
        points: str = None,
        soft_knee: float = None,
        gain: float = None,
        volume: float = None,
        delay: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def compensationdelay(
        self,
        *,
        mm: int = None,
        cm: int = None,
        m: int = None,
        dry: float = None,
        wet: float = None,
        temp: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def concat(
        self, *streams: "AudioStream", n: int = None, v: int = None, a: int = None, unsafe: bool = None, **kwargs: Any
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
                self,
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

    def crossfeed(
        self,
        *,
        strength: float = None,
        range: float = None,
        slope: float = None,
        level_in: float = None,
        level_out: float = None,
        block_size: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def crystalizer(self, *, i: float = None, c: bool = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "i": i,
                "c": c,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def dcshift(self, *, shift: float = None, limitergain: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "shift": shift,
                "limitergain": limitergain,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def deesser(
        self, *, i: float = None, m: float = None, f: float = None, s: int = None, **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def dialoguenhance(
        self, *, original: float = None, enhance: float = None, voice: float = None, **kwargs: Any
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
            streams=[
                self,
            ],
            kwargs={
                "original": original,
                "enhance": enhance,
                "voice": voice,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def drmeter(self, *, length: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "length": length,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def dynaudnorm(
        self,
        *,
        framelen: int = None,
        gausssize: int = None,
        peak: float = None,
        maxgain: float = None,
        targetrms: float = None,
        coupling: bool = None,
        correctdc: bool = None,
        altboundary: bool = None,
        compress: float = None,
        threshold: float = None,
        channels: str = None,
        overlap: float = None,
        curve: str,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)

    def ebur128(
        self,
        *,
        video: bool = None,
        size: str = None,
        meter: int = None,
        framelog: int = None,
        metadata: bool = None,
        peak: str = None,
        dualmono: bool = None,
        panlaw: float = None,
        target: int = None,
        gauge: int = None,
        scale: int = None,
        integrated: float = None,
        range: float = None,
        lra_low: float = None,
        lra_high: float = None,
        sample_peak: float = None,
        true_peak: float = None,
        **kwargs: Any
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
            streams=[
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
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def extrastereo(self, *, m: float = None, c: bool = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "m": m,
                "c": c,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def firequalizer(
        self,
        *,
        gain: str = None,
        gain_entry: str,
        delay: float = None,
        accuracy: float = None,
        wfunc: int = None,
        fixed: bool = None,
        multi: bool = None,
        zero_phase: bool = None,
        scale: int = None,
        dumpfile: str,
        dumpscale: int = None,
        fft2: bool = None,
        min_phase: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def flanger(
        self,
        *,
        delay: float = None,
        depth: float = None,
        regen: float = None,
        width: float = None,
        speed: float = None,
        shape: int = None,
        phase: float = None,
        interp: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def haas(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        side_gain: float = None,
        middle_source: int = None,
        middle_phase: bool = None,
        left_delay: float = None,
        left_balance: float = None,
        left_gain: float = None,
        left_phase: bool = None,
        right_delay: float = None,
        right_balance: float = None,
        right_gain: float = None,
        right_phase: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def hdcd(
        self,
        *,
        disable_autoconvert: bool = None,
        process_stereo: bool = None,
        cdt_ms: int = None,
        force_pe: bool = None,
        analyze_mode: int = None,
        bits_per_sample: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def headphone(
        self,
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
                self,
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
        return filter_node._as(0)

    def highpass(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def highshelf(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def join(
        self, *streams: "AudioStream", inputs: int = None, channel_layout: str = None, map: str, **kwargs: Any
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "channel_layout": channel_layout,
                "map": map,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def ladspa(
        self,
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
                self,
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
        return filter_node._as(0)

    def loudnorm(
        self,
        *,
        I: float = None,
        LRA: float = None,
        TP: float = None,
        measured_I: float = None,
        measured_LRA: float = None,
        measured_TP: float = None,
        measured_thresh: float = None,
        offset: float = None,
        linear: bool = None,
        dual_mono: bool = None,
        print_format: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def lowpass(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def lowshelf(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def lv2(
        self,
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
                self,
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
        return filter_node._as(0)

    def mcompand(self, *, args: str = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "args": args,
            }
            | kwargs,
        )
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={
                "args": args,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def replaygain(self, *, track_gain: float = None, track_peak: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "track_gain": track_gain,
                "track_peak": track_peak,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def rubberband(
        self,
        *,
        tempo: float = None,
        pitch: float = None,
        transients: int = None,
        detector: int = None,
        phase: int = None,
        window: int = None,
        smoothing: int = None,
        formant: int = None,
        pitchq: int = None,
        channels: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def showcqt(
        self,
        *,
        size: str = None,
        fps: str = None,
        bar_h: int = None,
        axis_h: int = None,
        sono_h: int = None,
        fullhd: bool = None,
        sono_v: str = None,
        bar_v: str = None,
        sono_g: float = None,
        bar_g: float = None,
        bar_t: float = None,
        timeclamp: float = None,
        attack: float = None,
        basefreq: float = None,
        endfreq: float = None,
        coeffclamp: float = None,
        tlength: str = None,
        count: int = None,
        fcount: int = None,
        fontfile: str,
        font: str,
        fontcolor: str = None,
        axisfile: str,
        axis: bool = None,
        csp: int = None,
        cscheme: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showcwt(
        self,
        *,
        size: str = None,
        rate: str = None,
        scale: int = None,
        iscale: int = None,
        min: float = None,
        max: float = None,
        imin: float = None,
        imax: float = None,
        logb: float = None,
        deviation: float = None,
        pps: int = None,
        mode: int = None,
        slide: int = None,
        direction: int = None,
        bar: float = None,
        rotation: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showfreqs(
        self,
        *,
        size: str = None,
        rate: str = None,
        mode: int = None,
        ascale: int = None,
        fscale: int = None,
        win_size: int = None,
        win_func: int = None,
        overlap: float = None,
        averaging: int = None,
        colors: str = None,
        cmode: int = None,
        minamp: float = None,
        data: int = None,
        channels: str = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showspatial(
        self, *, size: str = None, win_size: int = None, win_func: int = None, rate: str = None, **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showspectrum(
        self,
        *,
        size: str = None,
        slide: int = None,
        mode: int = None,
        color: int = None,
        scale: int = None,
        fscale: int = None,
        saturation: float = None,
        win_func: int = None,
        orientation: int = None,
        overlap: float = None,
        gain: float = None,
        data: int = None,
        rotation: float = None,
        start: int = None,
        stop: int = None,
        fps: str = None,
        legend: bool = None,
        drange: float = None,
        limit: float = None,
        opacity: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showspectrumpic(
        self,
        *,
        size: str = None,
        mode: int = None,
        color: int = None,
        scale: int = None,
        fscale: int = None,
        saturation: float = None,
        win_func: int = None,
        orientation: int = None,
        gain: float = None,
        legend: bool = None,
        rotation: float = None,
        start: int = None,
        stop: int = None,
        drange: float = None,
        limit: float = None,
        opacity: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showvolume(
        self,
        *,
        rate: str = None,
        b: int = None,
        w: int = None,
        h: int = None,
        f: float = None,
        c: str = None,
        t: bool = None,
        v: bool = None,
        dm: float = None,
        dmc: str = None,
        o: int = None,
        s: int = None,
        p: float = None,
        m: int = None,
        ds: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showwaves(
        self,
        *,
        size: str = None,
        mode: int = None,
        n: float = None,
        rate: str = None,
        split_channels: bool = None,
        colors: str = None,
        scale: int = None,
        draw: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def showwavespic(
        self,
        *,
        size: str = None,
        split_channels: bool = None,
        colors: str = None,
        scale: int = None,
        draw: int = None,
        filter: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._vs(0)

    def sidechaincompress(
        self,
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
        return filter_node._as(0)

    def sidechaingate(
        self,
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
        return filter_node._as(0)

    def silencedetect(self, *, n: float = None, d: int = None, mono: bool = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "n": n,
                "d": d,
                "mono": mono,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def silenceremove(
        self,
        *,
        start_periods: int = None,
        start_duration: int = None,
        start_threshold: float = None,
        start_silence: int = None,
        start_mode: int = None,
        stop_periods: int = None,
        stop_duration: int = None,
        stop_threshold: float = None,
        stop_silence: int = None,
        stop_mode: int = None,
        detection: int = None,
        window: int = None,
        timestamp: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def sofalizer(
        self,
        *,
        sofa: str,
        gain: float = None,
        rotation: float = None,
        elevation: float = None,
        radius: float = None,
        type: int = None,
        speakers: str,
        lfegain: float = None,
        framesize: int = None,
        normalize: bool = None,
        interpolate: bool = None,
        minphase: bool = None,
        anglestep: float = None,
        radstep: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def speechnorm(
        self,
        *,
        peak: float = None,
        expansion: float = None,
        compression: float = None,
        threshold: float = None,
        _raise: float = None,
        fall: float = None,
        channels: str = None,
        invert: bool = None,
        link: bool = None,
        rms: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def stereotools(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        balance_in: float = None,
        balance_out: float = None,
        softclip: bool = None,
        mutel: bool = None,
        muter: bool = None,
        phasel: bool = None,
        phaser: bool = None,
        mode: int = None,
        slev: float = None,
        sbal: float = None,
        mlev: float = None,
        mpan: float = None,
        base: float = None,
        delay: float = None,
        sclevel: float = None,
        phase: float = None,
        bmode_in: int = None,
        bmode_out: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def stereowiden(
        self,
        *,
        delay: float = None,
        feedback: float = None,
        crossfeed: float = None,
        drymix: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def superequalizer(
        self,
        *,
        _1b: float = None,
        _2b: float = None,
        _3b: float = None,
        _4b: float = None,
        _5b: float = None,
        _6b: float = None,
        _7b: float = None,
        _8b: float = None,
        _9b: float = None,
        _10b: float = None,
        _11b: float = None,
        _12b: float = None,
        _13b: float = None,
        _14b: float = None,
        _15b: float = None,
        _16b: float = None,
        _17b: float = None,
        _18b: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def surround(
        self,
        *,
        chl_out: str = None,
        chl_in: str = None,
        level_in: float = None,
        level_out: float = None,
        lfe: bool = None,
        lfe_low: int = None,
        lfe_high: int = None,
        lfe_mode: int = None,
        smooth: float = None,
        angle: float = None,
        focus: float = None,
        fc_in: float = None,
        fc_out: float = None,
        fl_in: float = None,
        fl_out: float = None,
        fr_in: float = None,
        fr_out: float = None,
        sl_in: float = None,
        sl_out: float = None,
        sr_in: float = None,
        sr_out: float = None,
        bl_in: float = None,
        bl_out: float = None,
        br_in: float = None,
        br_out: float = None,
        bc_in: float = None,
        bc_out: float = None,
        lfe_in: float = None,
        lfe_out: float = None,
        allx: float = None,
        ally: float = None,
        fcx: float = None,
        flx: float = None,
        frx: float = None,
        blx: float = None,
        brx: float = None,
        slx: float = None,
        srx: float = None,
        bcx: float = None,
        fcy: float = None,
        fly: float = None,
        fry: float = None,
        bly: float = None,
        bry: float = None,
        sly: float = None,
        sry: float = None,
        bcy: float = None,
        win_size: int = None,
        win_func: int = None,
        overlap: float = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def tiltshelf(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def treble(
        self,
        *,
        frequency: float = None,
        width_type: int = None,
        width: float = None,
        gain: float = None,
        poles: int = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: int = None,
        precision: int = None,
        blocksize: int = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

    def tremolo(self, *, f: float = None, d: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "f": f,
                "d": d,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def vibrato(self, *, f: float = None, d: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "f": f,
                "d": d,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def virtualbass(self, *, cutoff: float = None, strength: float = None, **kwargs: Any) -> "AudioStream":
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
            streams=[
                self,
            ],
            kwargs={
                "cutoff": cutoff,
                "strength": strength,
            }
            | kwargs,
        )
        return filter_node._as(0)

    def volume(
        self,
        *,
        volume: str = None,
        precision: int = None,
        eval: int = None,
        replaygain: int = None,
        replaygain_preamp: float = None,
        replaygain_noclip: bool = None,
        **kwargs: Any
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
            streams=[
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
        return filter_node._as(0)

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
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._as(0)


class VideoStream(Stream):
    def addroi(
        self,
        *,
        x: str = None,
        y: str = None,
        w: str = None,
        h: str = None,
        qoffset: float = None,
        clear: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.1 addroi
        Mark a region of interest in a video frame.

        The frame data is passed through unchanged, but metadata is attached
        to the frame indicating regions of interest which can affect the
        behaviour of later encoding.  Multiple regions can be marked by
        applying the filter multiple times.

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
            streams=[
                self,
            ],
            kwargs={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "qoffset": qoffset,
                "clear": clear,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def alphaextract(self, **kwargs: Any) -> "VideoStream":
        """

        11.2 alphaextract
        Extract the alpha component from the input as a grayscale video. This
        is especially useful with the alphamerge filter.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#alphaextract

        """
        filter_node = FilterNode(
            name="alphaextract",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def alphamerge(self, _alpha: "VideoStream", **kwargs: Any) -> "VideoStream":
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
                self,
                _alpha,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def amplify(
        self,
        *,
        radius: int = None,
        factor: float = None,
        threshold: float = None,
        tolerance: float = None,
        low: float = None,
        high: float = None,
        planes: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.4 amplify
        Amplify differences between current pixel and pixels of adjacent frames in
        same pixel location.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int radius: Set frame radius. Default is 2. Allowed range is from 1 to 63. For example radius of 3 will instruct filter to calculate average of 7 frames.
        :param float factor: Set factor to amplify difference. Default is 2. Allowed range is from 0 to 65535.
        :param float threshold: Set threshold for difference amplification. Any difference greater or equal to this value will not alter source pixel. Default is 10. Allowed range is from 0 to 65535.
        :param float tolerance: Set tolerance for difference amplification. Any difference lower to this value will not alter source pixel. Default is 0. Allowed range is from 0 to 65535.
        :param float low: Set lower limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will decrease source pixel value.
        :param float high: Set high limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will increase source pixel value.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amplify

        """
        filter_node = FilterNode(
            name="amplify",
            streams=[
                self,
            ],
            kwargs={
                "radius": radius,
                "factor": factor,
                "threshold": threshold,
                "tolerance": tolerance,
                "low": low,
                "high": high,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def atadenoise(
        self,
        *,
        _0a: float = None,
        _0b: float = None,
        _1a: float = None,
        _1b: float = None,
        _2a: float = None,
        _2b: float = None,
        s: int = None,
        p: str = None,
        a: int = None,
        _0s: float = None,
        _1s: float = None,
        _2s: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.6 atadenoise
        Apply an Adaptive Temporal Averaging Denoiser to the video input.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atadenoise

        """
        filter_node = FilterNode(
            name="atadenoise",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def avgblur(self, *, sizeX: int = None, planes: int = None, sizeY: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.7 avgblur
        Apply average blur filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int sizeX: Set horizontal radius size.
        :param int planes: Set which planes to filter. By default all planes are filtered.
        :param int sizeY: Set vertical radius size, if zero it will be same as sizeX. Default is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur

        """
        filter_node = FilterNode(
            name="avgblur",
            streams=[
                self,
            ],
            kwargs={
                "sizeX": sizeX,
                "planes": planes,
                "sizeY": sizeY,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def avgblur_vulkan(
        self, *, sizeX: int = None, sizeY: int = None, planes: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        14.1 avgblur_vulkan
        Apply an average blur filter, implemented on the GPU using Vulkan.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int sizeX: Set horizontal radius size. Range is [1, 32] and default value is 3.
        :param int sizeY: Set vertical radius size. Range is [1, 32] and default value is 3.
        :param int planes: Set which planes to filter. Default value is 0xf, by which all planes are processed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur_005fvulkan

        """
        filter_node = FilterNode(
            name="avgblur_vulkan",
            streams=[
                self,
            ],
            kwargs={
                "sizeX": sizeX,
                "sizeY": sizeY,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def backgroundkey(
        self, *, threshold: float = None, similarity: float = None, blend: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.8 backgroundkey
        Turns a static background into transparency.

        The filter accepts the following option:

        Parameters:
        ----------

        :param float threshold: Threshold for scene change detection.
        :param float similarity: Similarity percentage with the background.
        :param float blend: Set the blend amount for pixels that are not similar.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#backgroundkey

        """
        filter_node = FilterNode(
            name="backgroundkey",
            streams=[
                self,
            ],
            kwargs={
                "threshold": threshold,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bbox(self, *, min_val: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.9 bbox
        Compute the bounding box for the non-black pixels in the input frame
        luma plane.

        This filter computes the bounding box containing all the pixels with a
        luma value greater than the minimum allowed value.
        The parameters describing the bounding box are printed on the filter
        log.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int min_val: Set the minimal luma value. Default is 16.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bbox

        """
        filter_node = FilterNode(
            name="bbox",
            streams=[
                self,
            ],
            kwargs={
                "min_val": min_val,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bench(self, *, action: int = None, **kwargs: Any) -> "VideoStream":
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
            name="bench",
            streams=[
                self,
            ],
            kwargs={
                "action": action,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bilateral(
        self, *, sigmaS: float = None, sigmaR: float = None, planes: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.10 bilateral
        Apply bilateral filter, spatial smoothing while preserving edges.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float sigmaS: Set sigma of gaussian function to calculate spatial weight. Allowed range is 0 to 512. Default is 0.1.
        :param float sigmaR: Set sigma of gaussian function to calculate range weight. Allowed range is 0 to 1. Default is 0.1.
        :param int planes: Set planes to filter. Default is first only.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral

        """
        filter_node = FilterNode(
            name="bilateral",
            streams=[
                self,
            ],
            kwargs={
                "sigmaS": sigmaS,
                "sigmaR": sigmaR,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bilateral_cuda(
        self, *, sigmaS: float = None, sigmaR: float = None, window_size: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.11 bilateral_cuda
        CUDA accelerated bilateral filter, an edge preserving filter.
        This filter is mathematically accurate thanks to the use of GPU acceleration.
        For best output quality, use one to one chroma subsampling, i.e. yuv444p format.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float sigmaS: Set sigma of gaussian function to calculate spatial weight, also called sigma space. Allowed range is 0.1 to 512. Default is 0.1.
        :param float sigmaR: Set sigma of gaussian function to calculate color range weight, also called sigma color. Allowed range is 0.1 to 512. Default is 0.1.
        :param int window_size: Set window size of the bilateral function to determine the number of neighbours to loop on. If the number entered is even, one will be added automatically. Allowed range is 1 to 255. Default is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral_005fcuda

        """
        filter_node = FilterNode(
            name="bilateral_cuda",
            streams=[
                self,
            ],
            kwargs={
                "sigmaS": sigmaS,
                "sigmaR": sigmaR,
                "window_size": window_size,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bitplanenoise(self, *, bitplane: int = None, filter: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.12 bitplanenoise
        Show and measure bit plane noise.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int bitplane: Set which plane to analyze. Default is 1.
        :param bool filter: Filter out noisy pixels from bitplane set above. Default is disabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bitplanenoise

        """
        filter_node = FilterNode(
            name="bitplanenoise",
            streams=[
                self,
            ],
            kwargs={
                "bitplane": bitplane,
                "filter": filter,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def blackdetect(
        self, *, d: float = None, picture_black_ratio_th: float = None, pixel_black_th: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.13 blackdetect
        Detect video intervals that are (almost) completely black. Can be
        useful to detect chapter transitions, commercials, or invalid
        recordings.

        The filter outputs its detection analysis to both the log as well as
        frame metadata. If a black segment of at least the specified minimum
        duration is found, a line with the start and end timestamps as well
        as duration is printed to the log with level info. In addition,
        a log line with level debug is printed per frame showing the
        black amount detected for that frame.

        The filter also attaches metadata to the first frame of a black
        segment with key lavfi.black_start and to the first frame
        after the black segment ends with key lavfi.black_end. The
        value is the frame’s timestamp. This metadata is added regardless
        of the minimum duration specified.

        The filter accepts the following options:


        The following example sets the maximum pixel threshold to the minimum
        value, and detects only black intervals of 2 or more seconds:

        blackdetect=d=2:pix_th=0.00

        Parameters:
        ----------

        :param float d: Set the minimum detected black duration expressed in seconds. It must be a non-negative floating point number. Default value is 2.0.
        :param float picture_black_ratio_th: Set the threshold for considering a picture "black". Express the minimum value for the ratio: nb_black_pixels / nb_pixels for which a picture is considered black. Default value is 0.98.
        :param float pixel_black_th: Set the threshold for considering a pixel "black". The threshold expresses the maximum pixel luma value for which a pixel is considered "black". The provided value is scaled according to the following equation: absolute_threshold = luma_minimum_value + pixel_black_th * luma_range_size luma_range_size and luma_minimum_value depend on the input video format, the range is [0-255] for YUV full-range formats and [16-235] for YUV non full-range formats. Default value is 0.10.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackdetect

        """
        filter_node = FilterNode(
            name="blackdetect",
            streams=[
                self,
            ],
            kwargs={
                "d": d,
                "picture_black_ratio_th": picture_black_ratio_th,
                "pixel_black_th": pixel_black_th,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def blackframe(self, *, amount: int = None, threshold: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.14 blackframe
        Detect frames that are (almost) completely black. Can be useful to
        detect chapter transitions or commercials. Output lines consist of
        the frame number of the detected frame, the percentage of blackness,
        the position in the file if known or -1 and the timestamp in seconds.

        In order to display the output lines, you need to set the loglevel at
        least to the AV_LOG_INFO value.

        This filter exports frame metadata lavfi.blackframe.pblack.
        The value represents the percentage of pixels in the picture that
        are below the threshold value.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int amount: The percentage of the pixels that have to be below the threshold; it defaults to 98.
        :param int threshold: The threshold below which a pixel value is considered black; it defaults to 32.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackframe

        """
        filter_node = FilterNode(
            name="blackframe",
            streams=[
                self,
            ],
            kwargs={
                "amount": amount,
                "threshold": threshold,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def blend(
        self,
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
                self,
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
        return filter_node._vs(0)

    def blend_vulkan(
        self,
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
                self,
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
        return filter_node._vs(0)

    def blockdetect(
        self, *, period_min: int = None, period_max: int = None, planes: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.16 blockdetect
        Determines blockiness of frames without altering the input frames.

        Based on Remco Muijs and Ihor Kirenko: "A no-reference blocking artifact measure for adaptive video processing." 2005 13th European signal processing conference.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int period_min: Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        :param int period_max: Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        :param int planes: Set planes to filter. Default is first only.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blockdetect

        """
        filter_node = FilterNode(
            name="blockdetect",
            streams=[
                self,
            ],
            kwargs={
                "period_min": period_min,
                "period_max": period_max,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def blurdetect(
        self,
        *,
        high: float = None,
        low: float = None,
        radius: int = None,
        block_pct: int = None,
        block_width: int = None,
        block_height: int = None,
        planes: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.17 blurdetect
        Determines blurriness of frames without altering the input frames.

        Based on Marziliano, Pina, et al. "A no-reference perceptual blur metric."
        Allows for a block-based abbreviation.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "high": high,
                "low": low,
                "radius": radius,
                "block_pct": block_pct,
                "block_width": block_width,
                "block_height": block_height,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bm3d(
        self,
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
                self,
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
        return filter_node._vs(0)

    def boxblur(
        self,
        *,
        luma_radius: str = None,
        luma_power: int = None,
        chroma_radius: str,
        chroma_power: int = None,
        alpha_radius: str,
        alpha_power: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.19 boxblur
        Apply a boxblur algorithm to the input video.

        It accepts the following parameters:


        A description of the accepted options follows.

        Parameters:
        ----------

        :param str luma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int luma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str chroma_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int chroma_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.
        :param str alpha_radius: Set an expression for the box radius in pixels used for blurring the corresponding input plane. The radius value must be a non-negative number, and must not be greater than the value of the expression min(w,h)/2 for the luma and alpha planes, and of min(cw,ch)/2 for the chroma planes. Default value for luma_radius is "2". If not specified, chroma_radius and alpha_radius default to the corresponding value set for luma_radius. The expressions can contain the following constants: w h The input width and height in pixels. cw ch The input chroma image width and height in pixels. hsub vsub The horizontal and vertical chroma subsample values. For example, for the pixel format "yuv422p", hsub is 2 and vsub is 1.
        :param int alpha_power: Specify how many times the boxblur filter is applied to the corresponding plane. Default value for luma_power is 2. If not specified, chroma_power and alpha_power default to the corresponding value set for luma_power. A value of 0 will disable the effect.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#boxblur

        """
        filter_node = FilterNode(
            name="boxblur",
            streams=[
                self,
            ],
            kwargs={
                "luma_radius": luma_radius,
                "luma_power": luma_power,
                "chroma_radius": chroma_radius,
                "chroma_power": chroma_power,
                "alpha_radius": alpha_radius,
                "alpha_power": alpha_power,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def bwdif(self, *, mode: int = None, parity: int = None, deint: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.20 bwdif
        Deinterlace the input video ("bwdif" stands for "Bob Weaver
        Deinterlacing Filter").

        Motion adaptive deinterlacing based on yadif with the use of w3fdif and cubic
        interpolation algorithms.
        It accepts the following parameters:

        Parameters:
        ----------

        :param int mode: The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif

        """
        filter_node = FilterNode(
            name="bwdif",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "parity": parity,
                "deint": deint,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def cas(self, *, strength: float = None, planes: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.23 cas
        Apply Contrast Adaptive Sharpen filter to video stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float strength: Set the sharpening strength. Default value is 0.
        :param str planes: Set planes to filter. Default value is to filter all planes except alpha plane.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cas

        """
        filter_node = FilterNode(
            name="cas",
            streams=[
                self,
            ],
            kwargs={
                "strength": strength,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def ccrepack(self, **kwargs: Any) -> "VideoStream":
        """

        11.22 ccrepack
        Repack CEA-708 closed captioning side data

        This filter fixes various issues seen with commerical encoders
        related to upstream malformed CEA-708 payloads, specifically
        incorrect number of tuples (wrong cc_count for the target FPS),
        and incorrect ordering of tuples (i.e. the CEA-608 tuples are not at
        the first entries in the payload).

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#ccrepack

        """
        filter_node = FilterNode(
            name="ccrepack",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def chromaber_vulkan(self, *, dist_x: float = None, dist_y: float = None, **kwargs: Any) -> "VideoStream":
        """

        14.4 chromaber_vulkan
        Apply an effect that emulates chromatic aberration. Works best with RGB inputs,
        but provides a similar effect with YCbCr inputs too.

        Parameters:
        ----------

        :param float dist_x: Horizontal displacement multiplier. Each chroma pixel’s position will be multiplied by this amount, starting from the center of the image. Default is 0.
        :param float dist_y: Similarly, this sets the vertical displacement multiplier. Default is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromaber_005fvulkan

        """
        filter_node = FilterNode(
            name="chromaber_vulkan",
            streams=[
                self,
            ],
            kwargs={
                "dist_x": dist_x,
                "dist_y": dist_y,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def chromahold(
        self, *, color: str = None, similarity: float = None, blend: float = None, yuv: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.24 chromahold
        Remove all color information for all colors except for certain one.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str color: The color which will not be replaced with neutral chroma.
        :param float similarity: Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more preserved color.
        :param bool yuv: Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromahold

        """
        filter_node = FilterNode(
            name="chromahold",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def chromakey(
        self, *, color: str = None, similarity: float = None, blend: float = None, yuv: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.25 chromakey
        YUV colorspace color/chroma keying.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str color: The color which will be replaced with transparency.
        :param float similarity: Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.
        :param bool yuv: Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey

        """
        filter_node = FilterNode(
            name="chromakey",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def chromakey_cuda(
        self, *, color: str = None, similarity: float = None, blend: float = None, yuv: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.26 chromakey_cuda
        CUDA accelerated YUV colorspace color/chroma keying.

        This filter works like normal chromakey filter but operates on CUDA frames.
        for more details and parameters see chromakey.

        Parameters:
        ----------

        :param str color: None
        :param float similarity: None
        :param float blend: None
        :param bool yuv: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey_005fcuda

        """
        filter_node = FilterNode(
            name="chromakey_cuda",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def chromanr(
        self,
        *,
        thres: float = None,
        sizew: int = None,
        sizeh: int = None,
        stepw: int = None,
        steph: int = None,
        threy: float = None,
        threu: float = None,
        threv: float = None,
        distance: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.27 chromanr
        Reduce chrominance noise.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromanr

        """
        filter_node = FilterNode(
            name="chromanr",
            streams=[
                self,
            ],
            kwargs={
                "thres": thres,
                "sizew": sizew,
                "sizeh": sizeh,
                "stepw": stepw,
                "steph": steph,
                "threy": threy,
                "threu": threu,
                "threv": threv,
                "distance": distance,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def chromashift(
        self, *, cbh: int = None, cbv: int = None, crh: int = None, crv: int = None, edge: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.28 chromashift
        Shift chroma pixels horizontally and/or vertically.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int cbh: Set amount to shift chroma-blue horizontally.
        :param int cbv: Set amount to shift chroma-blue vertically.
        :param int crh: Set amount to shift chroma-red horizontally.
        :param int crv: Set amount to shift chroma-red vertically.
        :param int edge: Set edge mode, can be smear, default, or warp.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromashift

        """
        filter_node = FilterNode(
            name="chromashift",
            streams=[
                self,
            ],
            kwargs={
                "cbh": cbh,
                "cbv": cbv,
                "crh": crh,
                "crv": crv,
                "edge": edge,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def ciescope(
        self,
        *,
        system: int = None,
        cie: int = None,
        gamuts: str = None,
        size: int = None,
        intensity: float = None,
        contrast: float = None,
        corrgamma: bool = None,
        showwhite: bool = None,
        gamma: float = None,
        fill: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.29 ciescope
        Display CIE color diagram with pixels overlaid onto it.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def codecview(
        self,
        *,
        mv: str = None,
        qp: bool = None,
        mv_type: str = None,
        frame_type: str = None,
        block: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.30 codecview
        Visualize information exported by some codecs.

        Some codecs can export information through frames using side-data or other
        means. For example, some MPEG based codecs export motion vectors through the
        export_mvs flag in the codec flags2 option.

        The filter accepts the following option:

        Parameters:
        ----------

        :param str mv: Set motion vectors to visualize. Available flags for mv are: ‘pf’ forward predicted MVs of P-frames ‘bf’ forward predicted MVs of B-frames ‘bb’ backward predicted MVs of B-frames
        :param bool qp: Display quantization parameters using the chroma planes.
        :param str mv_type: Set motion vectors type to visualize. Includes MVs from all frames unless specified by frame_type option. Available flags for mv_type are: ‘fp’ forward predicted MVs ‘bp’ backward predicted MVs
        :param str frame_type: Set frame type to visualize motion vectors of. Available flags for frame_type are: ‘if’ intra-coded frames (I-frames) ‘pf’ predicted frames (P-frames) ‘bf’ bi-directionally predicted frames (B-frames)
        :param bool block: Display block partition structure using the luma plane.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#codecview

        """
        filter_node = FilterNode(
            name="codecview",
            streams=[
                self,
            ],
            kwargs={
                "mv": mv,
                "qp": qp,
                "mv_type": mv_type,
                "frame_type": frame_type,
                "block": block,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorbalance(
        self,
        *,
        rs: float = None,
        gs: float = None,
        bs: float = None,
        rm: float = None,
        gm: float = None,
        bm: float = None,
        rh: float = None,
        gh: float = None,
        bh: float = None,
        pl: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.31 colorbalance
        Modify intensity of primary colors (red, green and blue) of input frames.

        The filter allows an input frame to be adjusted in the shadows, midtones or highlights
        regions for the red-cyan, green-magenta or blue-yellow balance.

        A positive adjustment value shifts the balance towards the primary color, a negative
        value towards the complementary color.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorbalance

        """
        filter_node = FilterNode(
            name="colorbalance",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorchannelmixer(
        self,
        *,
        rr: float = None,
        rg: float = None,
        rb: float = None,
        ra: float = None,
        gr: float = None,
        gg: float = None,
        gb: float = None,
        ga: float = None,
        br: float = None,
        bg: float = None,
        bb: float = None,
        ba: float = None,
        ar: float = None,
        ag: float = None,
        ab: float = None,
        aa: float = None,
        pc: int = None,
        pa: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.34 colorchannelmixer
        Adjust video input frames by re-mixing color channels.

        This filter modifies a color channel by adding the values associated to
        the other channels of the same pixels. For example if the value to
        modify is red, the output value will be:

        red=red*rr + blue*rb + green*rg + alpha*ra

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer

        """
        filter_node = FilterNode(
            name="colorchannelmixer",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorcontrast(
        self,
        *,
        rc: float = None,
        gm: float = None,
        by: float = None,
        rcw: float = None,
        gmw: float = None,
        byw: float = None,
        pl: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.32 colorcontrast
        Adjust color contrast between RGB components.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float rc: Set the red-cyan contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float gm: Set the green-magenta contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float by: Set the blue-yellow contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        :param float rcw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float gmw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float byw: Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        :param float pl: Set the amount of preserving lightness. Default value is 0.0. Allowed range is from 0.0 to 1.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcontrast

        """
        filter_node = FilterNode(
            name="colorcontrast",
            streams=[
                self,
            ],
            kwargs={
                "rc": rc,
                "gm": gm,
                "by": by,
                "rcw": rcw,
                "gmw": gmw,
                "byw": byw,
                "pl": pl,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorcorrect(
        self,
        *,
        rl: float = None,
        bl: float = None,
        rh: float = None,
        bh: float = None,
        saturation: float = None,
        analyze: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.33 colorcorrect
        Adjust color white balance selectively for blacks and whites.
        This filter operates in YUV colorspace.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float rl: Set the red shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float bl: Set the blue shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float rh: Set the red highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float bh: Set the blue highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        :param float saturation: Set the amount of saturation. Allowed range is from -3.0 to 3.0. Default value is 1.
        :param int analyze: If set to anything other than manual it will analyze every frame and use derived parameters for filtering output frame. Possible values are: ‘manual’ ‘average’ ‘minmax’ ‘median’ Default value is manual.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcorrect

        """
        filter_node = FilterNode(
            name="colorcorrect",
            streams=[
                self,
            ],
            kwargs={
                "rl": rl,
                "bl": bl,
                "rh": rh,
                "bh": bh,
                "saturation": saturation,
                "analyze": analyze,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorhold(
        self, *, color: str = None, similarity: float = None, blend: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.37 colorhold
        Remove all color information for all RGB colors except for certain one.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str color: The color which will not be replaced with neutral gray.
        :param float similarity: Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels fully gray. Higher values result in more preserved color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorhold

        """
        filter_node = FilterNode(
            name="colorhold",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorize(
        self, *, hue: float = None, saturation: float = None, lightness: float = None, mix: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.35 colorize
        Overlay a solid color on the video stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float hue: Set the color hue. Allowed range is from 0 to 360. Default value is 0.
        :param float saturation: Set the color saturation. Allowed range is from 0 to 1. Default value is 0.5.
        :param float lightness: Set the color lightness. Allowed range is from 0 to 1. Default value is 0.5.
        :param float mix: Set the mix of source lightness. By default is set to 1.0. Allowed range is from 0.0 to 1.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorize

        """
        filter_node = FilterNode(
            name="colorize",
            streams=[
                self,
            ],
            kwargs={
                "hue": hue,
                "saturation": saturation,
                "lightness": lightness,
                "mix": mix,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorkey(
        self, *, color: str = None, similarity: float = None, blend: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.36 colorkey
        RGB colorspace color keying.
        This filter operates on 8-bit RGB format frames by setting the alpha component of each pixel
        which falls within the similarity radius of the key color to 0. The alpha value for pixels outside
        the similarity radius depends on the value of the blend option.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str color: Set the color for which alpha will be set to 0 (full transparency). See (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default is black.
        :param float similarity: Set the radius from the key color within which other colors also have full transparency. The computed distance is related to the unit fractional distance in 3D space between the RGB values of the key color and the pixel’s color. Range is 0.01 to 1.0. 0.01 matches within a very small radius around the exact key color, while 1.0 matches everything. Default is 0.01.
        :param float blend: Set how the alpha value for pixels that fall outside the similarity radius is computed. 0.0 makes pixels either fully transparent or fully opaque. Higher values result in semi-transparent pixels, with greater transparency the more similar the pixel color is to the key color. Range is 0.0 to 1.0. Default is 0.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorkey

        """
        filter_node = FilterNode(
            name="colorkey",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorkey_opencl(
        self, *, color: str = None, similarity: float = None, blend: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        12.3 colorkey_opencl
        RGB colorspace color keying.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str color: The color which will be replaced with transparency.
        :param float similarity: Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorkey_005fopencl

        """
        filter_node = FilterNode(
            name="colorkey_opencl",
            streams=[
                self,
            ],
            kwargs={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorlevels(
        self,
        *,
        rimin: float = None,
        gimin: float = None,
        bimin: float = None,
        aimin: float = None,
        rimax: float = None,
        gimax: float = None,
        bimax: float = None,
        aimax: float = None,
        romin: float = None,
        gomin: float = None,
        bomin: float = None,
        aomin: float = None,
        romax: float = None,
        gomax: float = None,
        bomax: float = None,
        aomax: float = None,
        preserve: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.38 colorlevels
        Adjust video input frames using levels.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorlevels

        """
        filter_node = FilterNode(
            name="colorlevels",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colormap(
        self,
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
                self,
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
        return filter_node._vs(0)

    def colormatrix(self, *, src: int = None, dst: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.40 colormatrix
        Convert color matrix.

        The filter accepts the following options:


        For example to convert from BT.601 to SMPTE-240M, use the command:

        colormatrix=bt601:smpte240m

        Parameters:
        ----------

        :param int src: Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020
        :param int dst: Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colormatrix

        """
        filter_node = FilterNode(
            name="colormatrix",
            streams=[
                self,
            ],
            kwargs={
                "src": src,
                "dst": dst,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorspace(
        self,
        *,
        all: int = None,
        space: int = None,
        range: int = None,
        primaries: int = None,
        trc: int = None,
        format: int = None,
        fast: bool = None,
        dither: int = None,
        wpadapt: int = None,
        iall: int = None,
        ispace: int = None,
        irange: int = None,
        iprimaries: int = None,
        itrc: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.41 colorspace
        Convert colorspace, transfer characteristics or color primaries.
        Input video needs to have an even size.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int all: None
        :param int space: None
        :param int range: None
        :param int primaries: None
        :param int trc: None
        :param int format: None
        :param bool fast: None
        :param int dither: None
        :param int wpadapt: None
        :param int iall: None
        :param int ispace: None
        :param int irange: None
        :param int iprimaries: None
        :param int itrc: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace

        """
        filter_node = FilterNode(
            name="colorspace",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colorspace_cuda(self, *, range: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.42 colorspace_cuda
        CUDA accelerated implementation of the colorspace filter.

        It is by no means feature complete compared to the software colorspace filter,
        and at the current time only supports color range conversion between jpeg/full
        and mpeg/limited range.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int range: Specify output color range. The accepted values are: ‘tv’ TV (restricted) range ‘mpeg’ MPEG (restricted) range ‘pc’ PC (full) range ‘jpeg’ JPEG (full) range

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace_005fcuda

        """
        filter_node = FilterNode(
            name="colorspace_cuda",
            streams=[
                self,
            ],
            kwargs={
                "range": range,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def colortemperature(
        self, *, temperature: float = None, mix: float = None, pl: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.43 colortemperature
        Adjust color temperature in video to simulate variations in ambient color temperature.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float temperature: Set the temperature in Kelvin. Allowed range is from 1000 to 40000. Default value is 6500 K.
        :param float mix: Set mixing with filtered output. Allowed range is from 0 to 1. Default value is 1.
        :param float pl: Set the amount of preserving lightness. Allowed range is from 0 to 1. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colortemperature

        """
        filter_node = FilterNode(
            name="colortemperature",
            streams=[
                self,
            ],
            kwargs={
                "temperature": temperature,
                "mix": mix,
                "pl": pl,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def convolution(
        self,
        *,
        _0m: str = None,
        _1m: str = None,
        _2m: str = None,
        _3m: str = None,
        _0rdiv: float = None,
        _1rdiv: float = None,
        _2rdiv: float = None,
        _3rdiv: float = None,
        _0bias: float = None,
        _1bias: float = None,
        _2bias: float = None,
        _3bias: float = None,
        _0mode: int = None,
        _1mode: int = None,
        _2mode: int = None,
        _3mode: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.44 convolution
        Apply convolution of 3x3, 5x5, 7x7 or horizontal/vertical up to 49 elements.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#convolution

        """
        filter_node = FilterNode(
            name="convolution",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def convolve(
        self, _impulse: "VideoStream", *, planes: int = None, impulse: int = None, noise: float = None, **kwargs: Any
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
                self,
                _impulse,
            ],
            kwargs={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def copy(self, **kwargs: Any) -> "VideoStream":
        """

        11.46 copy
        Copy the input video source unchanged to the output. This is mainly useful for
        testing purposes.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#copy

        """
        filter_node = FilterNode(
            name="copy",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def corr(self, _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
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
                self,
                _reference,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def cover_rect(self, *, cover: str, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.49 cover_rect
        Cover a rectangular object

        It accepts the following options:

        Parameters:
        ----------

        :param str cover: Filepath of the optional cover image, needs to be in yuv420.
        :param int mode: Set covering mode. It accepts the following values: ‘cover’ cover it by the supplied image ‘blur’ cover it by interpolating the surrounding pixels Default value is blur.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cover_005frect

        """
        filter_node = FilterNode(
            name="cover_rect",
            streams=[
                self,
            ],
            kwargs={
                "cover": cover,
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def crop(
        self,
        *,
        out_w: str = None,
        out_h: str = None,
        x: str = None,
        y: str = None,
        keep_aspect: bool = None,
        exact: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.50 crop
        Crop the input video to given dimensions.

        It accepts the following parameters:


        The out_w, out_h, x, y parameters are
        expressions containing the following constants:


        The expression for out_w may depend on the value of out_h,
        and the expression for out_h may depend on out_w, but they
        cannot depend on x and y, as x and y are
        evaluated after out_w and out_h.

        The x and y parameters specify the expressions for the
        position of the top-left corner of the output (non-cropped) area. They
        are evaluated for each frame. If the evaluated value is not valid, it
        is approximated to the nearest valid value.

        The expression for x may depend on y, and the expression
        for y may depend on x.

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
            streams=[
                self,
            ],
            kwargs={
                "out_w": out_w,
                "out_h": out_h,
                "x": x,
                "y": y,
                "keep_aspect": keep_aspect,
                "exact": exact,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def cropdetect(
        self,
        *,
        limit: float = None,
        round: int = None,
        reset: int = None,
        skip: int = None,
        max_outliers: int = None,
        mode: int = None,
        high: float = None,
        low: float = None,
        mv_threshold: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.51 cropdetect
        Auto-detect the crop size.

        It calculates the necessary cropping parameters and prints the
        recommended parameters via the logging system. The detected dimensions
        correspond to the non-black or video area of the input video according to mode.

        It accepts the following parameters:

        Parameters:
        ----------

        :param float limit: Set higher black value threshold, which can be optionally specified from nothing (0) to everything (255 for 8-bit based formats). An intensity value greater to the set value is considered non-black. It defaults to 24. You can also specify a value between 0.0 and 1.0 which will be scaled depending on the bitdepth of the pixel format.
        :param int round: The value which the width/height should be divisible by. It defaults to 16. The offset is automatically adjusted to center the video. Use 2 to get only even dimensions (needed for 4:2:2 video). 16 is best when encoding to most video codecs.
        :param int reset: Set the counter that determines after how many frames cropdetect will reset the previously detected largest video area and start over to detect the current optimal crop area. Default value is 0. This can be useful when channel logos distort the video area. 0 indicates ’never reset’, and returns the largest area encountered during playback.
        :param int skip: Set the number of initial frames for which evaluation is skipped. Default is 2. Range is 0 to INT_MAX.
        :param int max_outliers: None
        :param int mode: Depending on mode crop detection is based on either the mere black value of surrounding pixels or a combination of motion vectors and edge pixels. ‘black’ Detect black pixels surrounding the playing video. For fine control use option limit. ‘mvedges’ Detect the playing video by the motion vectors inside the video and scanning for edge pixels typically forming the border of a playing video.
        :param float high: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 5/255, and default value for high is 15/255.
        :param float low: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 5/255, and default value for high is 15/255.
        :param int mv_threshold: Set motion in pixel units as threshold for motion detection. It defaults to 8.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cropdetect

        """
        filter_node = FilterNode(
            name="cropdetect",
            streams=[
                self,
            ],
            kwargs={
                "limit": limit,
                "round": round,
                "reset": reset,
                "skip": skip,
                "max_outliers": max_outliers,
                "mode": mode,
                "high": high,
                "low": low,
                "mv_threshold": mv_threshold,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def cue(self, *, cue: int = None, preroll: int = None, buffer: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.52 cue
        Delay video filtering until a given wallclock timestamp. The filter first
        passes on preroll amount of frames, then it buffers at most
        buffer amount of frames and waits for the cue. After reaching the cue
        it forwards the buffered frames and also any subsequent frames coming in its
        input.

        The filter can be used synchronize the output of multiple ffmpeg processes for
        realtime output devices like decklink. By putting the delay in the filtering
        chain and pre-buffering frames the process can pass on data to output almost
        immediately after the target wallclock timestamp is reached.

        Perfect frame accuracy cannot be guaranteed, but the result is good enough for
        some use cases.

        Parameters:
        ----------

        :param int cue: The cue timestamp expressed in a UNIX timestamp in microseconds. Default is 0.
        :param int preroll: The duration of content to pass on as preroll expressed in seconds. Default is 0.
        :param int buffer: The maximum duration of content to buffer before waiting for the cue expressed in seconds. Default is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cue

        """
        filter_node = FilterNode(
            name="cue",
            streams=[
                self,
            ],
            kwargs={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def curves(
        self,
        *,
        preset: int = None,
        master: str,
        red: str,
        green: str,
        blue: str,
        all: str,
        psfile: str,
        plot: str,
        interp: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.53 curves
        Apply color adjustments using curves.

        This filter is similar to the Adobe Photoshop and GIMP curves tools. Each
        component (red, green and blue) has its values defined by N key points
        tied from each other using a smooth curve. The x-axis represents the pixel
        values from the input frame, and the y-axis the new pixel values to be set for
        the output frame.

        By default, a component curve is defined by the two points (0;0) and
        (1;1). This creates a straight line where each original pixel value is
        "adjusted" to its own value, which means no change to the image.

        The filter allows you to redefine these two points and add some more. A new
        curve will be define to pass smoothly through all these new coordinates. The
        new defined points needs to be strictly increasing over the x-axis, and their
        x and y values must be in the [0;1] interval. The curve is
        formed by using a natural or monotonic cubic spline interpolation, depending
        on the interp option (default: natural). The natural
        spline produces a smoother curve in general while the monotonic (pchip)
        spline guarantees the transitions between the specified points to be
        monotonic. If the computed curves happened to go outside the vector spaces,
        the values will be clipped accordingly.

        The filter accepts the following options:


        To avoid some filtergraph syntax conflicts, each key points list need to be
        defined using the following syntax: x0/y0 x1/y1 x2/y2 ....

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#curves

        """
        filter_node = FilterNode(
            name="curves",
            streams=[
                self,
            ],
            kwargs={
                "preset": preset,
                "master": master,
                "red": red,
                "green": green,
                "blue": blue,
                "all": all,
                "psfile": psfile,
                "plot": plot,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def datascope(
        self,
        *,
        size: str = None,
        x: int = None,
        y: int = None,
        mode: int = None,
        axis: bool = None,
        opacity: float = None,
        format: int = None,
        components: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.54 datascope
        Video data analysis filter.

        This filter shows hexadecimal pixel values of part of video.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "size": size,
                "x": x,
                "y": y,
                "mode": mode,
                "axis": axis,
                "opacity": opacity,
                "format": format,
                "components": components,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dblur(self, *, angle: float = None, radius: float = None, planes: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.55 dblur
        Apply Directional blur filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float angle: Set angle of directional blur. Default is 45.
        :param float radius: Set radius of directional blur. Default is 5.
        :param int planes: Set which planes to filter. By default all planes are filtered.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dblur

        """
        filter_node = FilterNode(
            name="dblur",
            streams=[
                self,
            ],
            kwargs={
                "angle": angle,
                "radius": radius,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dctdnoiz(
        self, *, sigma: float = None, overlap: int = None, expr: str, n: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.56 dctdnoiz
        Denoise frames using 2D DCT (frequency domain filtering).

        This filter is not designed for real time.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float sigma: Set the noise sigma constant. This sigma defines a hard threshold of 3 * sigma; every DCT coefficient (absolute value) below this threshold with be dropped. If you need a more advanced filtering, see expr. Default is 0.
        :param int overlap: Set number overlapping pixels for each block. Since the filter can be slow, you may want to reduce this value, at the cost of a less effective filter and the risk of various artefacts. If the overlapping value doesn’t permit processing the whole input width or height, a warning will be displayed and according borders won’t be denoised. Default value is blocksize-1, which is the best possible setting.
        :param str expr: Set the coefficient factor expression. For each coefficient of a DCT block, this expression will be evaluated as a multiplier value for the coefficient. If this is option is set, the sigma option will be ignored. The absolute value of the coefficient can be accessed through the c variable.
        :param int n: Set the blocksize using the number of bits. 1<<n defines the blocksize, which is the width and height of the processed blocks. The default value is 3 (8x8) and can be raised to 4 for a blocksize of 16x16. Note that changing this setting has huge consequences on the speed processing. Also, a larger block size does not necessarily means a better de-noising.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dctdnoiz

        """
        filter_node = FilterNode(
            name="dctdnoiz",
            streams=[
                self,
            ],
            kwargs={
                "sigma": sigma,
                "overlap": overlap,
                "expr": expr,
                "n": n,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def deband(
        self,
        *,
        _1thr: float = None,
        _2thr: float = None,
        _3thr: float = None,
        _4thr: float = None,
        range: int = None,
        direction: float = None,
        blur: bool = None,
        coupling: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.57 deband
        Remove banding artifacts from input video.
        It works by replacing banded pixels with average value of referenced pixels.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deband

        """
        filter_node = FilterNode(
            name="deband",
            streams=[
                self,
            ],
            kwargs={
                "1thr": _1thr,
                "2thr": _2thr,
                "3thr": _3thr,
                "4thr": _4thr,
                "range": range,
                "direction": direction,
                "blur": blur,
                "coupling": coupling,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def deblock(
        self,
        *,
        filter: int = None,
        block: int = None,
        alpha: float = None,
        beta: float = None,
        gamma: float = None,
        delta: float = None,
        planes: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.58 deblock
        Remove blocking artifacts from input video.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int filter: Set filter type, can be weak or strong. Default is strong. This controls what kind of deblocking is applied.
        :param int block: Set size of block, allowed range is from 4 to 512. Default is 8.
        :param float alpha: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float beta: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float gamma: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param float delta: Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        :param int planes: Set planes to filter. Default is to filter all available planes.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deblock

        """
        filter_node = FilterNode(
            name="deblock",
            streams=[
                self,
            ],
            kwargs={
                "filter": filter,
                "block": block,
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
                "delta": delta,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def decimate(
        self,
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
                self,
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
        return filter_node._vs(0)

    def deconvolve(
        self, _impulse: "VideoStream", *, planes: int = None, impulse: int = None, noise: float = None, **kwargs: Any
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
                self,
                _impulse,
            ],
            kwargs={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dedot(
        self, *, m: str = None, lt: float = None, tl: float = None, tc: float = None, ct: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.61 dedot
        Reduce cross-luminance (dot-crawl) and cross-color (rainbows) from video.

        It accepts the following options:

        Parameters:
        ----------

        :param str m: Set mode of operation. Can be combination of dotcrawl for cross-luminance reduction and/or rainbows for cross-color reduction.
        :param float lt: Set spatial luma threshold. Lower values increases reduction of cross-luminance.
        :param float tl: Set tolerance for temporal luma. Higher values increases reduction of cross-luminance.
        :param float tc: Set tolerance for chroma temporal variation. Higher values increases reduction of cross-color.
        :param float ct: Set temporal chroma threshold. Lower values increases reduction of cross-color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dedot

        """
        filter_node = FilterNode(
            name="dedot",
            streams=[
                self,
            ],
            kwargs={
                "m": m,
                "lt": lt,
                "tl": tl,
                "tc": tc,
                "ct": ct,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def deflate(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.62 deflate
        Apply deflate effect to the video.

        This filter replaces the pixel by the local(3x3) average by taking into account
        only values lower than the pixel.

        It accepts the following options:

        Parameters:
        ----------

        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflate

        """
        filter_node = FilterNode(
            name="deflate",
            streams=[
                self,
            ],
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def deflicker(self, *, size: int = None, mode: int = None, bypass: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.63 deflicker
        Remove temporal frame luminance variations.

        It accepts the following options:

        Parameters:
        ----------

        :param int size: Set moving-average filter size in frames. Default is 5. Allowed range is 2 - 129.
        :param int mode: Set averaging mode to smooth temporal luminance variations. Available values are: ‘am’ Arithmetic mean ‘gm’ Geometric mean ‘hm’ Harmonic mean ‘qm’ Quadratic mean ‘cm’ Cubic mean ‘pm’ Power mean ‘median’ Median
        :param bool bypass: Do not actually modify frame. Useful when one only wants metadata.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflicker

        """
        filter_node = FilterNode(
            name="deflicker",
            streams=[
                self,
            ],
            kwargs={
                "size": size,
                "mode": mode,
                "bypass": bypass,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dejudder(self, *, cycle: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.64 dejudder
        Remove judder produced by partially interlaced telecined content.

        Judder can be introduced, for instance, by pullup filter. If the original
        source was partially telecined content then the output of pullup,dejudder
        will have a variable frame rate. May change the recorded frame rate of the
        container. Aside from that change, this filter will not affect constant frame
        rate video.

        The option available in this filter is:

        Parameters:
        ----------

        :param int cycle: Specify the length of the window over which the judder repeats. Accepts any integer greater than 1. Useful values are: ‘4’ If the original was telecined from 24 to 30 fps (Film to NTSC). ‘5’ If the original was telecined from 25 to 30 fps (PAL to NTSC). ‘20’ If a mixture of the two. The default is ‘4’.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dejudder

        """
        filter_node = FilterNode(
            name="dejudder",
            streams=[
                self,
            ],
            kwargs={
                "cycle": cycle,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def delogo(
        self, *, x: str = None, y: str = None, w: str = None, h: str = None, show: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.65 delogo
        Suppress a TV station logo by a simple interpolation of the surrounding
        pixels. Just set a rectangle covering the logo and watch it disappear
        (and sometimes something even uglier appear - your mileage may vary).

        It accepts the following parameters:

        Parameters:
        ----------

        :param str x: Specify the top left corner coordinates of the logo. They must be specified.
        :param str y: Specify the top left corner coordinates of the logo. They must be specified.
        :param str w: Specify the width and height of the logo to clear. They must be specified.
        :param str h: Specify the width and height of the logo to clear. They must be specified.
        :param bool show: When set to 1, a green rectangle is drawn on the screen to simplify finding the right x, y, w, and h parameters. The default value is 0. The rectangle is drawn on the outermost pixels which will be (partly) replaced with interpolated values. The values of the next pixels immediately outside this rectangle in each direction will be used to compute the interpolated pixel values inside the rectangle.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#delogo

        """
        filter_node = FilterNode(
            name="delogo",
            streams=[
                self,
            ],
            kwargs={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "show": show,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def derain(
        self,
        *,
        filter_type: int = None,
        dnn_backend: int = None,
        model: str,
        input: str = None,
        output: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.66 derain
        Remove the rain in the input image/video by applying the derain methods based on
        convolutional neural networks. Supported models:


         Recurrent Squeeze-and-Excitation Context Aggregation Net (RESCAN).
        See http://openaccess.thecvf.com/content_ECCV_2018/papers/Xia_Li_Recurrent_Squeeze-and-Excitation_Context_ECCV_2018_paper.pdf.

        Training as well as model generation scripts are provided in
        the repository at https://github.com/XueweiMeng/derain_filter.git.

        The filter accepts the following options:


        To get full functionality (such as async execution), please use the dnn_processing filter.

        Parameters:
        ----------

        :param int filter_type: Specify which filter to use. This option accepts the following values: ‘derain’ Derain filter. To conduct derain filter, you need to use a derain model. ‘dehaze’ Dehaze filter. To conduct dehaze filter, you need to use a dehaze model. Default value is ‘derain’.
        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow can load files for only its format.
        :param str input: None
        :param str output: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#derain

        """
        filter_node = FilterNode(
            name="derain",
            streams=[
                self,
            ],
            kwargs={
                "filter_type": filter_type,
                "dnn_backend": dnn_backend,
                "model": model,
                "input": input,
                "output": output,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def deshake(
        self,
        *,
        x: int = None,
        y: int = None,
        w: int = None,
        h: int = None,
        rx: int = None,
        ry: int = None,
        edge: int = None,
        blocksize: int = None,
        contrast: int = None,
        search: int = None,
        filename: str,
        opencl: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.67 deshake
        Attempt to fix small changes in horizontal and/or vertical shift. This
        filter helps remove camera shake from hand-holding a camera, bumping a
        tripod, moving on a vehicle, etc.

        The filter accepts the following options:

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
        :param bool opencl: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deshake

        """
        filter_node = FilterNode(
            name="deshake",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def deshake_opencl(
        self,
        *,
        tripod: bool = None,
        debug: bool = None,
        adaptive_crop: bool = None,
        refine_features: bool = None,
        smooth_strength: float = None,
        smooth_window_multiplier: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        12.6 deshake_opencl
        Feature-point based video stabilization filter.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "tripod": tripod,
                "debug": debug,
                "adaptive_crop": adaptive_crop,
                "refine_features": refine_features,
                "smooth_strength": smooth_strength,
                "smooth_window_multiplier": smooth_window_multiplier,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def despill(
        self,
        *,
        type: int = None,
        mix: float = None,
        expand: float = None,
        red: float = None,
        green: float = None,
        blue: float = None,
        brightness: float = None,
        alpha: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.68 despill
        Remove unwanted contamination of foreground colors, caused by reflected color of
        greenscreen or bluescreen.

        This filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#despill

        """
        filter_node = FilterNode(
            name="despill",
            streams=[
                self,
            ],
            kwargs={
                "type": type,
                "mix": mix,
                "expand": expand,
                "red": red,
                "green": green,
                "blue": blue,
                "brightness": brightness,
                "alpha": alpha,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def detelecine(
        self, *, first_field: int = None, pattern: str = None, start_frame: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.69 detelecine
        Apply an exact inverse of the telecine operation. It requires a predefined
        pattern specified using the pattern option which must be the same as that passed
        to the telecine filter.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int first_field: ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        :param str pattern: A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.
        :param int start_frame: A number representing position of the first frame with respect to the telecine pattern. This is to be used if the stream is cut. The default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#detelecine

        """
        filter_node = FilterNode(
            name="detelecine",
            streams=[
                self,
            ],
            kwargs={
                "first_field": first_field,
                "pattern": pattern,
                "start_frame": start_frame,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dilation(
        self,
        *,
        coordinates: int = None,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.70 dilation
        Apply dilation effect to the video.

        This filter replaces the pixel by the local(3x3) maximum.

        It accepts the following options:

        Parameters:
        ----------

        :param int coordinates: Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8
        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dilation

        """
        filter_node = FilterNode(
            name="dilation",
            streams=[
                self,
            ],
            kwargs={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def displace(self, _xmap: "VideoStream", _ymap: "VideoStream", *, edge: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _xmap,
                _ymap,
            ],
            kwargs={
                "edge": edge,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def dnn_classify(
        self,
        *,
        dnn_backend: int = None,
        model: str,
        input: str,
        output: str,
        backend_configs: str,
        _async: bool = None,
        confidence: float = None,
        labels: str,
        target: str,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.72 dnn_classify
        Do classification with deep neural networks based on bounding boxes.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs for your system.
        :param bool _async: None
        :param float confidence: Set the confidence threshold (default: 0.5).
        :param str labels: Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0, and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        :param str target: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fclassify

        """
        filter_node = FilterNode(
            name="dnn_classify",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def dnn_detect(
        self,
        *,
        dnn_backend: int = None,
        model: str,
        input: str,
        output: str,
        backend_configs: str,
        _async: bool = None,
        confidence: float = None,
        labels: str,
        model_type: int = None,
        cell_w: int = None,
        cell_h: int = None,
        nb_classes: int = None,
        anchors: str,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.73 dnn_detect
        Do object detection with deep neural networks.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async.
        :param bool _async: None
        :param float confidence: Set the confidence threshold (default: 0.5).
        :param str labels: Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0 (usually it is ’background’), and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        :param int model_type: None
        :param int cell_w: None
        :param int cell_h: None
        :param int nb_classes: None
        :param str anchors: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fdetect

        """
        filter_node = FilterNode(
            name="dnn_detect",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def dnn_processing(
        self,
        *,
        dnn_backend: int = None,
        model: str,
        input: str,
        output: str,
        backend_configs: str,
        _async: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.74 dnn_processing
        Do image processing with deep neural networks. It works together with another filter
        which converts the pixel format of the Frame to what the dnn network requires.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow ‘openvino’ OpenVINO backend. To enable this backend you need to build and install the OpenVINO for C library (see https://github.com/openvinotoolkit/openvino/blob/master/build-instruction.md) and configure FFmpeg with --enable-libopenvino (–extra-cflags=-I... –extra-ldflags=-L... might be needed if the header files and libraries are not installed into system path)
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        :param str input: Set the input name of the dnn network.
        :param str output: Set the output name of the dnn network.
        :param str backend_configs: Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async. For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs of TensorFlow backend for your system.
        :param bool _async: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fprocessing

        """
        filter_node = FilterNode(
            name="dnn_processing",
            streams=[
                self,
            ],
            kwargs={
                "dnn_backend": dnn_backend,
                "model": model,
                "input": input,
                "output": output,
                "backend_configs": backend_configs,
                "async": _async,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def doubleweave(self, *, first_field: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.285 weave, doubleweave
        The weave takes a field-based video input and join
        each two sequential fields into single frame, producing a new double
        height clip with half the frame rate and half the frame count.

        The doubleweave works same as weave but without
        halving frame rate and frame count.

        It accepts the following option:

        Parameters:
        ----------

        :param int first_field: Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        filter_node = FilterNode(
            name="doubleweave",
            streams=[
                self,
            ],
            kwargs={
                "first_field": first_field,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def drawbox(
        self,
        *,
        x: str = None,
        y: str = None,
        width: str = None,
        height: str = None,
        color: str = None,
        thickness: str = None,
        replace: bool = None,
        box_source: str,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.75 drawbox
        Draw a colored box on the input image.

        It accepts the following parameters:


        The parameters for x, y, w and h and t are expressions containing the
        following constants:

        Parameters:
        ----------

        :param str x: The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        :param str y: The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        :param str width: The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        :param str height: The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        :param str color: Specify the color of the box to write. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the box edge color is the same as the video with inverted luma.
        :param str thickness: The expression which sets the thickness of the box edge. A value of fill will create a filled box. Default value is 3. See below for the list of accepted constants.
        :param bool replace: Applicable if the input has alpha. With value 1, the pixels of the painted box will overwrite the video’s color and alpha pixels. Default is 0, which composites the box onto the input, leaving the video’s alpha intact.
        :param str box_source: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawbox

        """
        filter_node = FilterNode(
            name="drawbox",
            streams=[
                self,
            ],
            kwargs={
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
                "thickness": thickness,
                "replace": replace,
                "box_source": box_source,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def drawgraph(
        self,
        *,
        m1: str = None,
        fg1: str = None,
        m2: str = None,
        fg2: str = None,
        m3: str = None,
        fg3: str = None,
        m4: str = None,
        fg4: str = None,
        bg: str = None,
        min: float = None,
        max: float = None,
        mode: int = None,
        slide: int = None,
        size: str = None,
        rate: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.76 drawgraph
        Draw a graph using input video metadata.

        It accepts the following parameters:


        Example using metadata from signalstats filter:

        signalstats,drawgraph=lavfi.signalstats.YAVG:min=0:max=255

        Example using metadata from ebur128 filter:

        ebur128=metadata=1,adrawgraph=lavfi.r128.M:min=-120:max=5

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
            streams=[
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
        return filter_node._vs(0)

    def drawgrid(
        self,
        *,
        x: str = None,
        y: str = None,
        width: str = None,
        height: str = None,
        color: str = None,
        thickness: str = None,
        replace: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.77 drawgrid
        Draw a grid on the input image.

        It accepts the following parameters:


        The parameters for x, y, w and h and t are expressions containing the
        following constants:

        Parameters:
        ----------

        :param str x: The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        :param str y: The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        :param str width: The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        :param str height: The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        :param str color: Specify the color of the grid. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the grid color is the same as the video with inverted luma.
        :param str thickness: The expression which sets the thickness of the grid line. Default value is 1. See below for the list of accepted constants.
        :param bool replace: Applicable if the input has alpha. With 1 the pixels of the painted grid will overwrite the video’s color and alpha pixels. Default is 0, which composites the grid onto the input, leaving the video’s alpha intact.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawgrid

        """
        filter_node = FilterNode(
            name="drawgrid",
            streams=[
                self,
            ],
            kwargs={
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
                "thickness": thickness,
                "replace": replace,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def drawtext(
        self,
        *,
        fontfile: str,
        text: str,
        textfile: str,
        fontcolor: str = None,
        fontcolor_expr: str = None,
        boxcolor: str = None,
        bordercolor: str = None,
        shadowcolor: str = None,
        box: bool = None,
        boxborderw: str = None,
        line_spacing: int = None,
        fontsize: str,
        text_align: str = None,
        x: str = None,
        y: str = None,
        boxw: int = None,
        boxh: int = None,
        shadowx: int = None,
        shadowy: int = None,
        borderw: int = None,
        tabsize: int = None,
        basetime: int = None,
        expansion: int = None,
        y_align: int = None,
        timecode: str,
        tc24hmax: bool = None,
        timecode_rate: float = None,
        reload: int = None,
        alpha: str = None,
        fix_bounds: bool = None,
        start_number: int = None,
        text_source: str,
        ft_load_flags: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.78 drawtext
        Draw a text string or text from a specified file on top of a video, using the
        libfreetype library.

        To enable compilation of this filter, you need to configure FFmpeg with
        --enable-libfreetype and --enable-libharfbuzz.
        To enable default font fallback and the font option you need to
        configure FFmpeg with --enable-libfontconfig.
        To enable the text_shaping option, you need to configure FFmpeg with
        --enable-libfribidi.

        Parameters:
        ----------

        :param str fontfile: None
        :param str text: None
        :param str textfile: None
        :param str fontcolor: None
        :param str fontcolor_expr: None
        :param str boxcolor: None
        :param str bordercolor: None
        :param str shadowcolor: None
        :param bool box: None
        :param str boxborderw: None
        :param int line_spacing: None
        :param str fontsize: None
        :param str text_align: None
        :param str x: None
        :param str y: None
        :param int boxw: None
        :param int boxh: None
        :param int shadowx: None
        :param int shadowy: None
        :param int borderw: None
        :param int tabsize: None
        :param int basetime: None
        :param int expansion: None
        :param int y_align: None
        :param str timecode: None
        :param bool tc24hmax: None
        :param float timecode_rate: None
        :param int reload: None
        :param str alpha: None
        :param bool fix_bounds: None
        :param int start_number: None
        :param str text_source: None
        :param str ft_load_flags: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawtext

        """
        filter_node = FilterNode(
            name="drawtext",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def edgedetect(
        self, *, high: float = None, low: float = None, mode: int = None, planes: str = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.79 edgedetect
        Detect and draw edges. The filter uses the Canny Edge Detection algorithm.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float high: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param float low: Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        :param int mode: Define the drawing mode. ‘wires’ Draw white/gray wires on black background. ‘colormix’ Mix the colors to create a paint/cartoon effect. ‘canny’ Apply Canny edge detector on all selected planes. Default value is wires.
        :param str planes: Select planes for filtering. By default all available planes are filtered.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#edgedetect

        """
        filter_node = FilterNode(
            name="edgedetect",
            streams=[
                self,
            ],
            kwargs={
                "high": high,
                "low": low,
                "mode": mode,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def elbg(
        self,
        *,
        codebook_length: int = None,
        nb_steps: int = None,
        seed: int = None,
        pal8: bool = None,
        use_alpha: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.80 elbg
        Apply a posterize effect using the ELBG (Enhanced LBG) algorithm.

        For each input image, the filter will compute the optimal mapping from
        the input to the output given the codebook length, that is the number
        of distinct output colors.

        This filter accepts the following options.

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
            streams=[
                self,
            ],
            kwargs={
                "codebook_length": codebook_length,
                "nb_steps": nb_steps,
                "seed": seed,
                "pal8": pal8,
                "use_alpha": use_alpha,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def entropy(self, *, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.81 entropy
        Measure graylevel entropy in histogram of color channels of video frames.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int mode: Can be either normal or diff. Default is normal. diff mode measures entropy of histogram delta values, absolute differences between neighbour histogram values.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#entropy

        """
        filter_node = FilterNode(
            name="entropy",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def epx(self, *, n: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.82 epx
        Apply the EPX magnification filter which is designed for pixel art.

        It accepts the following option:

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for 2xEPX, 3 for 3xEPX. Default is 3.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#epx

        """
        filter_node = FilterNode(
            name="epx",
            streams=[
                self,
            ],
            kwargs={
                "n": n,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def eq(
        self,
        *,
        contrast: str = None,
        brightness: str = None,
        saturation: str = None,
        gamma: str = None,
        gamma_r: str = None,
        gamma_g: str = None,
        gamma_b: str = None,
        gamma_weight: str = None,
        eval: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.83 eq
        Set brightness, contrast, saturation and approximate gamma adjustment.

        The filter accepts the following options:


        The expressions accept the following parameters:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#eq

        """
        filter_node = FilterNode(
            name="eq",
            streams=[
                self,
            ],
            kwargs={
                "contrast": contrast,
                "brightness": brightness,
                "saturation": saturation,
                "gamma": gamma,
                "gamma_r": gamma_r,
                "gamma_g": gamma_g,
                "gamma_b": gamma_b,
                "gamma_weight": gamma_weight,
                "eval": eval,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def erosion(
        self,
        *,
        coordinates: int = None,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.84 erosion
        Apply erosion effect to the video.

        This filter replaces the pixel by the local(3x3) minimum.

        It accepts the following options:

        Parameters:
        ----------

        :param int coordinates: Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8
        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#erosion

        """
        filter_node = FilterNode(
            name="erosion",
            streams=[
                self,
            ],
            kwargs={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def estdif(
        self,
        *,
        mode: int = None,
        parity: int = None,
        deint: int = None,
        rslope: int = None,
        redge: int = None,
        ecost: int = None,
        mcost: int = None,
        dcost: int = None,
        interp: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.85 estdif
        Deinterlace the input video ("estdif" stands for "Edge Slope
        Tracing Deinterlacing Filter").

        Spatial only filter that uses edge slope tracing algorithm
        to interpolate missing lines.
        It accepts the following parameters:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#estdif

        """
        filter_node = FilterNode(
            name="estdif",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "parity": parity,
                "deint": deint,
                "rslope": rslope,
                "redge": redge,
                "ecost": ecost,
                "mcost": mcost,
                "dcost": dcost,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def exposure(self, *, exposure: float = None, black: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.86 exposure
        Adjust exposure of the video stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float exposure: Set the exposure correction in EV. Allowed range is from -3.0 to 3.0 EV Default value is 0 EV.
        :param float black: Set the black level correction. Allowed range is from -1.0 to 1.0. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#exposure

        """
        filter_node = FilterNode(
            name="exposure",
            streams=[
                self,
            ],
            kwargs={
                "exposure": exposure,
                "black": black,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def extractplanes(self, *, planes: str = None, **kwargs: Any) -> FilterNode:
        """

        11.87 extractplanes
        Extract color channel components from input video stream into
        separate grayscale video streams.

        The filter accepts the following option:

        Parameters:
        ----------

        :param str planes: Set plane(s) to extract. Available values for planes are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’ Choosing planes not available in the input will result in an error. That means you cannot select r, g, b planes with y, u, v planes at same time.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extractplanes

        """
        filter_node = FilterNode(
            name="extractplanes",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )

        return filter_node

    def fade(
        self,
        *,
        type: int = None,
        start_frame: int = None,
        nb_frames: int = None,
        alpha: bool = None,
        start_time: int = None,
        duration: int = None,
        color: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.88 fade
        Apply a fade-in/out effect to the input video.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int type: The effect type can be either "in" for a fade-in, or "out" for a fade-out effect. Default is in.
        :param int start_frame: Specify the number of the frame to start applying the fade effect at. Default is 0.
        :param int nb_frames: The number of frames that the fade effect lasts. At the end of the fade-in effect, the output video will have the same intensity as the input video. At the end of the fade-out transition, the output video will be filled with the selected color. Default is 25.
        :param bool alpha: If set to 1, fade only alpha channel, if one exists on the input. Default value is 0.
        :param int start_time: Specify the timestamp (in seconds) of the frame to start to apply the fade effect. If both start_frame and start_time are specified, the fade will start at whichever comes last. Default is 0.
        :param int duration: The number of seconds for which the fade effect has to last. At the end of the fade-in effect the output video will have the same intensity as the input video, at the end of the fade-out transition the output video will be filled with the selected color. If both duration and nb_frames are specified, duration is used. Default is 0 (nb_frames is used by default).
        :param str color: Specify the color of the fade. Default is "black".

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fade

        """
        filter_node = FilterNode(
            name="fade",
            streams=[
                self,
            ],
            kwargs={
                "type": type,
                "start_frame": start_frame,
                "nb_frames": nb_frames,
                "alpha": alpha,
                "start_time": start_time,
                "duration": duration,
                "color": color,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def feedback(
        self, _feedin: "VideoStream", *, x: int = None, y: int = None, w: int = None, h: int = None, **kwargs: Any
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
                self,
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
            filter_node._vs(0),
            filter_node._vs(1),
        )

    def fftdnoiz(
        self,
        *,
        sigma: float = None,
        amount: float = None,
        block: int = None,
        overlap: float = None,
        method: int = None,
        prev: int = None,
        next: int = None,
        planes: int = None,
        window: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.90 fftdnoiz
        Denoise frames using 3D FFT (frequency domain filtering).

        The filter accepts the following options:

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
        :param int window: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz

        """
        filter_node = FilterNode(
            name="fftdnoiz",
            streams=[
                self,
            ],
            kwargs={
                "sigma": sigma,
                "amount": amount,
                "block": block,
                "overlap": overlap,
                "method": method,
                "prev": prev,
                "next": next,
                "planes": planes,
                "window": window,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fftfilt(
        self,
        *,
        dc_Y: int = None,
        dc_U: int = None,
        dc_V: int = None,
        weight_Y: str = None,
        weight_U: str,
        weight_V: str,
        eval: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.91 fftfilt
        Apply arbitrary expressions to samples in frequency domain

        Parameters:
        ----------

        :param int dc_Y: Adjust the dc value (gain) of the luma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param int dc_U: Adjust the dc value (gain) of the 1st chroma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param int dc_V: Adjust the dc value (gain) of the 2nd chroma plane of the image. The filter accepts an integer value in range 0 to 1000. The default value is set to 0.
        :param str weight_Y: Set the frequency domain weight expression for the luma plane.
        :param str weight_U: Set the frequency domain weight expression for the 1st chroma plane.
        :param str weight_V: Set the frequency domain weight expression for the 2nd chroma plane.
        :param int eval: Set when the expressions are evaluated. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization. ‘frame’ Evaluate expressions for each incoming frame. Default value is ‘init’. The filter accepts the following variables:

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fftfilt

        """
        filter_node = FilterNode(
            name="fftfilt",
            streams=[
                self,
            ],
            kwargs={
                "dc_Y": dc_Y,
                "dc_U": dc_U,
                "dc_V": dc_V,
                "weight_Y": weight_Y,
                "weight_U": weight_U,
                "weight_V": weight_V,
                "eval": eval,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def field(self, *, type: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.92 field
        Extract a single field from an interlaced image using stride
        arithmetic to avoid wasting CPU time. The output frames are marked as
        non-interlaced.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int type: Specify whether to extract the top (if the value is 0 or top) or the bottom field (if the value is 1 or bottom).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#field

        """
        filter_node = FilterNode(
            name="field",
            streams=[
                self,
            ],
            kwargs={
                "type": type,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fieldhint(self, *, hint: str, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.93 fieldhint
        Create new frames by copying the top and bottom fields from surrounding frames
        supplied as numbers by the hint file.


        Example of first several lines of hint file for relative mode:

        0,0 - # first frame
        1,0 - # second frame, use third's frame top field and second's frame bottom field
        1,0 - # third frame, use fourth's frame top field and third's frame bottom field
        1,0 -
        0,0 -
        0,0 -
        1,0 -
        1,0 -
        1,0 -
        0,0 -
        0,0 -
        1,0 -
        1,0 -
        1,0 -
        0,0 -

        Parameters:
        ----------

        :param str hint: Set file containing hints: absolute/relative frame numbers. There must be one line for each frame in a clip. Each line must contain two numbers separated by the comma, optionally followed by - or +. Numbers supplied on each line of file can not be out of [N-1,N+1] where N is current frame number for absolute mode or out of [-1, 1] range for relative mode. First number tells from which frame to pick up top field and second number tells from which frame to pick up bottom field. If optionally followed by + output frame will be marked as interlaced, else if followed by - output frame will be marked as progressive, else it will be marked same as input frame. If optionally followed by t output frame will use only top field, or in case of b it will use only bottom field. If line starts with # or ; that line is skipped.
        :param int mode: Can be item absolute or relative or pattern. Default is absolute. The pattern mode is same as relative mode, except at last entry of file if there are more frames to process than hint file is seek back to start.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldhint

        """
        filter_node = FilterNode(
            name="fieldhint",
            streams=[
                self,
            ],
            kwargs={
                "hint": hint,
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fieldmatch(
        self,
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
                self,
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
        return filter_node._vs(0)

    def fieldorder(self, *, order: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.95 fieldorder
        Transform the field order of the input video.

        It accepts the following parameters:


        The default value is ‘tff’.

        The transformation is done by shifting the picture content up or down
        by one line, and filling the remaining line with appropriate picture content.
        This method is consistent with most broadcast field order converters.

        If the input video is not flagged as being interlaced, or it is already
        flagged as being of the required output field order, then this filter does
        not alter the incoming video.

        It is very useful when converting to or from PAL DV material,
        which is bottom field first.

        For example:

        ffmpeg -i in.vob -vf "fieldorder=bff" out.dv

        Parameters:
        ----------

        :param int order: The output field order. Valid values are tff for top field first or bff for bottom field first.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldorder

        """
        filter_node = FilterNode(
            name="fieldorder",
            streams=[
                self,
            ],
            kwargs={
                "order": order,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fifo(self, **kwargs: Any) -> "VideoStream":
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
            name="fifo",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def fillborders(
        self,
        *,
        left: int = None,
        right: int = None,
        top: int = None,
        bottom: int = None,
        mode: int = None,
        color: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.97 fillborders
        Fill borders of the input video, without changing video stream dimensions.
        Sometimes video can have garbage at the four edges and you may not want to
        crop video input to keep size multiple of some number.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int left: Number of pixels to fill from left border.
        :param int right: Number of pixels to fill from right border.
        :param int top: Number of pixels to fill from top border.
        :param int bottom: Number of pixels to fill from bottom border.
        :param int mode: Set fill mode. It accepts the following values: ‘smear’ fill pixels using outermost pixels ‘mirror’ fill pixels using mirroring (half sample symmetric) ‘fixed’ fill pixels with constant value ‘reflect’ fill pixels using reflecting (whole sample symmetric) ‘wrap’ fill pixels using wrapping ‘fade’ fade pixels to constant value ‘margins’ fill pixels at top and bottom with weighted averages pixels near borders Default is smear.
        :param str color: Set color for pixels in fixed or fade mode. Default is black.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fillborders

        """
        filter_node = FilterNode(
            name="fillborders",
            streams=[
                self,
            ],
            kwargs={
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
                "mode": mode,
                "color": color,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def find_rect(
        self,
        *,
        object: str,
        threshold: float = None,
        mipmaps: int = None,
        xmin: int = None,
        ymin: int = None,
        xmax: int = None,
        ymax: int = None,
        discard: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.98 find_rect
        Find a rectangular object in the input video.

        The object to search for must be specified as a gray8 image specified with the
        object option.

        For each possible match, a score is computed. If the score reaches the specified
        threshold, the object is considered found.

        If the input video contains multiple instances of the object, the filter will
        find only one of them.

        When an object is found, the following metadata entries are set in the matching
        frame:

        It accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "object": object,
                "threshold": threshold,
                "mipmaps": mipmaps,
                "xmin": xmin,
                "ymin": ymin,
                "xmax": xmax,
                "ymax": ymax,
                "discard": discard,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def flip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        14.8 flip_vulkan
        Flips an image along both the vertical and horizontal axis.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#flip_005fvulkan

        """
        filter_node = FilterNode(
            name="flip_vulkan",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def floodfill(
        self,
        *,
        x: int = None,
        y: int = None,
        s0: int = None,
        s1: int = None,
        s2: int = None,
        s3: int = None,
        d0: int = None,
        d1: int = None,
        d2: int = None,
        d3: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.99 floodfill
        Flood area with values of same pixel components with another values.

        It accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#floodfill

        """
        filter_node = FilterNode(
            name="floodfill",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def format(self, *, pix_fmts: str, **kwargs: Any) -> "VideoStream":
        """

        11.100 format
        Convert the input video to one of the specified pixel formats.
        Libavfilter will try to pick one that is suitable as input to
        the next filter.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str pix_fmts: A ’|’-separated list of pixel format names, such as "pix_fmts=yuv420p|monow|rgb24".

        Ref: https://ffmpeg.org/ffmpeg-filters.html#format

        """
        filter_node = FilterNode(
            name="format",
            streams=[
                self,
            ],
            kwargs={
                "pix_fmts": pix_fmts,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fps(
        self, *, fps: str = None, start_time: float = None, round: int = None, eof_action: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.101 fps
        Convert the video to specified constant frame rate by duplicating or dropping
        frames as necessary.

        It accepts the following parameters:

        Alternatively, the options can be specified as a flat string:
        fps[:start_time[:round]].

        See also the setpts filter.

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
            streams=[
                self,
            ],
            kwargs={
                "fps": fps,
                "start_time": start_time,
                "round": round,
                "eof_action": eof_action,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def framepack(self, _right: "VideoStream", *, format: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _right,
            ],
            kwargs={
                "format": format,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def framerate(
        self,
        *,
        fps: str = None,
        interp_start: int = None,
        interp_end: int = None,
        scene: float = None,
        flags: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.103 framerate
        Change the frame rate by interpolating new video output frames from the source
        frames.

        This filter is not designed to function correctly with interlaced media. If
        you wish to change the frame rate of interlaced media then you are required
        to deinterlace before this filter and re-interlace after this filter.

        A description of the accepted options follows.

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
            streams=[
                self,
            ],
            kwargs={
                "fps": fps,
                "interp_start": interp_start,
                "interp_end": interp_end,
                "scene": scene,
                "flags": flags,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def framestep(self, *, step: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.104 framestep
        Select one frame every N-th frame.

        This filter accepts the following option:

        Parameters:
        ----------

        :param int step: Select frame after every step frames. Allowed values are positive integers higher than 0. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framestep

        """
        filter_node = FilterNode(
            name="framestep",
            streams=[
                self,
            ],
            kwargs={
                "step": step,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def freezedetect(self, *, n: float = None, d: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.105 freezedetect
        Detect frozen video.

        This filter logs a message and sets frame metadata when it detects that the
        input video has no significant change in content during a specified duration.
        Video freeze detection calculates the mean average absolute difference of all
        the components of video frames and compares it to a noise floor.

        The printed times and duration are expressed in seconds. The
        lavfi.freezedetect.freeze_start metadata key is set on the first frame
        whose timestamp equals or exceeds the detection duration and it contains the
        timestamp of the first frame of the freeze. The
        lavfi.freezedetect.freeze_duration and
        lavfi.freezedetect.freeze_end metadata keys are set on the first frame
        after the freeze.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float n: Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or as a difference ratio between 0 and 1. Default is -60dB, or 0.001.
        :param int d: Set freeze duration until notification (default is 2 seconds).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#freezedetect

        """
        filter_node = FilterNode(
            name="freezedetect",
            streams=[
                self,
            ],
            kwargs={
                "n": n,
                "d": d,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def freezeframes(
        self, _replace: "VideoStream", *, first: int = None, last: int = None, replace: int = None, **kwargs: Any
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
                self,
                _replace,
            ],
            kwargs={
                "first": first,
                "last": last,
                "replace": replace,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def frei0r(self, *, filter_name: str, filter_params: str, **kwargs: Any) -> "VideoStream":
        """

        11.107 frei0r
        Apply a frei0r effect to the input video.

        To enable the compilation of this filter, you need to install the frei0r
        header and configure FFmpeg with --enable-frei0r.

        It accepts the following parameters:


        A frei0r effect parameter can be a boolean (its value is either
        "y" or "n"), a double, a color (specified as
        R/G/B, where R, G, and B are floating point
        numbers between 0.0 and 1.0, inclusive) or a color description as specified in the
        (ffmpeg-utils)"Color" section in the ffmpeg-utils manual,
        a position (specified as X/Y, where
        X and Y are floating point numbers) and/or a string.

        The number and types of parameters depend on the loaded effect. If an
        effect parameter is not specified, the default value is set.

        Parameters:
        ----------

        :param str filter_name: The name of the frei0r effect to load. If the environment variable FREI0R_PATH is defined, the frei0r effect is searched for in each of the directories specified by the colon-separated list in FREI0R_PATH. Otherwise, the standard frei0r paths are searched, in this order: HOME/.frei0r-1/lib/, /usr/local/lib/frei0r-1/, /usr/lib/frei0r-1/.
        :param str filter_params: A ’|’-separated list of parameters to pass to the frei0r effect.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#frei0r

        """
        filter_node = FilterNode(
            name="frei0r",
            streams=[
                self,
            ],
            kwargs={
                "filter_name": filter_name,
                "filter_params": filter_params,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def fspp(
        self, *, quality: int = None, qp: int = None, strength: int = None, use_bframe_qp: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.108 fspp
        Apply fast and simple postprocessing. It is a faster version of spp.

        It splits (I)DCT into horizontal/vertical passes. Unlike the simple post-
        processing filter, one of them is performed once per block, not per pixel.
        This allows for much higher speed.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 4-5. Default value is 4.
        :param int qp: Force a constant quantization parameter. It accepts an integer in range 0-63. If not set, the filter will use the QP from the video stream (if available).
        :param int strength: Set filter strength. It accepts an integer in range -15 to 32. Lower values mean more details but also more artifacts, while higher values make the image smoother but also blurrier. Default value is 0 − PSNR optimal.
        :param bool use_bframe_qp: Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fspp

        """
        filter_node = FilterNode(
            name="fspp",
            streams=[
                self,
            ],
            kwargs={
                "quality": quality,
                "qp": qp,
                "strength": strength,
                "use_bframe_qp": use_bframe_qp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def gblur(
        self, *, sigma: float = None, steps: int = None, planes: int = None, sigmaV: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.109 gblur
        Apply Gaussian blur filter.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float sigma: Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.
        :param int steps: Set number of steps for Gaussian approximation. Default is 1.
        :param int planes: Set which planes to filter. By default all planes are filtered.
        :param float sigmaV: Set vertical sigma, if negative it will be same as sigma. Default is -1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gblur

        """
        filter_node = FilterNode(
            name="gblur",
            streams=[
                self,
            ],
            kwargs={
                "sigma": sigma,
                "steps": steps,
                "planes": planes,
                "sigmaV": sigmaV,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def gblur_vulkan(
        self,
        *,
        sigma: float = None,
        sigmaV: float = None,
        planes: int = None,
        size: int = None,
        sizeV: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        14.9 gblur_vulkan
        Apply Gaussian blur filter on Vulkan frames.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "sigma": sigma,
                "sigmaV": sigmaV,
                "planes": planes,
                "size": size,
                "sizeV": sizeV,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def geq(
        self,
        *,
        lum_expr: str,
        cb_expr: str,
        cr_expr: str,
        alpha_expr: str,
        red_expr: str,
        green_expr: str,
        blue_expr: str,
        interpolation: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.110 geq
        Apply generic equation to each pixel.

        The filter accepts the following options:


        The colorspace is selected according to the specified options. If one
        of the lum_expr, cb_expr, or cr_expr
        options is specified, the filter will automatically select a YCbCr
        colorspace. If one of the red_expr, green_expr, or
        blue_expr options is specified, it will select an RGB
        colorspace.

        If one of the chrominance expression is not defined, it falls back on the other
        one. If no alpha expression is specified it will evaluate to opaque value.
        If none of chrominance expressions are specified, they will evaluate
        to the luma expression.

        The expressions can use the following variables and functions:


        For functions, if x and y are outside the area, the value will be
        automatically clipped to the closer edge.

        Please note that this filter can use multiple threads in which case each slice
        will have its own expression state. If you want to use only a single expression
        state because your expressions depend on previous state then you should limit
        the number of filter threads to 1.

        Parameters:
        ----------

        :param str lum_expr: Set the luma expression.
        :param str cb_expr: Set the chrominance blue expression.
        :param str cr_expr: Set the chrominance red expression.
        :param str alpha_expr: Set the alpha expression.
        :param str red_expr: Set the red expression.
        :param str green_expr: Set the green expression.
        :param str blue_expr: Set the blue expression.
        :param int interpolation: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#geq

        """
        filter_node = FilterNode(
            name="geq",
            streams=[
                self,
            ],
            kwargs={
                "lum_expr": lum_expr,
                "cb_expr": cb_expr,
                "cr_expr": cr_expr,
                "alpha_expr": alpha_expr,
                "red_expr": red_expr,
                "green_expr": green_expr,
                "blue_expr": blue_expr,
                "interpolation": interpolation,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def gradfun(self, *, strength: float = None, radius: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.111 gradfun
        Fix the banding artifacts that are sometimes introduced into nearly flat
        regions by truncation to 8-bit color depth.
        Interpolate the gradients that should go where the bands are, and
        dither them.

        It is designed for playback only.  Do not use it prior to
        lossy compression, because compression tends to lose the dither and
        bring back the bands.

        It accepts the following parameters:


        Alternatively, the options can be specified as a flat string:
        strength[:radius]

        Parameters:
        ----------

        :param float strength: The maximum amount by which the filter will change any one pixel. This is also the threshold for detecting nearly flat regions. Acceptable values range from .51 to 64; the default value is 1.2. Out-of-range values will be clipped to the valid range.
        :param int radius: The neighborhood to fit the gradient to. A larger radius makes for smoother gradients, but also prevents the filter from modifying the pixels near detailed regions. Acceptable values are 8-32; the default value is 16. Out-of-range values will be clipped to the valid range.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gradfun

        """
        filter_node = FilterNode(
            name="gradfun",
            streams=[
                self,
            ],
            kwargs={
                "strength": strength,
                "radius": radius,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def graphmonitor(
        self,
        *,
        size: str = None,
        opacity: float = None,
        mode: str = None,
        flags: str = None,
        rate: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.112 graphmonitor
        Show various filtergraph stats.

        With this filter one can debug complete filtergraph.
        Especially issues with links filling with queued frames.

        The filter accepts the following options:

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
            streams=[
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
        return filter_node._vs(0)

    def grayworld(self, **kwargs: Any) -> "VideoStream":
        """

        11.113 grayworld
        A color constancy filter that applies color correction based on the grayworld assumption

        See: https://www.researchgate.net/publication/275213614_A_New_Color_Correction_Method_for_Underwater_Imaging

        The algorithm  uses linear light, so input
        data should be linearized beforehand (and possibly correctly tagged).


        ffmpeg -i INPUT -vf zscale=transfer=linear,grayworld,zscale=transfer=bt709,format=yuv420p OUTPUT

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#grayworld

        """
        filter_node = FilterNode(
            name="grayworld",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def greyedge(
        self, *, difford: int = None, minknorm: int = None, sigma: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.114 greyedge
        A color constancy variation filter which estimates scene illumination via grey edge algorithm
        and corrects the scene colors accordingly.

        See: https://staff.science.uva.nl/th.gevers/pub/GeversTIP07.pdf

        The filter accepts the following options:

        Parameters:
        ----------

        :param int difford: The order of differentiation to be applied on the scene. Must be chosen in the range [0,2] and default value is 1.
        :param int minknorm: The Minkowski parameter to be used for calculating the Minkowski distance. Must be chosen in the range [0,20] and default value is 1. Set to 0 for getting max value instead of calculating Minkowski distance.
        :param float sigma: The standard deviation of Gaussian blur to be applied on the scene. Must be chosen in the range [0,1024.0] and default value = 1. floor( sigma * break_off_sigma(3) ) can’t be equal to 0 if difford is greater than 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#greyedge

        """
        filter_node = FilterNode(
            name="greyedge",
            streams=[
                self,
            ],
            kwargs={
                "difford": difford,
                "minknorm": minknorm,
                "sigma": sigma,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def guided(
        self,
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
                self,
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
        return filter_node._vs(0)

    def haldclut(self, _clut: "VideoStream", *, clut: int = None, interp: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _clut,
            ],
            kwargs={
                "clut": clut,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hflip(self, **kwargs: Any) -> "VideoStream":
        """

        11.117 hflip
        Flip the input video horizontally.

        For example, to horizontally flip the input video with ffmpeg:

        ffmpeg -i in.avi -vf "hflip" out.avi

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#hflip

        """
        filter_node = FilterNode(
            name="hflip",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def hflip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        14.7 hflip_vulkan
        Flips an image horizontally.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#hflip_005fvulkan

        """
        filter_node = FilterNode(
            name="hflip_vulkan",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def histeq(
        self, *, strength: float = None, intensity: float = None, antibanding: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.118 histeq
        This filter applies a global color histogram equalization on a
        per-frame basis.

        It can be used to correct video that has a compressed range of pixel
        intensities.  The filter redistributes the pixel intensities to
        equalize their distribution across the intensity range. It may be
        viewed as an "automatically adjusting contrast filter". This filter is
        useful only for correcting degraded or poorly captured source
        video.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float strength: Determine the amount of equalization to be applied. As the strength is reduced, the distribution of pixel intensities more-and-more approaches that of the input frame. The value must be a float number in the range [0,1] and defaults to 0.200.
        :param float intensity: Set the maximum intensity that can generated and scale the output values appropriately. The strength should be set as desired and then the intensity can be limited if needed to avoid washing-out. The value must be a float number in the range [0,1] and defaults to 0.210.
        :param int antibanding: Set the antibanding level. If enabled the filter will randomly vary the luminance of output pixels by a small amount to avoid banding of the histogram. Possible values are none, weak or strong. It defaults to none.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#histeq

        """
        filter_node = FilterNode(
            name="histeq",
            streams=[
                self,
            ],
            kwargs={
                "strength": strength,
                "intensity": intensity,
                "antibanding": antibanding,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def histogram(
        self,
        *,
        level_height: int = None,
        scale_height: int = None,
        display_mode: int = None,
        levels_mode: int = None,
        components: int = None,
        fgopacity: float = None,
        bgopacity: float = None,
        colors_mode: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.119 histogram
        Compute and draw a color distribution histogram for the input video.

        The computed histogram is a representation of the color component
        distribution in an image.

        Standard histogram displays the color components distribution in an image.
        Displays color graph for each color component. Shows distribution of
        the Y, U, V, A or R, G, B components, depending on input format, in the
        current frame. Below each graph a color component scale meter is shown.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "level_height": level_height,
                "scale_height": scale_height,
                "display_mode": display_mode,
                "levels_mode": levels_mode,
                "components": components,
                "fgopacity": fgopacity,
                "bgopacity": bgopacity,
                "colors_mode": colors_mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hqdn3d(
        self,
        *,
        luma_spatial: float = None,
        chroma_spatial: float = None,
        luma_tmp: float = None,
        chroma_tmp: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.120 hqdn3d
        This is a high precision/quality 3d denoise filter. It aims to reduce
        image noise, producing smooth images and making still images really
        still. It should enhance compressibility.

        It accepts the following optional parameters:

        Parameters:
        ----------

        :param float luma_spatial: A non-negative floating point number which specifies spatial luma strength. It defaults to 4.0.
        :param float chroma_spatial: A non-negative floating point number which specifies spatial chroma strength. It defaults to 3.0*luma_spatial/4.0.
        :param float luma_tmp: A floating point number which specifies luma temporal strength. It defaults to 6.0*luma_spatial/4.0.
        :param float chroma_tmp: A floating point number which specifies chroma temporal strength. It defaults to luma_tmp*chroma_spatial/luma_spatial.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqdn3d

        """
        filter_node = FilterNode(
            name="hqdn3d",
            streams=[
                self,
            ],
            kwargs={
                "luma_spatial": luma_spatial,
                "chroma_spatial": chroma_spatial,
                "luma_tmp": luma_tmp,
                "chroma_tmp": chroma_tmp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hqx(self, *, n: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.125 hqx
        Apply a high-quality magnification filter designed for pixel art. This filter
        was originally created by Maxim Stepin.

        It accepts the following option:

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for hq2x, 3 for hq3x and 4 for hq4x. Default is 3.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqx

        """
        filter_node = FilterNode(
            name="hqx",
            streams=[
                self,
            ],
            kwargs={
                "n": n,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hstack(
        self, *streams: "VideoStream", inputs: int = None, shortest: bool = None, **kwargs: Any
    ) -> "VideoStream":
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "shortest": shortest,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hsvhold(
        self,
        *,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.127 hsvhold
        Turns a certain HSV range into gray values.

        This filter measures color difference between set HSV color in options
        and ones measured in video stream. Depending on options, output
        colors can be changed to be gray or not.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float hue: Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        :param float sat: Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float val: Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float similarity: Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more gray pixels, with a higher gray pixel the more similar the pixels color is to the key color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvhold

        """
        filter_node = FilterNode(
            name="hsvhold",
            streams=[
                self,
            ],
            kwargs={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hsvkey(
        self,
        *,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.128 hsvkey
        Turns a certain HSV range into transparency.

        This filter measures color difference between set HSV color in options
        and ones measured in video stream. Depending on options, output
        colors can be changed to transparent by adding alpha channel.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float hue: Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        :param float sat: Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float val: Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        :param float similarity: Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        :param float blend: Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvkey

        """
        filter_node = FilterNode(
            name="hsvkey",
            streams=[
                self,
            ],
            kwargs={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hue(self, *, h: str, s: str = None, H: str, b: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.129 hue
        Modify the hue and/or the saturation of the input.

        It accepts the following parameters:


        h and H are mutually exclusive, and can’t be
        specified at the same time.

        The b, h, H and s option values are
        expressions containing the following constants:

        Parameters:
        ----------

        :param str h: Specify the hue angle as a number of degrees. It accepts an expression, and defaults to "0".
        :param str s: Specify the saturation in the [-10,10] range. It accepts an expression and defaults to "1".
        :param str H: Specify the hue angle as a number of radians. It accepts an expression, and defaults to "0".
        :param str b: Specify the brightness in the [-10,10] range. It accepts an expression and defaults to "0".

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hue

        """
        filter_node = FilterNode(
            name="hue",
            streams=[
                self,
            ],
            kwargs={
                "h": h,
                "s": s,
                "H": H,
                "b": b,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def huesaturation(
        self,
        *,
        hue: float = None,
        saturation: float = None,
        intensity: float = None,
        colors: str = None,
        strength: float = None,
        rw: float = None,
        gw: float = None,
        bw: float = None,
        lightness: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.130 huesaturation
        Apply hue-saturation-intensity adjustments to input video stream.

        This filter operates in RGB colorspace.

        This filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#huesaturation

        """
        filter_node = FilterNode(
            name="huesaturation",
            streams=[
                self,
            ],
            kwargs={
                "hue": hue,
                "saturation": saturation,
                "intensity": intensity,
                "colors": colors,
                "strength": strength,
                "rw": rw,
                "gw": gw,
                "bw": bw,
                "lightness": lightness,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hwdownload(self, **kwargs: Any) -> "VideoStream":
        """

        11.121 hwdownload
        Download hardware frames to system memory.

        The input must be in hardware frames, and the output a non-hardware format.
        Not all formats will be supported on the output - it may be necessary to insert
        an additional format filter immediately following in the graph to get
        the output in a supported format.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwdownload

        """
        filter_node = FilterNode(
            name="hwdownload",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def hwmap(self, *, mode: str = None, derive_device: str, reverse: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.122 hwmap
        Map hardware frames to system memory or to another device.

        This filter has several different modes of operation; which one is used depends
        on the input and output formats:

         Hardware frame input, normal frame output

        Map the input frames to system memory and pass them to the output.  If the
        original hardware frame is later required (for example, after overlaying
        something else on part of it), the hwmap filter can be used again
        in the next mode to retrieve it.
         Normal frame input, hardware frame output

        If the input is actually a software-mapped hardware frame, then unmap it -
        that is, return the original hardware frame.

        Otherwise, a device must be provided.  Create new hardware surfaces on that
        device for the output, then map them back to the software format at the input
        and give those frames to the preceding filter.  This will then act like the
        hwupload filter, but may be able to avoid an additional copy when
        the input is already in a compatible format.
         Hardware frame input and output

        A device must be supplied for the output, either directly or with the
        derive_device option.  The input and output devices must be of
        different types and compatible - the exact meaning of this is
        system-dependent, but typically it means that they must refer to the same
        underlying hardware context (for example, refer to the same graphics card).

        If the input frames were originally created on the output device, then unmap
        to retrieve the original frames.

        Otherwise, map the frames to the output device - create new hardware frames
        on the output corresponding to the frames on the input.

        The following additional parameters are accepted:

        Parameters:
        ----------

        :param str mode: Set the frame mapping mode. Some combination of: read The mapped frame should be readable. write The mapped frame should be writeable. overwrite The mapping will always overwrite the entire frame. This may improve performance in some cases, as the original contents of the frame need not be loaded. direct The mapping must not involve any copying. Indirect mappings to copies of frames are created in some cases where either direct mapping is not possible or it would have unexpected properties. Setting this flag ensures that the mapping is direct and will fail if that is not possible. Defaults to read+write if not specified.
        :param str derive_device: Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.
        :param int reverse: In a hardware to hardware mapping, map in reverse - create frames in the sink and map them back to the source. This may be necessary in some cases where a mapping in one direction is required but only the opposite direction is supported by the devices being used. This option is dangerous - it may break the preceding filter in undefined ways if there are any additional constraints on that filter’s output. Do not use it without fully understanding the implications of its use.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwmap

        """
        filter_node = FilterNode(
            name="hwmap",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "derive_device": derive_device,
                "reverse": reverse,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hwupload(self, *, derive_device: str, **kwargs: Any) -> "VideoStream":
        """

        11.123 hwupload
        Upload system memory frames to hardware surfaces.

        The device to upload to must be supplied when the filter is initialised.  If
        using ffmpeg, select the appropriate device with the -filter_hw_device
        option or with the derive_device option.  The input and output devices
        must be of different types and compatible - the exact meaning of this is
        system-dependent, but typically it means that they must refer to the same
        underlying hardware context (for example, refer to the same graphics card).

        The following additional parameters are accepted:

        Parameters:
        ----------

        :param str derive_device: Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload

        """
        filter_node = FilterNode(
            name="hwupload",
            streams=[
                self,
            ],
            kwargs={
                "derive_device": derive_device,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hwupload_cuda(self, *, device: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.124 hwupload_cuda
        Upload system memory frames to a CUDA device.

        It accepts the following optional parameters:

        Parameters:
        ----------

        :param int device: The number of the CUDA device to use

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload_005fcuda

        """
        filter_node = FilterNode(
            name="hwupload_cuda",
            streams=[
                self,
            ],
            kwargs={
                "device": device,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def hysteresis(
        self, _alt: "VideoStream", *, planes: int = None, threshold: int = None, **kwargs: Any
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
                self,
                _alt,
            ],
            kwargs={
                "planes": planes,
                "threshold": threshold,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def iccdetect(self, *, force: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.132 iccdetect
        Detect the colorspace  from an embedded ICC profile (if present), and update
        the frame’s tags accordingly.

        This filter accepts the following options:

        Parameters:
        ----------

        :param bool force: If true, the frame’s existing colorspace tags will always be overridden by values detected from an ICC profile. Otherwise, they will only be assigned if they contain unknown. Enabled by default.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccdetect

        """
        filter_node = FilterNode(
            name="iccdetect",
            streams=[
                self,
            ],
            kwargs={
                "force": force,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def iccgen(
        self, *, color_primaries: int = None, color_trc: int = None, force: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.133 iccgen
        Generate ICC profiles and attach them to frames.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int color_primaries: Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        :param int color_trc: Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        :param bool force: If true, an ICC profile will be generated even if it would overwrite an already existing ICC profile. Disabled by default.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccgen

        """
        filter_node = FilterNode(
            name="iccgen",
            streams=[
                self,
            ],
            kwargs={
                "color_primaries": color_primaries,
                "color_trc": color_trc,
                "force": force,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def identity(self, _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
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
                self,
                _reference,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def idet(
        self,
        *,
        intl_thres: float = None,
        prog_thres: float = None,
        rep_thres: float = None,
        half_life: float = None,
        analyze_interlaced_flag: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.135 idet
        Detect video interlacing type.

        This filter tries to detect if the input frames are interlaced, progressive,
        top or bottom field first. It will also try to detect fields that are
        repeated between adjacent frames (a sign of telecine).

        Single frame detection considers only immediately adjacent frames when classifying each frame.
        Multiple frame detection incorporates the classification history of previous frames.

        The filter will log these metadata values:


        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "intl_thres": intl_thres,
                "prog_thres": prog_thres,
                "rep_thres": rep_thres,
                "half_life": half_life,
                "analyze_interlaced_flag": analyze_interlaced_flag,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def il(
        self,
        *,
        luma_mode: int = None,
        chroma_mode: int = None,
        alpha_mode: int = None,
        luma_swap: bool = None,
        chroma_swap: bool = None,
        alpha_swap: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.136 il
        Deinterleave or interleave fields.

        This filter allows one to process interlaced images fields without
        deinterlacing them. Deinterleaving splits the input frame into 2
        fields (so called half pictures). Odd lines are moved to the top
        half of the output image, even lines to the bottom half.
        You can process (filter) them independently and then re-interleave them.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int luma_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param int chroma_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param int alpha_mode: Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        :param bool luma_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        :param bool chroma_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        :param bool alpha_swap: Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#il

        """
        filter_node = FilterNode(
            name="il",
            streams=[
                self,
            ],
            kwargs={
                "luma_mode": luma_mode,
                "chroma_mode": chroma_mode,
                "alpha_mode": alpha_mode,
                "luma_swap": luma_swap,
                "chroma_swap": chroma_swap,
                "alpha_swap": alpha_swap,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def inflate(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.137 inflate
        Apply inflate effect to the video.

        This filter replaces the pixel by the local(3x3) average by taking into account
        only values higher than the pixel.

        It accepts the following options:

        Parameters:
        ----------

        :param int threshold0: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold1: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold2: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        :param int threshold3: Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#inflate

        """
        filter_node = FilterNode(
            name="inflate",
            streams=[
                self,
            ],
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def interlace(self, *, scan: int = None, lowpass: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.138 interlace
        Simple interlacing filter from progressive contents. This interleaves upper (or
        lower) lines from odd frames with lower (or upper) lines from even frames,
        halving the frame rate and preserving image height.


           Original        Original             New Frame
           Frame 'j'      Frame 'j+1'             (tff)
          ==========      ===========       ==================
            Line 0  -------------------->    Frame 'j' Line 0
            Line 1          Line 1  ---->   Frame 'j+1' Line 1
            Line 2 --------------------->    Frame 'j' Line 2
            Line 3          Line 3  ---->   Frame 'j+1' Line 3
             ...             ...                   ...
        New Frame + 1 will be generated by Frame 'j+2' and Frame 'j+3' and so on

        It accepts the following optional parameters:

        Parameters:
        ----------

        :param int scan: This determines whether the interlaced frame is taken from the even (tff - default) or odd (bff) lines of the progressive frame.
        :param int lowpass: Vertical lowpass filter to avoid twitter interlacing and reduce moire patterns. ‘0, off’ Disable vertical lowpass filter ‘1, linear’ Enable linear filter (default) ‘2, complex’ Enable complex filter. This will slightly less reduce twitter and moire but better retain detail and subjective sharpness impression.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#interlace

        """
        filter_node = FilterNode(
            name="interlace",
            streams=[
                self,
            ],
            kwargs={
                "scan": scan,
                "lowpass": lowpass,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def interleave(
        self, *streams: "VideoStream", nb_inputs: int = None, duration: int = None, **kwargs: Any
    ) -> "VideoStream":
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
                self,
                *streams,
            ],
            kwargs={
                "nb_inputs": nb_inputs,
                "duration": duration,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def kerndeint(
        self,
        *,
        thresh: int = None,
        map: bool = None,
        order: bool = None,
        sharp: bool = None,
        twoway: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.139 kerndeint
        Deinterlace input video by applying Donald Graft’s adaptive kernel
        deinterling. Work on interlaced parts of a video to produce
        progressive frames.

        The description of the accepted parameters follows.

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
            streams=[
                self,
            ],
            kwargs={
                "thresh": thresh,
                "map": map,
                "order": order,
                "sharp": sharp,
                "twoway": twoway,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def kirsch(self, *, planes: int = None, scale: float = None, delta: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.140 kirsch
        Apply kirsch operator to input video stream.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#kirsch

        """
        filter_node = FilterNode(
            name="kirsch",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lagfun(self, *, decay: float = None, planes: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.141 lagfun
        Slowly update darker pixels.

        This filter makes short flashes of light appear longer.
        This filter accepts the following options:

        Parameters:
        ----------

        :param float decay: Set factor for decaying. Default is .95. Allowed range is from 0 to 1.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lagfun

        """
        filter_node = FilterNode(
            name="lagfun",
            streams=[
                self,
            ],
            kwargs={
                "decay": decay,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def latency(self, **kwargs: Any) -> "VideoStream":
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
            name="latency",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def lenscorrection(
        self,
        *,
        cx: float = None,
        cy: float = None,
        k1: float = None,
        k2: float = None,
        i: int = None,
        fc: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.142 lenscorrection
        Correct radial lens distortion

        This filter can be used to correct for radial distortion as can result from the use
        of wide angle lenses, and thereby re-rectify the image. To find the right parameters
        one can use tools available for example as part of opencv or simply trial-and-error.
        To use opencv use the calibration sample (under samples/cpp) from the opencv sources
        and extract the k1 and k2 coefficients from the resulting matrix.

        Note that effectively the same filter is available in the open-source tools Krita and
        Digikam from the KDE project.

        In contrast to the vignette filter, which can also be used to compensate lens errors,
        this filter corrects the distortion of the image, whereas vignette corrects the
        brightness distribution, so you may want to use both filters together in certain
        cases, though you will have to take care of ordering, i.e. whether vignetting should
        be applied before or after lens correction.

        Parameters:
        ----------

        :param float cx: None
        :param float cy: None
        :param float k1: None
        :param float k2: None
        :param int i: None
        :param str fc: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lenscorrection

        """
        filter_node = FilterNode(
            name="lenscorrection",
            streams=[
                self,
            ],
            kwargs={
                "cx": cx,
                "cy": cy,
                "k1": k1,
                "k2": k2,
                "i": i,
                "fc": fc,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lensfun(
        self,
        *,
        make: str,
        model: str,
        lens_model: str,
        db_path: str,
        mode: int = None,
        focal_length: float = None,
        aperture: float = None,
        focus_distance: float = None,
        scale: float = None,
        target_geometry: int = None,
        reverse: bool = None,
        interpolation: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.143 lensfun
        Apply lens correction via the lensfun library (http://lensfun.sourceforge.net/).

        The lensfun filter requires the camera make, camera model, and lens model
        to apply the lens correction. The filter will load the lensfun database and
        query it to find the corresponding camera and lens entries in the database. As
        long as these entries can be found with the given options, the filter can
        perform corrections on frames. Note that incomplete strings will result in the
        filter choosing the best match with the given options, and the filter will
        output the chosen camera and lens models (logged with level "info"). You must
        provide the make, camera model, and lens model as they are required.

        To obtain a list of available makes and models, leave out one or both of make and
        model options. The filter will send the full list to the log with level INFO.
        The first column is the make and the second column is the model.
        To obtain a list of available lenses, set any values for make and model and leave out the
        lens_model option. The filter will send the full list of lenses in the log with level
        INFO. The ffmpeg tool will exit after the list is printed.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lensfun

        """
        filter_node = FilterNode(
            name="lensfun",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def libplacebo(
        self,
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
                self,
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
        return filter_node._vs(0)

    def libvmaf(
        self,
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
                self,
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
        return filter_node._vs(0)

    def limitdiff(
        self,
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
                self,
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
        return filter_node._vs(0)

    def limiter(self, *, min: int = None, max: int = None, planes: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.148 limiter
        Limits the pixel components values to the specified range [min, max].

        The filter accepts the following options:

        Parameters:
        ----------

        :param int min: Lower bound. Defaults to the lowest allowed value for the input.
        :param int max: Upper bound. Defaults to the highest allowed value for the input.
        :param int planes: Specify which planes will be processed. Defaults to all available.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#limiter

        """
        filter_node = FilterNode(
            name="limiter",
            streams=[
                self,
            ],
            kwargs={
                "min": min,
                "max": max,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def loop(
        self, *, loop: int = None, size: int = None, start: int = None, time: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.149 loop
        Loop video frames.

        The filter accepts the following options:

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
            streams=[
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
        return filter_node._vs(0)

    def lumakey(
        self, *, threshold: float = None, tolerance: float = None, softness: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.152 lumakey
        Turn certain luma values into transparency.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float threshold: Set the luma which will be used as base for transparency. Default value is 0.
        :param float tolerance: Set the range of luma values to be keyed out. Default value is 0.01.
        :param float softness: Set the range of softness. Default value is 0. Use this to control gradual transition from zero to full transparency.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lumakey

        """
        filter_node = FilterNode(
            name="lumakey",
            streams=[
                self,
            ],
            kwargs={
                "threshold": threshold,
                "tolerance": tolerance,
                "softness": softness,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lut(self, *, c0: str = None, c1: str = None, c2: str = None, c3: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.153 lut, lutrgb, lutyuv
        Compute a look-up table for binding each pixel component input value
        to an output value, and apply it to the input video.

        lutyuv applies a lookup table to a YUV input video, lutrgb
        to an RGB input video.

        These filters accept the following parameters:

        Each of them specifies the expression to use for computing the lookup table for
        the corresponding pixel component values.

        The exact component associated to each of the c* options depends on the
        format in input.

        The lut filter requires either YUV or RGB pixel formats in input,
        lutrgb requires RGB pixel formats in input, and lutyuv requires YUV.

        The expressions can contain the following constants and functions:


        All expressions default to "clipval".

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lut",
            streams=[
                self,
            ],
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lut1d(self, *, file: str, interp: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.150 lut1d
        Apply a 1D LUT to an input video.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str file: Set the 1D LUT file name. Currently supported formats: ‘cube’ Iridas ‘csp’ cineSpace
        :param int interp: Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘linear’ Interpolate values using the linear interpolation. ‘cosine’ Interpolate values using the cosine interpolation. ‘cubic’ Interpolate values using the cubic interpolation. ‘spline’ Interpolate values using the spline interpolation.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut1d

        """
        filter_node = FilterNode(
            name="lut1d",
            streams=[
                self,
            ],
            kwargs={
                "file": file,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lut2(
        self,
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
                self,
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
        return filter_node._vs(0)

    def lut3d(self, *, file: str, clut: int = None, interp: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.151 lut3d
        Apply a 3D LUT to an input video.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str file: Set the 3D LUT file name. Currently supported formats: ‘3dl’ AfterEffects ‘cube’ Iridas ‘dat’ DaVinci ‘m3d’ Pandora ‘csp’ cineSpace
        :param int clut: None
        :param int interp: Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘trilinear’ Interpolate values using the 8 points defining a cube. ‘tetrahedral’ Interpolate values using a tetrahedron. ‘pyramid’ Interpolate values using a pyramid. ‘prism’ Interpolate values using a prism.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut3d

        """
        filter_node = FilterNode(
            name="lut3d",
            streams=[
                self,
            ],
            kwargs={
                "file": file,
                "clut": clut,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lutrgb(self, *, c0: str = None, c1: str = None, c2: str = None, c3: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.153 lut, lutrgb, lutyuv
        Compute a look-up table for binding each pixel component input value
        to an output value, and apply it to the input video.

        lutyuv applies a lookup table to a YUV input video, lutrgb
        to an RGB input video.

        These filters accept the following parameters:

        Each of them specifies the expression to use for computing the lookup table for
        the corresponding pixel component values.

        The exact component associated to each of the c* options depends on the
        format in input.

        The lut filter requires either YUV or RGB pixel formats in input,
        lutrgb requires RGB pixel formats in input, and lutyuv requires YUV.

        The expressions can contain the following constants and functions:


        All expressions default to "clipval".

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lutrgb",
            streams=[
                self,
            ],
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def lutyuv(self, *, c0: str = None, c1: str = None, c2: str = None, c3: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.153 lut, lutrgb, lutyuv
        Compute a look-up table for binding each pixel component input value
        to an output value, and apply it to the input video.

        lutyuv applies a lookup table to a YUV input video, lutrgb
        to an RGB input video.

        These filters accept the following parameters:

        Each of them specifies the expression to use for computing the lookup table for
        the corresponding pixel component values.

        The exact component associated to each of the c* options depends on the
        format in input.

        The lut filter requires either YUV or RGB pixel formats in input,
        lutrgb requires RGB pixel formats in input, and lutyuv requires YUV.

        The expressions can contain the following constants and functions:


        All expressions default to "clipval".

        Parameters:
        ----------

        :param str c0: set first pixel component expression
        :param str c1: set second pixel component expression
        :param str c2: set third pixel component expression
        :param str c3: set fourth pixel component expression, corresponds to the alpha component

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        filter_node = FilterNode(
            name="lutyuv",
            streams=[
                self,
            ],
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def maskedclamp(
        self,
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
                self,
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
        return filter_node._vs(0)

    def maskedmax(
        self, _filter1: "VideoStream", _filter2: "VideoStream", *, planes: int = None, **kwargs: Any
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
                self,
                _filter1,
                _filter2,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def maskedmerge(
        self, _overlay: "VideoStream", _mask: "VideoStream", *, planes: int = None, **kwargs: Any
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
                self,
                _overlay,
                _mask,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def maskedmin(
        self, _filter1: "VideoStream", _filter2: "VideoStream", *, planes: int = None, **kwargs: Any
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
                self,
                _filter1,
                _filter2,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def maskedthreshold(
        self, _reference: "VideoStream", *, threshold: int = None, planes: int = None, mode: int = None, **kwargs: Any
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
                self,
                _reference,
            ],
            kwargs={
                "threshold": threshold,
                "planes": planes,
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def maskfun(
        self, *, low: int = None, high: int = None, planes: int = None, fill: int = None, sum: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.160 maskfun
        Create mask from input video.

        For example it is useful to create motion masks after tblend filter.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int low: Set low threshold. Any pixel component lower or exact than this value will be set to 0.
        :param int high: Set high threshold. Any pixel component higher than this value will be set to max value allowed for current pixel format.
        :param int planes: Set planes to filter, by default all available planes are filtered.
        :param int fill: Fill all frame pixels with this value.
        :param int sum: Set max average pixel value for frame. If sum of all pixel components is higher that this average, output frame will be completely filled with value set by fill option. Typically useful for scene changes when used in combination with tblend filter.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskfun

        """
        filter_node = FilterNode(
            name="maskfun",
            streams=[
                self,
            ],
            kwargs={
                "low": low,
                "high": high,
                "planes": planes,
                "fill": fill,
                "sum": sum,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def mcdeint(self, *, mode: int = None, parity: int = None, qp: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.161 mcdeint
        Apply motion-compensation deinterlacing.

        It needs one field per frame as input and must thus be used together
        with yadif=1/3 or equivalent.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Set the deinterlacing mode. It accepts one of the following values: ‘fast’ ‘medium’ ‘slow’ use iterative motion estimation ‘extra_slow’ like ‘slow’, but use multiple reference frames. Default value is ‘fast’.
        :param int parity: Set the picture field parity assumed for the input video. It must be one of the following values: ‘0, tff’ assume top field first ‘1, bff’ assume bottom field first Default value is ‘bff’.
        :param int qp: Set per-block quantization parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcdeint

        """
        filter_node = FilterNode(
            name="mcdeint",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "parity": parity,
                "qp": qp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def median(
        self, *, radius: int = None, planes: int = None, radiusV: int = None, percentile: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.162 median
        Pick median pixel from certain rectangle defined by radius.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int radius: Set horizontal radius size. Default value is 1. Allowed range is integer from 1 to 127.
        :param int planes: Set which planes to process. Default is 15, which is all available planes.
        :param int radiusV: Set vertical radius size. Default value is 0. Allowed range is integer from 0 to 127. If it is 0, value will be picked from horizontal radius option.
        :param float percentile: Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#median

        """
        filter_node = FilterNode(
            name="median",
            streams=[
                self,
            ],
            kwargs={
                "radius": radius,
                "planes": planes,
                "radiusV": radiusV,
                "percentile": percentile,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def mergeplanes(
        self,
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
                self,
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
        return filter_node._vs(0)

    def mestimate(
        self, *, method: int = None, mb_size: int = None, search_param: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.164 mestimate
        Estimate and export motion vectors using block matching algorithms.
        Motion vectors are stored in frame side data to be used by other filters.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int method: Specify the motion estimation method. Accepts one of the following values: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default value is ‘esa’.
        :param int mb_size: Macroblock size. Default 16.
        :param int search_param: Search parameter. Default 7.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mestimate

        """
        filter_node = FilterNode(
            name="mestimate",
            streams=[
                self,
            ],
            kwargs={
                "method": method,
                "mb_size": mb_size,
                "search_param": search_param,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def metadata(
        self,
        *,
        mode: int = None,
        key: str,
        value: str,
        function: int = None,
        expr: str,
        file: str,
        direct: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
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
            name="metadata",
            streams=[
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
        return filter_node._vs(0)

    def midequalizer(self, _in1: "VideoStream", *, planes: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _in1,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def minterpolate(
        self,
        *,
        fps: str = None,
        mi_mode: int = None,
        mc_mode: int = None,
        me_mode: int = None,
        me: int = None,
        mb_size: int = None,
        search_param: int = None,
        vsbmc: int = None,
        scd: int = None,
        scd_threshold: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.166 minterpolate
        Convert the video to specified frame rate using motion interpolation.

        This filter accepts the following options:

        Parameters:
        ----------

        :param str fps: Specify the output frame rate. This can be rational e.g. 60000/1001. Frames are dropped if fps is lower than source fps. Default 60.
        :param int mi_mode: Motion interpolation mode. Following values are accepted: ‘dup’ Duplicate previous or next frame for interpolating new ones. ‘blend’ Blend source frames. Interpolated frame is mean of previous and next frames. ‘mci’ Motion compensated interpolation. Following options are effective when this mode is selected: ‘mc_mode’ Motion compensation mode. Following values are accepted: ‘obmc’ Overlapped block motion compensation. ‘aobmc’ Adaptive overlapped block motion compensation. Window weighting coefficients are controlled adaptively according to the reliabilities of the neighboring motion vectors to reduce oversmoothing. Default mode is ‘obmc’. ‘me_mode’ Motion estimation mode. Following values are accepted: ‘bidir’ Bidirectional motion estimation. Motion vectors are estimated for each source frame in both forward and backward directions. ‘bilat’ Bilateral motion estimation. Motion vectors are estimated directly for interpolated frame. Default mode is ‘bilat’. ‘me’ The algorithm to be used for motion estimation. Following values are accepted: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default algorithm is ‘epzs’. ‘mb_size’ Macroblock size. Default 16. ‘search_param’ Motion estimation search parameter. Default 32. ‘vsbmc’ Enable variable-size block motion compensation. Motion estimation is applied with smaller block sizes at object boundaries in order to make the them less blur. Default is 0 (disabled).
        :param int mc_mode: None
        :param int me_mode: None
        :param int me: None
        :param int mb_size: None
        :param int search_param: None
        :param int vsbmc: None
        :param int scd: Scene change detection method. Scene change leads motion vectors to be in random direction. Scene change detection replace interpolated frames by duplicate ones. May not be needed for other modes. Following values are accepted: ‘none’ Disable scene change detection. ‘fdiff’ Frame difference. Corresponding pixel values are compared and if it satisfies scd_threshold scene change is detected. Default method is ‘fdiff’.
        :param float scd_threshold: Scene change detection threshold. Default is 10..

        Ref: https://ffmpeg.org/ffmpeg-filters.html#minterpolate

        """
        filter_node = FilterNode(
            name="minterpolate",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def mix(
        self,
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
                self,
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
        return filter_node._vs(0)

    def monochrome(
        self, *, cb: float = None, cr: float = None, size: float = None, high: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.168 monochrome
        Convert video to gray using custom color filter.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param float cb: Set the chroma blue spot. Allowed range is from -1 to 1. Default value is 0.
        :param float cr: Set the chroma red spot. Allowed range is from -1 to 1. Default value is 0.
        :param float size: Set the color filter size. Allowed range is from .1 to 10. Default value is 1.
        :param float high: Set the highlights strength. Allowed range is from 0 to 1. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#monochrome

        """
        filter_node = FilterNode(
            name="monochrome",
            streams=[
                self,
            ],
            kwargs={
                "cb": cb,
                "cr": cr,
                "size": size,
                "high": high,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def morpho(
        self, _structure: "VideoStream", *, mode: int = None, planes: int = None, structure: int = None, **kwargs: Any
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
                self,
                _structure,
            ],
            kwargs={
                "mode": mode,
                "planes": planes,
                "structure": structure,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def mpdecimate(
        self, *, max: int = None, keep: int = None, hi: int = None, lo: int = None, frac: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.170 mpdecimate
        Drop frames that do not differ greatly from the previous frame in
        order to reduce frame rate.

        The main use of this filter is for very-low-bitrate encoding
        (e.g. streaming over dialup modem), but it could in theory be used for
        fixing movies that were inverse-telecined incorrectly.

        A description of the accepted options follows.

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
            streams=[
                self,
            ],
            kwargs={
                "max": max,
                "keep": keep,
                "hi": hi,
                "lo": lo,
                "frac": frac,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def msad(self, _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
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
                self,
                _reference,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def multiply(
        self, _factor: "VideoStream", *, scale: float = None, offset: float = None, planes: str = None, **kwargs: Any
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
                self,
                _factor,
            ],
            kwargs={
                "scale": scale,
                "offset": offset,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def negate(self, *, components: str = None, negate_alpha: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.173 negate
        Negate (invert) the input video.

        It accepts the following option:

        Parameters:
        ----------

        :param str components: Set components to negate. Available values for components are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’
        :param bool negate_alpha: With value 1, it negates the alpha component, if present. Default value is 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#negate

        """
        filter_node = FilterNode(
            name="negate",
            streams=[
                self,
            ],
            kwargs={
                "components": components,
                "negate_alpha": negate_alpha,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def nlmeans(
        self, *, s: float = None, p: int = None, pc: int = None, r: int = None, rc: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.174 nlmeans
        Denoise frames using Non-Local Means algorithm.

        Each pixel is adjusted by looking for other pixels with similar contexts. This
        context similarity is defined by comparing their surrounding patches of size
        pxp. Patches are searched in an area of rxr
        around the pixel.

        Note that the research area defines centers for patches, which means some
        patches will be made of pixels outside that research area.

        The filter accepts the following options.

        Parameters:
        ----------

        :param float s: Set denoising strength. Default is 1.0. Must be in range [1.0, 30.0].
        :param int p: Set patch size. Default is 7. Must be odd number in range [0, 99].
        :param int pc: Same as p but for chroma planes. The default value is 0 and means automatic.
        :param int r: Set research size. Default is 15. Must be odd number in range [0, 99].
        :param int rc: Same as r but for chroma planes. The default value is 0 and means automatic.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans

        """
        filter_node = FilterNode(
            name="nlmeans",
            streams=[
                self,
            ],
            kwargs={
                "s": s,
                "p": p,
                "pc": pc,
                "r": r,
                "rc": rc,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def nlmeans_opencl(
        self, *, s: float = None, p: int = None, pc: int = None, r: int = None, rc: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        12.8 nlmeans_opencl
        Non-local Means denoise filter through OpenCL, this filter accepts same options as nlmeans.

        Parameters:
        ----------

        :param float s: None
        :param int p: None
        :param int pc: None
        :param int r: None
        :param int rc: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fopencl

        """
        filter_node = FilterNode(
            name="nlmeans_opencl",
            streams=[
                self,
            ],
            kwargs={
                "s": s,
                "p": p,
                "pc": pc,
                "r": r,
                "rc": rc,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def nlmeans_vulkan(
        self,
        *,
        s: float = None,
        p: int = None,
        r: int = None,
        t: int = None,
        s1: float = None,
        s2: float = None,
        s3: float = None,
        s4: float = None,
        p1: int = None,
        p2: int = None,
        p3: int = None,
        p4: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        14.10 nlmeans_vulkan
        Denoise frames using Non-Local Means algorithm, implemented on the GPU using
        Vulkan.
        Supports more pixel formats than nlmeans or nlmeans_opencl, including
        alpha channel support.

        The filter accepts the following options.

        Parameters:
        ----------

        :param float s: Set denoising strength for all components. Default is 1.0. Must be in range [1.0, 100.0].
        :param int p: Set patch size for all planes. Default is 7. Must be odd number in range [0, 99].
        :param int r: Set research size. Default is 15. Must be odd number in range [0, 99].
        :param int t: Set parallelism. Default is 36. Must be a number in the range [1, 168]. Larger values may speed up processing, at the cost of more VRAM. Lower values will slow it down, reducing VRAM usage. Only supported on GPUs with atomic float operations (RDNA3+, Ampere+).
        :param float s1: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s2: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s3: Set denoising strength for a specific component. Default is 1, equal to s. Must be odd number in range [1, 100].
        :param float s4: None
        :param int p1: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p2: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p3: Set patch size for a specific component. Default is 7, equal to p. Must be odd number in range [0, 99].
        :param int p4: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans_005fvulkan

        """
        filter_node = FilterNode(
            name="nlmeans_vulkan",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def nnedi(
        self,
        *,
        weights: str = None,
        deint: int = None,
        field: int = None,
        planes: int = None,
        nsize: int = None,
        nns: int = None,
        qual: int = None,
        etype: int = None,
        pscrn: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.175 nnedi
        Deinterlace video using neural network edge directed interpolation.

        This filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nnedi

        """
        filter_node = FilterNode(
            name="nnedi",
            streams=[
                self,
            ],
            kwargs={
                "weights": weights,
                "deint": deint,
                "field": field,
                "planes": planes,
                "nsize": nsize,
                "nns": nns,
                "qual": qual,
                "etype": etype,
                "pscrn": pscrn,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def noformat(self, *, pix_fmts: str, **kwargs: Any) -> "VideoStream":
        """

        11.176 noformat
        Force libavfilter not to use any of the specified pixel formats for the
        input to the next filter.

        It accepts the following parameters:

        Parameters:
        ----------

        :param str pix_fmts: A ’|’-separated list of pixel format names, such as pix_fmts=yuv420p|monow|rgb24".

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noformat

        """
        filter_node = FilterNode(
            name="noformat",
            streams=[
                self,
            ],
            kwargs={
                "pix_fmts": pix_fmts,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def noise(
        self,
        *,
        all_seed: int = None,
        all_strength: int = None,
        all_flags: str = None,
        c0_seed: int = None,
        c0_strength: int = None,
        c0_flags: str = None,
        c1_seed: int = None,
        c1_strength: int = None,
        c1_flags: str = None,
        c2_seed: int = None,
        c2_strength: int = None,
        c2_flags: str = None,
        c3_seed: int = None,
        c3_strength: int = None,
        c3_flags: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.177 noise
        Add noise on video input frame.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noise

        """
        filter_node = FilterNode(
            name="noise",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def normalize(
        self,
        *,
        blackpt: str = None,
        whitept: str = None,
        smoothing: int = None,
        independence: float = None,
        strength: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.178 normalize
        Normalize RGB video (aka histogram stretching, contrast stretching).
        See: https://en.wikipedia.org/wiki/Normalization_(image_processing)

        For each channel of each frame, the filter computes the input range and maps
        it linearly to the user-specified output range. The output range defaults
        to the full dynamic range from pure black to pure white.

        Temporal smoothing can be used on the input range to reduce flickering (rapid
        changes in brightness) caused when small dark or bright objects enter or leave
        the scene. This is similar to the auto-exposure (automatic gain control) on a
        video camera, and, like a video camera, it may cause a period of over- or
        under-exposure of the video.

        The R,G,B channels can be normalized independently, which may cause some
        color shifting, or linked together as a single channel, which prevents
        color shifting. Linked normalization preserves hue. Independent normalization
        does not, so it can be used to remove some color casts. Independent and linked
        normalization can be combined in any ratio.

        The normalize filter accepts the following options:

        Parameters:
        ----------

        :param str blackpt: Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        :param str whitept: Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        :param int smoothing: The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).
        :param float independence: Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).
        :param float strength: Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#normalize

        """
        filter_node = FilterNode(
            name="normalize",
            streams=[
                self,
            ],
            kwargs={
                "blackpt": blackpt,
                "whitept": whitept,
                "smoothing": smoothing,
                "independence": independence,
                "strength": strength,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def null(self, **kwargs: Any) -> "VideoStream":
        """

        11.179 null
        Pass the video source unchanged to the output.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#null

        """
        filter_node = FilterNode(
            name="null",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def ocr(
        self, *, datapath: str, language: str = None, whitelist: str = None, blacklist: str = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.180 ocr
        Optical Character Recognition

        This filter uses Tesseract for optical character recognition. To enable
        compilation of this filter, you need to configure FFmpeg with
        --enable-libtesseract.

        It accepts the following options:


        The filter exports recognized text as the frame metadata lavfi.ocr.text.
        The filter exports confidence of recognized words as the frame metadata lavfi.ocr.confidence.

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
            streams=[
                self,
            ],
            kwargs={
                "datapath": datapath,
                "language": language,
                "whitelist": whitelist,
                "blacklist": blacklist,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def ocv(self, *, filter_name: str, filter_params: str, **kwargs: Any) -> "VideoStream":
        """

        11.181 ocv
        Apply a video transform using libopencv.

        To enable this filter, install the libopencv library and headers and
        configure FFmpeg with --enable-libopencv.

        It accepts the following parameters:


        Refer to the official libopencv documentation for more precise
        information:
        http://docs.opencv.org/master/modules/imgproc/doc/filtering.html

        Several libopencv filters are supported; see the following subsections.

        Parameters:
        ----------

        :param str filter_name: The name of the libopencv filter to apply.
        :param str filter_params: The parameters to pass to the libopencv filter. If not specified, the default values are assumed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ocv

        """
        filter_node = FilterNode(
            name="ocv",
            streams=[
                self,
            ],
            kwargs={
                "filter_name": filter_name,
                "filter_params": filter_params,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def oscilloscope(
        self,
        *,
        x: float = None,
        y: float = None,
        s: float = None,
        t: float = None,
        o: float = None,
        tx: float = None,
        ty: float = None,
        tw: float = None,
        th: float = None,
        c: int = None,
        g: bool = None,
        st: bool = None,
        sc: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.182 oscilloscope
        2D Video Oscilloscope.

        Useful to measure spatial impulse, step responses, chroma delays, etc.

        It accepts the following parameters:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#oscilloscope

        """
        filter_node = FilterNode(
            name="oscilloscope",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def overlay(
        self,
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
                self,
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
        return filter_node._vs(0)

    def overlay_cuda(
        self,
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
                self,
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
        return filter_node._vs(0)

    def overlay_opencl(self, _overlay: "VideoStream", *, x: int = None, y: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _overlay,
            ],
            kwargs={
                "x": x,
                "y": y,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def overlay_vaapi(
        self,
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
                self,
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
        return filter_node._vs(0)

    def overlay_vulkan(self, _overlay: "VideoStream", *, x: int = None, y: int = None, **kwargs: Any) -> "VideoStream":
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
                self,
                _overlay,
            ],
            kwargs={
                "x": x,
                "y": y,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def owdenoise(
        self, *, depth: int = None, luma_strength: float = None, chroma_strength: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.185 owdenoise
        Apply Overcomplete Wavelet denoiser.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int depth: Set depth. Larger depth values will denoise lower frequency components more, but slow down filtering. Must be an int in the range 8-16, default is 8.
        :param float luma_strength: Set luma strength. Must be a double value in the range 0-1000, default is 1.0.
        :param float chroma_strength: Set chroma strength. Must be a double value in the range 0-1000, default is 1.0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#owdenoise

        """
        filter_node = FilterNode(
            name="owdenoise",
            streams=[
                self,
            ],
            kwargs={
                "depth": depth,
                "luma_strength": luma_strength,
                "chroma_strength": chroma_strength,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pad(
        self,
        *,
        width: str = None,
        height: str = None,
        x: str = None,
        y: str = None,
        color: str = None,
        eval: int = None,
        aspect: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.186 pad
        Add paddings to the input image, and place the original input at the
        provided x, y coordinates.

        It accepts the following parameters:


        The value for the width, height, x, and y
        options are expressions containing the following constants:

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
            streams=[
                self,
            ],
            kwargs={
                "width": width,
                "height": height,
                "x": x,
                "y": y,
                "color": color,
                "eval": eval,
                "aspect": aspect,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pad_opencl(
        self,
        *,
        width: str = None,
        height: str = None,
        x: str = None,
        y: str = None,
        color: str = None,
        aspect: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        12.10 pad_opencl
        Add paddings to the input image, and place the original input at the
        provided x, y coordinates.

        It accepts the following options:


        The value for the width, height, x, and y
        options are expressions containing the following constants:

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
            streams=[
                self,
            ],
            kwargs={
                "width": width,
                "height": height,
                "x": x,
                "y": y,
                "color": color,
                "aspect": aspect,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def palettegen(
        self,
        *,
        max_colors: int = None,
        reserve_transparent: bool = None,
        transparency_color: str = None,
        stats_mode: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.187 palettegen
        Generate one palette for a whole video stream.

        It accepts the following options:


        The filter also exports the frame metadata lavfi.color_quant_ratio
        (nb_color_in / nb_color_out) which you can use to evaluate the degree of
        color quantization of the palette. This information is also visible at
        info logging level.

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
            streams=[
                self,
            ],
            kwargs={
                "max_colors": max_colors,
                "reserve_transparent": reserve_transparent,
                "transparency_color": transparency_color,
                "stats_mode": stats_mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def paletteuse(
        self,
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
                self,
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
        return filter_node._vs(0)

    def perms(self, *, mode: int = None, seed: int = None, **kwargs: Any) -> "VideoStream":
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
            name="perms",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def perspective(
        self,
        *,
        x0: str = None,
        y0: str = None,
        x1: str = None,
        y1: str = None,
        x2: str = None,
        y2: str = None,
        x3: str = None,
        y3: str = None,
        interpolation: int = None,
        sense: int = None,
        eval: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.189 perspective
        Correct perspective of video not recorded perpendicular to the screen.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param str x0: None
        :param str y0: None
        :param str x1: None
        :param str y1: None
        :param str x2: None
        :param str y2: None
        :param str x3: None
        :param str y3: None
        :param int interpolation: None
        :param int sense: None
        :param int eval: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perspective

        """
        filter_node = FilterNode(
            name="perspective",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def phase(self, *, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.190 phase
        Delay interlaced video by one field time so that the field order changes.

        The intended use is to fix PAL movies that have been captured with the
        opposite field order to the film-to-video transfer.

        A description of the accepted parameters follows.

        Parameters:
        ----------

        :param int mode: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#phase

        """
        filter_node = FilterNode(
            name="phase",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def photosensitivity(
        self, *, frames: int = None, threshold: float = None, skip: int = None, bypass: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.191 photosensitivity
        Reduce various flashes in video, so to help users with epilepsy.

        It accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "frames": frames,
                "threshold": threshold,
                "skip": skip,
                "bypass": bypass,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pixdesctest(self, **kwargs: Any) -> "VideoStream":
        """

        11.192 pixdesctest
        Pixel format descriptor test filter, mainly useful for internal
        testing. The output video should be equal to the input video.

        For example:

        format=monow, pixdesctest

        can be used to test the monowhite pixel format descriptor definition.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixdesctest

        """
        filter_node = FilterNode(
            name="pixdesctest",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def pixelize(
        self, *, width: int = None, height: int = None, mode: int = None, planes: str = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.193 pixelize
        Apply pixelization to video stream.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int width: Set block dimensions that will be used for pixelization. Default value is 16.
        :param int height: Set block dimensions that will be used for pixelization. Default value is 16.
        :param int mode: Set the mode of pixelization used. Possible values are: ‘avg’ ‘min’ ‘max’ Default value is avg.
        :param str planes: Set what planes to filter. Default is to filter all planes.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixelize

        """
        filter_node = FilterNode(
            name="pixelize",
            streams=[
                self,
            ],
            kwargs={
                "width": width,
                "height": height,
                "mode": mode,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pixscope(
        self,
        *,
        x: float = None,
        y: float = None,
        w: int = None,
        h: int = None,
        o: float = None,
        wx: float = None,
        wy: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.194 pixscope
        Display sample values of color channels. Mainly useful for checking color
        and levels. Minimum supported resolution is 640x480.

        The filters accept the following options:

        Parameters:
        ----------

        :param float x: Set scope X position, relative offset on X axis.
        :param float y: Set scope Y position, relative offset on Y axis.
        :param int w: Set scope width.
        :param int h: Set scope height.
        :param float o: Set window opacity. This window also holds statistics about pixel area.
        :param float wx: Set window X position, relative offset on X axis.
        :param float wy: Set window Y position, relative offset on Y axis.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixscope

        """
        filter_node = FilterNode(
            name="pixscope",
            streams=[
                self,
            ],
            kwargs={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "o": o,
                "wx": wx,
                "wy": wy,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pp(self, *, subfilters: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.195 pp
        Enable the specified chain of postprocessing subfilters using libpostproc. This
        library should be automatically selected with a GPL build (--enable-gpl).
        Subfilters must be separated by ’/’ and can be disabled by prepending a ’-’.
        Each subfilter and some options have a short and a long name that can be used
        interchangeably, i.e. dr/dering are the same.

        The filters accept the following options:


        All subfilters share common options to determine their scope:


        These options can be appended after the subfilter name, separated by a ’|’.

        Available subfilters are:


        The horizontal and vertical deblocking filters share the difference and
        flatness values so you cannot set different horizontal and vertical
        thresholds.

        Parameters:
        ----------

        :param str subfilters: Set postprocessing subfilters string.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp

        """
        filter_node = FilterNode(
            name="pp",
            streams=[
                self,
            ],
            kwargs={
                "subfilters": subfilters,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pp7(self, *, qp: int = None, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.196 pp7
        Apply Postprocessing filter 7. It is variant of the spp filter,
        similar to spp = 6 with 7 point DCT, where only the center sample is
        used after IDCT.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int qp: Force a constant quantization parameter. It accepts an integer in range 0 to 63. If not set, the filter will use the QP from the video stream (if available).
        :param int mode: Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding. ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier). ‘medium’ Set medium thresholding (good results, default).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp7

        """
        filter_node = FilterNode(
            name="pp7",
            streams=[
                self,
            ],
            kwargs={
                "qp": qp,
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def premultiply(
        self, *streams: "VideoStream", planes: int = None, inplace: bool = None, **kwargs: Any
    ) -> "VideoStream":
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
                self,
                *streams,
            ],
            kwargs={
                "planes": planes,
                "inplace": inplace,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def prewitt(self, *, planes: int = None, scale: float = None, delta: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.198 prewitt
        Apply prewitt operator to input video stream.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#prewitt

        """
        filter_node = FilterNode(
            name="prewitt",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pseudocolor(
        self,
        *,
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        index: int = None,
        preset: int = None,
        opacity: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.199 pseudocolor
        Alter frame colors in video with pseudocolors.

        This filter accepts the following options:


        Each of the expression options specifies the expression to use for computing
        the lookup table for the corresponding pixel component values.

        The expressions can contain the following constants and functions:


        All expressions default to "val".

        Parameters:
        ----------

        :param str c0: set pixel first component expression
        :param str c1: set pixel second component expression
        :param str c2: set pixel third component expression
        :param str c3: set pixel fourth component expression, corresponds to the alpha component
        :param int index: set component to use as base for altering colors
        :param int preset: Pick one of built-in LUTs. By default is set to none. Available LUTs: ‘magma’ ‘inferno’ ‘plasma’ ‘viridis’ ‘turbo’ ‘cividis’ ‘range1’ ‘range2’ ‘shadows’ ‘highlights’ ‘solar’ ‘nominal’ ‘preferred’ ‘total’ ‘spectral’ ‘cool’ ‘heat’ ‘fiery’ ‘blues’ ‘green’ ‘helix’
        :param float opacity: Set opacity of output colors. Allowed range is from 0 to 1. Default value is set to 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pseudocolor

        """
        filter_node = FilterNode(
            name="pseudocolor",
            streams=[
                self,
            ],
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "index": index,
                "preset": preset,
                "opacity": opacity,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def psnr(
        self,
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
                self,
                _reference,
            ],
            kwargs={
                "stats_file": stats_file,
                "stats_version": stats_version,
                "output_max": output_max,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def pullup(
        self,
        *,
        jl: int = None,
        jr: int = None,
        jt: int = None,
        jb: int = None,
        sb: bool = None,
        mp: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.201 pullup
        Pulldown reversal (inverse telecine) filter, capable of handling mixed
        hard-telecine, 24000/1001 fps progressive, and 30000/1001 fps progressive
        content.

        The pullup filter is designed to take advantage of future context in making
        its decisions. This filter is stateless in the sense that it does not lock
        onto a pattern to follow, but it instead looks forward to the following
        fields in order to identify matches and rebuild progressive frames.

        To produce content with an even framerate, insert the fps filter after
        pullup, use fps=24000/1001 if the input frame rate is 29.97fps,
        fps=24 for 30fps and the (rare) telecined 25fps input.

        The filter accepts the following options:


        For best results (without duplicated frames in the output file) it is
        necessary to change the output frame rate. For example, to inverse
        telecine NTSC input:

        ffmpeg -i input -vf pullup -r 24000/1001 ...

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
            streams=[
                self,
            ],
            kwargs={
                "jl": jl,
                "jr": jr,
                "jt": jt,
                "jb": jb,
                "sb": sb,
                "mp": mp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def qp(self, *, qp: str, **kwargs: Any) -> "VideoStream":
        """

        11.202 qp
        Change video quantization parameters (QP).

        The filter accepts the following option:


        The expression is evaluated through the eval API and can contain, among others,
        the following constants:

        Parameters:
        ----------

        :param str qp: Set expression for quantization parameter.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#qp

        """
        filter_node = FilterNode(
            name="qp",
            streams=[
                self,
            ],
            kwargs={
                "qp": qp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def random(self, *, frames: int = None, seed: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.203 random
        Flush video frames from internal cache of frames into a random order.
        No frame is discarded.
        Inspired by frei0r nervous filter.

        Parameters:
        ----------

        :param int frames: Set size in number of frames of internal cache, in range from 2 to 512. Default is 30.
        :param int seed: Set seed for random number generator, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to less than 0, the filter will try to use a good random seed on a best effort basis.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#random

        """
        filter_node = FilterNode(
            name="random",
            streams=[
                self,
            ],
            kwargs={
                "frames": frames,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def readeia608(
        self,
        *,
        scan_min: int = None,
        scan_max: int = None,
        spw: float = None,
        chp: bool = None,
        lp: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.204 readeia608
        Read closed captioning (EIA-608) information from the top lines of a video frame.

        This filter adds frame metadata for lavfi.readeia608.X.cc and
        lavfi.readeia608.X.line, where X is the number of the identified line
        with EIA-608 data (starting from 0). A description of each metadata value follows:


        This filter accepts the following options:

        Parameters:
        ----------

        :param int scan_min: Set the line to start scanning for EIA-608 data. Default is 0.
        :param int scan_max: Set the line to end scanning for EIA-608 data. Default is 29.
        :param float spw: Set the ratio of width reserved for sync code detection. Default is 0.27. Allowed range is [0.1 - 0.7].
        :param bool chp: Enable checking the parity bit. In the event of a parity error, the filter will output 0x00 for that character. Default is false.
        :param bool lp: Lowpass lines prior to further processing. Default is enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#readeia608

        """
        filter_node = FilterNode(
            name="readeia608",
            streams=[
                self,
            ],
            kwargs={
                "scan_min": scan_min,
                "scan_max": scan_max,
                "spw": spw,
                "chp": chp,
                "lp": lp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def readvitc(
        self, *, scan_max: int = None, thr_b: float = None, thr_w: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.205 readvitc
        Read vertical interval timecode (VITC) information from the top lines of a
        video frame.

        The filter adds frame metadata key lavfi.readvitc.tc_str with the
        timecode value, if a valid timecode has been detected. Further metadata key
        lavfi.readvitc.found is set to 0/1 depending on whether
        timecode data has been found or not.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int scan_max: Set the maximum number of lines to scan for VITC data. If the value is set to -1 the full video frame is scanned. Default is 45.
        :param float thr_b: Set the luma threshold for black. Accepts float numbers in the range [0.0,1.0], default value is 0.2. The value must be equal or less than thr_w.
        :param float thr_w: Set the luma threshold for white. Accepts float numbers in the range [0.0,1.0], default value is 0.6. The value must be equal or greater than thr_b.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#readvitc

        """
        filter_node = FilterNode(
            name="readvitc",
            streams=[
                self,
            ],
            kwargs={
                "scan_max": scan_max,
                "thr_b": thr_b,
                "thr_w": thr_w,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def realtime(self, *, limit: int = None, speed: float = None, **kwargs: Any) -> "VideoStream":
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
            name="realtime",
            streams=[
                self,
            ],
            kwargs={
                "limit": limit,
                "speed": speed,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def remap(
        self, _xmap: "VideoStream", _ymap: "VideoStream", *, format: int = None, fill: str = None, **kwargs: Any
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
                self,
                _xmap,
                _ymap,
            ],
            kwargs={
                "format": format,
                "fill": fill,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def remap_opencl(
        self, _xmap: "VideoStream", _ymap: "VideoStream", *, interp: int = None, fill: str = None, **kwargs: Any
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
                self,
                _xmap,
                _ymap,
            ],
            kwargs={
                "interp": interp,
                "fill": fill,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def removegrain(
        self, *, m0: int = None, m1: int = None, m2: int = None, m3: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.207 removegrain
        The removegrain filter is a spatial denoiser for progressive video.


        Range of mode is from 0 to 24. Description of each mode follows:

        Parameters:
        ----------

        :param int m0: Set mode for the first plane.
        :param int m1: Set mode for the second plane.
        :param int m2: Set mode for the third plane.
        :param int m3: Set mode for the fourth plane.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removegrain

        """
        filter_node = FilterNode(
            name="removegrain",
            streams=[
                self,
            ],
            kwargs={
                "m0": m0,
                "m1": m1,
                "m2": m2,
                "m3": m3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def removelogo(self, *, filename: str, **kwargs: Any) -> "VideoStream":
        """

        11.208 removelogo
        Suppress a TV station logo, using an image file to determine which
        pixels comprise the logo. It works by filling in the pixels that
        comprise the logo with neighboring pixels.

        The filter accepts the following options:


        Pixels in the provided bitmap image with a value of zero are not
        considered part of the logo, non-zero pixels are considered part of
        the logo. If you use white (255) for the logo and black (0) for the
        rest, you will be safe. For making the filter bitmap, it is
        recommended to take a screen capture of a black frame with the logo
        visible, and then using a threshold filter followed by the erode
        filter once or twice.

        If needed, little splotches can be fixed manually. Remember that if
        logo pixels are not covered, the filter quality will be much
        reduced. Marking too many pixels as part of the logo does not hurt as
        much, but it will increase the amount of blurring needed to cover over
        the image and will destroy more information than necessary, and extra
        pixels will slow things down on a large logo.

        Parameters:
        ----------

        :param str filename: Set the filter bitmap file, which can be any image format supported by libavformat. The width and height of the image file must match those of the video stream being processed.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removelogo

        """
        filter_node = FilterNode(
            name="removelogo",
            streams=[
                self,
            ],
            kwargs={
                "filename": filename,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def repeatfields(self, **kwargs: Any) -> "VideoStream":
        """

        11.209 repeatfields
        This filter uses the repeat_field flag from the Video ES headers and hard repeats
        fields based on its value.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#repeatfields

        """
        filter_node = FilterNode(
            name="repeatfields",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def reverse(self, **kwargs: Any) -> "VideoStream":
        """

        11.210 reverse
        Reverse a video clip.

        Warning: This filter requires memory to buffer the entire clip, so trimming
        is suggested.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#reverse

        """
        filter_node = FilterNode(
            name="reverse",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def rgbashift(
        self,
        *,
        rh: int = None,
        rv: int = None,
        gh: int = None,
        gv: int = None,
        bh: int = None,
        bv: int = None,
        ah: int = None,
        av: int = None,
        edge: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.211 rgbashift
        Shift R/G/B/A pixels horizontally and/or vertically.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rgbashift

        """
        filter_node = FilterNode(
            name="rgbashift",
            streams=[
                self,
            ],
            kwargs={
                "rh": rh,
                "rv": rv,
                "gh": gh,
                "gv": gv,
                "bh": bh,
                "bv": bv,
                "ah": ah,
                "av": av,
                "edge": edge,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def roberts(self, *, planes: int = None, scale: float = None, delta: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.212 roberts
        Apply roberts cross operator to input video stream.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#roberts

        """
        filter_node = FilterNode(
            name="roberts",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def rotate(
        self,
        *,
        angle: str = None,
        out_w: str = None,
        out_h: str = None,
        fillcolor: str = None,
        bilinear: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.213 rotate
        Rotate video by an arbitrary angle expressed in radians.

        The filter accepts the following options:

        A description of the optional parameters follows.

        The expressions for the angle and the output size can contain the
        following constants and functions:

        Parameters:
        ----------

        :param str angle: Set an expression for the angle by which to rotate the input video clockwise, expressed as a number of radians. A negative value will result in a counter-clockwise rotation. By default it is set to "0". This expression is evaluated for each frame.
        :param str out_w: Set the output width expression, default value is "iw". This expression is evaluated just once during configuration.
        :param str out_h: Set the output height expression, default value is "ih". This expression is evaluated just once during configuration.
        :param str fillcolor: Set the color used to fill the output area not covered by the rotated image. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".
        :param bool bilinear: Enable bilinear interpolation if set to 1, a value of 0 disables it. Default value is 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rotate

        """
        filter_node = FilterNode(
            name="rotate",
            streams=[
                self,
            ],
            kwargs={
                "angle": angle,
                "out_w": out_w,
                "out_h": out_h,
                "fillcolor": fillcolor,
                "bilinear": bilinear,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sab(
        self,
        *,
        luma_radius: float = None,
        luma_pre_filter_radius: float = None,
        luma_strength: float = None,
        chroma_radius: float = None,
        chroma_pre_filter_radius: float = None,
        chroma_strength: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.214 sab
        Apply Shape Adaptive Blur.

        The filter accepts the following options:


        Each chroma option value, if not explicitly specified, is set to the
        corresponding luma option value.

        Parameters:
        ----------

        :param float luma_radius: Set luma blur filter strength, must be a value in range 0.1-4.0, default value is 1.0. A greater value will result in a more blurred image, and in slower processing.
        :param float luma_pre_filter_radius: Set luma pre-filter radius, must be a value in the 0.1-2.0 range, default value is 1.0.
        :param float luma_strength: Set luma maximum difference between pixels to still be considered, must be a value in the 0.1-100.0 range, default value is 1.0.
        :param float chroma_radius: Set chroma blur filter strength, must be a value in range -0.9-4.0. A greater value will result in a more blurred image, and in slower processing.
        :param float chroma_pre_filter_radius: Set chroma pre-filter radius, must be a value in the -0.9-2.0 range.
        :param float chroma_strength: Set chroma maximum difference between pixels to still be considered, must be a value in the -0.9-100.0 range.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sab

        """
        filter_node = FilterNode(
            name="sab",
            streams=[
                self,
            ],
            kwargs={
                "luma_radius": luma_radius,
                "luma_pre_filter_radius": luma_pre_filter_radius,
                "luma_strength": luma_strength,
                "chroma_radius": chroma_radius,
                "chroma_pre_filter_radius": chroma_pre_filter_radius,
                "chroma_strength": chroma_strength,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def scale(
        self,
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
    ) -> "VideoStream":
        """

        11.215 scale
        Scale (resize) the input video, using the libswscale library.

        The scale filter forces the output display aspect ratio to be the same
        of the input, by changing the output sample aspect ratio.

        If the input image format is different from the format requested by
        the next filter, the scale filter will convert the input to the
        requested format.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale

        """
        filter_node = FilterNode(
            name="scale",
            streams=[
                self,
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
        return filter_node._vs(0)

    def scale2ref(
        self,
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
                self,
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
            filter_node._vs(0),
            filter_node._vs(1),
        )

    def scale2ref_npp(
        self,
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
                self,
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
            filter_node._vs(0),
            filter_node._vs(1),
        )

    def scale_cuda(
        self,
        *,
        w: str = None,
        h: str = None,
        interp_algo: int = None,
        format: str = None,
        passthrough: bool = None,
        param: float = None,
        force_original_aspect_ratio: int = None,
        force_divisible_by: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.216 scale_cuda
        Scale (resize) and convert (pixel format) the input video, using accelerated CUDA kernels.
        Setting the output width and height works in the same way as for the scale filter.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "w": w,
                "h": h,
                "interp_algo": interp_algo,
                "format": format,
                "passthrough": passthrough,
                "param": param,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def scale_npp(
        self,
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
    ) -> "VideoStream":
        """

        11.217 scale_npp
        Use the NVIDIA Performance Primitives (libnpp) to perform scaling and/or pixel
        format conversion on CUDA video frames. Setting the output width and height
        works in the same way as for the scale filter.

        The following additional options are accepted:

        The values of the w and h options are expressions
        containing the following constants:

        Parameters:
        ----------

        :param str w: None
        :param str h: None
        :param str format: The pixel format of the output CUDA frames. If set to the string "same" (the default), the input format will be kept. Note that automatic format negotiation and conversion is not yet supported for hardware frames
        :param str s: None
        :param int interp_algo: The interpolation algorithm used for resizing. One of the following: nn Nearest neighbour. linear cubic cubic2p_bspline 2-parameter cubic (B=1, C=0) cubic2p_catmullrom 2-parameter cubic (B=0, C=1/2) cubic2p_b05c03 2-parameter cubic (B=1/2, C=3/10) super Supersampling lanczos
        :param int force_original_aspect_ratio: Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio. Possible values: ‘disable’ Scale the video as specified and disable this feature. ‘decrease’ The output video dimensions will automatically be decreased if needed. ‘increase’ The output video dimensions will automatically be increased if needed. One useful instance of this option is that when you know a specific device’s maximum allowed resolution, you can use this to limit the output video to that, while retaining the aspect ratio. For example, device A allows 1280x720 playback, and your video is 1920x800. Using this option (set it to decrease) and specifying 1280x720 to the command line makes the output 1280x533. Please note that this is a different thing than specifying -1 for w or h, you still need to specify the output resolution for this option to work.
        :param int force_divisible_by: Ensures that both the output dimensions, width and height, are divisible by the given integer when used together with force_original_aspect_ratio. This works similar to using -n in the w and h options. This option respects the value set for force_original_aspect_ratio, increasing or decreasing the resolution accordingly. The video’s aspect ratio may be slightly modified. This option can be handy if you need to have a video fit within or exceed a defined resolution using force_original_aspect_ratio but also have encoder restrictions on width or height divisibility.
        :param int eval: Specify when to evaluate width and height expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fnpp

        """
        filter_node = FilterNode(
            name="scale_npp",
            streams=[
                self,
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
        return filter_node._vs(0)

    def scale_vt(
        self,
        *,
        w: str = None,
        h: str = None,
        color_matrix: str,
        color_primaries: str,
        color_transfer: str,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.220 scale_vt
        Scale and convert the color parameters using VTPixelTransferSession.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "w": w,
                "h": h,
                "color_matrix": color_matrix,
                "color_primaries": color_primaries,
                "color_transfer": color_transfer,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def scdet(self, *, threshold: float = None, sc_pass: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.223 scdet
        Detect video scene change.

        This filter sets frame metadata with mafd between frame, the scene score, and
        forward the frame to the next filter, so they can use these metadata to detect
        scene change or others.

        In addition, this filter logs a message and sets frame metadata when it detects
        a scene change by threshold.

        lavfi.scd.mafd metadata keys are set with mafd for every frame.

        lavfi.scd.score metadata keys are set with scene change score for every frame
        to detect scene change.

        lavfi.scd.time metadata keys are set with current filtered frame time which
        detect scene change with threshold.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float threshold: Set the scene change detection threshold as a percentage of maximum change. Good values are in the [8.0, 14.0] range. The range for threshold is [0., 100.]. Default value is 10..
        :param bool sc_pass: Set the flag to pass scene change frames to the next filter. Default value is 0 You can enable it if you want to get snapshot of scene change frames only.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scdet

        """
        filter_node = FilterNode(
            name="scdet",
            streams=[
                self,
            ],
            kwargs={
                "threshold": threshold,
                "sc_pass": sc_pass,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def scharr(self, *, planes: int = None, scale: float = None, delta: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.221 scharr
        Apply scharr operator to input video stream.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scharr

        """
        filter_node = FilterNode(
            name="scharr",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def scroll(
        self, *, horizontal: float = None, vertical: float = None, hpos: float = None, vpos: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.222 scroll
        Scroll input video horizontally and/or vertically by constant speed.

        The filter accepts the following options:

        Parameters:
        ----------

        :param float horizontal: Set the horizontal scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        :param float vertical: Set the vertical scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        :param float hpos: Set the initial horizontal scrolling position. Default is 0. Allowed range is from 0 to 1.
        :param float vpos: Set the initial vertical scrolling position. Default is 0. Allowed range is from 0 to 1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scroll

        """
        filter_node = FilterNode(
            name="scroll",
            streams=[
                self,
            ],
            kwargs={
                "horizontal": horizontal,
                "vertical": vertical,
                "hpos": hpos,
                "vpos": vpos,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def segment(self, *, timestamps: str, frames: str, **kwargs: Any) -> FilterNode:
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
        :param str frames: Exact frame/sample count to split the segments.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment

        """
        filter_node = FilterNode(
            name="segment",
            streams=[
                self,
            ],
            kwargs={
                "timestamps": timestamps,
                "frames": frames,
            }
            | kwargs,
        )

        return filter_node

    def select(self, *, expr: str = None, outputs: int = None, **kwargs: Any) -> FilterNode:
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
            name="select",
            streams=[
                self,
            ],
            kwargs={
                "expr": expr,
                "outputs": outputs,
            }
            | kwargs,
        )

        return filter_node

    def selectivecolor(
        self,
        *,
        correction_method: int = None,
        reds: str,
        yellows: str,
        greens: str,
        cyans: str,
        blues: str,
        magentas: str,
        whites: str,
        neutrals: str,
        blacks: str,
        psfile: str,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.224 selectivecolor
        Adjust cyan, magenta, yellow and black (CMYK) to certain ranges of colors (such
        as "reds", "yellows", "greens", "cyans", ...). The adjustment range is defined
        by the "purity" of the color (that is, how saturated it already is).

        This filter is similar to the Adobe Photoshop Selective Color tool.

        The filter accepts the following options:


        All the adjustment settings (reds, yellows, ...) accept up to
        4 space separated floating point adjustment values in the [-1,1] range,
        respectively to adjust the amount of cyan, magenta, yellow and black for the
        pixels of its range.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#selectivecolor

        """
        filter_node = FilterNode(
            name="selectivecolor",
            streams=[
                self,
            ],
            kwargs={
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
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sendcmd(self, *, commands: str, filename: str, **kwargs: Any) -> "VideoStream":
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
            name="sendcmd",
            streams=[
                self,
            ],
            kwargs={
                "commands": commands,
                "filename": filename,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def separatefields(self, **kwargs: Any) -> "VideoStream":
        """

        11.225 separatefields
        The separatefields takes a frame-based video input and splits
        each frame into its components fields, producing a new half height clip
        with twice the frame rate and twice the frame count.

        This filter use field-dominance information in frame to decide which
        of each pair of fields to place first in the output.
        If it gets it wrong use setfield filter before separatefields filter.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#separatefields

        """
        filter_node = FilterNode(
            name="separatefields",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def setdar(self, *, dar: str = None, max: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.226 setdar, setsar
        The setdar filter sets the Display Aspect Ratio for the filter
        output video.

        This is done by changing the specified Sample (aka Pixel) Aspect
        Ratio, according to the following equation:

        DAR = HORIZONTAL_RESOLUTION / VERTICAL_RESOLUTION * SAR

        Keep in mind that the setdar filter does not modify the pixel
        dimensions of the video frame. Also, the display aspect ratio set by
        this filter may be changed by later filters in the filterchain,
        e.g. in case of scaling or if another "setdar" or a "setsar" filter is
        applied.

        The setsar filter sets the Sample (aka Pixel) Aspect Ratio for
        the filter output video.

        Note that as a consequence of the application of this filter, the
        output display aspect ratio will change according to the equation
        above.

        Keep in mind that the sample aspect ratio set by the setsar
        filter may be changed by later filters in the filterchain, e.g. if
        another "setsar" or a "setdar" filter is applied.

        It accepts the following parameters:


        The parameter sar is an expression containing the following constants:

        Parameters:
        ----------

        :param str dar: Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        :param int max: Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        filter_node = FilterNode(
            name="setdar",
            streams=[
                self,
            ],
            kwargs={
                "dar": dar,
                "max": max,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def setfield(self, *, mode: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.227 setfield
        Force field for the output video frame.

        The setfield filter marks the interlace type field for the
        output frames. It does not change the input frame, but only sets the
        corresponding property, which affects how the frame is treated by
        following filters (e.g. fieldorder or yadif).

        The filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Available values are: ‘auto’ Keep the same field property. ‘bff’ Mark the frame as bottom-field-first. ‘tff’ Mark the frame as top-field-first. ‘prog’ Mark the frame as progressive.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setfield

        """
        filter_node = FilterNode(
            name="setfield",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def setparams(
        self,
        *,
        field_mode: int = None,
        range: int = None,
        color_primaries: int = None,
        color_trc: int = None,
        colorspace: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.228 setparams
        Force frame parameter for the output video frame.

        The setparams filter marks interlace and color range for the
        output frames. It does not change the input frame, but only sets the
        corresponding property, which affects how the frame is treated by
        filters/encoders.

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
            streams=[
                self,
            ],
            kwargs={
                "field_mode": field_mode,
                "range": range,
                "color_primaries": color_primaries,
                "color_trc": color_trc,
                "colorspace": colorspace,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def setpts(self, *, expr: str = None, **kwargs: Any) -> "VideoStream":
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
            name="setpts",
            streams=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def setrange(self, *, range: int = None, **kwargs: Any) -> "VideoStream":
        """

        18.20 setrange
        Force color range for the output video frame.

        The setrange filter marks the color range property for the
        output frames. It does not change the input frame, but only sets the
        corresponding property, which affects how the frame is treated by
        following filters.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int range: Available values are: ‘auto’ Keep the same color range property. ‘unspecified, unknown’ Set the color range as unspecified. ‘limited, tv, mpeg’ Set the color range as limited. ‘full, pc, jpeg’ Set the color range as full.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setrange

        """
        filter_node = FilterNode(
            name="setrange",
            streams=[
                self,
            ],
            kwargs={
                "range": range,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def setsar(self, *, sar: str = None, max: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.226 setdar, setsar
        The setdar filter sets the Display Aspect Ratio for the filter
        output video.

        This is done by changing the specified Sample (aka Pixel) Aspect
        Ratio, according to the following equation:

        DAR = HORIZONTAL_RESOLUTION / VERTICAL_RESOLUTION * SAR

        Keep in mind that the setdar filter does not modify the pixel
        dimensions of the video frame. Also, the display aspect ratio set by
        this filter may be changed by later filters in the filterchain,
        e.g. in case of scaling or if another "setdar" or a "setsar" filter is
        applied.

        The setsar filter sets the Sample (aka Pixel) Aspect Ratio for
        the filter output video.

        Note that as a consequence of the application of this filter, the
        output display aspect ratio will change according to the equation
        above.

        Keep in mind that the sample aspect ratio set by the setsar
        filter may be changed by later filters in the filterchain, e.g. if
        another "setsar" or a "setdar" filter is applied.

        It accepts the following parameters:


        The parameter sar is an expression containing the following constants:

        Parameters:
        ----------

        :param str sar: Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        :param int max: Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        filter_node = FilterNode(
            name="setsar",
            streams=[
                self,
            ],
            kwargs={
                "sar": sar,
                "max": max,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def settb(self, *, expr: str = None, **kwargs: Any) -> "VideoStream":
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
            name="settb",
            streams=[
                self,
            ],
            kwargs={
                "expr": expr,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sharpen_npp(self, *, border_type: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.229 sharpen_npp
        Use the NVIDIA Performance Primitives (libnpp) to perform image sharpening with
        border control.

        The following additional options are accepted:

        Parameters:
        ----------

        :param int border_type: Type of sampling to be used ad frame borders. One of the following: replicate Replicate pixel values.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sharpen_005fnpp

        """
        filter_node = FilterNode(
            name="sharpen_npp",
            streams=[
                self,
            ],
            kwargs={
                "border_type": border_type,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def shear(
        self, *, shx: float = None, shy: float = None, fillcolor: str = None, interp: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.230 shear
        Apply shear transform to input video.

        This filter supports the following options:

        Parameters:
        ----------

        :param float shx: Shear factor in X-direction. Default value is 0. Allowed range is from -2 to 2.
        :param float shy: Shear factor in Y-direction. Default value is 0. Allowed range is from -2 to 2.
        :param str fillcolor: Set the color used to fill the output area not covered by the transformed video. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".
        :param int interp: Set interpolation type. Can be bilinear or nearest. Default is bilinear.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shear

        """
        filter_node = FilterNode(
            name="shear",
            streams=[
                self,
            ],
            kwargs={
                "shx": shx,
                "shy": shy,
                "fillcolor": fillcolor,
                "interp": interp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def showinfo(self, *, checksum: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.231 showinfo
        Show a line containing various information for each input video frame.
        The input video is not modified.

        This filter supports the following options:


        The shown line contains a sequence of key/value pairs of the form
        key:value.

        The following values are shown in the output:

        Parameters:
        ----------

        :param bool checksum: Calculate checksums of each plane. By default enabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showinfo

        """
        filter_node = FilterNode(
            name="showinfo",
            streams=[
                self,
            ],
            kwargs={
                "checksum": checksum,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def showpalette(self, *, s: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.232 showpalette
        Displays the 256 colors palette of each frame. This filter is only relevant for
        pal8 pixel format frames.

        It accepts the following option:

        Parameters:
        ----------

        :param int s: Set the size of the box used to represent one palette color entry. Default is 30 (for a 30x30 pixel box).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showpalette

        """
        filter_node = FilterNode(
            name="showpalette",
            streams=[
                self,
            ],
            kwargs={
                "s": s,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def shuffleframes(self, *, mapping: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.233 shuffleframes
        Reorder and/or duplicate and/or drop video frames.

        It accepts the following parameters:


        The first frame has the index 0. The default is to keep the input unchanged.

        Parameters:
        ----------

        :param str mapping: Set the destination indexes of input frames. This is space or ’|’ separated list of indexes that maps input frames to output frames. Number of indexes also sets maximal value that each index may have. ’-1’ index have special meaning and that is to drop frame.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleframes

        """
        filter_node = FilterNode(
            name="shuffleframes",
            streams=[
                self,
            ],
            kwargs={
                "mapping": mapping,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def shufflepixels(
        self,
        *,
        direction: int = None,
        mode: int = None,
        width: int = None,
        height: int = None,
        seed: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.234 shufflepixels
        Reorder pixels in video frames.

        This filter accepts the following options:

        Parameters:
        ----------

        :param int direction: Set shuffle direction. Can be forward or inverse direction. Default direction is forward.
        :param int mode: Set shuffle mode. Can be horizontal, vertical or block mode.
        :param int width: Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        :param int height: Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        :param int seed: Set random seed used with shuffling pixels. Mainly useful to set to be able to reverse filtering process to get original input. For example, to reverse forward shuffle you need to use same parameters and exact same seed and to set direction to inverse.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shufflepixels

        """
        filter_node = FilterNode(
            name="shufflepixels",
            streams=[
                self,
            ],
            kwargs={
                "direction": direction,
                "mode": mode,
                "width": width,
                "height": height,
                "seed": seed,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def shuffleplanes(
        self, *, map0: int = None, map1: int = None, map2: int = None, map3: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.235 shuffleplanes
        Reorder and/or duplicate video planes.

        It accepts the following parameters:


        The first plane has the index 0. The default is to keep the input unchanged.

        Parameters:
        ----------

        :param int map0: The index of the input plane to be used as the first output plane.
        :param int map1: The index of the input plane to be used as the second output plane.
        :param int map2: The index of the input plane to be used as the third output plane.
        :param int map3: The index of the input plane to be used as the fourth output plane.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleplanes

        """
        filter_node = FilterNode(
            name="shuffleplanes",
            streams=[
                self,
            ],
            kwargs={
                "map0": map0,
                "map1": map1,
                "map2": map2,
                "map3": map3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sidedata(self, *, mode: int = None, type: int = None, **kwargs: Any) -> "VideoStream":
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
            name="sidedata",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "type": type,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def signalstats(self, *, stat: str = None, out: int = None, c: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.236 signalstats
        Evaluate various visual metrics that assist in determining issues associated
        with the digitization of analog video media.

        By default the filter will log these metadata values:


        The filter accepts the following options:

        Parameters:
        ----------

        :param str stat: stat specify an additional form of image analysis. out output video with the specified type of pixel highlighted. Both options accept the following values: ‘tout’ Identify temporal outliers pixels. A temporal outlier is a pixel unlike the neighboring pixels of the same field. Examples of temporal outliers include the results of video dropouts, head clogs, or tape tracking issues. ‘vrep’ Identify vertical line repetition. Vertical line repetition includes similar rows of pixels within a frame. In born-digital video vertical line repetition is common, but this pattern is uncommon in video digitized from an analog source. When it occurs in video that results from the digitization of an analog source it can indicate concealment from a dropout compensator. ‘brng’ Identify pixels that fall outside of legal broadcast range.
        :param int out: stat specify an additional form of image analysis. out output video with the specified type of pixel highlighted. Both options accept the following values: ‘tout’ Identify temporal outliers pixels. A temporal outlier is a pixel unlike the neighboring pixels of the same field. Examples of temporal outliers include the results of video dropouts, head clogs, or tape tracking issues. ‘vrep’ Identify vertical line repetition. Vertical line repetition includes similar rows of pixels within a frame. In born-digital video vertical line repetition is common, but this pattern is uncommon in video digitized from an analog source. When it occurs in video that results from the digitization of an analog source it can indicate concealment from a dropout compensator. ‘brng’ Identify pixels that fall outside of legal broadcast range.
        :param str c: Set the highlight color for the out option. The default color is yellow.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#signalstats

        """
        filter_node = FilterNode(
            name="signalstats",
            streams=[
                self,
            ],
            kwargs={
                "stat": stat,
                "out": out,
                "c": c,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def signature(
        self,
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
                self,
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
        return filter_node._vs(0)

    def siti(self, *, print_summary: bool = None, **kwargs: Any) -> "VideoStream":
        """

        11.238 siti
        Calculate Spatial Information (SI) and Temporal Information (TI) scores for a video,
        as defined in ITU-T Rec. P.910 (11/21): Subjective video quality assessment methods
        for multimedia applications. Available PDF at https://www.itu.int/rec/T-REC-P.910-202111-S/en.
        Note that this is a legacy implementation that corresponds to a superseded recommendation.
        Refer to ITU-T Rec. P.910 (07/22) for the latest version: https://www.itu.int/rec/T-REC-P.910-202207-I/en

        It accepts the following option:

        Parameters:
        ----------

        :param bool print_summary: If set to 1, Summary statistics will be printed to the console. Default 0.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#siti

        """
        filter_node = FilterNode(
            name="siti",
            streams=[
                self,
            ],
            kwargs={
                "print_summary": print_summary,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def smartblur(
        self,
        *,
        luma_radius: float = None,
        luma_strength: float = None,
        luma_threshold: int = None,
        chroma_radius: float = None,
        chroma_strength: float = None,
        chroma_threshold: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.239 smartblur
        Blur the input video without impacting the outlines.

        It accepts the following options:


        If a chroma option is not explicitly set, the corresponding luma value
        is set.

        Parameters:
        ----------

        :param float luma_radius: Set the luma radius. The option value must be a float number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is 1.0.
        :param float luma_strength: Set the luma strength. The option value must be a float number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is 1.0.
        :param int luma_threshold: Set the luma threshold used as a coefficient to determine whether a pixel should be blurred or not. The option value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is 0.
        :param float chroma_radius: Set the chroma radius. The option value must be a float number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is luma_radius.
        :param float chroma_strength: Set the chroma strength. The option value must be a float number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is luma_strength.
        :param int chroma_threshold: Set the chroma threshold used as a coefficient to determine whether a pixel should be blurred or not. The option value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is luma_threshold.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#smartblur

        """
        filter_node = FilterNode(
            name="smartblur",
            streams=[
                self,
            ],
            kwargs={
                "luma_radius": luma_radius,
                "luma_strength": luma_strength,
                "luma_threshold": luma_threshold,
                "chroma_radius": chroma_radius,
                "chroma_strength": chroma_strength,
                "chroma_threshold": chroma_threshold,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sobel(self, *, planes: int = None, scale: float = None, delta: float = None, **kwargs: Any) -> "VideoStream":
        """

        11.240 sobel
        Apply sobel operator to input video stream.

        The filter accepts the following option:

        Parameters:
        ----------

        :param int planes: Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        :param float scale: Set value which will be multiplied with filtered result.
        :param float delta: Set value which will be added to filtered result.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sobel

        """
        filter_node = FilterNode(
            name="sobel",
            streams=[
                self,
            ],
            kwargs={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def spectrumsynth(
        self,
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
                self,
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
        return filter_node._as(0)

    def split(self, *, outputs: int = None, **kwargs: Any) -> FilterNode:
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
            name="split",
            streams=[
                self,
            ],
            kwargs={
                "outputs": outputs,
            }
            | kwargs,
        )

        return filter_node

    def spp(
        self, *, quality: int = None, qp: int = None, mode: int = None, use_bframe_qp: bool = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.241 spp
        Apply a simple postprocessing filter that compresses and decompresses the image
        at several (or - in the case of quality level 6 - all) shifts
        and average the results.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-6. If set to 0, the filter will have no effect. A value of 6 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        :param int qp: Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        :param int mode: Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding (default). ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier).
        :param bool use_bframe_qp: Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#spp

        """
        filter_node = FilterNode(
            name="spp",
            streams=[
                self,
            ],
            kwargs={
                "quality": quality,
                "qp": qp,
                "mode": mode,
                "use_bframe_qp": use_bframe_qp,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def sr(
        self,
        *,
        dnn_backend: int = None,
        scale_factor: int = None,
        model: str,
        input: str = None,
        output: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.242 sr
        Scale the input by applying one of the super-resolution methods based on
        convolutional neural networks. Supported models:


         Super-Resolution Convolutional Neural Network model (SRCNN).
        See https://arxiv.org/abs/1501.00092.

         Efficient Sub-Pixel Convolutional Neural Network model (ESPCN).
        See https://arxiv.org/abs/1609.05158.

        Training scripts as well as scripts for model file (.pb) saving can be found at
        https://github.com/XueweiMeng/sr/tree/sr_dnn_native. Original repository
        is at https://github.com/HighVoltageRocknRoll/sr.git.

        The filter accepts the following options:


        To get full functionality (such as async execution), please use the dnn_processing filter.

        Parameters:
        ----------

        :param int dnn_backend: Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        :param int scale_factor: Set scale factor for SRCNN model. Allowed values are 2, 3 and 4. Default value is 2. Scale factor is necessary for SRCNN model, because it accepts input upscaled using bicubic upscaling with proper scale factor.
        :param str model: Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        :param str input: None
        :param str output: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sr

        """
        filter_node = FilterNode(
            name="sr",
            streams=[
                self,
            ],
            kwargs={
                "dnn_backend": dnn_backend,
                "scale_factor": scale_factor,
                "model": model,
                "input": input,
                "output": output,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def ssim(self, _reference: "VideoStream", *, stats_file: str, **kwargs: Any) -> "VideoStream":
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
                self,
                _reference,
            ],
            kwargs={
                "stats_file": stats_file,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def stereo3d(self, *, _in: int = None, out: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.244 stereo3d
        Convert between different stereoscopic image formats.

        The filters accept the following options:

        Parameters:
        ----------

        :param int _in: Set stereoscopic image format of input. Available values for input image formats are: ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first Default value is ‘sbsl’.
        :param int out: Set stereoscopic image format of output. ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘arbg’ anaglyph red/blue gray (red filter on left eye, blue filter on right eye) ‘argg’ anaglyph red/green gray (red filter on left eye, green filter on right eye) ‘arcg’ anaglyph red/cyan gray (red filter on left eye, cyan filter on right eye) ‘arch’ anaglyph red/cyan half colored (red filter on left eye, cyan filter on right eye) ‘arcc’ anaglyph red/cyan color (red filter on left eye, cyan filter on right eye) ‘arcd’ anaglyph red/cyan color optimized with the least squares projection of dubois (red filter on left eye, cyan filter on right eye) ‘agmg’ anaglyph green/magenta gray (green filter on left eye, magenta filter on right eye) ‘agmh’ anaglyph green/magenta half colored (green filter on left eye, magenta filter on right eye) ‘agmc’ anaglyph green/magenta colored (green filter on left eye, magenta filter on right eye) ‘agmd’ anaglyph green/magenta color optimized with the least squares projection of dubois (green filter on left eye, magenta filter on right eye) ‘aybg’ anaglyph yellow/blue gray (yellow filter on left eye, blue filter on right eye) ‘aybh’ anaglyph yellow/blue half colored (yellow filter on left eye, blue filter on right eye) ‘aybc’ anaglyph yellow/blue colored (yellow filter on left eye, blue filter on right eye) ‘aybd’ anaglyph yellow/blue color optimized with the least squares projection of dubois (yellow filter on left eye, blue filter on right eye) ‘ml’ mono output (left eye only) ‘mr’ mono output (right eye only) ‘chl’ checkerboard, left eye first ‘chr’ checkerboard, right eye first ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first ‘hdmi’ HDMI frame pack Default value is ‘arcd’.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereo3d

        """
        filter_node = FilterNode(
            name="stereo3d",
            streams=[
                self,
            ],
            kwargs={
                "in": _in,
                "out": out,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def streamselect(self, *streams: "VideoStream", inputs: int = None, map: str, **kwargs: Any) -> FilterNode:
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "map": map,
            }
            | kwargs,
        )

        return filter_node

    def super2xsai(self, **kwargs: Any) -> "VideoStream":
        """

        11.247 super2xsai
        Scale the input by 2x and smooth using the Super2xSaI (Scale and
        Interpolate) pixel art scaling algorithm.

        Useful for enlarging pixel art images without reducing sharpness.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#super2xsai

        """
        filter_node = FilterNode(
            name="super2xsai",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def swaprect(
        self,
        *,
        w: str = None,
        h: str = None,
        x1: str = None,
        y1: str = None,
        x2: str = None,
        y2: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.248 swaprect
        Swap two rectangular objects in video.

        This filter accepts the following options:


        The all options are expressions containing the following constants:

        Parameters:
        ----------

        :param str w: Set object width.
        :param str h: Set object height.
        :param str x1: Set 1st rect x coordinate.
        :param str y1: Set 1st rect y coordinate.
        :param str x2: Set 2nd rect x coordinate.
        :param str y2: Set 2nd rect y coordinate. All expressions are evaluated once for each frame.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#swaprect

        """
        filter_node = FilterNode(
            name="swaprect",
            streams=[
                self,
            ],
            kwargs={
                "w": w,
                "h": h,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def swapuv(self, **kwargs: Any) -> "VideoStream":
        """

        11.249 swapuv
        Swap U & V plane.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#swapuv

        """
        filter_node = FilterNode(
            name="swapuv",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def tblend(
        self,
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

        11.250 tblend
        Blend successive video frames.

        See blend

        Parameters:
        ----------

        :param int c0_mode: None
        :param int c1_mode: None
        :param int c2_mode: None
        :param int c3_mode: None
        :param int all_mode: None
        :param str c0_expr: None
        :param str c1_expr: None
        :param str c2_expr: None
        :param str c3_expr: None
        :param str all_expr: None
        :param float c0_opacity: None
        :param float c1_opacity: None
        :param float c2_opacity: None
        :param float c3_opacity: None
        :param float all_opacity: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tblend

        """
        filter_node = FilterNode(
            name="tblend",
            streams=[
                self,
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
        return filter_node._vs(0)

    def telecine(self, *, first_field: int = None, pattern: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.251 telecine
        Apply telecine process to the video.

        This filter accepts the following options:



        Some typical patterns:

        NTSC output (30i):
        27.5p: 32222
        24p: 23 (classic)
        24p: 2332 (preferred)
        20p: 33
        18p: 334
        16p: 3444

        PAL output (25i):
        27.5p: 12222
        24p: 222222222223 ("Euro pulldown")
        16.67p: 33
        16p: 33333334

        Parameters:
        ----------

        :param int first_field: ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        :param str pattern: A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#telecine

        """
        filter_node = FilterNode(
            name="telecine",
            streams=[
                self,
            ],
            kwargs={
                "first_field": first_field,
                "pattern": pattern,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def thistogram(
        self,
        *,
        width: int = None,
        display_mode: int = None,
        levels_mode: int = None,
        components: int = None,
        bgopacity: float = None,
        envelope: bool = None,
        ecolor: str = None,
        slide: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.252 thistogram
        Compute and draw a color distribution histogram for the input video across time.

        Unlike histogram video filter which only shows histogram of single input frame
        at certain time, this filter shows also past histograms of number of frames defined
        by width option.

        The computed histogram is a representation of the color component
        distribution in an image.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "width": width,
                "display_mode": display_mode,
                "levels_mode": levels_mode,
                "components": components,
                "bgopacity": bgopacity,
                "envelope": envelope,
                "ecolor": ecolor,
                "slide": slide,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def threshold(
        self, _threshold: "VideoStream", _min: "VideoStream", _max: "VideoStream", *, planes: int = None, **kwargs: Any
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
                self,
                _threshold,
                _min,
                _max,
            ],
            kwargs={
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def thumbnail(self, *, n: int = None, log: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.254 thumbnail
        Select the most representative frame in a given sequence of consecutive frames.

        The filter accepts the following options:


        Since the filter keeps track of the whole frames sequence, a bigger n
        value will result in a higher memory usage, so a high value is not recommended.

        Parameters:
        ----------

        :param int n: Set the frames batch size to analyze; in a set of n frames, the filter will pick one of them, and then handle the next batch of n frames until the end. Default is 100.
        :param int log: Set the log level to display picked frame stats. Default is info.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#thumbnail

        """
        filter_node = FilterNode(
            name="thumbnail",
            streams=[
                self,
            ],
            kwargs={
                "n": n,
                "log": log,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tile(
        self,
        *,
        layout: str = None,
        nb_frames: int = None,
        margin: int = None,
        padding: int = None,
        color: str = None,
        overlap: int = None,
        init_padding: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.255 tile
        Tile several successive frames together.

        The untile filter can do the reverse.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "layout": layout,
                "nb_frames": nb_frames,
                "margin": margin,
                "padding": padding,
                "color": color,
                "overlap": overlap,
                "init_padding": init_padding,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tiltandshift(
        self, *, tilt: int = None, start: int = None, end: int = None, hold: int = None, pad: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.256 tiltandshift
        What happens when you invert time and space?

        Normally a video is composed of several frames that represent a different
        instant of time and shows a scence that evolves in the space captured by the
        frame. This filter is the antipode of that concept, taking inspiration by
        tilt and shift photography.

        A filtered frame contains the whole timeline of events composing the sequence,
        and this is obtained by placing a slice of pixels from each frame into a single
        one. However, since there are no infinite-width frames, this is done up the
        width of the input frame, and a video is recomposed by shifting away one
        column for each subsequent frame. In order to map space to time, the filter
        tilts each input frame as well, so that motion is preseved. This is accomplished
        by progressively selecting a different column from each input frame.

        The end result is a sort of inverted parralax, so that far away objects move
        much faster that the ones in the front. The ideal conditions for this video
        effect are when there is either very little motion and the backgroud is static,
        or when there is a lot of motion and a very wide depth of field (eg. wide
        panorama, while moving on a train).

        The filter accepts the following parameters:


        Normally the filter shifts and tils from the very first frame, and stops when
        the last one is received. However, before filtering starts, normal video may
        be preseved, so that the effect is slowly shifted in its place. Similarly,
        the last video frame may be reconstructed at the end. Alternatively it is
        possible to just start and end with black.

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
            streams=[
                self,
            ],
            kwargs={
                "tilt": tilt,
                "start": start,
                "end": end,
                "hold": hold,
                "pad": pad,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tinterlace(self, *, mode: int = None, flags: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.257 tinterlace
        Perform various types of temporal field interlacing.

        Frames are counted starting from 1, so the first input frame is
        considered odd.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int mode: Specify the mode of the interlacing. This option can also be specified as a value alone. See below for a list of values for this option. Available values are: ‘merge, 0’ Move odd frames into the upper field, even into the lower field, generating a double height frame at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 22222 44444 11111 33333 22222 44444 11111 33333 22222 44444 11111 33333 22222 44444 ‘drop_even, 1’ Only output odd frames, even frames are dropped, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 11111 33333 11111 33333 11111 33333 ‘drop_odd, 2’ Only output even frames, odd frames are dropped, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 22222 44444 22222 44444 22222 44444 22222 44444 ‘pad, 3’ Expand each frame to full height, but pad alternate lines with black, generating a frame with double height at the same input frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 11111 ..... 33333 ..... ..... 22222 ..... 44444 ‘interleave_top, 4’ Interleave the upper field from odd frames with the lower field from even frames, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- Output: 11111 33333 22222 44444 11111 33333 22222 44444 ‘interleave_bottom, 5’ Interleave the lower field from odd frames with the upper field from even frames, generating a frame with unchanged height at half frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 11111 22222<- 33333 44444<- 11111<- 22222 33333<- 44444 Output: 22222 44444 11111 33333 22222 44444 11111 33333 ‘interlacex2, 6’ Double frame rate with unchanged height. Frames are inserted each containing the second temporal field from the previous input frame and the first temporal field from the next input frame. This mode relies on the top_field_first flag. Useful for interlaced video displays with no field synchronisation. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 22222 22222 33333 33333 44444 44444 11111 11111 22222 22222 33333 33333 44444 11111 22222 22222 33333 33333 44444 44444 11111 11111 22222 22222 33333 33333 44444 ‘mergex2, 7’ Move odd frames into the upper field, even into the lower field, generating a double height frame at same frame rate. ------> time Input: Frame 1 Frame 2 Frame 3 Frame 4 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 11111 22222 33333 44444 Output: 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 11111 33333 33333 55555 22222 22222 44444 44444 Numeric values are deprecated but are accepted for backward compatibility reasons. Default mode is merge.
        :param str flags: Specify flags influencing the filter process. Available value for flags is: low_pass_filter, vlpf Enable linear vertical low-pass filtering in the filter. Vertical low-pass filtering is required when creating an interlaced destination from a progressive source which contains high-frequency vertical detail. Filtering will reduce interlace ’twitter’ and Moire patterning. complex_filter, cvlpf Enable complex vertical low-pass filtering. This will slightly less reduce interlace ’twitter’ and Moire patterning but better retain detail and subjective sharpness impression. bypass_il Bypass already interlaced frames, only adjust the frame rate. Vertical low-pass filtering and bypassing already interlaced frames can only be enabled for mode interleave_top and interleave_bottom.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tinterlace

        """
        filter_node = FilterNode(
            name="tinterlace",
            streams=[
                self,
            ],
            kwargs={
                "mode": mode,
                "flags": flags,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tlut2(self, *, c0: str = None, c1: str = None, c2: str = None, c3: str = None, **kwargs: Any) -> "VideoStream":
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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

        """
        filter_node = FilterNode(
            name="tlut2",
            streams=[
                self,
            ],
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tmedian(
        self, *, radius: int = None, planes: int = None, percentile: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.258 tmedian
        Pick median pixels from several successive input video frames.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int radius: Set radius of median filter. Default is 1. Allowed range is from 1 to 127.
        :param int planes: Set which planes to filter. Default value is 15, by which all planes are processed.
        :param float percentile: Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmedian

        """
        filter_node = FilterNode(
            name="tmedian",
            streams=[
                self,
            ],
            kwargs={
                "radius": radius,
                "planes": planes,
                "percentile": percentile,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tmidequalizer(
        self, *, radius: int = None, sigma: float = None, planes: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.259 tmidequalizer
        Apply Temporal Midway Video Equalization effect.

        Midway Video Equalization adjusts a sequence of video frames to have the same
        histograms, while maintaining their dynamics as much as possible. It’s
        useful for e.g. matching exposures from a video frames sequence.

        This filter accepts the following option:

        Parameters:
        ----------

        :param int radius: Set filtering radius. Default is 5. Allowed range is from 1 to 127.
        :param float sigma: Set filtering sigma. Default is 0.5. This controls strength of filtering. Setting this option to 0 effectively does nothing.
        :param int planes: Set which planes to process. Default is 15, which is all available planes.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmidequalizer

        """
        filter_node = FilterNode(
            name="tmidequalizer",
            streams=[
                self,
            ],
            kwargs={
                "radius": radius,
                "sigma": sigma,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tmix(
        self, *, frames: int = None, weights: str = None, scale: float = None, planes: str = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.260 tmix
        Mix successive video frames.

        A description of the accepted options follows.

        Parameters:
        ----------

        :param int frames: The number of successive frames to mix. If unspecified, it defaults to 3.
        :param str weights: Specify weight of each input video frame. Each weight is separated by space. If number of weights is smaller than number of frames last specified weight will be used for all remaining unset weights.
        :param float scale: Specify scale, if it is set it will be multiplied with sum of each weight multiplied with pixel values to give final destination pixel value. By default scale is auto scaled to sum of weights.
        :param str planes: Set which planes to filter. Default is all. Allowed range is from 0 to 15.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmix

        """
        filter_node = FilterNode(
            name="tmix",
            streams=[
                self,
            ],
            kwargs={
                "frames": frames,
                "weights": weights,
                "scale": scale,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tonemap(
        self, *, tonemap: int = None, param: float = None, desat: float = None, peak: float = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.261 tonemap
        Tone map colors from different dynamic ranges.

        This filter expects data in single precision floating point, as it needs to
        operate on (and can output) out-of-range values. Another filter, such as
        zscale, is needed to convert the resulting frame to a usable format.

        The tonemapping algorithms implemented only work on linear light, so input
        data should be linearized beforehand (and possibly correctly tagged).


        ffmpeg -i INPUT -vf zscale=transfer=linear,tonemap=clip,zscale=transfer=bt709,format=yuv420p OUTPUT

        Parameters:
        ----------

        :param int tonemap: None
        :param float param: None
        :param float desat: None
        :param float peak: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap

        """
        filter_node = FilterNode(
            name="tonemap",
            streams=[
                self,
            ],
            kwargs={
                "tonemap": tonemap,
                "param": param,
                "desat": desat,
                "peak": peak,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tonemap_opencl(
        self,
        *,
        tonemap: int = None,
        transfer: int = None,
        matrix: int = None,
        primaries: int = None,
        range: int = None,
        format: str = None,
        peak: float = None,
        param: float = None,
        desat: float = None,
        threshold: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        12.16 tonemap_opencl
        Perform HDR(PQ/HLG) to SDR conversion with tone-mapping.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int tonemap: Specify the tone-mapping operator to be used. Same as tonemap option in tonemap.
        :param int transfer: Set the output transfer characteristics. Possible values are: bt709 bt2020 Default is bt709.
        :param int matrix: Set the output colorspace matrix. Possible value are: bt709 bt2020 Default is same as input.
        :param int primaries: Set the output color primaries. Possible values are: bt709 bt2020 Default is same as input.
        :param int range: Set the output color range. Possible values are: tv/mpeg pc/jpeg Default is same as input.
        :param str format: Specify the output pixel format. Currently supported formats are: p010 nv12
        :param float peak: None
        :param float param: Tune the tone mapping algorithm. same as param option in tonemap.
        :param float desat: Apply desaturation for highlights that exceed this level of brightness. The higher the parameter, the more color information will be preserved. This setting helps prevent unnaturally blown-out colors for super-highlights, by (smoothly) turning into white instead. This makes images feel more natural, at the cost of reducing information about out-of-range colors. The default value is 0.5, and the algorithm here is a little different from the cpu version tonemap currently. A setting of 0.0 disables this option.
        :param float threshold: The tonemapping algorithm parameters is fine-tuned per each scene. And a threshold is used to detect whether the scene has changed or not. If the distance between the current frame average brightness and the current running average exceeds a threshold value, we would re-calculate scene average and peak brightness. The default value is 0.2.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap_005fopencl

        """
        filter_node = FilterNode(
            name="tonemap_opencl",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def tonemap_vaapi(self, *, format: str, matrix: str, primaries: str, transfer: str, **kwargs: Any) -> "VideoStream":
        """

        13.2 tonemap_vaapi
        Perform HDR(High Dynamic Range) to SDR(Standard Dynamic Range) conversion with tone-mapping.
        It maps the dynamic range of HDR10 content to the SDR content.
        It currently only accepts HDR10 as input.

        It accepts the following parameters:

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
            streams=[
                self,
            ],
            kwargs={
                "format": format,
                "matrix": matrix,
                "primaries": primaries,
                "transfer": transfer,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def tpad(
        self,
        *,
        start: int = None,
        stop: int = None,
        start_mode: int = None,
        stop_mode: int = None,
        start_duration: int = None,
        stop_duration: int = None,
        color: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.262 tpad
        Temporarily pad video frames.

        The filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "start": start,
                "stop": stop,
                "start_mode": start_mode,
                "stop_mode": stop_mode,
                "start_duration": start_duration,
                "stop_duration": stop_duration,
                "color": color,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def transpose(self, *, dir: int = None, passthrough: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.263 transpose
        Transpose rows with columns in the input video and optionally flip it.

        It accepts the following parameters:


        For example to rotate by 90 degrees clockwise and preserve portrait
        layout:

        transpose=dir=1:passthrough=portrait

        The command above can also be specified as:

        transpose=1:portrait

        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘0, 4, cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip (default), that is: L.R L.l . . -> . . l.r R.r ‘1, 5, clock’ Rotate by 90 degrees clockwise, that is: L.R l.L . . -> . . l.r r.R ‘2, 6, cclock’ Rotate by 90 degrees counterclockwise, that is: L.R R.r . . -> . . l.r L.l ‘3, 7, clock_flip’ Rotate by 90 degrees clockwise and vertically flip, that is: L.R r.R . . -> . . l.r l.L For values between 4-7, the transposition is only done if the input video geometry is portrait and not landscape. These values are deprecated, the passthrough option should be used instead. Numerical values are deprecated, and should be dropped in favor of symbolic constants.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height). Default value is none.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose

        """
        filter_node = FilterNode(
            name="transpose",
            streams=[
                self,
            ],
            kwargs={
                "dir": dir,
                "passthrough": passthrough,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def transpose_npp(self, *, dir: int = None, passthrough: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.264 transpose_npp
        Transpose rows with columns in the input video and optionally flip it.
        For more in depth examples see the transpose video filter, which shares mostly the same options.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fnpp

        """
        filter_node = FilterNode(
            name="transpose_npp",
            streams=[
                self,
            ],
            kwargs={
                "dir": dir,
                "passthrough": passthrough,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def transpose_vt(self, *, dir: int = None, passthrough: int = None, **kwargs: Any) -> "VideoStream":
        """

        14.12 transpose_vt
        Transpose rows with columns in the input video and optionally flip it.
        For more in depth examples see the transpose video filter, which shares mostly the same options.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip. ‘hflip’ Flip the input video horizontally. ‘vflip’ Flip the input video vertically.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvt

        """
        filter_node = FilterNode(
            name="transpose_vt",
            streams=[
                self,
            ],
            kwargs={
                "dir": dir,
                "passthrough": passthrough,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def transpose_vulkan(self, *, dir: int = None, passthrough: int = None, **kwargs: Any) -> "VideoStream":
        """

        14.13 transpose_vulkan
        Transpose rows with columns in the input video and optionally flip it.
        For more in depth examples see the transpose video filter, which shares mostly the same options.

        It accepts the following parameters:

        Parameters:
        ----------

        :param int dir: Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.
        :param int passthrough: Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvulkan

        """
        filter_node = FilterNode(
            name="transpose_vulkan",
            streams=[
                self,
            ],
            kwargs={
                "dir": dir,
                "passthrough": passthrough,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def trim(
        self,
        *,
        start: int = None,
        end: int = None,
        start_pts: int = None,
        end_pts: int = None,
        duration: int = None,
        start_frame: int = None,
        end_frame: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.265 trim
        Trim the input so that the output contains one continuous subpart of the input.

        It accepts the following parameters:

        start, end, and duration are expressed as time
        duration specifications; see
        (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
        for the accepted syntax.

        Note that the first two sets of the start/end options and the duration
        option look at the frame timestamp, while the _frame variants simply count the
        frames that pass through the filter. Also note that this filter does not modify
        the timestamps. If you wish for the output timestamps to start at zero, insert a
        setpts filter after the trim filter.

        If multiple start or end options are set, this filter tries to be greedy and
        keep all the frames that match at least one of the specified constraints. To keep
        only the part that matches all the constraints at once, chain multiple trim
        filters.

        The defaults are such that all the input is kept. So it is possible to set e.g.
        just the end values to keep everything before the specified time.

        Examples:

         Drop everything except the second minute of input:

        ffmpeg -i INPUT -vf trim=60:120

         Keep only the first second:

        ffmpeg -i INPUT -vf trim=duration=1

        Parameters:
        ----------

        :param int start: None
        :param int end: None
        :param int start_pts: None
        :param int end_pts: None
        :param int duration: None
        :param int start_frame: None
        :param int end_frame: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#trim

        """
        filter_node = FilterNode(
            name="trim",
            streams=[
                self,
            ],
            kwargs={
                "start": start,
                "end": end,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "start_frame": start_frame,
                "end_frame": end_frame,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def unpremultiply(
        self, *streams: "VideoStream", planes: int = None, inplace: bool = None, **kwargs: Any
    ) -> "VideoStream":
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
                self,
                *streams,
            ],
            kwargs={
                "planes": planes,
                "inplace": inplace,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def unsharp(
        self,
        *,
        luma_msize_x: int = None,
        luma_msize_y: int = None,
        luma_amount: float = None,
        chroma_msize_x: int = None,
        chroma_msize_y: int = None,
        chroma_amount: float = None,
        alpha_msize_x: int = None,
        alpha_msize_y: int = None,
        alpha_amount: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.267 unsharp
        Sharpen or blur the input video.

        It accepts the following parameters:


        All parameters are optional and default to the equivalent of the
        string ’5:5:1.0:5:5:0.0’.

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#unsharp

        """
        filter_node = FilterNode(
            name="unsharp",
            streams=[
                self,
            ],
            kwargs={
                "luma_msize_x": luma_msize_x,
                "luma_msize_y": luma_msize_y,
                "luma_amount": luma_amount,
                "chroma_msize_x": chroma_msize_x,
                "chroma_msize_y": chroma_msize_y,
                "chroma_amount": chroma_amount,
                "alpha_msize_x": alpha_msize_x,
                "alpha_msize_y": alpha_msize_y,
                "alpha_amount": alpha_amount,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def unsharp_opencl(
        self,
        *,
        luma_msize_x: float = None,
        luma_msize_y: float = None,
        luma_amount: float = None,
        chroma_msize_x: float = None,
        chroma_msize_y: float = None,
        chroma_amount: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        12.17 unsharp_opencl
        Sharpen or blur the input video.

        It accepts the following parameters:


        All parameters are optional and default to the equivalent of the
        string ’5:5:1.0:5:5:0.0’.

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
            streams=[
                self,
            ],
            kwargs={
                "luma_msize_x": luma_msize_x,
                "luma_msize_y": luma_msize_y,
                "luma_amount": luma_amount,
                "chroma_msize_x": chroma_msize_x,
                "chroma_msize_y": chroma_msize_y,
                "chroma_amount": chroma_amount,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def untile(self, *, layout: str = None, **kwargs: Any) -> "VideoStream":
        """

        11.268 untile
        Decompose a video made of tiled images into the individual images.

        The frame rate of the output video is the frame rate of the input video
        multiplied by the number of tiles.

        This filter does the reverse of tile.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str layout: Set the grid size (i.e. the number of lines and columns). For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#untile

        """
        filter_node = FilterNode(
            name="untile",
            streams=[
                self,
            ],
            kwargs={
                "layout": layout,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def uspp(
        self, *, quality: int = None, qp: int = None, use_bframe_qp: bool = None, codec: str = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.269 uspp
        Apply ultra slow/simple postprocessing filter that compresses and decompresses
        the image at several (or - in the case of quality level 8 - all)
        shifts and average the results.

        The way this differs from the behavior of spp is that uspp actually encodes &
        decodes each case with libavcodec Snow, whereas spp uses a simplified intra only 8x8
        DCT similar to MJPEG.

        This filter is only available in ffmpeg version 4.4 or earlier.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int quality: Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-8. If set to 0, the filter will have no effect. A value of 8 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        :param int qp: Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        :param bool use_bframe_qp: None
        :param str codec: Use specified codec instead of snow.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#uspp

        """
        filter_node = FilterNode(
            name="uspp",
            streams=[
                self,
            ],
            kwargs={
                "quality": quality,
                "qp": qp,
                "use_bframe_qp": use_bframe_qp,
                "codec": codec,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def v360(
        self,
        *,
        input: int = None,
        output: int = None,
        interp: int = None,
        w: int = None,
        h: int = None,
        in_stereo: int = None,
        out_stereo: int = None,
        in_forder: str = None,
        out_forder: str = None,
        in_frot: str = None,
        out_frot: str = None,
        in_pad: float = None,
        out_pad: float = None,
        fin_pad: int = None,
        fout_pad: int = None,
        yaw: float = None,
        pitch: float = None,
        roll: float = None,
        rorder: str = None,
        h_fov: float = None,
        v_fov: float = None,
        d_fov: float = None,
        h_flip: bool = None,
        v_flip: bool = None,
        d_flip: bool = None,
        ih_flip: bool = None,
        iv_flip: bool = None,
        in_trans: bool = None,
        out_trans: bool = None,
        ih_fov: float = None,
        iv_fov: float = None,
        id_fov: float = None,
        h_offset: float = None,
        v_offset: float = None,
        alpha_mask: bool = None,
        reset_rot: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.270 v360
        Convert 360 videos between various formats.

        The filter accepts the following options:

        Parameters:
        ----------

        :param int input: Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        :param int output: Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        :param int interp: Set interpolation method. Note: more complex interpolation methods require much more memory to run. Available methods: ‘near’ ‘nearest’ Nearest neighbour. ‘line’ ‘linear’ Bilinear interpolation. ‘lagrange9’ Lagrange9 interpolation. ‘cube’ ‘cubic’ Bicubic interpolation. ‘lanc’ ‘lanczos’ Lanczos interpolation. ‘sp16’ ‘spline16’ Spline16 interpolation. ‘gauss’ ‘gaussian’ Gaussian interpolation. ‘mitchell’ Mitchell interpolation. Default value is ‘line’.
        :param int w: Set the output video resolution. Default resolution depends on formats.
        :param int h: Set the output video resolution. Default resolution depends on formats.
        :param int in_stereo: Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        :param int out_stereo: Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        :param str in_forder: None
        :param str out_forder: None
        :param str in_frot: None
        :param str out_frot: None
        :param float in_pad: None
        :param float out_pad: None
        :param int fin_pad: None
        :param int fout_pad: None
        :param float yaw: Set rotation for the output video. Values in degrees.
        :param float pitch: Set rotation for the output video. Values in degrees.
        :param float roll: Set rotation for the output video. Values in degrees.
        :param str rorder: Set rotation order for the output video. Choose one item for each position. ‘y, Y’ yaw ‘p, P’ pitch ‘r, R’ roll Default value is ‘ypr’.
        :param float h_fov: None
        :param float v_fov: None
        :param float d_fov: None
        :param bool h_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool v_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool d_flip: Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        :param bool ih_flip: Set if input video is flipped horizontally/vertically. Boolean values.
        :param bool iv_flip: Set if input video is flipped horizontally/vertically. Boolean values.
        :param bool in_trans: Set if input video is transposed. Boolean value, by default disabled.
        :param bool out_trans: Set if output video needs to be transposed. Boolean value, by default disabled.
        :param float ih_fov: None
        :param float iv_fov: None
        :param float id_fov: None
        :param float h_offset: Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        :param float v_offset: Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        :param bool alpha_mask: Build mask in alpha plane for all unmapped pixels by marking them fully transparent. Boolean value, by default disabled.
        :param bool reset_rot: Reset rotation of output video. Boolean value, by default disabled.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#v360

        """
        filter_node = FilterNode(
            name="v360",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def vaguedenoiser(
        self,
        *,
        threshold: float = None,
        method: int = None,
        nsteps: int = None,
        percent: float = None,
        planes: int = None,
        type: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.271 vaguedenoiser
        Apply a wavelet based denoiser.

        It transforms each frame from the video input into the wavelet domain,
        using Cohen-Daubechies-Feauveau 9/7. Then it applies some filtering to
        the obtained coefficients. It does an inverse wavelet transform after.
        Due to wavelet properties, it should give a nice smoothed result, and
        reduced noise, without blurring picture features.

        This filter accepts the following options:

        Parameters:
        ----------

        :param float threshold: The filtering strength. The higher, the more filtered the video will be. Hard thresholding can use a higher threshold than soft thresholding before the video looks overfiltered. Default value is 2.
        :param int method: The filtering method the filter will use. It accepts the following values: ‘hard’ All values under the threshold will be zeroed. ‘soft’ All values under the threshold will be zeroed. All values above will be reduced by the threshold. ‘garrote’ Scales or nullifies coefficients - intermediary between (more) soft and (less) hard thresholding. Default is garrote.
        :param int nsteps: Number of times, the wavelet will decompose the picture. Picture can’t be decomposed beyond a particular point (typically, 8 for a 640x480 frame - as 2^9 = 512 > 480). Valid values are integers between 1 and 32. Default value is 6.
        :param float percent: Partial of full denoising (limited coefficients shrinking), from 0 to 100. Default value is 85.
        :param int planes: A list of the planes to process. By default all planes are processed.
        :param int type: The threshold type the filter will use. It accepts the following values: ‘universal’ Threshold used is same for all decompositions. ‘bayes’ Threshold used depends also on each decomposition coefficients. Default is universal.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vaguedenoiser

        """
        filter_node = FilterNode(
            name="vaguedenoiser",
            streams=[
                self,
            ],
            kwargs={
                "threshold": threshold,
                "method": method,
                "nsteps": nsteps,
                "percent": percent,
                "planes": planes,
                "type": type,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def varblur(
        self, _radius: "VideoStream", *, min_r: int = None, max_r: int = None, planes: int = None, **kwargs: Any
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
                self,
                _radius,
            ],
            kwargs={
                "min_r": min_r,
                "max_r": max_r,
                "planes": planes,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def vectorscope(
        self,
        *,
        mode: int = None,
        x: int = None,
        y: int = None,
        intensity: float = None,
        envelope: int = None,
        graticule: int = None,
        opacity: float = None,
        flags: str = None,
        bgopacity: float = None,
        lthreshold: float = None,
        hthreshold: float = None,
        colorspace: int = None,
        tint0: float = None,
        tint1: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.273 vectorscope
        Display 2 color component values in the two dimensional graph (which is called
        a vectorscope).

        This filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def vflip(self, **kwargs: Any) -> "VideoStream":
        """

        11.276 vflip
        Flip the input video vertically.

        For example, to vertically flip a video with ffmpeg:

        ffmpeg -i in.avi -vf "vflip" out.avi

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#vflip

        """
        filter_node = FilterNode(
            name="vflip",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def vflip_vulkan(self, **kwargs: Any) -> "VideoStream":
        """

        14.6 vflip_vulkan
        Flips an image vertically.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#vflip_005fvulkan

        """
        filter_node = FilterNode(
            name="vflip_vulkan",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def vfrdet(self, **kwargs: Any) -> "VideoStream":
        """

        11.277 vfrdet
        Detect variable frame rate video.

        This filter tries to detect if the input is variable or constant frame rate.

        At end it will output number of frames detected as having variable delta pts,
        and ones with constant delta pts.
        If there was frames with variable delta, than it will also show min, max and
        average delta encountered.

        Parameters:
        ----------


        Ref: https://ffmpeg.org/ffmpeg-filters.html#vfrdet

        """
        filter_node = FilterNode(
            name="vfrdet",
            streams=[
                self,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def vibrance(
        self,
        *,
        intensity: float = None,
        rbal: float = None,
        gbal: float = None,
        bbal: float = None,
        rlum: float = None,
        glum: float = None,
        blum: float = None,
        alternate: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.278 vibrance
        Boost or alter saturation.

        The filter accepts the following options:

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

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrance

        """
        filter_node = FilterNode(
            name="vibrance",
            streams=[
                self,
            ],
            kwargs={
                "intensity": intensity,
                "rbal": rbal,
                "gbal": gbal,
                "bbal": bbal,
                "rlum": rlum,
                "glum": glum,
                "blum": blum,
                "alternate": alternate,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def vidstabdetect(
        self,
        *,
        result: str = None,
        shakiness: int = None,
        accuracy: int = None,
        stepsize: int = None,
        mincontrast: float = None,
        show: int = None,
        tripod: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.274 vidstabdetect
        Analyze video stabilization/deshaking. Perform pass 1 of 2, see
        vidstabtransform for pass 2.

        This filter generates a file with relative translation and rotation
        transform information about subsequent frames, which is then used by
        the vidstabtransform filter.

        To enable compilation of this filter you need to configure FFmpeg with
        --enable-libvidstab.

        This filter accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
                "result": result,
                "shakiness": shakiness,
                "accuracy": accuracy,
                "stepsize": stepsize,
                "mincontrast": mincontrast,
                "show": show,
                "tripod": tripod,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def vidstabtransform(
        self,
        *,
        input: str = None,
        smoothing: int = None,
        optalgo: int = None,
        maxshift: int = None,
        maxangle: float = None,
        crop: int = None,
        invert: int = None,
        relative: int = None,
        zoom: float = None,
        optzoom: int = None,
        zoomspeed: float = None,
        interpol: int = None,
        tripod: bool = None,
        debug: bool = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.275 vidstabtransform
        Video stabilization/deshaking: pass 2 of 2,
        see vidstabdetect for pass 1.

        Read a file with transform information for each frame and
        apply/compensate them. Together with the vidstabdetect
        filter this can be used to deshake videos. See also
        http://public.hronopik.de/vid.stab. It is important to also use
        the unsharp filter, see below.

        To enable compilation of this filter you need to configure FFmpeg with
        --enable-libvidstab.

        Parameters:
        ----------

        :param str input: None
        :param int smoothing: None
        :param int optalgo: None
        :param int maxshift: None
        :param float maxangle: None
        :param int crop: None
        :param int invert: None
        :param int relative: None
        :param float zoom: None
        :param int optzoom: None
        :param float zoomspeed: None
        :param int interpol: None
        :param bool tripod: None
        :param bool debug: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vidstabtransform

        """
        filter_node = FilterNode(
            name="vidstabtransform",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def vif(self, _reference: "VideoStream", **kwargs: Any) -> "VideoStream":
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
                self,
                _reference,
            ],
            kwargs={} | kwargs,
        )
        return filter_node._vs(0)

    def vignette(
        self,
        *,
        angle: str = None,
        x0: str = None,
        y0: str = None,
        mode: int = None,
        eval: int = None,
        dither: bool = None,
        aspect: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.280 vignette
        Make or reverse a natural vignetting effect.

        The filter accepts the following options:

        Parameters:
        ----------

        :param str angle: Set lens angle expression as a number of radians. The value is clipped in the [0,PI/2] range. Default value: "PI/5"
        :param str x0: Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        :param str y0: Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        :param int mode: Set forward/backward mode. Available modes are: ‘forward’ The larger the distance from the central point, the darker the image becomes. ‘backward’ The larger the distance from the central point, the brighter the image becomes. This can be used to reverse a vignette effect, though there is no automatic detection to extract the lens angle and other settings (yet). It can also be used to create a burning effect. Default value is ‘forward’.
        :param int eval: Set evaluation mode for the expressions (angle, x0, y0). It accepts the following values: ‘init’ Evaluate expressions only once during the filter initialization. ‘frame’ Evaluate expressions for each incoming frame. This is way slower than the ‘init’ mode since it requires all the scalers to be re-computed, but it allows advanced dynamic expressions. Default value is ‘init’.
        :param bool dither: Set dithering to reduce the circular banding effects. Default is 1 (enabled).
        :param float aspect: Set vignette aspect. This setting allows one to adjust the shape of the vignette. Setting this value to the SAR of the input will make a rectangular vignetting following the dimensions of the video. Default is 1/1.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vignette

        """
        filter_node = FilterNode(
            name="vignette",
            streams=[
                self,
            ],
            kwargs={
                "angle": angle,
                "x0": x0,
                "y0": y0,
                "mode": mode,
                "eval": eval,
                "dither": dither,
                "aspect": aspect,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def vmafmotion(self, *, stats_file: str, **kwargs: Any) -> "VideoStream":
        """

        11.281 vmafmotion
        Obtain the average VMAF motion score of a video.
        It is one of the component metrics of VMAF.

        The obtained average motion score is printed through the logging system.

        The filter accepts the following options:


        Example:

        ffmpeg -i ref.mpg -vf vmafmotion -f null -

        Parameters:
        ----------

        :param str stats_file: If specified, the filter will use the named file to save the motion score of each frame with respect to the previous frame. When filename equals "-" the data is sent to standard output.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vmafmotion

        """
        filter_node = FilterNode(
            name="vmafmotion",
            streams=[
                self,
            ],
            kwargs={
                "stats_file": stats_file,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def vstack(
        self, *streams: "VideoStream", inputs: int = None, shortest: bool = None, **kwargs: Any
    ) -> "VideoStream":
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "shortest": shortest,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def w3fdif(
        self, *, filter: int = None, mode: int = None, parity: int = None, deint: int = None, **kwargs: Any
    ) -> "VideoStream":
        """

        11.283 w3fdif
        Deinterlace the input video ("w3fdif" stands for "Weston 3 Field
        Deinterlacing Filter").

        Based on the process described by Martin Weston for BBC R&D, and
        implemented based on the de-interlace algorithm written by Jim
        Easterbrook for BBC R&D, the Weston 3 field deinterlacing filter
        uses filter coefficients calculated by BBC R&D.

        This filter uses field-dominance information in frame to decide which
        of each pair of fields to place first in the output.
        If it gets it wrong use setfield filter before w3fdif filter.

        There are two sets of filter coefficients, so called "simple"
        and "complex". Which set of filter coefficients is used can
        be set by passing an optional parameter:

        Parameters:
        ----------

        :param int filter: Set the interlacing filter coefficients. Accepts one of the following values: ‘simple’ Simple filter coefficient set. ‘complex’ More-complex filter coefficient set. Default value is ‘complex’.
        :param int mode: The interlacing mode to adopt. It accepts one of the following values: frame Output one frame for each frame. field Output one frame for each field. The default value is field.
        :param int parity: The picture field parity assumed for the input interlaced video. It accepts one of the following values: tff Assume the top field is first. bff Assume the bottom field is first. auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        :param int deint: Specify which frames to deinterlace. Accepts one of the following values: ‘all’ Deinterlace all frames, ‘interlaced’ Only deinterlace frames marked as interlaced. Default value is ‘all’.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#w3fdif

        """
        filter_node = FilterNode(
            name="w3fdif",
            streams=[
                self,
            ],
            kwargs={
                "filter": filter,
                "mode": mode,
                "parity": parity,
                "deint": deint,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def waveform(
        self,
        *,
        mode: int = None,
        intensity: float = None,
        mirror: bool = None,
        display: int = None,
        components: int = None,
        envelope: int = None,
        filter: int = None,
        graticule: int = None,
        opacity: float = None,
        flags: str = None,
        scale: int = None,
        bgopacity: float = None,
        tint0: float = None,
        tint1: float = None,
        fitmode: int = None,
        input: int = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.284 waveform
        Video waveform monitor.

        The waveform monitor plots color component intensity. By default luma
        only. Each column of the waveform corresponds to a column of pixels in the
        source video.

        It accepts the following options:

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
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)

    def weave(self, *, first_field: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.285 weave, doubleweave
        The weave takes a field-based video input and join
        each two sequential fields into single frame, producing a new double
        height clip with half the frame rate and half the frame count.

        The doubleweave works same as weave but without
        halving frame rate and frame count.

        It accepts the following option:

        Parameters:
        ----------

        :param int first_field: Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        filter_node = FilterNode(
            name="weave",
            streams=[
                self,
            ],
            kwargs={
                "first_field": first_field,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def xbr(self, *, n: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.286 xbr
        Apply the xBR high-quality magnification filter which is designed for pixel
        art. It follows a set of edge-detection rules, see
        https://forums.libretro.com/t/xbr-algorithm-tutorial/123.

        It accepts the following option:

        Parameters:
        ----------

        :param int n: Set the scaling dimension: 2 for 2xBR, 3 for 3xBR and 4 for 4xBR. Default is 3.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xbr

        """
        filter_node = FilterNode(
            name="xbr",
            streams=[
                self,
            ],
            kwargs={
                "n": n,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def xcorrelate(
        self, _secondary: "VideoStream", *, planes: int = None, secondary: int = None, **kwargs: Any
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
                self,
                _secondary,
            ],
            kwargs={
                "planes": planes,
                "secondary": secondary,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def xfade(
        self,
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
                self,
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
        return filter_node._vs(0)

    def xfade_opencl(
        self,
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
                self,
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
        return filter_node._vs(0)

    def xmedian(
        self, *streams: "VideoStream", inputs: int = None, planes: int = None, percentile: float = None, **kwargs: Any
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
                self,
                *streams,
            ],
            kwargs={
                "inputs": inputs,
                "planes": planes,
                "percentile": percentile,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def xstack(
        self,
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
                self,
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
        return filter_node._vs(0)

    def yaepblur(self, *, radius: int = None, planes: int = None, sigma: int = None, **kwargs: Any) -> "VideoStream":
        """

        11.293 yaepblur
        Apply blur filter while preserving edges ("yaepblur" means "yet another edge preserving blur filter").
        The algorithm is described in
        "J. S. Lee, Digital image enhancement and noise filtering by use of local statistics, IEEE Trans. Pattern Anal. Mach. Intell. PAMI-2, 1980."

        It accepts the following parameters:

        Parameters:
        ----------

        :param int radius: Set the window radius. Default value is 3.
        :param int planes: Set which planes to filter. Default is only the first plane.
        :param int sigma: Set blur strength. Default value is 128.

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yaepblur

        """
        filter_node = FilterNode(
            name="yaepblur",
            streams=[
                self,
            ],
            kwargs={
                "radius": radius,
                "planes": planes,
                "sigma": sigma,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def zoompan(
        self,
        *,
        zoom: str = None,
        x: str = None,
        y: str = None,
        d: str = None,
        s: str = None,
        fps: str = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.294 zoompan
        Apply Zoom & Pan effect.

        This filter accepts the following options:


        Each expression can contain the following constants:

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
            streams=[
                self,
            ],
            kwargs={
                "zoom": zoom,
                "x": x,
                "y": y,
                "d": d,
                "s": s,
                "fps": fps,
            }
            | kwargs,
        )
        return filter_node._vs(0)

    def zscale(
        self,
        *,
        w: str,
        h: str,
        size: str,
        dither: int = None,
        filter: int = None,
        out_range: int = None,
        primaries: int = None,
        transfer: int = None,
        matrix: int = None,
        in_range: int = None,
        primariesin: int = None,
        transferin: int = None,
        matrixin: int = None,
        chromal: int = None,
        chromalin: int = None,
        npl: float = None,
        agamma: bool = None,
        param_a: float = None,
        param_b: float = None,
        **kwargs: Any
    ) -> "VideoStream":
        """

        11.295 zscale
        Scale (resize) the input video, using the z.lib library:
        https://github.com/sekrit-twc/zimg. To enable compilation of this
        filter, you need to configure FFmpeg with --enable-libzimg.

        The zscale filter forces the output display aspect ratio to be the same
        as the input, by changing the output sample aspect ratio.

        If the input image format is different from the format requested by
        the next filter, the zscale filter will convert the input to the
        requested format.

        Parameters:
        ----------

        :param str w: None
        :param str h: None
        :param str size: None
        :param int dither: None
        :param int filter: None
        :param int out_range: None
        :param int primaries: None
        :param int transfer: None
        :param int matrix: None
        :param int in_range: None
        :param int primariesin: None
        :param int transferin: None
        :param int matrixin: None
        :param int chromal: None
        :param int chromalin: None
        :param float npl: None
        :param bool agamma: None
        :param float param_a: None
        :param float param_b: None

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zscale

        """
        filter_node = FilterNode(
            name="zscale",
            streams=[
                self,
            ],
            kwargs={
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
            | kwargs,
        )
        return filter_node._vs(0)
