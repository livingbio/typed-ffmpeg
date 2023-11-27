from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def headphone(
    stream: Stream,
    map: str,
    gain: float = 0,
    type: Literal["time", "freq"] = "freq",
    lfe: float = 0,
    size: int = 1024,
    hrir: Literal["stereo", "multich"] = "stereo",
) -> Stream:
    """
    Apply head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones. The HRIRs are provided via additional streams, for each channel one stereo input stream is needed.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    map : str
        Set mapping of input streams for convolution. The argument is a '|'-separated list of channel names in order as they are given as additional stream inputs for filter. This also specify number of input streams. Number of input streams must be not less than number of channels in first stream plus one.
    gain : float, optional
        Set gain applied to audio. Value is in dB. Default is 0.
    type : str, optional
        Set processing type. Can be 'time' or 'freq'. 'time' is processing audio in time domain which is slow. 'freq' is processing audio in frequency domain which is fast. Default is 'freq'.
    lfe : float, optional
        Set custom gain for LFE channels. Value is in dB. Default is 0.
    size : int, optional
        Set size of frame in number of samples which will be processed at once. Default value is 1024. Allowed range is from 1024 to 96000.
    hrir : str, optional
        Set format of hrir stream. Default value is 'stereo'. Alternative value is 'multich'. If value is set to 'stereo', the number of additional streams should be greater or equal to the number of input channels in the first input stream. Also, each additional stream should have stereo number of channels. If value is set to 'multich', the number of additional streams should be exactly one. Also, the number of input channels of additional stream should be equal or greater than twice the number of channels of the first input stream.

    Example usage:
    --------------
    stream.headphone(
        map='FL|FR|BR|FL|FR|BR',
        gain=-6,
        type='time',
        lfe=-3,
        size=2048,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#headphone
    """
    return FilterNode(
        stream,
        headphone.__name__,
        kwargs={
            "map": map,
            "gain": gain,
            "type": type,
            "lfe": lfe,
            "size": size,
            "hrir": hrir,
        },
    ).stream()
