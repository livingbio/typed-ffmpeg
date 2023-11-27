from typing import Literal, Union

from ..node import FilterNode
from ..stream import Stream


def astats(
    stream: Stream,
    length: float = 0.05,
    metadata: Union[Literal["none"], str] = "",
    reset: int = 0,
    measure_perchannel: Union[Literal["none"], str] = "all",
    measure_overall: Union[Literal["none"], str] = "all",
) -> Stream:
    """
    Display time domain statistical information about the audio channels. Statistics are calculated and displayed for each audio channel and, where applicable, an overall figure is also given.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    length : float, optional
        Short window length in seconds, used for peak and trough RMS measurement.
        Default is 0.05 (50 milliseconds). Allowed range is [0 - 10].
    metadata : Union[Literal["none"], str], optional
        Set metadata injection. All the metadata keys are prefixed with lavfi.astats.X, where X is channel number starting from 1 or string Overall. Default is disabled.

        Available keys for each channel are:
        Bit_depth
        Crest_factor
        DC_offset
        Dynamic_range
        Entropy
        Flat_factor
        Max_difference
        Max_level
        Mean_difference
        Min_difference
        Min_level
        Noise_floor
        Noise_floor_count
        Number_of_Infs
        Number_of_NaNs
        Number_of_denormals
        Peak_count
        Abs_Peak_count
        Peak_level
        RMS_difference
        RMS_peak
        RMS_trough
        Zero_crossings
        Zero_crossings_rate

    reset : int, optional
        Set the number of frames over which cumulative stats are calculated before being reset.
        Default is disabled.
    measure_perchannel : Union[Literal["none"], str], optional
        Select the parameters which are measured per channel.
        The metadata keys can be used as flags, default is 'all' which measures everything. 'none' disables all per channel measurement.
    measure_overall : Union[Literal["none"], str], optional
        Select the parameters which are measured overall.
        The metadata keys can be used as flags, default is 'all' which measures everything. 'none' disables all overall measurement.

    Example usage:
    --------------
    stream.astats(
        length=0.1,
        metadata="lavfi.astats.Overall.Peak_count",
        reset=100,
        measure_perchannel="None",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#astats
    """
    return FilterNode(
        stream,
        astats.__name__,
        kwargs={
            "length": length,
            "metadata": metadata,
            "reset": reset,
            "measure_perchannel": measure_perchannel,
            "measure_overall": measure_overall,
        },
    ).stream()
