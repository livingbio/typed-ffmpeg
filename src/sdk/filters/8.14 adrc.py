from typing import Union

from ..node import FilterNode
from ..stream import Stream


def adrc(
    stream: Stream,
    transfer: Union[str, float] = "p",
    attack: float = 50,
    release: float = 100,
    channels: str = "all",
) -> Stream:
    """
    Apply spectral dynamic range controller filter to input audio stream.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    transfer : Union[str, float], optional
        Set the transfer expression. The expression can contain the following constants:
            - ch: current channel number
            - sn: current sample number
            - nb_channels: number of channels
            - t: timestamp expressed in seconds
            - sr: sample rate
            - p: current frequency power value, in dB
            - f: current frequency in Hz
        Default value is 'p'.
    attack : float, optional
        Set the attack in milliseconds. Default is 50 milliseconds.
        Allowed range is from 1 to 1000 milliseconds.
    release : float, optional
        Set the release in milliseconds. Default is 100 milliseconds.
        Allowed range is from 5 to 2000 milliseconds.
    channels : str, optional
        Set which channels to filter. By default, 'all' channels in the audio stream are filtered.

    Example usage:
    --------------
    stream.adrc(
        transfer='p*exp(-40*(t-2)*(t-2))',
        attack=100,
        release=200,
        channels='1',
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adrc
    """
    return FilterNode(
        stream,
        adrc.__name__,
        kwargs={"transfer": transfer, "attack": attack, "release": release, "channels": channels},
    ).stream()
