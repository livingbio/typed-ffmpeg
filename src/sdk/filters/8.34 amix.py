from typing import Optional, Sequence, Union

from ..node import FilterNode
from ..stream import Stream


def amix(
    stream: Stream,
    inputs: int = 2,
    duration: Optional[str] = None,
    dropout_transition: float = 2.0,
    weights: Optional[Sequence[Union[int, float]]] = None,
    normalize: bool = True,
) -> Stream:
    """
    Mixes multiple audio inputs into a single output.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    inputs : int, optional
        The number of inputs. If unspecified, it defaults to 2.
    duration : str, optional
        How to determine the end-of-stream.
        "longest" - The duration of the longest input. (default)
        "shortest" - The duration of the shortest input.
        "first" - The duration of the first input.
    dropout_transition : float, optional
        The transition time, in seconds, for volume renormalization when an input stream ends.
        The default value is 2 seconds.
    weights : Sequence[Union[int, float]], optional
        Specify the weight of each input audio stream as a sequence of numbers separated
        by a space. If fewer weights are specified compared to the number of inputs, the
        last weight is assigned to the remaining inputs. The default weight for each input is 1.
    normalize : bool, optional
        Always scale inputs instead of only doing summation of samples.
        Beware of heavy clipping if inputs are not normalized prior or after filtering
        by this filter if this option is disabled. By default is enabled.

    Example usage:
    --------------
    stream.amix(inputs=3, duration="shortest", dropout_transition=5, weights=[1, 2, 1], normalize=True)

    Ref: https://ffmpeg.org/ffmpeg-filters.html#amix
    """
    return FilterNode(
        stream,
        amix.__name__,
        kwargs={
            "inputs": inputs,
            "duration": duration,
            "dropout_transition": dropout_transition,
            "weights": weights,
            "normalize": normalize,
        },
    ).stream()
