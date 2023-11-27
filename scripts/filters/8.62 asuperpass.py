from ..node import FilterNode
from ..stream import Stream


def asuperpass(
    stream: Stream,
    centerf: int = 1000,
    order: int = 4,
    qfactor: float = 1,
    level: float = 1,
) -> Stream:
    """
    Apply high order Butterworth band-pass filter.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        centerf : int, optional
            Set center frequency in Hertz. Allowed range is 2 to 999999. Default value is 1000.
        order : int, optional
            Set filter order. Available values are from 4 to 20. Default value is 4.
        qfactor : float, optional
            Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
        level : float, optional
            Set input gain level. Allowed range is from 0 to 2. Default value is 1.

    Example usage:
    --------------
    stream.asuperpass(
        centerf=2000,
        order=8,
        qfactor=0.5,
        level=0.8,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#asuperpass
    """
    return FilterNode(
        stream,
        asuperpass.__name__,
        kwargs={
            "centerf": centerf,
            "order": order,
            "qfactor": qfactor,
            "level": level,
        },
    ).stream()
