from ..node import FilterNode
from ..stream import Stream


def stereowiden(
    stream: Stream,
    delay: int = 20,
    feedback: float = 0.3,
    crossfeed: float = 0.3,
    drymix: float = 0.8,
) -> Stream:
    """
    This filter enhances the stereo effect by suppressing the signal common to both channels and by delaying the signal of the left into the right and vice versa, thereby widening the stereo effect.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        delay : int, optional
            Time in milliseconds of the delay of the left signal into the right and vice versa.
            Default is 20 milliseconds.
        feedback : float, optional
            Amount of gain in delayed signal into the right and vice versa. Gives a delay
            effect of the left signal in the right output and vice versa, which gives the widening effect.
            Default is 0.3.
        crossfeed : float, optional
            Crossfeed of the left signal into the right with inverted phase. This helps in suppressing
            the mono. If the value is 1, it will cancel all the signal common to both channels.
            Default is 0.3.
        drymix : float, optional
            Set the level of the input signal of the original channel.
            Default is 0.8.

    Example usage:
    --------------
    stream.stereowiden(
        delay=30,
        feedback=0.5,
        crossfeed=0.5,
        drymix=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#stereowiden
    """
    return FilterNode(
        stream,
        stereowiden.__name__,
        kwargs={
            "delay": delay,
            "feedback": feedback,
            "crossfeed": crossfeed,
            "drymix": drymix,
        },
    ).stream()
