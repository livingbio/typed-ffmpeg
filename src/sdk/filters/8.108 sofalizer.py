from typing import Union

from ..node import FilterNode
from ..stream import Stream


def sofalizer(
    stream: Stream,
    sofa: str,
    gain: float = 0,
    rotation: float = 0,
    elevation: float = 0,
    radius: float = 1,
    type: str = Union["time", "freq"],
    speakers: str = "",
    lfegain: float = 0,
    framesize: int = 1024,
    normalize: bool = True,
    interpolate: bool = False,
    minphase: bool = False,
    anglestep: float = 1,
    radstep: float = 1,
) -> Stream:
    """
    SOFAlizer uses head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones (audio formats up to 9 channels supported). The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database). SOFAlizer is developed at the Acoustics Research Institute (ARI) of the Austrian Academy of Sciences.

    To enable compilation of this filter, you need to configure FFmpeg with --enable-libmysofa.

    The filter accepts the following options:
    - sofa : str
        Set the SOFA file used for rendering.
    - gain : float, optional
        Set gain applied to audio. Value is in dB. Default is 0.
    - rotation : float, optional
        Set rotation of virtual loudspeakers in deg. Default is 0.
    - elevation : float, optional
        Set elevation of virtual speakers in deg. Default is 0.
    - radius : float, optional
        Set distance in meters between loudspeakers and the listener with near-field HRTFs. Default is 1.
    - type : str, optional
        Set processing type. Can be 'time' or 'freq'. 'time' is processing audio in the time domain which is slow. 'freq' is processing audio in the frequency domain which is fast. Default is 'freq'.
    - speakers : str, optional
        Set custom positions of virtual loudspeakers. Syntax for this option is: '<CH> <AZIM> <ELEV>[|<CH> <AZIM> <ELEV>|...]'. Each virtual loudspeaker is described with a short channel name following with azimuth and elevation in degrees. Each virtual loudspeaker description is separated by '|'. For example, to override front left and front right channel positions use: 'speakers=FL 45 15|FR 345 15'. Descriptions with unrecognized channel names are ignored.
    - lfegain : float, optional
        Set custom gain for LFE channels. Value is in dB. Default is 0.
    - framesize : int, optional
        Set custom frame size in number of samples. Default is 1024. Allowed range is from 1024 to 96000. Only used if the option 'type' is set to 'freq'.
    - normalize : bool, optional
        Should all IRs be normalized upon importing SOFA file. By default is enabled.
    - interpolate : bool, optional
        Should nearest IRs be interpolated with neighbor IRs if the exact position does not match. By default is disabled.
    - minphase : bool, optional
        Minphase all IRs upon loading of the SOFA file. By default is disabled.
    - anglestep : float, optional
        Set neighbor search angle step. Only used if the option 'interpolate' is enabled.
    - radstep : float, optional
        Set neighbor search radius step. Only used if the option 'interpolate' is enabled.

    Example usage:
    --------------
    stream.sofalizer(
        sofa='path/to/sofa/file.sofa',
        gain=-6,
        rotation=30,
        elevation=15,
        radius=2,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#sofalizer
    """
    return FilterNode(
        stream,
        sofalizer.__name__,
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
        },
    ).stream()
