from typing import Any, Literal


class FilterNode:
    def __init__(self, *stream: "Stream", name: str, **kwargs: Any) -> None:
        ...

    def stream(self) -> "Stream":
        raise NotImplementedError()


class Stream:
    def aap(
        self,
        *,
        order: int,
        projection: int,
        mu: float,
        delta: float,
        out_mode: str = None,
        precision: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.1 aap Apply Affine Projection algorithm to the first audio stream using the second audio stream. This adaptive filter is used to estimate unknown audio based on multiple input audio samples. Affine projection algorithm can make trade-offs between computation complexity with convergence speed. A description of the accepted options follows.

        Parameters:
        ----------
        order:
            Set the filter order.
        projection:
            Set the projection order.
        mu:
            Set the filter mu.
        delta:
            Set the coefficient to initialize internal covariance matrix.
        out_mode:
            Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aap

        """
        return FilterNode(
            *[self],
            name="aap",
            kwargs={
                "order": order,
                "projection": projection,
                "mu": mu,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
                **kwargs,
            }
        ).stream()

    def acompressor(
        self,
        *,
        level_in: float = None,
        mode: str = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        link: str = None,
        detection: str = None,
        mix: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.2 acompressor A compressor is mainly used to reduce the dynamic range of a signal. Especially modern music is mostly compressed at a high ratio to improve the overall loudness. It’s done to get the highest attention of a listener, "fatten" the sound and bring more "power" to the track. If a signal is compressed too much it may sound dull or "dead" afterwards or it may start to "pump" (which could be a powerful effect but can also destroy a track completely). The right compression is the key to reach a professional sound and is the high art of mixing and mastering. Because of its complex settings it may take a long time to get the right feeling for this kind of effect. Compression is done by detecting the volume above a chosen level threshold and dividing it by the factor set with ratio. So if you set the threshold to -12dB and your signal reaches -6dB a ratio of 2:1 will result in a signal at -9dB. Because an exact manipulation of the signal would cause distortion of the waveform the reduction can be levelled over the time. This is done by setting "Attack" and "Release". attack determines how long the signal has to rise above the threshold before any reduction will occur and release sets the time the signal has to fall below the threshold to reduce the reduction again. Shorter signals than the chosen attack time will be left untouched. The overall reduction of the signal can be made up afterwards with the makeup setting. So compressing the peaks of a signal about 6dB and raising the makeup to this level results in a signal twice as loud than the source. To gain a softer entry in the compression the knee flattens the hard edge at the threshold in the range of the chosen decibels. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input gain. Default is 1. Range is between 0.015625 and 64.
        mode:
            Set mode of compressor operation. Can be upward or downward. Default is downward.
        threshold:
            If a signal of stream rises above this level it will affect the gain reduction. By default it is 0.125. Range is between 0.00097563 and 1.
        ratio:
            Set a ratio by which the signal is reduced. 1:2 means that if the level rose 4dB above the threshold, it will be only 2dB above after the reduction. Default is 2. Range is between 1 and 20.
        attack:
            Amount of milliseconds the signal has to rise above the threshold before gain reduction starts. Default is 20. Range is between 0.01 and 2000.
        release:
            Amount of milliseconds the signal has to fall below the threshold before reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
        makeup:
            Set the amount by how much signal will be amplified after processing. Default is 1. Range is from 1 to 64.
        knee:
            Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.82843. Range is between 1 and 8.
        link:
            Choose if the average level between all channels of input stream or the louder(maximum) channel of input stream affects the reduction. Default is average.
        detection:
            Should the exact signal be taken in case of peak or an RMS one in case of rms. Default is rms which is mostly smoother.
        mix:
            How much to use compressed signal in output. Default is 1. Range is between 0 and 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acompressor

        """
        return FilterNode(
            *[self],
            name="acompressor",
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
                "mix": mix,
                **kwargs,
            }
        ).stream()

    def acontrast(self, *, contrast: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.3 acontrast Simple audio dynamic range compression/expansion filter. The filter accepts the following options:

        Parameters:
        ----------
        contrast:
            Set contrast. Default is 33. Allowed range is between 0 and 100.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acontrast

        """
        return FilterNode(*[self], name="acontrast", kwargs={"contrast": contrast, **kwargs}).stream()

    def acopy(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.4 acopy Copy the input audio source unchanged to the output. This is mainly useful for testing purposes.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acopy

        """
        return FilterNode(*[self], name="acopy", kwargs={**kwargs}).stream()

    def acrossfade(
        self,
        *,
        nb_samples: int,
        duration: str,
        overlap: bool,
        curve1: Literal[
            "tri",
            "qsin",
            "hsin",
            "esin",
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
            "nofade",
        ],
        curve2: Literal[
            "tri",
            "qsin",
            "hsin",
            "esin",
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
            "nofade",
        ],
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.5 acrossfade Apply cross fade from one input audio stream to another input audio stream. The cross fade is applied for specified duration near the end of first stream. The filter accepts the following options:

        Parameters:
        ----------
        nb_samples:
            Specify the number of samples for which the cross fade effect has to last. At the end of the cross fade effect the first input audio will be completely silent. Default is 44100.
        duration:
            Specify the duration of the cross fade effect. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. By default the duration is determined by nb_samples. If set this option is used instead of nb_samples.
        overlap:
            Should first stream end overlap with second stream start. Default is enabled.
        curve1:
            Set curve for cross fade transition for first stream.
        curve2:
            Set curve for cross fade transition for second stream. For description of available curve types see afade filter description.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossfade

        """
        return FilterNode(
            *[self],
            name="acrossfade",
            kwargs={
                "nb_samples": nb_samples,
                "duration": duration,
                "overlap": overlap,
                "curve1": curve1,
                "curve2": curve2,
                **kwargs,
            }
        ).stream()

    def acrossover(
        self,
        *,
        split: list[str],
        order: str = None,
        level: float = None,
        gains: list[str] = None,
        precision: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.6 acrossover Split audio stream into several bands. This filter splits audio stream into two or more frequency ranges. Summing all streams back will give flat output. The filter accepts the following options:

        Parameters:
        ----------
        split:
            Set split frequencies. Those must be positive and increasing.
        order:
            Set filter order for each band split. This controls filter roll-off or steepness of filter transfer function. Available values are: ‘2nd’ 12 dB per octave. ‘4th’ 24 dB per octave. ‘6th’ 36 dB per octave. ‘8th’ 48 dB per octave. ‘10th’ 60 dB per octave. ‘12th’ 72 dB per octave. ‘14th’ 84 dB per octave. ‘16th’ 96 dB per octave. ‘18th’ 108 dB per octave. ‘20th’ 120 dB per octave. Default is 4th.
        level:
            Set input gain level. Allowed range is from 0 to 1. Default value is 1.
        gains:
            Set output gain for each band. Default value is 1 for all bands.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format. Default value is auto.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrossover

        """
        return FilterNode(
            *[self],
            name="acrossover",
            kwargs={"split": split, "order": order, "level": level, "gains": gains, "precision": precision, **kwargs}
        ).stream()

    def acrusher(
        self,
        *,
        level_in: float,
        level_out: float,
        bits: int,
        mix: float,
        mode: str,
        dc: float,
        aa: float,
        samples: int,
        lfo: bool,
        lforange: float,
        lforate: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.7 acrusher Reduce audio bit resolution. This filter is bit crusher with enhanced functionality. A bit crusher is used to audibly reduce number of bits an audio signal is sampled with. This doesn’t change the bit depth at all, it just produces the effect. Material reduced in bit depth sounds more harsh and "digital". This filter is able to even round to continuous values instead of discrete bit depths. Additionally it has a D/C offset which results in different crushing of the lower and the upper half of the signal. An Anti-Aliasing setting is able to produce "softer" crushing sounds. Another feature of this filter is the logarithmic mode. This setting switches from linear distances between bits to logarithmic ones. The result is a much more "natural" sounding crusher which doesn’t gate low signals for example. The human ear has a logarithmic perception, so this kind of crushing is much more pleasant. Logarithmic crushing is also able to get anti-aliased. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set level in.
        level_out:
            Set level out.
        bits:
            Set bit reduction.
        mix:
            Set mixing amount.
        mode:
            Can be linear: lin or logarithmic: log.
        dc:
            Set DC.
        aa:
            Set anti-aliasing.
        samples:
            Set sample reduction.
        lfo:
            Enable LFO. By default disabled.
        lforange:
            Set LFO range.
        lforate:
            Set LFO rate.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acrusher

        """
        return FilterNode(
            *[self],
            name="acrusher",
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
                **kwargs,
            }
        ).stream()

    def acue(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.8 acue Delay audio filtering until a given wallclock timestamp. See the cue filter.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#acue

        """
        return FilterNode(*[self], name="acue", kwargs={**kwargs}).stream()

    def addroi(
        self, *, x: str, y: str, w: str, h: str, qoffset: float, clear: bool, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.1 addroi Mark a region of interest in a video frame. The frame data is passed through unchanged, but metadata is attached to the frame indicating regions of interest which can affect the behaviour of later encoding. Multiple regions can be marked by applying the filter multiple times.

        Parameters:
        ----------
        x:
            Region distance in pixels from the left edge of the frame.
        y:
            Region distance in pixels from the top edge of the frame.
        w:
            Region width in pixels.
        h:
            Region height in pixels. The parameters x, y, w and h are expressions, and may contain the following variables: iw Width of the input frame. ih Height of the input frame.
        qoffset:
            Quantisation offset to apply within the region. This must be a real value in the range -1 to +1. A value of zero indicates no quality change. A negative value asks for better quality (less quantisation), while a positive value asks for worse quality (greater quantisation). The range is calibrated so that the extreme values indicate the largest possible offset - if the rest of the frame is encoded with the worst possible quality, an offset of -1 indicates that this region should be encoded with the best possible quality anyway. Intermediate values are then interpolated in some codec-dependent way. For example, in 10-bit H.264 the quantisation parameter varies between -12 and 51. A typical qoffset value of -1/10 therefore indicates that this region should be encoded with a QP around one-tenth of the full range better than the rest of the frame. So, if most of the frame were to be encoded with a QP of around 30, this region would get a QP of around 24 (an offset of approximately -1/10 * (51 - -12) = -6.3). An extreme value of -1 would indicate that this region should be encoded with the best possible quality regardless of the treatment of the rest of the frame - that is, should be encoded at a QP of -12.
        clear:
            If set to true, remove any existing regions of interest marked on the frame before adding the new one.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#addroi

        """
        return FilterNode(
            *[self],
            name="addroi",
            kwargs={"x": x, "y": y, "w": w, "h": h, "qoffset": qoffset, "clear": clear, **kwargs}
        ).stream()

    def adeclick(
        self,
        *,
        window: int = None,
        overlap: int = None,
        arorder: int = None,
        threshold: int = None,
        burst: int = None,
        method: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.9 adeclick Remove impulsive noise from input audio. Samples detected as impulsive noise are replaced by interpolated samples using autoregressive modelling.

        Parameters:
        ----------
        window:
            Set window size, in milliseconds. Allowed range is from 10 to 100. Default value is 55 milliseconds. This sets size of window which will be processed at once.
        overlap:
            Set window overlap, in percentage of window size. Allowed range is from 50 to 95. Default value is 75 percent. Setting this to a very high value increases impulsive noise removal but makes whole process much slower.
        arorder:
            Set autoregression order, in percentage of window size. Allowed range is from 0 to 25. Default value is 2 percent. This option also controls quality of interpolated samples using neighbour good samples.
        threshold:
            Set threshold value. Allowed range is from 1 to 100. Default value is 2. This controls the strength of impulsive noise which is going to be removed. The lower value, the more samples will be detected as impulsive noise.
        burst:
            Set burst fusion, in percentage of window size. Allowed range is 0 to 10. Default value is 2. If any two samples detected as noise are spaced less than this value then any sample between those two samples will be also detected as noise.
        method:
            Set overlap method. It accepts the following values: add, a Select overlap-add method. Even not interpolated samples are slightly changed with this method. save, s Select overlap-save method. Not interpolated samples remain unchanged. Default value is a.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclick

        """
        return FilterNode(
            *[self],
            name="adeclick",
            kwargs={
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "burst": burst,
                "method": method,
                **kwargs,
            }
        ).stream()

    def adeclip(
        self,
        *,
        window: int = None,
        overlap: int = None,
        arorder: int = None,
        threshold: int = None,
        hsize: int = None,
        method: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.10 adeclip Remove clipped samples from input audio. Samples detected as clipped are replaced by interpolated samples using autoregressive modelling.

        Parameters:
        ----------
        window:
            Set window size, in milliseconds. Allowed range is from 10 to 100. Default value is 55 milliseconds. This sets size of window which will be processed at once.
        overlap:
            Set window overlap, in percentage of window size. Allowed range is from 50 to 95. Default value is 75 percent.
        arorder:
            Set autoregression order, in percentage of window size. Allowed range is from 0 to 25. Default value is 8 percent. This option also controls quality of interpolated samples using neighbour good samples.
        threshold:
            Set threshold value. Allowed range is from 1 to 100. Default value is 10. Higher values make clip detection less aggressive.
        hsize:
            Set size of histogram used to detect clips. Allowed range is from 100 to 9999. Default value is 1000. Higher values make clip detection less aggressive.
        method:
            Set overlap method. It accepts the following values: add, a Select overlap-add method. Even not interpolated samples are slightly changed with this method. save, s Select overlap-save method. Not interpolated samples remain unchanged. Default value is a.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adeclip

        """
        return FilterNode(
            *[self],
            name="adeclip",
            kwargs={
                "window": window,
                "overlap": overlap,
                "arorder": arorder,
                "threshold": threshold,
                "hsize": hsize,
                "method": method,
                **kwargs,
            }
        ).stream()

    def adecorrelate(self, *, stages: int = None, seed: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.11 adecorrelate Apply decorrelation to input audio stream. The filter accepts the following options:

        Parameters:
        ----------
        stages:
            Set decorrelation stages of filtering. Allowed range is from 1 to 16. Default value is 6.
        seed:
            Set random seed used for setting delay in samples across channels.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adecorrelate

        """
        return FilterNode(*[self], name="adecorrelate", kwargs={"stages": stages, "seed": seed, **kwargs}).stream()

    def adelay(self, *, delays: str, all: bool, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.12 adelay Delay one or more audio channels. Samples in delayed channel are filled with silence. The filter accepts the following option:

        Parameters:
        ----------
        delays:
            Set list of delays in milliseconds for each channel separated by ’|’. Unused delays will be silently ignored. If number of given delays is smaller than number of channels all remaining channels will not be delayed. If you want to delay exact number of samples, append ’S’ to number. If you want instead to delay in seconds, append ’s’ to number.
        all:
            Use last set delay for all remaining channels. By default is disabled. This option if enabled changes how option delays is interpreted.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adelay

        """
        return FilterNode(*[self], name="adelay", kwargs={"delays": delays, "all": all, **kwargs}).stream()

    def adenorm(self, *, level: float = None, type: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.13 adenorm Remedy denormals in audio by adding extremely low-level noise. This filter shall be placed before any filter that can produce denormals. A description of the accepted parameters follows.

        Parameters:
        ----------
        level:
            Set level of added noise in dB. Default is -351. Allowed range is from -451 to -90.
        type:
            Set type of added noise. dc Add DC signal. ac Add AC signal. square Add square signal. pulse Add pulse signal. Default is dc.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adenorm

        """
        return FilterNode(*[self], name="adenorm", kwargs={"level": level, "type": type, **kwargs}).stream()

    def aderivative(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.14 aderivative, aintegral Compute derivative/integral of audio stream. Applying both filters one after another produces original audio.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        return FilterNode(*[self], name="aderivative", kwargs={**kwargs}).stream()

    def adrc(
        self,
        *,
        transfer: str = None,
        attack: int = None,
        release: int = None,
        channels: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.15 adrc Apply spectral dynamic range controller filter to input audio stream. A description of the accepted options follows.

        Parameters:
        ----------
        transfer:
            Set the transfer expression. The expression can contain the following constants: ch current channel number sn current sample number nb_channels number of channels t timestamp expressed in seconds sr sample rate p current frequency power value, in dB f current frequency in Hz Default value is p.
        attack:
            Set the attack in milliseconds. Default is 50 milliseconds. Allowed range is from 1 to 1000 milliseconds.
        release:
            Set the release in milliseconds. Default is 100 milliseconds. Allowed range is from 5 to 2000 milliseconds.
        channels:
            Set which channels to filter, by default all channels in audio stream are filtered.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adrc

        """
        return FilterNode(
            *[self],
            name="adrc",
            kwargs={"transfer": transfer, "attack": attack, "release": release, "channels": channels, **kwargs}
        ).stream()

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
        mode: str = None,
        dftype: str = None,
        tftype: str = None,
        auto: str = None,
        precision: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.16 adynamicequalizer Apply dynamic equalization to input audio stream. A description of the accepted options follows.

        Parameters:
        ----------
        threshold:
            Set the detection threshold used to trigger equalization. Threshold detection is using detection filter. Default value is 0. Allowed range is from 0 to 100.
        dfrequency:
            Set the detection frequency in Hz used for detection filter used to trigger equalization. Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
        dqfactor:
            Set the detection resonance factor for detection filter used to trigger equalization. Default value is 1. Allowed range is from 0.001 to 1000.
        tfrequency:
            Set the target frequency of equalization filter. Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
        tqfactor:
            Set the target resonance factor for target equalization filter. Default value is 1. Allowed range is from 0.001 to 1000.
        attack:
            Set the amount of milliseconds the signal from detection has to rise above the detection threshold before equalization starts. Default is 20. Allowed range is between 1 and 2000.
        release:
            Set the amount of milliseconds the signal from detection has to fall below the detection threshold before equalization ends. Default is 200. Allowed range is between 1 and 2000.
        ratio:
            Set the ratio by which the equalization gain is raised. Default is 1. Allowed range is between 0 and 30.
        makeup:
            Set the makeup offset by which the equalization gain is raised. Default is 0. Allowed range is between 0 and 100.
        range:
            Set the max allowed cut/boost amount. Default is 50. Allowed range is from 1 to 200.
        mode:
            Set the mode of filter operation, can be one of the following: ‘listen’ Output only isolated detection signal. ‘cutbelow’ Cut frequencies below detection threshold. ‘cutabove’ Cut frequencies above detection threshold. ‘boostbelow’ Boost frequencies below detection threshold. ‘boostabove’ Boost frequencies above detection threshold. Default mode is ‘cutbelow’.
        dftype:
            Set the type of detection filter, can be one of the following: ‘bandpass’ ‘lowpass’ ‘highpass’ ‘peak’ Default type is ‘bandpass’.
        tftype:
            Set the type of target filter, can be one of the following: ‘bell’ ‘lowshelf’ ‘highshelf’ Default type is ‘bell’.
        auto:
            Automatically gather threshold from detection filter. By default is ‘disabled’. This option is useful to detect threshold in certain time frame of input audio stream, in such case option value is changed at runtime. Available values are: ‘disabled’ Disable using automatically gathered threshold value. ‘off’ Stop picking threshold value. ‘on’ Start picking threshold value. ‘adaptive’ Adaptively pick threshold value, by calculating sliding window entropy.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer

        """
        return FilterNode(
            *[self],
            name="adynamicequalizer",
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
                **kwargs,
            }
        ).stream()

    def adynamicsmooth(
        self, *, sensitivity: float = None, basefreq: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.17 adynamicsmooth Apply dynamic smoothing to input audio stream. A description of the accepted options follows.

        Parameters:
        ----------
        sensitivity:
            Set an amount of sensitivity to frequency fluctations. Default is 2. Allowed range is from 0 to 1e+06.
        basefreq:
            Set a base frequency for smoothing. Default value is 22050. Allowed range is from 2 to 1e+06.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth

        """
        return FilterNode(
            *[self], name="adynamicsmooth", kwargs={"sensitivity": sensitivity, "basefreq": basefreq, **kwargs}
        ).stream()

    def aecho(
        self,
        *,
        in_gain: float = None,
        out_gain: float = None,
        delays: str = None,
        decays: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.18 aecho Apply echoing to the input audio. Echoes are reflected sound and can occur naturally amongst mountains (and sometimes large buildings) when talking or shouting; digital echo effects emulate this behaviour and are often used to help fill out the sound of a single instrument or vocal. The time difference between the original signal and the reflection is the delay, and the loudness of the reflected signal is the decay. Multiple echoes can have different delays and decays. A description of the accepted parameters follows.

        Parameters:
        ----------
        in_gain:
            Set input gain of reflected signal. Default is 0.6.
        out_gain:
            Set output gain of reflected signal. Default is 0.3.
        delays:
            Set list of time intervals in milliseconds between original signal and reflections separated by ’|’. Allowed range for each delay is (0 - 90000.0]. Default is 1000.
        decays:
            Set list of loudness of reflected signals separated by ’|’. Allowed range for each decay is (0 - 1.0]. Default is 0.5.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aecho

        """
        return FilterNode(
            *[self],
            name="aecho",
            kwargs={"in_gain": in_gain, "out_gain": out_gain, "delays": delays, "decays": decays, **kwargs}
        ).stream()

    def aemphasis(
        self, *, level_in: float, level_out: float, mode: str = None, type: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.19 aemphasis Audio emphasis filter creates or restores material directly taken from LPs or emphased CDs with different filter curves. E.g. to store music on vinyl the signal has to be altered by a filter first to even out the disadvantages of this recording medium. Once the material is played back the inverse filter has to be applied to restore the distortion of the frequency response. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input gain.
        level_out:
            Set output gain.
        mode:
            Set filter mode. For restoring material use reproduction mode, otherwise use production mode. Default is reproduction mode.
        type:
            Set filter type. Selects medium. Can be one of the following: col select Columbia. emi select EMI. bsi select BSI (78RPM). riaa select RIAA. cd select Compact Disc (CD). 50fm select 50µs (FM). 75fm select 75µs (FM). 50kf select 50µs (FM-KF). 75kf select 75µs (FM-KF).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aemphasis

        """
        return FilterNode(
            *[self],
            name="aemphasis",
            kwargs={"level_in": level_in, "level_out": level_out, "mode": mode, "type": type, **kwargs}
        ).stream()

    def aeval(self, *, exprs: str, channel_layout: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.20 aeval Modify an audio signal according to the specified expressions. This filter accepts one or more expressions (one for each channel), which are evaluated and used to modify a corresponding audio signal. It accepts the following parameters: Each expression in exprs can contain the following constants and functions: Note: this filter is slow. For faster processing you should use a dedicated filter.

        Parameters:
        ----------
        exprs:
            Set the ’|’-separated expressions list for each separate channel. If the number of input channels is greater than the number of expressions, the last specified expression is used for the remaining output channels.
        channel_layout:
            Set output channel layout. If not specified, the channel layout is specified by the number of expressions. If set to ‘same’, it will use by default the same input channel layout.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aeval

        """
        return FilterNode(
            *[self], name="aeval", kwargs={"exprs": exprs, "channel_layout": channel_layout, **kwargs}
        ).stream()

    def aexciter(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        amount: float = None,
        drive: float = None,
        blend: float = None,
        freq: float = None,
        ceil: float,
        listen: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.21 aexciter An exciter is used to produce high sound that is not present in the original signal. This is done by creating harmonic distortions of the signal which are restricted in range and added to the original signal. An Exciter raises the upper end of an audio signal without simply raising the higher frequencies like an equalizer would do to create a more "crisp" or "brilliant" sound. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input level prior processing of signal. Allowed range is from 0 to 64. Default value is 1.
        level_out:
            Set output level after processing of signal. Allowed range is from 0 to 64. Default value is 1.
        amount:
            Set the amount of harmonics added to original signal. Allowed range is from 0 to 64. Default value is 1.
        drive:
            Set the amount of newly created harmonics. Allowed range is from 0.1 to 10. Default value is 8.5.
        blend:
            Set the octave of newly created harmonics. Allowed range is from -10 to 10. Default value is 0.
        freq:
            Set the lower frequency limit of producing harmonics in Hz. Allowed range is from 2000 to 12000 Hz. Default is 7500 Hz.
        ceil:
            Set the upper frequency limit of producing harmonics. Allowed range is from 9999 to 20000 Hz. If value is lower than 10000 Hz no limit is applied.
        listen:
            Mute the original signal and output only added harmonics. By default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aexciter

        """
        return FilterNode(
            *[self],
            name="aexciter",
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "amount": amount,
                "drive": drive,
                "blend": blend,
                "freq": freq,
                "ceil": ceil,
                "listen": listen,
                **kwargs,
            }
        ).stream()

    def afade(
        self,
        *,
        type: str = None,
        start_sample: int = None,
        nb_samples: int = None,
        start_time: str = None,
        duration: str,
        curve: str = None,
        silence: float = None,
        unity: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.22 afade Apply fade-in/out effect to input audio. A description of the accepted parameters follows.

        Parameters:
        ----------
        type:
            Specify the effect type, can be either in for fade-in, or out for a fade-out effect. Default is in.
        start_sample:
            Specify the number of the start sample for starting to apply the fade effect. Default is 0.
        nb_samples:
            Specify the number of samples for which the fade effect has to last. At the end of the fade-in effect the output audio will have the same volume as the input audio, at the end of the fade-out transition the output audio will be silence. Default is 44100.
        start_time:
            Specify the start time of the fade effect. Default is 0. The value must be specified as a time duration; see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. If set this option is used instead of start_sample.
        duration:
            Specify the duration of the fade effect. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. At the end of the fade-in effect the output audio will have the same volume as the input audio, at the end of the fade-out transition the output audio will be silence. By default the duration is determined by nb_samples. If set this option is used instead of nb_samples.
        curve:
            Set curve for fade transition. It accepts the following values: tri select triangular, linear slope (default) qsin select quarter of sine wave hsin select half of sine wave esin select exponential sine wave log select logarithmic ipar select inverted parabola qua select quadratic cub select cubic squ select square root cbr select cubic root par select parabola exp select exponential iqsin select inverted quarter of sine wave ihsin select inverted half of sine wave dese select double-exponential seat desi select double-exponential sigmoid losi select logistic sigmoid sinc select sine cardinal function isinc select inverted sine cardinal function quat select quartic quatr select quartic root qsin2 select squared quarter of sine wave hsin2 select squared half of sine wave nofade no fade applied
        silence:
            Set the initial gain for fade-in or final gain for fade-out. Default value is 0.0.
        unity:
            Set the initial gain for fade-out or final gain for fade-in. Default value is 1.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afade

        """
        return FilterNode(
            *[self],
            name="afade",
            kwargs={
                "type": type,
                "start_sample": start_sample,
                "nb_samples": nb_samples,
                "start_time": start_time,
                "duration": duration,
                "curve": curve,
                "silence": silence,
                "unity": unity,
                **kwargs,
            }
        ).stream()

    def afftdn(
        self,
        *,
        noise_reduction: float = None,
        noise_floor: float = None,
        noise_type: str = None,
        band_noise: str,
        residual_floor: float = None,
        track_noise: bool = None,
        track_residual: bool = None,
        output_mode: str = None,
        adaptivity: float = None,
        floor_offset: float = None,
        noise_link: str = None,
        band_multiplier: float = None,
        sample_noise: str = None,
        gain_smooth: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.23 afftdn Denoise audio samples with FFT. A description of the accepted parameters follows.

        Parameters:
        ----------
        noise_reduction:
            Set the noise reduction in dB, allowed range is 0.01 to 97. Default value is 12 dB.
        noise_floor:
            Set the noise floor in dB, allowed range is -80 to -20. Default value is -50 dB.
        noise_type:
            Set the noise type. It accepts the following values: white, w Select white noise. vinyl, v Select vinyl noise. shellac, s Select shellac noise. custom, c Select custom noise, defined in bn option. Default value is white noise.
        band_noise:
            Set custom band noise profile for every one of 15 bands. Bands are separated by ’ ’ or ’|’.
        residual_floor:
            Set the residual floor in dB, allowed range is -80 to -20. Default value is -38 dB.
        track_noise:
            Enable noise floor tracking. By default is disabled. With this enabled, noise floor is automatically adjusted.
        track_residual:
            Enable residual tracking. By default is disabled.
        output_mode:
            Set the output mode. It accepts the following values: input, i Pass input unchanged. output, o Pass noise filtered out. noise, n Pass only noise. Default value is output.
        adaptivity:
            Set the adaptivity factor, used how fast to adapt gains adjustments per each frequency bin. Value 0 enables instant adaptation, while higher values react much slower. Allowed range is from 0 to 1. Default value is 0.5.
        floor_offset:
            Set the noise floor offset factor. This option is used to adjust offset applied to measured noise floor. It is only effective when noise floor tracking is enabled. Allowed range is from -2.0 to 2.0. Default value is 1.0.
        noise_link:
            Set the noise link used for multichannel audio. It accepts the following values: none Use unchanged channel’s noise floor. min Use measured min noise floor of all channels. max Use measured max noise floor of all channels. average Use measured average noise floor of all channels. Default value is min.
        band_multiplier:
            Set the band multiplier factor, used how much to spread bands across frequency bins. Allowed range is from 0.2 to 5. Default value is 1.25.
        sample_noise:
            Toggle capturing and measurement of noise profile from input audio. It accepts the following values: start, begin Start sample noise capture. stop, end Stop sample noise capture and measure new noise band profile. Default value is none.
        gain_smooth:
            Set gain smooth spatial radius, used to smooth gains applied to each frequency bin. Useful to reduce random music noise artefacts. Higher values increases smoothing of gains. Allowed range is from 0 to 50. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftdn

        """
        return FilterNode(
            *[self],
            name="afftdn",
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
                **kwargs,
            }
        ).stream()

    def afftfilt(
        self,
        *,
        real: str = None,
        imag: str = None,
        win_size: int = None,
        win_func: str = None,
        overlap: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.24 afftfilt Apply arbitrary expressions to samples in frequency domain.

        Parameters:
        ----------
        real:
            Set frequency domain real expression for each separate channel separated by ’|’. Default is "re". If the number of input channels is greater than the number of expressions, the last specified expression is used for the remaining output channels.
        imag:
            Set frequency domain imaginary expression for each separate channel separated by ’|’. Default is "im". Each expression in real and imag can contain the following constants and functions: sr sample rate b current frequency bin number nb number of available bins ch channel number of the current expression chs number of channels pts current frame pts re current real part of frequency bin of current channel im current imaginary part of frequency bin of current channel real(b, ch) Return the value of real part of frequency bin at location (bin,channel) imag(b, ch) Return the value of imaginary part of frequency bin at location (bin,channel)
        win_size:
            Set window size. Allowed range is from 16 to 131072. Default is 4096
        win_func:
            Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        overlap:
            Set window overlap. If set to 1, the recommended overlap for selected window function will be picked. Default is 0.75.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afftfilt

        """
        return FilterNode(
            *[self],
            name="afftfilt",
            kwargs={
                "real": real,
                "imag": imag,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                **kwargs,
            }
        ).stream()

    def afifo(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.96 fifo, afifo Buffer input images and send them when they are requested. It is mainly useful when auto-inserted by the libavfilter framework. It does not take parameters.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fifo_002c-afifo

        """
        return FilterNode(*[self], name="afifo", kwargs={**kwargs}).stream()

    def afir(
        self,
        *,
        dry: float,
        wet: float,
        length: float,
        irnorm: float,
        irlink: bool,
        irgain: float,
        irfmt: str,
        maxir: float,
        minp: float,
        maxp: float,
        nbirs: float,
        ir: float,
        precision: str = None,
        irload: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.25 afir Apply an arbitrary Finite Impulse Response filter. This filter is designed for applying long FIR filters, up to 60 seconds long. It can be used as component for digital crossover filters, room equalization, cross talk cancellation, wavefield synthesis, auralization, ambiophonics, ambisonics and spatialization. This filter uses the streams higher than first one as FIR coefficients. If the non-first stream holds a single channel, it will be used for all input channels in the first stream, otherwise the number of channels in the non-first stream must be same as the number of channels in the first stream. It accepts the following parameters:

        Parameters:
        ----------
        dry:
            Set dry gain. This sets input gain.
        wet:
            Set wet gain. This sets final output gain.
        length:
            Set Impulse Response filter length. Default is 1, which means whole IR is processed.
        irnorm:
            Set norm to be applied to IR coefficients before filtering. Allowed range is from -1 to 2. IR coefficients are normalized with calculated vector norm set by this option. For negative values, no norm is calculated, and IR coefficients are not modified at all. Default is 1.
        irlink:
            For multichannel IR if this option is set to true, all IR channels will be normalized with maximal measured gain of all IR channels coefficients as set by irnorm option. When disabled, all IR coefficients in each IR channel will be normalized independently. Default is true.
        irgain:
            Set gain to be applied to IR coefficients before filtering. Allowed range is 0 to 1. This gain is applied after any gain applied with irnorm option.
        irfmt:
            Set format of IR stream. Can be mono or input. Default is input.
        maxir:
            Set max allowed Impulse Response filter duration in seconds. Default is 30 seconds. Allowed range is 0.1 to 60 seconds.
        minp:
            Set minimal partition size used for convolution. Default is 8192. Allowed range is from 1 to 65536. Lower values decreases latency at cost of higher CPU usage.
        maxp:
            Set maximal partition size used for convolution. Default is 8192. Allowed range is from 8 to 65536. Lower values may increase CPU usage.
        nbirs:
            Set number of input impulse responses streams which will be switchable at runtime. Allowed range is from 1 to 32. Default is 1.
        ir:
            Set IR stream which will be used for convolution, starting from 0, should always be lower than supplied value by nbirs option. Default is 0. This option can be changed at runtime via commands.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format. Default value is auto.
        irload:
            Set when to load IR stream. Can be init or access. First one load and prepares all IRs on initialization, second one once on first access of specific IR. Default is init.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afir

        """
        return FilterNode(
            *[self],
            name="afir",
            kwargs={
                "dry": dry,
                "wet": wet,
                "length": length,
                "irnorm": irnorm,
                "irlink": irlink,
                "irgain": irgain,
                "irfmt": irfmt,
                "maxir": maxir,
                "minp": minp,
                "maxp": maxp,
                "nbirs": nbirs,
                "ir": ir,
                "precision": precision,
                "irload": irload,
                **kwargs,
            }
        ).stream()

    def aformat(
        self, *, sample_fmts: str, sample_rates: str, channel_layouts: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.26 aformat Set output format constraints for the input audio. The framework will negotiate the most appropriate format to minimize conversions. It accepts the following parameters: If a parameter is omitted, all values are allowed. Force the output to either unsigned 8-bit or signed 16-bit stereo aformat=sample_fmts=u8|s16:channel_layouts=stereo

        Parameters:
        ----------
        sample_fmts:
            A ’|’-separated list of requested sample formats.
        sample_rates:
            A ’|’-separated list of requested sample rates.
        channel_layouts:
            A ’|’-separated list of requested channel layouts. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aformat

        """
        return FilterNode(
            *[self],
            name="aformat",
            kwargs={
                "sample_fmts": sample_fmts,
                "sample_rates": sample_rates,
                "channel_layouts": channel_layouts,
                **kwargs,
            }
        ).stream()

    def afreqshift(
        self, *, shift: float = None, level: float = None, order: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.27 afreqshift Apply frequency shift to input audio samples. The filter accepts the following options:

        Parameters:
        ----------
        shift:
            Specify frequency shift. Allowed range is -INT_MAX to INT_MAX. Default value is 0.0.
        level:
            Set output gain applied to final output. Allowed range is from 0.0 to 1.0. Default value is 1.0.
        order:
            Set filter order used for filtering. Allowed range is from 1 to 16. Default value is 8.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afreqshift

        """
        return FilterNode(
            *[self], name="afreqshift", kwargs={"shift": shift, "level": level, "order": order, **kwargs}
        ).stream()

    def afwtdn(
        self,
        *,
        sigma: float = None,
        levels: int = None,
        wavet: str,
        percent: int = None,
        profile: bool = None,
        adaptive: bool = None,
        samples: int = None,
        softness: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.28 afwtdn Reduce broadband noise from input samples using Wavelets. A description of the accepted options follows.

        Parameters:
        ----------
        sigma:
            Set the noise sigma, allowed range is from 0 to 1. Default value is 0. This option controls strength of denoising applied to input samples. Most useful way to set this option is via decibels, eg. -45dB.
        levels:
            Set the number of wavelet levels of decomposition. Allowed range is from 1 to 12. Default value is 10. Setting this too low make denoising performance very poor.
        wavet:
            Set wavelet type for decomposition of input frame. They are sorted by number of coefficients, from lowest to highest. More coefficients means worse filtering speed, but overall better quality. Available wavelets are: ‘sym2’ ‘sym4’ ‘rbior68’ ‘deb10’ ‘sym10’ ‘coif5’ ‘bl3’
        percent:
            Set percent of full denoising. Allowed range is from 0 to 100 percent. Default value is 85 percent or partial denoising.
        profile:
            If enabled, first input frame will be used as noise profile. If first frame samples contain non-noise performance will be very poor.
        adaptive:
            If enabled, input frames are analyzed for presence of noise. If noise is detected with high possibility then input frame profile will be used for processing following frames, until new noise frame is detected.
        samples:
            Set size of single frame in number of samples. Allowed range is from 512 to 65536. Default frame size is 8192 samples.
        softness:
            Set softness applied inside thresholding function. Allowed range is from 0 to 10. Default softness is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#afwtdn

        """
        return FilterNode(
            *[self],
            name="afwtdn",
            kwargs={
                "sigma": sigma,
                "levels": levels,
                "wavet": wavet,
                "percent": percent,
                "profile": profile,
                "adaptive": adaptive,
                "samples": samples,
                "softness": softness,
                **kwargs,
            }
        ).stream()

    def agate(
        self,
        *,
        level_in: float = None,
        mode: str = None,
        range: float = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        detection: str = None,
        link: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.29 agate A gate is mainly used to reduce lower parts of a signal. This kind of signal processing reduces disturbing noise between useful signals. Gating is done by detecting the volume below a chosen level threshold and dividing it by the factor set with ratio. The bottom of the noise floor is set via range. Because an exact manipulation of the signal would cause distortion of the waveform the reduction can be levelled over time. This is done by setting attack and release. attack determines how long the signal has to fall below the threshold before any reduction will occur and release sets the time the signal has to rise above the threshold to reduce the reduction again. Shorter signals than the chosen attack time will be left untouched.

        Parameters:
        ----------
        level_in:
            Set input level before filtering. Default is 1. Allowed range is from 0.015625 to 64.
        mode:
            Set the mode of operation. Can be upward or downward. Default is downward. If set to upward mode, higher parts of signal will be amplified, expanding dynamic range in upward direction. Otherwise, in case of downward lower parts of signal will be reduced.
        range:
            Set the level of gain reduction when the signal is below the threshold. Default is 0.06125. Allowed range is from 0 to 1. Setting this to 0 disables reduction and then filter behaves like expander.
        threshold:
            If a signal rises above this level the gain reduction is released. Default is 0.125. Allowed range is from 0 to 1.
        ratio:
            Set a ratio by which the signal is reduced. Default is 2. Allowed range is from 1 to 9000.
        attack:
            Amount of milliseconds the signal has to rise above the threshold before gain reduction stops. Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
        release:
            Amount of milliseconds the signal has to fall below the threshold before the reduction is increased again. Default is 250 milliseconds. Allowed range is from 0.01 to 9000.
        makeup:
            Set amount of amplification of signal after processing. Default is 1. Allowed range is from 1 to 64.
        knee:
            Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.828427125. Allowed range is from 1 to 8.
        detection:
            Choose if exact signal should be taken for detection or an RMS like one. Default is rms. Can be peak or rms.
        link:
            Choose if the average level between all channels or the louder channel affects the reduction. Default is average. Can be average or maximum.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#agate

        """
        return FilterNode(
            *[self],
            name="agate",
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
                **kwargs,
            }
        ).stream()

    def aiir(
        self,
        *,
        zeros: str,
        poles: str,
        gains: str,
        dry_gain: float,
        wet_gain: float,
        format: str,
        process: str,
        precision: str,
        normalize: bool = None,
        mix: float = None,
        response: bool = None,
        channel: int = None,
        size: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.30 aiir Apply an arbitrary Infinite Impulse Response filter. It accepts the following parameters: Coefficients in tf and sf format are separated by spaces and are in ascending order. Coefficients in zp format are separated by spaces and order of coefficients doesn’t matter. Coefficients in zp format are complex numbers with i imaginary unit. Different coefficients and gains can be provided for every channel, in such case use ’|’ to separate coefficients or gains. Last provided coefficients will be used for all remaining channels.

        Parameters:
        ----------
        zeros:
            Set B/numerator/zeros/reflection coefficients.
        poles:
            Set A/denominator/poles/ladder coefficients.
        gains:
            Set channels gains.
        dry_gain:
            Set input gain.
        wet_gain:
            Set output gain.
        format:
            Set coefficients format. ‘ll’ lattice-ladder function ‘sf’ analog transfer function ‘tf’ digital transfer function ‘zp’ Z-plane zeros/poles, cartesian (default) ‘pr’ Z-plane zeros/poles, polar radians ‘pd’ Z-plane zeros/poles, polar degrees ‘sp’ S-plane zeros/poles
        process:
            Set type of processing. ‘d’ direct processing ‘s’ serial processing ‘p’ parallel processing
        precision:
            Set filtering precision. ‘dbl’ double-precision floating-point (default) ‘flt’ single-precision floating-point ‘i32’ 32-bit integers ‘i16’ 16-bit integers
        normalize:
            Normalize filter coefficients, by default is enabled. Enabling it will normalize magnitude response at DC to 0dB.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        response:
            Show IR frequency response, magnitude(magenta), phase(green) and group delay(yellow) in additional video stream. By default it is disabled.
        channel:
            Set for which IR channel to display frequency response. By default is first channel displayed. This option is used only when response is enabled.
        size:
            Set video stream size. This option is used only when response is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aiir

        """
        return FilterNode(
            *[self],
            name="aiir",
            kwargs={
                "zeros": zeros,
                "poles": poles,
                "gains": gains,
                "dry_gain": dry_gain,
                "wet_gain": wet_gain,
                "format": format,
                "process": process,
                "precision": precision,
                "normalize": normalize,
                "mix": mix,
                "response": response,
                "channel": channel,
                "size": size,
                **kwargs,
            }
        ).stream()

    def aintegral(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.14 aderivative, aintegral Compute derivative/integral of audio stream. Applying both filters one after another produces original audio.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral

        """
        return FilterNode(*[self], name="aintegral", kwargs={**kwargs}).stream()

    def alimiter(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        limit: float = None,
        attack: float = None,
        release: float = None,
        asc: bool,
        asc_level: float,
        level: bool = None,
        latency: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.31 alimiter The limiter prevents an input signal from rising over a desired threshold. This limiter uses lookahead technology to prevent your signal from distorting. It means that there is a small delay after the signal is processed. Keep in mind that the delay it produces is the attack time you set. The filter accepts the following options: Depending on picked setting it is recommended to upsample input 2x or 4x times with aresample before applying this filter.

        Parameters:
        ----------
        level_in:
            Set input gain. Default is 1.
        level_out:
            Set output gain. Default is 1.
        limit:
            Don’t let signals above this level pass the limiter. Default is 1.
        attack:
            The limiter will reach its attenuation level in this amount of time in milliseconds. Default is 5 milliseconds.
        release:
            Come back from limiting to attenuation 1.0 in this amount of milliseconds. Default is 50 milliseconds.
        asc:
            When gain reduction is always needed ASC takes care of releasing to an average reduction level rather than reaching a reduction of 0 in the release time.
        asc_level:
            Select how much the release time is affected by ASC, 0 means nearly no changes in release time while 1 produces higher release times.
        level:
            Auto level output signal. Default is enabled. This normalizes audio back to 0dB if enabled.
        latency:
            Compensate the delay introduced by using the lookahead buffer set with attack parameter. Also flush the valid audio data in the lookahead buffer when the stream hits EOF.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#alimiter

        """
        return FilterNode(
            *[self],
            name="alimiter",
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
                **kwargs,
            }
        ).stream()

    def allpass(
        self,
        *,
        frequency: float,
        width_type: str,
        width: float,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        order: int = None,
        transform: str,
        precision: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.32 allpass Apply a two-pole all-pass filter with central frequency (in Hz) frequency, and filter-width width. An all-pass filter changes the audio’s frequency to phase relationship without changing its frequency to amplitude relationship. The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set frequency in Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        order:
            Set the filter order, can be 1 or 2. Default is 2.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#allpass

        """
        return FilterNode(
            *[self],
            name="allpass",
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
                **kwargs,
            }
        ).stream()

    def aloop(
        self, *, loop: int = None, size: int = None, start: int = None, time: float, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.33 aloop Loop audio samples. The filter accepts the following options:

        Parameters:
        ----------
        loop:
            Set the number of loops. Setting this value to -1 will result in infinite loops. Default is 0.
        size:
            Set maximal number of samples. Default is 0.
        start:
            Set first sample of loop. Default is 0.
        time:
            Set the time of loop start in seconds. Only used if option named start is set to -1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aloop

        """
        return FilterNode(
            *[self], name="aloop", kwargs={"loop": loop, "size": size, "start": start, "time": time, **kwargs}
        ).stream()

    def alphaextract(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.2 alphaextract Extract the alpha component from the input as a grayscale video. This is especially useful with the alphamerge filter.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#alphaextract

        """
        return FilterNode(*[self], name="alphaextract", kwargs={**kwargs}).stream()

    def alphamerge(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.3 alphamerge Add or replace the alpha component of the primary input with the grayscale value of a second input. This is intended for use with alphaextract to allow the transmission or storage of frame sequences that have alpha in a format that doesn’t support an alpha channel. For example, to reconstruct full frames from a normal YUV-encoded video and a separate video created with alphaextract, you might use: movie=in_alpha.mkv [alpha]; [in][alpha] alphamerge [out]

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#alphamerge

        """
        return FilterNode(*[self], name="alphamerge", kwargs={**kwargs}).stream()

    def amerge(self, *, inputs: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.34 amerge Merge two or more audio streams into a single multi-channel stream. The filter accepts the following options: If the channel layouts of the inputs are disjoint, and therefore compatible, the channel layout of the output will be set accordingly and the channels will be reordered as necessary. If the channel layouts of the inputs are not disjoint, the output will have all the channels of the first input then all the channels of the second input, in that order, and the channel layout of the output will be the default value corresponding to the total number of channels. For example, if the first input is in 2.1 (FL+FR+LF) and the second input is FC+BL+BR, then the output will be in 5.1, with the channels in the following order: a1, a2, b1, a3, b2, b3 (a1 is the first channel of the first input, b1 is the first channel of the second input). On the other hand, if both input are in stereo, the output channels will be in the default order: a1, a2, b1, b2, and the channel layout will be arbitrarily set to 4.0, which may or may not be the expected value. All inputs must have the same sample rate, and format. If inputs do not have the same duration, the output will stop with the shortest.

        Parameters:
        ----------
        inputs:
            Set the number of inputs. Default is 2.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amerge

        """
        return FilterNode(*[self], name="amerge", kwargs={"inputs": inputs, **kwargs}).stream()

    def amix(
        self,
        *,
        inputs: int = None,
        duration: str = None,
        dropout_transition: float = None,
        weights: str,
        normalize: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.35 amix Mixes multiple audio inputs into a single output. Note that this filter only supports float samples (the amerge and pan audio filters support many formats). If the amix input has integer samples then aresample will be automatically inserted to perform the conversion to float samples. It accepts the following parameters:

        Parameters:
        ----------
        inputs:
            The number of inputs. If unspecified, it defaults to 2.
        duration:
            How to determine the end-of-stream. longest The duration of the longest input. (default) shortest The duration of the shortest input. first The duration of the first input.
        dropout_transition:
            The transition time, in seconds, for volume renormalization when an input stream ends. The default value is 2 seconds.
        weights:
            Specify weight of each input audio stream as a sequence of numbers separated by a space. If fewer weights are specified compared to number of inputs, the last weight is assigned to the remaining inputs. Default weight for each input is 1.
        normalize:
            Always scale inputs instead of only doing summation of samples. Beware of heavy clipping if inputs are not normalized prior or after filtering by this filter if this option is disabled. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amix

        """
        return FilterNode(
            *[self],
            name="amix",
            kwargs={
                "inputs": inputs,
                "duration": duration,
                "dropout_transition": dropout_transition,
                "weights": weights,
                "normalize": normalize,
                **kwargs,
            }
        ).stream()

    def amplify(
        self,
        *,
        radius: int = None,
        factor: int = None,
        threshold: int = None,
        tolerance: int = None,
        low: int = None,
        high: int = None,
        planes: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.4 amplify Amplify differences between current pixel and pixels of adjacent frames in same pixel location. This filter accepts the following options:

        Parameters:
        ----------
        radius:
            Set frame radius. Default is 2. Allowed range is from 1 to 63. For example radius of 3 will instruct filter to calculate average of 7 frames.
        factor:
            Set factor to amplify difference. Default is 2. Allowed range is from 0 to 65535.
        threshold:
            Set threshold for difference amplification. Any difference greater or equal to this value will not alter source pixel. Default is 10. Allowed range is from 0 to 65535.
        tolerance:
            Set tolerance for difference amplification. Any difference lower to this value will not alter source pixel. Default is 0. Allowed range is from 0 to 65535.
        low:
            Set lower limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will decrease source pixel value.
        high:
            Set high limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535. This option controls maximum possible value that will increase source pixel value.
        planes:
            Set which planes to filter. Default is all. Allowed range is from 0 to 15.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amplify

        """
        return FilterNode(
            *[self],
            name="amplify",
            kwargs={
                "radius": radius,
                "factor": factor,
                "threshold": threshold,
                "tolerance": tolerance,
                "low": low,
                "high": high,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def amultiply(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.36 amultiply Multiply first audio stream with second audio stream and store result in output audio stream. Multiplication is done by multiplying each sample from first stream with sample at same position from second stream. With this element-wise multiplication one can create amplitude fades and amplitude modulations.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#amultiply

        """
        return FilterNode(*[self], name="amultiply", kwargs={**kwargs}).stream()

    def anequalizer(
        self, *, params: str, curves: bool, size: str, mgain: float, fscale: str, colors: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.37 anequalizer High-order parametric multiband equalizer for each channel. It accepts the following parameters:

        Parameters:
        ----------
        params:
            This option string is in format: "cchn f=cf w=w g=g t=f | ..." Each equalizer band is separated by ’|’. chn Set channel number to which equalization will be applied. If input doesn’t have that channel the entry is ignored. f Set central frequency for band. If input doesn’t have that frequency the entry is ignored. w Set band width in Hertz. g Set band gain in dB. t Set filter type for band, optional, can be: ‘0’ Butterworth, this is default. ‘1’ Chebyshev type 1. ‘2’ Chebyshev type 2.
        curves:
            With this option activated frequency response of anequalizer is displayed in video stream.
        size:
            Set video stream size. Only useful if curves option is activated.
        mgain:
            Set max gain that will be displayed. Only useful if curves option is activated. Setting this to a reasonable value makes it possible to display gain which is derived from neighbour bands which are too close to each other and thus produce higher gain when both are activated.
        fscale:
            Set frequency scale used to draw frequency response in video output. Can be linear or logarithmic. Default is logarithmic.
        colors:
            Set color for each channel curve which is going to be displayed in video stream. This is list of color names separated by space or by ’|’. Unrecognised or missing colors will be replaced by white color.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anequalizer

        """
        return FilterNode(
            *[self],
            name="anequalizer",
            kwargs={
                "params": params,
                "curves": curves,
                "size": size,
                "mgain": mgain,
                "fscale": fscale,
                "colors": colors,
                **kwargs,
            }
        ).stream()

    def anlmdn(
        self,
        *,
        strength: float = None,
        patch: int = None,
        research: int = None,
        output: str = None,
        smooth: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.38 anlmdn Reduce broadband noise in audio samples using Non-Local Means algorithm. Each sample is adjusted by looking for other samples with similar contexts. This context similarity is defined by comparing their surrounding patches of size p. Patches are searched in an area of r around the sample. The filter accepts the following options:

        Parameters:
        ----------
        strength:
            Set denoising strength. Allowed range is from 0.00001 to 10000. Default value is 0.00001.
        patch:
            Set patch radius duration. Allowed range is from 1 to 100 milliseconds. Default value is 2 milliseconds.
        research:
            Set research radius duration. Allowed range is from 2 to 300 milliseconds. Default value is 6 milliseconds.
        output:
            Set the output mode. It accepts the following values: i Pass input unchanged. o Pass noise filtered out. n Pass only noise. Default value is o.
        smooth:
            Set smooth factor. Default value is 11. Allowed range is from 1 to 1000.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmdn

        """
        return FilterNode(
            *[self],
            name="anlmdn",
            kwargs={
                "strength": strength,
                "patch": patch,
                "research": research,
                "output": output,
                "smooth": smooth,
                **kwargs,
            }
        ).stream()

    def anlmf(
        self,
        *,
        order: int,
        mu: float,
        eps: float,
        leakage: float,
        out_mode: str = None,
        precision: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.39 anlmf, anlms Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream. This adaptive filter is used to mimic a desired filter by finding the filter coefficients that relate to producing the least mean square of the error signal (difference between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream). A description of the accepted options follows.

        Parameters:
        ----------
        order:
            Set filter order.
        mu:
            Set filter mu.
        eps:
            Set the filter eps.
        leakage:
            Set the filter leakage.
        out_mode:
            It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

        """
        return FilterNode(
            *[self],
            name="anlmf",
            kwargs={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
                **kwargs,
            }
        ).stream()

    def anlms(
        self,
        *,
        order: int,
        mu: float,
        eps: float,
        leakage: float,
        out_mode: str = None,
        precision: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.39 anlmf, anlms Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream. This adaptive filter is used to mimic a desired filter by finding the filter coefficients that relate to producing the least mean square of the error signal (difference between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream). A description of the accepted options follows.

        Parameters:
        ----------
        order:
            Set filter order.
        mu:
            Set filter mu.
        eps:
            Set the filter eps.
        leakage:
            Set the filter leakage.
        out_mode:
            It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms

        """
        return FilterNode(
            *[self],
            name="anlms",
            kwargs={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
                **kwargs,
            }
        ).stream()

    def anull(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.40 anull Pass the audio source unchanged to the output.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#anull

        """
        return FilterNode(*[self], name="anull", kwargs={**kwargs}).stream()

    def apad(
        self,
        *,
        packet_size: int = None,
        pad_len: int,
        whole_len: int,
        pad_dur: str,
        whole_dur: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.41 apad Pad the end of an audio stream with silence. This can be used together with ffmpeg -shortest to extend audio streams to the same length as the video stream. A description of the accepted options follows. If neither the pad_len nor the whole_len nor pad_dur nor whole_dur option is set, the filter will add silence to the end of the input stream indefinitely. Note that for ffmpeg 4.4 and earlier a zero pad_dur or whole_dur also caused the filter to add silence indefinitely.

        Parameters:
        ----------
        packet_size:
            Set silence packet size. Default value is 4096.
        pad_len:
            Set the number of samples of silence to add to the end. After the value is reached, the stream is terminated. This option is mutually exclusive with whole_len.
        whole_len:
            Set the minimum total number of samples in the output audio stream. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with pad_len.
        pad_dur:
            Specify the duration of samples of silence to add. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value.
        whole_dur:
            Specify the minimum total duration in the output audio stream. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Used only if set to non-negative value. If the value is longer than the input audio length, silence is added to the end, until the value is reached. This option is mutually exclusive with pad_dur



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apad

        """
        return FilterNode(
            *[self],
            name="apad",
            kwargs={
                "packet_size": packet_size,
                "pad_len": pad_len,
                "whole_len": whole_len,
                "pad_dur": pad_dur,
                "whole_dur": whole_dur,
                **kwargs,
            }
        ).stream()

    def aphaser(
        self,
        *,
        in_gain: float = None,
        out_gain: float = None,
        delay: float = None,
        decay: float = None,
        speed: float = None,
        type: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.42 aphaser Add a phasing effect to the input audio. A phaser filter creates series of peaks and troughs in the frequency spectrum. The position of the peaks and troughs are modulated so that they vary over time, creating a sweeping effect. A description of the accepted parameters follows.

        Parameters:
        ----------
        in_gain:
            Set input gain. Default is 0.4.
        out_gain:
            Set output gain. Default is 0.74
        delay:
            Set delay in milliseconds. Default is 3.0.
        decay:
            Set decay. Default is 0.4.
        speed:
            Set modulation speed in Hz. Default is 0.5.
        type:
            Set modulation type. Default is triangular. It accepts the following values: ‘triangular, t’ ‘sinusoidal, s’



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaser

        """
        return FilterNode(
            *[self],
            name="aphaser",
            kwargs={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delay": delay,
                "decay": decay,
                "speed": speed,
                "type": type,
                **kwargs,
            }
        ).stream()

    def aphaseshift(
        self, *, shift: float = None, level: float = None, order: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.43 aphaseshift Apply phase shift to input audio samples. The filter accepts the following options:

        Parameters:
        ----------
        shift:
            Specify phase shift. Allowed range is from -1.0 to 1.0. Default value is 0.0.
        level:
            Set output gain applied to final output. Allowed range is from 0.0 to 1.0. Default value is 1.0.
        order:
            Set filter order used for filtering. Allowed range is from 1 to 16. Default value is 8.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaseshift

        """
        return FilterNode(
            *[self], name="aphaseshift", kwargs={"shift": shift, "level": level, "order": order, **kwargs}
        ).stream()

    def apsnr(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.44 apsnr Measure Audio Peak Signal-to-Noise Ratio. This filter takes two audio streams for input, and outputs first audio stream. Results are in dB per channel at end of either input.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apsnr

        """
        return FilterNode(*[self], name="apsnr", kwargs={**kwargs}).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.45 apsyclip Apply Psychoacoustic clipper to input audio stream. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input gain. By default it is 1. Range is [0.015625 - 64].
        level_out:
            Set output gain. By default it is 1. Range is [0.015625 - 64].
        clip:
            Set the clipping start value. Default value is 0dBFS or 1.
        diff:
            Output only difference samples, useful to hear introduced distortions. By default is disabled.
        adaptive:
            Set strength of adaptive distortion applied. Default value is 0.5. Allowed range is from 0 to 1.
        iterations:
            Set number of iterations of psychoacoustic clipper. Allowed range is from 1 to 20. Default value is 10.
        level:
            Auto level output signal. Default is disabled. This normalizes audio back to 0dBFS if enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apsyclip

        """
        return FilterNode(
            *[self],
            name="apsyclip",
            kwargs={
                "level_in": level_in,
                "level_out": level_out,
                "clip": clip,
                "diff": diff,
                "adaptive": adaptive,
                "iterations": iterations,
                "level": level,
                **kwargs,
            }
        ).stream()

    def apulsator(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        mode: str = None,
        amount: float,
        offset_l: float = None,
        offset_r: float = None,
        width: float = None,
        timing: str = None,
        bpm: float = None,
        ms: float = None,
        hz: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.46 apulsator Audio pulsator is something between an autopanner and a tremolo. But it can produce funny stereo effects as well. Pulsator changes the volume of the left and right channel based on a LFO (low frequency oscillator) with different waveforms and shifted phases. This filter have the ability to define an offset between left and right channel. An offset of 0 means that both LFO shapes match each other. The left and right channel are altered equally - a conventional tremolo. An offset of 50% means that the shape of the right channel is exactly shifted in phase (or moved backwards about half of the frequency) - pulsator acts as an autopanner. At 1 both curves match again. Every setting in between moves the phase shift gapless between all stages and produces some "bypassing" sounds with sine and triangle waveforms. The more you set the offset near 1 (starting from the 0.5) the faster the signal passes from the left to the right speaker. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input gain. By default it is 1. Range is [0.015625 - 64].
        level_out:
            Set output gain. By default it is 1. Range is [0.015625 - 64].
        mode:
            Set waveform shape the LFO will use. Can be one of: sine, triangle, square, sawup or sawdown. Default is sine.
        amount:
            Set modulation. Define how much of original signal is affected by the LFO.
        offset_l:
            Set left channel offset. Default is 0. Allowed range is [0 - 1].
        offset_r:
            Set right channel offset. Default is 0.5. Allowed range is [0 - 1].
        width:
            Set pulse width. Default is 1. Allowed range is [0 - 2].
        timing:
            Set possible timing mode. Can be one of: bpm, ms or hz. Default is hz.
        bpm:
            Set bpm. Default is 120. Allowed range is [30 - 300]. Only used if timing is set to bpm.
        ms:
            Set ms. Default is 500. Allowed range is [10 - 2000]. Only used if timing is set to ms.
        hz:
            Set frequency in Hz. Default is 2. Allowed range is [0.01 - 100]. Only used if timing is set to hz.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#apulsator

        """
        return FilterNode(
            *[self],
            name="apulsator",
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
                **kwargs,
            }
        ).stream()

    def aresample(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.47 aresample Resample the input audio to the specified parameters, using the libswresample library. If none are specified then the filter will automatically convert between its input and output. This filter is also able to stretch/squeeze the audio data to make it match the timestamps or to inject silence / cut out audio to make it match the timestamps, do a combination of both or do neither. The filter accepts the syntax [sample_rate:]resampler_options, where sample_rate expresses a sample rate and resampler_options is a list of key=value pairs, separated by ":". See the (ffmpeg-resampler)"Resampler Options" section in the ffmpeg-resampler(1) manual for the complete list of supported options.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aresample

        """
        return FilterNode(*[self], name="aresample", kwargs={**kwargs}).stream()

    def areverse(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.48 areverse Reverse an audio clip. Warning: This filter requires memory to buffer the entire clip, so trimming is suggested.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#areverse

        """
        return FilterNode(*[self], name="areverse", kwargs={**kwargs}).stream()

    def arls(
        self,
        *,
        order: int,
        _lambda: float,
        delta: float,
        out_mode: str = None,
        precision: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.49 arls Apply Recursive Least Squares algorithm to the first audio stream using the second audio stream. This adaptive filter is used to mimic a desired filter by recursively finding the filter coefficients that relate to producing the minimal weighted linear least squares cost function of the error signal (difference between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream). A description of the accepted options follows.

        Parameters:
        ----------
        order:
            Set the filter order.
        _lambda:
            Set the forgetting factor.
        delta:
            Set the coefficient to initialize internal covariance matrix.
        out_mode:
            Set the filter output samples. It accepts the following values: i Pass the 1st input. d Pass the 2nd input. o Pass difference between desired, 2nd input and error signal estimate. n Pass difference between input, 1st input and error signal estimate. e Pass error signal estimated samples. Default value is o.
        precision:
            Set which precision to use when processing samples. auto Auto pick internal sample format depending on other filters. float Always use single-floating point precision sample format. double Always use double-floating point precision sample format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#arls

        """
        return FilterNode(
            *[self],
            name="arls",
            kwargs={
                "order": order,
                "lambda": _lambda,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
                **kwargs,
            }
        ).stream()

    def arnndn(self, *, model: str, mix: float = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.50 arnndn Reduce noise from speech using Recurrent Neural Networks. This filter accepts the following options:

        Parameters:
        ----------
        model:
            Set train model file to load. This option is always required.
        mix:
            Set how much to mix filtered samples into final output. Allowed range is from -1 to 1. Default value is 1. Negative values are special, they set how much to keep filtered noise in the final filter output. Set this option to -1 to hear actual noise removed from input signal.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#arnndn

        """
        return FilterNode(*[self], name="arnndn", kwargs={"model": model, "mix": mix, **kwargs}).stream()

    def asdr(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.51 asdr Measure Audio Signal-to-Distortion Ratio. This filter takes two audio streams for input, and outputs first audio stream. Results are in dB per channel at end of either input.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asdr

        """
        return FilterNode(*[self], name="asdr", kwargs={**kwargs}).stream()

    def asetnsamples(self, *, nb_out_samples: int, pad: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.52 asetnsamples Set the number of samples per each output audio frame. The last output packet may contain a different number of samples, as the filter will flush all the remaining samples when the input audio signals its end. The filter accepts the following options: For example, to set the number of per-frame samples to 1234 and disable padding for the last frame, use: asetnsamples=n=1234:p=0

        Parameters:
        ----------
        nb_out_samples:
            Set the number of frames per each output audio frame. The number is intended as the number of samples per each channel. Default value is 1024.
        pad:
            If set to 1, the filter will pad the last audio frame with zeroes, so that the last frame will contain the same number of samples as the previous ones. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetnsamples

        """
        return FilterNode(
            *[self], name="asetnsamples", kwargs={"nb_out_samples": nb_out_samples, "pad": pad, **kwargs}
        ).stream()

    def asetrate(self, *, sample_rate: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.53 asetrate Set the sample rate without altering the PCM data. This will result in a change of speed and pitch. The filter accepts the following options:

        Parameters:
        ----------
        sample_rate:
            Set the output sample rate. Default is 44100 Hz.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asetrate

        """
        return FilterNode(*[self], name="asetrate", kwargs={"sample_rate": sample_rate, **kwargs}).stream()

    def ashowinfo(
        self,
        *,
        n: int,
        pts: int,
        pts_time: float,
        fmt: str,
        chlayout: str,
        rate: int,
        nb_samples: int,
        checksum: str,
        plane_checksums: list[str],
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.54 ashowinfo Show a line containing various information for each input audio frame. The input audio is not modified. The shown line contains a sequence of key/value pairs of the form key:value. The following values are shown in the output:

        Parameters:
        ----------
        n:
            The (sequential) number of the input frame, starting from 0.
        pts:
            The presentation timestamp of the input frame, in time base units; the time base depends on the filter input pad, and is usually 1/sample_rate.
        pts_time:
            The presentation timestamp of the input frame in seconds.
        fmt:
            The sample format.
        chlayout:
            The channel layout.
        rate:
            The sample rate for the audio frame.
        nb_samples:
            The number of samples (per channel) in the frame.
        checksum:
            The Adler-32 checksum (printed in hexadecimal) of the audio data. For planar audio, the data is treated as if all the planes were concatenated.
        plane_checksums:
            A list of Adler-32 checksums for each data plane.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ashowinfo

        """
        return FilterNode(
            *[self],
            name="ashowinfo",
            kwargs={
                "n": n,
                "pts": pts,
                "pts_time": pts_time,
                "fmt": fmt,
                "chlayout": chlayout,
                "rate": rate,
                "nb_samples": nb_samples,
                "checksum": checksum,
                "plane_checksums": plane_checksums,
                **kwargs,
            }
        ).stream()

    def asisdr(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.55 asisdr Measure Audio Scaled-Invariant Signal-to-Distortion Ratio. This filter takes two audio streams for input, and outputs first audio stream. Results are in dB per channel at end of either input.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asisdr

        """
        return FilterNode(*[self], name="asisdr", kwargs={**kwargs}).stream()

    def asoftclip(
        self,
        *,
        type: str,
        threshold: float = None,
        output: float = None,
        param: float,
        oversample: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.56 asoftclip Apply audio soft clipping. Soft clipping is a type of distortion effect where the amplitude of a signal is saturated along a smooth curve, rather than the abrupt shape of hard-clipping. This filter accepts the following options:

        Parameters:
        ----------
        type:
            Set type of soft-clipping. It accepts the following values: hard tanh atan cubic exp alg quintic sin erf
        threshold:
            Set threshold from where to start clipping. Default value is 0dB or 1.
        output:
            Set gain applied to output. Default value is 0dB or 1.
        param:
            Set additional parameter which controls sigmoid function.
        oversample:
            Set oversampling factor.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asoftclip

        """
        return FilterNode(
            *[self],
            name="asoftclip",
            kwargs={
                "type": type,
                "threshold": threshold,
                "output": output,
                "param": param,
                "oversample": oversample,
                **kwargs,
            }
        ).stream()

    def aspectralstats(
        self,
        *,
        win_size: int = None,
        win_func: str = None,
        overlap: float = None,
        measure: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.57 aspectralstats Display frequency domain statistical information about the audio channels. Statistics are calculated and stored as metadata for each audio channel and for each audio frame. It accepts the following option: A list of each metadata key follows:

        Parameters:
        ----------
        win_size:
            Set the window length in samples. Default value is 2048. Allowed range is from 32 to 65536.
        win_func:
            Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        overlap:
            Set window overlap. Allowed range is from 0 to 1. Default value is 0.5.
        measure:
            Select the parameters which are measured. The metadata keys can be used as flags, default is all which measures everything. none disables all measurement.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#aspectralstats

        """
        return FilterNode(
            *[self],
            name="aspectralstats",
            kwargs={"win_size": win_size, "win_func": win_func, "overlap": overlap, "measure": measure, **kwargs}
        ).stream()

    def asr(
        self,
        *,
        rate: int = None,
        hmm: str,
        dict: str,
        lm: str,
        lmctl: str,
        lmname: str,
        logfn: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.58 asr Automatic Speech Recognition This filter uses PocketSphinx for speech recognition. To enable compilation of this filter, you need to configure FFmpeg with --enable-pocketsphinx. It accepts the following options: The filter exports recognized speech as the frame metadata lavfi.asr.text.

        Parameters:
        ----------
        rate:
            Set sampling rate of input audio. Defaults is 16000. This need to match speech models, otherwise one will get poor results.
        hmm:
            Set dictionary containing acoustic model files.
        dict:
            Set pronunciation dictionary.
        lm:
            Set language model file.
        lmctl:
            Set language model set.
        lmname:
            Set which language model to use.
        logfn:
            Set output for log messages.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asr

        """
        return FilterNode(
            *[self],
            name="asr",
            kwargs={
                "rate": rate,
                "hmm": hmm,
                "dict": dict,
                "lm": lm,
                "lmctl": lmctl,
                "lmname": lmname,
                "logfn": logfn,
                **kwargs,
            }
        ).stream()

    def ass(self, *, shaping: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.5 ass Same as the subtitles filter, except that it doesn’t require libavcodec and libavformat to work. On the other hand, it is limited to ASS (Advanced Substation Alpha) subtitles files. This filter accepts the following option in addition to the common options from the subtitles filter:

        Parameters:
        ----------
        shaping:
            Set the shaping engine Available values are: ‘auto’ The default libass shaping engine, which is the best available. ‘simple’ Fast, font-agnostic shaper that can do only substitutions ‘complex’ Slower shaper using OpenType for substitutions and positioning The default is auto.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ass

        """
        return FilterNode(*[self], name="ass", kwargs={"shaping": shaping, **kwargs}).stream()

    def astats(
        self,
        *,
        length: float = None,
        metadata: str,
        reset: bool = None,
        measure_perchannel: str = None,
        measure_overall: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.59 astats Display time domain statistical information about the audio channels. Statistics are calculated and displayed for each audio channel and, where applicable, an overall figure is also given. It accepts the following option: A description of the measure keys follow:

        Parameters:
        ----------
        length:
            Short window length in seconds, used for peak and trough RMS measurement. Default is 0.05 (50 milliseconds). Allowed range is [0 - 10].
        metadata:
            Set metadata injection. All the metadata keys are prefixed with lavfi.astats.X, where X is channel number starting from 1 or string Overall. Default is disabled. Available keys for each channel are: Bit_depth Crest_factor DC_offset Dynamic_range Entropy Flat_factor Max_difference Max_level Mean_difference Min_difference Min_level Noise_floor Noise_floor_count Number_of_Infs Number_of_NaNs Number_of_denormals Peak_count Abs_Peak_count Peak_level RMS_difference RMS_peak RMS_trough Zero_crossings Zero_crossings_rate and for Overall: Bit_depth DC_offset Entropy Flat_factor Max_difference Max_level Mean_difference Min_difference Min_level Noise_floor Noise_floor_count Number_of_Infs Number_of_NaNs Number_of_denormals Number_of_samples Peak_count Abs_Peak_count Peak_level RMS_difference RMS_level RMS_peak RMS_trough For example, a full key looks like lavfi.astats.1.DC_offset or lavfi.astats.Overall.Peak_count. Read below for the description of the keys.
        reset:
            Set the number of frames over which cumulative stats are calculated before being reset. Default is disabled.
        measure_perchannel:
            Select the parameters which are measured per channel. The metadata keys can be used as flags, default is all which measures everything. none disables all per channel measurement.
        measure_overall:
            Select the parameters which are measured overall. The metadata keys can be used as flags, default is all which measures everything. none disables all overall measurement.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#astats

        """
        return FilterNode(
            *[self],
            name="astats",
            kwargs={
                "length": length,
                "metadata": metadata,
                "reset": reset,
                "measure_perchannel": measure_perchannel,
                "measure_overall": measure_overall,
                **kwargs,
            }
        ).stream()

    def astreamselect(self, *, inputs: int = None, map: list[str], **kwargs: dict[str, Any]) -> "Stream":
        """
        11.245 streamselect, astreamselect Select video or audio streams. The filter accepts the following options:

        Parameters:
        ----------
        inputs:
            Set number of inputs. Default is 2.
        map:
            Set input indexes to remap to outputs.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

        """
        return FilterNode(*[self], name="astreamselect", kwargs={"inputs": inputs, "map": map, **kwargs}).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.60 asubboost Boost subwoofer frequencies. The filter accepts the following options:

        Parameters:
        ----------
        dry:
            Set dry gain, how much of original signal is kept. Allowed range is from 0 to 1. Default value is 1.0.
        wet:
            Set wet gain, how much of filtered signal is kept. Allowed range is from 0 to 1. Default value is 1.0.
        boost:
            Set max boost factor. Allowed range is from 1 to 12. Default value is 2.
        decay:
            Set delay line decay gain value. Allowed range is from 0 to 1. Default value is 0.0.
        feedback:
            Set delay line feedback gain value. Allowed range is from 0 to 1. Default value is 0.9.
        cutoff:
            Set cutoff frequency in Hertz. Allowed range is 50 to 900. Default value is 100.
        slope:
            Set slope amount for cutoff frequency. Allowed range is 0.0001 to 1. Default value is 0.5.
        delay:
            Set delay. Allowed range is from 1 to 100. Default value is 20.
        channels:
            Set the channels to process. Default value is all available.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubboost

        """
        return FilterNode(
            *[self],
            name="asubboost",
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
                **kwargs,
            }
        ).stream()

    def asubcut(
        self, *, cutoff: float = None, order: int = None, level: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.61 asubcut Cut subwoofer frequencies. This filter allows to set custom, steeper roll off than highpass filter, and thus is able to more attenuate frequency content in stop-band. The filter accepts the following options:

        Parameters:
        ----------
        cutoff:
            Set cutoff frequency in Hertz. Allowed range is 2 to 200. Default value is 20.
        order:
            Set filter order. Available values are from 3 to 20. Default value is 10.
        level:
            Set input gain level. Allowed range is from 0 to 1. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asubcut

        """
        return FilterNode(
            *[self], name="asubcut", kwargs={"cutoff": cutoff, "order": order, "level": level, **kwargs}
        ).stream()

    def asupercut(
        self, *, cutoff: int = None, order: int = None, level: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.62 asupercut Cut super frequencies. The filter accepts the following options:

        Parameters:
        ----------
        cutoff:
            Set cutoff frequency in Hertz. Allowed range is 20000 to 192000. Default value is 20000.
        order:
            Set filter order. Available values are from 3 to 20. Default value is 10.
        level:
            Set input gain level. Allowed range is from 0 to 1. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asupercut

        """
        return FilterNode(
            *[self], name="asupercut", kwargs={"cutoff": cutoff, "order": order, "level": level, **kwargs}
        ).stream()

    def asuperpass(
        self,
        *,
        centerf: float = None,
        order: int = None,
        qfactor: float = None,
        level: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.63 asuperpass Apply high order Butterworth band-pass filter. The filter accepts the following options:

        Parameters:
        ----------
        centerf:
            Set center frequency in Hertz. Allowed range is 2 to 999999. Default value is 1000.
        order:
            Set filter order. Available values are from 4 to 20. Default value is 4.
        qfactor:
            Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
        level:
            Set input gain level. Allowed range is from 0 to 2. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperpass

        """
        return FilterNode(
            *[self],
            name="asuperpass",
            kwargs={"centerf": centerf, "order": order, "qfactor": qfactor, "level": level, **kwargs}
        ).stream()

    def asuperstop(
        self,
        *,
        centerf: float = None,
        order: int = None,
        qfactor: float = None,
        level: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.64 asuperstop Apply high order Butterworth band-stop filter. The filter accepts the following options:

        Parameters:
        ----------
        centerf:
            Set center frequency in Hertz. Allowed range is 2 to 999999. Default value is 1000.
        order:
            Set filter order. Available values are from 4 to 20. Default value is 4.
        qfactor:
            Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
        level:
            Set input gain level. Allowed range is from 0 to 2. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperstop

        """
        return FilterNode(
            *[self],
            name="asuperstop",
            kwargs={"centerf": centerf, "order": order, "qfactor": qfactor, "level": level, **kwargs}
        ).stream()

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
        a: str = None,
        _0s: int = None,
        _1s: int = None,
        _2s: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.6 atadenoise Apply an Adaptive Temporal Averaging Denoiser to the video input. The filter accepts the following options:

        Parameters:
        ----------
        _0a:
            Set threshold A for 1st plane. Default is 0.02. Valid range is 0 to 0.3.
        _0b:
            Set threshold B for 1st plane. Default is 0.04. Valid range is 0 to 5.
        _1a:
            Set threshold A for 2nd plane. Default is 0.02. Valid range is 0 to 0.3.
        _1b:
            Set threshold B for 2nd plane. Default is 0.04. Valid range is 0 to 5.
        _2a:
            Set threshold A for 3rd plane. Default is 0.02. Valid range is 0 to 0.3.
        _2b:
            Set threshold B for 3rd plane. Default is 0.04. Valid range is 0 to 5. Threshold A is designed to react on abrupt changes in the input signal and threshold B is designed to react on continuous changes in the input signal.
        s:
            Set number of frames filter will use for averaging. Default is 9. Must be odd number in range [5, 129].
        p:
            Set what planes of frame filter will use for averaging. Default is all.
        a:
            Set what variant of algorithm filter will use for averaging. Default is p parallel. Alternatively can be set to s serial. Parallel can be faster then serial, while other way around is never true. Parallel will abort early on first change being greater then thresholds, while serial will continue processing other side of frames if they are equal or below thresholds.
        _0s:
            Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.
        _1s:
            Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.
        _2s:
            Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767. Valid range is from 0 to 32767. This options controls weight for each pixel in radius defined by size. Default value means every pixel have same weight. Setting this option to 0 effectively disables filtering.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atadenoise

        """
        return FilterNode(
            *[self],
            name="atadenoise",
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
                **kwargs,
            }
        ).stream()

    def atempo(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.65 atempo Adjust audio tempo. The filter accepts exactly one parameter, the audio tempo. If not specified then the filter will assume nominal 1.0 tempo. Tempo must be in the [0.5, 100.0] range. Note that tempo greater than 2 will skip some samples rather than blend them in. If for any reason this is a concern it is always possible to daisy-chain several instances of atempo to achieve the desired product tempo.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atempo

        """
        return FilterNode(*[self], name="atempo", kwargs={**kwargs}).stream()

    def atilt(
        self,
        *,
        freq: float = None,
        slope: float = None,
        width: float = None,
        order: str,
        level: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.66 atilt Apply spectral tilt filter to audio stream. This filter apply any spectral roll-off slope over any specified frequency band. The filter accepts the following options:

        Parameters:
        ----------
        freq:
            Set central frequency of tilt in Hz. Default is 10000 Hz.
        slope:
            Set slope direction of tilt. Default is 0. Allowed range is from -1 to 1.
        width:
            Set width of tilt. Default is 1000. Allowed range is from 100 to 10000.
        order:
            Set order of tilt filter.
        level:
            Set input volume level. Allowed range is from 0 to 4. Default is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atilt

        """
        return FilterNode(
            *[self],
            name="atilt",
            kwargs={"freq": freq, "slope": slope, "width": width, "order": order, "level": level, **kwargs}
        ).stream()

    def atrim(
        self,
        *,
        start: str,
        end: str,
        start_pts: str,
        end_pts: str,
        duration: str,
        start_sample: int,
        end_sample: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.67 atrim Trim the input so that the output contains one continuous subpart of the input. It accepts the following parameters: start, end, and duration are expressed as time duration specifications; see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual. Note that the first two sets of the start/end options and the duration option look at the frame timestamp, while the _sample options simply count the samples that pass through the filter. So start/end_pts and start/end_sample will give different results when the timestamps are wrong, inexact or do not start at zero. Also note that this filter does not modify the timestamps. If you wish to have the output timestamps start at zero, insert the asetpts filter after the atrim filter. If multiple start or end options are set, this filter tries to be greedy and keep all samples that match at least one of the specified constraints. To keep only the part that matches all the constraints at once, chain multiple atrim filters. The defaults are such that all the input is kept. So it is possible to set e.g. just the end values to keep everything before the specified time. Examples: Drop everything except the second minute of input: ffmpeg -i INPUT -af atrim=60:120 Keep only the first 1000 samples: ffmpeg -i INPUT -af atrim=end_sample=1000

        Parameters:
        ----------
        start:
            Timestamp (in seconds) of the start of the section to keep. I.e. the audio sample with the timestamp start will be the first sample in the output.
        end:
            Specify time of the first audio sample that will be dropped, i.e. the audio sample immediately preceding the one with the timestamp end will be the last sample in the output.
        start_pts:
            Same as start, except this option sets the start timestamp in samples instead of seconds.
        end_pts:
            Same as end, except this option sets the end timestamp in samples instead of seconds.
        duration:
            The maximum duration of the output in seconds.
        start_sample:
            The number of the first sample that should be output.
        end_sample:
            The number of the first sample that should be dropped.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#atrim

        """
        return FilterNode(
            *[self],
            name="atrim",
            kwargs={
                "start": start,
                "end": end,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "start_sample": start_sample,
                "end_sample": end_sample,
                **kwargs,
            }
        ).stream()

    def avgblur(self, *, sizeX: int, planes: str, sizeY: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.7 avgblur Apply average blur filter. The filter accepts the following options:

        Parameters:
        ----------
        sizeX:
            Set horizontal radius size.
        planes:
            Set which planes to filter. By default all planes are filtered.
        sizeY:
            Set vertical radius size, if zero it will be same as sizeX. Default is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#avgblur

        """
        return FilterNode(
            *[self], name="avgblur", kwargs={"sizeX": sizeX, "planes": planes, "sizeY": sizeY, **kwargs}
        ).stream()

    def axcorrelate(self, *, size: int = None, algo: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.68 axcorrelate Calculate normalized windowed cross-correlation between two input audio streams. Resulted samples are always between -1 and 1 inclusive. If result is 1 it means two input samples are highly correlated in that selected segment. Result 0 means they are not correlated at all. If result is -1 it means two input samples are out of phase, which means they cancel each other. The filter accepts the following options:

        Parameters:
        ----------
        size:
            Set size of segment over which cross-correlation is calculated. Default is 256. Allowed range is from 2 to 131072.
        algo:
            Set algorithm for cross-correlation. Can be slow or fast or best. Default is best. Fast algorithm assumes mean values over any given segment are always zero and thus need much less calculations to make. This is generally not true, but is valid for typical audio streams.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#axcorrelate

        """
        return FilterNode(*[self], name="axcorrelate", kwargs={"size": size, "algo": algo, **kwargs}).stream()

    def backgroundkey(self, *, threshold: float, similarity: float, blend: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.8 backgroundkey Turns a static background into transparency. The filter accepts the following option:

        Parameters:
        ----------
        threshold:
            Threshold for scene change detection.
        similarity:
            Similarity percentage with the background.
        blend:
            Set the blend amount for pixels that are not similar.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#backgroundkey

        """
        return FilterNode(
            *[self],
            name="backgroundkey",
            kwargs={"threshold": threshold, "similarity": similarity, "blend": blend, **kwargs}
        ).stream()

    def bandpass(
        self,
        *,
        frequency: float = None,
        csg: int = None,
        width_type: str,
        width: float,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.69 bandpass Apply a two-pole Butterworth band-pass filter with central frequency frequency, and (3dB-point) band-width width. The csg option selects a constant skirt gain (peak gain = Q) instead of the default: constant 0dB peak gain. The filter roll off at 6dB per octave (20dB per decade). The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set the filter’s central frequency. Default is 3000.
        csg:
            Constant skirt gain if set to 1. Defaults to 0.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandpass

        """
        return FilterNode(
            *[self],
            name="bandpass",
            kwargs={
                "frequency": frequency,
                "csg": csg,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def bandreject(
        self,
        *,
        frequency: float = None,
        width_type: str,
        width: float,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.70 bandreject Apply a two-pole Butterworth band-reject filter with central frequency frequency, and (3dB-point) band-width width. The filter roll off at 6dB per octave (20dB per decade). The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set the filter’s central frequency. Default is 3000.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bandreject

        """
        return FilterNode(
            *[self],
            name="bandreject",
            kwargs={
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def bass(
        self,
        *,
        gain: float,
        frequency: float = None,
        width_type: str,
        width: float,
        poles: int = None,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.71 bass, lowshelf Boost or cut the bass (lower) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi’s tone-controls. This is also known as shelving equalisation (EQ). The filter accepts the following options:

        Parameters:
        ----------
        gain:
            Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency:
            Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Determine how steep is the filter’s shelf transition.
        poles:
            Set number of poles. Default is 2.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        return FilterNode(
            *[self],
            name="bass",
            kwargs={
                "gain": gain,
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def bbox(self, *, min_val: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.9 bbox Compute the bounding box for the non-black pixels in the input frame luma plane. This filter computes the bounding box containing all the pixels with a luma value greater than the minimum allowed value. The parameters describing the bounding box are printed on the filter log. The filter accepts the following option:

        Parameters:
        ----------
        min_val:
            Set the minimal luma value. Default is 16.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bbox

        """
        return FilterNode(*[self], name="bbox", kwargs={"min_val": min_val, **kwargs}).stream()

    def bilateral(
        self, *, sigmaS: float = None, sigmaR: float = None, planes: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.10 bilateral Apply bilateral filter, spatial smoothing while preserving edges. The filter accepts the following options:

        Parameters:
        ----------
        sigmaS:
            Set sigma of gaussian function to calculate spatial weight. Allowed range is 0 to 512. Default is 0.1.
        sigmaR:
            Set sigma of gaussian function to calculate range weight. Allowed range is 0 to 1. Default is 0.1.
        planes:
            Set planes to filter. Default is first only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral

        """
        return FilterNode(
            *[self], name="bilateral", kwargs={"sigmaS": sigmaS, "sigmaR": sigmaR, "planes": planes, **kwargs}
        ).stream()

    def bilateral_cuda(
        self, *, sigmaS: float = None, sigmaR: float = None, window_size: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.11 bilateral_cuda CUDA accelerated bilateral filter, an edge preserving filter. This filter is mathematically accurate thanks to the use of GPU acceleration. For best output quality, use one to one chroma subsampling, i.e. yuv444p format. The filter accepts the following options:

        Parameters:
        ----------
        sigmaS:
            Set sigma of gaussian function to calculate spatial weight, also called sigma space. Allowed range is 0.1 to 512. Default is 0.1.
        sigmaR:
            Set sigma of gaussian function to calculate color range weight, also called sigma color. Allowed range is 0.1 to 512. Default is 0.1.
        window_size:
            Set window size of the bilateral function to determine the number of neighbours to loop on. If the number entered is even, one will be added automatically. Allowed range is 1 to 255. Default is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bilateral_005fcuda

        """
        return FilterNode(
            *[self],
            name="bilateral_cuda",
            kwargs={"sigmaS": sigmaS, "sigmaR": sigmaR, "window_size": window_size, **kwargs}
        ).stream()

    def biquad(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.72 biquad Apply a biquad IIR filter with the given coefficients. Where b0, b1, b2 and a0, a1, a2 are the numerator and denominator coefficients respectively. and channels, c specify which channels to filter, by default all available are filtered.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#biquad

        """
        return FilterNode(*[self], name="biquad", kwargs={**kwargs}).stream()

    def bitplanenoise(self, *, bitplane: int = None, filter: bool = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.12 bitplanenoise Show and measure bit plane noise. The filter accepts the following options:

        Parameters:
        ----------
        bitplane:
            Set which plane to analyze. Default is 1.
        filter:
            Filter out noisy pixels from bitplane set above. Default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bitplanenoise

        """
        return FilterNode(
            *[self], name="bitplanenoise", kwargs={"bitplane": bitplane, "filter": filter, **kwargs}
        ).stream()

    def blackdetect(
        self,
        *,
        black_min_duration: float = None,
        picture_black_ratio_th: float = None,
        pixel_black_th: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.13 blackdetect Detect video intervals that are (almost) completely black. Can be useful to detect chapter transitions, commercials, or invalid recordings. The filter outputs its detection analysis to both the log as well as frame metadata. If a black segment of at least the specified minimum duration is found, a line with the start and end timestamps as well as duration is printed to the log with level info. In addition, a log line with level debug is printed per frame showing the black amount detected for that frame. The filter also attaches metadata to the first frame of a black segment with key lavfi.black_start and to the first frame after the black segment ends with key lavfi.black_end. The value is the frame’s timestamp. This metadata is added regardless of the minimum duration specified. The filter accepts the following options: The following example sets the maximum pixel threshold to the minimum value, and detects only black intervals of 2 or more seconds: blackdetect=d=2:pix_th=0.00

        Parameters:
        ----------
        black_min_duration:
            Set the minimum detected black duration expressed in seconds. It must be a non-negative floating point number. Default value is 2.0.
        picture_black_ratio_th:
            Set the threshold for considering a picture "black". Express the minimum value for the ratio: nb_black_pixels / nb_pixels for which a picture is considered black. Default value is 0.98.
        pixel_black_th:
            Set the threshold for considering a pixel "black". The threshold expresses the maximum pixel luma value for which a pixel is considered "black". The provided value is scaled according to the following equation: absolute_threshold = luma_minimum_value + pixel_black_th * luma_range_size luma_range_size and luma_minimum_value depend on the input video format, the range is [0-255] for YUV full-range formats and [16-235] for YUV non full-range formats. Default value is 0.10.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackdetect

        """
        return FilterNode(
            *[self],
            name="blackdetect",
            kwargs={
                "black_min_duration": black_min_duration,
                "picture_black_ratio_th": picture_black_ratio_th,
                "pixel_black_th": pixel_black_th,
                **kwargs,
            }
        ).stream()

    def blackframe(self, *, amount: int = None, threshold: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.14 blackframe Detect frames that are (almost) completely black. Can be useful to detect chapter transitions or commercials. Output lines consist of the frame number of the detected frame, the percentage of blackness, the position in the file if known or -1 and the timestamp in seconds. In order to display the output lines, you need to set the loglevel at least to the AV_LOG_INFO value. This filter exports frame metadata lavfi.blackframe.pblack. The value represents the percentage of pixels in the picture that are below the threshold value. It accepts the following parameters:

        Parameters:
        ----------
        amount:
            The percentage of the pixels that have to be below the threshold; it defaults to 98.
        threshold:
            The threshold below which a pixel value is considered black; it defaults to 32.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blackframe

        """
        return FilterNode(
            *[self], name="blackframe", kwargs={"amount": amount, "threshold": threshold, **kwargs}
        ).stream()

    def blend(
        self,
        *,
        c0_mode: str = None,
        c1_mode: str = None,
        c2_mode: str = None,
        c3_mode: str = None,
        all_mode: str = None,
        c0_opacity: float,
        c1_opacity: float,
        c2_opacity: float,
        c3_opacity: float,
        all_opacity: float,
        c0_expr: str,
        c1_expr: str,
        c2_expr: str,
        c3_expr: str,
        all_expr: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.15 blend Blend two video frames into each other. The blend filter takes two input streams and outputs one stream, the first input is the "top" layer and second input is "bottom" layer. By default, the output terminates when the longest input terminates. The tblend (time blend) filter takes two consecutive frames from one single stream, and outputs the result obtained by blending the new frame on top of the old frame. A description of the accepted options follows. The blend filter also supports the framesync options.

        Parameters:
        ----------
        c0_mode:
            Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
        c1_mode:
            Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
        c2_mode:
            Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
        c3_mode:
            Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
        all_mode:
            Set blend mode for specific pixel component or all pixel components in case of all_mode. Default value is normal. Available values for component modes are: ‘addition’ ‘and’ ‘average’ ‘bleach’ ‘burn’ ‘darken’ ‘difference’ ‘divide’ ‘dodge’ ‘exclusion’ ‘extremity’ ‘freeze’ ‘geometric’ ‘glow’ ‘grainextract’ ‘grainmerge’ ‘hardlight’ ‘hardmix’ ‘hardoverlay’ ‘harmonic’ ‘heat’ ‘interpolate’ ‘lighten’ ‘linearlight’ ‘multiply’ ‘multiply128’ ‘negation’ ‘normal’ ‘or’ ‘overlay’ ‘phoenix’ ‘pinlight’ ‘reflect’ ‘screen’ ‘softdifference’ ‘softlight’ ‘stain’ ‘subtract’ ‘vividlight’ ‘xor’
        c0_opacity:
            Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
        c1_opacity:
            Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
        c2_opacity:
            Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
        c3_opacity:
            Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
        all_opacity:
            Set blend opacity for specific pixel component or all pixel components in case of all_opacity. Only used in combination with pixel component blend modes.
        c0_expr:
            Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
        c1_expr:
            Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
        c2_expr:
            Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
        c3_expr:
            Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).
        all_expr:
            Set blend expression for specific pixel component or all pixel components in case of all_expr. Note that related mode options will be ignored if those are set. The expressions can use the following variables: N The sequential number of the filtered frame, starting from 0. X Y the coordinates of the current sample W H the width and height of currently filtered plane SW SH Width and height scale for the plane being filtered. It is the ratio between the dimensions of the current plane to the luma plane, e.g. for a yuv420p frame, the values are 1,1 for the luma plane and 0.5,0.5 for the chroma planes. T Time of the current frame, expressed in seconds. TOP, A Value of pixel component at current location for first video frame (top layer). BOTTOM, B Value of pixel component at current location for second video frame (bottom layer).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blend

        """
        return FilterNode(
            *[self],
            name="blend",
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
                "c0_expr": c0_expr,
                "c1_expr": c1_expr,
                "c2_expr": c2_expr,
                "c3_expr": c3_expr,
                "all_expr": all_expr,
                **kwargs,
            }
        ).stream()

    def blockdetect(
        self,
        *,
        period_min: list[str] = None,
        period_max: list[str] = None,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.16 blockdetect Determines blockiness of frames without altering the input frames. Based on Remco Muijs and Ihor Kirenko: "A no-reference blocking artifact measure for adaptive video processing." 2005 13th European signal processing conference. The filter accepts the following options:

        Parameters:
        ----------
        period_min:
            Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        period_max:
            Set minimum and maximum values for determining pixel grids (periods). Default values are [3,24].
        planes:
            Set planes to filter. Default is first only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blockdetect

        """
        return FilterNode(
            *[self],
            name="blockdetect",
            kwargs={"period_min": period_min, "period_max": period_max, "planes": planes, **kwargs}
        ).stream()

    def blurdetect(
        self,
        *,
        low: str,
        high: str,
        radius: int,
        block_pct: int,
        block_width: int,
        block_height: int,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.17 blurdetect Determines blurriness of frames without altering the input frames. Based on Marziliano, Pina, et al. "A no-reference perceptual blur metric." Allows for a block-based abbreviation. The filter accepts the following options:

        Parameters:
        ----------
        low:
            Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        high:
            Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        radius:
            Define the radius to search around an edge pixel for local maxima.
        block_pct:
            Determine blurriness only for the most significant blocks, given in percentage.
        block_width:
            Determine blurriness for blocks of width block_width. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_height.
        block_height:
            Determine blurriness for blocks of height block_height. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_width.
        planes:
            Set planes to filter. Default is first only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#blurdetect

        """
        return FilterNode(
            *[self],
            name="blurdetect",
            kwargs={
                "low": low,
                "high": high,
                "radius": radius,
                "block_pct": block_pct,
                "block_width": block_width,
                "block_height": block_height,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def bm3d(
        self,
        *,
        sigma: float = None,
        block: str,
        bstep: int = None,
        group: int = None,
        range: int,
        mstep: int = None,
        thmse: int,
        hdthr: float,
        estim: str = None,
        ref: bool = None,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.18 bm3d Denoise frames using Block-Matching 3D algorithm. The filter accepts the following options.

        Parameters:
        ----------
        sigma:
            Set denoising strength. Default value is 1. Allowed range is from 0 to 999.9. The denoising algorithm is very sensitive to sigma, so adjust it according to the source.
        block:
            Set local patch size. This sets dimensions in 2D.
        bstep:
            Set sliding step for processing blocks. Default value is 4. Allowed range is from 1 to 64. Smaller values allows processing more reference blocks and is slower.
        group:
            Set maximal number of similar blocks for 3rd dimension. Default value is 1. When set to 1, no block matching is done. Larger values allows more blocks in single group. Allowed range is from 1 to 256.
        range:
            Set radius for search block matching. Default is 9. Allowed range is from 1 to INT32_MAX.
        mstep:
            Set step between two search locations for block matching. Default is 1. Allowed range is from 1 to 64. Smaller is slower.
        thmse:
            Set threshold of mean square error for block matching. Valid range is 0 to INT32_MAX.
        hdthr:
            Set thresholding parameter for hard thresholding in 3D transformed domain. Larger values results in stronger hard-thresholding filtering in frequency domain.
        estim:
            Set filtering estimation mode. Can be basic or final. Default is basic.
        ref:
            If enabled, filter will use 2nd stream for block matching. Default is disabled for basic value of estim option, and always enabled if value of estim is final.
        planes:
            Set planes to filter. Default is all available except alpha.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bm3d

        """
        return FilterNode(
            *[self],
            name="bm3d",
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
                **kwargs,
            }
        ).stream()

    def boxblur(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.19 boxblur Apply a boxblur algorithm to the input video. It accepts the following parameters: A description of the accepted options follows.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#boxblur

        """
        return FilterNode(*[self], name="boxblur", kwargs={**kwargs}).stream()

    def bs2b(self, *, profile: str, fcut: float, feed: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.73 bs2b Bauer stereo to binaural transformation, which improves headphone listening of stereo audio records. To enable compilation of this filter you need to configure FFmpeg with --enable-libbs2b. It accepts the following parameters:

        Parameters:
        ----------
        profile:
            Pre-defined crossfeed level. default Default level (fcut=700, feed=50). cmoy Chu Moy circuit (fcut=700, feed=60). jmeier Jan Meier circuit (fcut=650, feed=95).
        fcut:
            Cut frequency (in Hz).
        feed:
            Feed level (in Hz).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bs2b

        """
        return FilterNode(
            *[self], name="bs2b", kwargs={"profile": profile, "fcut": fcut, "feed": feed, **kwargs}
        ).stream()

    def bwdif(self, *, mode: str = None, parity: str = None, deint: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.20 bwdif Deinterlace the input video ("bwdif" stands for "Bob Weaver Deinterlacing Filter"). Motion adaptive deinterlacing based on yadif with the use of w3fdif and cubic interpolation algorithms. It accepts the following parameters:

        Parameters:
        ----------
        mode:
            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif

        """
        return FilterNode(
            *[self], name="bwdif", kwargs={"mode": mode, "parity": parity, "deint": deint, **kwargs}
        ).stream()

    def bwdif_cuda(
        self, *, mode: str = None, parity: str = None, deint: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.21 bwdif_cuda Deinterlace the input video using the bwdif algorithm, but implemented in CUDA so that it can work as part of a GPU accelerated pipeline with nvdec and/or nvenc. It accepts the following parameters:

        Parameters:
        ----------
        mode:
            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. The default value is send_field.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bwdif_005fcuda

        """
        return FilterNode(
            *[self], name="bwdif_cuda", kwargs={"mode": mode, "parity": parity, "deint": deint, **kwargs}
        ).stream()

    def cas(self, *, strength: float = None, planes: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.23 cas Apply Contrast Adaptive Sharpen filter to video stream. The filter accepts the following options:

        Parameters:
        ----------
        strength:
            Set the sharpening strength. Default value is 0.
        planes:
            Set planes to filter. Default value is to filter all planes except alpha plane.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cas

        """
        return FilterNode(*[self], name="cas", kwargs={"strength": strength, "planes": planes, **kwargs}).stream()

    def ccrepack(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.22 ccrepack Repack CEA-708 closed captioning side data This filter fixes various issues seen with commerical encoders related to upstream malformed CEA-708 payloads, specifically incorrect number of tuples (wrong cc_count for the target FPS), and incorrect ordering of tuples (i.e. the CEA-608 tuples are not at the first entries in the payload).

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ccrepack

        """
        return FilterNode(*[self], name="ccrepack", kwargs={**kwargs}).stream()

    def channelmap(self, *, map: str, channel_layout: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.74 channelmap Remap input channels to new locations. It accepts the following parameters: If no mapping is present, the filter will implicitly map input channels to output channels, preserving indices.

        Parameters:
        ----------
        map:
            Map channels from input to output. The argument is a ’|’-separated list of mappings, each in the in_channel-out_channel or in_channel form. in_channel can be either the name of the input channel (e.g. FL for front left) or its index in the input channel layout. out_channel is the name of the output channel or its index in the output channel layout. If out_channel is not given then it is implicitly an index, starting with zero and increasing by one for each mapping.
        channel_layout:
            The channel layout of the output stream.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelmap

        """
        return FilterNode(
            *[self], name="channelmap", kwargs={"map": map, "channel_layout": channel_layout, **kwargs}
        ).stream()

    def channelsplit(self, *, channel_layout: str = None, channels: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.75 channelsplit Split each channel from an input audio stream into a separate output stream. It accepts the following parameters:

        Parameters:
        ----------
        channel_layout:
            The channel layout of the input stream. The default is "stereo".
        channels:
            A channel layout describing the channels to be extracted as separate output streams or "all" to extract each input channel as a separate stream. The default is "all". Choosing channels not present in channel layout in the input will result in an error.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#channelsplit

        """
        return FilterNode(
            *[self], name="channelsplit", kwargs={"channel_layout": channel_layout, "channels": channels, **kwargs}
        ).stream()

    def chorus(
        self,
        *,
        in_gain: float = None,
        out_gain: float = None,
        delays: list[str],
        decays: list[str],
        speeds: list[str],
        depths: list[str],
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.76 chorus Add a chorus effect to the audio. Can make a single vocal sound like a chorus, but can also be applied to instrumentation. Chorus resembles an echo effect with a short delay, but whereas with echo the delay is constant, with chorus, it is varied using using sinusoidal or triangular modulation. The modulation depth defines the range the modulated delay is played before or after the delay. Hence the delayed sound will sound slower or faster, that is the delayed sound tuned around the original one, like in a chorus where some vocals are slightly off key. It accepts the following parameters:

        Parameters:
        ----------
        in_gain:
            Set input gain. Default is 0.4.
        out_gain:
            Set output gain. Default is 0.4.
        delays:
            Set delays. A typical delay is around 40ms to 60ms.
        decays:
            Set decays.
        speeds:
            Set speeds.
        depths:
            Set depths.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chorus

        """
        return FilterNode(
            *[self],
            name="chorus",
            kwargs={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
                "speeds": speeds,
                "depths": depths,
                **kwargs,
            }
        ).stream()

    def chromahold(
        self, *, color: str, similarity: float, blend: float, yuv: bool, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.24 chromahold Remove all color information for all colors except for certain one. The filter accepts the following options:

        Parameters:
        ----------
        color:
            The color which will not be replaced with neutral chroma.
        similarity:
            Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        blend:
            Blend percentage. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more preserved color.
        yuv:
            Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromahold

        """
        return FilterNode(
            *[self],
            name="chromahold",
            kwargs={"color": color, "similarity": similarity, "blend": blend, "yuv": yuv, **kwargs}
        ).stream()

    def chromakey(
        self, *, color: str, similarity: float, blend: float, yuv: bool, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.25 chromakey YUV colorspace color/chroma keying. The filter accepts the following options:

        Parameters:
        ----------
        color:
            The color which will be replaced with transparency.
        similarity:
            Similarity percentage with the key color. 0.01 matches only the exact key color, while 1.0 matches everything.
        blend:
            Blend percentage. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.
        yuv:
            Signals that the color passed is already in YUV instead of RGB. Literal colors like "green" or "red" don’t make sense with this enabled anymore. This can be used to pass exact YUV values as hexadecimal numbers.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey

        """
        return FilterNode(
            *[self],
            name="chromakey",
            kwargs={"color": color, "similarity": similarity, "blend": blend, "yuv": yuv, **kwargs}
        ).stream()

    def chromakey_cuda(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.26 chromakey_cuda CUDA accelerated YUV colorspace color/chroma keying. This filter works like normal chromakey filter but operates on CUDA frames. for more details and parameters see chromakey.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromakey_005fcuda

        """
        return FilterNode(*[self], name="chromakey_cuda", kwargs={**kwargs}).stream()

    def chromanr(
        self,
        *,
        thres: int = None,
        sizew: int = None,
        sizeh: int = None,
        stepw: int = None,
        steph: int = None,
        threy: int = None,
        threu: int = None,
        threv: int = None,
        distance: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.27 chromanr Reduce chrominance noise. The filter accepts the following options:

        Parameters:
        ----------
        thres:
            Set threshold for averaging chrominance values. Sum of absolute difference of Y, U and V pixel components of current pixel and neighbour pixels lower than this threshold will be used in averaging. Luma component is left unchanged and is copied to output. Default value is 30. Allowed range is from 1 to 200.
        sizew:
            Set horizontal radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.
        sizeh:
            Set vertical radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.
        stepw:
            Set horizontal step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.
        steph:
            Set vertical step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.
        threy:
            Set Y threshold for averaging chrominance values. Set finer control for max allowed difference between Y components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        threu:
            Set U threshold for averaging chrominance values. Set finer control for max allowed difference between U components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        threv:
            Set V threshold for averaging chrominance values. Set finer control for max allowed difference between V components of current pixel and neigbour pixels. Default value is 200. Allowed range is from 1 to 200.
        distance:
            Set distance type used in calculations. ‘manhattan’ Absolute difference. ‘euclidean’ Difference squared. Default distance type is manhattan.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromanr

        """
        return FilterNode(
            *[self],
            name="chromanr",
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
                **kwargs,
            }
        ).stream()

    def chromashift(
        self, *, cbh: float, cbv: float, crh: float, crv: float, edge: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.28 chromashift Shift chroma pixels horizontally and/or vertically. The filter accepts the following options:

        Parameters:
        ----------
        cbh:
            Set amount to shift chroma-blue horizontally.
        cbv:
            Set amount to shift chroma-blue vertically.
        crh:
            Set amount to shift chroma-red horizontally.
        crv:
            Set amount to shift chroma-red vertically.
        edge:
            Set edge mode, can be smear, default, or warp.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#chromashift

        """
        return FilterNode(
            *[self], name="chromashift", kwargs={"cbh": cbh, "cbv": cbv, "crh": crh, "crv": crv, "edge": edge, **kwargs}
        ).stream()

    def ciescope(
        self,
        *,
        system: str,
        cie: str,
        gamuts: str,
        size: int,
        intensity: float,
        contrast: float,
        corrgamma: bool,
        showwhite: bool,
        gamma: float,
        fill: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.29 ciescope Display CIE color diagram with pixels overlaid onto it. The filter accepts the following options:

        Parameters:
        ----------
        system:
            Set color system. ‘ntsc, 470m’ ‘ebu, 470bg’ ‘smpte’ ‘240m’ ‘apple’ ‘widergb’ ‘cie1931’ ‘rec709, hdtv’ ‘uhdtv, rec2020’ ‘dcip3’
        cie:
            Set CIE system. ‘xyy’ ‘ucs’ ‘luv’
        gamuts:
            Set what gamuts to draw. See system option for available values.
        size:
            Set ciescope size, by default set to 512.
        intensity:
            Set intensity used to map input pixel values to CIE diagram.
        contrast:
            Set contrast used to draw tongue colors that are out of active color system gamut.
        corrgamma:
            Correct gamma displayed on scope, by default enabled.
        showwhite:
            Show white point on CIE diagram, by default disabled.
        gamma:
            Set input gamma. Used only with XYZ input color space.
        fill:
            Fill with CIE colors. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ciescope

        """
        return FilterNode(
            *[self],
            name="ciescope",
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
                **kwargs,
            }
        ).stream()

    def codecview(
        self, *, block: bool, mv: str, qp: bool, mv_type: str, frame_type: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.30 codecview Visualize information exported by some codecs. Some codecs can export information through frames using side-data or other means. For example, some MPEG based codecs export motion vectors through the export_mvs flag in the codec flags2 option. The filter accepts the following option:

        Parameters:
        ----------
        block:
            Display block partition structure using the luma plane.
        mv:
            Set motion vectors to visualize. Available flags for mv are: ‘pf’ forward predicted MVs of P-frames ‘bf’ forward predicted MVs of B-frames ‘bb’ backward predicted MVs of B-frames
        qp:
            Display quantization parameters using the chroma planes.
        mv_type:
            Set motion vectors type to visualize. Includes MVs from all frames unless specified by frame_type option. Available flags for mv_type are: ‘fp’ forward predicted MVs ‘bp’ backward predicted MVs
        frame_type:
            Set frame type to visualize motion vectors of. Available flags for frame_type are: ‘if’ intra-coded frames (I-frames) ‘pf’ predicted frames (P-frames) ‘bf’ bi-directionally predicted frames (B-frames)



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#codecview

        """
        return FilterNode(
            *[self],
            name="codecview",
            kwargs={"block": block, "mv": mv, "qp": qp, "mv_type": mv_type, "frame_type": frame_type, **kwargs}
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.31 colorbalance Modify intensity of primary colors (red, green and blue) of input frames. The filter allows an input frame to be adjusted in the shadows, midtones or highlights regions for the red-cyan, green-magenta or blue-yellow balance. A positive adjustment value shifts the balance towards the primary color, a negative value towards the complementary color. The filter accepts the following options:

        Parameters:
        ----------
        rs:
            Adjust red, green and blue shadows (darkest pixels).
        gs:
            Adjust red, green and blue shadows (darkest pixels).
        bs:
            Adjust red, green and blue shadows (darkest pixels).
        rm:
            Adjust red, green and blue midtones (medium pixels).
        gm:
            Adjust red, green and blue midtones (medium pixels).
        bm:
            Adjust red, green and blue midtones (medium pixels).
        rh:
            Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        gh:
            Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        bh:
            Adjust red, green and blue highlights (brightest pixels). Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        pl:
            Preserve lightness when changing color balance. Default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorbalance

        """
        return FilterNode(
            *[self],
            name="colorbalance",
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
                **kwargs,
            }
        ).stream()

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
        pc: str = None,
        pa: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.34 colorchannelmixer Adjust video input frames by re-mixing color channels. This filter modifies a color channel by adding the values associated to the other channels of the same pixels. For example if the value to modify is red, the output value will be: red=red*rr + blue*rb + green*rg + alpha*ra The filter accepts the following options:

        Parameters:
        ----------
        rr:
            Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        rg:
            Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        rb:
            Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        ra:
            Adjust contribution of input red, green, blue and alpha channels for output red channel. Default is 1 for rr, and 0 for rg, rb and ra.
        gr:
            Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        gg:
            Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        gb:
            Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        ga:
            Adjust contribution of input red, green, blue and alpha channels for output green channel. Default is 1 for gg, and 0 for gr, gb and ga.
        br:
            Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        bg:
            Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        bb:
            Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        ba:
            Adjust contribution of input red, green, blue and alpha channels for output blue channel. Default is 1 for bb, and 0 for br, bg and ba.
        ar:
            Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        ag:
            Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        ab:
            Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        aa:
            Adjust contribution of input red, green, blue and alpha channels for output alpha channel. Default is 1 for aa, and 0 for ar, ag and ab. Allowed ranges for options are [-2.0, 2.0].
        pc:
            Set preserve color mode. The accepted values are: ‘none’ Disable color preserving, this is default. ‘lum’ Preserve luminance. ‘max’ Preserve max value of RGB triplet. ‘avg’ Preserve average value of RGB triplet. ‘sum’ Preserve sum value of RGB triplet. ‘nrm’ Preserve normalized value of RGB triplet. ‘pwr’ Preserve power value of RGB triplet.
        pa:
            Set the preserve color amount when changing colors. Allowed range is from [0.0, 1.0]. Default is 0.0, thus disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer

        """
        return FilterNode(
            *[self],
            name="colorchannelmixer",
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
                **kwargs,
            }
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.32 colorcontrast Adjust color contrast between RGB components. The filter accepts the following options:

        Parameters:
        ----------
        rc:
            Set the red-cyan contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        gm:
            Set the green-magenta contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        by:
            Set the blue-yellow contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
        rcw:
            Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        gmw:
            Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        byw:
            Set the weight of each rc, gm, by option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
        pl:
            Set the amount of preserving lightness. Default value is 0.0. Allowed range is from 0.0 to 1.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcontrast

        """
        return FilterNode(
            *[self],
            name="colorcontrast",
            kwargs={"rc": rc, "gm": gm, "by": by, "rcw": rcw, "gmw": gmw, "byw": byw, "pl": pl, **kwargs}
        ).stream()

    def colorcorrect(
        self,
        *,
        rl: float = None,
        bl: float = None,
        rh: float = None,
        bh: float = None,
        saturation: float = None,
        analyze: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.33 colorcorrect Adjust color white balance selectively for blacks and whites. This filter operates in YUV colorspace. The filter accepts the following options:

        Parameters:
        ----------
        rl:
            Set the red shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        bl:
            Set the blue shadow spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        rh:
            Set the red highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        bh:
            Set the blue highlight spot. Allowed range is from -1.0 to 1.0. Default value is 0.
        saturation:
            Set the amount of saturation. Allowed range is from -3.0 to 3.0. Default value is 1.
        analyze:
            If set to anything other than manual it will analyze every frame and use derived parameters for filtering output frame. Possible values are: ‘manual’ ‘average’ ‘minmax’ ‘median’ Default value is manual.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorcorrect

        """
        return FilterNode(
            *[self],
            name="colorcorrect",
            kwargs={"rl": rl, "bl": bl, "rh": rh, "bh": bh, "saturation": saturation, "analyze": analyze, **kwargs}
        ).stream()

    def colorhold(self, *, color: str, similarity: float, blend: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.37 colorhold Remove all color information for all RGB colors except for certain one. The filter accepts the following options:

        Parameters:
        ----------
        color:
            The color which will not be replaced with neutral gray.
        similarity:
            Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
        blend:
            Blend percentage. 0.0 makes pixels fully gray. Higher values result in more preserved color.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorhold

        """
        return FilterNode(
            *[self], name="colorhold", kwargs={"color": color, "similarity": similarity, "blend": blend, **kwargs}
        ).stream()

    def colorize(
        self,
        *,
        hue: float = None,
        saturation: float = None,
        lightness: float = None,
        mix: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.35 colorize Overlay a solid color on the video stream. The filter accepts the following options:

        Parameters:
        ----------
        hue:
            Set the color hue. Allowed range is from 0 to 360. Default value is 0.
        saturation:
            Set the color saturation. Allowed range is from 0 to 1. Default value is 0.5.
        lightness:
            Set the color lightness. Allowed range is from 0 to 1. Default value is 0.5.
        mix:
            Set the mix of source lightness. By default is set to 1.0. Allowed range is from 0.0 to 1.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorize

        """
        return FilterNode(
            *[self],
            name="colorize",
            kwargs={"hue": hue, "saturation": saturation, "lightness": lightness, "mix": mix, **kwargs}
        ).stream()

    def colorkey(
        self, *, color: str = None, similarity: float = None, blend: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.36 colorkey RGB colorspace color keying. This filter operates on 8-bit RGB format frames by setting the alpha component of each pixel which falls within the similarity radius of the key color to 0. The alpha value for pixels outside the similarity radius depends on the value of the blend option. The filter accepts the following options:

        Parameters:
        ----------
        color:
            Set the color for which alpha will be set to 0 (full transparency). See (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default is black.
        similarity:
            Set the radius from the key color within which other colors also have full transparency. The computed distance is related to the unit fractional distance in 3D space between the RGB values of the key color and the pixel’s color. Range is 0.01 to 1.0. 0.01 matches within a very small radius around the exact key color, while 1.0 matches everything. Default is 0.01.
        blend:
            Set how the alpha value for pixels that fall outside the similarity radius is computed. 0.0 makes pixels either fully transparent or fully opaque. Higher values result in semi-transparent pixels, with greater transparency the more similar the pixel color is to the key color. Range is 0.0 to 1.0. Default is 0.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorkey

        """
        return FilterNode(
            *[self], name="colorkey", kwargs={"color": color, "similarity": similarity, "blend": blend, **kwargs}
        ).stream()

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
        preserve: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.38 colorlevels Adjust video input frames using levels. The filter accepts the following options:

        Parameters:
        ----------
        rimin:
            Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        gimin:
            Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        bimin:
            Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        aimin:
            Adjust red, green, blue and alpha input black point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
        rimax:
            Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        gimax:
            Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        bimax:
            Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        aimax:
            Adjust red, green, blue and alpha input white point. Allowed ranges for options are [-1.0, 1.0]. Defaults are 1. Input levels are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones.
        romin:
            Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        gomin:
            Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        bomin:
            Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        aomin:
            Adjust red, green, blue and alpha output black point. Allowed ranges for options are [0, 1.0]. Defaults are 0.
        romax:
            Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        gomax:
            Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        bomax:
            Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        aomax:
            Adjust red, green, blue and alpha output white point. Allowed ranges for options are [0, 1.0]. Defaults are 1. Output levels allows manual selection of a constrained output level range.
        preserve:
            Set preserve color mode. The accepted values are: ‘none’ Disable color preserving, this is default. ‘lum’ Preserve luminance. ‘max’ Preserve max value of RGB triplet. ‘avg’ Preserve average value of RGB triplet. ‘sum’ Preserve sum value of RGB triplet. ‘nrm’ Preserve normalized value of RGB triplet. ‘pwr’ Preserve power value of RGB triplet.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorlevels

        """
        return FilterNode(
            *[self],
            name="colorlevels",
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
                **kwargs,
            }
        ).stream()

    def colormap(
        self, *, patch_size: str, nb_patches: int, type: str = None, kernel: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.39 colormap Apply custom color maps to video stream. This filter needs three input video streams. First stream is video stream that is going to be filtered out. Second and third video stream specify color patches for source color to target color mapping. The filter accepts the following options:

        Parameters:
        ----------
        patch_size:
            Set the source and target video stream patch size in pixels.
        nb_patches:
            Set the max number of used patches from source and target video stream. Default value is number of patches available in additional video streams. Max allowed number of patches is 64.
        type:
            Set the adjustments used for target colors. Can be relative or absolute. Defaults is absolute.
        kernel:
            Set the kernel used to measure color differences between mapped colors. The accepted values are: ‘euclidean’ ‘weuclidean’ Default is euclidean.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colormap

        """
        return FilterNode(
            *[self],
            name="colormap",
            kwargs={"patch_size": patch_size, "nb_patches": nb_patches, "type": type, "kernel": kernel, **kwargs}
        ).stream()

    def colormatrix(self, *, src: str, dst: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.40 colormatrix Convert color matrix. The filter accepts the following options: For example to convert from BT.601 to SMPTE-240M, use the command: colormatrix=bt601:smpte240m

        Parameters:
        ----------
        src:
            Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020
        dst:
            Specify the source and destination color matrix. Both values must be specified. The accepted values are: ‘bt709’ BT.709 ‘fcc’ FCC ‘bt601’ BT.601 ‘bt470’ BT.470 ‘bt470bg’ BT.470BG ‘smpte170m’ SMPTE-170M ‘smpte240m’ SMPTE-240M ‘bt2020’ BT.2020



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colormatrix

        """
        return FilterNode(*[self], name="colormatrix", kwargs={"src": src, "dst": dst, **kwargs}).stream()

    def colorspace(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.41 colorspace Convert colorspace, transfer characteristics or color primaries. Input video needs to have an even size. The filter accepts the following options:

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace

        """
        return FilterNode(*[self], name="colorspace", kwargs={**kwargs}).stream()

    def colorspace_cuda(self, *, range: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.42 colorspace_cuda CUDA accelerated implementation of the colorspace filter. It is by no means feature complete compared to the software colorspace filter, and at the current time only supports color range conversion between jpeg/full and mpeg/limited range. The filter accepts the following options:

        Parameters:
        ----------
        range:
            Specify output color range. The accepted values are: ‘tv’ TV (restricted) range ‘mpeg’ MPEG (restricted) range ‘pc’ PC (full) range ‘jpeg’ JPEG (full) range



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colorspace_005fcuda

        """
        return FilterNode(*[self], name="colorspace_cuda", kwargs={"range": range, **kwargs}).stream()

    def colortemperature(
        self, *, temperature: int = None, mix: float = None, pl: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.43 colortemperature Adjust color temperature in video to simulate variations in ambient color temperature. The filter accepts the following options:

        Parameters:
        ----------
        temperature:
            Set the temperature in Kelvin. Allowed range is from 1000 to 40000. Default value is 6500 K.
        mix:
            Set mixing with filtered output. Allowed range is from 0 to 1. Default value is 1.
        pl:
            Set the amount of preserving lightness. Allowed range is from 0 to 1. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#colortemperature

        """
        return FilterNode(
            *[self], name="colortemperature", kwargs={"temperature": temperature, "mix": mix, "pl": pl, **kwargs}
        ).stream()

    def compand(
        self,
        *,
        attacks: list[str],
        decays: list[str],
        points: list[str],
        soft_knee: float,
        gain: float,
        volume: float,
        delay: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.77 compand Compress or expand the audio’s dynamic range. It accepts the following parameters:

        Parameters:
        ----------
        attacks:
            A list of times in seconds for each channel over which the instantaneous level of the input signal is averaged to determine its volume. attacks refers to increase of volume and decays refers to decrease of volume. For most situations, the attack time (response to the audio getting louder) should be shorter than the decay time, because the human ear is more sensitive to sudden loud audio than sudden soft audio. A typical value for attack is 0.3 seconds and a typical value for decay is 0.8 seconds. If specified number of attacks & decays is lower than number of channels, the last set attack/decay will be used for all remaining channels.
        decays:
            A list of times in seconds for each channel over which the instantaneous level of the input signal is averaged to determine its volume. attacks refers to increase of volume and decays refers to decrease of volume. For most situations, the attack time (response to the audio getting louder) should be shorter than the decay time, because the human ear is more sensitive to sudden loud audio than sudden soft audio. A typical value for attack is 0.3 seconds and a typical value for decay is 0.8 seconds. If specified number of attacks & decays is lower than number of channels, the last set attack/decay will be used for all remaining channels.
        points:
            A list of points for the transfer function, specified in dB relative to the maximum possible signal amplitude. Each key points list must be defined using the following syntax: x0/y0|x1/y1|x2/y2|.... or x0/y0 x1/y1 x2/y2 .... The input values must be in strictly increasing order but the transfer function does not have to be monotonically rising. The point 0/0 is assumed but may be overridden (by 0/out-dBn). Typical values for the transfer function are -70/-70|-60/-20|1/0.
        soft_knee:
            Set the curve radius in dB for all joints. It defaults to 0.01.
        gain:
            Set the additional gain in dB to be applied at all points on the transfer function. This allows for easy adjustment of the overall gain. It defaults to 0.
        volume:
            Set an initial volume, in dB, to be assumed for each channel when filtering starts. This permits the user to supply a nominal level initially, so that, for example, a very large gain is not applied to initial signal levels before the companding has begun to operate. A typical value for audio which is initially quiet is -90 dB. It defaults to 0.
        delay:
            Set a delay, in seconds. The input audio is analyzed immediately, but audio is delayed before being fed to the volume adjuster. Specifying a delay approximately equal to the attack/decay times allows the filter to effectively operate in predictive rather than reactive mode. It defaults to 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compand

        """
        return FilterNode(
            *[self],
            name="compand",
            kwargs={
                "attacks": attacks,
                "decays": decays,
                "points": points,
                "soft-knee": soft_knee,
                "gain": gain,
                "volume": volume,
                "delay": delay,
                **kwargs,
            }
        ).stream()

    def compensationdelay(
        self,
        *,
        mm: int = None,
        cm: int = None,
        m: int = None,
        dry: float = None,
        wet: float = None,
        temp: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.78 compensationdelay Compensation Delay Line is a metric based delay to compensate differing positions of microphones or speakers. For example, you have recorded guitar with two microphones placed in different locations. Because the front of sound wave has fixed speed in normal conditions, the phasing of microphones can vary and depends on their location and interposition. The best sound mix can be achieved when these microphones are in phase (synchronized). Note that a distance of ~30 cm between microphones makes one microphone capture the signal in antiphase to the other microphone. That makes the final mix sound moody. This filter helps to solve phasing problems by adding different delays to each microphone track and make them synchronized. The best result can be reached when you take one track as base and synchronize other tracks one by one with it. Remember that synchronization/delay tolerance depends on sample rate, too. Higher sample rates will give more tolerance. The filter accepts the following parameters:

        Parameters:
        ----------
        mm:
            Set millimeters distance. This is compensation distance for fine tuning. Default is 0.
        cm:
            Set cm distance. This is compensation distance for tightening distance setup. Default is 0.
        m:
            Set meters distance. This is compensation distance for hard distance setup. Default is 0.
        dry:
            Set dry amount. Amount of unprocessed (dry) signal. Default is 0.
        wet:
            Set wet amount. Amount of processed (wet) signal. Default is 1.
        temp:
            Set temperature in degrees Celsius. This is the temperature of the environment. Default is 20.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#compensationdelay

        """
        return FilterNode(
            *[self],
            name="compensationdelay",
            kwargs={"mm": mm, "cm": cm, "m": m, "dry": dry, "wet": wet, "temp": temp, **kwargs}
        ).stream()

    def convolution(
        self,
        *,
        _0m: list[str],
        _1m: list[str],
        _2m: list[str],
        _3m: list[str],
        _0rdiv: float,
        _1rdiv: float,
        _2rdiv: float,
        _3rdiv: float,
        _0bias: float,
        _1bias: float,
        _2bias: float,
        _3bias: float,
        _0mode: str,
        _1mode: str,
        _2mode: str,
        _3mode: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.44 convolution Apply convolution of 3x3, 5x5, 7x7 or horizontal/vertical up to 49 elements. The filter accepts the following options:

        Parameters:
        ----------
        _0m:
            Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        _1m:
            Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        _2m:
            Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        _3m:
            Set matrix for each plane. Matrix is sequence of 9, 25 or 49 signed integers in square mode, and from 1 to 49 odd number of signed integers in row mode.
        _0rdiv:
            Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        _1rdiv:
            Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        _2rdiv:
            Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        _3rdiv:
            Set multiplier for calculated value for each plane. If unset or 0, it will be sum of all matrix elements.
        _0bias:
            Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        _1bias:
            Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        _2bias:
            Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        _3bias:
            Set bias for each plane. This value is added to the result of the multiplication. Useful for making the overall image brighter or darker. Default is 0.0.
        _0mode:
            Set matrix mode for each plane. Can be square, row or column. Default is square.
        _1mode:
            Set matrix mode for each plane. Can be square, row or column. Default is square.
        _2mode:
            Set matrix mode for each plane. Can be square, row or column. Default is square.
        _3mode:
            Set matrix mode for each plane. Can be square, row or column. Default is square.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#convolution

        """
        return FilterNode(
            *[self],
            name="convolution",
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
                **kwargs,
            }
        ).stream()

    def convolve(self, *, planes: str = None, impulse: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.45 convolve Apply 2D convolution of video stream in frequency domain using second stream as impulse. The filter accepts the following options: The convolve filter also supports the framesync options.

        Parameters:
        ----------
        planes:
            Set which planes to process.
        impulse:
            Set which impulse video frames will be processed, can be first or all. Default is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#convolve

        """
        return FilterNode(*[self], name="convolve", kwargs={"planes": planes, "impulse": impulse, **kwargs}).stream()

    def copy(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.46 copy Copy the input video source unchanged to the output. This is mainly useful for testing purposes.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#copy

        """
        return FilterNode(*[self], name="copy", kwargs={**kwargs}).stream()

    def coreimage(self, *, list_filters: bool, filter: str, output_rect: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.47 coreimage Video filtering on GPU using Apple’s CoreImage API on OSX. Hardware acceleration is based on an OpenGL context. Usually, this means it is processed by video hardware. However, software-based OpenGL implementations exist which means there is no guarantee for hardware processing. It depends on the respective OSX. There are many filters and image generators provided by Apple that come with a large variety of options. The filter has to be referenced by its name along with its options. The coreimage filter accepts the following options: Several filters can be chained for successive processing without GPU-HOST transfers allowing for fast processing of complex filter chains. Currently, only filters with zero (generators) or exactly one (filters) input image and one output image are supported. Also, transition filters are not yet usable as intended. Some filters generate output images with additional padding depending on the respective filter kernel. The padding is automatically removed to ensure the filter output has the same size as the input image. For image generators, the size of the output image is determined by the previous output image of the filter chain or the input image of the whole filterchain, respectively. The generators do not use the pixel information of this image to generate their output. However, the generated output is blended onto this image, resulting in partial or complete coverage of the output image. The coreimagesrc video source can be used for generating input images which are directly fed into the filter chain. By using it, providing input images by another video source or an input video is not required.

        Parameters:
        ----------
        list_filters:
            List all available filters and generators along with all their respective options as well as possible minimum and maximum values along with the default values. list_filters=true
        filter:
            Specify all filters by their respective name and options. Use list_filters to determine all valid filter names and options. Numerical options are specified by a float value and are automatically clamped to their respective value range. Vector and color options have to be specified by a list of space separated float values. Character escaping has to be done. A special option name default is available to use default options for a filter. It is required to specify either default or at least one of the filter options. All omitted options are used with their default values. The syntax of the filter string is as follows: filter=<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...][#<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...]][#...]
        output_rect:
            Specify a rectangle where the output of the filter chain is copied into the input image. It is given by a list of space separated float values: output_rect=x\ y\ width\ height If not given, the output rectangle equals the dimensions of the input image. The output rectangle is automatically cropped at the borders of the input image. Negative values are valid for each component. output_rect=25\ 25\ 100\ 100



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#coreimage

        """
        return FilterNode(
            *[self],
            name="coreimage",
            kwargs={"list_filters": list_filters, "filter": filter, "output_rect": output_rect, **kwargs}
        ).stream()

    def corr(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.48 corr Obtain the correlation between two input videos. This filter takes two input videos. Both input videos must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The obtained per component, average, min and max correlation is printed through the logging system. The filter stores the calculated correlation of each frame in frame metadata. This filter also supports the framesync options. In the below example the input file main.mpg being processed is compared with the reference file ref.mpg. ffmpeg -i main.mpg -i ref.mpg -lavfi corr -f null -

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#corr

        """
        return FilterNode(*[self], name="corr", kwargs={**kwargs}).stream()

    def cover_rect(self, *, cover: str, mode: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.49 cover_rect Cover a rectangular object It accepts the following options:

        Parameters:
        ----------
        cover:
            Filepath of the optional cover image, needs to be in yuv420.
        mode:
            Set covering mode. It accepts the following values: ‘cover’ cover it by the supplied image ‘blur’ cover it by interpolating the surrounding pixels Default value is blur.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cover_005frect

        """
        return FilterNode(*[self], name="cover_rect", kwargs={"cover": cover, "mode": mode, **kwargs}).stream()

    def crop(
        self, *, w: str, h: str, x: str, y: str, keep_aspect: int, exact: int, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.50 crop Crop the input video to given dimensions. It accepts the following parameters: The out_w, out_h, x, y parameters are expressions containing the following constants: The expression for out_w may depend on the value of out_h, and the expression for out_h may depend on out_w, but they cannot depend on x and y, as x and y are evaluated after out_w and out_h. The x and y parameters specify the expressions for the position of the top-left corner of the output (non-cropped) area. They are evaluated for each frame. If the evaluated value is not valid, it is approximated to the nearest valid value. The expression for x may depend on y, and the expression for y may depend on x.

        Parameters:
        ----------
        w:
            The width of the output video. It defaults to iw. This expression is evaluated only once during the filter configuration, or when the ‘w’ or ‘out_w’ command is sent.
        h:
            The height of the output video. It defaults to ih. This expression is evaluated only once during the filter configuration, or when the ‘h’ or ‘out_h’ command is sent.
        x:
            The horizontal position, in the input video, of the left edge of the output video. It defaults to (in_w-out_w)/2. This expression is evaluated per-frame.
        y:
            The vertical position, in the input video, of the top edge of the output video. It defaults to (in_h-out_h)/2. This expression is evaluated per-frame.
        keep_aspect:
            If set to 1 will force the output display aspect ratio to be the same of the input, by changing the output sample aspect ratio. It defaults to 0.
        exact:
            Enable exact cropping. If enabled, subsampled videos will be cropped at exact width/height/x/y as specified and will not be rounded to nearest smaller value. It defaults to 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crop

        """
        return FilterNode(
            *[self],
            name="crop",
            kwargs={"w": w, "h": h, "x": x, "y": y, "keep_aspect": keep_aspect, "exact": exact, **kwargs}
        ).stream()

    def cropdetect(
        self,
        *,
        mode: str,
        limit: str = None,
        round: int = None,
        skip: int,
        reset_count: int = None,
        mv_threshold: int = None,
        low: float = None,
        high: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.51 cropdetectAuto-detect the crop size.It calculates the necessary cropping parameters and prints therecommended parameters via the logging system. The detected dimensionscorrespond to the non-black or video area of the input video according to mode.It accepts the following parameters:

        Parameters:
        ----------
        mode:
            Depending on mode crop detection is based on either the mere black value of surrounding pixels or a combination of motion vectors and edge pixels.‘black’Detect black pixels surrounding the playing video. For fine control use option limit.‘mvedges’Detect the playing video by the motion vectors inside the video and scanning for edge pixels typically forming the border of a playing video.
        limit:
            Set higher black value threshold, which can be optionally specifiedfrom nothing (0) to everything (255 for 8-bit based formats). An intensityvalue greater to the set value is considered non-black. It defaults to 24.You can also specify a value between 0.0 and 1.0 which will be scaled dependingon the bitdepth of the pixel format.
        round:
            The value which the width/height should be divisible by. It defaults to16. The offset is automatically adjusted to center the video. Use 2 toget only even dimensions (needed for 4:2:2 video). 16 is best whenencoding to most video codecs.
        skip:
            Set the number of initial frames for which evaluation is skipped.Default is 2. Range is 0 to INT_MAX.
        reset_count:
            Set the counter that determines after how many frames cropdetect willreset the previously detected largest video area and start over todetect the current optimal crop area. Default value is 0.This can be useful when channel logos distort the video area. 0indicates ’never reset’, and returns the largest area encountered duringplayback.
        mv_threshold:
            Set motion in pixel units as threshold for motion detection. It defaults to 8.
        low:
            Set low and high threshold values used by the Canny thresholdingalgorithm.The high threshold selects the "strong" edge pixels, which are thenconnected through 8-connectivity with the "weak" edge pixels selectedby the low threshold.low and high threshold values must be chosen in the range[0,1], and low should be lesser or equal to high.Default value for low is 5/255, and default value for highis 15/255.
        high:
            Set low and high threshold values used by the Canny thresholdingalgorithm.The high threshold selects the "strong" edge pixels, which are thenconnected through 8-connectivity with the "weak" edge pixels selectedby the low threshold.low and high threshold values must be chosen in the range[0,1], and low should be lesser or equal to high.Default value for low is 5/255, and default value for highis 15/255.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cropdetect

        """
        return FilterNode(
            *[self],
            name="cropdetect",
            kwargs={
                "mode": mode,
                "limit": limit,
                "round": round,
                "skip": skip,
                "reset_count": reset_count,
                "mv_threshold": mv_threshold,
                "low": low,
                "high": high,
                **kwargs,
            }
        ).stream()

    def crossfeed(
        self,
        *,
        strength: float = None,
        range: float = None,
        slope: float = None,
        level_in: float = None,
        level_out: float = None,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.79 crossfeed Apply headphone crossfeed filter. Crossfeed is the process of blending the left and right channels of stereo audio recording. It is mainly used to reduce extreme stereo separation of low frequencies. The intent is to produce more speaker like sound to the listener. The filter accepts the following options:

        Parameters:
        ----------
        strength:
            Set strength of crossfeed. Default is 0.2. Allowed range is from 0 to 1. This sets gain of low shelf filter for side part of stereo image. Default is -6dB. Max allowed is -30db when strength is set to 1.
        range:
            Set soundstage wideness. Default is 0.5. Allowed range is from 0 to 1. This sets cut off frequency of low shelf filter. Default is cut off near 1550 Hz. With range set to 1 cut off frequency is set to 2100 Hz.
        slope:
            Set curve slope of low shelf filter. Default is 0.5. Allowed range is from 0.01 to 1.
        level_in:
            Set input gain. Default is 0.9.
        level_out:
            Set output gain. Default is 1.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crossfeed

        """
        return FilterNode(
            *[self],
            name="crossfeed",
            kwargs={
                "strength": strength,
                "range": range,
                "slope": slope,
                "level_in": level_in,
                "level_out": level_out,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def crystalizer(self, *, i: float = None, c: bool = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.80 crystalizer Simple algorithm for audio noise sharpening. This filter linearly increases differences between each audio sample. The filter accepts the following options:

        Parameters:
        ----------
        i:
            Sets the intensity of effect (default: 2.0). Must be in range between -10.0 to 0 (unchanged sound) to 10.0 (maximum effect). To inverse filtering use negative value.
        c:
            Enable clipping. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#crystalizer

        """
        return FilterNode(*[self], name="crystalizer", kwargs={"i": i, "c": c, **kwargs}).stream()

    def cue(self, *, cue: int, preroll: float, buffer: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.52 cue Delay video filtering until a given wallclock timestamp. The filter first passes on preroll amount of frames, then it buffers at most buffer amount of frames and waits for the cue. After reaching the cue it forwards the buffered frames and also any subsequent frames coming in its input. The filter can be used synchronize the output of multiple ffmpeg processes for realtime output devices like decklink. By putting the delay in the filtering chain and pre-buffering frames the process can pass on data to output almost immediately after the target wallclock timestamp is reached. Perfect frame accuracy cannot be guaranteed, but the result is good enough for some use cases.

        Parameters:
        ----------
        cue:
            The cue timestamp expressed in a UNIX timestamp in microseconds. Default is 0.
        preroll:
            The duration of content to pass on as preroll expressed in seconds. Default is 0.
        buffer:
            The maximum duration of content to buffer before waiting for the cue expressed in seconds. Default is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#cue

        """
        return FilterNode(
            *[self], name="cue", kwargs={"cue": cue, "preroll": preroll, "buffer": buffer, **kwargs}
        ).stream()

    def curves(
        self,
        *,
        preset: str = None,
        master: str,
        red: str,
        green: str,
        blue: str,
        all: str,
        psfile: str,
        plot: str,
        interp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.53 curves Apply color adjustments using curves. This filter is similar to the Adobe Photoshop and GIMP curves tools. Each component (red, green and blue) has its values defined by N key points tied from each other using a smooth curve. The x-axis represents the pixel values from the input frame, and the y-axis the new pixel values to be set for the output frame. By default, a component curve is defined by the two points (0;0) and (1;1). This creates a straight line where each original pixel value is "adjusted" to its own value, which means no change to the image. The filter allows you to redefine these two points and add some more. A new curve will be define to pass smoothly through all these new coordinates. The new defined points needs to be strictly increasing over the x-axis, and their x and y values must be in the [0;1] interval. The curve is formed by using a natural or monotonic cubic spline interpolation, depending on the interp option (default: natural). The natural spline produces a smoother curve in general while the monotonic (pchip) spline guarantees the transitions between the specified points to be monotonic. If the computed curves happened to go outside the vector spaces, the values will be clipped accordingly. The filter accepts the following options: To avoid some filtergraph syntax conflicts, each key points list need to be defined using the following syntax: x0/y0 x1/y1 x2/y2 ....

        Parameters:
        ----------
        preset:
            Select one of the available color presets. This option can be used in addition to the r, g, b parameters; in this case, the later options takes priority on the preset values. Available presets are: ‘none’ ‘color_negative’ ‘cross_process’ ‘darker’ ‘increase_contrast’ ‘lighter’ ‘linear_contrast’ ‘medium_contrast’ ‘negative’ ‘strong_contrast’ ‘vintage’ Default is none.
        master:
            Set the master key points. These points will define a second pass mapping. It is sometimes called a "luminance" or "value" mapping. It can be used with r, g, b or all since it acts like a post-processing LUT.
        red:
            Set the key points for the red component.
        green:
            Set the key points for the green component.
        blue:
            Set the key points for the blue component.
        all:
            Set the key points for all components (not including master). Can be used in addition to the other key points component options. In this case, the unset component(s) will fallback on this all setting.
        psfile:
            Specify a Photoshop curves file (.acv) to import the settings from.
        plot:
            Save Gnuplot script of the curves in specified file.
        interp:
            Specify the kind of interpolation. Available algorithms are: ‘natural’ Natural cubic spline using a piece-wise cubic polynomial that is twice continuously differentiable. ‘pchip’ Monotonic cubic spline using a piecewise cubic Hermite interpolating polynomial (PCHIP).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#curves

        """
        return FilterNode(
            *[self],
            name="curves",
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
                **kwargs,
            }
        ).stream()

    def datascope(
        self,
        *,
        size: str,
        x: int,
        y: int,
        mode: str,
        axis: bool,
        opacity: float,
        format: str,
        components: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.54 datascope Video data analysis filter. This filter shows hexadecimal pixel values of part of video. The filter accepts the following options:

        Parameters:
        ----------
        size:
            Set output video size.
        x:
            Set x offset from where to pick pixels.
        y:
            Set y offset from where to pick pixels.
        mode:
            Set scope mode, can be one of the following: ‘mono’ Draw hexadecimal pixel values with white color on black background. ‘color’ Draw hexadecimal pixel values with input video pixel color on black background. ‘color2’ Draw hexadecimal pixel values on color background picked from input video, the text color is picked in such way so its always visible.
        axis:
            Draw rows and columns numbers on left and top of video.
        opacity:
            Set background opacity.
        format:
            Set display number format. Can be hex, or dec. Default is hex.
        components:
            Set pixel components to display. By default all pixel components are displayed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#datascope

        """
        return FilterNode(
            *[self],
            name="datascope",
            kwargs={
                "size": size,
                "x": x,
                "y": y,
                "mode": mode,
                "axis": axis,
                "opacity": opacity,
                "format": format,
                "components": components,
                **kwargs,
            }
        ).stream()

    def dblur(
        self, *, angle: float = None, radius: float = None, planes: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.55 dblur Apply Directional blur filter. The filter accepts the following options:

        Parameters:
        ----------
        angle:
            Set angle of directional blur. Default is 45.
        radius:
            Set radius of directional blur. Default is 5.
        planes:
            Set which planes to filter. By default all planes are filtered.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dblur

        """
        return FilterNode(
            *[self], name="dblur", kwargs={"angle": angle, "radius": radius, "planes": planes, **kwargs}
        ).stream()

    def dcshift(self, *, shift: float, limitergain: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.81 dcshift Apply a DC shift to the audio. This can be useful to remove a DC offset (caused perhaps by a hardware problem in the recording chain) from the audio. The effect of a DC offset is reduced headroom and hence volume. The astats filter can be used to determine if a signal has a DC offset.

        Parameters:
        ----------
        shift:
            Set the DC shift, allowed range is [-1, 1]. It indicates the amount to shift the audio.
        limitergain:
            Optional. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is used to prevent clipping.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dcshift

        """
        return FilterNode(
            *[self], name="dcshift", kwargs={"shift": shift, "limitergain": limitergain, **kwargs}
        ).stream()

    def dctdnoiz(self, *, sigma: float = None, overlap: int, expr: str, n: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.56 dctdnoiz Denoise frames using 2D DCT (frequency domain filtering). This filter is not designed for real time. The filter accepts the following options:

        Parameters:
        ----------
        sigma:
            Set the noise sigma constant. This sigma defines a hard threshold of 3 * sigma; every DCT coefficient (absolute value) below this threshold with be dropped. If you need a more advanced filtering, see expr. Default is 0.
        overlap:
            Set number overlapping pixels for each block. Since the filter can be slow, you may want to reduce this value, at the cost of a less effective filter and the risk of various artefacts. If the overlapping value doesn’t permit processing the whole input width or height, a warning will be displayed and according borders won’t be denoised. Default value is blocksize-1, which is the best possible setting.
        expr:
            Set the coefficient factor expression. For each coefficient of a DCT block, this expression will be evaluated as a multiplier value for the coefficient. If this is option is set, the sigma option will be ignored. The absolute value of the coefficient can be accessed through the c variable.
        n:
            Set the blocksize using the number of bits. 1<<n defines the blocksize, which is the width and height of the processed blocks. The default value is 3 (8x8) and can be raised to 4 for a blocksize of 16x16. Note that changing this setting has huge consequences on the speed processing. Also, a larger block size does not necessarily means a better de-noising.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dctdnoiz

        """
        return FilterNode(
            *[self], name="dctdnoiz", kwargs={"sigma": sigma, "overlap": overlap, "expr": expr, "n": n, **kwargs}
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.57 deband Remove banding artifacts from input video. It works by replacing banded pixels with average value of referenced pixels. The filter accepts the following options:

        Parameters:
        ----------
        _1thr:
            Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        _2thr:
            Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        _3thr:
            Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        _4thr:
            Set banding detection threshold for each plane. Default is 0.02. Valid range is 0.00003 to 0.5. If difference between current pixel and reference pixel is less than threshold, it will be considered as banded.
        range:
            Banding detection range in pixels. Default is 16. If positive, random number in range 0 to set value will be used. If negative, exact absolute value will be used. The range defines square of four pixels around current pixel.
        direction:
            Set direction in radians from which four pixel will be compared. If positive, random direction from 0 to set direction will be picked. If negative, exact of absolute value will be picked. For example direction 0, -PI or -2*PI radians will pick only pixels on same row and -PI/2 will pick only pixels on same column.
        blur:
            If enabled, current pixel is compared with average value of all four surrounding pixels. The default is enabled. If disabled current pixel is compared with all four surrounding pixels. The pixel is considered banded if only all four differences with surrounding pixels are less than threshold.
        coupling:
            If enabled, current pixel is changed if and only if all pixel components are banded, e.g. banding detection threshold is triggered for all color components. The default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deband

        """
        return FilterNode(
            *[self],
            name="deband",
            kwargs={
                "1thr": _1thr,
                "2thr": _2thr,
                "3thr": _3thr,
                "4thr": _4thr,
                "range": range,
                "direction": direction,
                "blur": blur,
                "coupling": coupling,
                **kwargs,
            }
        ).stream()

    def deblock(
        self,
        *,
        filter: str = None,
        block: int = None,
        alpha: float = None,
        beta: float = None,
        gamma: float = None,
        delta: float = None,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.58 deblock Remove blocking artifacts from input video. The filter accepts the following options:

        Parameters:
        ----------
        filter:
            Set filter type, can be weak or strong. Default is strong. This controls what kind of deblocking is applied.
        block:
            Set size of block, allowed range is from 4 to 512. Default is 8.
        alpha:
            Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        beta:
            Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        gamma:
            Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        delta:
            Set blocking detection thresholds. Allowed range is 0 to 1. Defaults are: 0.098 for alpha and 0.05 for the rest. Using higher threshold gives more deblocking strength. Setting alpha controls threshold detection at exact edge of block. Remaining options controls threshold detection near the edge. Each one for below/above or left/right. Setting any of those to 0 disables deblocking.
        planes:
            Set planes to filter. Default is to filter all available planes.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deblock

        """
        return FilterNode(
            *[self],
            name="deblock",
            kwargs={
                "filter": filter,
                "block": block,
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
                "delta": delta,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def decimate(
        self,
        *,
        cycle: int = None,
        dupthresh: float = None,
        scthresh: int = None,
        blockx: int = None,
        blocky: int = None,
        ppsrc: int = None,
        chroma: int = None,
        mixed: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.59 decimate Drop duplicated frames at regular intervals. The filter accepts the following options:

        Parameters:
        ----------
        cycle:
            Set the number of frames from which one will be dropped. Setting this to N means one frame in every batch of N frames will be dropped. Default is 5.
        dupthresh:
            Set the threshold for duplicate detection. If the difference metric for a frame is less than or equal to this value, then it is declared as duplicate. Default is 1.1
        scthresh:
            Set scene change threshold. Default is 15.
        blockx:
            Set the size of the x and y-axis blocks used during metric calculations. Larger blocks give better noise suppression, but also give worse detection of small movements. Must be a power of two. Default is 32.
        blocky:
            Set the size of the x and y-axis blocks used during metric calculations. Larger blocks give better noise suppression, but also give worse detection of small movements. Must be a power of two. Default is 32.
        ppsrc:
            Mark main input as a pre-processed input and activate clean source input stream. This allows the input to be pre-processed with various filters to help the metrics calculation while keeping the frame selection lossless. When set to 1, the first stream is for the pre-processed input, and the second stream is the clean source from where the kept frames are chosen. Default is 0.
        chroma:
            Set whether or not chroma is considered in the metric calculations. Default is 1.
        mixed:
            Set whether or not the input only partially contains content to be decimated. Default is false. If enabled video output stream will be in variable frame rate.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#decimate

        """
        return FilterNode(
            *[self],
            name="decimate",
            kwargs={
                "cycle": cycle,
                "dupthresh": dupthresh,
                "scthresh": scthresh,
                "blockx": blockx,
                "blocky": blocky,
                "ppsrc": ppsrc,
                "chroma": chroma,
                "mixed": mixed,
                **kwargs,
            }
        ).stream()

    def deconvolve(
        self, *, planes: str = None, impulse: str = None, noise: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.60 deconvolve Apply 2D deconvolution of video stream in frequency domain using second stream as impulse. The filter accepts the following options: The deconvolve filter also supports the framesync options.

        Parameters:
        ----------
        planes:
            Set which planes to process.
        impulse:
            Set which impulse video frames will be processed, can be first or all. Default is all.
        noise:
            Set noise when doing divisions. Default is 0.0000001. Useful when width and height are not same and not power of 2 or if stream prior to convolving had noise.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deconvolve

        """
        return FilterNode(
            *[self], name="deconvolve", kwargs={"planes": planes, "impulse": impulse, "noise": noise, **kwargs}
        ).stream()

    def dedot(self, *, m: str, lt: float, tl: float, tc: float, ct: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.61 dedot Reduce cross-luminance (dot-crawl) and cross-color (rainbows) from video. It accepts the following options:

        Parameters:
        ----------
        m:
            Set mode of operation. Can be combination of dotcrawl for cross-luminance reduction and/or rainbows for cross-color reduction.
        lt:
            Set spatial luma threshold. Lower values increases reduction of cross-luminance.
        tl:
            Set tolerance for temporal luma. Higher values increases reduction of cross-luminance.
        tc:
            Set tolerance for chroma temporal variation. Higher values increases reduction of cross-color.
        ct:
            Set temporal chroma threshold. Lower values increases reduction of cross-color.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dedot

        """
        return FilterNode(
            *[self], name="dedot", kwargs={"m": m, "lt": lt, "tl": tl, "tc": tc, "ct": ct, **kwargs}
        ).stream()

    def deesser(
        self, *, i: float = None, m: float = None, f: float = None, s: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.82 deesser Apply de-essing to the audio samples.

        Parameters:
        ----------
        i:
            Set intensity for triggering de-essing. Allowed range is from 0 to 1. Default is 0.
        m:
            Set amount of ducking on treble part of sound. Allowed range is from 0 to 1. Default is 0.5.
        f:
            How much of original frequency content to keep when de-essing. Allowed range is from 0 to 1. Default is 0.5.
        s:
            Set the output mode. It accepts the following values: i Pass input unchanged. o Pass ess filtered out. e Pass only ess. Default value is o.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deesser

        """
        return FilterNode(*[self], name="deesser", kwargs={"i": i, "m": m, "f": f, "s": s, **kwargs}).stream()

    def deflate(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.62 deflate Apply deflate effect to the video. This filter replaces the pixel by the local(3x3) average by taking into account only values lower than the pixel. It accepts the following options:

        Parameters:
        ----------
        threshold0:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold1:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold2:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold3:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflate

        """
        return FilterNode(
            *[self],
            name="deflate",
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
                **kwargs,
            }
        ).stream()

    def deflicker(
        self, *, size: int = None, mode: str = None, bypass: bool = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.63 deflicker Remove temporal frame luminance variations. It accepts the following options:

        Parameters:
        ----------
        size:
            Set moving-average filter size in frames. Default is 5. Allowed range is 2 - 129.
        mode:
            Set averaging mode to smooth temporal luminance variations. Available values are: ‘am’ Arithmetic mean ‘gm’ Geometric mean ‘hm’ Harmonic mean ‘qm’ Quadratic mean ‘cm’ Cubic mean ‘pm’ Power mean ‘median’ Median
        bypass:
            Do not actually modify frame. Useful when one only wants metadata.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deflicker

        """
        return FilterNode(
            *[self], name="deflicker", kwargs={"size": size, "mode": mode, "bypass": bypass, **kwargs}
        ).stream()

    def dejudder(self, *, cycle: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.64 dejudder Remove judder produced by partially interlaced telecined content. Judder can be introduced, for instance, by pullup filter. If the original source was partially telecined content then the output of pullup,dejudder will have a variable frame rate. May change the recorded frame rate of the container. Aside from that change, this filter will not affect constant frame rate video. The option available in this filter is:

        Parameters:
        ----------
        cycle:
            Specify the length of the window over which the judder repeats. Accepts any integer greater than 1. Useful values are: ‘4’ If the original was telecined from 24 to 30 fps (Film to NTSC). ‘5’ If the original was telecined from 25 to 30 fps (PAL to NTSC). ‘20’ If a mixture of the two. The default is ‘4’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dejudder

        """
        return FilterNode(*[self], name="dejudder", kwargs={"cycle": cycle, **kwargs}).stream()

    def delogo(self, *, x: int, y: int, w: int, h: int, show: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.65 delogo Suppress a TV station logo by a simple interpolation of the surrounding pixels. Just set a rectangle covering the logo and watch it disappear (and sometimes something even uglier appear - your mileage may vary). It accepts the following parameters:

        Parameters:
        ----------
        x:
            Specify the top left corner coordinates of the logo. They must be specified.
        y:
            Specify the top left corner coordinates of the logo. They must be specified.
        w:
            Specify the width and height of the logo to clear. They must be specified.
        h:
            Specify the width and height of the logo to clear. They must be specified.
        show:
            When set to 1, a green rectangle is drawn on the screen to simplify finding the right x, y, w, and h parameters. The default value is 0. The rectangle is drawn on the outermost pixels which will be (partly) replaced with interpolated values. The values of the next pixels immediately outside this rectangle in each direction will be used to compute the interpolated pixel values inside the rectangle.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#delogo

        """
        return FilterNode(
            *[self], name="delogo", kwargs={"x": x, "y": y, "w": w, "h": h, "show": show, **kwargs}
        ).stream()

    def derain(self, *, filter_type: str = None, dnn_backend: str, model: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.66 derain Remove the rain in the input image/video by applying the derain methods based on convolutional neural networks. Supported models: Recurrent Squeeze-and-Excitation Context Aggregation Net (RESCAN). See http://openaccess.thecvf.com/content_ECCV_2018/papers/Xia_Li_Recurrent_Squeeze-and-Excitation_Context_ECCV_2018_paper.pdf. Training as well as model generation scripts are provided in the repository at https://github.com/XueweiMeng/derain_filter.git. The filter accepts the following options: To get full functionality (such as async execution), please use the dnn_processing filter.

        Parameters:
        ----------
        filter_type:
            Specify which filter to use. This option accepts the following values: ‘derain’ Derain filter. To conduct derain filter, you need to use a derain model. ‘dehaze’ Dehaze filter. To conduct dehaze filter, you need to use a dehaze model. Default value is ‘derain’.
        dnn_backend:
            Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        model:
            Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow can load files for only its format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#derain

        """
        return FilterNode(
            *[self],
            name="derain",
            kwargs={"filter_type": filter_type, "dnn_backend": dnn_backend, "model": model, **kwargs}
        ).stream()

    def deshake(
        self,
        *,
        x: int = None,
        y: int = None,
        w: int = None,
        h: int = None,
        rx: int = None,
        ry: int = None,
        edge: str = None,
        blocksize: int = None,
        contrast: int = None,
        search: str = None,
        filename: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.67 deshake Attempt to fix small changes in horizontal and/or vertical shift. This filter helps remove camera shake from hand-holding a camera, bumping a tripod, moving on a vehicle, etc. The filter accepts the following options:

        Parameters:
        ----------
        x:
            Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        y:
            Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        w:
            Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        h:
            Specify a rectangular area where to limit the search for motion vectors. If desired the search for motion vectors can be limited to a rectangular area of the frame defined by its top left corner, width and height. These parameters have the same meaning as the drawbox filter which can be used to visualise the position of the bounding box. This is useful when simultaneous movement of subjects within the frame might be confused for camera motion by the motion vector search. If any or all of x, y, w and h are set to -1 then the full frame is used. This allows later options to be set without specifying the bounding box for the motion vector search. Default - search the whole frame.
        rx:
            Specify the maximum extent of movement in x and y directions in the range 0-64 pixels. Default 16.
        ry:
            Specify the maximum extent of movement in x and y directions in the range 0-64 pixels. Default 16.
        edge:
            Specify how to generate pixels to fill blanks at the edge of the frame. Available values are: ‘blank, 0’ Fill zeroes at blank locations ‘original, 1’ Original image at blank locations ‘clamp, 2’ Extruded edge value at blank locations ‘mirror, 3’ Mirrored edge at blank locations Default value is ‘mirror’.
        blocksize:
            Specify the blocksize to use for motion search. Range 4-128 pixels, default 8.
        contrast:
            Specify the contrast threshold for blocks. Only blocks with more than the specified contrast (difference between darkest and lightest pixels) will be considered. Range 1-255, default 125.
        search:
            Specify the search strategy. Available values are: ‘exhaustive, 0’ Set exhaustive search ‘less, 1’ Set less exhaustive search. Default value is ‘exhaustive’.
        filename:
            If set then a detailed log of the motion search is written to the specified file.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#deshake

        """
        return FilterNode(
            *[self],
            name="deshake",
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
                **kwargs,
            }
        ).stream()

    def despill(
        self,
        *,
        type: str,
        mix: str,
        expand: float,
        red: float,
        green: float,
        blue: float,
        brightness: float,
        alpha: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.68 despill Remove unwanted contamination of foreground colors, caused by reflected color of greenscreen or bluescreen. This filter accepts the following options:

        Parameters:
        ----------
        type:
            Set what type of despill to use.
        mix:
            Set how spillmap will be generated.
        expand:
            Set how much to get rid of still remaining spill.
        red:
            Controls amount of red in spill area.
        green:
            Controls amount of green in spill area. Should be -1 for greenscreen.
        blue:
            Controls amount of blue in spill area. Should be -1 for bluescreen.
        brightness:
            Controls brightness of spill area, preserving colors.
        alpha:
            Modify alpha from generated spillmap.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#despill

        """
        return FilterNode(
            *[self],
            name="despill",
            kwargs={
                "type": type,
                "mix": mix,
                "expand": expand,
                "red": red,
                "green": green,
                "blue": blue,
                "brightness": brightness,
                "alpha": alpha,
                **kwargs,
            }
        ).stream()

    def detelecine(
        self, *, first_field: str = None, pattern: str = None, start_frame: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.69 detelecine Apply an exact inverse of the telecine operation. It requires a predefined pattern specified using the pattern option which must be the same as that passed to the telecine filter. This filter accepts the following options:

        Parameters:
        ----------
        first_field:
            ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        pattern:
            A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.
        start_frame:
            A number representing position of the first frame with respect to the telecine pattern. This is to be used if the stream is cut. The default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#detelecine

        """
        return FilterNode(
            *[self],
            name="detelecine",
            kwargs={"first_field": first_field, "pattern": pattern, "start_frame": start_frame, **kwargs}
        ).stream()

    def dialoguenhance(
        self, *, original: float = None, enhance: float = None, voice: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.83 dialoguenhance Enhance dialogue in stereo audio. This filter accepts stereo input and produce surround (3.0) channels output. The newly produced front center channel have enhanced speech dialogue originally available in both stereo channels. This filter outputs front left and front right channels same as available in stereo input. The filter accepts the following options:

        Parameters:
        ----------
        original:
            Set the original center factor to keep in front center channel output. Allowed range is from 0 to 1. Default value is 1.
        enhance:
            Set the dialogue enhance factor to put in front center channel output. Allowed range is from 0 to 3. Default value is 1.
        voice:
            Set the voice detection factor. Allowed range is from 2 to 32. Default value is 2.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance

        """
        return FilterNode(
            *[self], name="dialoguenhance", kwargs={"original": original, "enhance": enhance, "voice": voice, **kwargs}
        ).stream()

    def dilation(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        coordinates: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.70 dilation Apply dilation effect to the video. This filter replaces the pixel by the local(3x3) maximum. It accepts the following options:

        Parameters:
        ----------
        threshold0:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold1:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold2:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold3:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        coordinates:
            Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dilation

        """
        return FilterNode(
            *[self],
            name="dilation",
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
                "coordinates": coordinates,
                **kwargs,
            }
        ).stream()

    def displace(self, *, edge: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.71 displace Displace pixels as indicated by second and third input stream. It takes three input streams and outputs one stream, the first input is the source, and second and third input are displacement maps. The second input specifies how much to displace pixels along the x-axis, while the third input specifies how much to displace pixels along the y-axis. If one of displacement map streams terminates, last frame from that displacement map will be used. Note that once generated, displacements maps can be reused over and over again. A description of the accepted options follows.

        Parameters:
        ----------
        edge:
            Set displace behavior for pixels that are out of range. Available values are: ‘blank’ Missing pixels are replaced by black pixels. ‘smear’ Adjacent pixels will spread out to replace missing pixels. ‘wrap’ Out of range pixels are wrapped so they point to pixels of other side. ‘mirror’ Out of range pixels will be replaced with mirrored pixels. Default is ‘smear’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#displace

        """
        return FilterNode(*[self], name="displace", kwargs={"edge": edge, **kwargs}).stream()

    def dnn_classify(
        self,
        *,
        dnn_backend: str,
        model: str,
        input: str,
        output: str,
        confidence: float = None,
        labels: str,
        backend_configs: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.72 dnn_classify Do classification with deep neural networks based on bounding boxes. The filter accepts the following options:

        Parameters:
        ----------
        dnn_backend:
            Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        model:
            Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        input:
            Set the input name of the dnn network.
        output:
            Set the output name of the dnn network.
        confidence:
            Set the confidence threshold (default: 0.5).
        labels:
            Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0, and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        backend_configs:
            Set the configs to be passed into backend For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs for your system.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fclassify

        """
        return FilterNode(
            *[self],
            name="dnn_classify",
            kwargs={
                "dnn_backend": dnn_backend,
                "model": model,
                "input": input,
                "output": output,
                "confidence": confidence,
                "labels": labels,
                "backend_configs": backend_configs,
                **kwargs,
            }
        ).stream()

    def dnn_detect(
        self,
        *,
        dnn_backend: str,
        model: str,
        input: str,
        output: str,
        confidence: float = None,
        labels: str,
        backend_configs: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.73 dnn_detect Do object detection with deep neural networks. The filter accepts the following options:

        Parameters:
        ----------
        dnn_backend:
            Specify which DNN backend to use for model loading and execution. This option accepts only openvino now, tensorflow backends will be added.
        model:
            Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats.
        input:
            Set the input name of the dnn network.
        output:
            Set the output name of the dnn network.
        confidence:
            Set the confidence threshold (default: 0.5).
        labels:
            Set path to label file specifying the mapping between label id and name. Each label name is written in one line, tailing spaces and empty lines are skipped. The first line is the name of label id 0 (usually it is ’background’), and the second line is the name of label id 1, etc. The label id is considered as name if the label file is not provided.
        backend_configs:
            Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fdetect

        """
        return FilterNode(
            *[self],
            name="dnn_detect",
            kwargs={
                "dnn_backend": dnn_backend,
                "model": model,
                "input": input,
                "output": output,
                "confidence": confidence,
                "labels": labels,
                "backend_configs": backend_configs,
                **kwargs,
            }
        ).stream()

    def dnn_processing(
        self, *, dnn_backend: str, model: str, input: str, output: str, backend_configs: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.74 dnn_processing Do image processing with deep neural networks. It works together with another filter which converts the pixel format of the Frame to what the dnn network requires. The filter accepts the following options:

        Parameters:
        ----------
        dnn_backend:
            Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow ‘openvino’ OpenVINO backend. To enable this backend you need to build and install the OpenVINO for C library (see https://github.com/openvinotoolkit/openvino/blob/master/build-instruction.md) and configure FFmpeg with --enable-libopenvino (–extra-cflags=-I... –extra-ldflags=-L... might be needed if the header files and libraries are not installed into system path)
        model:
            Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        input:
            Set the input name of the dnn network.
        output:
            Set the output name of the dnn network.
        backend_configs:
            Set the configs to be passed into backend. To use async execution, set async (default: set). Roll back to sync execution if the backend does not support async. For tensorflow backend, you can set its configs with sess_config options, please use tools/python/tf_sess_config.py to get the configs of TensorFlow backend for your system.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dnn_005fprocessing

        """
        return FilterNode(
            *[self],
            name="dnn_processing",
            kwargs={
                "dnn_backend": dnn_backend,
                "model": model,
                "input": input,
                "output": output,
                "backend_configs": backend_configs,
                **kwargs,
            }
        ).stream()

    def doubleweave(self, *, first_field: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.284 weave, doubleweave The weave takes a field-based video input and join each two sequential fields into single frame, producing a new double height clip with half the frame rate and half the frame count. The doubleweave works same as weave but without halving frame rate and frame count. It accepts the following option:

        Parameters:
        ----------
        first_field:
            Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        return FilterNode(*[self], name="doubleweave", kwargs={"first_field": first_field, **kwargs}).stream()

    def drawbox(
        self,
        *,
        x: str,
        y: str,
        width: str,
        height: str,
        color: str,
        thickness: str,
        replace: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.75 drawbox Draw a colored box on the input image. It accepts the following parameters: The parameters for x, y, w and h and t are expressions containing the following constants:

        Parameters:
        ----------
        x:
            The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        y:
            The expressions which specify the top left corner coordinates of the box. It defaults to 0.
        width:
            The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        height:
            The expressions which specify the width and height of the box; if 0 they are interpreted as the input width and height. It defaults to 0.
        color:
            Specify the color of the box to write. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the box edge color is the same as the video with inverted luma.
        thickness:
            The expression which sets the thickness of the box edge. A value of fill will create a filled box. Default value is 3. See below for the list of accepted constants.
        replace:
            Applicable if the input has alpha. With value 1, the pixels of the painted box will overwrite the video’s color and alpha pixels. Default is 0, which composites the box onto the input, leaving the video’s alpha intact.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawbox

        """
        return FilterNode(
            *[self],
            name="drawbox",
            kwargs={
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
                "thickness": thickness,
                "replace": replace,
                **kwargs,
            }
        ).stream()

    def drawgraph(
        self,
        *,
        m1: str,
        fg1: str,
        m2: str,
        fg2: str,
        m3: str,
        fg3: str,
        m4: str,
        fg4: str,
        min: float,
        max: float,
        bg: str,
        mode: str = None,
        slide: str = None,
        size: str,
        rate: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.76 drawgraph Draw a graph using input video metadata. It accepts the following parameters: Example using metadata from signalstats filter: signalstats,drawgraph=lavfi.signalstats.YAVG:min=0:max=255 Example using metadata from ebur128 filter: ebur128=metadata=1,adrawgraph=lavfi.r128.M:min=-120:max=5

        Parameters:
        ----------
        m1:
            Set 1st frame metadata key from which metadata values will be used to draw a graph.
        fg1:
            Set 1st foreground color expression.
        m2:
            Set 2nd frame metadata key from which metadata values will be used to draw a graph.
        fg2:
            Set 2nd foreground color expression.
        m3:
            Set 3rd frame metadata key from which metadata values will be used to draw a graph.
        fg3:
            Set 3rd foreground color expression.
        m4:
            Set 4th frame metadata key from which metadata values will be used to draw a graph.
        fg4:
            Set 4th foreground color expression.
        min:
            Set minimal value of metadata value.
        max:
            Set maximal value of metadata value.
        bg:
            Set graph background color. Default is white.
        mode:
            Set graph mode. Available values for mode is: ‘bar’ ‘dot’ ‘line’ Default is line.
        slide:
            Set slide mode. Available values for slide is: ‘frame’ Draw new frame when right border is reached. ‘replace’ Replace old columns with new ones. ‘scroll’ Scroll from right to left. ‘rscroll’ Scroll from left to right. ‘picture’ Draw single picture. Default is frame.
        size:
            Set size of graph video. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. The default value is 900x256.
        rate:
            Set the output frame rate. Default value is 25. The foreground color expressions can use the following variables: MIN Minimal value of metadata value. MAX Maximal value of metadata value. VAL Current metadata key value. The color is defined as 0xAABBGGRR.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawgraph

        """
        return FilterNode(
            *[self],
            name="drawgraph",
            kwargs={
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "min": min,
                "max": max,
                "bg": bg,
                "mode": mode,
                "slide": slide,
                "size": size,
                "rate": rate,
                **kwargs,
            }
        ).stream()

    def drawgrid(
        self,
        *,
        x: str,
        y: str,
        width: str,
        height: str,
        color: str,
        thickness: str,
        replace: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.77 drawgrid Draw a grid on the input image. It accepts the following parameters: The parameters for x, y, w and h and t are expressions containing the following constants:

        Parameters:
        ----------
        x:
            The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        y:
            The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
        width:
            The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        height:
            The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the input width and height, respectively, minus thickness, so image gets framed. Default to 0.
        color:
            Specify the color of the grid. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value invert is used, the grid color is the same as the video with inverted luma.
        thickness:
            The expression which sets the thickness of the grid line. Default value is 1. See below for the list of accepted constants.
        replace:
            Applicable if the input has alpha. With 1 the pixels of the painted grid will overwrite the video’s color and alpha pixels. Default is 0, which composites the grid onto the input, leaving the video’s alpha intact.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawgrid

        """
        return FilterNode(
            *[self],
            name="drawgrid",
            kwargs={
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
                "thickness": thickness,
                "replace": replace,
                **kwargs,
            }
        ).stream()

    def drawtext(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.78 drawtext Draw a text string or text from a specified file on top of a video, using the libfreetype library. To enable compilation of this filter, you need to configure FFmpeg with --enable-libfreetype and --enable-libharfbuzz. To enable default font fallback and the font option you need to configure FFmpeg with --enable-libfontconfig. To enable the text_shaping option, you need to configure FFmpeg with --enable-libfribidi.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drawtext

        """
        return FilterNode(*[self], name="drawtext", kwargs={**kwargs}).stream()

    def drmeter(self, *, length: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.84 drmeter Measure audio dynamic range. DR values of 14 and higher is found in very dynamic material. DR of 8 to 13 is found in transition material. And anything less that 8 have very poor dynamics and is very compressed. The filter accepts the following options:

        Parameters:
        ----------
        length:
            Set window length in seconds used to split audio into segments of equal length. Default is 3 seconds.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#drmeter

        """
        return FilterNode(*[self], name="drmeter", kwargs={"length": length, **kwargs}).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.85 dynaudnorm Dynamic Audio Normalizer. This filter applies a certain amount of gain to the input audio in order to bring its peak magnitude to a target level (e.g. 0 dBFS). However, in contrast to more "simple" normalization algorithms, the Dynamic Audio Normalizer *dynamically* re-adjusts the gain factor to the input audio. This allows for applying extra gain to the "quiet" sections of the audio while avoiding distortions or clipping the "loud" sections. In other words: The Dynamic Audio Normalizer will "even out" the volume of quiet and loud sections, in the sense that the volume of each section is brought to the same target level. Note, however, that the Dynamic Audio Normalizer achieves this goal *without* applying "dynamic range compressing". It will retain 100% of the dynamic range *within* each section of the audio file.

        Parameters:
        ----------
        framelen:
            Set the frame length in milliseconds. In range from 10 to 8000 milliseconds. Default is 500 milliseconds. The Dynamic Audio Normalizer processes the input audio in small chunks, referred to as frames. This is required, because a peak magnitude has no meaning for just a single sample value. Instead, we need to determine the peak magnitude for a contiguous sequence of sample values. While a "standard" normalizer would simply use the peak magnitude of the complete file, the Dynamic Audio Normalizer determines the peak magnitude individually for each frame. The length of a frame is specified in milliseconds. By default, the Dynamic Audio Normalizer uses a frame length of 500 milliseconds, which has been found to give good results with most files. Note that the exact frame length, in number of samples, will be determined automatically, based on the sampling rate of the individual input audio file.
        gausssize:
            Set the Gaussian filter window size. In range from 3 to 301, must be odd number. Default is 31. Probably the most important parameter of the Dynamic Audio Normalizer is the window size of the Gaussian smoothing filter. The filter’s window size is specified in frames, centered around the current frame. For the sake of simplicity, this must be an odd number. Consequently, the default value of 31 takes into account the current frame, as well as the 15 preceding frames and the 15 subsequent frames. Using a larger window results in a stronger smoothing effect and thus in less gain variation, i.e. slower gain adaptation. Conversely, using a smaller window results in a weaker smoothing effect and thus in more gain variation, i.e. faster gain adaptation. In other words, the more you increase this value, the more the Dynamic Audio Normalizer will behave like a "traditional" normalization filter. On the contrary, the more you decrease this value, the more the Dynamic Audio Normalizer will behave like a dynamic range compressor.
        peak:
            Set the target peak value. This specifies the highest permissible magnitude level for the normalized audio input. This filter will try to approach the target peak magnitude as closely as possible, but at the same time it also makes sure that the normalized signal will never exceed the peak magnitude. A frame’s maximum local gain factor is imposed directly by the target peak magnitude. The default value is 0.95 and thus leaves a headroom of 5%*. It is not recommended to go above this value.
        maxgain:
            Set the maximum gain factor. In range from 1.0 to 100.0. Default is 10.0. The Dynamic Audio Normalizer determines the maximum possible (local) gain factor for each input frame, i.e. the maximum gain factor that does not result in clipping or distortion. The maximum gain factor is determined by the frame’s highest magnitude sample. However, the Dynamic Audio Normalizer additionally bounds the frame’s maximum gain factor by a predetermined (global) maximum gain factor. This is done in order to avoid excessive gain factors in "silent" or almost silent frames. By default, the maximum gain factor is 10.0, For most inputs the default value should be sufficient and it usually is not recommended to increase this value. Though, for input with an extremely low overall volume level, it may be necessary to allow even higher gain factors. Note, however, that the Dynamic Audio Normalizer does not simply apply a "hard" threshold (i.e. cut off values above the threshold). Instead, a "sigmoid" threshold function will be applied. This way, the gain factors will smoothly approach the threshold value, but never exceed that value.
        targetrms:
            Set the target RMS. In range from 0.0 to 1.0. Default is 0.0 - disabled. By default, the Dynamic Audio Normalizer performs "peak" normalization. This means that the maximum local gain factor for each frame is defined (only) by the frame’s highest magnitude sample. This way, the samples can be amplified as much as possible without exceeding the maximum signal level, i.e. without clipping. Optionally, however, the Dynamic Audio Normalizer can also take into account the frame’s root mean square, abbreviated RMS. In electrical engineering, the RMS is commonly used to determine the power of a time-varying signal. It is therefore considered that the RMS is a better approximation of the "perceived loudness" than just looking at the signal’s peak magnitude. Consequently, by adjusting all frames to a constant RMS value, a uniform "perceived loudness" can be established. If a target RMS value has been specified, a frame’s local gain factor is defined as the factor that would result in exactly that RMS value. Note, however, that the maximum local gain factor is still restricted by the frame’s highest magnitude sample, in order to prevent clipping.
        coupling:
            Enable channels coupling. By default is enabled. By default, the Dynamic Audio Normalizer will amplify all channels by the same amount. This means the same gain factor will be applied to all channels, i.e. the maximum possible gain factor is determined by the "loudest" channel. However, in some recordings, it may happen that the volume of the different channels is uneven, e.g. one channel may be "quieter" than the other one(s). In this case, this option can be used to disable the channel coupling. This way, the gain factor will be determined independently for each channel, depending only on the individual channel’s highest magnitude sample. This allows for harmonizing the volume of the different channels.
        correctdc:
            Enable DC bias correction. By default is disabled. An audio signal (in the time domain) is a sequence of sample values. In the Dynamic Audio Normalizer these sample values are represented in the -1.0 to 1.0 range, regardless of the original input format. Normally, the audio signal, or "waveform", should be centered around the zero point. That means if we calculate the mean value of all samples in a file, or in a single frame, then the result should be 0.0 or at least very close to that value. If, however, there is a significant deviation of the mean value from 0.0, in either positive or negative direction, this is referred to as a DC bias or DC offset. Since a DC bias is clearly undesirable, the Dynamic Audio Normalizer provides optional DC bias correction. With DC bias correction enabled, the Dynamic Audio Normalizer will determine the mean value, or "DC correction" offset, of each input frame and subtract that value from all of the frame’s sample values which ensures those samples are centered around 0.0 again. Also, in order to avoid "gaps" at the frame boundaries, the DC correction offset values will be interpolated smoothly between neighbouring frames.
        altboundary:
            Enable alternative boundary mode. By default is disabled. The Dynamic Audio Normalizer takes into account a certain neighbourhood around each frame. This includes the preceding frames as well as the subsequent frames. However, for the "boundary" frames, located at the very beginning and at the very end of the audio file, not all neighbouring frames are available. In particular, for the first few frames in the audio file, the preceding frames are not known. And, similarly, for the last few frames in the audio file, the subsequent frames are not known. Thus, the question arises which gain factors should be assumed for the missing frames in the "boundary" region. The Dynamic Audio Normalizer implements two modes to deal with this situation. The default boundary mode assumes a gain factor of exactly 1.0 for the missing frames, resulting in a smooth "fade in" and "fade out" at the beginning and at the end of the input, respectively.
        compress:
            Set the compress factor. In range from 0.0 to 30.0. Default is 0.0. By default, the Dynamic Audio Normalizer does not apply "traditional" compression. This means that signal peaks will not be pruned and thus the full dynamic range will be retained within each local neighbourhood. However, in some cases it may be desirable to combine the Dynamic Audio Normalizer’s normalization algorithm with a more "traditional" compression. For this purpose, the Dynamic Audio Normalizer provides an optional compression (thresholding) function. If (and only if) the compression feature is enabled, all input frames will be processed by a soft knee thresholding function prior to the actual normalization process. Put simply, the thresholding function is going to prune all samples whose magnitude exceeds a certain threshold value. However, the Dynamic Audio Normalizer does not simply apply a fixed threshold value. Instead, the threshold value will be adjusted for each individual frame. In general, smaller parameters result in stronger compression, and vice versa. Values below 3.0 are not recommended, because audible distortion may appear.
        threshold:
            Set the target threshold value. This specifies the lowest permissible magnitude level for the audio input which will be normalized. If input frame volume is above this value frame will be normalized. Otherwise frame may not be normalized at all. The default value is set to 0, which means all input frames will be normalized. This option is mostly useful if digital noise is not wanted to be amplified.
        channels:
            Specify which channels to filter, by default all available channels are filtered.
        overlap:
            Specify overlap for frames. If set to 0 (default) no frame overlapping is done. Using >0 and <1 values will make less conservative gain adjustments, like when framelen option is set to smaller value, if framelen option value is compensated for non-zero overlap then gain adjustments will be smoother across time compared to zero overlap case.
        curve:
            Specify the peak mapping curve expression which is going to be used when calculating gain applied to frames. The max output frame gain will still be limited by other options mentioned previously for this filter. The expression can contain the following constants: ch current channel number sn current sample number nb_channels number of channels t timestamp expressed in seconds sr sample rate p current frame peak value



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm

        """
        return FilterNode(
            *[self],
            name="dynaudnorm",
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
                **kwargs,
            }
        ).stream()

    def earwax(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.86 earwax Make audio easier to listen to on headphones. This filter adds ‘cues’ to 44.1kHz stereo (i.e. audio CD format) audio so that when listened to on headphones the stereo image is moved from inside your head (standard for headphones) to outside and in front of the listener (standard for speakers). Ported from SoX.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#earwax

        """
        return FilterNode(*[self], name="earwax", kwargs={**kwargs}).stream()

    def edgedetect(
        self,
        *,
        low: str = None,
        high: str = None,
        mode: Literal["wires", "colormix", "canny"] = None,
        planes: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.79 edgedetect Detect and draw edges. The filter uses the Canny Edge Detection algorithm. The filter accepts the following options:

        Parameters:
        ----------
        low:
            Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        high:
            Set low and high threshold values used by the Canny thresholding algorithm. The high threshold selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the low threshold. low and high threshold values must be chosen in the range [0,1], and low should be lesser or equal to high. Default value for low is 20/255, and default value for high is 50/255.
        mode:
            Define the drawing mode. ‘wires’ Draw white/gray wires on black background. ‘colormix’ Mix the colors to create a paint/cartoon effect. ‘canny’ Apply Canny edge detector on all selected planes. Default value is wires.
        planes:
            Select planes for filtering. By default all available planes are filtered.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#edgedetect

        """
        return FilterNode(
            *[self], name="edgedetect", kwargs={"low": low, "high": high, "mode": mode, "planes": planes, **kwargs}
        ).stream()

    def elbg(
        self,
        *,
        codebook_length: int = None,
        nb_steps: int = None,
        seed: int = None,
        pal8: bool = None,
        use_alpha: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.80 elbg Apply a posterize effect using the ELBG (Enhanced LBG) algorithm. For each input image, the filter will compute the optimal mapping from the input to the output given the codebook length, that is the number of distinct output colors. This filter accepts the following options.

        Parameters:
        ----------
        codebook_length:
            Set codebook length. The value must be a positive integer, and represents the number of distinct output colors. Default value is 256.
        nb_steps:
            Set the maximum number of iterations to apply for computing the optimal mapping. The higher the value the better the result and the higher the computation time. Default value is 1.
        seed:
            Set a random seed, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to -1, the filter will try to use a good random seed on a best effort basis.
        pal8:
            Set pal8 output pixel format. This option does not work with codebook length greater than 256. Default is disabled.
        use_alpha:
            Include alpha values in the quantization calculation. Allows creating palettized output images (e.g. PNG8) with multiple alpha smooth blending.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#elbg

        """
        return FilterNode(
            *[self],
            name="elbg",
            kwargs={
                "codebook_length": codebook_length,
                "nb_steps": nb_steps,
                "seed": seed,
                "pal8": pal8,
                "use_alpha": use_alpha,
                **kwargs,
            }
        ).stream()

    def entropy(self, *, mode: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.81 entropy Measure graylevel entropy in histogram of color channels of video frames. It accepts the following parameters:

        Parameters:
        ----------
        mode:
            Can be either normal or diff. Default is normal. diff mode measures entropy of histogram delta values, absolute differences between neighbour histogram values.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#entropy

        """
        return FilterNode(*[self], name="entropy", kwargs={"mode": mode, **kwargs}).stream()

    def epx(self, *, n: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.82 epx Apply the EPX magnification filter which is designed for pixel art. It accepts the following option:

        Parameters:
        ----------
        n:
            Set the scaling dimension: 2 for 2xEPX, 3 for 3xEPX. Default is 3.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#epx

        """
        return FilterNode(*[self], name="epx", kwargs={"n": n, **kwargs}).stream()

    def eq(
        self,
        *,
        contrast: float = None,
        brightness: float = None,
        saturation: float = None,
        gamma: float = None,
        gamma_r: float = None,
        gamma_g: float = None,
        gamma_b: float = None,
        gamma_weight: float = None,
        eval: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.83 eq Set brightness, contrast, saturation and approximate gamma adjustment. The filter accepts the following options: The expressions accept the following parameters:

        Parameters:
        ----------
        contrast:
            Set the contrast expression. The value must be a float value in range -1000.0 to 1000.0. The default value is "1".
        brightness:
            Set the brightness expression. The value must be a float value in range -1.0 to 1.0. The default value is "0".
        saturation:
            Set the saturation expression. The value must be a float in range 0.0 to 3.0. The default value is "1".
        gamma:
            Set the gamma expression. The value must be a float in range 0.1 to 10.0. The default value is "1".
        gamma_r:
            Set the gamma expression for red. The value must be a float in range 0.1 to 10.0. The default value is "1".
        gamma_g:
            Set the gamma expression for green. The value must be a float in range 0.1 to 10.0. The default value is "1".
        gamma_b:
            Set the gamma expression for blue. The value must be a float in range 0.1 to 10.0. The default value is "1".
        gamma_weight:
            Set the gamma weight expression. It can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting overamplified and just plain white. The value must be a float in range 0.0 to 1.0. A value of 0.0 turns the gamma correction all the way down while 1.0 leaves it at its full strength. Default is "1".
        eval:
            Set when the expressions for brightness, contrast, saturation and gamma expressions are evaluated. It accepts the following values: ‘init’ only evaluate expressions once during the filter initialization or when a command is processed ‘frame’ evaluate expressions for each incoming frame Default value is ‘init’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#eq

        """
        return FilterNode(
            *[self],
            name="eq",
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
                **kwargs,
            }
        ).stream()

    def equalizer(
        self,
        *,
        frequency: float,
        width_type: str,
        width: float,
        gain: float,
        mix: float,
        channels: str,
        normalize: bool,
        transform: str,
        precision: str,
        block_size: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.87 equalizer Apply a two-pole peaking equalisation (EQ) filter. With this filter, the signal-level at and around a selected frequency can be increased or decreased, whilst (unlike bandpass and bandreject filters) that at all other frequencies is unchanged. In order to produce complex equalisation curves, this filter can be given several times, each with a different central frequency. The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set the filter’s central frequency in Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units.
        gain:
            Set the required gain or attenuation in dB. Beware of clipping when using a positive gain.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#equalizer

        """
        return FilterNode(
            *[self],
            name="equalizer",
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
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def erosion(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        coordinates: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.84 erosion Apply erosion effect to the video. This filter replaces the pixel by the local(3x3) minimum. It accepts the following options:

        Parameters:
        ----------
        threshold0:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold1:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold2:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold3:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        coordinates:
            Flag which specifies the pixel to refer to. Default is 255 i.e. all eight pixels are used. Flags to local 3x3 coordinates maps like this: 1 2 3 4 5 6 7 8



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#erosion

        """
        return FilterNode(
            *[self],
            name="erosion",
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
                "coordinates": coordinates,
                **kwargs,
            }
        ).stream()

    def estdif(
        self,
        *,
        mode: str = None,
        parity: str = None,
        deint: str = None,
        rslope: int = None,
        redge: int = None,
        ecost: int = None,
        mcost: int = None,
        dcost: int = None,
        interp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.85 estdif Deinterlace the input video ("estdif" stands for "Edge Slope Tracing Deinterlacing Filter"). Spatial only filter that uses edge slope tracing algorithm to interpolate missing lines. It accepts the following parameters:

        Parameters:
        ----------
        mode:
            The interlacing mode to adopt. It accepts one of the following values: frame Output one frame for each frame. field Output one frame for each field. The default value is field.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: tff Assume the top field is first. bff Assume the bottom field is first. auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: all Deinterlace all frames. interlaced Only deinterlace frames marked as interlaced. The default value is all.
        rslope:
            Specify the search radius for edge slope tracing. Default value is 1. Allowed range is from 1 to 15.
        redge:
            Specify the search radius for best edge matching. Default value is 2. Allowed range is from 0 to 15.
        ecost:
            Specify the edge cost for edge matching. Default value is 2. Allowed range is from 0 to 50.
        mcost:
            Specify the middle cost for edge matching. Default value is 1. Allowed range is from 0 to 50.
        dcost:
            Specify the distance cost for edge matching. Default value is 1. Allowed range is from 0 to 50.
        interp:
            Specify the interpolation used. Default is 4-point interpolation. It accepts one of the following values: 2p Two-point interpolation. 4p Four-point interpolation. 6p Six-point interpolation.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#estdif

        """
        return FilterNode(
            *[self],
            name="estdif",
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
                **kwargs,
            }
        ).stream()

    def exposure(self, *, exposure: float = None, black: float = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.86 exposure Adjust exposure of the video stream. The filter accepts the following options:

        Parameters:
        ----------
        exposure:
            Set the exposure correction in EV. Allowed range is from -3.0 to 3.0 EV Default value is 0 EV.
        black:
            Set the black level correction. Allowed range is from -1.0 to 1.0. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#exposure

        """
        return FilterNode(*[self], name="exposure", kwargs={"exposure": exposure, "black": black, **kwargs}).stream()

    def extractplanes(self, *, planes: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.87 extractplanes Extract color channel components from input video stream into separate grayscale video streams. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set plane(s) to extract. Available values for planes are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’ Choosing planes not available in the input will result in an error. That means you cannot select r, g, b planes with y, u, v planes at same time.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extractplanes

        """
        return FilterNode(*[self], name="extractplanes", kwargs={"planes": planes, **kwargs}).stream()

    def extrastereo(self, *, m: float = None, c: bool = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.88 extrastereo Linearly increases the difference between left and right channels which adds some sort of "live" effect to playback. The filter accepts the following options:

        Parameters:
        ----------
        m:
            Sets the difference coefficient (default: 2.5). 0.0 means mono sound (average of both channels), with 1.0 sound will be unchanged, with -1.0 left and right channels will be swapped.
        c:
            Enable clipping. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#extrastereo

        """
        return FilterNode(*[self], name="extrastereo", kwargs={"m": m, "c": c, **kwargs}).stream()

    def fade(
        self,
        *,
        type: str = None,
        start_frame: int = None,
        nb_frames: int = None,
        alpha: int = None,
        start_time: float = None,
        duration: float = None,
        color: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.88 fade Apply a fade-in/out effect to the input video. It accepts the following parameters:

        Parameters:
        ----------
        type:
            The effect type can be either "in" for a fade-in, or "out" for a fade-out effect. Default is in.
        start_frame:
            Specify the number of the frame to start applying the fade effect at. Default is 0.
        nb_frames:
            The number of frames that the fade effect lasts. At the end of the fade-in effect, the output video will have the same intensity as the input video. At the end of the fade-out transition, the output video will be filled with the selected color. Default is 25.
        alpha:
            If set to 1, fade only alpha channel, if one exists on the input. Default value is 0.
        start_time:
            Specify the timestamp (in seconds) of the frame to start to apply the fade effect. If both start_frame and start_time are specified, the fade will start at whichever comes last. Default is 0.
        duration:
            The number of seconds for which the fade effect has to last. At the end of the fade-in effect the output video will have the same intensity as the input video, at the end of the fade-out transition the output video will be filled with the selected color. If both duration and nb_frames are specified, duration is used. Default is 0 (nb_frames is used by default).
        color:
            Specify the color of the fade. Default is "black".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fade

        """
        return FilterNode(
            *[self],
            name="fade",
            kwargs={
                "type": type,
                "start_frame": start_frame,
                "nb_frames": nb_frames,
                "alpha": alpha,
                "start_time": start_time,
                "duration": duration,
                "color": color,
                **kwargs,
            }
        ).stream()

    def feedback(self, *, x: int, y: int, w: int, h: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.89 feedback Apply feedback video filter. This filter pass cropped input frames to 2nd output. From there it can be filtered with other video filters. After filter receives frame from 2nd input, that frame is combined on top of original frame from 1st input and passed to 1st output. The typical usage is filter only part of frame. The filter accepts the following options:

        Parameters:
        ----------
        x:
            Set the top left crop position.
        y:
            Set the top left crop position.
        w:
            Set the crop size.
        h:
            Set the crop size.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#feedback

        """
        return FilterNode(*[self], name="feedback", kwargs={"x": x, "y": y, "w": w, "h": h, **kwargs}).stream()

    def fftdnoiz(
        self,
        *,
        sigma: float = None,
        amount: float = None,
        block: int = None,
        overlap: float = None,
        method: str = None,
        prev: int = None,
        next: int = None,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.90 fftdnoiz Denoise frames using 3D FFT (frequency domain filtering). The filter accepts the following options:

        Parameters:
        ----------
        sigma:
            Set the noise sigma constant. This sets denoising strength. Default value is 1. Allowed range is from 0 to 30. Using very high sigma with low overlap may give blocking artifacts.
        amount:
            Set amount of denoising. By default all detected noise is reduced. Default value is 1. Allowed range is from 0 to 1.
        block:
            Set size of block in pixels, Default is 32, can be 8 to 256.
        overlap:
            Set block overlap. Default is 0.5. Allowed range is from 0.2 to 0.8.
        method:
            Set denoising method. Default is wiener, can also be hard.
        prev:
            Set number of previous frames to use for denoising. By default is set to 0.
        next:
            Set number of next frames to to use for denoising. By default is set to 0.
        planes:
            Set planes which will be filtered, by default are all available filtered except alpha.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz

        """
        return FilterNode(
            *[self],
            name="fftdnoiz",
            kwargs={
                "sigma": sigma,
                "amount": amount,
                "block": block,
                "overlap": overlap,
                "method": method,
                "prev": prev,
                "next": next,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def field(self, *, type: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.92 field Extract a single field from an interlaced image using stride arithmetic to avoid wasting CPU time. The output frames are marked as non-interlaced. The filter accepts the following options:

        Parameters:
        ----------
        type:
            Specify whether to extract the top (if the value is 0 or top) or the bottom field (if the value is 1 or bottom).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#field

        """
        return FilterNode(*[self], name="field", kwargs={"type": type, **kwargs}).stream()

    def fieldhint(self, *, hint: str, mode: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.93 fieldhint Create new frames by copying the top and bottom fields from surrounding frames supplied as numbers by the hint file. Example of first several lines of hint file for relative mode: 0,0 - # first frame 1,0 - # second frame, use third's frame top field and second's frame bottom field 1,0 - # third frame, use fourth's frame top field and third's frame bottom field 1,0 - 0,0 - 0,0 - 1,0 - 1,0 - 1,0 - 0,0 - 0,0 - 1,0 - 1,0 - 1,0 - 0,0 -

        Parameters:
        ----------
        hint:
            Set file containing hints: absolute/relative frame numbers. There must be one line for each frame in a clip. Each line must contain two numbers separated by the comma, optionally followed by - or +. Numbers supplied on each line of file can not be out of [N-1,N+1] where N is current frame number for absolute mode or out of [-1, 1] range for relative mode. First number tells from which frame to pick up top field and second number tells from which frame to pick up bottom field. If optionally followed by + output frame will be marked as interlaced, else if followed by - output frame will be marked as progressive, else it will be marked same as input frame. If optionally followed by t output frame will use only top field, or in case of b it will use only bottom field. If line starts with # or ; that line is skipped.
        mode:
            Can be item absolute or relative or pattern. Default is absolute. The pattern mode is same as relative mode, except at last entry of file if there are more frames to process than hint file is seek back to start.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldhint

        """
        return FilterNode(*[self], name="fieldhint", kwargs={"hint": hint, "mode": mode, **kwargs}).stream()

    def fieldmatch(
        self,
        *,
        order: str = None,
        mode: str = None,
        ppsrc: int = None,
        field: str = None,
        mchroma: int = None,
        y0: int = None,
        y1: int = None,
        scthresh: float = None,
        combmatch: str = None,
        combdbg: str = None,
        cthresh: int = None,
        chroma: int = None,
        blockx: int = None,
        blocky: int = None,
        combpel: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.94 fieldmatch Field matching filter for inverse telecine. It is meant to reconstruct the progressive frames from a telecined stream. The filter does not drop duplicated frames, so to achieve a complete inverse telecine fieldmatch needs to be followed by a decimation filter such as decimate in the filtergraph. The separation of the field matching and the decimation is notably motivated by the possibility of inserting a de-interlacing filter fallback between the two. If the source has mixed telecined and real interlaced content, fieldmatch will not be able to match fields for the interlaced parts. But these remaining combed frames will be marked as interlaced, and thus can be de-interlaced by a later filter such as yadif before decimation. In addition to the various configuration options, fieldmatch can take an optional second stream, activated through the ppsrc option. If enabled, the frames reconstruction will be based on the fields and frames from this second stream. This allows the first input to be pre-processed in order to help the various algorithms of the filter, while keeping the output lossless (assuming the fields are matched properly). Typically, a field-aware denoiser, or brightness/contrast adjustments can help. Note that this filter uses the same algorithms as TIVTC/TFM (AviSynth project) and VIVTC/VFM (VapourSynth project). The later is a light clone of TFM from which fieldmatch is based on. While the semantic and usage are very close, some behaviour and options names can differ. The decimate filter currently only works for constant frame rate input. If your input has mixed telecined (30fps) and progressive content with a lower framerate like 24fps use the following filterchain to produce the necessary cfr stream: dejudder,fps=30000/1001,fieldmatch,decimate. The filter accepts the following options:

        Parameters:
        ----------
        order:
            Specify the assumed field order of the input stream. Available values are: ‘auto’ Auto detect parity (use FFmpeg’s internal parity value). ‘bff’ Assume bottom field first. ‘tff’ Assume top field first. Note that it is sometimes recommended not to trust the parity announced by the stream. Default value is auto.
        mode:
            Set the matching mode or strategy to use. pc mode is the safest in the sense that it won’t risk creating jerkiness due to duplicate frames when possible, but if there are bad edits or blended fields it will end up outputting combed frames when a good match might actually exist. On the other hand, pcn_ub mode is the most risky in terms of creating jerkiness, but will almost always find a good frame if there is one. The other values are all somewhere in between pc and pcn_ub in terms of risking jerkiness and creating duplicate frames versus finding good matches in sections with bad edits, orphaned fields, blended fields, etc. More details about p/c/n/u/b are available in p/c/n/u/b meaning section. Available values are: ‘pc’ 2-way matching (p/c) ‘pc_n’ 2-way matching, and trying 3rd match if still combed (p/c + n) ‘pc_u’ 2-way matching, and trying 3rd match (same order) if still combed (p/c + u) ‘pc_n_ub’ 2-way matching, trying 3rd match if still combed, and trying 4th/5th matches if still combed (p/c + n + u/b) ‘pcn’ 3-way matching (p/c/n) ‘pcn_ub’ 3-way matching, and trying 4th/5th matches if all 3 of the original matches are detected as combed (p/c/n + u/b) The parenthesis at the end indicate the matches that would be used for that mode assuming order=tff (and field on auto or top). In terms of speed pc mode is by far the fastest and pcn_ub is the slowest. Default value is pc_n.
        ppsrc:
            Mark the main input stream as a pre-processed input, and enable the secondary input stream as the clean source to pick the fields from. See the filter introduction for more details. It is similar to the clip2 feature from VFM/TFM. Default value is 0 (disabled).
        field:
            Set the field to match from. It is recommended to set this to the same value as order unless you experience matching failures with that setting. In certain circumstances changing the field that is used to match from can have a large impact on matching performance. Available values are: ‘auto’ Automatic (same value as order). ‘bottom’ Match from the bottom field. ‘top’ Match from the top field. Default value is auto.
        mchroma:
            Set whether or not chroma is included during the match comparisons. In most cases it is recommended to leave this enabled. You should set this to 0 only if your clip has bad chroma problems such as heavy rainbowing or other artifacts. Setting this to 0 could also be used to speed things up at the cost of some accuracy. Default value is 1.
        y0:
            These define an exclusion band which excludes the lines between y0 and y1 from being included in the field matching decision. An exclusion band can be used to ignore subtitles, a logo, or other things that may interfere with the matching. y0 sets the starting scan line and y1 sets the ending line; all lines in between y0 and y1 (including y0 and y1) will be ignored. Setting y0 and y1 to the same value will disable the feature. y0 and y1 defaults to 0.
        y1:
            These define an exclusion band which excludes the lines between y0 and y1 from being included in the field matching decision. An exclusion band can be used to ignore subtitles, a logo, or other things that may interfere with the matching. y0 sets the starting scan line and y1 sets the ending line; all lines in between y0 and y1 (including y0 and y1) will be ignored. Setting y0 and y1 to the same value will disable the feature. y0 and y1 defaults to 0.
        scthresh:
            Set the scene change detection threshold as a percentage of maximum change on the luma plane. Good values are in the [8.0, 14.0] range. Scene change detection is only relevant in case combmatch=sc. The range for scthresh is [0.0, 100.0]. Default value is 12.0.
        combmatch:
            When combatch is not none, fieldmatch will take into account the combed scores of matches when deciding what match to use as the final match. Available values are: ‘none’ No final matching based on combed scores. ‘sc’ Combed scores are only used when a scene change is detected. ‘full’ Use combed scores all the time. Default is sc.
        combdbg:
            Force fieldmatch to calculate the combed metrics for certain matches and print them. This setting is known as micout in TFM/VFM vocabulary. Available values are: ‘none’ No forced calculation. ‘pcn’ Force p/c/n calculations. ‘pcnub’ Force p/c/n/u/b calculations. Default value is none.
        cthresh:
            This is the area combing threshold used for combed frame detection. This essentially controls how "strong" or "visible" combing must be to be detected. Larger values mean combing must be more visible and smaller values mean combing can be less visible or strong and still be detected. Valid settings are from -1 (every pixel will be detected as combed) to 255 (no pixel will be detected as combed). This is basically a pixel difference value. A good range is [8, 12]. Default value is 9.
        chroma:
            Sets whether or not chroma is considered in the combed frame decision. Only disable this if your source has chroma problems (rainbowing, etc.) that are causing problems for the combed frame detection with chroma enabled. Actually, using chroma=0 is usually more reliable, except for the case where there is chroma only combing in the source. Default value is 0.
        blockx:
            Respectively set the x-axis and y-axis size of the window used during combed frame detection. This has to do with the size of the area in which combpel pixels are required to be detected as combed for a frame to be declared combed. See the combpel parameter description for more info. Possible values are any number that is a power of 2 starting at 4 and going up to 512. Default value is 16.
        blocky:
            Respectively set the x-axis and y-axis size of the window used during combed frame detection. This has to do with the size of the area in which combpel pixels are required to be detected as combed for a frame to be declared combed. See the combpel parameter description for more info. Possible values are any number that is a power of 2 starting at 4 and going up to 512. Default value is 16.
        combpel:
            The number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed. While cthresh controls how "visible" the combing must be, this setting controls "how much" combing there must be in any localized area (a window defined by the blockx and blocky settings) on the frame. Minimum value is 0 and maximum is blocky x blockx (at which point no frames will ever be detected as combed). This setting is known as MI in TFM/VFM vocabulary. Default value is 80.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldmatch

        """
        return FilterNode(
            *[self],
            name="fieldmatch",
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
                **kwargs,
            }
        ).stream()

    def fieldorder(self, *, order: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.95 fieldorder Transform the field order of the input video. It accepts the following parameters: The default value is ‘tff’. The transformation is done by shifting the picture content up or down by one line, and filling the remaining line with appropriate picture content. This method is consistent with most broadcast field order converters. If the input video is not flagged as being interlaced, or it is already flagged as being of the required output field order, then this filter does not alter the incoming video. It is very useful when converting to or from PAL DV material, which is bottom field first. For example: ffmpeg -i in.vob -vf "fieldorder=bff" out.dv

        Parameters:
        ----------
        order:
            The output field order. Valid values are tff for top field first or bff for bottom field first.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fieldorder

        """
        return FilterNode(*[self], name="fieldorder", kwargs={"order": order, **kwargs}).stream()

    def fifo(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.96 fifo, afifo Buffer input images and send them when they are requested. It is mainly useful when auto-inserted by the libavfilter framework. It does not take parameters.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fifo_002c-afifo

        """
        return FilterNode(*[self], name="fifo", kwargs={**kwargs}).stream()

    def fillborders(
        self,
        *,
        left: int,
        right: int,
        top: int,
        bottom: int,
        mode: str = None,
        color: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.97 fillborders Fill borders of the input video, without changing video stream dimensions. Sometimes video can have garbage at the four edges and you may not want to crop video input to keep size multiple of some number. This filter accepts the following options:

        Parameters:
        ----------
        left:
            Number of pixels to fill from left border.
        right:
            Number of pixels to fill from right border.
        top:
            Number of pixels to fill from top border.
        bottom:
            Number of pixels to fill from bottom border.
        mode:
            Set fill mode. It accepts the following values: ‘smear’ fill pixels using outermost pixels ‘mirror’ fill pixels using mirroring (half sample symmetric) ‘fixed’ fill pixels with constant value ‘reflect’ fill pixels using reflecting (whole sample symmetric) ‘wrap’ fill pixels using wrapping ‘fade’ fade pixels to constant value ‘margins’ fill pixels at top and bottom with weighted averages pixels near borders Default is smear.
        color:
            Set color for pixels in fixed or fade mode. Default is black.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fillborders

        """
        return FilterNode(
            *[self],
            name="fillborders",
            kwargs={"left": left, "right": right, "top": top, "bottom": bottom, "mode": mode, "color": color, **kwargs}
        ).stream()

    def firequalizer(
        self,
        *,
        gain: str = None,
        gain_entry: str,
        delay: float = None,
        accuracy: float = None,
        wfunc: str = None,
        fixed: bool = None,
        multi: bool = None,
        zero_phase: bool = None,
        scale: str = None,
        dumpfile: str,
        dumpscale: str = None,
        fft2: bool = None,
        min_phase: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.89 firequalizer Apply FIR Equalization using arbitrary frequency response. The filter accepts the following option:

        Parameters:
        ----------
        gain:
            Set gain curve equation (in dB). The expression can contain variables: f the evaluated frequency sr sample rate ch channel number, set to 0 when multichannels evaluation is disabled chid channel id, see libavutil/channel_layout.h, set to the first channel id when multichannels evaluation is disabled chs number of channels chlayout channel_layout, see libavutil/channel_layout.h and functions: gain_interpolate(f) interpolate gain on frequency f based on gain_entry cubic_interpolate(f) same as gain_interpolate, but smoother This option is also available as command. Default is gain_interpolate(f).
        gain_entry:
            Set gain entry for gain_interpolate function. The expression can contain functions: entry(f, g) store gain entry at frequency f with value g This option is also available as command.
        delay:
            Set filter delay in seconds. Higher value means more accurate. Default is 0.01.
        accuracy:
            Set filter accuracy in Hz. Lower value means more accurate. Default is 5.
        wfunc:
            Set window function. Acceptable values are: rectangular rectangular window, useful when gain curve is already smooth hann hann window (default) hamming hamming window blackman blackman window nuttall3 3-terms continuous 1st derivative nuttall window mnuttall3 minimum 3-terms discontinuous nuttall window nuttall 4-terms continuous 1st derivative nuttall window bnuttall minimum 4-terms discontinuous nuttall (blackman-nuttall) window bharris blackman-harris window tukey tukey window
        fixed:
            If enabled, use fixed number of audio samples. This improves speed when filtering with large delay. Default is disabled.
        multi:
            Enable multichannels evaluation on gain. Default is disabled.
        zero_phase:
            Enable zero phase mode by subtracting timestamp to compensate delay. Default is disabled.
        scale:
            Set scale used by gain. Acceptable values are: linlin linear frequency, linear gain linlog linear frequency, logarithmic (in dB) gain (default) loglin logarithmic (in octave scale where 20 Hz is 0) frequency, linear gain loglog logarithmic frequency, logarithmic gain
        dumpfile:
            Set file for dumping, suitable for gnuplot.
        dumpscale:
            Set scale for dumpfile. Acceptable values are same with scale option. Default is linlog.
        fft2:
            Enable 2-channel convolution using complex FFT. This improves speed significantly. Default is disabled.
        min_phase:
            Enable minimum phase impulse response. Default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#firequalizer

        """
        return FilterNode(
            *[self],
            name="firequalizer",
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
                **kwargs,
            }
        ).stream()

    def flanger(
        self,
        *,
        delay: float = None,
        depth: float = None,
        regen: float = None,
        width: float = None,
        speed: float = None,
        shape: str = None,
        phase: float = None,
        interp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.90 flanger Apply a flanging effect to the audio. The filter accepts the following options:

        Parameters:
        ----------
        delay:
            Set base delay in milliseconds. Range from 0 to 30. Default value is 0.
        depth:
            Set added sweep delay in milliseconds. Range from 0 to 10. Default value is 2.
        regen:
            Set percentage regeneration (delayed signal feedback). Range from -95 to 95. Default value is 0.
        width:
            Set percentage of delayed signal mixed with original. Range from 0 to 100. Default value is 71.
        speed:
            Set sweeps per second (Hz). Range from 0.1 to 10. Default value is 0.5.
        shape:
            Set swept wave shape, can be triangular or sinusoidal. Default value is sinusoidal.
        phase:
            Set swept wave percentage-shift for multi channel. Range from 0 to 100. Default value is 25.
        interp:
            Set delay-line interpolation, linear or quadratic. Default is linear.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#flanger

        """
        return FilterNode(
            *[self],
            name="flanger",
            kwargs={
                "delay": delay,
                "depth": depth,
                "regen": regen,
                "width": width,
                "speed": speed,
                "shape": shape,
                "phase": phase,
                "interp": interp,
                **kwargs,
            }
        ).stream()

    def floodfill(
        self,
        *,
        x: int,
        y: int,
        s0: float,
        s1: float,
        s2: float,
        s3: float,
        d0: float,
        d1: float,
        d2: float,
        d3: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.99 floodfill Flood area with values of same pixel components with another values. It accepts the following options:

        Parameters:
        ----------
        x:
            Set pixel x coordinate.
        y:
            Set pixel y coordinate.
        s0:
            Set source #0 component value.
        s1:
            Set source #1 component value.
        s2:
            Set source #2 component value.
        s3:
            Set source #3 component value.
        d0:
            Set destination #0 component value.
        d1:
            Set destination #1 component value.
        d2:
            Set destination #2 component value.
        d3:
            Set destination #3 component value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#floodfill

        """
        return FilterNode(
            *[self],
            name="floodfill",
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
                **kwargs,
            }
        ).stream()

    def format(self, *, pix_fmts: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.100 format Convert the input video to one of the specified pixel formats. Libavfilter will try to pick one that is suitable as input to the next filter. It accepts the following parameters:

        Parameters:
        ----------
        pix_fmts:
            A ’|’-separated list of pixel format names, such as "pix_fmts=yuv420p|monow|rgb24".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#format

        """
        return FilterNode(*[self], name="format", kwargs={"pix_fmts": pix_fmts, **kwargs}).stream()

    def fps(
        self,
        *,
        fps: str = None,
        start_time: float = None,
        round: str = None,
        eof_action: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.101 fps Convert the video to specified constant frame rate by duplicating or dropping frames as necessary. It accepts the following parameters: Alternatively, the options can be specified as a flat string: fps[:start_time[:round]]. See also the setpts filter.

        Parameters:
        ----------
        fps:
            The desired output frame rate. It accepts expressions containing the following constants: ‘source_fps’ The input’s frame rate ‘ntsc’ NTSC frame rate of 30000/1001 ‘pal’ PAL frame rate of 25.0 ‘film’ Film frame rate of 24.0 ‘ntsc_film’ NTSC-film frame rate of 24000/1001 The default is 25.
        start_time:
            Assume the first PTS should be the given value, in seconds. This allows for padding/trimming at the start of stream. By default, no assumption is made about the first frame’s expected PTS, so no padding or trimming is done. For example, this could be set to 0 to pad the beginning with duplicates of the first frame if a video stream starts after the audio stream or to trim any frames with a negative PTS.
        round:
            Timestamp (PTS) rounding method. Possible values are: zero round towards 0 inf round away from 0 down round towards -infinity up round towards +infinity near round to nearest The default is near.
        eof_action:
            Action performed when reading the last frame. Possible values are: round Use same timestamp rounding method as used for other frames. pass Pass through last frame if input duration has not been reached yet. The default is round.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fps

        """
        return FilterNode(
            *[self],
            name="fps",
            kwargs={"fps": fps, "start_time": start_time, "round": round, "eof_action": eof_action, **kwargs}
        ).stream()

    def framepack(self, *, format: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.102 framepack Pack two different video streams into a stereoscopic video, setting proper metadata on supported codecs. The two views should have the same size and framerate and processing will stop when the shorter video ends. Please note that you may conveniently adjust view properties with the scale and fps filters. It accepts the following parameters: Some examples: # Convert left and right views into a frame-sequential video ffmpeg -i LEFT -i RIGHT -filter_complex framepack=frameseq OUTPUT # Convert views into a side-by-side video with the same output resolution as the input ffmpeg -i LEFT -i RIGHT -filter_complex [0:v]scale=w=iw/2[left],[1:v]scale=w=iw/2[right],[left][right]framepack=sbs OUTPUT

        Parameters:
        ----------
        format:
            The desired packing format. Supported values are: sbs The views are next to each other (default). tab The views are on top of each other. lines The views are packed by line. columns The views are packed by column. frameseq The views are temporally interleaved.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framepack

        """
        return FilterNode(*[self], name="framepack", kwargs={"format": format, **kwargs}).stream()

    def framerate(
        self,
        *,
        fps: str = None,
        interp_start: int = None,
        interp_end: int = None,
        scene: float = None,
        flags: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.103 framerate Change the frame rate by interpolating new video output frames from the source frames. This filter is not designed to function correctly with interlaced media. If you wish to change the frame rate of interlaced media then you are required to deinterlace before this filter and re-interlace after this filter. A description of the accepted options follows.

        Parameters:
        ----------
        fps:
            Specify the output frames per second. This option can also be specified as a value alone. The default is 50.
        interp_start:
            Specify the start of a range where the output frame will be created as a linear interpolation of two frames. The range is [0-255], the default is 15.
        interp_end:
            Specify the end of a range where the output frame will be created as a linear interpolation of two frames. The range is [0-255], the default is 240.
        scene:
            Specify the level at which a scene change is detected as a value between 0 and 100 to indicate a new scene; a low value reflects a low probability for the current frame to introduce a new scene, while a higher value means the current frame is more likely to be one. The default is 8.2.
        flags:
            Specify flags influencing the filter process. Available value for flags is: scene_change_detect, scd Enable scene change detection using the value of the option scene. This flag is enabled by default.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framerate

        """
        return FilterNode(
            *[self],
            name="framerate",
            kwargs={
                "fps": fps,
                "interp_start": interp_start,
                "interp_end": interp_end,
                "scene": scene,
                "flags": flags,
                **kwargs,
            }
        ).stream()

    def framestep(self, *, step: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.104 framestep Select one frame every N-th frame. This filter accepts the following option:

        Parameters:
        ----------
        step:
            Select frame after every step frames. Allowed values are positive integers higher than 0. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#framestep

        """
        return FilterNode(*[self], name="framestep", kwargs={"step": step, **kwargs}).stream()

    def freezedetect(self, *, noise: str, duration: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.105 freezedetect Detect frozen video. This filter logs a message and sets frame metadata when it detects that the input video has no significant change in content during a specified duration. Video freeze detection calculates the mean average absolute difference of all the components of video frames and compares it to a noise floor. The printed times and duration are expressed in seconds. The lavfi.freezedetect.freeze_start metadata key is set on the first frame whose timestamp equals or exceeds the detection duration and it contains the timestamp of the first frame of the freeze. The lavfi.freezedetect.freeze_duration and lavfi.freezedetect.freeze_end metadata keys are set on the first frame after the freeze. The filter accepts the following options:

        Parameters:
        ----------
        noise:
            Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or as a difference ratio between 0 and 1. Default is -60dB, or 0.001.
        duration:
            Set freeze duration until notification (default is 2 seconds).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#freezedetect

        """
        return FilterNode(
            *[self], name="freezedetect", kwargs={"noise": noise, "duration": duration, **kwargs}
        ).stream()

    def freezeframes(self, *, first: int, last: int, replace: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.106 freezeframes Freeze video frames. This filter freezes video frames using frame from 2nd input. The filter accepts the following options:

        Parameters:
        ----------
        first:
            Set number of first frame from which to start freeze.
        last:
            Set number of last frame from which to end freeze.
        replace:
            Set number of frame from 2nd input which will be used instead of replaced frames.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#freezeframes

        """
        return FilterNode(
            *[self], name="freezeframes", kwargs={"first": first, "last": last, "replace": replace, **kwargs}
        ).stream()

    def frei0r(self, *, filter_name: str, filter_params: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.107 frei0r Apply a frei0r effect to the input video. To enable the compilation of this filter, you need to install the frei0r header and configure FFmpeg with --enable-frei0r. It accepts the following parameters: A frei0r effect parameter can be a boolean (its value is either "y" or "n"), a double, a color (specified as R/G/B, where R, G, and B are floating point numbers between 0.0 and 1.0, inclusive) or a color description as specified in the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual, a position (specified as X/Y, where X and Y are floating point numbers) and/or a string. The number and types of parameters depend on the loaded effect. If an effect parameter is not specified, the default value is set.

        Parameters:
        ----------
        filter_name:
            The name of the frei0r effect to load. If the environment variable FREI0R_PATH is defined, the frei0r effect is searched for in each of the directories specified by the colon-separated list in FREI0R_PATH. Otherwise, the standard frei0r paths are searched, in this order: HOME/.frei0r-1/lib/, /usr/local/lib/frei0r-1/, /usr/lib/frei0r-1/.
        filter_params:
            A ’|’-separated list of parameters to pass to the frei0r effect.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#frei0r

        """
        return FilterNode(
            *[self], name="frei0r", kwargs={"filter_name": filter_name, "filter_params": filter_params, **kwargs}
        ).stream()

    def fspp(
        self, *, quality: int = None, qp: int, strength: int = None, use_bframe_qp: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.108 fspp Apply fast and simple postprocessing. It is a faster version of spp. It splits (I)DCT into horizontal/vertical passes. Unlike the simple post- processing filter, one of them is performed once per block, not per pixel. This allows for much higher speed. The filter accepts the following options:

        Parameters:
        ----------
        quality:
            Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 4-5. Default value is 4.
        qp:
            Force a constant quantization parameter. It accepts an integer in range 0-63. If not set, the filter will use the QP from the video stream (if available).
        strength:
            Set filter strength. It accepts an integer in range -15 to 32. Lower values mean more details but also more artifacts, while higher values make the image smoother but also blurrier. Default value is 0 − PSNR optimal.
        use_bframe_qp:
            Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#fspp

        """
        return FilterNode(
            *[self],
            name="fspp",
            kwargs={"quality": quality, "qp": qp, "strength": strength, "use_bframe_qp": use_bframe_qp, **kwargs}
        ).stream()

    def gblur(
        self, *, sigma: float = None, steps: int = None, planes: str, sigmaV: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.109 gblur Apply Gaussian blur filter. The filter accepts the following options:

        Parameters:
        ----------
        sigma:
            Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.
        steps:
            Set number of steps for Gaussian approximation. Default is 1.
        planes:
            Set which planes to filter. By default all planes are filtered.
        sigmaV:
            Set vertical sigma, if negative it will be same as sigma. Default is -1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gblur

        """
        return FilterNode(
            *[self], name="gblur", kwargs={"sigma": sigma, "steps": steps, "planes": planes, "sigmaV": sigmaV, **kwargs}
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.110 geq Apply generic equation to each pixel. The filter accepts the following options: The colorspace is selected according to the specified options. If one of the lum_expr, cb_expr, or cr_expr options is specified, the filter will automatically select a YCbCr colorspace. If one of the red_expr, green_expr, or blue_expr options is specified, it will select an RGB colorspace. If one of the chrominance expression is not defined, it falls back on the other one. If no alpha expression is specified it will evaluate to opaque value. If none of chrominance expressions are specified, they will evaluate to the luma expression. The expressions can use the following variables and functions: For functions, if x and y are outside the area, the value will be automatically clipped to the closer edge. Please note that this filter can use multiple threads in which case each slice will have its own expression state. If you want to use only a single expression state because your expressions depend on previous state then you should limit the number of filter threads to 1.

        Parameters:
        ----------
        lum_expr:
            Set the luma expression.
        cb_expr:
            Set the chrominance blue expression.
        cr_expr:
            Set the chrominance red expression.
        alpha_expr:
            Set the alpha expression.
        red_expr:
            Set the red expression.
        green_expr:
            Set the green expression.
        blue_expr:
            Set the blue expression.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#geq

        """
        return FilterNode(
            *[self],
            name="geq",
            kwargs={
                "lum_expr": lum_expr,
                "cb_expr": cb_expr,
                "cr_expr": cr_expr,
                "alpha_expr": alpha_expr,
                "red_expr": red_expr,
                "green_expr": green_expr,
                "blue_expr": blue_expr,
                **kwargs,
            }
        ).stream()

    def gradfun(self, *, strength: float = None, radius: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.111 gradfun Fix the banding artifacts that are sometimes introduced into nearly flat regions by truncation to 8-bit color depth. Interpolate the gradients that should go where the bands are, and dither them. It is designed for playback only. Do not use it prior to lossy compression, because compression tends to lose the dither and bring back the bands. It accepts the following parameters: Alternatively, the options can be specified as a flat string: strength[:radius]

        Parameters:
        ----------
        strength:
            The maximum amount by which the filter will change any one pixel. This is also the threshold for detecting nearly flat regions. Acceptable values range from .51 to 64; the default value is 1.2. Out-of-range values will be clipped to the valid range.
        radius:
            The neighborhood to fit the gradient to. A larger radius makes for smoother gradients, but also prevents the filter from modifying the pixels near detailed regions. Acceptable values are 8-32; the default value is 16. Out-of-range values will be clipped to the valid range.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#gradfun

        """
        return FilterNode(*[self], name="gradfun", kwargs={"strength": strength, "radius": radius, **kwargs}).stream()

    def graphmonitor(
        self,
        *,
        size: str = None,
        opacity: float = None,
        mode: str = None,
        flags: str = None,
        rate: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.112 graphmonitor Show various filtergraph stats. With this filter one can debug complete filtergraph. Especially issues with links filling with queued frames. The filter accepts the following options:

        Parameters:
        ----------
        size:
            Set video output size. Default is hd720.
        opacity:
            Set video opacity. Default is 0.9. Allowed range is from 0 to 1.
        mode:
            Set output mode flags. Available values for flags are: ‘full’ No any filtering. Default. ‘compact’ Show only filters with queued frames. ‘nozero’ Show only filters with non-zero stats. ‘noeof’ Show only filters with non-eof stat. ‘nodisabled’ Show only filters that are enabled in timeline.
        flags:
            Set flags which enable which stats are shown in video. Available values for flags are: ‘none’ All flags turned off. ‘all’ All flags turned on. ‘queue’ Display number of queued frames in each link. ‘frame_count_in’ Display number of frames taken from filter. ‘frame_count_out’ Display number of frames given out from filter. ‘frame_count_delta’ Display delta number of frames between above two values. ‘pts’ Display current filtered frame pts. ‘pts_delta’ Display pts delta between current and previous frame. ‘time’ Display current filtered frame time. ‘time_delta’ Display time delta between current and previous frame. ‘timebase’ Display time base for filter link. ‘format’ Display used format for filter link. ‘size’ Display video size or number of audio channels in case of audio used by filter link. ‘rate’ Display video frame rate or sample rate in case of audio used by filter link. ‘eof’ Display link output status. ‘sample_count_in’ Display number of samples taken from filter. ‘sample_count_out’ Display number of samples given out from filter. ‘sample_count_delta’ Display delta number of samples between above two values. ‘disabled’ Show the timeline filter status.
        rate:
            Set upper limit for video rate of output stream, Default value is 25. This guarantee that output video frame rate will not be higher than this value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#graphmonitor

        """
        return FilterNode(
            *[self],
            name="graphmonitor",
            kwargs={"size": size, "opacity": opacity, "mode": mode, "flags": flags, "rate": rate, **kwargs}
        ).stream()

    def grayworld(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.113 grayworld A color constancy filter that applies color correction based on the grayworld assumption See: https://www.researchgate.net/publication/275213614_A_New_Color_Correction_Method_for_Underwater_Imaging The algorithm uses linear light, so input data should be linearized beforehand (and possibly correctly tagged). ffmpeg -i INPUT -vf zscale=transfer=linear,grayworld,zscale=transfer=bt709,format=yuv420p OUTPUT

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#grayworld

        """
        return FilterNode(*[self], name="grayworld", kwargs={**kwargs}).stream()

    def greyedge(
        self, *, difford: float = None, minknorm: float = None, sigma: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.114 greyedge A color constancy variation filter which estimates scene illumination via grey edge algorithm and corrects the scene colors accordingly. See: https://staff.science.uva.nl/th.gevers/pub/GeversTIP07.pdf The filter accepts the following options:

        Parameters:
        ----------
        difford:
            The order of differentiation to be applied on the scene. Must be chosen in the range [0,2] and default value is 1.
        minknorm:
            The Minkowski parameter to be used for calculating the Minkowski distance. Must be chosen in the range [0,20] and default value is 1. Set to 0 for getting max value instead of calculating Minkowski distance.
        sigma:
            The standard deviation of Gaussian blur to be applied on the scene. Must be chosen in the range [0,1024.0] and default value = 1. floor( sigma * break_off_sigma(3) ) can’t be equal to 0 if difford is greater than 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#greyedge

        """
        return FilterNode(
            *[self], name="greyedge", kwargs={"difford": difford, "minknorm": minknorm, "sigma": sigma, **kwargs}
        ).stream()

    def guided(
        self,
        *,
        radius: int = None,
        eps: float = None,
        mode: str = None,
        sub: int = None,
        guidance: str = None,
        planes: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.115 guided Apply guided filter for edge-preserving smoothing, dehazing and so on. The filter accepts the following options:

        Parameters:
        ----------
        radius:
            Set the box radius in pixels. Allowed range is 1 to 20. Default is 3.
        eps:
            Set regularization parameter (with square). Allowed range is 0 to 1. Default is 0.01.
        mode:
            Set filter mode. Can be basic or fast. Default is basic.
        sub:
            Set subsampling ratio for fast mode. Range is 2 to 64. Default is 4. No subsampling occurs in basic mode.
        guidance:
            Set guidance mode. Can be off or on. Default is off. If off, single input is required. If on, two inputs of the same resolution and pixel format are required. The second input serves as the guidance.
        planes:
            Set planes to filter. Default is first only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#guided

        """
        return FilterNode(
            *[self],
            name="guided",
            kwargs={
                "radius": radius,
                "eps": eps,
                "mode": mode,
                "sub": sub,
                "guidance": guidance,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def haas(
        self,
        *,
        level_in: float = None,
        level_out: float = None,
        side_gain: float = None,
        middle_source: str = None,
        middle_phase: bool = None,
        left_delay: float = None,
        left_balance: float = None,
        left_gain: float = None,
        left_phase: bool = None,
        right_delay: float = None,
        right_balance: float = None,
        right_gain: float = None,
        right_phase: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.91 haas Apply Haas effect to audio. Note that this makes most sense to apply on mono signals. With this filter applied to mono signals it give some directionality and stretches its stereo image. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input level. By default is 1, or 0dB
        level_out:
            Set output level. By default is 1, or 0dB.
        side_gain:
            Set gain applied to side part of signal. By default is 1.
        middle_source:
            Set kind of middle source. Can be one of the following: ‘left’ Pick left channel. ‘right’ Pick right channel. ‘mid’ Pick middle part signal of stereo image. ‘side’ Pick side part signal of stereo image.
        middle_phase:
            Change middle phase. By default is disabled.
        left_delay:
            Set left channel delay. By default is 2.05 milliseconds.
        left_balance:
            Set left channel balance. By default is -1.
        left_gain:
            Set left channel gain. By default is 1.
        left_phase:
            Change left phase. By default is disabled.
        right_delay:
            Set right channel delay. By defaults is 2.12 milliseconds.
        right_balance:
            Set right channel balance. By default is 1.
        right_gain:
            Set right channel gain. By default is 1.
        right_phase:
            Change right phase. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#haas

        """
        return FilterNode(
            *[self],
            name="haas",
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
                **kwargs,
            }
        ).stream()

    def haldclut(
        self, *, clut: str = None, shortest: int = None, repeatlast: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.116 haldclut Apply a Hald CLUT to a video stream. First input is the video stream to process, and second one is the Hald CLUT. The Hald CLUT input can be a simple picture or a complete video stream. The filter accepts the following options: haldclut also has the same interpolation options as lut3d (both filters share the same internals). This filter also supports the framesync options. More information about the Hald CLUT can be found on Eskil Steenberg’s website (Hald CLUT author) at http://www.quelsolaar.com/technology/clut.html.

        Parameters:
        ----------
        clut:
            Set which CLUT video frames will be processed from second input stream, can be first or all. Default is all.
        shortest:
            Force termination when the shortest input terminates. Default is 0.
        repeatlast:
            Continue applying the last CLUT after the end of the stream. A value of 0 disable the filter after the last frame of the CLUT is reached. Default is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#haldclut

        """
        return FilterNode(
            *[self], name="haldclut", kwargs={"clut": clut, "shortest": shortest, "repeatlast": repeatlast, **kwargs}
        ).stream()

    def hdcd(
        self,
        *,
        disable_autoconvert: bool,
        process_stereo: bool,
        cdt_ms: int,
        force_pe: bool,
        analyze_mode: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.92 hdcd Decodes High Definition Compatible Digital (HDCD) data. A 16-bit PCM stream with embedded HDCD codes is expanded into a 20-bit PCM stream. The filter supports the Peak Extend and Low-level Gain Adjustment features of HDCD, and detects the Transient Filter flag. ffmpeg -i HDCD16.flac -af hdcd OUT24.flac When using the filter with wav, note the default encoding for wav is 16-bit, so the resulting 20-bit stream will be truncated back to 16-bit. Use something like -acodec pcm_s24le after the filter to get 24-bit PCM output. ffmpeg -i HDCD16.wav -af hdcd OUT16.wav ffmpeg -i HDCD16.wav -af hdcd -c:a pcm_s24le OUT24.wav The filter accepts the following options:

        Parameters:
        ----------
        disable_autoconvert:
            Disable any automatic format conversion or resampling in the filter graph.
        process_stereo:
            Process the stereo channels together. If target_gain does not match between channels, consider it invalid and use the last valid target_gain.
        cdt_ms:
            Set the code detect timer period in ms.
        force_pe:
            Always extend peaks above -3dBFS even if PE isn’t signaled.
        analyze_mode:
            Replace audio with a solid tone and adjust the amplitude to signal some specific aspect of the decoding process. The output file can be loaded in an audio editor alongside the original to aid analysis. analyze_mode=pe:force_pe=true can be used to see all samples above the PE level. Modes are: ‘0, off’ Disabled ‘1, lle’ Gain adjustment level at each sample ‘2, pe’ Samples where peak extend occurs ‘3, cdt’ Samples where the code detect timer is active ‘4, tgm’ Samples where the target gain does not match between channels



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hdcd

        """
        return FilterNode(
            *[self],
            name="hdcd",
            kwargs={
                "disable_autoconvert": disable_autoconvert,
                "process_stereo": process_stereo,
                "cdt_ms": cdt_ms,
                "force_pe": force_pe,
                "analyze_mode": analyze_mode,
                **kwargs,
            }
        ).stream()

    def headphone(
        self,
        *,
        map: str,
        gain: float,
        type: str,
        lfe: float,
        size: float = None,
        hrir: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.93 headphone Apply head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones. The HRIRs are provided via additional streams, for each channel one stereo input stream is needed. The filter accepts the following options:

        Parameters:
        ----------
        map:
            Set mapping of input streams for convolution. The argument is a ’|’-separated list of channel names in order as they are given as additional stream inputs for filter. This also specify number of input streams. Number of input streams must be not less than number of channels in first stream plus one.
        gain:
            Set gain applied to audio. Value is in dB. Default is 0.
        type:
            Set processing type. Can be time or freq. time is processing audio in time domain which is slow. freq is processing audio in frequency domain which is fast. Default is freq.
        lfe:
            Set custom gain for LFE channels. Value is in dB. Default is 0.
        size:
            Set size of frame in number of samples which will be processed at once. Default value is 1024. Allowed range is from 1024 to 96000.
        hrir:
            Set format of hrir stream. Default value is stereo. Alternative value is multich. If value is set to stereo, number of additional streams should be greater or equal to number of input channels in first input stream. Also each additional stream should have stereo number of channels. If value is set to multich, number of additional streams should be exactly one. Also number of input channels of additional stream should be equal or greater than twice number of channels of first input stream.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#headphone

        """
        return FilterNode(
            *[self],
            name="headphone",
            kwargs={"map": map, "gain": gain, "type": type, "lfe": lfe, "size": size, "hrir": hrir, **kwargs}
        ).stream()

    def hflip(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.117 hflip Flip the input video horizontally. For example, to horizontally flip the input video with ffmpeg: ffmpeg -i in.avi -vf "hflip" out.avi

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hflip

        """
        return FilterNode(*[self], name="hflip", kwargs={**kwargs}).stream()

    def highpass(
        self,
        *,
        frequency: float = None,
        poles: int = None,
        width_type: str = None,
        width: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: str,
        precision: str = None,
        block_size: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.94 highpass Apply a high-pass filter with 3dB point frequency. The filter can be either single-pole, or double-pole (the default). The filter roll off at 6dB per pole per octave (20dB per pole per decade). The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set frequency in Hz. Default is 3000.
        poles:
            Set number of poles. Default is 2.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units. Applies only to double-pole filter. The default is 0.707q and gives a Butterworth response.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#highpass

        """
        return FilterNode(
            *[self],
            name="highpass",
            kwargs={
                "frequency": frequency,
                "poles": poles,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def highshelf(
        self,
        *,
        gain: float,
        frequency: float,
        width_type: str,
        width: float,
        poles: int = None,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.116 treble, highshelf Boost or cut treble (upper) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi’s tone-controls. This is also known as shelving equalisation (EQ). The filter accepts the following options:

        Parameters:
        ----------
        gain:
            Give the gain at whichever is the lower of ~22 kHz and the Nyquist frequency. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency:
            Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Determine how steep is the filter’s shelf transition.
        poles:
            Set number of poles. Default is 2.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        return FilterNode(
            *[self],
            name="highshelf",
            kwargs={
                "gain": gain,
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def histeq(
        self, *, strength: float = None, intensity: float = None, antibanding: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.118 histeq This filter applies a global color histogram equalization on a per-frame basis. It can be used to correct video that has a compressed range of pixel intensities. The filter redistributes the pixel intensities to equalize their distribution across the intensity range. It may be viewed as an "automatically adjusting contrast filter". This filter is useful only for correcting degraded or poorly captured source video. The filter accepts the following options:

        Parameters:
        ----------
        strength:
            Determine the amount of equalization to be applied. As the strength is reduced, the distribution of pixel intensities more-and-more approaches that of the input frame. The value must be a float number in the range [0,1] and defaults to 0.200.
        intensity:
            Set the maximum intensity that can generated and scale the output values appropriately. The strength should be set as desired and then the intensity can be limited if needed to avoid washing-out. The value must be a float number in the range [0,1] and defaults to 0.210.
        antibanding:
            Set the antibanding level. If enabled the filter will randomly vary the luminance of output pixels by a small amount to avoid banding of the histogram. Possible values are none, weak or strong. It defaults to none.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#histeq

        """
        return FilterNode(
            *[self],
            name="histeq",
            kwargs={"strength": strength, "intensity": intensity, "antibanding": antibanding, **kwargs}
        ).stream()

    def histogram(
        self,
        *,
        level_height: int = None,
        scale_height: int = None,
        display_mode: str = None,
        levels_mode: str = None,
        components: int = None,
        fgopacity: float = None,
        bgopacity: float = None,
        colors_mode: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.119 histogram Compute and draw a color distribution histogram for the input video. The computed histogram is a representation of the color component distribution in an image. Standard histogram displays the color components distribution in an image. Displays color graph for each color component. Shows distribution of the Y, U, V, A or R, G, B components, depending on input format, in the current frame. Below each graph a color component scale meter is shown. The filter accepts the following options:

        Parameters:
        ----------
        level_height:
            Set height of level. Default value is 200. Allowed range is [50, 2048].
        scale_height:
            Set height of color scale. Default value is 12. Allowed range is [0, 40].
        display_mode:
            Set display mode. It accepts the following values: ‘stack’ Per color component graphs are placed below each other. ‘parade’ Per color component graphs are placed side by side. ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. Default is stack.
        levels_mode:
            Set mode. Can be either linear, or logarithmic. Default is linear.
        components:
            Set what color components to display. Default is 7.
        fgopacity:
            Set foreground opacity. Default is 0.7.
        bgopacity:
            Set background opacity. Default is 0.5.
        colors_mode:
            Set colors mode. It accepts the following values: ‘whiteonblack’ ‘blackonwhite’ ‘whiteongray’ ‘blackongray’ ‘coloronblack’ ‘coloronwhite’ ‘colorongray’ ‘blackoncolor’ ‘whiteoncolor’ ‘grayoncolor’ Default is whiteonblack.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#histogram

        """
        return FilterNode(
            *[self],
            name="histogram",
            kwargs={
                "level_height": level_height,
                "scale_height": scale_height,
                "display_mode": display_mode,
                "levels_mode": levels_mode,
                "components": components,
                "fgopacity": fgopacity,
                "bgopacity": bgopacity,
                "colors_mode": colors_mode,
                **kwargs,
            }
        ).stream()

    def hqdn3d(
        self,
        *,
        luma_spatial: float = None,
        chroma_spatial: float = None,
        luma_tmp: float = None,
        chroma_tmp: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.120 hqdn3d This is a high precision/quality 3d denoise filter. It aims to reduce image noise, producing smooth images and making still images really still. It should enhance compressibility. It accepts the following optional parameters:

        Parameters:
        ----------
        luma_spatial:
            A non-negative floating point number which specifies spatial luma strength. It defaults to 4.0.
        chroma_spatial:
            A non-negative floating point number which specifies spatial chroma strength. It defaults to 3.0*luma_spatial/4.0.
        luma_tmp:
            A floating point number which specifies luma temporal strength. It defaults to 6.0*luma_spatial/4.0.
        chroma_tmp:
            A floating point number which specifies chroma temporal strength. It defaults to luma_tmp*chroma_spatial/luma_spatial.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqdn3d

        """
        return FilterNode(
            *[self],
            name="hqdn3d",
            kwargs={
                "luma_spatial": luma_spatial,
                "chroma_spatial": chroma_spatial,
                "luma_tmp": luma_tmp,
                "chroma_tmp": chroma_tmp,
                **kwargs,
            }
        ).stream()

    def hqx(self, *, n: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.125 hqx Apply a high-quality magnification filter designed for pixel art. This filter was originally created by Maxim Stepin. It accepts the following option:

        Parameters:
        ----------
        n:
            Set the scaling dimension: 2 for hq2x, 3 for hq3x and 4 for hq4x. Default is 3.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hqx

        """
        return FilterNode(*[self], name="hqx", kwargs={"n": n, **kwargs}).stream()

    def hstack(self, *, inputs: int = None, shortest: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.126 hstack Stack input videos horizontally. All streams must be of same pixel format and of same height. Note that this filter is faster than using overlay and pad filter to create same output. The filter accepts the following option:

        Parameters:
        ----------
        inputs:
            Set number of input streams. Default is 2.
        shortest:
            If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hstack

        """
        return FilterNode(*[self], name="hstack", kwargs={"inputs": inputs, "shortest": shortest, **kwargs}).stream()

    def hsvhold(
        self,
        *,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.127 hsvhold Turns a certain HSV range into gray values. This filter measures color difference between set HSV color in options and ones measured in video stream. Depending on options, output colors can be changed to be gray or not. The filter accepts the following options:

        Parameters:
        ----------
        hue:
            Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        sat:
            Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        val:
            Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        similarity:
            Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        blend:
            Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully gray, or not gray at all. Higher values result in more gray pixels, with a higher gray pixel the more similar the pixels color is to the key color.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvhold

        """
        return FilterNode(
            *[self],
            name="hsvhold",
            kwargs={"hue": hue, "sat": sat, "val": val, "similarity": similarity, "blend": blend, **kwargs}
        ).stream()

    def hsvkey(
        self,
        *,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.128 hsvkey Turns a certain HSV range into transparency. This filter measures color difference between set HSV color in options and ones measured in video stream. Depending on options, output colors can be changed to transparent by adding alpha channel. The filter accepts the following options:

        Parameters:
        ----------
        hue:
            Set the hue value which will be used in color difference calculation. Allowed range is from -360 to 360. Default value is 0.
        sat:
            Set the saturation value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        val:
            Set the value which will be used in color difference calculation. Allowed range is from -1 to 1. Default value is 0.
        similarity:
            Set similarity percentage with the key color. Allowed range is from 0 to 1. Default value is 0.01. 0.00001 matches only the exact key color, while 1.0 matches everything.
        blend:
            Blend percentage. Allowed range is from 0 to 1. Default value is 0. 0.0 makes pixels either fully transparent, or not transparent at all. Higher values result in semi-transparent pixels, with a higher transparency the more similar the pixels color is to the key color.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hsvkey

        """
        return FilterNode(
            *[self],
            name="hsvkey",
            kwargs={"hue": hue, "sat": sat, "val": val, "similarity": similarity, "blend": blend, **kwargs}
        ).stream()

    def hue(self, *, h: str, s: str, H: str, b: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.129 hue Modify the hue and/or the saturation of the input. It accepts the following parameters: h and H are mutually exclusive, and can’t be specified at the same time. The b, h, H and s option values are expressions containing the following constants:

        Parameters:
        ----------
        h:
            Specify the hue angle as a number of degrees. It accepts an expression, and defaults to "0".
        s:
            Specify the saturation in the [-10,10] range. It accepts an expression and defaults to "1".
        H:
            Specify the hue angle as a number of radians. It accepts an expression, and defaults to "0".
        b:
            Specify the brightness in the [-10,10] range. It accepts an expression and defaults to "0".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hue

        """
        return FilterNode(*[self], name="hue", kwargs={"h": h, "s": s, "H": H, "b": b, **kwargs}).stream()

    def huesaturation(
        self,
        *,
        hue: float = None,
        saturation: float = None,
        intensity: float = None,
        colors: list[str],
        strength: float = None,
        rw: float = None,
        lightness: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.130 huesaturation Apply hue-saturation-intensity adjustments to input video stream. This filter operates in RGB colorspace. This filter accepts the following options:

        Parameters:
        ----------
        hue:
            Set the hue shift in degrees to apply. Default is 0. Allowed range is from -180 to 180.
        saturation:
            Set the saturation shift. Default is 0. Allowed range is from -1 to 1.
        intensity:
            Set the intensity shift. Default is 0. Allowed range is from -1 to 1.
        colors:
            Set which primary and complementary colors are going to be adjusted. This options is set by providing one or multiple values. This can select multiple colors at once. By default all colors are selected. ‘r’ Adjust reds. ‘y’ Adjust yellows. ‘g’ Adjust greens. ‘c’ Adjust cyans. ‘b’ Adjust blues. ‘m’ Adjust magentas. ‘a’ Adjust all colors.
        strength:
            Set strength of filtering. Allowed range is from 0 to 100. Default value is 1.
        rw:
            Set weight for each RGB component. Allowed range is from 0 to 1. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightess processing.
        lightness:
            Set preserving lightness, by default is disabled. Adjusting hues can change lightness from original RGB triplet, with this option enabled lightness is kept at same value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#huesaturation

        """
        return FilterNode(
            *[self],
            name="huesaturation",
            kwargs={
                "hue": hue,
                "saturation": saturation,
                "intensity": intensity,
                "colors": colors,
                "strength": strength,
                "rw": rw,
                "lightness": lightness,
                **kwargs,
            }
        ).stream()

    def hwdownload(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.121 hwdownload Download hardware frames to system memory. The input must be in hardware frames, and the output a non-hardware format. Not all formats will be supported on the output - it may be necessary to insert an additional format filter immediately following in the graph to get the output in a supported format.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwdownload

        """
        return FilterNode(*[self], name="hwdownload", kwargs={**kwargs}).stream()

    def hwmap(self, *, mode: str, derive_device: str, reverse: bool, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.122 hwmap Map hardware frames to system memory or to another device. This filter has several different modes of operation; which one is used depends on the input and output formats: Hardware frame input, normal frame output Map the input frames to system memory and pass them to the output. If the original hardware frame is later required (for example, after overlaying something else on part of it), the hwmap filter can be used again in the next mode to retrieve it. Normal frame input, hardware frame output If the input is actually a software-mapped hardware frame, then unmap it - that is, return the original hardware frame. Otherwise, a device must be provided. Create new hardware surfaces on that device for the output, then map them back to the software format at the input and give those frames to the preceding filter. This will then act like the hwupload filter, but may be able to avoid an additional copy when the input is already in a compatible format. Hardware frame input and output A device must be supplied for the output, either directly or with the derive_device option. The input and output devices must be of different types and compatible - the exact meaning of this is system-dependent, but typically it means that they must refer to the same underlying hardware context (for example, refer to the same graphics card). If the input frames were originally created on the output device, then unmap to retrieve the original frames. Otherwise, map the frames to the output device - create new hardware frames on the output corresponding to the frames on the input. The following additional parameters are accepted:

        Parameters:
        ----------
        mode:
            Set the frame mapping mode. Some combination of: read The mapped frame should be readable. write The mapped frame should be writeable. overwrite The mapping will always overwrite the entire frame. This may improve performance in some cases, as the original contents of the frame need not be loaded. direct The mapping must not involve any copying. Indirect mappings to copies of frames are created in some cases where either direct mapping is not possible or it would have unexpected properties. Setting this flag ensures that the mapping is direct and will fail if that is not possible. Defaults to read+write if not specified.
        derive_device:
            Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.
        reverse:
            In a hardware to hardware mapping, map in reverse - create frames in the sink and map them back to the source. This may be necessary in some cases where a mapping in one direction is required but only the opposite direction is supported by the devices being used. This option is dangerous - it may break the preceding filter in undefined ways if there are any additional constraints on that filter’s output. Do not use it without fully understanding the implications of its use.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwmap

        """
        return FilterNode(
            *[self], name="hwmap", kwargs={"mode": mode, "derive_device": derive_device, "reverse": reverse, **kwargs}
        ).stream()

    def hwupload(self, *, derive_device: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.123 hwupload Upload system memory frames to hardware surfaces. The device to upload to must be supplied when the filter is initialised. If using ffmpeg, select the appropriate device with the -filter_hw_device option or with the derive_device option. The input and output devices must be of different types and compatible - the exact meaning of this is system-dependent, but typically it means that they must refer to the same underlying hardware context (for example, refer to the same graphics card). The following additional parameters are accepted:

        Parameters:
        ----------
        derive_device:
            Rather than using the device supplied at initialisation, instead derive a new device of type type from the device the input frames exist on.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload

        """
        return FilterNode(*[self], name="hwupload", kwargs={"derive_device": derive_device, **kwargs}).stream()

    def hwupload_cuda(self, *, device: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.124 hwupload_cuda Upload system memory frames to a CUDA device. It accepts the following optional parameters:

        Parameters:
        ----------
        device:
            The number of the CUDA device to use



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hwupload_005fcuda

        """
        return FilterNode(*[self], name="hwupload_cuda", kwargs={"device": device, **kwargs}).stream()

    def hysteresis(self, *, planes: int, threshold: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.131 hysteresis Grow first stream into second stream by connecting components. This makes it possible to build more robust edge masks. This filter accepts the following options: The hysteresis filter also supports the framesync options.

        Parameters:
        ----------
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.
        threshold:
            Set threshold which is used in filtering. If pixel component value is higher than this value filter algorithm for connecting components is activated. By default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#hysteresis

        """
        return FilterNode(
            *[self], name="hysteresis", kwargs={"planes": planes, "threshold": threshold, **kwargs}
        ).stream()

    def iccdetect(self, *, force: bool = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.132 iccdetect Detect the colorspace from an embedded ICC profile (if present), and update the frame’s tags accordingly. This filter accepts the following options:

        Parameters:
        ----------
        force:
            If true, the frame’s existing colorspace tags will always be overridden by values detected from an ICC profile. Otherwise, they will only be assigned if they contain unknown. Enabled by default.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccdetect

        """
        return FilterNode(*[self], name="iccdetect", kwargs={"force": force, **kwargs}).stream()

    def iccgen(
        self, *, color_primaries: str = None, color_trc: str = None, force: bool = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.133 iccgen Generate ICC profiles and attach them to frames. This filter accepts the following options:

        Parameters:
        ----------
        color_primaries:
            Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        color_trc:
            Configure the colorspace that the ICC profile will be generated for. The default value of auto infers the value from the input frame’s metadata, defaulting to BT.709/sRGB as appropriate. See the setparams filter for a list of possible values, but note that unknown are not valid values for this filter.
        force:
            If true, an ICC profile will be generated even if it would overwrite an already existing ICC profile. Disabled by default.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#iccgen

        """
        return FilterNode(
            *[self],
            name="iccgen",
            kwargs={"color_primaries": color_primaries, "color_trc": color_trc, "force": force, **kwargs}
        ).stream()

    def identity(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.134 identity Obtain the identity score between two input videos. This filter takes two input videos. Both input videos must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The obtained per component, average, min and max identity score is printed through the logging system. The filter stores the calculated identity scores of each frame in frame metadata. This filter also supports the framesync options. In the below example the input file main.mpg being processed is compared with the reference file ref.mpg. ffmpeg -i main.mpg -i ref.mpg -lavfi identity -f null -

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#identity

        """
        return FilterNode(*[self], name="identity", kwargs={**kwargs}).stream()

    def il(
        self,
        *,
        luma_mode: str = None,
        chroma_mode: str = None,
        alpha_mode: str = None,
        luma_swap: int = None,
        chroma_swap: int = None,
        alpha_swap: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.136 il Deinterleave or interleave fields. This filter allows one to process interlaced images fields without deinterlacing them. Deinterleaving splits the input frame into 2 fields (so called half pictures). Odd lines are moved to the top half of the output image, even lines to the bottom half. You can process (filter) them independently and then re-interleave them. The filter accepts the following options:

        Parameters:
        ----------
        luma_mode:
            Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        chroma_mode:
            Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        alpha_mode:
            Available values for luma_mode, chroma_mode and alpha_mode are: ‘none’ Do nothing. ‘deinterleave, d’ Deinterleave fields, placing one above the other. ‘interleave, i’ Interleave fields. Reverse the effect of deinterleaving. Default value is none.
        luma_swap:
            Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        chroma_swap:
            Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
        alpha_swap:
            Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#il

        """
        return FilterNode(
            *[self],
            name="il",
            kwargs={
                "luma_mode": luma_mode,
                "chroma_mode": chroma_mode,
                "alpha_mode": alpha_mode,
                "luma_swap": luma_swap,
                "chroma_swap": chroma_swap,
                "alpha_swap": alpha_swap,
                **kwargs,
            }
        ).stream()

    def inflate(
        self,
        *,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.137 inflate Apply inflate effect to the video. This filter replaces the pixel by the local(3x3) average by taking into account only values higher than the pixel. It accepts the following options:

        Parameters:
        ----------
        threshold0:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold1:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold2:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.
        threshold3:
            Limit the maximum change for each plane, default is 65535. If 0, plane will remain unchanged.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#inflate

        """
        return FilterNode(
            *[self],
            name="inflate",
            kwargs={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
                **kwargs,
            }
        ).stream()

    def interlace(self, *, scan: str = None, lowpass: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.138 interlace Simple interlacing filter from progressive contents. This interleaves upper (or lower) lines from odd frames with lower (or upper) lines from even frames, halving the frame rate and preserving image height. Original Original New Frame Frame 'j' Frame 'j+1' (tff) ========== =========== ================== Line 0 --------------------> Frame 'j' Line 0 Line 1 Line 1 ----> Frame 'j+1' Line 1 Line 2 ---------------------> Frame 'j' Line 2 Line 3 Line 3 ----> Frame 'j+1' Line 3 ... ... ... New Frame + 1 will be generated by Frame 'j+2' and Frame 'j+3' and so on It accepts the following optional parameters:

        Parameters:
        ----------
        scan:
            This determines whether the interlaced frame is taken from the even (tff - default) or odd (bff) lines of the progressive frame.
        lowpass:
            Vertical lowpass filter to avoid twitter interlacing and reduce moire patterns. ‘0, off’ Disable vertical lowpass filter ‘1, linear’ Enable linear filter (default) ‘2, complex’ Enable complex filter. This will slightly less reduce twitter and moire but better retain detail and subjective sharpness impression.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#interlace

        """
        return FilterNode(*[self], name="interlace", kwargs={"scan": scan, "lowpass": lowpass, **kwargs}).stream()

    def join(self, *, inputs: int = None, channel_layout: str = None, map: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.95 join Join multiple input streams into one multi-channel stream. It accepts the following parameters: The filter will attempt to guess the mappings when they are not specified explicitly. It does so by first trying to find an unused matching input channel and if that fails it picks the first unused input channel. Join 3 inputs (with properly set channel layouts): ffmpeg -i INPUT1 -i INPUT2 -i INPUT3 -filter_complex join=inputs=3 OUTPUT Build a 5.1 output from 6 single-channel streams: ffmpeg -i fl -i fr -i fc -i sl -i sr -i lfe -filter_complex 'join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-SL|4.0-SR|5.0-LFE' out

        Parameters:
        ----------
        inputs:
            The number of input streams. It defaults to 2.
        channel_layout:
            The desired output channel layout. It defaults to stereo.
        map:
            Map channels from inputs to output. The argument is a ’|’-separated list of mappings, each in the input_idx.in_channel-out_channel form. input_idx is the 0-based index of the input stream. in_channel can be either the name of the input channel (e.g. FL for front left) or its index in the specified input stream. out_channel is the name of the output channel.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#join

        """
        return FilterNode(
            *[self], name="join", kwargs={"inputs": inputs, "channel_layout": channel_layout, "map": map, **kwargs}
        ).stream()

    def kerndeint(
        self,
        *,
        thresh: int = None,
        map: int = None,
        order: int = None,
        sharp: int = None,
        twoway: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.139 kerndeint Deinterlace input video by applying Donald Graft’s adaptive kernel deinterling. Work on interlaced parts of a video to produce progressive frames. The description of the accepted parameters follows.

        Parameters:
        ----------
        thresh:
            Set the threshold which affects the filter’s tolerance when determining if a pixel line must be processed. It must be an integer in the range [0,255] and defaults to 10. A value of 0 will result in applying the process on every pixels.
        map:
            Paint pixels exceeding the threshold value to white if set to 1. Default is 0.
        order:
            Set the fields order. Swap fields if set to 1, leave fields alone if 0. Default is 0.
        sharp:
            Enable additional sharpening if set to 1. Default is 0.
        twoway:
            Enable twoway sharpening if set to 1. Default is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#kerndeint

        """
        return FilterNode(
            *[self],
            name="kerndeint",
            kwargs={"thresh": thresh, "map": map, "order": order, "sharp": sharp, "twoway": twoway, **kwargs}
        ).stream()

    def kirsch(self, *, planes: int, scale: float, delta: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.140 kirsch Apply kirsch operator to input video stream. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        scale:
            Set value which will be multiplied with filtered result.
        delta:
            Set value which will be added to filtered result.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#kirsch

        """
        return FilterNode(
            *[self], name="kirsch", kwargs={"planes": planes, "scale": scale, "delta": delta, **kwargs}
        ).stream()

    def ladspa(
        self,
        *,
        file: str,
        plugin: str,
        controls: str,
        sample_rate: int = None,
        nb_samples: int = None,
        duration: str,
        latency: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.96 ladspa Load a LADSPA (Linux Audio Developer’s Simple Plugin API) plugin. To enable compilation of this filter you need to configure FFmpeg with --enable-ladspa.

        Parameters:
        ----------
        file:
            Specifies the name of LADSPA plugin library to load. If the environment variable LADSPA_PATH is defined, the LADSPA plugin is searched in each one of the directories specified by the colon separated list in LADSPA_PATH, otherwise in the standard LADSPA paths, which are in this order: HOME/.ladspa/lib/, /usr/local/lib/ladspa/, /usr/lib/ladspa/.
        plugin:
            Specifies the plugin within the library. Some libraries contain only one plugin, but others contain many of them. If this is not set filter will list all available plugins within the specified library.
        controls:
            Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). Controls need to be defined using the following syntax: c0=value0|c1=value1|c2=value2|..., where valuei is the value set on the i-th control. Alternatively they can be also defined using the following syntax: value0|value1|value2|..., where valuei is the value set on the i-th control. If controls is set to help, all available controls and their valid ranges are printed.
        sample_rate:
            Specify the sample rate, default to 44100. Only used if plugin have zero inputs.
        nb_samples:
            Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.
        duration:
            Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.
        latency:
            Enable latency compensation, by default is disabled. Only used if plugin have inputs.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ladspa

        """
        return FilterNode(
            *[self],
            name="ladspa",
            kwargs={
                "file": file,
                "plugin": plugin,
                "controls": controls,
                "sample_rate": sample_rate,
                "nb_samples": nb_samples,
                "duration": duration,
                "latency": latency,
                **kwargs,
            }
        ).stream()

    def lagfun(self, *, decay: float = None, planes: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.141 lagfun Slowly update darker pixels. This filter makes short flashes of light appear longer. This filter accepts the following options:

        Parameters:
        ----------
        decay:
            Set factor for decaying. Default is .95. Allowed range is from 0 to 1.
        planes:
            Set which planes to filter. Default is all. Allowed range is from 0 to 15.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lagfun

        """
        return FilterNode(*[self], name="lagfun", kwargs={"decay": decay, "planes": planes, **kwargs}).stream()

    def lenscorrection(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.142 lenscorrection Correct radial lens distortion This filter can be used to correct for radial distortion as can result from the use of wide angle lenses, and thereby re-rectify the image. To find the right parameters one can use tools available for example as part of opencv or simply trial-and-error. To use opencv use the calibration sample (under samples/cpp) from the opencv sources and extract the k1 and k2 coefficients from the resulting matrix. Note that effectively the same filter is available in the open-source tools Krita and Digikam from the KDE project. In contrast to the vignette filter, which can also be used to compensate lens errors, this filter corrects the distortion of the image, whereas vignette corrects the brightness distribution, so you may want to use both filters together in certain cases, though you will have to take care of ordering, i.e. whether vignetting should be applied before or after lens correction.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lenscorrection

        """
        return FilterNode(*[self], name="lenscorrection", kwargs={**kwargs}).stream()

    def lensfun(
        self,
        *,
        make: str,
        model: str,
        lens_model: str,
        db_path: str,
        mode: str,
        focal_length: float,
        aperture: float,
        focus_distance: float,
        scale: float,
        target_geometry: str,
        reverse: bool,
        interpolation: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.143 lensfun Apply lens correction via the lensfun library (http://lensfun.sourceforge.net/). The lensfun filter requires the camera make, camera model, and lens model to apply the lens correction. The filter will load the lensfun database and query it to find the corresponding camera and lens entries in the database. As long as these entries can be found with the given options, the filter can perform corrections on frames. Note that incomplete strings will result in the filter choosing the best match with the given options, and the filter will output the chosen camera and lens models (logged with level "info"). You must provide the make, camera model, and lens model as they are required. To obtain a list of available makes and models, leave out one or both of make and model options. The filter will send the full list to the log with level INFO. The first column is the make and the second column is the model. To obtain a list of available lenses, set any values for make and model and leave out the lens_model option. The filter will send the full list of lenses in the log with level INFO. The ffmpeg tool will exit after the list is printed. The filter accepts the following options:

        Parameters:
        ----------
        make:
            The make of the camera (for example, "Canon"). This option is required.
        model:
            The model of the camera (for example, "Canon EOS 100D"). This option is required.
        lens_model:
            The model of the lens (for example, "Canon EF-S 18-55mm f/3.5-5.6 IS STM"). This option is required.
        db_path:
            The full path to the lens database folder. If not set, the filter will attempt to load the database from the install path when the library was built. Default is unset.
        mode:
            The type of correction to apply. The following values are valid options: ‘vignetting’ Enables fixing lens vignetting. ‘geometry’ Enables fixing lens geometry. This is the default. ‘subpixel’ Enables fixing chromatic aberrations. ‘vig_geo’ Enables fixing lens vignetting and lens geometry. ‘vig_subpixel’ Enables fixing lens vignetting and chromatic aberrations. ‘distortion’ Enables fixing both lens geometry and chromatic aberrations. ‘all’ Enables all possible corrections.
        focal_length:
            The focal length of the image/video (zoom; expected constant for video). For example, a 18–55mm lens has focal length range of [18–55], so a value in that range should be chosen when using that lens. Default 18.
        aperture:
            The aperture of the image/video (expected constant for video). Note that aperture is only used for vignetting correction. Default 3.5.
        focus_distance:
            The focus distance of the image/video (expected constant for video). Note that focus distance is only used for vignetting and only slightly affects the vignetting correction process. If unknown, leave it at the default value (which is 1000).
        scale:
            The scale factor which is applied after transformation. After correction the video is no longer necessarily rectangular. This parameter controls how much of the resulting image is visible. The value 0 means that a value will be chosen automatically such that there is little or no unmapped area in the output image. 1.0 means that no additional scaling is done. Lower values may result in more of the corrected image being visible, while higher values may avoid unmapped areas in the output.
        target_geometry:
            The target geometry of the output image/video. The following values are valid options: ‘rectilinear (default)’ ‘fisheye’ ‘panoramic’ ‘equirectangular’ ‘fisheye_orthographic’ ‘fisheye_stereographic’ ‘fisheye_equisolid’ ‘fisheye_thoby’
        reverse:
            Apply the reverse of image correction (instead of correcting distortion, apply it).
        interpolation:
            The type of interpolation used when correcting distortion. The following values are valid options: ‘nearest’ ‘linear (default)’ ‘lanczos’



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lensfun

        """
        return FilterNode(
            *[self],
            name="lensfun",
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
                **kwargs,
            }
        ).stream()

    def libplacebo(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.144 libplacebo Flexible GPU-accelerated processing filter based on libplacebo (https://code.videolan.org/videolan/libplacebo).

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#libplacebo

        """
        return FilterNode(*[self], name="libplacebo", kwargs={**kwargs}).stream()

    def libvmaf(
        self,
        *,
        model: str = None,
        feature: str,
        log_path: str,
        log_fmt: str,
        pool: str = None,
        n_threads: int = None,
        n_subsample: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.145 libvmaf Calculate the VMAF (Video Multi-Method Assessment Fusion) score for a reference/distorted pair of input videos. The first input is the distorted video, and the second input is the reference video. The obtained VMAF score is printed through the logging system. It requires Netflix’s vmaf library (libvmaf) as a pre-requisite. After installing the library it can be enabled using: ./configure --enable-libvmaf. The filter has following options: This filter also supports the framesync options.

        Parameters:
        ----------
        model:
            A ‘|‘ delimited list of vmaf models. Each model can be configured with a number of parameters. Default value: "version=vmaf_v0.6.1"
        feature:
            A ‘|‘ delimited list of features. Each feature can be configured with a number of parameters.
        log_path:
            Set the file path to be used to store log files.
        log_fmt:
            Set the format of the log file (xml, json, csv, or sub).
        pool:
            Set the pool method to be used for computing vmaf. Options are min, harmonic_mean or mean (default).
        n_threads:
            Set number of threads to be used when initializing libvmaf. Default value: 0, no threads.
        n_subsample:
            Set frame subsampling interval to be used.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#libvmaf

        """
        return FilterNode(
            *[self],
            name="libvmaf",
            kwargs={
                "model": model,
                "feature": feature,
                "log_path": log_path,
                "log_fmt": log_fmt,
                "pool": pool,
                "n_threads": n_threads,
                "n_subsample": n_subsample,
                **kwargs,
            }
        ).stream()

    def libvmaf_cuda(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.146 libvmaf_cuda This is the CUDA variant of the libvmaf filter. It only accepts CUDA frames. It requires Netflix’s vmaf library (libvmaf) as a pre-requisite. After installing the library it can be enabled using: ./configure --enable-nonfree --enable-ffnvcodec --enable-libvmaf.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#libvmaf_005fcuda

        """
        return FilterNode(*[self], name="libvmaf_cuda", kwargs={**kwargs}).stream()

    def limitdiff(
        self, *, threshold: float, elasticity: float, reference: bool, planes: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.147 limitdiff Apply limited difference filter using second and optionally third video stream. The filter accepts the following options:

        Parameters:
        ----------
        threshold:
            Set the threshold to use when allowing certain differences between video streams. Any absolute difference value lower or exact than this threshold will pick pixel components from first video stream.
        elasticity:
            Set the elasticity of soft thresholding when processing video streams. This value multiplied with first one sets second threshold. Any absolute difference value greater or exact than second threshold will pick pixel components from second video stream. For values between those two threshold linear interpolation between first and second video stream will be used.
        reference:
            Enable the reference (third) video stream processing. By default is disabled. If set, this video stream will be used for calculating absolute difference with first video stream.
        planes:
            Specify which planes will be processed. Defaults to all available.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#limitdiff

        """
        return FilterNode(
            *[self],
            name="limitdiff",
            kwargs={
                "threshold": threshold,
                "elasticity": elasticity,
                "reference": reference,
                "planes": planes,
                **kwargs,
            }
        ).stream()

    def limiter(self, *, min: float, max: float, planes: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.148 limiter Limits the pixel components values to the specified range [min, max]. The filter accepts the following options:

        Parameters:
        ----------
        min:
            Lower bound. Defaults to the lowest allowed value for the input.
        max:
            Upper bound. Defaults to the highest allowed value for the input.
        planes:
            Specify which planes will be processed. Defaults to all available.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#limiter

        """
        return FilterNode(*[self], name="limiter", kwargs={"min": min, "max": max, "planes": planes, **kwargs}).stream()

    def loop(self, *, loop: int, size: int, start: int, time: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.149 loop Loop video frames. The filter accepts the following options:

        Parameters:
        ----------
        loop:
            Set the number of loops. Setting this value to -1 will result in infinite loops. Default is 0.
        size:
            Set maximal size in number of frames. Default is 0.
        start:
            Set first frame of loop. Default is 0.
        time:
            Set the time of loop start in seconds. Only used if option named start is set to -1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#loop

        """
        return FilterNode(
            *[self], name="loop", kwargs={"loop": loop, "size": size, "start": start, "time": time, **kwargs}
        ).stream()

    def loudnorm(
        self,
        *,
        I: float = None,
        LRA: float = None,
        TP: float = None,
        measured_I: float,
        measured_LRA: float,
        measured_TP: float,
        measured_thresh: float,
        offset: float = None,
        linear: bool = None,
        dual_mono: bool = None,
        print_format: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.97 loudnorm EBU R128 loudness normalization. Includes both dynamic and linear normalization modes. Support for both single pass (livestreams, files) and double pass (files) modes. This algorithm can target IL, LRA, and maximum true peak. In dynamic mode, to accurately detect true peaks, the audio stream will be upsampled to 192 kHz. Use the -ar option or aresample filter to explicitly set an output sample rate. The filter accepts the following options:

        Parameters:
        ----------
        I:
            Set integrated loudness target. Range is -70.0 - -5.0. Default value is -24.0.
        LRA:
            Set loudness range target. Range is 1.0 - 50.0. Default value is 7.0.
        TP:
            Set maximum true peak. Range is -9.0 - +0.0. Default value is -2.0.
        measured_I:
            Measured IL of input file. Range is -99.0 - +0.0.
        measured_LRA:
            Measured LRA of input file. Range is 0.0 - 99.0.
        measured_TP:
            Measured true peak of input file. Range is -99.0 - +99.0.
        measured_thresh:
            Measured threshold of input file. Range is -99.0 - +0.0.
        offset:
            Set offset gain. Gain is applied before the true-peak limiter. Range is -99.0 - +99.0. Default is +0.0.
        linear:
            Normalize by linearly scaling the source audio. measured_I, measured_LRA, measured_TP, and measured_thresh must all be specified. Target LRA shouldn’t be lower than source LRA and the change in integrated loudness shouldn’t result in a true peak which exceeds the target TP. If any of these conditions aren’t met, normalization mode will revert to dynamic. Options are true or false. Default is true.
        dual_mono:
            Treat mono input files as "dual-mono". If a mono file is intended for playback on a stereo system, its EBU R128 measurement will be perceptually incorrect. If set to true, this option will compensate for this effect. Multi-channel input files are not affected by this option. Options are true or false. Default is false.
        print_format:
            Set print format for stats. Options are summary, json, or none. Default value is none.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#loudnorm

        """
        return FilterNode(
            *[self],
            name="loudnorm",
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
                **kwargs,
            }
        ).stream()

    def lowpass(
        self,
        *,
        frequency: float = None,
        poles: int = None,
        width_type: str = None,
        width: float = None,
        mix: float = None,
        channels: str = None,
        normalize: bool = None,
        transform: str,
        precision: str = None,
        block_size: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.98 lowpass Apply a low-pass filter with 3dB point frequency. The filter can be either single-pole or double-pole (the default). The filter roll off at 6dB per pole per octave (20dB per pole per decade). The filter accepts the following options:

        Parameters:
        ----------
        frequency:
            Set frequency in Hz. Default is 500.
        poles:
            Set number of poles. Default is 2.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Specify the band-width of a filter in width_type units. Applies only to double-pole filter. The default is 0.707q and gives a Butterworth response.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lowpass

        """
        return FilterNode(
            *[self],
            name="lowpass",
            kwargs={
                "frequency": frequency,
                "poles": poles,
                "width_type": width_type,
                "width": width,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def lowshelf(
        self,
        *,
        gain: float,
        frequency: float = None,
        width_type: str,
        width: float,
        poles: int = None,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.71 bass, lowshelf Boost or cut the bass (lower) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi’s tone-controls. This is also known as shelving equalisation (EQ). The filter accepts the following options:

        Parameters:
        ----------
        gain:
            Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency:
            Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Determine how steep is the filter’s shelf transition.
        poles:
            Set number of poles. Default is 2.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf

        """
        return FilterNode(
            *[self],
            name="lowshelf",
            kwargs={
                "gain": gain,
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def lumakey(
        self, *, threshold: float = None, tolerance: float = None, softness: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.152 lumakey Turn certain luma values into transparency. The filter accepts the following options:

        Parameters:
        ----------
        threshold:
            Set the luma which will be used as base for transparency. Default value is 0.
        tolerance:
            Set the range of luma values to be keyed out. Default value is 0.01.
        softness:
            Set the range of softness. Default value is 0. Use this to control gradual transition from zero to full transparency.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lumakey

        """
        return FilterNode(
            *[self],
            name="lumakey",
            kwargs={"threshold": threshold, "tolerance": tolerance, "softness": softness, **kwargs}
        ).stream()

    def lut(
        self,
        *,
        c0: str,
        c1: str,
        c2: str,
        c3: str,
        r: str,
        g: str,
        b: str,
        a: str,
        y: str,
        u: str,
        v: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.153 lut, lutrgb, lutyuv Compute a look-up table for binding each pixel component input value to an output value, and apply it to the input video. lutyuv applies a lookup table to a YUV input video, lutrgb to an RGB input video. These filters accept the following parameters: Each of them specifies the expression to use for computing the lookup table for the corresponding pixel component values. The exact component associated to each of the c* options depends on the format in input. The lut filter requires either YUV or RGB pixel formats in input, lutrgb requires RGB pixel formats in input, and lutyuv requires YUV. The expressions can contain the following constants and functions: All expressions default to "clipval".

        Parameters:
        ----------
        c0:
            set first pixel component expression
        c1:
            set second pixel component expression
        c2:
            set third pixel component expression
        c3:
            set fourth pixel component expression, corresponds to the alpha component
        r:
            set red component expression
        g:
            set green component expression
        b:
            set blue component expression
        a:
            alpha component expression
        y:
            set Y/luma component expression
        u:
            set U/Cb component expression
        v:
            set V/Cr component expression



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        return FilterNode(
            *[self],
            name="lut",
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
                "y": y,
                "u": u,
                "v": v,
                **kwargs,
            }
        ).stream()

    def lut1d(self, *, file: str, interp: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.150 lut1d Apply a 1D LUT to an input video. The filter accepts the following options:

        Parameters:
        ----------
        file:
            Set the 1D LUT file name. Currently supported formats: ‘cube’ Iridas ‘csp’ cineSpace
        interp:
            Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘linear’ Interpolate values using the linear interpolation. ‘cosine’ Interpolate values using the cosine interpolation. ‘cubic’ Interpolate values using the cubic interpolation. ‘spline’ Interpolate values using the spline interpolation.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut1d

        """
        return FilterNode(*[self], name="lut1d", kwargs={"file": file, "interp": interp, **kwargs}).stream()

    def lut2(self, *, c0: str, c1: str, c2: str, c3: str, d: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.154 lut2, tlut2 The lut2 filter takes two input streams and outputs one stream. The tlut2 (time lut2) filter takes two consecutive frames from one single stream. This filter accepts the following parameters: The lut2 filter also supports the framesync options. Each of them specifies the expression to use for computing the lookup table for the corresponding pixel component values. The exact component associated to each of the c* options depends on the format in inputs. The expressions can contain the following constants: All expressions default to "x".

        Parameters:
        ----------
        c0:
            set first pixel component expression
        c1:
            set second pixel component expression
        c2:
            set third pixel component expression
        c3:
            set fourth pixel component expression, corresponds to the alpha component
        d:
            set output bit depth, only available for lut2 filter. By default is 0, which means bit depth is automatically picked from first input format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

        """
        return FilterNode(
            *[self], name="lut2", kwargs={"c0": c0, "c1": c1, "c2": c2, "c3": c3, "d": d, **kwargs}
        ).stream()

    def lut3d(self, *, file: str, interp: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.151 lut3d Apply a 3D LUT to an input video. The filter accepts the following options:

        Parameters:
        ----------
        file:
            Set the 3D LUT file name. Currently supported formats: ‘3dl’ AfterEffects ‘cube’ Iridas ‘dat’ DaVinci ‘m3d’ Pandora ‘csp’ cineSpace
        interp:
            Select interpolation mode. Available values are: ‘nearest’ Use values from the nearest defined point. ‘trilinear’ Interpolate values using the 8 points defining a cube. ‘tetrahedral’ Interpolate values using a tetrahedron. ‘pyramid’ Interpolate values using a pyramid. ‘prism’ Interpolate values using a prism.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut3d

        """
        return FilterNode(*[self], name="lut3d", kwargs={"file": file, "interp": interp, **kwargs}).stream()

    def lutrgb(
        self,
        *,
        c0: str,
        c1: str,
        c2: str,
        c3: str,
        r: str,
        g: str,
        b: str,
        a: str,
        y: str,
        u: str,
        v: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.153 lut, lutrgb, lutyuv Compute a look-up table for binding each pixel component input value to an output value, and apply it to the input video. lutyuv applies a lookup table to a YUV input video, lutrgb to an RGB input video. These filters accept the following parameters: Each of them specifies the expression to use for computing the lookup table for the corresponding pixel component values. The exact component associated to each of the c* options depends on the format in input. The lut filter requires either YUV or RGB pixel formats in input, lutrgb requires RGB pixel formats in input, and lutyuv requires YUV. The expressions can contain the following constants and functions: All expressions default to "clipval".

        Parameters:
        ----------
        c0:
            set first pixel component expression
        c1:
            set second pixel component expression
        c2:
            set third pixel component expression
        c3:
            set fourth pixel component expression, corresponds to the alpha component
        r:
            set red component expression
        g:
            set green component expression
        b:
            set blue component expression
        a:
            alpha component expression
        y:
            set Y/luma component expression
        u:
            set U/Cb component expression
        v:
            set V/Cr component expression



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        return FilterNode(
            *[self],
            name="lutrgb",
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
                "y": y,
                "u": u,
                "v": v,
                **kwargs,
            }
        ).stream()

    def lutyuv(
        self,
        *,
        c0: str,
        c1: str,
        c2: str,
        c3: str,
        r: str,
        g: str,
        b: str,
        a: str,
        y: str,
        u: str,
        v: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.153 lut, lutrgb, lutyuv Compute a look-up table for binding each pixel component input value to an output value, and apply it to the input video. lutyuv applies a lookup table to a YUV input video, lutrgb to an RGB input video. These filters accept the following parameters: Each of them specifies the expression to use for computing the lookup table for the corresponding pixel component values. The exact component associated to each of the c* options depends on the format in input. The lut filter requires either YUV or RGB pixel formats in input, lutrgb requires RGB pixel formats in input, and lutyuv requires YUV. The expressions can contain the following constants and functions: All expressions default to "clipval".

        Parameters:
        ----------
        c0:
            set first pixel component expression
        c1:
            set second pixel component expression
        c2:
            set third pixel component expression
        c3:
            set fourth pixel component expression, corresponds to the alpha component
        r:
            set red component expression
        g:
            set green component expression
        b:
            set blue component expression
        a:
            alpha component expression
        y:
            set Y/luma component expression
        u:
            set U/Cb component expression
        v:
            set V/Cr component expression



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv

        """
        return FilterNode(
            *[self],
            name="lutyuv",
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
                "y": y,
                "u": u,
                "v": v,
                **kwargs,
            }
        ).stream()

    def lv2(
        self,
        *,
        plugin: str,
        controls: str,
        sample_rate: int = None,
        nb_samples: int = None,
        duration: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.99 lv2 Load a LV2 (LADSPA Version 2) plugin. To enable compilation of this filter you need to configure FFmpeg with --enable-lv2.

        Parameters:
        ----------
        plugin:
            Specifies the plugin URI. You may need to escape ’:’.
        controls:
            Set the ’|’ separated list of controls which are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). If controls is set to help, all available controls and their valid ranges are printed.
        sample_rate:
            Specify the sample rate, default to 44100. Only used if plugin have zero inputs.
        nb_samples:
            Set the number of samples per channel per each output frame, default is 1024. Only used if plugin have zero inputs.
        duration:
            Set the minimum duration of the sourced audio. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the resulting duration may be greater than the specified duration, as the generated audio is always cut at the end of a complete frame. If not specified, or the expressed duration is negative, the audio is supposed to be generated forever. Only used if plugin have zero inputs.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lv2

        """
        return FilterNode(
            *[self],
            name="lv2",
            kwargs={
                "plugin": plugin,
                "controls": controls,
                "sample_rate": sample_rate,
                "nb_samples": nb_samples,
                "duration": duration,
                **kwargs,
            }
        ).stream()

    def maskedclamp(
        self, *, undershoot: float = None, overshoot: float = None, planes: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.155 maskedclamp Clamp the first input stream with the second input and third input stream. Returns the value of first stream to be between second input stream - undershoot and third input stream + overshoot. This filter accepts the following options:

        Parameters:
        ----------
        undershoot:
            Default value is 0.
        overshoot:
            Default value is 0.
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedclamp

        """
        return FilterNode(
            *[self],
            name="maskedclamp",
            kwargs={"undershoot": undershoot, "overshoot": overshoot, "planes": planes, **kwargs}
        ).stream()

    def maskedmax(self, *, planes: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.156 maskedmax Merge the second and third input stream into output stream using absolute differences between second input stream and first input stream and absolute difference between third input stream and first input stream. The picked value will be from second input stream if second absolute difference is greater than first one or from third input stream otherwise. This filter accepts the following options:

        Parameters:
        ----------
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmax

        """
        return FilterNode(*[self], name="maskedmax", kwargs={"planes": planes, **kwargs}).stream()

    def maskedmerge(self, *, planes: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.157 maskedmerge Merge the first input stream with the second input stream using per pixel weights in the third input stream. A value of 0 in the third stream pixel component means that pixel component from first stream is returned unchanged, while maximum value (eg. 255 for 8-bit videos) means that pixel component from second stream is returned unchanged. Intermediate values define the amount of merging between both input stream’s pixel components. This filter accepts the following options:

        Parameters:
        ----------
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmerge

        """
        return FilterNode(*[self], name="maskedmerge", kwargs={"planes": planes, **kwargs}).stream()

    def maskedmin(self, *, planes: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.158 maskedmin Merge the second and third input stream into output stream using absolute differences between second input stream and first input stream and absolute difference between third input stream and first input stream. The picked value will be from second input stream if second absolute difference is less than first one or from third input stream otherwise. This filter accepts the following options:

        Parameters:
        ----------
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from first stream. By default value 0xf, all planes will be processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedmin

        """
        return FilterNode(*[self], name="maskedmin", kwargs={"planes": planes, **kwargs}).stream()

    def maskedthreshold(self, *, threshold: float, planes: int, mode: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.159 maskedthreshold Pick pixels comparing absolute difference of two video streams with fixed threshold. If absolute difference between pixel component of first and second video stream is equal or lower than user supplied threshold than pixel component from first video stream is picked, otherwise pixel component from second video stream is picked. This filter accepts the following options:

        Parameters:
        ----------
        threshold:
            Set threshold used when picking pixels from absolute difference from two input video streams.
        planes:
            Set which planes will be processed as bitmap, unprocessed planes will be copied from second stream. By default value 0xf, all planes will be processed.
        mode:
            Set mode of filter operation. Can be abs or diff. Default is abs.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskedthreshold

        """
        return FilterNode(
            *[self], name="maskedthreshold", kwargs={"threshold": threshold, "planes": planes, "mode": mode, **kwargs}
        ).stream()

    def maskfun(
        self, *, low: float, high: float, planes: str, fill: float, sum: float, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.160 maskfun Create mask from input video. For example it is useful to create motion masks after tblend filter. This filter accepts the following options:

        Parameters:
        ----------
        low:
            Set low threshold. Any pixel component lower or exact than this value will be set to 0.
        high:
            Set high threshold. Any pixel component higher than this value will be set to max value allowed for current pixel format.
        planes:
            Set planes to filter, by default all available planes are filtered.
        fill:
            Fill all frame pixels with this value.
        sum:
            Set max average pixel value for frame. If sum of all pixel components is higher that this average, output frame will be completely filled with value set by fill option. Typically useful for scene changes when used in combination with tblend filter.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#maskfun

        """
        return FilterNode(
            *[self],
            name="maskfun",
            kwargs={"low": low, "high": high, "planes": planes, "fill": fill, "sum": sum, **kwargs}
        ).stream()

    def mcdeint(self, *, mode: str = None, parity: str = None, qp: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.161 mcdeint Apply motion-compensation deinterlacing. It needs one field per frame as input and must thus be used together with yadif=1/3 or equivalent. This filter accepts the following options:

        Parameters:
        ----------
        mode:
            Set the deinterlacing mode. It accepts one of the following values: ‘fast’ ‘medium’ ‘slow’ use iterative motion estimation ‘extra_slow’ like ‘slow’, but use multiple reference frames. Default value is ‘fast’.
        parity:
            Set the picture field parity assumed for the input video. It must be one of the following values: ‘0, tff’ assume top field first ‘1, bff’ assume bottom field first Default value is ‘bff’.
        qp:
            Set per-block quantization parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcdeint

        """
        return FilterNode(*[self], name="mcdeint", kwargs={"mode": mode, "parity": parity, "qp": qp, **kwargs}).stream()

    def mcompand(self, *, args: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.100 mcompand Multiband Compress or expand the audio’s dynamic range. The input audio is divided into bands using 4th order Linkwitz-Riley IIRs. This is akin to the crossover of a loudspeaker, and results in flat frequency response when absent compander action. It accepts the following parameters:

        Parameters:
        ----------
        args:
            This option syntax is: attack,decay,[attack,decay..] soft-knee points crossover_frequency [delay [initial_volume [gain]]] | attack,decay ... For explanation of each item refer to compand filter documentation.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mcompand

        """
        return FilterNode(*[self], name="mcompand", kwargs={"args": args, **kwargs}).stream()

    def median(
        self,
        *,
        radius: int = None,
        planes: int = None,
        radiusV: int = None,
        percentile: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.162 median Pick median pixel from certain rectangle defined by radius. This filter accepts the following options:

        Parameters:
        ----------
        radius:
            Set horizontal radius size. Default value is 1. Allowed range is integer from 1 to 127.
        planes:
            Set which planes to process. Default is 15, which is all available planes.
        radiusV:
            Set vertical radius size. Default value is 0. Allowed range is integer from 0 to 127. If it is 0, value will be picked from horizontal radius option.
        percentile:
            Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#median

        """
        return FilterNode(
            *[self],
            name="median",
            kwargs={"radius": radius, "planes": planes, "radiusV": radiusV, "percentile": percentile, **kwargs}
        ).stream()

    def mergeplanes(
        self,
        *,
        mapping: str = None,
        format: str = None,
        map0s: int = None,
        map1s: int = None,
        map2s: int = None,
        map3s: int = None,
        map0p: int = None,
        map1p: int = None,
        map2p: int = None,
        map3p: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.163 mergeplanes Merge color channel components from several video streams. The filter accepts up to 4 input streams, and merge selected input planes to the output video. This filter accepts the following options:

        Parameters:
        ----------
        mapping:
            Set input to output plane mapping. Default is 0. The mappings is specified as a bitmap. It should be specified as a hexadecimal number in the form 0xAa[Bb[Cc[Dd]]]. ’Aa’ describes the mapping for the first plane of the output stream. ’A’ sets the number of the input stream to use (from 0 to 3), and ’a’ the plane number of the corresponding input to use (from 0 to 3). The rest of the mappings is similar, ’Bb’ describes the mapping for the output stream second plane, ’Cc’ describes the mapping for the output stream third plane and ’Dd’ describes the mapping for the output stream fourth plane.
        format:
            Set output pixel format. Default is yuva444p.
        map0s:
            Set input to output stream mapping for output Nth plane. Default is 0.
        map1s:
            Set input to output stream mapping for output Nth plane. Default is 0.
        map2s:
            Set input to output stream mapping for output Nth plane. Default is 0.
        map3s:
            Set input to output stream mapping for output Nth plane. Default is 0.
        map0p:
            Set input to output plane mapping for output Nth plane. Default is 0.
        map1p:
            Set input to output plane mapping for output Nth plane. Default is 0.
        map2p:
            Set input to output plane mapping for output Nth plane. Default is 0.
        map3p:
            Set input to output plane mapping for output Nth plane. Default is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mergeplanes

        """
        return FilterNode(
            *[self],
            name="mergeplanes",
            kwargs={
                "mapping": mapping,
                "format": format,
                "map0s": map0s,
                "map1s": map1s,
                "map2s": map2s,
                "map3s": map3s,
                "map0p": map0p,
                "map1p": map1p,
                "map2p": map2p,
                "map3p": map3p,
                **kwargs,
            }
        ).stream()

    def mestimate(
        self, *, method: str = None, mb_size: int = None, search_param: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.164 mestimate Estimate and export motion vectors using block matching algorithms. Motion vectors are stored in frame side data to be used by other filters. This filter accepts the following options:

        Parameters:
        ----------
        method:
            Specify the motion estimation method. Accepts one of the following values: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default value is ‘esa’.
        mb_size:
            Macroblock size. Default 16.
        search_param:
            Search parameter. Default 7.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mestimate

        """
        return FilterNode(
            *[self],
            name="mestimate",
            kwargs={"method": method, "mb_size": mb_size, "search_param": search_param, **kwargs}
        ).stream()

    def midequalizer(self, *, planes: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.165 midequalizer Apply Midway Image Equalization effect using two video streams. Midway Image Equalization adjusts a pair of images to have the same histogram, while maintaining their dynamics as much as possible. It’s useful for e.g. matching exposures from a pair of stereo cameras. This filter has two inputs and one output, which must be of same pixel format, but may be of different sizes. The output of filter is first input adjusted with midway histogram of both inputs. This filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes to process. Default is 15, which is all available planes.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#midequalizer

        """
        return FilterNode(*[self], name="midequalizer", kwargs={"planes": planes, **kwargs}).stream()

    def minterpolate(
        self, *, fps: str, mi_mode: str, scd: str, scd_threshold: float, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.166 minterpolate Convert the video to specified frame rate using motion interpolation. This filter accepts the following options:

        Parameters:
        ----------
        fps:
            Specify the output frame rate. This can be rational e.g. 60000/1001. Frames are dropped if fps is lower than source fps. Default 60.
        mi_mode:
            Motion interpolation mode. Following values are accepted: ‘dup’ Duplicate previous or next frame for interpolating new ones. ‘blend’ Blend source frames. Interpolated frame is mean of previous and next frames. ‘mci’ Motion compensated interpolation. Following options are effective when this mode is selected: ‘mc_mode’ Motion compensation mode. Following values are accepted: ‘obmc’ Overlapped block motion compensation. ‘aobmc’ Adaptive overlapped block motion compensation. Window weighting coefficients are controlled adaptively according to the reliabilities of the neighboring motion vectors to reduce oversmoothing. Default mode is ‘obmc’. ‘me_mode’ Motion estimation mode. Following values are accepted: ‘bidir’ Bidirectional motion estimation. Motion vectors are estimated for each source frame in both forward and backward directions. ‘bilat’ Bilateral motion estimation. Motion vectors are estimated directly for interpolated frame. Default mode is ‘bilat’. ‘me’ The algorithm to be used for motion estimation. Following values are accepted: ‘esa’ Exhaustive search algorithm. ‘tss’ Three step search algorithm. ‘tdls’ Two dimensional logarithmic search algorithm. ‘ntss’ New three step search algorithm. ‘fss’ Four step search algorithm. ‘ds’ Diamond search algorithm. ‘hexbs’ Hexagon-based search algorithm. ‘epzs’ Enhanced predictive zonal search algorithm. ‘umh’ Uneven multi-hexagon search algorithm. Default algorithm is ‘epzs’. ‘mb_size’ Macroblock size. Default 16. ‘search_param’ Motion estimation search parameter. Default 32. ‘vsbmc’ Enable variable-size block motion compensation. Motion estimation is applied with smaller block sizes at object boundaries in order to make the them less blur. Default is 0 (disabled).
        scd:
            Scene change detection method. Scene change leads motion vectors to be in random direction. Scene change detection replace interpolated frames by duplicate ones. May not be needed for other modes. Following values are accepted: ‘none’ Disable scene change detection. ‘fdiff’ Frame difference. Corresponding pixel values are compared and if it satisfies scd_threshold scene change is detected. Default method is ‘fdiff’.
        scd_threshold:
            Scene change detection threshold. Default is 10..



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#minterpolate

        """
        return FilterNode(
            *[self],
            name="minterpolate",
            kwargs={"fps": fps, "mi_mode": mi_mode, "scd": scd, "scd_threshold": scd_threshold, **kwargs}
        ).stream()

    def mix(
        self,
        *,
        inputs: int = None,
        weights: str,
        scale: float,
        planes: int = None,
        duration: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.167 mix Mix several video input streams into one video stream. A description of the accepted options follows.

        Parameters:
        ----------
        inputs:
            The number of inputs. If unspecified, it defaults to 2.
        weights:
            Specify weight of each input video stream as sequence. Each weight is separated by space. If number of weights is smaller than number of frames last specified weight will be used for all remaining unset weights.
        scale:
            Specify scale, if it is set it will be multiplied with sum of each weight multiplied with pixel values to give final destination pixel value. By default scale is auto scaled to sum of weights.
        planes:
            Set which planes to filter. Default is all. Allowed range is from 0 to 15.
        duration:
            Specify how end of stream is determined. ‘longest’ The duration of the longest input. (default) ‘shortest’ The duration of the shortest input. ‘first’ The duration of the first input.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mix

        """
        return FilterNode(
            *[self],
            name="mix",
            kwargs={
                "inputs": inputs,
                "weights": weights,
                "scale": scale,
                "planes": planes,
                "duration": duration,
                **kwargs,
            }
        ).stream()

    def monochrome(
        self, *, cb: float = None, cr: float = None, size: float = None, high: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.168 monochrome Convert video to gray using custom color filter. A description of the accepted options follows.

        Parameters:
        ----------
        cb:
            Set the chroma blue spot. Allowed range is from -1 to 1. Default value is 0.
        cr:
            Set the chroma red spot. Allowed range is from -1 to 1. Default value is 0.
        size:
            Set the color filter size. Allowed range is from .1 to 10. Default value is 1.
        high:
            Set the highlights strength. Allowed range is from 0 to 1. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#monochrome

        """
        return FilterNode(
            *[self], name="monochrome", kwargs={"cb": cb, "cr": cr, "size": size, "high": high, **kwargs}
        ).stream()

    def morpho(self, *, mode: str = None, planes: str, structure: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.169 morpho This filter allows to apply main morphological grayscale transforms, erode and dilate with arbitrary structures set in second input stream. Unlike naive implementation and much slower performance in erosion and dilation filters, when speed is critical morpho filter should be used instead. A description of accepted options follows, The morpho filter also supports the framesync options.

        Parameters:
        ----------
        mode:
            Set morphological transform to apply, can be: ‘erode’ ‘dilate’ ‘open’ ‘close’ ‘gradient’ ‘tophat’ ‘blackhat’ Default is erode.
        planes:
            Set planes to filter, by default all planes except alpha are filtered.
        structure:
            Set which structure video frames will be processed from second input stream, can be first or all. Default is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#morpho

        """
        return FilterNode(
            *[self], name="morpho", kwargs={"mode": mode, "planes": planes, "structure": structure, **kwargs}
        ).stream()

    def mpdecimate(
        self,
        *,
        max: int = None,
        keep: int = None,
        hi: float = None,
        lo: float = None,
        frac: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.170 mpdecimate Drop frames that do not differ greatly from the previous frame in order to reduce frame rate. The main use of this filter is for very-low-bitrate encoding (e.g. streaming over dialup modem), but it could in theory be used for fixing movies that were inverse-telecined incorrectly. A description of the accepted options follows.

        Parameters:
        ----------
        max:
            Set the maximum number of consecutive frames which can be dropped (if positive), or the minimum interval between dropped frames (if negative). If the value is 0, the frame is dropped disregarding the number of previous sequentially dropped frames. Default value is 0.
        keep:
            Set the maximum number of consecutive similar frames to ignore before to start dropping them. If the value is 0, the frame is dropped disregarding the number of previous sequentially similar frames. Default value is 0.
        hi:
            Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.
        lo:
            Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.
        frac:
            Set the dropping threshold values. Values for hi and lo are for 8x8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block. A frame is a candidate for dropping if no 8x8 blocks differ by more than a threshold of hi, and if no more than frac blocks (1 meaning the whole image) differ by more than a threshold of lo. Default value for hi is 64*12, default value for lo is 64*5, and default value for frac is 0.33.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#mpdecimate

        """
        return FilterNode(
            *[self], name="mpdecimate", kwargs={"max": max, "keep": keep, "hi": hi, "lo": lo, "frac": frac, **kwargs}
        ).stream()

    def msad(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.171 msad Obtain the MSAD (Mean Sum of Absolute Differences) between two input videos. This filter takes two input videos. Both input videos must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The obtained per component, average, min and max MSAD is printed through the logging system. The filter stores the calculated MSAD of each frame in frame metadata. This filter also supports the framesync options. In the below example the input file main.mpg being processed is compared with the reference file ref.mpg. ffmpeg -i main.mpg -i ref.mpg -lavfi msad -f null -

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#msad

        """
        return FilterNode(*[self], name="msad", kwargs={**kwargs}).stream()

    def multiply(
        self, *, scale: float = None, offset: float = None, planes: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.172 multiply Multiply first video stream pixels values with second video stream pixels values. The filter accepts the following options:

        Parameters:
        ----------
        scale:
            Set the scale applied to second video stream. By default is 1. Allowed range is from 0 to 9.
        offset:
            Set the offset applied to second video stream. By default is 0.5. Allowed range is from -1 to 1.
        planes:
            Specify planes from input video stream that will be processed. By default all planes are processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#multiply

        """
        return FilterNode(
            *[self], name="multiply", kwargs={"scale": scale, "offset": offset, "planes": planes, **kwargs}
        ).stream()

    def negate(self, *, components: str, negate_alpha: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.173 negate Negate (invert) the input video. It accepts the following option:

        Parameters:
        ----------
        components:
            Set components to negate. Available values for components are: ‘y’ ‘u’ ‘v’ ‘a’ ‘r’ ‘g’ ‘b’
        negate_alpha:
            With value 1, it negates the alpha component, if present. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#negate

        """
        return FilterNode(
            *[self], name="negate", kwargs={"components": components, "negate_alpha": negate_alpha, **kwargs}
        ).stream()

    def nlmeans(
        self, *, s: float = None, p: int = None, pc: int = None, r: int = None, rc: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.174 nlmeans Denoise frames using Non-Local Means algorithm. Each pixel is adjusted by looking for other pixels with similar contexts. This context similarity is defined by comparing their surrounding patches of size pxp. Patches are searched in an area of rxr around the pixel. Note that the research area defines centers for patches, which means some patches will be made of pixels outside that research area. The filter accepts the following options.

        Parameters:
        ----------
        s:
            Set denoising strength. Default is 1.0. Must be in range [1.0, 30.0].
        p:
            Set patch size. Default is 7. Must be odd number in range [0, 99].
        pc:
            Same as p but for chroma planes. The default value is 0 and means automatic.
        r:
            Set research size. Default is 15. Must be odd number in range [0, 99].
        rc:
            Same as r but for chroma planes. The default value is 0 and means automatic.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nlmeans

        """
        return FilterNode(
            *[self], name="nlmeans", kwargs={"s": s, "p": p, "pc": pc, "r": r, "rc": rc, **kwargs}
        ).stream()

    def nnedi(
        self,
        *,
        weights: str,
        deint: str = None,
        field: str,
        planes: str,
        nsize: str,
        nns: str,
        qual: str,
        etype: str,
        pscrn: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.175 nnedi Deinterlace video using neural network edge directed interpolation. This filter accepts the following options:

        Parameters:
        ----------
        weights:
            Mandatory option, without binary file filter can not work. Currently file can be found here: https://github.com/dubhater/vapoursynth-nnedi3/blob/master/src/nnedi3_weights.bin
        deint:
            Set which frames to deinterlace, by default it is all. Can be all or interlaced.
        field:
            Set mode of operation. Can be one of the following: ‘af’ Use frame flags, both fields. ‘a’ Use frame flags, single field. ‘t’ Use top field only. ‘b’ Use bottom field only. ‘tf’ Use both fields, top first. ‘bf’ Use both fields, bottom first.
        planes:
            Set which planes to process, by default filter process all frames.
        nsize:
            Set size of local neighborhood around each pixel, used by the predictor neural network. Can be one of the following: ‘s8x6’ ‘s16x6’ ‘s32x6’ ‘s48x6’ ‘s8x4’ ‘s16x4’ ‘s32x4’
        nns:
            Set the number of neurons in predictor neural network. Can be one of the following: ‘n16’ ‘n32’ ‘n64’ ‘n128’ ‘n256’
        qual:
            Controls the number of different neural network predictions that are blended together to compute the final output value. Can be fast, default or slow.
        etype:
            Set which set of weights to use in the predictor. Can be one of the following: ‘a, abs’ weights trained to minimize absolute error ‘s, mse’ weights trained to minimize squared error
        pscrn:
            Controls whether or not the prescreener neural network is used to decide which pixels should be processed by the predictor neural network and which can be handled by simple cubic interpolation. The prescreener is trained to know whether cubic interpolation will be sufficient for a pixel or whether it should be predicted by the predictor nn. The computational complexity of the prescreener nn is much less than that of the predictor nn. Since most pixels can be handled by cubic interpolation, using the prescreener generally results in much faster processing. The prescreener is pretty accurate, so the difference between using it and not using it is almost always unnoticeable. Can be one of the following: ‘none’ ‘original’ ‘new’ ‘new2’ ‘new3’ Default is new.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#nnedi

        """
        return FilterNode(
            *[self],
            name="nnedi",
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
                **kwargs,
            }
        ).stream()

    def noformat(self, *, pix_fmts: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.176 noformat Force libavfilter not to use any of the specified pixel formats for the input to the next filter. It accepts the following parameters:

        Parameters:
        ----------
        pix_fmts:
            A ’|’-separated list of pixel format names, such as pix_fmts=yuv420p|monow|rgb24".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noformat

        """
        return FilterNode(*[self], name="noformat", kwargs={"pix_fmts": pix_fmts, **kwargs}).stream()

    def noise(
        self,
        *,
        all_seed: int = None,
        c0_seed: int = None,
        c1_seed: int = None,
        c2_seed: int = None,
        c3_seed: int = None,
        all_strength: int = None,
        c0_strength: int = None,
        c1_strength: int = None,
        c2_strength: int = None,
        c3_strength: int = None,
        all_flags: str,
        c0_flags: str,
        c1_flags: str,
        c2_flags: str,
        c3_flags: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.177 noise Add noise on video input frame. The filter accepts the following options:

        Parameters:
        ----------
        all_seed:
            Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        c0_seed:
            Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        c1_seed:
            Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        c2_seed:
            Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        c3_seed:
            Set noise seed for specific pixel component or all pixel components in case of all_seed. Default value is 123457.
        all_strength:
            Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        c0_strength:
            Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        c1_strength:
            Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        c2_strength:
            Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        c3_strength:
            Set noise strength for specific pixel component or all pixel components in case all_strength. Default value is 0. Allowed range is [0, 100].
        all_flags:
            Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        c0_flags:
            Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        c1_flags:
            Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        c2_flags:
            Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)
        c3_flags:
            Set pixel component flags or set flags for all components if all_flags. Available values for component flags are: ‘a’ averaged temporal noise (smoother) ‘p’ mix random noise with a (semi)regular pattern ‘t’ temporal noise (noise pattern changes between frames) ‘u’ uniform noise (gaussian otherwise)



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#noise

        """
        return FilterNode(
            *[self],
            name="noise",
            kwargs={
                "all_seed": all_seed,
                "c0_seed": c0_seed,
                "c1_seed": c1_seed,
                "c2_seed": c2_seed,
                "c3_seed": c3_seed,
                "all_strength": all_strength,
                "c0_strength": c0_strength,
                "c1_strength": c1_strength,
                "c2_strength": c2_strength,
                "c3_strength": c3_strength,
                "all_flags": all_flags,
                "c0_flags": c0_flags,
                "c1_flags": c1_flags,
                "c2_flags": c2_flags,
                "c3_flags": c3_flags,
                **kwargs,
            }
        ).stream()

    def normalize(
        self,
        *,
        blackpt: str,
        whitept: str,
        smoothing: int,
        independence: float,
        strength: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.178 normalize Normalize RGB video (aka histogram stretching, contrast stretching). See: https://en.wikipedia.org/wiki/Normalization_(image_processing) For each channel of each frame, the filter computes the input range and maps it linearly to the user-specified output range. The output range defaults to the full dynamic range from pure black to pure white. Temporal smoothing can be used on the input range to reduce flickering (rapid changes in brightness) caused when small dark or bright objects enter or leave the scene. This is similar to the auto-exposure (automatic gain control) on a video camera, and, like a video camera, it may cause a period of over- or under-exposure of the video. The R,G,B channels can be normalized independently, which may cause some color shifting, or linked together as a single channel, which prevents color shifting. Linked normalization preserves hue. Independent normalization does not, so it can be used to remove some color casts. Independent and linked normalization can be combined in any ratio. The normalize filter accepts the following options:

        Parameters:
        ----------
        blackpt:
            Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        whitept:
            Colors which define the output range. The minimum input value is mapped to the blackpt. The maximum input value is mapped to the whitept. The defaults are black and white respectively. Specifying white for blackpt and black for whitept will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.
        smoothing:
            The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).
        independence:
            Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).
        strength:
            Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#normalize

        """
        return FilterNode(
            *[self],
            name="normalize",
            kwargs={
                "blackpt": blackpt,
                "whitept": whitept,
                "smoothing": smoothing,
                "independence": independence,
                "strength": strength,
                **kwargs,
            }
        ).stream()

    def null(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.179 null Pass the video source unchanged to the output.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#null

        """
        return FilterNode(*[self], name="null", kwargs={**kwargs}).stream()

    def ocr(
        self, *, datapath: str, language: str, whitelist: str, blacklist: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.180 ocr Optical Character Recognition This filter uses Tesseract for optical character recognition. To enable compilation of this filter, you need to configure FFmpeg with --enable-libtesseract. It accepts the following options: The filter exports recognized text as the frame metadata lavfi.ocr.text. The filter exports confidence of recognized words as the frame metadata lavfi.ocr.confidence.

        Parameters:
        ----------
        datapath:
            Set datapath to tesseract data. Default is to use whatever was set at installation.
        language:
            Set language, default is "eng".
        whitelist:
            Set character whitelist.
        blacklist:
            Set character blacklist.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ocr

        """
        return FilterNode(
            *[self],
            name="ocr",
            kwargs={
                "datapath": datapath,
                "language": language,
                "whitelist": whitelist,
                "blacklist": blacklist,
                **kwargs,
            }
        ).stream()

    def ocv(self, *, filter_name: str, filter_params: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.181 ocv Apply a video transform using libopencv. To enable this filter, install the libopencv library and headers and configure FFmpeg with --enable-libopencv. It accepts the following parameters: Refer to the official libopencv documentation for more precise information: http://docs.opencv.org/master/modules/imgproc/doc/filtering.html Several libopencv filters are supported; see the following subsections.

        Parameters:
        ----------
        filter_name:
            The name of the libopencv filter to apply.
        filter_params:
            The parameters to pass to the libopencv filter. If not specified, the default values are assumed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ocv

        """
        return FilterNode(
            *[self], name="ocv", kwargs={"filter_name": filter_name, "filter_params": filter_params, **kwargs}
        ).stream()

    def oscilloscope(
        self,
        *,
        x: float,
        y: float,
        s: float,
        t: float,
        o: float,
        tx: float,
        ty: float,
        tw: float,
        th: float,
        c: str,
        g: bool,
        st: bool,
        sc: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.182 oscilloscope 2D Video Oscilloscope. Useful to measure spatial impulse, step responses, chroma delays, etc. It accepts the following parameters:

        Parameters:
        ----------
        x:
            Set scope center x position.
        y:
            Set scope center y position.
        s:
            Set scope size, relative to frame diagonal.
        t:
            Set scope tilt/rotation.
        o:
            Set trace opacity.
        tx:
            Set trace center x position.
        ty:
            Set trace center y position.
        tw:
            Set trace width, relative to width of frame.
        th:
            Set trace height, relative to height of frame.
        c:
            Set which components to trace. By default it traces first three components.
        g:
            Draw trace grid. By default is enabled.
        st:
            Draw some statistics. By default is enabled.
        sc:
            Draw scope. By default is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#oscilloscope

        """
        return FilterNode(
            *[self],
            name="oscilloscope",
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
                **kwargs,
            }
        ).stream()

    def overlay(
        self,
        *,
        x: str = None,
        y: str = None,
        eof_action: str,
        eval: str = None,
        shortest: str,
        format: str = None,
        repeatlast: str,
        alpha: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.183 overlay Overlay one video on top of another. It takes two inputs and has one output. The first input is the "main" video on which the second input is overlaid. It accepts the following parameters: A description of the accepted options follows. The x, and y expressions can contain the following parameters. This filter also supports the framesync options. Note that the n, t variables are available only when evaluation is done per frame, and will evaluate to NAN when eval is set to ‘init’. Be aware that frames are taken from each input video in timestamp order, hence, if their initial timestamps differ, it is a good idea to pass the two inputs through a setpts=PTS-STARTPTS filter to have them begin in the same zero timestamp, as the example for the movie filter does. You can chain together more overlays but you should test the efficiency of such approach.

        Parameters:
        ----------
        x:
            Set the expression for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions. In case the expression is invalid, it is set to a huge value (meaning that the overlay will not be displayed within the output visible area).
        y:
            Set the expression for the x and y coordinates of the overlaid video on the main video. Default value is "0" for both expressions. In case the expression is invalid, it is set to a huge value (meaning that the overlay will not be displayed within the output visible area).
        eof_action:
            See framesync.
        eval:
            Set when the expressions for x, and y are evaluated. It accepts the following values: ‘init’ only evaluate expressions once during the filter initialization or when a command is processed ‘frame’ evaluate expressions for each incoming frame Default value is ‘frame’.
        shortest:
            See framesync.
        format:
            Set the format for the output video. It accepts the following values: ‘yuv420’ force YUV 4:2:0 8-bit planar output ‘yuv420p10’ force YUV 4:2:0 10-bit planar output ‘yuv422’ force YUV 4:2:2 8-bit planar output ‘yuv422p10’ force YUV 4:2:2 10-bit planar output ‘yuv444’ force YUV 4:4:4 8-bit planar output ‘yuv444p10’ force YUV 4:4:4 10-bit planar output ‘rgb’ force RGB 8-bit packed output ‘gbrp’ force RGB 8-bit planar output ‘auto’ automatically pick format Default value is ‘yuv420’.
        repeatlast:
            See framesync.
        alpha:
            Set format of alpha of the overlaid video, it can be straight or premultiplied. Default is straight.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay

        """
        return FilterNode(
            *[self],
            name="overlay",
            kwargs={
                "x": x,
                "y": y,
                "eof_action": eof_action,
                "eval": eval,
                "shortest": shortest,
                "format": format,
                "repeatlast": repeatlast,
                "alpha": alpha,
                **kwargs,
            }
        ).stream()

    def overlay_cuda(
        self,
        *,
        x: str = None,
        y: str = None,
        eval: str = None,
        eof_action: str,
        shortest: str,
        repeatlast: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.184 overlay_cuda Overlay one video on top of another. This is the CUDA variant of the overlay filter. It only accepts CUDA frames. The underlying input pixel formats have to match. It takes two inputs and has one output. The first input is the "main" video on which the second input is overlaid. It accepts the following parameters: This filter also supports the framesync options.

        Parameters:
        ----------
        x:
            Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
        y:
            Set expressions for the x and y coordinates of the overlaid video on the main video. They can contain the following parameters: main_w, W main_h, H The main input width and height. overlay_w, w overlay_h, h The overlay input width and height. x y The computed values for x and y. They are evaluated for each new frame. n The ordinal index of the main input frame, starting from 0. pos The byte offset position in the file of the main input frame, NAN if unknown. Deprecated, do not use. t The timestamp of the main input frame, expressed in seconds, NAN if unknown. Default value is "0" for both expressions.
        eval:
            Set when the expressions for x and y are evaluated. It accepts the following values: init Evaluate expressions once during filter initialization or when a command is processed. frame Evaluate expressions for each incoming frame Default value is frame.
        eof_action:
            See framesync.
        shortest:
            See framesync.
        repeatlast:
            See framesync.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#overlay_005fcuda

        """
        return FilterNode(
            *[self],
            name="overlay_cuda",
            kwargs={
                "x": x,
                "y": y,
                "eval": eval,
                "eof_action": eof_action,
                "shortest": shortest,
                "repeatlast": repeatlast,
                **kwargs,
            }
        ).stream()

    def owdenoise(
        self, *, depth: int = None, luma_strength: float = None, chroma_strength: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.185 owdenoise Apply Overcomplete Wavelet denoiser. The filter accepts the following options:

        Parameters:
        ----------
        depth:
            Set depth. Larger depth values will denoise lower frequency components more, but slow down filtering. Must be an int in the range 8-16, default is 8.
        luma_strength:
            Set luma strength. Must be a double value in the range 0-1000, default is 1.0.
        chroma_strength:
            Set chroma strength. Must be a double value in the range 0-1000, default is 1.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#owdenoise

        """
        return FilterNode(
            *[self],
            name="owdenoise",
            kwargs={"depth": depth, "luma_strength": luma_strength, "chroma_strength": chroma_strength, **kwargs}
        ).stream()

    def pad(
        self,
        *,
        width: str = None,
        height: str = None,
        x: str = None,
        y: str = None,
        color: str = None,
        eval: str = None,
        aspect: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.186 pad Add paddings to the input image, and place the original input at the provided x, y coordinates. It accepts the following parameters: The value for the width, height, x, and y options are expressions containing the following constants:

        Parameters:
        ----------
        width:
            Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        height:
            Specify an expression for the size of the output image with the paddings added. If the value for width or height is 0, the corresponding input size is used for the output. The width expression can reference the value set by the height expression, and vice versa. The default value of width and height is 0.
        x:
            Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        y:
            Specify the offsets to place the input image at within the padded area, with respect to the top/left border of the output image. The x expression can reference the value set by the y expression, and vice versa. The default value of x and y is 0. If x or y evaluate to a negative number, they’ll be changed so the input image is centered on the padded area.
        color:
            Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".
        eval:
            Specify when to evaluate width, height, x and y expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame. Default value is ‘init’.
        aspect:
            Pad to aspect instead to a resolution.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pad

        """
        return FilterNode(
            *[self],
            name="pad",
            kwargs={
                "width": width,
                "height": height,
                "x": x,
                "y": y,
                "color": color,
                "eval": eval,
                "aspect": aspect,
                **kwargs,
            }
        ).stream()

    def palettegen(
        self,
        *,
        max_colors: int,
        reserve_transparent: bool,
        transparency_color: str,
        stats_mode: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.187 palettegen Generate one palette for a whole video stream. It accepts the following options: The filter also exports the frame metadata lavfi.color_quant_ratio (nb_color_in / nb_color_out) which you can use to evaluate the degree of color quantization of the palette. This information is also visible at info logging level.

        Parameters:
        ----------
        max_colors:
            Set the maximum number of colors to quantize in the palette. Note: the palette will still contain 256 colors; the unused palette entries will be black.
        reserve_transparent:
            Create a palette of 255 colors maximum and reserve the last one for transparency. Reserving the transparency color is useful for GIF optimization. If not set, the maximum of colors in the palette will be 256. You probably want to disable this option for a standalone image. Set by default.
        transparency_color:
            Set the color that will be used as background for transparency.
        stats_mode:
            Set statistics mode. It accepts the following values: ‘full’ Compute full frame histograms. ‘diff’ Compute histograms only for the part that differs from previous frame. This might be relevant to give more importance to the moving part of your input if the background is static. ‘single’ Compute new histogram for each frame. Default value is full.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#palettegen

        """
        return FilterNode(
            *[self],
            name="palettegen",
            kwargs={
                "max_colors": max_colors,
                "reserve_transparent": reserve_transparent,
                "transparency_color": transparency_color,
                "stats_mode": stats_mode,
                **kwargs,
            }
        ).stream()

    def paletteuse(
        self,
        *,
        dither: str = None,
        bayer_scale: int = None,
        diff_mode: str = None,
        new: bool,
        alpha_threshold: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.188 paletteuse Use a palette to downsample an input video stream. The filter takes two inputs: one video stream and a palette. The palette must be a 256 pixels image. It accepts the following options:

        Parameters:
        ----------
        dither:
            Select dithering mode. Available algorithms are: ‘bayer’ Ordered 8x8 bayer dithering (deterministic) ‘heckbert’ Dithering as defined by Paul Heckbert in 1982 (simple error diffusion). Note: this dithering is sometimes considered "wrong" and is included as a reference. ‘floyd_steinberg’ Floyd and Steingberg dithering (error diffusion) ‘sierra2’ Frankie Sierra dithering v2 (error diffusion) ‘sierra2_4a’ Frankie Sierra dithering v2 "Lite" (error diffusion) ‘sierra3’ Frankie Sierra dithering v3 (error diffusion) ‘burkes’ Burkes dithering (error diffusion) ‘atkinson’ Atkinson dithering by Bill Atkinson at Apple Computer (error diffusion) ‘none’ Disable dithering. Default is sierra2_4a.
        bayer_scale:
            When bayer dithering is selected, this option defines the scale of the pattern (how much the crosshatch pattern is visible). A low value means more visible pattern for less banding, and higher value means less visible pattern at the cost of more banding. The option must be an integer value in the range [0,5]. Default is 2.
        diff_mode:
            If set, define the zone to process ‘rectangle’ Only the changing rectangle will be reprocessed. This is similar to GIF cropping/offsetting compression mechanism. This option can be useful for speed if only a part of the image is changing, and has use cases such as limiting the scope of the error diffusal dither to the rectangle that bounds the moving scene (it leads to more deterministic output if the scene doesn’t change much, and as a result less moving noise and better GIF compression). Default is none.
        new:
            Take new palette for each output frame.
        alpha_threshold:
            Sets the alpha threshold for transparency. Alpha values above this threshold will be treated as completely opaque, and values below this threshold will be treated as completely transparent. The option must be an integer value in the range [0,255]. Default is 128.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#paletteuse

        """
        return FilterNode(
            *[self],
            name="paletteuse",
            kwargs={
                "dither": dither,
                "bayer_scale": bayer_scale,
                "diff_mode": diff_mode,
                "new": new,
                "alpha_threshold": alpha_threshold,
                **kwargs,
            }
        ).stream()

    def perspective(
        self,
        *,
        x0: str,
        y0: str,
        x1: str,
        y1: str,
        x2: str,
        y2: str,
        x3: str,
        y3: str,
        interpolation: str,
        sense: str,
        eval: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.189 perspective Correct perspective of video not recorded perpendicular to the screen. A description of the accepted parameters follows.

        Parameters:
        ----------
        x0:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        y0:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        x1:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        y1:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        x2:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        y2:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        x3:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        y3:
            Set coordinates expression for top left, top right, bottom left and bottom right corners. Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged. If the sense option is set to source, then the specified points will be sent to the corners of the destination. If the sense option is set to destination, then the corners of the source will be sent to the specified coordinates. The expressions can use the following variables: W H the width and height of video frame. in Input frame count. on Output frame count.
        interpolation:
            Set interpolation for perspective correction. It accepts the following values: ‘linear’ ‘cubic’ Default value is ‘linear’.
        sense:
            Set interpretation of coordinate options. It accepts the following values: ‘0, source’ Send point in the source specified by the given coordinates to the corners of the destination. ‘1, destination’ Send the corners of the source to the point in the destination specified by the given coordinates. Default value is ‘source’.
        eval:
            Set when the expressions for coordinates x0,y0,...x3,y3 are evaluated. It accepts the following values: ‘init’ only evaluate expressions once during the filter initialization or when a command is processed ‘frame’ evaluate expressions for each incoming frame Default value is ‘init’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#perspective

        """
        return FilterNode(
            *[self],
            name="perspective",
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
                **kwargs,
            }
        ).stream()

    def phase(self, *, mode: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.190 phase Delay interlaced video by one field time so that the field order changes. The intended use is to fix PAL movies that have been captured with the opposite field order to the film-to-video transfer. A description of the accepted parameters follows.

        Parameters:
        ----------
        mode:
            Set phase mode. It accepts the following values: ‘t’ Capture field order top-first, transfer bottom-first. Filter will delay the bottom field. ‘b’ Capture field order bottom-first, transfer top-first. Filter will delay the top field. ‘p’ Capture and transfer with the same field order. This mode only exists for the documentation of the other options to refer to, but if you actually select it, the filter will faithfully do nothing. ‘a’ Capture field order determined automatically by field flags, transfer opposite. Filter selects among ‘t’ and ‘b’ modes on a frame by frame basis using field flags. If no field information is available, then this works just like ‘u’. ‘u’ Capture unknown or varying, transfer opposite. Filter selects among ‘t’ and ‘b’ on a frame by frame basis by analyzing the images and selecting the alternative that produces best match between the fields. ‘T’ Capture top-first, transfer unknown or varying. Filter selects among ‘t’ and ‘p’ using image analysis. ‘B’ Capture bottom-first, transfer unknown or varying. Filter selects among ‘b’ and ‘p’ using image analysis. ‘A’ Capture determined by field flags, transfer unknown or varying. Filter selects among ‘t’, ‘b’ and ‘p’ using field flags and image analysis. If no field information is available, then this works just like ‘U’. This is the default mode. ‘U’ Both capture and transfer unknown or varying. Filter selects among ‘t’, ‘b’ and ‘p’ using image analysis only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#phase

        """
        return FilterNode(*[self], name="phase", kwargs={"mode": mode, **kwargs}).stream()

    def photosensitivity(
        self,
        *,
        frames: int = None,
        threshold: float = None,
        skip: int = None,
        bypass: bool = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.191 photosensitivity Reduce various flashes in video, so to help users with epilepsy. It accepts the following options:

        Parameters:
        ----------
        frames:
            Set how many frames to use when filtering. Default is 30.
        threshold:
            Set detection threshold factor. Default is 1. Lower is stricter.
        skip:
            Set how many pixels to skip when sampling frames. Default is 1. Allowed range is from 1 to 1024.
        bypass:
            Leave frames unchanged. Default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#photosensitivity

        """
        return FilterNode(
            *[self],
            name="photosensitivity",
            kwargs={"frames": frames, "threshold": threshold, "skip": skip, "bypass": bypass, **kwargs}
        ).stream()

    def pixdesctest(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.192 pixdesctest Pixel format descriptor test filter, mainly useful for internal testing. The output video should be equal to the input video. For example: format=monow, pixdesctest can be used to test the monowhite pixel format descriptor definition.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixdesctest

        """
        return FilterNode(*[self], name="pixdesctest", kwargs={**kwargs}).stream()

    def pixelize(
        self, *, width: int = None, height: int = None, mode: str = None, planes: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.193 pixelize Apply pixelization to video stream. The filter accepts the following options:

        Parameters:
        ----------
        width:
            Set block dimensions that will be used for pixelization. Default value is 16.
        height:
            Set block dimensions that will be used for pixelization. Default value is 16.
        mode:
            Set the mode of pixelization used. Possible values are: ‘avg’ ‘min’ ‘max’ Default value is avg.
        planes:
            Set what planes to filter. Default is to filter all planes.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixelize

        """
        return FilterNode(
            *[self],
            name="pixelize",
            kwargs={"width": width, "height": height, "mode": mode, "planes": planes, **kwargs}
        ).stream()

    def pixscope(
        self, *, x: float, y: float, w: float, h: float, o: float, wx: float, wy: float, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.194 pixscope Display sample values of color channels. Mainly useful for checking color and levels. Minimum supported resolution is 640x480. The filters accept the following options:

        Parameters:
        ----------
        x:
            Set scope X position, relative offset on X axis.
        y:
            Set scope Y position, relative offset on Y axis.
        w:
            Set scope width.
        h:
            Set scope height.
        o:
            Set window opacity. This window also holds statistics about pixel area.
        wx:
            Set window X position, relative offset on X axis.
        wy:
            Set window Y position, relative offset on Y axis.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pixscope

        """
        return FilterNode(
            *[self], name="pixscope", kwargs={"x": x, "y": y, "w": w, "h": h, "o": o, "wx": wx, "wy": wy, **kwargs}
        ).stream()

    def pp(self, *, subfilters: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.195 pp Enable the specified chain of postprocessing subfilters using libpostproc. This library should be automatically selected with a GPL build (--enable-gpl). Subfilters must be separated by ’/’ and can be disabled by prepending a ’-’. Each subfilter and some options have a short and a long name that can be used interchangeably, i.e. dr/dering are the same. The filters accept the following options: All subfilters share common options to determine their scope: These options can be appended after the subfilter name, separated by a ’|’. Available subfilters are: The horizontal and vertical deblocking filters share the difference and flatness values so you cannot set different horizontal and vertical thresholds.

        Parameters:
        ----------
        subfilters:
            Set postprocessing subfilters string.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp

        """
        return FilterNode(*[self], name="pp", kwargs={"subfilters": subfilters, **kwargs}).stream()

    def pp7(self, *, qp: int, mode: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.196 pp7 Apply Postprocessing filter 7. It is variant of the spp filter, similar to spp = 6 with 7 point DCT, where only the center sample is used after IDCT. The filter accepts the following options:

        Parameters:
        ----------
        qp:
            Force a constant quantization parameter. It accepts an integer in range 0 to 63. If not set, the filter will use the QP from the video stream (if available).
        mode:
            Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding. ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier). ‘medium’ Set medium thresholding (good results, default).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pp7

        """
        return FilterNode(*[self], name="pp7", kwargs={"qp": qp, "mode": mode, **kwargs}).stream()

    def premultiply(self, *, planes: int, inplace: bool, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.197 premultiply Apply alpha premultiply effect to input video stream using first plane of second stream as alpha. Both streams must have same dimensions and same pixel format. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        inplace:
            Do not require 2nd input for processing, instead use alpha plane from input stream.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#premultiply

        """
        return FilterNode(*[self], name="premultiply", kwargs={"planes": planes, "inplace": inplace, **kwargs}).stream()

    def prewitt(self, *, planes: int, scale: float, delta: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.198 prewitt Apply prewitt operator to input video stream. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        scale:
            Set value which will be multiplied with filtered result.
        delta:
            Set value which will be added to filtered result.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#prewitt

        """
        return FilterNode(
            *[self], name="prewitt", kwargs={"planes": planes, "scale": scale, "delta": delta, **kwargs}
        ).stream()

    def pseudocolor(
        self, *, c0: str, c1: str, c2: str, c3: str, index: str, preset: str, opacity: float, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.199 pseudocolor Alter frame colors in video with pseudocolors. This filter accepts the following options: Each of the expression options specifies the expression to use for computing the lookup table for the corresponding pixel component values. The expressions can contain the following constants and functions: All expressions default to "val".

        Parameters:
        ----------
        c0:
            set pixel first component expression
        c1:
            set pixel second component expression
        c2:
            set pixel third component expression
        c3:
            set pixel fourth component expression, corresponds to the alpha component
        index:
            set component to use as base for altering colors
        preset:
            Pick one of built-in LUTs. By default is set to none. Available LUTs: ‘magma’ ‘inferno’ ‘plasma’ ‘viridis’ ‘turbo’ ‘cividis’ ‘range1’ ‘range2’ ‘shadows’ ‘highlights’ ‘solar’ ‘nominal’ ‘preferred’ ‘total’ ‘spectral’ ‘cool’ ‘heat’ ‘fiery’ ‘blues’ ‘green’ ‘helix’
        opacity:
            Set opacity of output colors. Allowed range is from 0 to 1. Default value is set to 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pseudocolor

        """
        return FilterNode(
            *[self],
            name="pseudocolor",
            kwargs={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "index": index,
                "preset": preset,
                "opacity": opacity,
                **kwargs,
            }
        ).stream()

    def psnr(self, *, stats_file: str, stats_version: int, stats_add_max: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.200 psnr Obtain the average, maximum and minimum PSNR (Peak Signal to Noise Ratio) between two input videos. This filter takes in input two input videos, the first input is considered the "main" source and is passed unchanged to the output. The second input is used as a "reference" video for computing the PSNR. Both video inputs must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The obtained average PSNR is printed through the logging system. The filter stores the accumulated MSE (mean squared error) of each frame, and at the end of the processing it is averaged across all frames equally, and the following formula is applied to obtain the PSNR: PSNR = 10*log10(MAX^2/MSE) Where MAX is the average of the maximum values of each component of the image. The description of the accepted parameters follows. This filter also supports the framesync options. The file printed if stats_file is selected, contains a sequence of key/value pairs of the form key:value for each compared couple of frames. If a stats_version greater than 1 is specified, a header line precedes the list of per-frame-pair stats, with key value pairs following the frame format with the following parameters: A description of each shown per-frame-pair parameter follows:

        Parameters:
        ----------
        stats_file:
            If specified the filter will use the named file to save the PSNR of each individual frame. When filename equals "-" the data is sent to standard output.
        stats_version:
            Specifies which version of the stats file format to use. Details of each format are written below. Default value is 1.
        stats_add_max:
            Determines whether the max value is output to the stats log. Default value is 0. Requires stats_version >= 2. If this is set and stats_version < 2, the filter will return an error.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#psnr

        """
        return FilterNode(
            *[self],
            name="psnr",
            kwargs={"stats_file": stats_file, "stats_version": stats_version, "stats_add_max": stats_add_max, **kwargs}
        ).stream()

    def pullup(
        self,
        *,
        jl: int = None,
        jr: int = None,
        jt: int = None,
        jb: int = None,
        sb: int = None,
        mp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.201 pullup Pulldown reversal (inverse telecine) filter, capable of handling mixed hard-telecine, 24000/1001 fps progressive, and 30000/1001 fps progressive content. The pullup filter is designed to take advantage of future context in making its decisions. This filter is stateless in the sense that it does not lock onto a pattern to follow, but it instead looks forward to the following fields in order to identify matches and rebuild progressive frames. To produce content with an even framerate, insert the fps filter after pullup, use fps=24000/1001 if the input frame rate is 29.97fps, fps=24 for 30fps and the (rare) telecined 25fps input. The filter accepts the following options: For best results (without duplicated frames in the output file) it is necessary to change the output frame rate. For example, to inverse telecine NTSC input: ffmpeg -i input -vf pullup -r 24000/1001 ...

        Parameters:
        ----------
        jl:
            These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        jr:
            These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        jt:
            These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        jb:
            These options set the amount of "junk" to ignore at the left, right, top, and bottom of the image, respectively. Left and right are in units of 8 pixels, while top and bottom are in units of 2 lines. The default is 8 pixels on each side.
        sb:
            Set the strict breaks. Setting this option to 1 will reduce the chances of filter generating an occasional mismatched frame, but it may also cause an excessive number of frames to be dropped during high motion sequences. Conversely, setting it to -1 will make filter match fields more easily. This may help processing of video where there is slight blurring between the fields, but may also cause there to be interlaced frames in the output. Default value is 0.
        mp:
            Set the metric plane to use. It accepts the following values: ‘l’ Use luma plane. ‘u’ Use chroma blue plane. ‘v’ Use chroma red plane. This option may be set to use chroma plane instead of the default luma plane for doing filter’s computations. This may improve accuracy on very clean source material, but more likely will decrease accuracy, especially if there is chroma noise (rainbow effect) or any grayscale video. The main purpose of setting mp to a chroma plane is to reduce CPU load and make pullup usable in realtime on slow machines.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#pullup

        """
        return FilterNode(
            *[self], name="pullup", kwargs={"jl": jl, "jr": jr, "jt": jt, "jb": jb, "sb": sb, "mp": mp, **kwargs}
        ).stream()

    def qp(self, *, qp: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.202 qp Change video quantization parameters (QP). The filter accepts the following option: The expression is evaluated through the eval API and can contain, among others, the following constants:

        Parameters:
        ----------
        qp:
            Set expression for quantization parameter.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#qp

        """
        return FilterNode(*[self], name="qp", kwargs={"qp": qp, **kwargs}).stream()

    def random(self, *, frames: int = None, seed: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.203 random Flush video frames from internal cache of frames into a random order. No frame is discarded. Inspired by frei0r nervous filter.

        Parameters:
        ----------
        frames:
            Set size in number of frames of internal cache, in range from 2 to 512. Default is 30.
        seed:
            Set seed for random number generator, must be an integer included between 0 and UINT32_MAX. If not specified, or if explicitly set to less than 0, the filter will try to use a good random seed on a best effort basis.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#random

        """
        return FilterNode(*[self], name="random", kwargs={"frames": frames, "seed": seed, **kwargs}).stream()

    def readvitc(
        self, *, scan_max: int = None, thr_b: float = None, thr_w: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.205 readvitc Read vertical interval timecode (VITC) information from the top lines of a video frame. The filter adds frame metadata key lavfi.readvitc.tc_str with the timecode value, if a valid timecode has been detected. Further metadata key lavfi.readvitc.found is set to 0/1 depending on whether timecode data has been found or not. This filter accepts the following options:

        Parameters:
        ----------
        scan_max:
            Set the maximum number of lines to scan for VITC data. If the value is set to -1 the full video frame is scanned. Default is 45.
        thr_b:
            Set the luma threshold for black. Accepts float numbers in the range [0.0,1.0], default value is 0.2. The value must be equal or less than thr_w.
        thr_w:
            Set the luma threshold for white. Accepts float numbers in the range [0.0,1.0], default value is 0.6. The value must be equal or greater than thr_b.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#readvitc

        """
        return FilterNode(
            *[self], name="readvitc", kwargs={"scan_max": scan_max, "thr_b": thr_b, "thr_w": thr_w, **kwargs}
        ).stream()

    def remap(self, *, format: str = None, fill: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.206 remap Remap pixels using 2nd: Xmap and 3rd: Ymap input video stream. Destination pixel at position (X, Y) will be picked from source (x, y) position where x = Xmap(X, Y) and y = Ymap(X, Y). If mapping values are out of range, zero value for pixel will be used for destination pixel. Xmap and Ymap input video streams must be of same dimensions. Output video stream will have Xmap/Ymap video stream dimensions. Xmap and Ymap input video streams are 16bit depth, single channel.

        Parameters:
        ----------
        format:
            Specify pixel format of output from this filter. Can be color or gray. Default is color.
        fill:
            Specify the color of the unmapped pixels. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. Default color is black.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#remap

        """
        return FilterNode(*[self], name="remap", kwargs={"format": format, "fill": fill, **kwargs}).stream()

    def removegrain(
        self, *, m0: int = None, m1: int = None, m2: int = None, m3: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.207 removegrain The removegrain filter is a spatial denoiser for progressive video. Range of mode is from 0 to 24. Description of each mode follows:

        Parameters:
        ----------
        m0:
            Set mode for the first plane.
        m1:
            Set mode for the second plane.
        m2:
            Set mode for the third plane.
        m3:
            Set mode for the fourth plane.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removegrain

        """
        return FilterNode(
            *[self], name="removegrain", kwargs={"m0": m0, "m1": m1, "m2": m2, "m3": m3, **kwargs}
        ).stream()

    def removelogo(self, *, filename: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.208 removelogo Suppress a TV station logo, using an image file to determine which pixels comprise the logo. It works by filling in the pixels that comprise the logo with neighboring pixels. The filter accepts the following options: Pixels in the provided bitmap image with a value of zero are not considered part of the logo, non-zero pixels are considered part of the logo. If you use white (255) for the logo and black (0) for the rest, you will be safe. For making the filter bitmap, it is recommended to take a screen capture of a black frame with the logo visible, and then using a threshold filter followed by the erode filter once or twice. If needed, little splotches can be fixed manually. Remember that if logo pixels are not covered, the filter quality will be much reduced. Marking too many pixels as part of the logo does not hurt as much, but it will increase the amount of blurring needed to cover over the image and will destroy more information than necessary, and extra pixels will slow things down on a large logo.

        Parameters:
        ----------
        filename:
            Set the filter bitmap file, which can be any image format supported by libavformat. The width and height of the image file must match those of the video stream being processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#removelogo

        """
        return FilterNode(*[self], name="removelogo", kwargs={"filename": filename, **kwargs}).stream()

    def repeatfields(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.209 repeatfields This filter uses the repeat_field flag from the Video ES headers and hard repeats fields based on its value.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#repeatfields

        """
        return FilterNode(*[self], name="repeatfields", kwargs={**kwargs}).stream()

    def replaygain(self, *, track_gain: float, track_peak: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.102 replaygain ReplayGain scanner filter. This filter takes an audio stream as an input and outputs it unchanged. At end of filtering it displays track_gain and track_peak. The filter accepts the following exported read-only options:

        Parameters:
        ----------
        track_gain:
            Exported track gain in dB at end of stream.
        track_peak:
            Exported track peak at end of stream.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#replaygain

        """
        return FilterNode(
            *[self], name="replaygain", kwargs={"track_gain": track_gain, "track_peak": track_peak, **kwargs}
        ).stream()

    def resample(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.103 resample Convert the audio sample format, sample rate and channel layout. It is not meant to be used directly.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#resample

        """
        return FilterNode(*[self], name="resample", kwargs={**kwargs}).stream()

    def reverse(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.210 reverse Reverse a video clip. Warning: This filter requires memory to buffer the entire clip, so trimming is suggested.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#reverse

        """
        return FilterNode(*[self], name="reverse", kwargs={**kwargs}).stream()

    def rgbashift(
        self,
        *,
        rh: float,
        rv: float,
        gh: float,
        gv: float,
        bh: float,
        bv: float,
        ah: float,
        av: float,
        edge: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.211 rgbashift Shift R/G/B/A pixels horizontally and/or vertically. The filter accepts the following options:

        Parameters:
        ----------
        rh:
            Set amount to shift red horizontally.
        rv:
            Set amount to shift red vertically.
        gh:
            Set amount to shift green horizontally.
        gv:
            Set amount to shift green vertically.
        bh:
            Set amount to shift blue horizontally.
        bv:
            Set amount to shift blue vertically.
        ah:
            Set amount to shift alpha horizontally.
        av:
            Set amount to shift alpha vertically.
        edge:
            Set edge mode, can be smear, default, or warp.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rgbashift

        """
        return FilterNode(
            *[self],
            name="rgbashift",
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
                **kwargs,
            }
        ).stream()

    def roberts(self, *, planes: int, scale: float, delta: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.212 roberts Apply roberts cross operator to input video stream. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        scale:
            Set value which will be multiplied with filtered result.
        delta:
            Set value which will be added to filtered result.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#roberts

        """
        return FilterNode(
            *[self], name="roberts", kwargs={"planes": planes, "scale": scale, "delta": delta, **kwargs}
        ).stream()

    def rotate(
        self, *, angle: str, out_w: str, out_h: str, bilinear: int, fillcolor: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.213 rotate Rotate video by an arbitrary angle expressed in radians. The filter accepts the following options: A description of the optional parameters follows. The expressions for the angle and the output size can contain the following constants and functions:

        Parameters:
        ----------
        angle:
            Set an expression for the angle by which to rotate the input video clockwise, expressed as a number of radians. A negative value will result in a counter-clockwise rotation. By default it is set to "0". This expression is evaluated for each frame.
        out_w:
            Set the output width expression, default value is "iw". This expression is evaluated just once during configuration.
        out_h:
            Set the output height expression, default value is "ih". This expression is evaluated just once during configuration.
        bilinear:
            Enable bilinear interpolation if set to 1, a value of 0 disables it. Default value is 1.
        fillcolor:
            Set the color used to fill the output area not covered by the rotated image. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rotate

        """
        return FilterNode(
            *[self],
            name="rotate",
            kwargs={
                "angle": angle,
                "out_w": out_w,
                "out_h": out_h,
                "bilinear": bilinear,
                "fillcolor": fillcolor,
                **kwargs,
            }
        ).stream()

    def rubberband(
        self,
        *,
        tempo: float,
        pitch: float,
        transients: str,
        detector: str,
        phase: str,
        window: str,
        smoothing: str,
        formant: str,
        pitchq: str,
        channels: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.104 rubberband Apply time-stretching and pitch-shifting with librubberband. To enable compilation of this filter, you need to configure FFmpeg with --enable-librubberband. The filter accepts the following options:

        Parameters:
        ----------
        tempo:
            Set tempo scale factor.
        pitch:
            Set pitch scale factor.
        transients:
            Set transients detector. Possible values are: crisp mixed smooth
        detector:
            Set detector. Possible values are: compound percussive soft
        phase:
            Set phase. Possible values are: laminar independent
        window:
            Set processing window size. Possible values are: standard short long
        smoothing:
            Set smoothing. Possible values are: off on
        formant:
            Enable formant preservation when shift pitching. Possible values are: shifted preserved
        pitchq:
            Set pitch quality. Possible values are: quality speed consistency
        channels:
            Set channels. Possible values are: apart together



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#rubberband

        """
        return FilterNode(
            *[self],
            name="rubberband",
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
                **kwargs,
            }
        ).stream()

    def sab(
        self,
        *,
        luma_radius: float = None,
        luma_pre_filter_radius: float = None,
        luma_strength: float = None,
        chroma_radius: float,
        chroma_pre_filter_radius: float,
        chroma_strength: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.214 sab Apply Shape Adaptive Blur. The filter accepts the following options: Each chroma option value, if not explicitly specified, is set to the corresponding luma option value.

        Parameters:
        ----------
        luma_radius:
            Set luma blur filter strength, must be a value in range 0.1-4.0, default value is 1.0. A greater value will result in a more blurred image, and in slower processing.
        luma_pre_filter_radius:
            Set luma pre-filter radius, must be a value in the 0.1-2.0 range, default value is 1.0.
        luma_strength:
            Set luma maximum difference between pixels to still be considered, must be a value in the 0.1-100.0 range, default value is 1.0.
        chroma_radius:
            Set chroma blur filter strength, must be a value in range -0.9-4.0. A greater value will result in a more blurred image, and in slower processing.
        chroma_pre_filter_radius:
            Set chroma pre-filter radius, must be a value in the -0.9-2.0 range.
        chroma_strength:
            Set chroma maximum difference between pixels to still be considered, must be a value in the -0.9-100.0 range.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sab

        """
        return FilterNode(
            *[self],
            name="sab",
            kwargs={
                "luma_radius": luma_radius,
                "luma_pre_filter_radius": luma_pre_filter_radius,
                "luma_strength": luma_strength,
                "chroma_radius": chroma_radius,
                "chroma_pre_filter_radius": chroma_pre_filter_radius,
                "chroma_strength": chroma_strength,
                **kwargs,
            }
        ).stream()

    def scale(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.215 scale Scale (resize) the input video, using the libswscale library. The scale filter forces the output display aspect ratio to be the same of the input, by changing the output sample aspect ratio. If the input image format is different from the format requested by the next filter, the scale filter will convert the input to the requested format.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale

        """
        return FilterNode(*[self], name="scale", kwargs={**kwargs}).stream()

    def scale2ref(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.218 scale2ref Scale (resize) the input video, based on a reference video. See the scale filter for available options, scale2ref supports the same but uses the reference video instead of the main input as basis. scale2ref also supports the following additional constants for the w and h options:

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref

        """
        return FilterNode(*[self], name="scale2ref", kwargs={**kwargs}).stream()

    def scale2ref_npp(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.219 scale2ref_npp Use the NVIDIA Performance Primitives (libnpp) to scale (resize) the input video, based on a reference video. See the scale_npp filter for available options, scale2ref_npp supports the same but uses the reference video instead of the main input as basis. scale2ref_npp also supports the following additional constants for the w and h options:

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale2ref_005fnpp

        """
        return FilterNode(*[self], name="scale2ref_npp", kwargs={**kwargs}).stream()

    def scale_cuda(
        self,
        *,
        w: str,
        h: str,
        interp_algo: str,
        format: str,
        passthrough: int,
        param: str,
        force_original_aspect_ratio: bool,
        force_divisible_by: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.216 scale_cuda Scale (resize) and convert (pixel format) the input video, using accelerated CUDA kernels. Setting the output width and height works in the same way as for the scale filter. The filter accepts the following options:

        Parameters:
        ----------
        w:
            Set the output video dimension expression. Default value is the input dimension. Allows for the same expressions as the scale filter.
        h:
            Set the output video dimension expression. Default value is the input dimension. Allows for the same expressions as the scale filter.
        interp_algo:
            Sets the algorithm used for scaling: nearest Nearest neighbour Used by default if input parameters match the desired output. bilinear Bilinear bicubic Bicubic This is the default. lanczos Lanczos
        format:
            Controls the output pixel format. By default, or if none is specified, the input pixel format is used. The filter does not support converting between YUV and RGB pixel formats.
        passthrough:
            If set to 0, every frame is processed, even if no conversion is necessary. This mode can be useful to use the filter as a buffer for a downstream frame-consumer that exhausts the limited decoder frame pool. If set to 1, frames are passed through as-is if they match the desired output parameters. This is the default behaviour.
        param:
            Algorithm-Specific parameter. Affects the curves of the bicubic algorithm.
        force_original_aspect_ratio:
            Work the same as the identical scale filter options.
        force_divisible_by:
            Work the same as the identical scale filter options.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fcuda

        """
        return FilterNode(
            *[self],
            name="scale_cuda",
            kwargs={
                "w": w,
                "h": h,
                "interp_algo": interp_algo,
                "format": format,
                "passthrough": passthrough,
                "param": param,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                **kwargs,
            }
        ).stream()

    def scale_npp(
        self,
        *,
        format: str,
        interp_algo: str,
        force_original_aspect_ratio: str,
        force_divisible_by: int,
        eval: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.217 scale_npp Use the NVIDIA Performance Primitives (libnpp) to perform scaling and/or pixel format conversion on CUDA video frames. Setting the output width and height works in the same way as for the scale filter. The following additional options are accepted: The values of the w and h options are expressions containing the following constants:

        Parameters:
        ----------
        format:
            The pixel format of the output CUDA frames. If set to the string "same" (the default), the input format will be kept. Note that automatic format negotiation and conversion is not yet supported for hardware frames
        interp_algo:
            The interpolation algorithm used for resizing. One of the following: nn Nearest neighbour. linear cubic cubic2p_bspline 2-parameter cubic (B=1, C=0) cubic2p_catmullrom 2-parameter cubic (B=0, C=1/2) cubic2p_b05c03 2-parameter cubic (B=1/2, C=3/10) super Supersampling lanczos
        force_original_aspect_ratio:
            Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio. Possible values: ‘disable’ Scale the video as specified and disable this feature. ‘decrease’ The output video dimensions will automatically be decreased if needed. ‘increase’ The output video dimensions will automatically be increased if needed. One useful instance of this option is that when you know a specific device’s maximum allowed resolution, you can use this to limit the output video to that, while retaining the aspect ratio. For example, device A allows 1280x720 playback, and your video is 1920x800. Using this option (set it to decrease) and specifying 1280x720 to the command line makes the output 1280x533. Please note that this is a different thing than specifying -1 for w or h, you still need to specify the output resolution for this option to work.
        force_divisible_by:
            Ensures that both the output dimensions, width and height, are divisible by the given integer when used together with force_original_aspect_ratio. This works similar to using -n in the w and h options. This option respects the value set for force_original_aspect_ratio, increasing or decreasing the resolution accordingly. The video’s aspect ratio may be slightly modified. This option can be handy if you need to have a video fit within or exceed a defined resolution using force_original_aspect_ratio but also have encoder restrictions on width or height divisibility.
        eval:
            Specify when to evaluate width and height expression. It accepts the following values: ‘init’ Only evaluate expressions once during the filter initialization or when a command is processed. ‘frame’ Evaluate expressions for each incoming frame.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fnpp

        """
        return FilterNode(
            *[self],
            name="scale_npp",
            kwargs={
                "format": format,
                "interp_algo": interp_algo,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                "eval": eval,
                **kwargs,
            }
        ).stream()

    def scale_vt(
        self, *, w: str, h: str, color_matrix: str, color_primaries: str, color_transfer: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.220 scale_vt Scale and convert the color parameters using VTPixelTransferSession. The filter accepts the following options:

        Parameters:
        ----------
        w:
            Set the output video dimension expression. Default value is the input dimension.
        h:
            Set the output video dimension expression. Default value is the input dimension.
        color_matrix:
            Set the output colorspace matrix.
        color_primaries:
            Set the output color primaries.
        color_transfer:
            Set the output transfer characteristics.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scale_005fvt

        """
        return FilterNode(
            *[self],
            name="scale_vt",
            kwargs={
                "w": w,
                "h": h,
                "color_matrix": color_matrix,
                "color_primaries": color_primaries,
                "color_transfer": color_transfer,
                **kwargs,
            }
        ).stream()

    def scdet(self, *, threshold: float = None, sc_pass: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.223 scdet Detect video scene change. This filter sets frame metadata with mafd between frame, the scene score, and forward the frame to the next filter, so they can use these metadata to detect scene change or others. In addition, this filter logs a message and sets frame metadata when it detects a scene change by threshold. lavfi.scd.mafd metadata keys are set with mafd for every frame. lavfi.scd.score metadata keys are set with scene change score for every frame to detect scene change. lavfi.scd.time metadata keys are set with current filtered frame time which detect scene change with threshold. The filter accepts the following options:

        Parameters:
        ----------
        threshold:
            Set the scene change detection threshold as a percentage of maximum change. Good values are in the [8.0, 14.0] range. The range for threshold is [0., 100.]. Default value is 10..
        sc_pass:
            Set the flag to pass scene change frames to the next filter. Default value is 0 You can enable it if you want to get snapshot of scene change frames only.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scdet

        """
        return FilterNode(*[self], name="scdet", kwargs={"threshold": threshold, "sc_pass": sc_pass, **kwargs}).stream()

    def scharr(self, *, planes: int, scale: float, delta: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.221 scharr Apply scharr operator to input video stream. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        scale:
            Set value which will be multiplied with filtered result.
        delta:
            Set value which will be added to filtered result.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scharr

        """
        return FilterNode(
            *[self], name="scharr", kwargs={"planes": planes, "scale": scale, "delta": delta, **kwargs}
        ).stream()

    def scroll(
        self,
        *,
        horizontal: float = None,
        vertical: float = None,
        hpos: float = None,
        vpos: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.222 scroll Scroll input video horizontally and/or vertically by constant speed. The filter accepts the following options:

        Parameters:
        ----------
        horizontal:
            Set the horizontal scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        vertical:
            Set the vertical scrolling speed. Default is 0. Allowed range is from -1 to 1. Negative values changes scrolling direction.
        hpos:
            Set the initial horizontal scrolling position. Default is 0. Allowed range is from 0 to 1.
        vpos:
            Set the initial vertical scrolling position. Default is 0. Allowed range is from 0 to 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#scroll

        """
        return FilterNode(
            *[self],
            name="scroll",
            kwargs={"horizontal": horizontal, "vertical": vertical, "hpos": hpos, "vpos": vpos, **kwargs}
        ).stream()

    def selectivecolor(
        self,
        *,
        correction_method: str = None,
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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.224 selectivecolor Adjust cyan, magenta, yellow and black (CMYK) to certain ranges of colors (such as "reds", "yellows", "greens", "cyans", ...). The adjustment range is defined by the "purity" of the color (that is, how saturated it already is). This filter is similar to the Adobe Photoshop Selective Color tool. The filter accepts the following options: All the adjustment settings (reds, yellows, ...) accept up to 4 space separated floating point adjustment values in the [-1,1] range, respectively to adjust the amount of cyan, magenta, yellow and black for the pixels of its range.

        Parameters:
        ----------
        correction_method:
            Select color correction method. Available values are: ‘absolute’ Specified adjustments are applied "as-is" (added/subtracted to original pixel component value). ‘relative’ Specified adjustments are relative to the original component value. Default is absolute.
        reds:
            Adjustments for red pixels (pixels where the red component is the maximum)
        yellows:
            Adjustments for yellow pixels (pixels where the blue component is the minimum)
        greens:
            Adjustments for green pixels (pixels where the green component is the maximum)
        cyans:
            Adjustments for cyan pixels (pixels where the red component is the minimum)
        blues:
            Adjustments for blue pixels (pixels where the blue component is the maximum)
        magentas:
            Adjustments for magenta pixels (pixels where the green component is the minimum)
        whites:
            Adjustments for white pixels (pixels where all components are greater than 128)
        neutrals:
            Adjustments for all pixels except pure black and pure white
        blacks:
            Adjustments for black pixels (pixels where all components are lesser than 128)
        psfile:
            Specify a Photoshop selective color file (.asv) to import the settings from.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#selectivecolor

        """
        return FilterNode(
            *[self],
            name="selectivecolor",
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
                **kwargs,
            }
        ).stream()

    def separatefields(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.225 separatefields The separatefields takes a frame-based video input and splits each frame into its components fields, producing a new half height clip with twice the frame rate and twice the frame count. This filter use field-dominance information in frame to decide which of each pair of fields to place first in the output. If it gets it wrong use setfield filter before separatefields filter.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#separatefields

        """
        return FilterNode(*[self], name="separatefields", kwargs={**kwargs}).stream()

    def setdar(self, *, r: str, max: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.226 setdar, setsar The setdar filter sets the Display Aspect Ratio for the filter output video. This is done by changing the specified Sample (aka Pixel) Aspect Ratio, according to the following equation: DAR = HORIZONTAL_RESOLUTION / VERTICAL_RESOLUTION * SAR Keep in mind that the setdar filter does not modify the pixel dimensions of the video frame. Also, the display aspect ratio set by this filter may be changed by later filters in the filterchain, e.g. in case of scaling or if another "setdar" or a "setsar" filter is applied. The setsar filter sets the Sample (aka Pixel) Aspect Ratio for the filter output video. Note that as a consequence of the application of this filter, the output display aspect ratio will change according to the equation above. Keep in mind that the sample aspect ratio set by the setsar filter may be changed by later filters in the filterchain, e.g. if another "setsar" or a "setdar" filter is applied. It accepts the following parameters: The parameter sar is an expression containing the following constants:

        Parameters:
        ----------
        r:
            Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        max:
            Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        return FilterNode(*[self], name="setdar", kwargs={"r": r, "max": max, **kwargs}).stream()

    def setfield(self, *, mode: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.227 setfield Force field for the output video frame. The setfield filter marks the interlace type field for the output frames. It does not change the input frame, but only sets the corresponding property, which affects how the frame is treated by following filters (e.g. fieldorder or yadif). The filter accepts the following options:

        Parameters:
        ----------
        mode:
            Available values are: ‘auto’ Keep the same field property. ‘bff’ Mark the frame as bottom-field-first. ‘tff’ Mark the frame as top-field-first. ‘prog’ Mark the frame as progressive.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setfield

        """
        return FilterNode(*[self], name="setfield", kwargs={"mode": mode, **kwargs}).stream()

    def setparams(
        self,
        *,
        field_mode: str = None,
        range: str = None,
        color_primaries: str = None,
        color_trc: str = None,
        colorspace: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.228 setparams Force frame parameter for the output video frame. The setparams filter marks interlace and color range for the output frames. It does not change the input frame, but only sets the corresponding property, which affects how the frame is treated by filters/encoders.

        Parameters:
        ----------
        field_mode:
            Available values are: ‘auto’ Keep the same field property (default). ‘bff’ Mark the frame as bottom-field-first. ‘tff’ Mark the frame as top-field-first. ‘prog’ Mark the frame as progressive.
        range:
            Available values are: ‘auto’ Keep the same color range property (default). ‘unspecified, unknown’ Mark the frame as unspecified color range. ‘limited, tv, mpeg’ Mark the frame as limited range. ‘full, pc, jpeg’ Mark the frame as full range.
        color_primaries:
            Set the color primaries. Available values are: ‘auto’ Keep the same color primaries property (default). ‘bt709’ ‘unknown’ ‘bt470m’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘film’ ‘bt2020’ ‘smpte428’ ‘smpte431’ ‘smpte432’ ‘jedec-p22’
        color_trc:
            Set the color transfer. Available values are: ‘auto’ Keep the same color trc property (default). ‘bt709’ ‘unknown’ ‘bt470m’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘linear’ ‘log100’ ‘log316’ ‘iec61966-2-4’ ‘bt1361e’ ‘iec61966-2-1’ ‘bt2020-10’ ‘bt2020-12’ ‘smpte2084’ ‘smpte428’ ‘arib-std-b67’
        colorspace:
            Set the colorspace. Available values are: ‘auto’ Keep the same colorspace property (default). ‘gbr’ ‘bt709’ ‘unknown’ ‘fcc’ ‘bt470bg’ ‘smpte170m’ ‘smpte240m’ ‘ycgco’ ‘bt2020nc’ ‘bt2020c’ ‘smpte2085’ ‘chroma-derived-nc’ ‘chroma-derived-c’ ‘ictcp’



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setparams

        """
        return FilterNode(
            *[self],
            name="setparams",
            kwargs={
                "field_mode": field_mode,
                "range": range,
                "color_primaries": color_primaries,
                "color_trc": color_trc,
                "colorspace": colorspace,
                **kwargs,
            }
        ).stream()

    def setsar(self, *, r: str, max: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.226 setdar, setsar The setdar filter sets the Display Aspect Ratio for the filter output video. This is done by changing the specified Sample (aka Pixel) Aspect Ratio, according to the following equation: DAR = HORIZONTAL_RESOLUTION / VERTICAL_RESOLUTION * SAR Keep in mind that the setdar filter does not modify the pixel dimensions of the video frame. Also, the display aspect ratio set by this filter may be changed by later filters in the filterchain, e.g. in case of scaling or if another "setdar" or a "setsar" filter is applied. The setsar filter sets the Sample (aka Pixel) Aspect Ratio for the filter output video. Note that as a consequence of the application of this filter, the output display aspect ratio will change according to the equation above. Keep in mind that the sample aspect ratio set by the setsar filter may be changed by later filters in the filterchain, e.g. if another "setsar" or a "setdar" filter is applied. It accepts the following parameters: The parameter sar is an expression containing the following constants:

        Parameters:
        ----------
        r:
            Set the aspect ratio used by the filter. The parameter can be a floating point number string, or an expression. If the parameter is not specified, the value "0" is assumed, meaning that the same input value is used.
        max:
            Set the maximum integer value to use for expressing numerator and denominator when reducing the expressed aspect ratio to a rational. Default value is 100.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar

        """
        return FilterNode(*[self], name="setsar", kwargs={"r": r, "max": max, **kwargs}).stream()

    def sharpen_npp(self, *, border_type: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.229 sharpen_npp Use the NVIDIA Performance Primitives (libnpp) to perform image sharpening with border control. The following additional options are accepted:

        Parameters:
        ----------
        border_type:
            Type of sampling to be used ad frame borders. One of the following: replicate Replicate pixel values.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sharpen_005fnpp

        """
        return FilterNode(*[self], name="sharpen_npp", kwargs={"border_type": border_type, **kwargs}).stream()

    def shear(
        self,
        *,
        shx: float = None,
        shy: float = None,
        fillcolor: str = None,
        interp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.230 shear Apply shear transform to input video. This filter supports the following options:

        Parameters:
        ----------
        shx:
            Shear factor in X-direction. Default value is 0. Allowed range is from -2 to 2.
        shy:
            Shear factor in Y-direction. Default value is 0. Allowed range is from -2 to 2.
        fillcolor:
            Set the color used to fill the output area not covered by the transformed video. For the general syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special value "none" is selected then no background is printed (useful for example if the background is never shown). Default value is "black".
        interp:
            Set interpolation type. Can be bilinear or nearest. Default is bilinear.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shear

        """
        return FilterNode(
            *[self], name="shear", kwargs={"shx": shx, "shy": shy, "fillcolor": fillcolor, "interp": interp, **kwargs}
        ).stream()

    def showinfo(self, *, checksum: bool = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.231 showinfo Show a line containing various information for each input video frame. The input video is not modified. This filter supports the following options: The shown line contains a sequence of key/value pairs of the form key:value. The following values are shown in the output:

        Parameters:
        ----------
        checksum:
            Calculate checksums of each plane. By default enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showinfo

        """
        return FilterNode(*[self], name="showinfo", kwargs={"checksum": checksum, **kwargs}).stream()

    def showpalette(self, *, s: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.232 showpalette Displays the 256 colors palette of each frame. This filter is only relevant for pal8 pixel format frames. It accepts the following option:

        Parameters:
        ----------
        s:
            Set the size of the box used to represent one palette color entry. Default is 30 (for a 30x30 pixel box).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#showpalette

        """
        return FilterNode(*[self], name="showpalette", kwargs={"s": s, **kwargs}).stream()

    def shuffleframes(self, *, mapping: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.233 shuffleframes Reorder and/or duplicate and/or drop video frames. It accepts the following parameters: The first frame has the index 0. The default is to keep the input unchanged.

        Parameters:
        ----------
        mapping:
            Set the destination indexes of input frames. This is space or ’|’ separated list of indexes that maps input frames to output frames. Number of indexes also sets maximal value that each index may have. ’-1’ index have special meaning and that is to drop frame.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleframes

        """
        return FilterNode(*[self], name="shuffleframes", kwargs={"mapping": mapping, **kwargs}).stream()

    def shufflepixels(
        self, *, direction: str = None, mode: str, width: int, height: int, seed: int, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.234 shufflepixels Reorder pixels in video frames. This filter accepts the following options:

        Parameters:
        ----------
        direction:
            Set shuffle direction. Can be forward or inverse direction. Default direction is forward.
        mode:
            Set shuffle mode. Can be horizontal, vertical or block mode.
        width:
            Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        height:
            Set shuffle block_size. In case of horizontal shuffle mode only width part of size is used, and in case of vertical shuffle mode only height part of size is used.
        seed:
            Set random seed used with shuffling pixels. Mainly useful to set to be able to reverse filtering process to get original input. For example, to reverse forward shuffle you need to use same parameters and exact same seed and to set direction to inverse.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shufflepixels

        """
        return FilterNode(
            *[self],
            name="shufflepixels",
            kwargs={"direction": direction, "mode": mode, "width": width, "height": height, "seed": seed, **kwargs}
        ).stream()

    def shuffleplanes(self, *, map0: int, map1: int, map2: int, map3: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.235 shuffleplanes Reorder and/or duplicate video planes. It accepts the following parameters: The first plane has the index 0. The default is to keep the input unchanged.

        Parameters:
        ----------
        map0:
            The index of the input plane to be used as the first output plane.
        map1:
            The index of the input plane to be used as the second output plane.
        map2:
            The index of the input plane to be used as the third output plane.
        map3:
            The index of the input plane to be used as the fourth output plane.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#shuffleplanes

        """
        return FilterNode(
            *[self], name="shuffleplanes", kwargs={"map0": map0, "map1": map1, "map2": map2, "map3": map3, **kwargs}
        ).stream()

    def sidechaincompress(
        self,
        *,
        level_in: float = None,
        mode: str = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        link: str = None,
        detection: str = None,
        level_sc: float = None,
        mix: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.105 sidechaincompress This filter acts like normal compressor but has the ability to compress detected signal using second input signal. It needs two input streams and returns one output stream. First input stream will be processed depending on second stream signal. The filtered signal then can be filtered with other filters in later stages of processing. See pan and amerge filter. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input gain. Default is 1. Range is between 0.015625 and 64.
        mode:
            Set mode of compressor operation. Can be upward or downward. Default is downward.
        threshold:
            If a signal of second stream raises above this level it will affect the gain reduction of first stream. By default is 0.125. Range is between 0.00097563 and 1.
        ratio:
            Set a ratio about which the signal is reduced. 1:2 means that if the level raised 4dB above the threshold, it will be only 2dB above after the reduction. Default is 2. Range is between 1 and 20.
        attack:
            Amount of milliseconds the signal has to rise above the threshold before gain reduction starts. Default is 20. Range is between 0.01 and 2000.
        release:
            Amount of milliseconds the signal has to fall below the threshold before reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
        makeup:
            Set the amount by how much signal will be amplified after processing. Default is 1. Range is from 1 to 64.
        knee:
            Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.82843. Range is between 1 and 8.
        link:
            Choose if the average level between all channels of side-chain stream or the louder(maximum) channel of side-chain stream affects the reduction. Default is average.
        detection:
            Should the exact signal be taken in case of peak or an RMS one in case of rms. Default is rms which is mainly smoother.
        level_sc:
            Set sidechain gain. Default is 1. Range is between 0.015625 and 64.
        mix:
            How much to use compressed signal in output. Default is 1. Range is between 0 and 1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress

        """
        return FilterNode(
            *[self],
            name="sidechaincompress",
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
                **kwargs,
            }
        ).stream()

    def sidechaingate(
        self,
        *,
        level_in: float = None,
        mode: str = None,
        range: float = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        detection: str = None,
        link: str = None,
        level_sc: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.106 sidechaingate A sidechain gate acts like a normal (wideband) gate but has the ability to filter the detected signal before sending it to the gain reduction stage. Normally a gate uses the full range signal to detect a level above the threshold. For example: If you cut all lower frequencies from your sidechain signal the gate will decrease the volume of your track only if not enough highs appear. With this technique you are able to reduce the resonation of a natural drum or remove "rumbling" of muted strokes from a heavily distorted guitar. It needs two input streams and returns one output stream. First input stream will be processed depending on second stream signal. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input level before filtering. Default is 1. Allowed range is from 0.015625 to 64.
        mode:
            Set the mode of operation. Can be upward or downward. Default is downward. If set to upward mode, higher parts of signal will be amplified, expanding dynamic range in upward direction. Otherwise, in case of downward lower parts of signal will be reduced.
        range:
            Set the level of gain reduction when the signal is below the threshold. Default is 0.06125. Allowed range is from 0 to 1. Setting this to 0 disables reduction and then filter behaves like expander.
        threshold:
            If a signal rises above this level the gain reduction is released. Default is 0.125. Allowed range is from 0 to 1.
        ratio:
            Set a ratio about which the signal is reduced. Default is 2. Allowed range is from 1 to 9000.
        attack:
            Amount of milliseconds the signal has to rise above the threshold before gain reduction stops. Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
        release:
            Amount of milliseconds the signal has to fall below the threshold before the reduction is increased again. Default is 250 milliseconds. Allowed range is from 0.01 to 9000.
        makeup:
            Set amount of amplification of signal after processing. Default is 1. Allowed range is from 1 to 64.
        knee:
            Curve the sharp knee around the threshold to enter gain reduction more softly. Default is 2.828427125. Allowed range is from 1 to 8.
        detection:
            Choose if exact signal should be taken for detection or an RMS like one. Default is rms. Can be peak or rms.
        link:
            Choose if the average level between all channels or the louder channel affects the reduction. Default is average. Can be average or maximum.
        level_sc:
            Set sidechain gain. Default is 1. Range is from 0.015625 to 64.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sidechaingate

        """
        return FilterNode(
            *[self],
            name="sidechaingate",
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
                **kwargs,
            }
        ).stream()

    def signature(
        self,
        *,
        detectmode: str = None,
        nb_inputs: int = None,
        filename: str,
        format: str = None,
        th_d: int = None,
        th_dc: int = None,
        th_xh: int = None,
        th_di: int = None,
        th_it: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.237 signature Calculates the MPEG-7 Video Signature. The filter can handle more than one input. In this case the matching between the inputs can be calculated additionally. The filter always passes through the first input. The signature of each stream can be written into a file. It accepts the following options:

        Parameters:
        ----------
        detectmode:
            Enable or disable the matching process. Available values are: ‘off’ Disable the calculation of a matching (default). ‘full’ Calculate the matching for the whole video and output whether the whole video matches or only parts. ‘fast’ Calculate only until a matching is found or the video ends. Should be faster in some cases.
        nb_inputs:
            Set the number of inputs. The option value must be a non negative integer. Default value is 1.
        filename:
            Set the path to which the output is written. If there is more than one input, the path must be a prototype, i.e. must contain %d or %0nd (where n is a positive integer), that will be replaced with the input number. If no filename is specified, no output will be written. This is the default.
        format:
            Choose the output format. Available values are: ‘binary’ Use the specified binary representation (default). ‘xml’ Use the specified xml representation.
        th_d:
            Set threshold to detect one word as similar. The option value must be an integer greater than zero. The default value is 9000.
        th_dc:
            Set threshold to detect all words as similar. The option value must be an integer greater than zero. The default value is 60000.
        th_xh:
            Set threshold to detect frames as similar. The option value must be an integer greater than zero. The default value is 116.
        th_di:
            Set the minimum length of a sequence in frames to recognize it as matching sequence. The option value must be a non negative integer value. The default value is 0.
        th_it:
            Set the minimum relation, that matching frames to all frames must have. The option value must be a double value between 0 and 1. The default value is 0.5.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#signature

        """
        return FilterNode(
            *[self],
            name="signature",
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
                **kwargs,
            }
        ).stream()

    def silencedetect(self, *, noise: str, duration: str, mono: bool, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.107 silencedetect Detect silence in an audio stream. This filter logs a message when it detects that the input audio volume is less or equal to a noise tolerance value for a duration greater or equal to the minimum detected noise duration. The printed times and duration are expressed in seconds. The lavfi.silence_start or lavfi.silence_start.X metadata key is set on the first frame whose timestamp equals or exceeds the detection duration and it contains the timestamp of the first frame of the silence. The lavfi.silence_duration or lavfi.silence_duration.X and lavfi.silence_end or lavfi.silence_end.X metadata keys are set on the first frame after the silence. If mono is enabled, and each channel is evaluated separately, the .X suffixed keys are used, and X corresponds to the channel number. The filter accepts the following options:

        Parameters:
        ----------
        noise:
            Set noise tolerance. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default is -60dB, or 0.001.
        duration:
            Set silence duration until notification (default is 2 seconds). See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax.
        mono:
            Process each channel separately, instead of combined. By default is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silencedetect

        """
        return FilterNode(
            *[self], name="silencedetect", kwargs={"noise": noise, "duration": duration, "mono": mono, **kwargs}
        ).stream()

    def silenceremove(
        self,
        *,
        start_periods: int = None,
        start_duration: float = None,
        start_threshold: float = None,
        start_silence: float = None,
        start_mode: str = None,
        stop_periods: int = None,
        stop_duration: float = None,
        stop_threshold: float = None,
        stop_silence: float = None,
        stop_mode: str = None,
        detection: str = None,
        window: float = None,
        timestamp: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.108 silenceremove Remove silence from the beginning, middle or end of the audio. The filter accepts the following options:

        Parameters:
        ----------
        start_periods:
            This value is used to indicate if audio should be trimmed at beginning of the audio. A value of zero indicates no silence should be trimmed from the beginning. When specifying a non-zero value, it trims audio up until it finds non-silence. Normally, when trimming silence from beginning of audio the start_periods will be 1 but it can be increased to higher values to trim all audio up to specific count of non-silence periods. Default value is 0.
        start_duration:
            Specify the amount of time that non-silence must be detected before it stops trimming audio. By increasing the duration, bursts of noises can be treated as silence and trimmed off. Default value is 0.
        start_threshold:
            This indicates what sample value should be treated as silence. For digital audio, a value of 0 may be fine but for audio recorded from analog, you may wish to increase the value to account for background noise. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default value is 0.
        start_silence:
            Specify max duration of silence at beginning that will be kept after trimming. Default is 0, which is equal to trimming all samples detected as silence.
        start_mode:
            Specify mode of detection of silence end at start of multi-channel audio. Can be any or all. Default is any. With any, any sample from any channel that is detected as non-silence will trigger end of silence trimming at start of audio stream. With all, only if every sample from every channel is detected as non-silence will trigger end of silence trimming at start of audio stream, limited usage.
        stop_periods:
            Set the count for trimming silence from the end of audio. When specifying a positive value, it trims audio after it finds specified silence period. To remove silence from the middle of a file, specify a stop_periods that is negative. This value is then treated as a positive value and is used to indicate the effect should restart processing as specified by stop_periods, making it suitable for removing periods of silence in the middle of the audio. Default value is 0.
        stop_duration:
            Specify a duration of silence that must exist before audio is not copied any more. By specifying a higher duration, silence that is wanted can be left in the audio. Default value is 0.
        stop_threshold:
            This is the same as start_threshold but for trimming silence from the end of audio. Can be specified in dB (in case "dB" is appended to the specified value) or amplitude ratio. Default value is 0.
        stop_silence:
            Specify max duration of silence at end that will be kept after trimming. Default is 0, which is equal to trimming all samples detected as silence.
        stop_mode:
            Specify mode of detection of silence start after start of multi-channel audio. Can be any or all. Default is all. With any, any sample from any channel that is detected as silence will trigger start of silence trimming after start of audio stream, limited usage. With all, only if every sample from every channel is detected as silence will trigger start of silence trimming after start of audio stream.
        detection:
            Set how is silence detected. avg Mean of absolute values of samples in moving window. rms Root squared mean of absolute values of samples in moving window. peak Maximum of absolute values of samples in moving window. median Median of absolute values of samples in moving window. ptp Absolute of max peak to min peak difference of samples in moving window. dev Standard deviation of values of samples in moving window. Default value is rms.
        window:
            Set duration in number of seconds used to calculate size of window in number of samples for detecting silence. Using 0 will effectively disable any windowing and use only single sample per channel for silence detection. In that case it may be needed to also set start_silence and/or stop_silence to nonzero values with also start_duration and/or stop_duration to nonzero values. Default value is 0.02. Allowed range is from 0 to 10.
        timestamp:
            Set processing mode of every audio frame output timestamp. write Full timestamps rewrite, keep only the start time for the first output frame. copy Non-dropped frames are left with same timestamp as input audio frame. Defaults value is write.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#silenceremove

        """
        return FilterNode(
            *[self],
            name="silenceremove",
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
                **kwargs,
            }
        ).stream()

    def siti(self, *, print_summary: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.238 siti Calculate Spatial Information (SI) and Temporal Information (TI) scores for a video, as defined in ITU-T Rec. P.910 (11/21): Subjective video quality assessment methods for multimedia applications. Available PDF at https://www.itu.int/rec/T-REC-P.910-202111-S/en. Note that this is a legacy implementation that corresponds to a superseded recommendation. Refer to ITU-T Rec. P.910 (07/22) for the latest version: https://www.itu.int/rec/T-REC-P.910-202207-I/en It accepts the following option:

        Parameters:
        ----------
        print_summary:
            If set to 1, Summary statistics will be printed to the console. Default 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#siti

        """
        return FilterNode(*[self], name="siti", kwargs={"print_summary": print_summary, **kwargs}).stream()

    def sobel(self, *, planes: int, scale: float, delta: float, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.240 sobel Apply sobel operator to input video stream. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.
        scale:
            Set value which will be multiplied with filtered result.
        delta:
            Set value which will be added to filtered result.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sobel

        """
        return FilterNode(
            *[self], name="sobel", kwargs={"planes": planes, "scale": scale, "delta": delta, **kwargs}
        ).stream()

    def sofalizer(
        self,
        *,
        sofa: str,
        gain: float,
        rotation: float,
        elevation: float,
        radius: float,
        type: str,
        speakers: str,
        lfegain: float,
        framesize: float,
        normalize: bool,
        interpolate: bool,
        minphase: bool,
        anglestep: float,
        radstep: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.109 sofalizer SOFAlizer uses head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones (audio formats up to 9 channels supported). The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database). SOFAlizer is developed at the Acoustics Research Institute (ARI) of the Austrian Academy of Sciences. To enable compilation of this filter you need to configure FFmpeg with --enable-libmysofa. The filter accepts the following options:

        Parameters:
        ----------
        sofa:
            Set the SOFA file used for rendering.
        gain:
            Set gain applied to audio. Value is in dB. Default is 0.
        rotation:
            Set rotation of virtual loudspeakers in deg. Default is 0.
        elevation:
            Set elevation of virtual speakers in deg. Default is 0.
        radius:
            Set distance in meters between loudspeakers and the listener with near-field HRTFs. Default is 1.
        type:
            Set processing type. Can be time or freq. time is processing audio in time domain which is slow. freq is processing audio in frequency domain which is fast. Default is freq.
        speakers:
            Set custom positions of virtual loudspeakers. Syntax for this option is: <CH> <AZIM> <ELEV>[|<CH> <AZIM> <ELEV>|...]. Each virtual loudspeaker is described with short channel name following with azimuth and elevation in degrees. Each virtual loudspeaker description is separated by ’|’. For example to override front left and front right channel positions use: ’speakers=FL 45 15|FR 345 15’. Descriptions with unrecognised channel names are ignored.
        lfegain:
            Set custom gain for LFE channels. Value is in dB. Default is 0.
        framesize:
            Set custom frame size in number of samples. Default is 1024. Allowed range is from 1024 to 96000. Only used if option ‘type’ is set to freq.
        normalize:
            Should all IRs be normalized upon importing SOFA file. By default is enabled.
        interpolate:
            Should nearest IRs be interpolated with neighbor IRs if exact position does not match. By default is disabled.
        minphase:
            Minphase all IRs upon loading of SOFA file. By default is disabled.
        anglestep:
            Set neighbor search angle step. Only used if option interpolate is enabled.
        radstep:
            Set neighbor search radius step. Only used if option interpolate is enabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sofalizer

        """
        return FilterNode(
            *[self],
            name="sofalizer",
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
                **kwargs,
            }
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.110 speechnorm Speech Normalizer. This filter expands or compresses each half-cycle of audio samples (local set of samples all above or all below zero and between two nearest zero crossings) depending on threshold value, so audio reaches target peak value under conditions controlled by below options. The filter accepts the following options:

        Parameters:
        ----------
        peak:
            Set the expansion target peak value. This specifies the highest allowed absolute amplitude level for the normalized audio input. Default value is 0.95. Allowed range is from 0.0 to 1.0.
        expansion:
            Set the maximum expansion factor. Allowed range is from 1.0 to 50.0. Default value is 2.0. This option controls maximum local half-cycle of samples expansion. The maximum expansion would be such that local peak value reaches target peak value but never to surpass it and that ratio between new and previous peak value does not surpass this option value.
        compression:
            Set the maximum compression factor. Allowed range is from 1.0 to 50.0. Default value is 2.0. This option controls maximum local half-cycle of samples compression. This option is used only if threshold option is set to value greater than 0.0, then in such cases when local peak is lower or same as value set by threshold all samples belonging to that peak’s half-cycle will be compressed by current compression factor.
        threshold:
            Set the threshold value. Default value is 0.0. Allowed range is from 0.0 to 1.0. This option specifies which half-cycles of samples will be compressed and which will be expanded. Any half-cycle samples with their local peak value below or same as this option value will be compressed by current compression factor, otherwise, if greater than threshold value they will be expanded with expansion factor so that it could reach peak target value but never surpass it.
        _raise:
            Set the expansion raising amount per each half-cycle of samples. Default value is 0.001. Allowed range is from 0.0 to 1.0. This controls how fast expansion factor is raised per each new half-cycle until it reaches expansion value. Setting this options too high may lead to distortions.
        fall:
            Set the compression raising amount per each half-cycle of samples. Default value is 0.001. Allowed range is from 0.0 to 1.0. This controls how fast compression factor is raised per each new half-cycle until it reaches compression value.
        channels:
            Specify which channels to filter, by default all available channels are filtered.
        invert:
            Enable inverted filtering, by default is disabled. This inverts interpretation of threshold option. When enabled any half-cycle of samples with their local peak value below or same as threshold option will be expanded otherwise it will be compressed.
        link:
            Link channels when calculating gain applied to each filtered channel sample, by default is disabled. When disabled each filtered channel gain calculation is independent, otherwise when this option is enabled the minimum of all possible gains for each filtered channel is used.
        rms:
            Set the expansion target RMS value. This specifies the highest allowed RMS level for the normalized audio input. Default value is 0.0, thus disabled. Allowed range is from 0.0 to 1.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#speechnorm

        """
        return FilterNode(
            *[self],
            name="speechnorm",
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
                **kwargs,
            }
        ).stream()

    def spp(
        self, *, quality: int = None, qp: int, mode: str = None, use_bframe_qp: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.241 spp Apply a simple postprocessing filter that compresses and decompresses the image at several (or - in the case of quality level 6 - all) shifts and average the results. The filter accepts the following options:

        Parameters:
        ----------
        quality:
            Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-6. If set to 0, the filter will have no effect. A value of 6 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        qp:
            Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        mode:
            Set thresholding mode. Available modes are: ‘hard’ Set hard thresholding (default). ‘soft’ Set soft thresholding (better de-ringing effect, but likely blurrier).
        use_bframe_qp:
            Enable the use of the QP from the B-Frames if set to 1. Using this option may cause flicker since the B-Frames have often larger QP. Default is 0 (not enabled).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#spp

        """
        return FilterNode(
            *[self],
            name="spp",
            kwargs={"quality": quality, "qp": qp, "mode": mode, "use_bframe_qp": use_bframe_qp, **kwargs}
        ).stream()

    def sr(self, *, dnn_backend: str, model: str, scale_factor: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.242 sr Scale the input by applying one of the super-resolution methods based on convolutional neural networks. Supported models: Super-Resolution Convolutional Neural Network model (SRCNN). See https://arxiv.org/abs/1501.00092. Efficient Sub-Pixel Convolutional Neural Network model (ESPCN). See https://arxiv.org/abs/1609.05158. Training scripts as well as scripts for model file (.pb) saving can be found at https://github.com/XueweiMeng/sr/tree/sr_dnn_native. Original repository is at https://github.com/HighVoltageRocknRoll/sr.git. The filter accepts the following options: To get full functionality (such as async execution), please use the dnn_processing filter.

        Parameters:
        ----------
        dnn_backend:
            Specify which DNN backend to use for model loading and execution. This option accepts the following values: ‘tensorflow’ TensorFlow backend. To enable this backend you need to install the TensorFlow for C library (see https://www.tensorflow.org/install/lang_c) and configure FFmpeg with --enable-libtensorflow
        model:
            Set path to model file specifying network architecture and its parameters. Note that different backends use different file formats. TensorFlow, OpenVINO backend can load files for only its format.
        scale_factor:
            Set scale factor for SRCNN model. Allowed values are 2, 3 and 4. Default value is 2. Scale factor is necessary for SRCNN model, because it accepts input upscaled using bicubic upscaling with proper scale factor.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#sr

        """
        return FilterNode(
            *[self],
            name="sr",
            kwargs={"dnn_backend": dnn_backend, "model": model, "scale_factor": scale_factor, **kwargs}
        ).stream()

    def ssim(self, *, stats_file: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.243 ssim Obtain the SSIM (Structural SImilarity Metric) between two input videos. This filter takes in input two input videos, the first input is considered the "main" source and is passed unchanged to the output. The second input is used as a "reference" video for computing the SSIM. Both video inputs must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The filter stores the calculated SSIM of each frame. The description of the accepted parameters follows. The file printed if stats_file is selected, contains a sequence of key/value pairs of the form key:value for each compared couple of frames. A description of each shown parameter follows: This filter also supports the framesync options.

        Parameters:
        ----------
        stats_file:
            If specified the filter will use the named file to save the SSIM of each individual frame. When filename equals "-" the data is sent to standard output.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#ssim

        """
        return FilterNode(*[self], name="ssim", kwargs={"stats_file": stats_file, **kwargs}).stream()

    def stereo3d(self, *, _in: str = None, out: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.244 stereo3d Convert between different stereoscopic image formats. The filters accept the following options:

        Parameters:
        ----------
        _in:
            Set stereoscopic image format of input. Available values for input image formats are: ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first Default value is ‘sbsl’.
        out:
            Set stereoscopic image format of output. ‘sbsl’ side by side parallel (left eye left, right eye right) ‘sbsr’ side by side crosseye (right eye left, left eye right) ‘sbs2l’ side by side parallel with half width resolution (left eye left, right eye right) ‘sbs2r’ side by side crosseye with half width resolution (right eye left, left eye right) ‘abl’ ‘tbl’ above-below (left eye above, right eye below) ‘abr’ ‘tbr’ above-below (right eye above, left eye below) ‘ab2l’ ‘tb2l’ above-below with half height resolution (left eye above, right eye below) ‘ab2r’ ‘tb2r’ above-below with half height resolution (right eye above, left eye below) ‘al’ alternating frames (left eye first, right eye second) ‘ar’ alternating frames (right eye first, left eye second) ‘irl’ interleaved rows (left eye has top row, right eye starts on next row) ‘irr’ interleaved rows (right eye has top row, left eye starts on next row) ‘arbg’ anaglyph red/blue gray (red filter on left eye, blue filter on right eye) ‘argg’ anaglyph red/green gray (red filter on left eye, green filter on right eye) ‘arcg’ anaglyph red/cyan gray (red filter on left eye, cyan filter on right eye) ‘arch’ anaglyph red/cyan half colored (red filter on left eye, cyan filter on right eye) ‘arcc’ anaglyph red/cyan color (red filter on left eye, cyan filter on right eye) ‘arcd’ anaglyph red/cyan color optimized with the least squares projection of dubois (red filter on left eye, cyan filter on right eye) ‘agmg’ anaglyph green/magenta gray (green filter on left eye, magenta filter on right eye) ‘agmh’ anaglyph green/magenta half colored (green filter on left eye, magenta filter on right eye) ‘agmc’ anaglyph green/magenta colored (green filter on left eye, magenta filter on right eye) ‘agmd’ anaglyph green/magenta color optimized with the least squares projection of dubois (green filter on left eye, magenta filter on right eye) ‘aybg’ anaglyph yellow/blue gray (yellow filter on left eye, blue filter on right eye) ‘aybh’ anaglyph yellow/blue half colored (yellow filter on left eye, blue filter on right eye) ‘aybc’ anaglyph yellow/blue colored (yellow filter on left eye, blue filter on right eye) ‘aybd’ anaglyph yellow/blue color optimized with the least squares projection of dubois (yellow filter on left eye, blue filter on right eye) ‘ml’ mono output (left eye only) ‘mr’ mono output (right eye only) ‘chl’ checkerboard, left eye first ‘chr’ checkerboard, right eye first ‘icl’ interleaved columns, left eye first ‘icr’ interleaved columns, right eye first ‘hdmi’ HDMI frame pack Default value is ‘arcd’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereo3d

        """
        return FilterNode(*[self], name="stereo3d", kwargs={"in": _in, "out": out, **kwargs}).stream()

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
        mode: str = None,
        slev: float = None,
        sbal: float = None,
        mlev: float = None,
        mpan: float = None,
        base: float = None,
        delay: float = None,
        sclevel: float = None,
        phase: float = None,
        bmode_in: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.111 stereotools This filter has some handy utilities to manage stereo signals, for converting M/S stereo recordings to L/R signal while having control over the parameters or spreading the stereo image of master track. The filter accepts the following options:

        Parameters:
        ----------
        level_in:
            Set input level before filtering for both channels. Defaults is 1. Allowed range is from 0.015625 to 64.
        level_out:
            Set output level after filtering for both channels. Defaults is 1. Allowed range is from 0.015625 to 64.
        balance_in:
            Set input balance between both channels. Default is 0. Allowed range is from -1 to 1.
        balance_out:
            Set output balance between both channels. Default is 0. Allowed range is from -1 to 1.
        softclip:
            Enable softclipping. Results in analog distortion instead of harsh digital 0dB clipping. Disabled by default.
        mutel:
            Mute the left channel. Disabled by default.
        muter:
            Mute the right channel. Disabled by default.
        phasel:
            Change the phase of the left channel. Disabled by default.
        phaser:
            Change the phase of the right channel. Disabled by default.
        mode:
            Set stereo mode. Available values are: ‘lr>lr’ Left/Right to Left/Right, this is default. ‘lr>ms’ Left/Right to Mid/Side. ‘ms>lr’ Mid/Side to Left/Right. ‘lr>ll’ Left/Right to Left/Left. ‘lr>rr’ Left/Right to Right/Right. ‘lr>l+r’ Left/Right to Left + Right. ‘lr>rl’ Left/Right to Right/Left. ‘ms>ll’ Mid/Side to Left/Left. ‘ms>rr’ Mid/Side to Right/Right. ‘ms>rl’ Mid/Side to Right/Left. ‘lr>l-r’ Left/Right to Left - Right.
        slev:
            Set level of side signal. Default is 1. Allowed range is from 0.015625 to 64.
        sbal:
            Set balance of side signal. Default is 0. Allowed range is from -1 to 1.
        mlev:
            Set level of the middle signal. Default is 1. Allowed range is from 0.015625 to 64.
        mpan:
            Set middle signal pan. Default is 0. Allowed range is from -1 to 1.
        base:
            Set stereo base between mono and inversed channels. Default is 0. Allowed range is from -1 to 1.
        delay:
            Set delay in milliseconds how much to delay left from right channel and vice versa. Default is 0. Allowed range is from -20 to 20.
        sclevel:
            Set S/C level. Default is 1. Allowed range is from 1 to 100.
        phase:
            Set the stereo phase in degrees. Default is 0. Allowed range is from 0 to 360.
        bmode_in:
            Set balance mode for balance_in/balance_out option. Can be one of the following: ‘balance’ Classic balance mode. Attenuate one channel at time. Gain is raised up to 1. ‘amplitude’ Similar as classic mode above but gain is raised up to 2. ‘power’ Equal power distribution, from -6dB to +6dB range.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereotools

        """
        return FilterNode(
            *[self],
            name="stereotools",
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
                **kwargs,
            }
        ).stream()

    def stereowiden(
        self,
        *,
        delay: float = None,
        feedback: float = None,
        crossfeed: float = None,
        drymix: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.112 stereowiden This filter enhance the stereo effect by suppressing signal common to both channels and by delaying the signal of left into right and vice versa, thereby widening the stereo effect. The filter accepts the following options:

        Parameters:
        ----------
        delay:
            Time in milliseconds of the delay of left signal into right and vice versa. Default is 20 milliseconds.
        feedback:
            Amount of gain in delayed signal into right and vice versa. Gives a delay effect of left signal in right output and vice versa which gives widening effect. Default is 0.3.
        crossfeed:
            Cross feed of left into right with inverted phase. This helps in suppressing the mono. If the value is 1 it will cancel all the signal common to both channels. Default is 0.3.
        drymix:
            Set level of input signal of original channel. Default is 0.8.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#stereowiden

        """
        return FilterNode(
            *[self],
            name="stereowiden",
            kwargs={"delay": delay, "feedback": feedback, "crossfeed": crossfeed, "drymix": drymix, **kwargs}
        ).stream()

    def streamselect(self, *, inputs: int = None, map: list[str], **kwargs: dict[str, Any]) -> "Stream":
        """
        11.245 streamselect, astreamselect Select video or audio streams. The filter accepts the following options:

        Parameters:
        ----------
        inputs:
            Set number of inputs. Default is 2.
        map:
            Set input indexes to remap to outputs.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect

        """
        return FilterNode(*[self], name="streamselect", kwargs={"inputs": inputs, "map": map, **kwargs}).stream()

    def subtitles(
        self,
        *,
        filename: str,
        original_size: str,
        fontsdir: str,
        alpha: bool,
        charenc: str,
        stream_index: int,
        force_style: str,
        wrap_unicode: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.246 subtitles Draw subtitles on top of input video using the libass library. To enable compilation of this filter you need to configure FFmpeg with --enable-libass. This filter also requires a build with libavcodec and libavformat to convert the passed subtitles file to ASS (Advanced Substation Alpha) subtitles format. The filter accepts the following options: If the first key is not specified, it is assumed that the first value specifies the filename. For example, to render the file sub.srt on top of the input video, use the command: subtitles=sub.srt which is equivalent to: subtitles=filename=sub.srt To render the default subtitles stream from file video.mkv, use: subtitles=video.mkv To render the second subtitles stream from that file, use: subtitles=video.mkv:si=1 To make the subtitles stream from sub.srt appear in 80% transparent blue DejaVu Serif, use: subtitles=sub.srt:force_style='Fontname=DejaVu Serif,PrimaryColour=&HCCFF0000'

        Parameters:
        ----------
        filename:
            Set the filename of the subtitle file to read. It must be specified.
        original_size:
            Specify the size of the original video, the video for which the ASS file was composed. For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual. Due to a misdesign in ASS aspect ratio arithmetic, this is necessary to correctly scale the fonts if the aspect ratio has been changed.
        fontsdir:
            Set a directory path containing fonts that can be used by the filter. These fonts will be used in addition to whatever the font provider uses.
        alpha:
            Process alpha channel, by default alpha channel is untouched.
        charenc:
            Set subtitles input character encoding. subtitles filter only. Only useful if not UTF-8.
        stream_index:
            Set subtitles stream index. subtitles filter only.
        force_style:
            Override default style or script info parameters of the subtitles. It accepts a string containing ASS style format KEY=VALUE couples separated by ",".
        wrap_unicode:
            Break lines according to the Unicode Line Breaking Algorithm. Availability requires at least libass release 0.17.0 (or LIBASS_VERSION 0x01600010), and libass must have been built with libunibreak. The option is enabled by default except for native ASS.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#subtitles

        """
        return FilterNode(
            *[self],
            name="subtitles",
            kwargs={
                "filename": filename,
                "original_size": original_size,
                "fontsdir": fontsdir,
                "alpha": alpha,
                "charenc": charenc,
                "stream_index": stream_index,
                "force_style": force_style,
                "wrap_unicode": wrap_unicode,
                **kwargs,
            }
        ).stream()

    def super2xsai(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.247 super2xsai Scale the input by 2x and smooth using the Super2xSaI (Scale and Interpolate) pixel art scaling algorithm. Useful for enlarging pixel art images without reducing sharpness.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#super2xsai

        """
        return FilterNode(*[self], name="super2xsai", kwargs={**kwargs}).stream()

    def superequalizer(
        self,
        *,
        _1b: float,
        _2b: float,
        _3b: float,
        _4b: float,
        _5b: float,
        _6b: float,
        _7b: float,
        _8b: float,
        _9b: float,
        _10b: float,
        _11b: float,
        _12b: float,
        _13b: float,
        _14b: float,
        _15b: float,
        _16b: float,
        _17b: float,
        _18b: float,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.113 superequalizer Apply 18 band equalizer. The filter accepts the following options:

        Parameters:
        ----------
        _1b:
            Set 65Hz band gain.
        _2b:
            Set 92Hz band gain.
        _3b:
            Set 131Hz band gain.
        _4b:
            Set 185Hz band gain.
        _5b:
            Set 262Hz band gain.
        _6b:
            Set 370Hz band gain.
        _7b:
            Set 523Hz band gain.
        _8b:
            Set 740Hz band gain.
        _9b:
            Set 1047Hz band gain.
        _10b:
            Set 1480Hz band gain.
        _11b:
            Set 2093Hz band gain.
        _12b:
            Set 2960Hz band gain.
        _13b:
            Set 4186Hz band gain.
        _14b:
            Set 5920Hz band gain.
        _15b:
            Set 8372Hz band gain.
        _16b:
            Set 11840Hz band gain.
        _17b:
            Set 16744Hz band gain.
        _18b:
            Set 20000Hz band gain.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#superequalizer

        """
        return FilterNode(
            *[self],
            name="superequalizer",
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
                **kwargs,
            }
        ).stream()

    def surround(
        self,
        *,
        chl_out: str = None,
        chl_in: str = None,
        level_in: float = None,
        level_out: float = None,
        lfe: bool = None,
        lfe_low: float = None,
        lfe_high: float = None,
        lfe_mode: str = None,
        smooth: float = None,
        angle: int = None,
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
        fcy: float = None,
        win_size: int = None,
        win_func: str = None,
        overlap: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.114 surround Apply audio surround upmix filter. This filter allows to produce multichannel output from audio stream. The filter accepts the following options:

        Parameters:
        ----------
        chl_out:
            Set output channel layout. By default, this is 5.1. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.
        chl_in:
            Set input channel layout. By default, this is stereo. See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual for the required syntax.
        level_in:
            Set input volume level. By default, this is 1.
        level_out:
            Set output volume level. By default, this is 1.
        lfe:
            Enable LFE channel output if output channel layout has it. By default, this is enabled.
        lfe_low:
            Set LFE low cut off frequency. By default, this is 128 Hz.
        lfe_high:
            Set LFE high cut off frequency. By default, this is 256 Hz.
        lfe_mode:
            Set LFE mode, can be add or sub. Default is add. In add mode, LFE channel is created from input audio and added to output. In sub mode, LFE channel is created from input audio and added to output but also all non-LFE output channels are subtracted with output LFE channel.
        smooth:
            Set temporal smoothness strength, used to gradually change factors when transforming stereo sound in time. Allowed range is from 0.0 to 1.0. Useful to improve output quality with focus option values greater than 0.0. Default is 0.0. Only values inside this range and without edges are effective.
        angle:
            Set angle of stereo surround transform, Allowed range is from 0 to 360. Default is 90.
        focus:
            Set focus of stereo surround transform, Allowed range is from -1 to 1. Default is 0.
        fc_in:
            Set front center input volume. By default, this is 1.
        fc_out:
            Set front center output volume. By default, this is 1.
        fl_in:
            Set front left input volume. By default, this is 1.
        fl_out:
            Set front left output volume. By default, this is 1.
        fr_in:
            Set front right input volume. By default, this is 1.
        fr_out:
            Set front right output volume. By default, this is 1.
        sl_in:
            Set side left input volume. By default, this is 1.
        sl_out:
            Set side left output volume. By default, this is 1.
        sr_in:
            Set side right input volume. By default, this is 1.
        sr_out:
            Set side right output volume. By default, this is 1.
        bl_in:
            Set back left input volume. By default, this is 1.
        bl_out:
            Set back left output volume. By default, this is 1.
        br_in:
            Set back right input volume. By default, this is 1.
        br_out:
            Set back right output volume. By default, this is 1.
        bc_in:
            Set back center input volume. By default, this is 1.
        bc_out:
            Set back center output volume. By default, this is 1.
        lfe_in:
            Set LFE input volume. By default, this is 1.
        lfe_out:
            Set LFE output volume. By default, this is 1.
        allx:
            Set spread usage of stereo image across X axis for all channels. Allowed range is from -1 to 15. By default this value is negative -1, and thus unused.
        ally:
            Set spread usage of stereo image across Y axis for all channels. Allowed range is from -1 to 15. By default this value is negative -1, and thus unused.
        fcx:
            Set spread usage of stereo image across X axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        fcy:
            Set spread usage of stereo image across Y axis for each channel. Allowed range is from 0.06 to 15. By default this value is 0.5.
        win_size:
            Set window size. Allowed range is from 1024 to 65536. Default size is 4096.
        win_func:
            Set window function. It accepts the following values: ‘rect’ ‘bartlett’ ‘hann, hanning’ ‘hamming’ ‘blackman’ ‘welch’ ‘flattop’ ‘bharris’ ‘bnuttall’ ‘bhann’ ‘sine’ ‘nuttall’ ‘lanczos’ ‘gauss’ ‘tukey’ ‘dolph’ ‘cauchy’ ‘parzen’ ‘poisson’ ‘bohman’ ‘kaiser’ Default is hann.
        overlap:
            Set window overlap. If set to 1, the recommended overlap for selected window function will be picked. Default is 0.5.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#surround

        """
        return FilterNode(
            *[self],
            name="surround",
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
                "fcy": fcy,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                **kwargs,
            }
        ).stream()

    def swaprect(self, *, w: str, h: str, x1: str, y1: str, x2: str, y2: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.248 swaprect Swap two rectangular objects in video. This filter accepts the following options: The all options are expressions containing the following constants:

        Parameters:
        ----------
        w:
            Set object width.
        h:
            Set object height.
        x1:
            Set 1st rect x coordinate.
        y1:
            Set 1st rect y coordinate.
        x2:
            Set 2nd rect x coordinate.
        y2:
            Set 2nd rect y coordinate. All expressions are evaluated once for each frame.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#swaprect

        """
        return FilterNode(
            *[self], name="swaprect", kwargs={"w": w, "h": h, "x1": x1, "y1": y1, "x2": x2, "y2": y2, **kwargs}
        ).stream()

    def swapuv(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.249 swapuv Swap U & V plane.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#swapuv

        """
        return FilterNode(*[self], name="swapuv", kwargs={**kwargs}).stream()

    def tblend(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.250 tblend Blend successive video frames. See blend

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tblend

        """
        return FilterNode(*[self], name="tblend", kwargs={**kwargs}).stream()

    def telecine(self, *, first_field: str = None, pattern: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.251 telecine Apply telecine process to the video. This filter accepts the following options: Some typical patterns: NTSC output (30i): 27.5p: 32222 24p: 23 (classic) 24p: 2332 (preferred) 20p: 33 18p: 334 16p: 3444 PAL output (25i): 27.5p: 12222 24p: 222222222223 ("Euro pulldown") 16.67p: 33 16p: 33333334

        Parameters:
        ----------
        first_field:
            ‘top, t’ top field first ‘bottom, b’ bottom field first The default value is top.
        pattern:
            A string of numbers representing the pulldown pattern you wish to apply. The default value is 23.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#telecine

        """
        return FilterNode(
            *[self], name="telecine", kwargs={"first_field": first_field, "pattern": pattern, **kwargs}
        ).stream()

    def thistogram(
        self,
        *,
        width: int = None,
        display_mode: str = None,
        levels_mode: str = None,
        components: int = None,
        bgopacity: float = None,
        envelope: bool = None,
        ecolor: str = None,
        slide: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.252 thistogram Compute and draw a color distribution histogram for the input video across time. Unlike histogram video filter which only shows histogram of single input frame at certain time, this filter shows also past histograms of number of frames defined by width option. The computed histogram is a representation of the color component distribution in an image. The filter accepts the following options:

        Parameters:
        ----------
        width:
            Set width of single color component output. Default value is 0. Value of 0 means width will be picked from input video. This also set number of passed histograms to keep. Allowed range is [0, 8192].
        display_mode:
            Set display mode. It accepts the following values: ‘stack’ Per color component graphs are placed below each other. ‘parade’ Per color component graphs are placed side by side. ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. Default is stack.
        levels_mode:
            Set mode. Can be either linear, or logarithmic. Default is linear.
        components:
            Set what color components to display. Default is 7.
        bgopacity:
            Set background opacity. Default is 0.9.
        envelope:
            Show envelope. Default is disabled.
        ecolor:
            Set envelope color. Default is gold.
        slide:
            Set slide mode. Available values for slide is: ‘frame’ Draw new frame when right border is reached. ‘replace’ Replace old columns with new ones. ‘scroll’ Scroll from right to left. ‘rscroll’ Scroll from left to right. ‘picture’ Draw single picture. Default is replace.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#thistogram

        """
        return FilterNode(
            *[self],
            name="thistogram",
            kwargs={
                "width": width,
                "display_mode": display_mode,
                "levels_mode": levels_mode,
                "components": components,
                "bgopacity": bgopacity,
                "envelope": envelope,
                "ecolor": ecolor,
                "slide": slide,
                **kwargs,
            }
        ).stream()

    def threshold(self, *, planes: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.253 threshold Apply threshold effect to video stream. This filter needs four video streams to perform thresholding. First stream is stream we are filtering. Second stream is holding threshold values, third stream is holding min values, and last, fourth stream is holding max values. The filter accepts the following option: For example if first stream pixel’s component value is less then threshold value of pixel component from 2nd threshold stream, third stream value will picked, otherwise fourth stream pixel component value will be picked. Using color source filter one can perform various types of thresholding:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#threshold

        """
        return FilterNode(*[self], name="threshold", kwargs={"planes": planes, **kwargs}).stream()

    def thumbnail(self, *, n: int = None, log: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.254 thumbnail Select the most representative frame in a given sequence of consecutive frames. The filter accepts the following options: Since the filter keeps track of the whole frames sequence, a bigger n value will result in a higher memory usage, so a high value is not recommended.

        Parameters:
        ----------
        n:
            Set the frames batch size to analyze; in a set of n frames, the filter will pick one of them, and then handle the next batch of n frames until the end. Default is 100.
        log:
            Set the log level to display picked frame stats. Default is info.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#thumbnail

        """
        return FilterNode(*[self], name="thumbnail", kwargs={"n": n, "log": log, **kwargs}).stream()

    def tile(
        self,
        *,
        layout: str,
        nb_frames: int,
        margin: int,
        padding: int,
        color: str,
        overlap: int,
        init_padding: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.255 tile Tile several successive frames together. The untile filter can do the reverse. The filter accepts the following options:

        Parameters:
        ----------
        layout:
            Set the grid size in the form COLUMNSxROWS. Range is up to UINT_MAX cells. Default is 6x5.
        nb_frames:
            Set the maximum number of frames to render in the given area. It must be less than or equal to wxh. The default value is 0, meaning all the area will be used.
        margin:
            Set the outer border margin in pixels. Range is 0 to 1024. Default is 0.
        padding:
            Set the inner border thickness (i.e. the number of pixels between frames). For more advanced padding options (such as having different values for the edges), refer to the pad video filter. Range is 0 to 1024. Default is 0.
        color:
            Specify the color of the unused area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".
        overlap:
            Set the number of frames to overlap when tiling several successive frames together. The value must be between 0 and nb_frames - 1. Default is 0.
        init_padding:
            Set the number of frames to initially be empty before displaying first output frame. This controls how soon will one get first output frame. The value must be between 0 and nb_frames - 1. Default is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tile

        """
        return FilterNode(
            *[self],
            name="tile",
            kwargs={
                "layout": layout,
                "nb_frames": nb_frames,
                "margin": margin,
                "padding": padding,
                "color": color,
                "overlap": overlap,
                "init_padding": init_padding,
                **kwargs,
            }
        ).stream()

    def tiltshelf(
        self,
        *,
        gain: float,
        frequency: float,
        width_type: str,
        width: float,
        poles: int = None,
        mix: float = None,
        channels: str,
        normalize: bool = None,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.115 tiltshelf Boost or cut the lower frequencies and cut or boost higher frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi’s tone-controls. This is also known as shelving equalisation (EQ). The filter accepts the following options:

        Parameters:
        ----------
        gain:
            Give the gain at 0 Hz. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency:
            Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Determine how steep is the filter’s shelf transition.
        poles:
            Set number of poles. Default is 2.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tiltshelf

        """
        return FilterNode(
            *[self],
            name="tiltshelf",
            kwargs={
                "gain": gain,
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def tinterlace(self, *, flags: list[str], **kwargs: dict[str, Any]) -> "Stream":
        """
        11.256 tinterlace Perform various types of temporal field interlacing. Frames are counted starting from 1, so the first input frame is considered odd. The filter accepts the following options:

        Parameters:
        ----------
        flags:
            Specify flags influencing the filter process. Available value for flags is: low_pass_filter, vlpf Enable linear vertical low-pass filtering in the filter. Vertical low-pass filtering is required when creating an interlaced destination from a progressive source which contains high-frequency vertical detail. Filtering will reduce interlace ’twitter’ and Moire patterning. complex_filter, cvlpf Enable complex vertical low-pass filtering. This will slightly less reduce interlace ’twitter’ and Moire patterning but better retain detail and subjective sharpness impression. bypass_il Bypass already interlaced frames, only adjust the frame rate. Vertical low-pass filtering and bypassing already interlaced frames can only be enabled for mode interleave_top and interleave_bottom.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tinterlace

        """
        return FilterNode(*[self], name="tinterlace", kwargs={"flags": flags, **kwargs}).stream()

    def tlut2(self, *, c0: str, c1: str, c2: str, c3: str, d: int, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.154 lut2, tlut2 The lut2 filter takes two input streams and outputs one stream. The tlut2 (time lut2) filter takes two consecutive frames from one single stream. This filter accepts the following parameters: The lut2 filter also supports the framesync options. Each of them specifies the expression to use for computing the lookup table for the corresponding pixel component values. The exact component associated to each of the c* options depends on the format in inputs. The expressions can contain the following constants: All expressions default to "x".

        Parameters:
        ----------
        c0:
            set first pixel component expression
        c1:
            set second pixel component expression
        c2:
            set third pixel component expression
        c3:
            set fourth pixel component expression, corresponds to the alpha component
        d:
            set output bit depth, only available for lut2 filter. By default is 0, which means bit depth is automatically picked from first input format.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2

        """
        return FilterNode(
            *[self], name="tlut2", kwargs={"c0": c0, "c1": c1, "c2": c2, "c3": c3, "d": d, **kwargs}
        ).stream()

    def tmedian(
        self, *, radius: int = None, planes: int = None, percentile: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.257 tmedian Pick median pixels from several successive input video frames. The filter accepts the following options:

        Parameters:
        ----------
        radius:
            Set radius of median filter. Default is 1. Allowed range is from 1 to 127.
        planes:
            Set which planes to filter. Default value is 15, by which all planes are processed.
        percentile:
            Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmedian

        """
        return FilterNode(
            *[self], name="tmedian", kwargs={"radius": radius, "planes": planes, "percentile": percentile, **kwargs}
        ).stream()

    def tmidequalizer(
        self, *, radius: int = None, sigma: float = None, planes: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.258 tmidequalizer Apply Temporal Midway Video Equalization effect. Midway Video Equalization adjusts a sequence of video frames to have the same histograms, while maintaining their dynamics as much as possible. It’s useful for e.g. matching exposures from a video frames sequence. This filter accepts the following option:

        Parameters:
        ----------
        radius:
            Set filtering radius. Default is 5. Allowed range is from 1 to 127.
        sigma:
            Set filtering sigma. Default is 0.5. This controls strength of filtering. Setting this option to 0 effectively does nothing.
        planes:
            Set which planes to process. Default is 15, which is all available planes.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmidequalizer

        """
        return FilterNode(
            *[self], name="tmidequalizer", kwargs={"radius": radius, "sigma": sigma, "planes": planes, **kwargs}
        ).stream()

    def tmix(
        self, *, frames: int = None, weights: str, scale: float, planes: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.259 tmix Mix successive video frames. A description of the accepted options follows.

        Parameters:
        ----------
        frames:
            The number of successive frames to mix. If unspecified, it defaults to 3.
        weights:
            Specify weight of each input video frame. Each weight is separated by space. If number of weights is smaller than number of frames last specified weight will be used for all remaining unset weights.
        scale:
            Specify scale, if it is set it will be multiplied with sum of each weight multiplied with pixel values to give final destination pixel value. By default scale is auto scaled to sum of weights.
        planes:
            Set which planes to filter. Default is all. Allowed range is from 0 to 15.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tmix

        """
        return FilterNode(
            *[self],
            name="tmix",
            kwargs={"frames": frames, "weights": weights, "scale": scale, "planes": planes, **kwargs}
        ).stream()

    def tonemap(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.260 tonemap Tone map colors from different dynamic ranges. This filter expects data in single precision floating point, as it needs to operate on (and can output) out-of-range values. Another filter, such as zscale, is needed to convert the resulting frame to a usable format. The tonemapping algorithms implemented only work on linear light, so input data should be linearized beforehand (and possibly correctly tagged). ffmpeg -i INPUT -vf zscale=transfer=linear,tonemap=clip,zscale=transfer=bt709,format=yuv420p OUTPUT

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tonemap

        """
        return FilterNode(*[self], name="tonemap", kwargs={**kwargs}).stream()

    def tpad(
        self,
        *,
        start: int = None,
        stop: int = None,
        start_mode: str = None,
        stop_mode: str = None,
        start_duration: str = None,
        color: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.261 tpad Temporarily pad video frames. The filter accepts the following options:

        Parameters:
        ----------
        start:
            Specify number of delay frames before input video stream. Default is 0.
        stop:
            Specify number of padding frames after input video stream. Set to -1 to pad indefinitely. Default is 0.
        start_mode:
            Set kind of frames added to beginning of stream. Can be either add or clone. With add frames of solid-color are added. With clone frames are clones of first frame. Default is add.
        stop_mode:
            Set kind of frames added to end of stream. Can be either add or clone. With add frames of solid-color are added. With clone frames are clones of last frame. Default is add.
        start_duration:
            Specify the duration of the start/stop delay. See (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. These options override start and stop. Default is 0.
        color:
            Specify the color of the padded area. For the syntax of this option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. The default value of color is "black".



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tpad

        """
        return FilterNode(
            *[self],
            name="tpad",
            kwargs={
                "start": start,
                "stop": stop,
                "start_mode": start_mode,
                "stop_mode": stop_mode,
                "start_duration": start_duration,
                "color": color,
                **kwargs,
            }
        ).stream()

    def transpose(self, *, passthrough: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.262 transpose Transpose rows with columns in the input video and optionally flip it. It accepts the following parameters: For example to rotate by 90 degrees clockwise and preserve portrait layout: transpose=dir=1:passthrough=portrait The command above can also be specified as: transpose=1:portrait

        Parameters:
        ----------
        passthrough:
            Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height). Default value is none.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose

        """
        return FilterNode(*[self], name="transpose", kwargs={"passthrough": passthrough, **kwargs}).stream()

    def transpose_npp(self, *, dir: str = None, passthrough: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.263 transpose_npp Transpose rows with columns in the input video and optionally flip it. For more in depth examples see the transpose video filter, which shares mostly the same options. It accepts the following parameters:

        Parameters:
        ----------
        dir:
            Specify the transposition direction. Can assume the following values: ‘cclock_flip’ Rotate by 90 degrees counterclockwise and vertically flip. (default) ‘clock’ Rotate by 90 degrees clockwise. ‘cclock’ Rotate by 90 degrees counterclockwise. ‘clock_flip’ Rotate by 90 degrees clockwise and vertically flip.
        passthrough:
            Do not apply the transposition if the input geometry matches the one specified by the specified value. It accepts the following values: ‘none’ Always apply transposition. (default) ‘portrait’ Preserve portrait geometry (when height >= width). ‘landscape’ Preserve landscape geometry (when width >= height).



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#transpose_005fnpp

        """
        return FilterNode(
            *[self], name="transpose_npp", kwargs={"dir": dir, "passthrough": passthrough, **kwargs}
        ).stream()

    def treble(
        self,
        *,
        gain: float,
        frequency: float,
        width_type: str,
        width: float,
        poles: int,
        mix: float,
        channels: str,
        normalize: bool,
        transform: str,
        precision: str,
        block_size: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.116 treble, highshelf Boost or cut treble (upper) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi’s tone-controls. This is also known as shelving equalisation (EQ). The filter accepts the following options:

        Parameters:
        ----------
        gain:
            Give the gain at whichever is the lower of ~22 kHz and the Nyquist frequency. Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of clipping when using a positive gain.
        frequency:
            Set the filter’s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 3000 Hz.
        width_type:
            Set method to specify band-width of filter. h Hz q Q-Factor o octave s slope k kHz
        width:
            Determine how steep is the filter’s shelf transition.
        poles:
            Set number of poles. Default is 2.
        mix:
            How much to use filtered signal in output. Default is 1. Range is between 0 and 1.
        channels:
            Specify which channels to filter, by default all available are filtered.
        normalize:
            Normalize biquad coefficients, by default is disabled. Enabling it will normalize magnitude response at DC to 0dB.
        transform:
            Set transform type of IIR filter. di dii tdi tdii latt svf zdf
        precision:
            Set precision of filtering. auto Pick automatic sample format depending on surround filters. s16 Always use signed 16-bit. s32 Always use signed 32-bit. f32 Always use float 32-bit. f64 Always use float 64-bit.
        block_size:
            Set block size used for reverse IIR processing. If this value is set to high enough value (higher than impulse response length truncated when reaches near zero values) filtering will become linear phase otherwise if not big enough it will just produce nasty artifacts. Note that filter delay will be exactly this many samples when set to non-zero value.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf

        """
        return FilterNode(
            *[self],
            name="treble",
            kwargs={
                "gain": gain,
                "frequency": frequency,
                "width_type": width_type,
                "width": width,
                "poles": poles,
                "mix": mix,
                "channels": channels,
                "normalize": normalize,
                "transform": transform,
                "precision": precision,
                "block_size": block_size,
                **kwargs,
            }
        ).stream()

    def tremolo(self, *, f: float = None, d: float = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.117 tremolo Sinusoidal amplitude modulation. The filter accepts the following options:

        Parameters:
        ----------
        f:
            Modulation frequency in Hertz. Modulation frequencies in the subharmonic range (20 Hz or lower) will result in a tremolo effect. This filter may also be used as a ring modulator by specifying a modulation frequency higher than 20 Hz. Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        d:
            Depth of modulation as a percentage. Range is 0.0 - 1.0. Default value is 0.5.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#tremolo

        """
        return FilterNode(*[self], name="tremolo", kwargs={"f": f, "d": d, **kwargs}).stream()

    def trim(
        self,
        *,
        start: str,
        end: str,
        start_pts: str,
        end_pts: str,
        duration: str,
        start_frame: int,
        end_frame: int,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.264 trim Trim the input so that the output contains one continuous subpart of the input. It accepts the following parameters: start, end, and duration are expressed as time duration specifications; see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual for the accepted syntax. Note that the first two sets of the start/end options and the duration option look at the frame timestamp, while the _frame variants simply count the frames that pass through the filter. Also note that this filter does not modify the timestamps. If you wish for the output timestamps to start at zero, insert a setpts filter after the trim filter. If multiple start or end options are set, this filter tries to be greedy and keep all the frames that match at least one of the specified constraints. To keep only the part that matches all the constraints at once, chain multiple trim filters. The defaults are such that all the input is kept. So it is possible to set e.g. just the end values to keep everything before the specified time. Examples: Drop everything except the second minute of input: ffmpeg -i INPUT -vf trim=60:120 Keep only the first second: ffmpeg -i INPUT -vf trim=duration=1

        Parameters:
        ----------
        start:
            Specify the time of the start of the kept section, i.e. the frame with the timestamp start will be the first frame in the output.
        end:
            Specify the time of the first frame that will be dropped, i.e. the frame immediately preceding the one with the timestamp end will be the last frame in the output.
        start_pts:
            This is the same as start, except this option sets the start timestamp in timebase units instead of seconds.
        end_pts:
            This is the same as end, except this option sets the end timestamp in timebase units instead of seconds.
        duration:
            The maximum duration of the output in seconds.
        start_frame:
            The number of the first frame that should be passed to the output.
        end_frame:
            The number of the first frame that should be dropped.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#trim

        """
        return FilterNode(
            *[self],
            name="trim",
            kwargs={
                "start": start,
                "end": end,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "start_frame": start_frame,
                "end_frame": end_frame,
                **kwargs,
            }
        ).stream()

    def unpremultiply(self, *, planes: int, inplace: bool, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.265 unpremultiply Apply alpha unpremultiply effect to input video stream using first plane of second stream as alpha. Both streams must have same dimensions and same pixel format. The filter accepts the following option:

        Parameters:
        ----------
        planes:
            Set which planes will be processed, unprocessed planes will be copied. By default value 0xf, all planes will be processed. If the format has 1 or 2 components, then luma is bit 0. If the format has 3 or 4 components: for RGB formats bit 0 is green, bit 1 is blue and bit 2 is red; for YUV formats bit 0 is luma, bit 1 is chroma-U and bit 2 is chroma-V. If present, the alpha channel is always the last bit.
        inplace:
            Do not require 2nd input for processing, instead use alpha plane from input stream.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#unpremultiply

        """
        return FilterNode(
            *[self], name="unpremultiply", kwargs={"planes": planes, "inplace": inplace, **kwargs}
        ).stream()

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
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.266 unsharp Sharpen or blur the input video. It accepts the following parameters: All parameters are optional and default to the equivalent of the string ’5:5:1.0:5:5:0.0’.

        Parameters:
        ----------
        luma_msize_x:
            Set the luma matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        luma_msize_y:
            Set the luma matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        luma_amount:
            Set the luma effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 1.0.
        chroma_msize_x:
            Set the chroma matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        chroma_msize_y:
            Set the chroma matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        chroma_amount:
            Set the chroma effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 0.0.
        alpha_msize_x:
            Set the alpha matrix horizontal size. It must be an odd integer between 3 and 23. The default value is 5.
        alpha_msize_y:
            Set the alpha matrix vertical size. It must be an odd integer between 3 and 23. The default value is 5.
        alpha_amount:
            Set the alpha effect strength. It must be a floating point number, reasonable values lay between -1.5 and 1.5. Negative values will blur the input video, while positive values will sharpen it, a value of zero will disable the effect. Default value is 0.0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#unsharp

        """
        return FilterNode(
            *[self],
            name="unsharp",
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
                **kwargs,
            }
        ).stream()

    def untile(self, *, layout: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.267 untile Decompose a video made of tiled images into the individual images. The frame rate of the output video is the frame rate of the input video multiplied by the number of tiles. This filter does the reverse of tile. The filter accepts the following options:

        Parameters:
        ----------
        layout:
            Set the grid size (i.e. the number of lines and columns). For the syntax of this option, check the (ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#untile

        """
        return FilterNode(*[self], name="untile", kwargs={"layout": layout, **kwargs}).stream()

    def uspp(self, *, quality: int = None, qp: int, codec: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.268 uspp Apply ultra slow/simple postprocessing filter that compresses and decompresses the image at several (or - in the case of quality level 8 - all) shifts and average the results. The way this differs from the behavior of spp is that uspp actually encodes & decodes each case with libavcodec Snow, whereas spp uses a simplified intra only 8x8 DCT similar to MJPEG. This filter is only available in ffmpeg version 4.4 or earlier. The filter accepts the following options:

        Parameters:
        ----------
        quality:
            Set quality. This option defines the number of levels for averaging. It accepts an integer in the range 0-8. If set to 0, the filter will have no effect. A value of 8 means the higher quality. For each increment of that value the speed drops by a factor of approximately 2. Default value is 3.
        qp:
            Force a constant quantization parameter. If not set, the filter will use the QP from the video stream (if available).
        codec:
            Use specified codec instead of snow.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#uspp

        """
        return FilterNode(
            *[self], name="uspp", kwargs={"quality": quality, "qp": qp, "codec": codec, **kwargs}
        ).stream()

    def v360(
        self,
        *,
        input: str,
        output: str,
        interp: str,
        w: float,
        h: float,
        in_stereo: str,
        out_stereo: str,
        yaw: float,
        pitch: float,
        roll: float,
        rorder: str,
        h_flip: bool,
        v_flip: bool,
        d_flip: bool,
        ih_flip: bool,
        iv_flip: bool,
        in_trans: bool,
        out_trans: bool,
        h_offset: float,
        v_offset: float,
        alpha_mask: bool,
        reset_rot: bool,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.269 v360 Convert 360 videos between various formats. The filter accepts the following options:

        Parameters:
        ----------
        input:
            Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        output:
            Set format of the input/output video. Available formats: ‘e’ ‘equirect’ Equirectangular projection. ‘c3x2’ ‘c6x1’ ‘c1x6’ Cubemap with 3x2/6x1/1x6 layout. Format specific options: in_pad out_pad Set padding proportion for the input/output cubemap. Values in decimals. Example values: ‘0’ No padding. ‘0.01’ 1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels) Default value is ‘0’. Maximum value is ‘0.1’. fin_pad fout_pad Set fixed padding for the input/output cubemap. Values in pixels. Default value is ‘0’. If greater than zero it overrides other padding options. in_forder out_forder Set order of faces for the input/output cubemap. Choose one direction for each position. Designation of directions: ‘r’ right ‘l’ left ‘u’ up ‘d’ down ‘f’ forward ‘b’ back Default value is ‘rludfb’. in_frot out_frot Set rotation of faces for the input/output cubemap. Choose one angle for each position. Designation of angles: ‘0’ 0 degrees clockwise ‘1’ 90 degrees clockwise ‘2’ 180 degrees clockwise ‘3’ 270 degrees clockwise Default value is ‘000000’. ‘eac’ Equi-Angular Cubemap. ‘flat’ ‘gnomonic’ ‘rectilinear’ Regular video. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘dfisheye’ Dual fisheye. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘barrel’ ‘fb’ ‘barrelsplit’ Facebook’s 360 formats. ‘sg’ Stereographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘mercator’ Mercator format. ‘ball’ Ball format, gives significant distortion toward the back. ‘hammer’ Hammer-Aitoff map projection format. ‘sinusoidal’ Sinusoidal map projection format. ‘fisheye’ Fisheye projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘pannini’ Pannini projection. Format specific options: h_fov Set output pannini parameter. ih_fov Set input pannini parameter. ‘cylindrical’ Cylindrical projection. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘perspective’ Perspective projection. (output only) Format specific options: v_fov Set perspective parameter. ‘tetrahedron’ Tetrahedron projection. ‘tsp’ Truncated square pyramid projection. ‘he’ ‘hequirect’ Half equirectangular projection. ‘equisolid’ Equisolid format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘og’ Orthographic format. Format specific options: h_fov v_fov d_fov Set output horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ih_fov iv_fov id_fov Set input horizontal/vertical/diagonal field of view. Values in degrees. If diagonal field of view is set it overrides horizontal and vertical field of view. ‘octahedron’ Octahedron projection. ‘cylindricalea’ Cylindrical Equal Area projection.
        interp:
            Set interpolation method. Note: more complex interpolation methods require much more memory to run. Available methods: ‘near’ ‘nearest’ Nearest neighbour. ‘line’ ‘linear’ Bilinear interpolation. ‘lagrange9’ Lagrange9 interpolation. ‘cube’ ‘cubic’ Bicubic interpolation. ‘lanc’ ‘lanczos’ Lanczos interpolation. ‘sp16’ ‘spline16’ Spline16 interpolation. ‘gauss’ ‘gaussian’ Gaussian interpolation. ‘mitchell’ Mitchell interpolation. Default value is ‘line’.
        w:
            Set the output video resolution. Default resolution depends on formats.
        h:
            Set the output video resolution. Default resolution depends on formats.
        in_stereo:
            Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        out_stereo:
            Set the input/output stereo format. ‘2d’ 2D mono ‘sbs’ Side by side ‘tb’ Top bottom Default value is ‘2d’ for input and output format.
        yaw:
            Set rotation for the output video. Values in degrees.
        pitch:
            Set rotation for the output video. Values in degrees.
        roll:
            Set rotation for the output video. Values in degrees.
        rorder:
            Set rotation order for the output video. Choose one item for each position. ‘y, Y’ yaw ‘p, P’ pitch ‘r, R’ roll Default value is ‘ypr’.
        h_flip:
            Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        v_flip:
            Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        d_flip:
            Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
        ih_flip:
            Set if input video is flipped horizontally/vertically. Boolean values.
        iv_flip:
            Set if input video is flipped horizontally/vertically. Boolean values.
        in_trans:
            Set if input video is transposed. Boolean value, by default disabled.
        out_trans:
            Set if output video needs to be transposed. Boolean value, by default disabled.
        h_offset:
            Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        v_offset:
            Set output horizontal/vertical off-axis offset. Default is set to 0. Allowed range is from -1 to 1.
        alpha_mask:
            Build mask in alpha plane for all unmapped pixels by marking them fully transparent. Boolean value, by default disabled.
        reset_rot:
            Reset rotation of output video. Boolean value, by default disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#v360

        """
        return FilterNode(
            *[self],
            name="v360",
            kwargs={
                "input": input,
                "output": output,
                "interp": interp,
                "w": w,
                "h": h,
                "in_stereo": in_stereo,
                "out_stereo": out_stereo,
                "yaw": yaw,
                "pitch": pitch,
                "roll": roll,
                "rorder": rorder,
                "h_flip": h_flip,
                "v_flip": v_flip,
                "d_flip": d_flip,
                "ih_flip": ih_flip,
                "iv_flip": iv_flip,
                "in_trans": in_trans,
                "out_trans": out_trans,
                "h_offset": h_offset,
                "v_offset": v_offset,
                "alpha_mask": alpha_mask,
                "reset_rot": reset_rot,
                **kwargs,
            }
        ).stream()

    def vaguedenoiser(
        self,
        *,
        threshold: float = None,
        method: str = None,
        nsteps: int = None,
        percent: int = None,
        planes: list[str],
        type: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.270 vaguedenoiser Apply a wavelet based denoiser. It transforms each frame from the video input into the wavelet domain, using Cohen-Daubechies-Feauveau 9/7. Then it applies some filtering to the obtained coefficients. It does an inverse wavelet transform after. Due to wavelet properties, it should give a nice smoothed result, and reduced noise, without blurring picture features. This filter accepts the following options:

        Parameters:
        ----------
        threshold:
            The filtering strength. The higher, the more filtered the video will be. Hard thresholding can use a higher threshold than soft thresholding before the video looks overfiltered. Default value is 2.
        method:
            The filtering method the filter will use. It accepts the following values: ‘hard’ All values under the threshold will be zeroed. ‘soft’ All values under the threshold will be zeroed. All values above will be reduced by the threshold. ‘garrote’ Scales or nullifies coefficients - intermediary between (more) soft and (less) hard thresholding. Default is garrote.
        nsteps:
            Number of times, the wavelet will decompose the picture. Picture can’t be decomposed beyond a particular point (typically, 8 for a 640x480 frame - as 2^9 = 512 > 480). Valid values are integers between 1 and 32. Default value is 6.
        percent:
            Partial of full denoising (limited coefficients shrinking), from 0 to 100. Default value is 85.
        planes:
            A list of the planes to process. By default all planes are processed.
        type:
            The threshold type the filter will use. It accepts the following values: ‘universal’ Threshold used is same for all decompositions. ‘bayes’ Threshold used depends also on each decomposition coefficients. Default is universal.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vaguedenoiser

        """
        return FilterNode(
            *[self],
            name="vaguedenoiser",
            kwargs={
                "threshold": threshold,
                "method": method,
                "nsteps": nsteps,
                "percent": percent,
                "planes": planes,
                "type": type,
                **kwargs,
            }
        ).stream()

    def varblur(
        self, *, min_r: int = None, max_r: int = None, planes: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.271 varblur Apply variable blur filter by using 2nd video stream to set blur radius. The 2nd stream must have the same dimensions. This filter accepts the following options: The varblur filter also supports the framesync options.

        Parameters:
        ----------
        min_r:
            Set min allowed radius. Allowed range is from 0 to 254. Default is 0.
        max_r:
            Set max allowed radius. Allowed range is from 1 to 255. Default is 8.
        planes:
            Set which planes to process. By default, all are used.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#varblur

        """
        return FilterNode(
            *[self], name="varblur", kwargs={"min_r": min_r, "max_r": max_r, "planes": planes, **kwargs}
        ).stream()

    def vectorscope(
        self,
        *,
        mode: str = None,
        x: int = None,
        y: int = None,
        intensity: float,
        envelope: str = None,
        graticule: str,
        opacity: float,
        flags: list[str],
        bgopacity: float,
        lthreshold: float = None,
        hthreshold: float = None,
        colorspace: str = None,
        tint0: float = None,
        tint1: float = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.272 vectorscope Display 2 color component values in the two dimensional graph (which is called a vectorscope). This filter accepts the following options:

        Parameters:
        ----------
        mode:
            Set vectorscope mode. It accepts the following values: ‘gray’ ‘tint’ Gray values are displayed on graph, higher brightness means more pixels have same component color value on location in graph. This is the default mode. ‘color’ Gray values are displayed on graph. Surrounding pixels values which are not present in video frame are drawn in gradient of 2 color components which are set by option x and y. The 3rd color component is static. ‘color2’ Actual color components values present in video frame are displayed on graph. ‘color3’ Similar as color2 but higher frequency of same values x and y on graph increases value of another color component, which is luminance by default values of x and y. ‘color4’ Actual colors present in video frame are displayed on graph. If two different colors map to same position on graph then color with higher value of component not present in graph is picked. ‘color5’ Gray values are displayed on graph. Similar to color but with 3rd color component picked from radial gradient.
        x:
            Set which color component will be represented on X-axis. Default is 1.
        y:
            Set which color component will be represented on Y-axis. Default is 2.
        intensity:
            Set intensity, used by modes: gray, color, color3 and color5 for increasing brightness of color component which represents frequency of (X, Y) location in graph.
        envelope:
            ‘none’ No envelope, this is default. ‘instant’ Instant envelope, even darkest single pixel will be clearly highlighted. ‘peak’ Hold maximum and minimum values presented in graph over time. This way you can still spot out of range values without constantly looking at vectorscope. ‘peak+instant’ Peak and instant envelope combined together.
        graticule:
            Set what kind of graticule to draw. ‘none’ ‘green’ ‘color’ ‘invert’
        opacity:
            Set graticule opacity.
        flags:
            Set graticule flags. ‘white’ Draw graticule for white point. ‘black’ Draw graticule for black point. ‘name’ Draw color points short names.
        bgopacity:
            Set background opacity.
        lthreshold:
            Set low threshold for color component not represented on X or Y axis. Values lower than this value will be ignored. Default is 0. Note this value is multiplied with actual max possible value one pixel component can have. So for 8-bit input and low threshold value of 0.1 actual threshold is 0.1 * 255 = 25.
        hthreshold:
            Set high threshold for color component not represented on X or Y axis. Values higher than this value will be ignored. Default is 1. Note this value is multiplied with actual max possible value one pixel component can have. So for 8-bit input and high threshold value of 0.9 actual threshold is 0.9 * 255 = 230.
        colorspace:
            Set what kind of colorspace to use when drawing graticule. ‘auto’ ‘601’ ‘709’ Default is auto.
        tint0:
            Set color tint for gray/tint vectorscope mode. By default both options are zero. This means no tint, and output will remain gray.
        tint1:
            Set color tint for gray/tint vectorscope mode. By default both options are zero. This means no tint, and output will remain gray.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vectorscope

        """
        return FilterNode(
            *[self],
            name="vectorscope",
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
                **kwargs,
            }
        ).stream()

    def vflip(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.275 vflip Flip the input video vertically. For example, to vertically flip a video with ffmpeg: ffmpeg -i in.avi -vf "vflip" out.avi

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vflip

        """
        return FilterNode(*[self], name="vflip", kwargs={**kwargs}).stream()

    def vfrdet(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.276 vfrdet Detect variable frame rate video. This filter tries to detect if the input is variable or constant frame rate. At end it will output number of frames detected as having variable delta pts, and ones with constant delta pts. If there was frames with variable delta, than it will also show min, max and average delta encountered.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vfrdet

        """
        return FilterNode(*[self], name="vfrdet", kwargs={**kwargs}).stream()

    def vibrance(
        self,
        *,
        intensity: int = None,
        rbal: int = None,
        gbal: int = None,
        bbal: int = None,
        rlum: float,
        glum: float,
        blum: float,
        alternate: int = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.277 vibrance Boost or alter saturation. The filter accepts the following options:

        Parameters:
        ----------
        intensity:
            Set strength of boost if positive value or strength of alter if negative value. Default is 0. Allowed range is from -2 to 2.
        rbal:
            Set the red balance. Default is 1. Allowed range is from -10 to 10.
        gbal:
            Set the green balance. Default is 1. Allowed range is from -10 to 10.
        bbal:
            Set the blue balance. Default is 1. Allowed range is from -10 to 10.
        rlum:
            Set the red luma coefficient.
        glum:
            Set the green luma coefficient.
        blum:
            Set the blue luma coefficient.
        alternate:
            If intensity is negative and this is set to 1, colors will change, otherwise colors will be less saturated, more towards gray.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrance

        """
        return FilterNode(
            *[self],
            name="vibrance",
            kwargs={
                "intensity": intensity,
                "rbal": rbal,
                "gbal": gbal,
                "bbal": bbal,
                "rlum": rlum,
                "glum": glum,
                "blum": blum,
                "alternate": alternate,
                **kwargs,
            }
        ).stream()

    def vibrato(self, *, f: float = None, d: float = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.118 vibrato Sinusoidal phase modulation. The filter accepts the following options:

        Parameters:
        ----------
        f:
            Modulation frequency in Hertz. Range is 0.1 - 20000.0. Default value is 5.0 Hz.
        d:
            Depth of modulation as a percentage. Range is 0.0 - 1.0. Default value is 0.5.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vibrato

        """
        return FilterNode(*[self], name="vibrato", kwargs={"f": f, "d": d, **kwargs}).stream()

    def vidstabdetect(
        self,
        *,
        result: str = None,
        shakiness: int = None,
        accuracy: int = None,
        stepsize: int = None,
        mincontrast: float = None,
        tripod: int = None,
        show: int = None,
        fileformat: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.273 vidstabdetect Analyze video stabilization/deshaking. Perform pass 1 of 2, see vidstabtransform for pass 2. This filter generates a file with relative translation and rotation transform information about subsequent frames, which is then used by the vidstabtransform filter. To enable compilation of this filter you need to configure FFmpeg with --enable-libvidstab. This filter accepts the following options:

        Parameters:
        ----------
        result:
            Set the path to the file used to write the transforms information. Default value is transforms.trf.
        shakiness:
            Set how shaky the video is and how quick the camera is. It accepts an integer in the range 1-10, a value of 1 means little shakiness, a value of 10 means strong shakiness. Default value is 5.
        accuracy:
            Set the accuracy of the detection process. It must be a value in the range 1-15. A value of 1 means low accuracy, a value of 15 means high accuracy. Default value is 15.
        stepsize:
            Set stepsize of the search process. The region around minimum is scanned with 1 pixel resolution. Default value is 6.
        mincontrast:
            Set minimum contrast. Below this value a local measurement field is discarded. Must be a floating point value in the range 0-1. Default value is 0.3.
        tripod:
            Set reference frame number for tripod mode. If enabled, the motion of the frames is compared to a reference frame in the filtered stream, identified by the specified number. The idea is to compensate all movements in a more-or-less static scene and keep the camera view absolutely still. If set to 0, it is disabled. The frames are counted starting from 1.
        show:
            Show fields and transforms in the resulting frames. It accepts an integer in the range 0-2. Default value is 0, which disables any visualization.
        fileformat:
            Format for the transforms data file to be written. Acceptable values are ‘ascii’ Human-readable plain text ‘binary’ Binary format, roughly 40% smaller than ascii. (default)



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vidstabdetect

        """
        return FilterNode(
            *[self],
            name="vidstabdetect",
            kwargs={
                "result": result,
                "shakiness": shakiness,
                "accuracy": accuracy,
                "stepsize": stepsize,
                "mincontrast": mincontrast,
                "tripod": tripod,
                "show": show,
                "fileformat": fileformat,
                **kwargs,
            }
        ).stream()

    def vidstabtransform(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.274 vidstabtransform Video stabilization/deshaking: pass 2 of 2, see vidstabdetect for pass 1. Read a file with transform information for each frame and apply/compensate them. Together with the vidstabdetect filter this can be used to deshake videos. See also http://public.hronopik.de/vid.stab. It is important to also use the unsharp filter, see below. To enable compilation of this filter you need to configure FFmpeg with --enable-libvidstab.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vidstabtransform

        """
        return FilterNode(*[self], name="vidstabtransform", kwargs={**kwargs}).stream()

    def vif(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.278 vif Obtain the average VIF (Visual Information Fidelity) between two input videos. This filter takes two input videos. Both input videos must have the same resolution and pixel format for this filter to work correctly. Also it assumes that both inputs have the same number of frames, which are compared one by one. The obtained average VIF score is printed through the logging system. The filter stores the calculated VIF score of each frame. This filter also supports the framesync options. In the below example the input file main.mpg being processed is compared with the reference file ref.mpg. ffmpeg -i main.mpg -i ref.mpg -lavfi vif -f null -

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vif

        """
        return FilterNode(*[self], name="vif", kwargs={**kwargs}).stream()

    def vignette(
        self,
        *,
        angle: str = None,
        x0: str = None,
        y0: str = None,
        mode: str = None,
        eval: str = None,
        dither: int = None,
        aspect: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.279 vignette Make or reverse a natural vignetting effect. The filter accepts the following options:

        Parameters:
        ----------
        angle:
            Set lens angle expression as a number of radians. The value is clipped in the [0,PI/2] range. Default value: "PI/5"
        x0:
            Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        y0:
            Set center coordinates expressions. Respectively "w/2" and "h/2" by default.
        mode:
            Set forward/backward mode. Available modes are: ‘forward’ The larger the distance from the central point, the darker the image becomes. ‘backward’ The larger the distance from the central point, the brighter the image becomes. This can be used to reverse a vignette effect, though there is no automatic detection to extract the lens angle and other settings (yet). It can also be used to create a burning effect. Default value is ‘forward’.
        eval:
            Set evaluation mode for the expressions (angle, x0, y0). It accepts the following values: ‘init’ Evaluate expressions only once during the filter initialization. ‘frame’ Evaluate expressions for each incoming frame. This is way slower than the ‘init’ mode since it requires all the scalers to be re-computed, but it allows advanced dynamic expressions. Default value is ‘init’.
        dither:
            Set dithering to reduce the circular banding effects. Default is 1 (enabled).
        aspect:
            Set vignette aspect. This setting allows one to adjust the shape of the vignette. Setting this value to the SAR of the input will make a rectangular vignetting following the dimensions of the video. Default is 1/1.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vignette

        """
        return FilterNode(
            *[self],
            name="vignette",
            kwargs={
                "angle": angle,
                "x0": x0,
                "y0": y0,
                "mode": mode,
                "eval": eval,
                "dither": dither,
                "aspect": aspect,
                **kwargs,
            }
        ).stream()

    def virtualbass(self, *, cutoff: float = None, strength: float = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.119 virtualbass Apply audio Virtual Bass filter. This filter accepts stereo input and produce stereo with LFE (2.1) channels output. The newly produced LFE channel have enhanced virtual bass originally obtained from both stereo channels. This filter outputs front left and front right channels unchanged as available in stereo input. The filter accepts the following options:

        Parameters:
        ----------
        cutoff:
            Set the virtual bass cutoff frequency. Default value is 250 Hz. Allowed range is from 100 to 500 Hz.
        strength:
            Set the virtual bass strength. Allowed range is from 0.5 to 3. Default value is 3.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#virtualbass

        """
        return FilterNode(
            *[self], name="virtualbass", kwargs={"cutoff": cutoff, "strength": strength, **kwargs}
        ).stream()

    def vmafmotion(self, *, stats_file: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.280 vmafmotion Obtain the average VMAF motion score of a video. It is one of the component metrics of VMAF. The obtained average motion score is printed through the logging system. The filter accepts the following options: Example: ffmpeg -i ref.mpg -vf vmafmotion -f null -

        Parameters:
        ----------
        stats_file:
            If specified, the filter will use the named file to save the motion score of each frame with respect to the previous frame. When filename equals "-" the data is sent to standard output.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vmafmotion

        """
        return FilterNode(*[self], name="vmafmotion", kwargs={"stats_file": stats_file, **kwargs}).stream()

    def volume(
        self,
        *,
        volume: str = None,
        precision: str = None,
        replaygain: str = None,
        replaygain_preamp: float = None,
        replaygain_noclip: int = None,
        eval: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        8.120 volume Adjust the input audio volume. It accepts the following parameters: The volume expression can contain the following parameters. Note that when eval is set to ‘once’ only the sample_rate and tb variables are available, all other variables will evaluate to NAN.

        Parameters:
        ----------
        volume:
            Set audio volume expression. Output values are clipped to the maximum value. The output audio volume is given by the relation: output_volume = volume * input_volume The default value for volume is "1.0".
        precision:
            This parameter represents the mathematical precision. It determines which input sample formats will be allowed, which affects the precision of the volume scaling. fixed 8-bit fixed-point; this limits input sample format to U8, S16, and S32. float 32-bit floating-point; this limits input sample format to FLT. (default) double 64-bit floating-point; this limits input sample format to DBL.
        replaygain:
            Choose the behaviour on encountering ReplayGain side data in input frames. drop Remove ReplayGain side data, ignoring its contents (the default). ignore Ignore ReplayGain side data, but leave it in the frame. track Prefer the track gain, if present. album Prefer the album gain, if present.
        replaygain_preamp:
            Pre-amplification gain in dB to apply to the selected replaygain gain. Default value for replaygain_preamp is 0.0.
        replaygain_noclip:
            Prevent clipping by limiting the gain applied. Default value for replaygain_noclip is 1.
        eval:
            Set when the volume expression is evaluated. It accepts the following values: ‘once’ only evaluate expression once during the filter initialization, or when the ‘volume’ command is sent ‘frame’ evaluate expression for each incoming frame Default value is ‘once’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#volume

        """
        return FilterNode(
            *[self],
            name="volume",
            kwargs={
                "volume": volume,
                "precision": precision,
                "replaygain": replaygain,
                "replaygain_preamp": replaygain_preamp,
                "replaygain_noclip": replaygain_noclip,
                "eval": eval,
                **kwargs,
            }
        ).stream()

    def volumedetect(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        8.121 volumedetect Detect the volume of the input video. The filter has no parameters. It supports only 16-bit signed integer samples, so the input will be converted when needed. Statistics about the volume will be printed in the log when the input stream end is reached. In particular it will show the mean volume (root mean square), maximum volume (on a per-sample basis), and the beginning of a histogram of the registered volume values (from the maximum value to a cumulated 1/1000 of the samples). All volumes are in decibels relative to the maximum PCM value.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#volumedetect

        """
        return FilterNode(*[self], name="volumedetect", kwargs={**kwargs}).stream()

    def vstack(self, *, inputs: int = None, shortest: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.281 vstack Stack input videos vertically. All streams must be of same pixel format and of same width. Note that this filter is faster than using overlay and pad filter to create same output. The filter accepts the following options:

        Parameters:
        ----------
        inputs:
            Set number of input streams. Default is 2.
        shortest:
            If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#vstack

        """
        return FilterNode(*[self], name="vstack", kwargs={"inputs": inputs, "shortest": shortest, **kwargs}).stream()

    def w3fdif(
        self, *, filter: str = None, mode: str = None, parity: str = None, deint: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.282 w3fdif Deinterlace the input video ("w3fdif" stands for "Weston 3 Field Deinterlacing Filter"). Based on the process described by Martin Weston for BBC R&D, and implemented based on the de-interlace algorithm written by Jim Easterbrook for BBC R&D, the Weston 3 field deinterlacing filter uses filter coefficients calculated by BBC R&D. This filter uses field-dominance information in frame to decide which of each pair of fields to place first in the output. If it gets it wrong use setfield filter before w3fdif filter. There are two sets of filter coefficients, so called "simple" and "complex". Which set of filter coefficients is used can be set by passing an optional parameter:

        Parameters:
        ----------
        filter:
            Set the interlacing filter coefficients. Accepts one of the following values: ‘simple’ Simple filter coefficient set. ‘complex’ More-complex filter coefficient set. Default value is ‘complex’.
        mode:
            The interlacing mode to adopt. It accepts one of the following values: frame Output one frame for each frame. field Output one frame for each field. The default value is field.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: tff Assume the top field is first. bff Assume the bottom field is first. auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: ‘all’ Deinterlace all frames, ‘interlaced’ Only deinterlace frames marked as interlaced. Default value is ‘all’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#w3fdif

        """
        return FilterNode(
            *[self], name="w3fdif", kwargs={"filter": filter, "mode": mode, "parity": parity, "deint": deint, **kwargs}
        ).stream()

    def waveform(
        self,
        *,
        mode: str = None,
        intensity: float = None,
        mirror: int = None,
        display: str = None,
        components: int = None,
        envelope: str = None,
        filter: str = None,
        graticule: str,
        opacity: float,
        flags: list[str],
        scale: str = None,
        bgopacity: float,
        tint0: str,
        tint1: str,
        fitmode: str = None,
        input: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.283 waveform Video waveform monitor. The waveform monitor plots color component intensity. By default luma only. Each column of the waveform corresponds to a column of pixels in the source video. It accepts the following options:

        Parameters:
        ----------
        mode:
            Can be either row, or column. Default is column. In row mode, the graph on the left side represents color component value 0 and the right side represents value = 255. In column mode, the top side represents color component value = 0 and bottom side represents value = 255.
        intensity:
            Set intensity. Smaller values are useful to find out how many values of the same luminance are distributed across input rows/columns. Default value is 0.04. Allowed range is [0, 1].
        mirror:
            Set mirroring mode. 0 means unmirrored, 1 means mirrored. In mirrored mode, higher values will be represented on the left side for row mode and at the top for column mode. Default is 1 (mirrored).
        display:
            Set display mode. It accepts the following values: ‘overlay’ Presents information identical to that in the parade, except that the graphs representing color components are superimposed directly over one another. This display mode makes it easier to spot relative differences or similarities in overlapping areas of the color components that are supposed to be identical, such as neutral whites, grays, or blacks. ‘stack’ Display separate graph for the color components side by side in row mode or one below the other in column mode. ‘parade’ Display separate graph for the color components side by side in column mode or one below the other in row mode. Using this display mode makes it easy to spot color casts in the highlights and shadows of an image, by comparing the contours of the top and the bottom graphs of each waveform. Since whites, grays, and blacks are characterized by exactly equal amounts of red, green, and blue, neutral areas of the picture should display three waveforms of roughly equal width/height. If not, the correction is easy to perform by making level adjustments the three waveforms. Default is stack.
        components:
            Set which color components to display. Default is 1, which means only luma or red color component if input is in RGB colorspace. If is set for example to 7 it will display all 3 (if) available color components.
        envelope:
            ‘none’ No envelope, this is default. ‘instant’ Instant envelope, minimum and maximum values presented in graph will be easily visible even with small step value. ‘peak’ Hold minimum and maximum values presented in graph across time. This way you can still spot out of range values without constantly looking at waveforms. ‘peak+instant’ Peak and instant envelope combined together.
        filter:
            ‘lowpass’ No filtering, this is default. ‘flat’ Luma and chroma combined together. ‘aflat’ Similar as above, but shows difference between blue and red chroma. ‘xflat’ Similar as above, but use different colors. ‘yflat’ Similar as above, but again with different colors. ‘chroma’ Displays only chroma. ‘color’ Displays actual color value on waveform. ‘acolor’ Similar as above, but with luma showing frequency of chroma values.
        graticule:
            Set which graticule to display. ‘none’ Do not display graticule. ‘green’ Display green graticule showing legal broadcast ranges. ‘orange’ Display orange graticule showing legal broadcast ranges. ‘invert’ Display invert graticule showing legal broadcast ranges.
        opacity:
            Set graticule opacity.
        flags:
            Set graticule flags. ‘numbers’ Draw numbers above lines. By default enabled. ‘dots’ Draw dots instead of lines.
        scale:
            Set scale used for displaying graticule. ‘digital’ ‘millivolts’ ‘ire’ Default is digital.
        bgopacity:
            Set background opacity.
        tint0:
            Set tint for output. Only used with lowpass filter and when display is not overlay and input pixel formats are not RGB.
        tint1:
            Set tint for output. Only used with lowpass filter and when display is not overlay and input pixel formats are not RGB.
        fitmode:
            Set sample aspect ratio of video output frames. Can be used to configure waveform so it is not streched too much in one of directions. ‘none’ Set sample aspect ration to 1/1. ‘size’ Set sample aspect ratio to match input size of video Default is ‘none’.
        input:
            Set input formats for filter to pick from. Can be ‘all’, for selecting from all available formats, or ‘first’, for selecting first available format. Default is ‘first’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#waveform

        """
        return FilterNode(
            *[self],
            name="waveform",
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
                **kwargs,
            }
        ).stream()

    def weave(self, *, first_field: str, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.284 weave, doubleweave The weave takes a field-based video input and join each two sequential fields into single frame, producing a new double height clip with half the frame rate and half the frame count. The doubleweave works same as weave but without halving frame rate and frame count. It accepts the following option:

        Parameters:
        ----------
        first_field:
            Set first field. Available values are: ‘top, t’ Set the frame as top-field-first. ‘bottom, b’ Set the frame as bottom-field-first.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave

        """
        return FilterNode(*[self], name="weave", kwargs={"first_field": first_field, **kwargs}).stream()

    def xbr(self, *, n: int = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.285 xbr Apply the xBR high-quality magnification filter which is designed for pixel art. It follows a set of edge-detection rules, see https://forums.libretro.com/t/xbr-algorithm-tutorial/123. It accepts the following option:

        Parameters:
        ----------
        n:
            Set the scaling dimension: 2 for 2xBR, 3 for 3xBR and 4 for 4xBR. Default is 3.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xbr

        """
        return FilterNode(*[self], name="xbr", kwargs={"n": n, **kwargs}).stream()

    def xcorrelate(self, *, planes: str, secondary: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.286 xcorrelate Apply normalized cross-correlation between first and second input video stream. Second input video stream dimensions must be lower than first input video stream. The filter accepts the following options: The xcorrelate filter also supports the framesync options.

        Parameters:
        ----------
        planes:
            Set which planes to process.
        secondary:
            Set which secondary video frames will be processed from second input video stream, can be first or all. Default is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xcorrelate

        """
        return FilterNode(
            *[self], name="xcorrelate", kwargs={"planes": planes, "secondary": secondary, **kwargs}
        ).stream()

    def xfade(
        self,
        *,
        transition: str = None,
        duration: float = None,
        offset: float = None,
        expr: str,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.287 xfade Apply cross fade from one input video stream to another input video stream. The cross fade is applied for specified duration. Both inputs must be constant frame-rate and have the same resolution, pixel format, frame rate and timebase. The filter accepts the following options:

        Parameters:
        ----------
        transition:
            Set one of available transition effects: ‘custom’ ‘fade’ ‘wipeleft’ ‘wiperight’ ‘wipeup’ ‘wipedown’ ‘slideleft’ ‘slideright’ ‘slideup’ ‘slidedown’ ‘circlecrop’ ‘rectcrop’ ‘distance’ ‘fadeblack’ ‘fadewhite’ ‘radial’ ‘smoothleft’ ‘smoothright’ ‘smoothup’ ‘smoothdown’ ‘circleopen’ ‘circleclose’ ‘vertopen’ ‘vertclose’ ‘horzopen’ ‘horzclose’ ‘dissolve’ ‘pixelize’ ‘diagtl’ ‘diagtr’ ‘diagbl’ ‘diagbr’ ‘hlslice’ ‘hrslice’ ‘vuslice’ ‘vdslice’ ‘hblur’ ‘fadegrays’ ‘wipetl’ ‘wipetr’ ‘wipebl’ ‘wipebr’ ‘squeezeh’ ‘squeezev’ ‘zoomin’ ‘fadefast’ ‘fadeslow’ ‘hlwind’ ‘hrwind’ ‘vuwind’ ‘vdwind’ ‘coverleft’ ‘coverright’ ‘coverup’ ‘coverdown’ ‘revealleft’ ‘revealright’ ‘revealup’ ‘revealdown’ Default transition effect is fade.
        duration:
            Set cross fade duration in seconds. Range is 0 to 60 seconds. Default duration is 1 second.
        offset:
            Set cross fade start relative to first input stream in seconds. Default offset is 0.
        expr:
            Set expression for custom transition effect. The expressions can use the following variables and functions: X Y The coordinates of the current sample. W H The width and height of the image. P Progress of transition effect. PLANE Currently processed plane. A Return value of first input at current location and plane. B Return value of second input at current location and plane. a0(x, y) a1(x, y) a2(x, y) a3(x, y) Return the value of the pixel at location (x,y) of the first/second/third/fourth component of first input. b0(x, y) b1(x, y) b2(x, y) b3(x, y) Return the value of the pixel at location (x,y) of the first/second/third/fourth component of second input.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xfade

        """
        return FilterNode(
            *[self],
            name="xfade",
            kwargs={"transition": transition, "duration": duration, "offset": offset, "expr": expr, **kwargs}
        ).stream()

    def xmedian(
        self, *, inputs: int = None, planes: int = None, percentile: float = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.288 xmedian Pick median pixels from several input videos. The filter accepts the following options:

        Parameters:
        ----------
        inputs:
            Set number of inputs. Default is 3. Allowed range is from 3 to 255. If number of inputs is even number, than result will be mean value between two median values.
        planes:
            Set which planes to filter. Default value is 15, by which all planes are processed.
        percentile:
            Set median percentile. Default value is 0.5. Default value of 0.5 will pick always median values, while 0 will pick minimum values, and 1 maximum values.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xmedian

        """
        return FilterNode(
            *[self], name="xmedian", kwargs={"inputs": inputs, "planes": planes, "percentile": percentile, **kwargs}
        ).stream()

    def xstack(
        self, *, inputs: int = None, layout: str, grid: str, shortest: int = None, fill: str, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.289 xstack Stack video inputs into custom layout. All streams must be of same pixel format. The filter accepts the following options:

        Parameters:
        ----------
        inputs:
            Set number of input streams. Default is 2.
        layout:
            Specify layout of inputs. This option requires the desired layout configuration to be explicitly set by the user. This sets position of each video input in output. Each input is separated by ’|’. The first number represents the column, and the second number represents the row. Numbers start at 0 and are separated by ’_’. Optionally one can use wX and hX, where X is video input from which to take width or height. Multiple values can be used when separated by ’+’. In such case values are summed together. Note that if inputs are of different sizes gaps may appear, as not all of the output video frame will be filled. Similarly, videos can overlap each other if their position doesn’t leave enough space for the full frame of adjoining videos. For 2 inputs, a default layout of 0_0|w0_0 (equivalent to grid=2x1) is set. In all other cases, a layout or a grid must be set by the user. Either grid or layout can be specified at a time. Specifying both will result in an error.
        grid:
            Specify a fixed size grid of inputs. This option is used to create a fixed size grid of the input streams. Set the grid size in the form COLUMNSxROWS. There must be ROWS * COLUMNS input streams and they will be arranged as a grid with ROWS rows and COLUMNS columns. When using this option, each input stream within a row must have the same height and all the rows must have the same width. If grid is set, then inputs option is ignored and is implicitly set to ROWS * COLUMNS. For 2 inputs, a default grid of 2x1 (equivalent to layout=0_0|w0_0) is set. In all other cases, a layout or a grid must be set by the user. Either grid or layout can be specified at a time. Specifying both will result in an error.
        shortest:
            If set to 1, force the output to terminate when the shortest input terminates. Default value is 0.
        fill:
            If set to valid color, all unused pixels will be filled with that color. By default fill is set to none, so it is disabled.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#xstack

        """
        return FilterNode(
            *[self],
            name="xstack",
            kwargs={"inputs": inputs, "layout": layout, "grid": grid, "shortest": shortest, "fill": fill, **kwargs}
        ).stream()

    def yadif(self, *, mode: str = None, parity: str = None, deint: str = None, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.290 yadif Deinterlace the input video ("yadif" means "yet another deinterlacing filter"). It accepts the following parameters:

        Parameters:
        ----------
        mode:
            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. 2, send_frame_nospatial Like send_frame, but it skips the spatial interlacing check. 3, send_field_nospatial Like send_field, but it skips the spatial interlacing check. The default value is send_frame.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yadif

        """
        return FilterNode(
            *[self], name="yadif", kwargs={"mode": mode, "parity": parity, "deint": deint, **kwargs}
        ).stream()

    def yadif_cuda(
        self, *, mode: str = None, parity: str = None, deint: str = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.291 yadif_cuda Deinterlace the input video using the yadif algorithm, but implemented in CUDA so that it can work as part of a GPU accelerated pipeline with nvdec and/or nvenc. It accepts the following parameters:

        Parameters:
        ----------
        mode:
            The interlacing mode to adopt. It accepts one of the following values: 0, send_frame Output one frame for each frame. 1, send_field Output one frame for each field. 2, send_frame_nospatial Like send_frame, but it skips the spatial interlacing check. 3, send_field_nospatial Like send_field, but it skips the spatial interlacing check. The default value is send_frame.
        parity:
            The picture field parity assumed for the input interlaced video. It accepts one of the following values: 0, tff Assume the top field is first. 1, bff Assume the bottom field is first. -1, auto Enable automatic detection of field parity. The default value is auto. If the interlacing is unknown or the decoder does not export this information, top field first will be assumed.
        deint:
            Specify which frames to deinterlace. Accepts one of the following values: 0, all Deinterlace all frames. 1, interlaced Only deinterlace frames marked as interlaced. The default value is all.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yadif_005fcuda

        """
        return FilterNode(
            *[self], name="yadif_cuda", kwargs={"mode": mode, "parity": parity, "deint": deint, **kwargs}
        ).stream()

    def yaepblur(
        self, *, radius: int = None, planes: str = None, sigma: int = None, **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.292 yaepblur Apply blur filter while preserving edges ("yaepblur" means "yet another edge preserving blur filter"). The algorithm is described in "J. S. Lee, Digital image enhancement and noise filtering by use of local statistics, IEEE Trans. Pattern Anal. Mach. Intell. PAMI-2, 1980." It accepts the following parameters:

        Parameters:
        ----------
        radius:
            Set the window radius. Default value is 3.
        planes:
            Set which planes to filter. Default is only the first plane.
        sigma:
            Set blur strength. Default value is 128.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#yaepblur

        """
        return FilterNode(
            *[self], name="yaepblur", kwargs={"radius": radius, "planes": planes, "sigma": sigma, **kwargs}
        ).stream()

    def zoompan(
        self,
        *,
        zoom: float = None,
        x: float = None,
        y: float = None,
        d: float = None,
        s: str = None,
        fps: str = None,
        **kwargs: dict[str, Any]
    ) -> "Stream":
        """
        11.293 zoompan Apply Zoom & Pan effect. This filter accepts the following options: Each expression can contain the following constants:

        Parameters:
        ----------
        zoom:
            Set the zoom expression. Range is 1-10. Default is 1.
        x:
            Set the x and y expression. Default is 0.
        y:
            Set the x and y expression. Default is 0.
        d:
            Set the duration expression in number of frames. This sets for how many number of frames effect will last for single input image. Default is 90.
        s:
            Set the output image size, default is ’hd720’.
        fps:
            Set the output frame rate, default is ’25’.



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zoompan

        """
        return FilterNode(
            *[self], name="zoompan", kwargs={"zoom": zoom, "x": x, "y": y, "d": d, "s": s, "fps": fps, **kwargs}
        ).stream()

    def zscale(self, **kwargs: dict[str, Any]) -> "Stream":
        """
        11.294 zscale Scale (resize) the input video, using the z.lib library: https://github.com/sekrit-twc/zimg. To enable compilation of this filter, you need to configure FFmpeg with --enable-libzimg. The zscale filter forces the output display aspect ratio to be the same as the input, by changing the output sample aspect ratio. If the input image format is different from the format requested by the next filter, the zscale filter will convert the input to the requested format.

        Parameters:
        ----------



        Example usage:
        --------------

        Ref: https://ffmpeg.org/ffmpeg-filters.html#zscale

        """
        return FilterNode(*[self], name="zscale", kwargs={**kwargs}).stream()
