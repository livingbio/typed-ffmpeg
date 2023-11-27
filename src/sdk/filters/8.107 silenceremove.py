from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def silenceremove(
    stream: Stream,
    start_periods: int = 0,
    start_duration: float = 0,
    start_threshold: float = 0,
    start_silence: float = 0,
    start_mode: str = Literal["any", "all"],
    stop_periods: int = 0,
    stop_duration: float = 0,
    stop_threshold: float = 0,
    stop_silence: float = 0,
    stop_mode: str = Literal["any", "all"],
    detection: str = Literal["avg", "rms", "peak", "median", "ptp", "dev"],
    window: float = 0.02,
    timestamp: str = Literal["write", "copy"],
) -> Stream:
    """
    Remove silence from the beginning, middle or end of the audio.

    The filter accepts the following options:

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    start_periods : int, optional
        This value is used to indicate if audio should be trimmed at the beginning of
        the audio. A value of zero indicates no silence should be trimmed from the
        beginning. When specifying a non-zero value, it trims audio up until it
        finds non-silence. Normally, when trimming silence from the beginning of audio,
        the start_periods will be 1 but it can be increased to higher values to trim
        all audio up to a specific count of non-silence periods. Default value is 0.
    start_duration : float, optional
        Specify the amount of time that non-silence must be detected before it stops
        trimming audio. By increasing the duration, bursts of noises can be treated
        as silence and trimmed off. Default value is 0.
    start_threshold : float, optional
        This indicates what sample value should be treated as silence. For digital
        audio, a value of 0 may be fine but for audio recorded from analog,
        you may wish to increase the value to account for background noise.
        Can be specified in dB (in case "dB" is appended to the specified value)
        or amplitude ratio. Default value is 0.
    start_silence : float, optional
        Specify the maximum duration of silence at the beginning that will be kept after
        trimming. Default is 0, which is equal to trimming all samples detected
        as silence.
    start_mode : str, optional
        Specify mode of detection of silence end at the start of multi-channel audio.
        Can be "any" or "all". Default is "any". With "any", any sample from any channel
        that is detected as non-silence will trigger end of silence trimming at the start
        of the audio stream. With "all", only if every sample from every channel is
        detected as non-silence will trigger end of silence trimming at the start
        of the audio stream.
    stop_periods : int, optional
        Set the count for trimming silence from the end of audio. When specifying a
        positive value, it trims audio after it finds the specified silence period.
        To remove silence from the middle of a file, specify a stop_periods that is
        negative. This value is then treated as a positive value and is used to indicate
        the effect should restart processing as specified by stop_periods, making it
        suitable for removing periods of silence in the middle of the audio.
        Default value is 0.
    stop_duration : float, optional
        Specify a duration of silence that must exist before audio is not copied any more.
        By specifying a higher duration, silence that is wanted can be left in the audio.
        Default value is 0.
    stop_threshold : float, optional
        This is the same as start_threshold but for trimming silence from
        the end of audio. Can be specified in dB (in case "dB" is appended to the
        specified value) or amplitude ratio. Default value is 0.
    stop_silence : float, optional
        Specify the maximum duration of silence at the end that will be kept after
        trimming. Default is 0, which is equal to trimming all samples detected
        as silence.
    stop_mode : str, optional
        Specify mode of detection of silence start after the start of multi-channel audio.
        Can be "any" or "all". Default is "all". With "any", any sample from any channel
        that is detected as silence will trigger the start of silence trimming after
        the start of the audio stream, limited usage. With "all", only if every sample
        from every channel is detected as silence will trigger the start of silence
        trimming after the start of the audio stream.
    detection : str, optional
        Set how silence is detected. Can be "avg", "rms", "peak", "median", "ptp", or "dev".
        Default value is "rms".
    window : float, optional
        Set the duration in number of seconds used to calculate the size of the window
        in number of samples for detecting silence. Using 0 will effectively disable
        any windowing and use only a single sample per channel for silence detection.
        In that case, it may be needed to also set start_silence and/or stop_silence
        to nonzero values with also start_duration and/or stop_duration to nonzero values.
        Default value is 0.02. Allowed range is from 0 to 10.
    timestamp : str, optional
        Set the processing mode of every audio frame output timestamp.
        Can be "write" or "copy". Defaults value is "write".

    Example usage:
    --------------
    stream.silenceremove(start_periods=1, start_threshold=-50, detection="rms")

    Ref: https://ffmpeg.org/ffmpeg-filters.html#silenceremove
    """
    return FilterNode(
        stream,
        silenceremove.__name__,
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
        },
    ).stream()
