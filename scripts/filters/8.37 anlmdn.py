from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def anlmdn(
    stream: Stream,
    strength: float = 0.00001,
    patch: int = 2,
    research: int = 6,
    output: str = Literal["i", "o", "n"],
    smooth: int = 11,
) -> Stream:
    """
    Reduce broadband noise in audio samples using Non-Local Means algorithm.

    Each sample is adjusted by looking for other samples with similar contexts. This
    context similarity is defined by comparing their surrounding patches of size `p`. Patches are searched in an area of `r` around the sample.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        strength : float, optional
            Set denoising strength. Allowed range is from 0.00001 to 10000.
            Default value is 0.00001.
        patch : int, optional
            Set patch radius duration. Allowed range is from 1 to 100 milliseconds.
            Default value is 2 milliseconds.
        research : int, optional
            Set research radius duration. Allowed range is from 2 to 300 milliseconds.
            Default value is 6 milliseconds.
        output : str, optional
            Set the output mode.
            It accepts the following values:
                'i': Pass input unchanged.
                'o': Pass noise filtered out.
                'n': Pass only noise.
            Default value is 'o'.
        smooth : int, optional
            Set smooth factor. Default value is 11. Allowed range is from 1 to 1000.

    Example usage:
    --------------
    stream.anlmdn(
        strength=0.0001,
        patch=5,
        research=10,
        output='n',
        smooth=20,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#anlmdn
    """
    return FilterNode(
        stream,
        anlmdn.__name__,
        kwargs={
            "strength": strength,
            "patch": patch,
            "research": research,
            "output": output,
            "smooth": smooth,
        },
    ).stream()
