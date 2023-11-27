from typing import List, Optional

from ..node import FilterNode
from ..stream import Stream


def adelay(
    stream: Stream,
    delays: Optional[List[str]] = None,
    use_last_delay_for_all_channels: bool = False,
) -> Stream:
    """
    Delay one or more audio channels.

    Samples in delayed channel are filled with silence.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
            The input stream to filter.
        delays : Optional[List[str]], optional
            Set list of delays in milliseconds for each channel separated by '|'.
            Unused delays will be silently ignored. If the number of given delays is
            smaller than the number of channels, all remaining channels will not be delayed.
            If you want to delay an exact number of samples, append 'S' to the number.
            If you want instead to delay in seconds, append 's' to the number.
        use_last_delay_for_all_channels : bool, optional
            Use the last set delay for all remaining channels. By default, it is disabled.
            This option, if enabled, changes how the 'delays' option is interpreted.

    Example usage:
    --------------
    stream.adelay(
        delays=["500|1000", "800|1200"],
        use_last_delay_for_all_channels=False,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#adelay
    """
    return FilterNode(
        stream,
        adelay.__name__,
        kwargs={
            "delays": "|".join(delays) if delays else None,
            "all": int(use_last_delay_for_all_channels),
        },
    ).stream()
