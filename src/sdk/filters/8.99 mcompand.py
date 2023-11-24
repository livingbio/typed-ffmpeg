from typing import List

from ..node import FilterNode
from ..stream import Stream


def mcompand(
    stream: Stream,
    args: List[str],
) -> Stream:
    """
    Multiband Compress or expand the audio's dynamic range.

    The input audio is divided into bands using 4th order Linkwitz-Riley IIRs.
    This is akin to the crossover of a loudspeaker, and results in flat frequency
    response when absent compander action.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    args : List[str]
        This option syntax is:
        attack,decay,[attack,decay..] soft-knee points crossover_frequency [delay [initial_volume [gain]]] | attack,decay ...
        For explanation of each item refer to compand filter documentation.

    Example usage:
    --------------
    stream.mcompand(
        args=['0.01,1,0,-90,-90,0,-70,0', '0.008,0.1,0.02,-90,-30,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20'],
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#mcompand
    """
    return FilterNode(
        stream,
        mcompand.__name__,
        kwargs={
            "args": args,
        },
    ).stream()
