from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def ladspa(
    stream: Stream,
    file: Optional[str] = None,
    plugin: Optional[str] = None,
    controls: Optional[str] = None,
    sample_rate: Optional[int] = None,
    nb_samples: Optional[int] = None,
    duration: Optional[str] = None,
    latency: bool = False,
) -> Stream:
    """
    Load a LADSPA (Linux Audio Developer's Simple Plugin API) plugin.

    To enable compilation of this filter, you need to configure FFmpeg with `--enable-ladspa`.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    file : str, optional
        Specifies the name of the LADSPA plugin library to load. If the environment
        variable `LADSPA_PATH` is defined, the LADSPA plugin is searched in
        each one of the directories specified by the colon-separated list in `LADSPA_PATH`,
        otherwise in the standard LADSPA paths, which are in this order:
        `HOME/.ladspa/lib/`, `/usr/local/lib/ladspa/`, `/usr/lib/ladspa/`.
    plugin : str, optional
        Specifies the plugin within the library. Some libraries contain only
        one plugin, but others contain many of them. If this is not set filter
        will list all available plugins within the specified library.
    controls : str, optional
        Set the '|' separated list of controls which are zero or more floating point
        values that determine the behavior of the loaded plugin (for example delay,
        threshold or gain).
        Controls need to be defined using the following syntax:
        `c0=<value0>|c1=<value1>|c2=<value2>|...`, where
        `<valuei>` is the value set on the i-th control.
        Alternatively, they can be also defined using the following syntax:
        `<value0>|<value1>|<value2>|...`, where
        `<valuei>` is the value set on the i-th control.
        If `controls` is set to `help`, all available controls and their valid ranges are printed.
    sample_rate : int, optional
        Specify the sample rate, default to 44100. Only used if the plugin has zero inputs.
    nb_samples : int, optional
        Set the number of samples per channel per each output frame, default
        is 1024. Only used if the plugin has zero inputs.
    duration : str, optional
        Set the minimum duration of the sourced audio. See the Time duration section in the ffmpeg-utils manual
        for the accepted syntax.
        Note that the resulting duration may be greater than the specified duration,
        as the generated audio is always cut at the end of a complete frame.
        If not specified, or the expressed duration is negative, the audio is
        supposed to be generated forever.
        Only used if the plugin has zero inputs.
    latency : bool, optional
        Enable latency compensation, by default is disabled.
        Only used if the plugin has inputs.

    Example usage:
    --------------
    stream.ladspa(
        file='path/to/plugin.so',
        plugin='my_plugin',
        controls='c0=1.0|c1=2.0',
        sample_rate=48000,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#ladspa
    """
    return FilterNode(
        stream,
        ladspa.__name__,
        kwargs={
            "file": file,
            "plugin": plugin,
            "controls": controls,
            "sample_rate": sample_rate,
            "nb_samples": nb_samples,
            "duration": duration,
            "latency": latency,
        },
    ).stream()
