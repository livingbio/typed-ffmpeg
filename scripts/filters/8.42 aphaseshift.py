from ..node import FilterNode
from ..stream import Stream


def aphaseshift(
    stream: Stream,
    shift: float = 0.0,
    level: float = 1.0,
    order: int = 8,
) -> Stream:
    """
    Apply phase shift to input audio samples.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        shift : float, optional
            Specify phase shift. Allowed range is from -1.0 to 1.0.
            Default value is 0.0.
        level : float, optional
            Set output gain applied to final output. Allowed range is from 0.0 to 1.0.
            Default value is 1.0.
        order : int, optional
            Set filter order used for filtering. Allowed range is from 1 to 16.
            Default value is 8.

    Example usage:
    --------------
    stream.aphaseshift(
        shift=0.5,
        level=0.8,
        order=4,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#aphaseshift
    """
    return FilterNode(
        stream,
        aphaseshift.__name__,
        kwargs={
            "shift": shift,
            "level": level,
            "order": order,
        },
    ).stream()
