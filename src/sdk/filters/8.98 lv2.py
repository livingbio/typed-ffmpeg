from typing import Union

from ..node import FilterNode
from ..stream import Stream


def lv2(
    stream: Stream,
    plugin: str,
    controls: Union[str, float] = "",
    sample_rate: int = 44100,
    nb_samples: int = 1024,
    duration: str = "",
) -> Stream:
    """
    Load a LV2 (LADSPA Version 2) plugin.

    To enable compilation of this filter you need to configure FFmpeg with `--enable-lv2`.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    plugin : str
        Specifies the plugin URI. You may need to escape ':'.
    controls : Union[str, float], optional
        Set the '|' separated list of controls which are zero or more floating point
        values that determine the behavior of the loaded plugin (for example delay,
        threshold or gain).
        If `controls` is set to 'help', all available controls and their valid ranges are printed.
        Default is '' (empty string).
    sample_rate : int, optional
        Specify the sample rate. Default is 44100. Only used if plugin has zero inputs.
    nb_samples : int, optional
        Set the number of samples per channel per each output frame. Default is 1024.
        Only used if plugin has zero inputs.
    duration : str, optional
        Set the minimum duration of the sourced audio. See the Time duration section in the ffmpeg-utils(1) manual
        for the accepted syntax.
        Note that the resulting duration may be greater than the specified duration,
        as the generated audio is always cut at the end of a complete frame.
        If not specified, or the expressed duration is negative, the audio is supposed to be generated forever.
        Only used if plugin has zero inputs.

    Example usage:
    --------------
    stream.lv2(plugin='http://example.com/myplugin')

    Ref: https://ffmpeg.org/ffmpeg-filters.html#lv2
    """
    return FilterNode(
        stream,
        lv2.__name__,
        kwargs={
            "plugin": plugin,
            "controls": controls,
            "sample_rate": sample_rate,
            "nb_samples": nb_samples,
            "duration": duration,
        },
    ).stream()
