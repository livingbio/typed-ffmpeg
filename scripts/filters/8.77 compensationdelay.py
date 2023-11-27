from typing import Optional

from ..node import FilterNode
from ..stream import Stream


def compensationdelay(
    stream: Stream,
    mm: float = 0,
    cm: float = 0,
    m: float = 0,
    dry: Optional[float] = 0,
    wet: Optional[float] = 1,
    temp: int = 20,
) -> Stream:
    """
    Compensation Delay Line is a metric based delay to compensate differing positions of microphones or speakers.

    For example, you have recorded guitar with two microphones placed in different locations. Because the front of sound wave has fixed speed in normal conditions, the phasing of microphones can vary and depends on their location and interposition. The best sound mix can be achieved when these microphones are in phase (synchronized).
    Note that a distance of ~30 cm between microphones makes one microphone capture the signal in antiphase to the other microphone. That makes the final mix sound moody.
    This filter helps to solve phasing problems by adding different delays to each microphone track and make them synchronized.

    The best result can be reached when you take one track as base and synchronize other tracks one by one with it.
    Remember that synchronization/delay tolerance depends on sample rate, too. Higher sample rates will give more tolerance.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    mm : float, optional
        Set millimeters distance. This is compensation distance for fine tuning.
        Default is 0.
    cm : float, optional
        Set cm distance. This is compensation distance for tightening distance setup.
        Default is 0.
    m : float, optional
        Set meters distance. This is compensation distance for hard distance setup.
        Default is 0.
    dry : float, optional
        Set dry amount. Amount of unprocessed (dry) signal.
        Default is 0.
    wet : float, optional
        Set wet amount. Amount of processed (wet) signal.
        Default is 1.
    temp : int, optional
        Set temperature in degrees Celsius. This is the temperature of the environment.
        Default is 20.

    Example usage:
    --------------
    stream.compensationdelay(
        mm=5.5,
        cm=1.2,
        m=0,
        dry=0.2,
        wet=0.8,
        temp=25,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#compensationdelay
    """
    return FilterNode(
        stream,
        compensationdelay.__name__,
        kwargs={
            "mm": mm,
            "cm": cm,
            "m": m,
            "dry": dry,
            "wet": wet,
            "temp": temp,
        },
    ).stream()
