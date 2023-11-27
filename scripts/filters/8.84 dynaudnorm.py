from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def dynaudnorm(
    stream: Stream,
    framelen: Optional[float] = 500,
    gausssize: Optional[int] = 31,
    peak: Optional[float] = 0.95,
    maxgain: Optional[float] = 10.0,
    targetrms: Optional[float] = 0.0,
    coupling: bool = True,
    correctdc: bool = False,
    altboundary: bool = False,
    compress: Optional[float] = 0.0,
    threshold: Optional[float] = 0.0,
    channels: Optional[str] = None,
    overlap: Optional[float] = 0.0,
    curve: Optional[str] = None,
) -> Stream:
    """
    Dynamic Audio Normalizer.

    This filter applies a certain amount of gain to the input audio in order to bring its peak magnitude to a target level (e.g. 0 dBFS). However, in contrast to more "simple" normalization algorithms, the Dynamic Audio Normalizer *dynamically* re-adjusts the gain factor to the input audio. This allows for applying extra gain to the "quiet" sections of the audio while avoiding distortions or clipping the "loud" sections. In other words: The Dynamic Audio Normalizer will "even out" the volume of quiet and loud sections, in the sense that the volume of each section is brought to the same target level. Note, however, that the Dynamic Audio Normalizer achieves this goal *without* applying "dynamic range compressing". It will retain 100% of the dynamic range *within* each section of the audio file.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    framelen : float, optional
        Set the frame length in milliseconds. In the range from 10 to 8000 milliseconds.
        Default is 500 milliseconds.
        The Dynamic Audio Normalizer processes the input audio in small chunks, referred to as frames. This is required because a peak magnitude has no meaning for just a single sample value. Instead, we need to determine the peak magnitude for a contiguous sequence of sample values. While a "standard" normalizer would simply use the peak magnitude of the complete file, the Dynamic Audio Normalizer determines the peak magnitude individually for each frame. The length of a frame is specified in milliseconds. By default, the Dynamic Audio Normalizer uses a frame length of 500 milliseconds, which has been found to give good results with most files. Note that the exact frame length, in number of samples, will be determined automatically based on the sampling rate of the individual input audio file.
    gausssize : int, optional
        Set the Gaussian filter window size. In the range from 3 to 301, must be an odd number.
        Default is 31.
        Probably the most important parameter of the Dynamic Audio Normalizer is the window size of the Gaussian smoothing filter. The filter's window size is specified in frames, centered around the current frame. For the sake of simplicity, this must be an odd number. Consequently, the default value of 31 takes into account the current frame, as well as the 15 preceding frames and the 15 subsequent frames. Using a larger window results in a stronger smoothing effect and thus in less gain variation, i.e. slower gain adaptation. Conversely, using a smaller window results in a weaker smoothing effect and thus in more gain variation, i.e. faster gain adaptation. In other words, the more you increase this value, the more the Dynamic Audio Normalizer will behave like a "traditional" normalization filter. On the contrary, the more you decrease this value, the more the Dynamic Audio Normalizer will behave like a dynamic range compressor.
    peak : float, optional
        Set the target peak value. This specifies the highest permissible magnitude level for the normalized audio input. This filter will try to approach the target peak magnitude as closely as possible, but at the same time, it also makes sure that the normalized signal will never exceed the peak magnitude. A frame's maximum local gain factor is imposed directly by the target peak magnitude. The default value is 0.95 and thus leaves a headroom of 5%*. It is not recommended to go above this value.
    maxgain : float, optional
        Set the maximum gain factor. In the range from 1.0 to 100.0. Default is 10.0.
        The Dynamic Audio Normalizer determines the maximum possible (local) gain factor for each input frame, i.e. the maximum gain factor that does not result in clipping or distortion. The maximum gain factor is determined by the frame's highest magnitude sample. However, the Dynamic Audio Normalizer additionally bounds the frame's maximum gain factor by a predetermined (global) maximum gain factor. This is done in order to avoid excessive gain factors in "silent" or almost silent frames. By default, the maximum gain factor is 10.0. For most inputs, the default value should be sufficient, and it usually is not recommended to increase this value. Though, for input with an extremely low overall volume level, it may be necessary to allow even higher gain factors. Note, however, that the Dynamic Audio Normalizer does not simply apply a "hard" threshold (i.e. cut off values above the threshold). Instead, a "sigmoid" threshold function will be applied. This way, the gain factors will smoothly approach the threshold value, but never exceed that value.
    targetrms : float, optional
        Set the target RMS. In the range from 0.0 to 1.0. Default is 0.0 - disabled.
        By default, the Dynamic Audio Normalizer performs "peak" normalization. This means that the maximum local gain factor for each frame is defined (only) by the frame's highest magnitude sample. This way, the samples can be amplified as much as possible without exceeding the maximum signal level, i.e. without clipping. Optionally, however, the Dynamic Audio Normalizer can also take into account the frame's root mean square, abbreviated RMS. In electrical engineering, the RMS is commonly used to determine the power of a time-varying signal. It is therefore considered that the RMS is a better approximation of the "perceived loudness" than just looking at the signal's peak magnitude. Consequently, by adjusting all frames to a constant RMS value, a uniform "perceived loudness" can be established. If a target RMS value has been specified, a frame's local gain factor is defined as the factor that would result in exactly that RMS value. Note, however, that the maximum local gain factor is still restricted by the frame's highest magnitude sample, in order to prevent clipping.
    coupling : bool, optional
        Enable channels coupling. By default is enabled.
        By default, the Dynamic Audio Normalizer will amplify all channels by the same amount. This means the same gain factor will be applied to all channels, i.e. the maximum possible gain factor is determined by the "loudest" channel. However, in some recordings, it may happen that the volume of the different channels is uneven, e.g. one channel may be "quieter" than the other one(s). In this case, this option can be used to disable the channel coupling. This way, the gain factor will be determined independently for each channel, depending only on the individual channel's highest magnitude sample. This allows for harmonizing the volume of the different channels.
    correctdc : bool, optional
        Enable DC bias correction. By default is disabled.
        An audio signal (in the time domain) is a sequence of sample values. In the Dynamic Audio Normalizer, these sample values are represented in the -1.0 to 1.0 range, regardless of the original input format. Normally, the audio signal, or "waveform", should be centered around the zero point. That means if we calculate the mean value of all samples in a file, or in a single frame, then the result should be 0.0 or at least very close to that value. If, however, there is a significant deviation of the mean value from 0.0, in either positive or negative direction, this is referred to as a DC bias or DC offset. Since a DC bias is clearly undesirable, the Dynamic Audio Normalizer provides optional DC bias correction.
        With DC bias correction enabled, the Dynamic Audio Normalizer will determine the mean value, or "DC correction" offset, of each input frame and subtract that value from all of the frame's sample values which ensures those samples are centered around 0.0 again. Also, in order to avoid "gaps" at the frame boundaries, the DC correction offset values will be interpolated smoothly between neighbouring frames.
    altboundary : bool, optional
        Enable alternative boundary mode. By default is disabled.
        The Dynamic Audio Normalizer takes into account a certain neighbourhood around each frame. This includes the preceding frames as well as the subsequent frames. However, for the "boundary" frames, located at the very beginning and at the very end of the audio file, not all neighbouring frames are available. In particular, for the first few frames in the audio file, the preceding frames are not known. And, similarly, for the last few frames in the audio file, the subsequent frames are not known. Thus, the question arises which gain factors should be assumed for the missing frames in the "boundary" region. The Dynamic Audio Normalizer implements two modes to deal with this situation. The default boundary mode assumes a gain factor of exactly 1.0 for the missing frames, resulting in a smooth "fade in" and "fade out" at the beginning and at the end of the input, respectively.
    compress : float, optional
        Set the compress factor. In the range from 0.0 to 30.0. Default is 0.0.
        By default, the Dynamic Audio Normalizer does not apply "traditional" compression. This means that signal peaks will not be pruned and thus the full dynamic range will be retained within each local neighbourhood. However, in some cases, it may be desirable to combine the Dynamic Audio Normalizer's normalization algorithm with a more "traditional" compression.
        For this purpose, the Dynamic Audio Normalizer provides an optional compression (thresholding) function. If (and only if) the compression feature is enabled, all input frames will be processed by a soft knee thresholding function prior to the actual normalization process. Put simply, the thresholding function is going to prune all samples whose magnitude exceeds a certain threshold value. However, the Dynamic Audio Normalizer does not simply apply a fixed threshold value. Instead, the threshold value will be adjusted for each individual frame.
        In general, smaller parameters result in stronger compression, and vice versa. Values below 3.0 are not recommended because audible distortion may appear.
    threshold : float, optional
        Set the target threshold value. This specifies the lowest permissible magnitude level for the audio input which will be normalized. If input frame volume is above this value frame will be normalized. Otherwise frame may not be normalized at all. The default value is set to 0, which means all input frames will be normalized. This option is mostly useful if digital noise is not wanted to be amplified.
    channels : str, optional
        Specify which channels to filter, by default all available channels are filtered.
    overlap : float, optional
        Specify the overlap for frames. If set to 0 (default) no frame overlapping is done. Using > 0 and < 1 values will make less conservative gain adjustments, like when framelen option is set to a smaller value, if framelen option value is compensated for non-zero overlap then gain adjustments will be smoother across time compared to the zero overlap case.
    curve : str, optional
        Specify the peak mapping curve expression that is going to be used when calculating the gain applied to frames. The max output frame gain will still be limited by other options mentioned previously for this filter.

    Returns:
    -------
    Stream
        The output stream after applying the dynamic audio normalization filter.

    Example usage:
    --------------
    stream.dynaudnorm(
        framelen=500,
        gausssize=31,
        peak=0.95,
        maxgain=10.0,
        targetrms=0.0,
        coupling=True,
        correctdc=False,
        altboundary=False,
        compress=0.0,
        threshold=0.0,
        channels=None,
        overlap=0.0,
        curve=None,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm
    """
    return FilterNode(
        stream,
        dynaudnorm.__name__,
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
        },
    ).stream()
