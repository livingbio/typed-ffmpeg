from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def rubberband(
    stream: Stream,
    tempo: float = 1.0,
    pitch: float = 1.0,
    transients: str = Literal["crisp", "mixed", "smooth"],
    detector: str = Literal["compound", "percussive", "soft"],
    phase: str = Literal["laminar", "independent"],
    window: str = Literal["standard", "short", "long"],
    smoothing: str = Literal["off", "on"],
    formant: str = Literal["shifted", "preserved"],
    pitchq: str = Literal["quality", "speed", "consistency"],
    channels: str = Literal["apart", "together"],
) -> Stream:
    """
    Apply time-stretching and pitch-shifting with librubberband.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    tempo : float, optional
        Set tempo scale factor. Default is 1.0.
    pitch : float, optional
        Set pitch scale factor. Default is 1.0.
    transients : str, optional
        Set transients detector.
        Possible values are: 'crisp', 'mixed', 'smooth'.
    detector : str, optional
        Set detector.
        Possible values are: 'compound', 'percussive', 'soft'.
    phase : str, optional
        Set phase.
        Possible values are: 'laminar', 'independent'.
    window : str, optional
        Set processing window size.
        Possible values are: 'standard', 'short', 'long'.
    smoothing : str, optional
        Set smoothing.
        Possible values are: 'off', 'on'.
    formant : str, optional
        Enable formant preservation when shift pitching.
        Possible values are: 'shifted', 'preserved'.
    pitchq : str, optional
        Set pitch quality.
        Possible values are: 'quality', 'speed', 'consistency'.
    channels : str, optional
        Set channels.
        Possible values are: 'apart', 'together'.

    Example usage:
    --------------
    stream.rubberband(
        tempo=1.25,
        pitch=0.8,
        transients="smooth",
        detector="compound",
        phase="independent",
        window="standard",
        smoothing="on",
        formant="preserved",
        pitchq="quality",
        channels="together",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#rubberband
    """
    return FilterNode(
        stream,
        rubberband.__name__,
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
        },
    ).stream()
