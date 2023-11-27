from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def asr(
    stream: Stream,
    rate: Optional[int] = 16000,
    hmm: Optional[str] = None,
    dict: Optional[str] = None,
    lm: Optional[str] = None,
    lmctl: Optional[str] = None,
    lmname: Optional[str] = None,
    logfn: Optional[str] = None,
) -> Stream:
    """
    Automatic Speech Recognition

    This filter uses PocketSphinx for speech recognition. To enable
    compilation of this filter, you need to configure FFmpeg with
    '--enable-pocketsphinx'.

    Parameters:
    -----------
    stream : Stream
        The input stream to filter.
    rate : int, optional
        Set sampling rate of input audio. Default is 16000. This needs to match speech models, otherwise one will get poor results.
    hmm : str, optional
        Set dictionary containing acoustic model files.
    dict : str, optional
        Set pronunciation dictionary.
    lm : str, optional
        Set language model file.
    lmctl : str, optional
        Set language model set.
    lmname : str, optional
        Set which language model to use.
    logfn : str, optional
        Set output for log messages.

    Returns:
    --------
    stream : Stream
        The output stream with recognized speech metadata.

    Example usage:
    --------------
    stream.asr(
        rate=44100,
        hmm='your/hmm/directory',
        dict='your/dictionary/directory',
        lm='your/language/model/file',
        lmctl='your/language/model/set',
        lmname='your/lm/name',
        logfn='your/log/file',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asr
    """
    return FilterNode(
        stream,
        asr.__name__,
        kwargs={
            "rate": rate,
            "hmm": hmm,
            "dict": dict,
            "lm": lm,
            "lmctl": lmctl,
            "lmname": lmname,
            "logfn": logfn,
        },
    ).stream()
