from typing import Literal

from ..node import FilterNode
from ..stream import Stream


def firequalizer(
    stream: Stream,
    gain: str = "gain_interpolate(f)",
    gain_entry: str = None,
    delay: float = 0.01,
    accuracy: float = 5,
    wfunc: Literal[
        "rectangular",
        "hann",
        "hamming",
        "blackman",
        "nuttall3",
        "mnuttall3",
        "nuttall",
        "bnuttall",
        "bharris",
        "tukey",
    ] = "hann",
    fixed: bool = False,
    multi: bool = False,
    zero_phase: bool = False,
    scale: Literal["linlin", "linlog", "loglin", "loglog"] = "linlog",
    dumpfile: str = None,
    dumpscale: Literal["linlin", "linlog", "loglin", "loglog"] = "linlog",
    fft2: bool = False,
    min_phase: bool = False,
) -> Stream:
    """
    Apply FIR Equalization using arbitrary frequency response.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    gain : str, optional
        Set gain curve equation (in dB). The expression can contain variables:
            - f : the evaluated frequency
            - sr : sample rate
            - ch : channel number, set to 0 when multichannels evaluation is disabled
            - chid : channel id, see libavutil/channel_layout.h, set to the first channel id when
              multichannels evaluation is disabled
            - chs : number of channels
            - chlayout : channel_layout, see libavutil/channel_layout.h

        and functions:
            - gain_interpolate(f) : interpolate gain on frequency f based on gain_entry
            - cubic_interpolate(f) : same as gain_interpolate, but smoother

        This option is also available as command. Default is 'gain_interpolate(f)'.
    gain_entry : str, optional
        Set gain entry for gain_interpolate function. The expression can contain functions:
            - entry(f, g) : store gain entry at frequency f with value g

        This option is also available as command.
    delay : float, optional
        Set filter delay in seconds. Higher value means more accurate.
        Default is 0.01.
    accuracy : float, optional
        Set filter accuracy in Hz. Lower value means more accurate.
        Default is 5.
    wfunc : str, optional
        Set window function. Acceptable values are:
            - 'rectangular' : rectangular window, useful when gain curve is already smooth
            - 'hann' : hann window (default)
            - 'hamming' : hamming window
            - 'blackman' : blackman window
            - 'nuttall3' : 3-terms continuous 1st derivative nuttall window
            - 'mnuttall3' : minimum 3-terms discontinuous nuttall window
            - 'nuttall' : 4-terms continuous 1st derivative nuttall window
            - 'bnuttall' : minimum 4-terms discontinuous nuttall (blackman-nuttall) window
            - 'bharris' : blackman-harris window
            - 'tukey' : tukey window
    fixed : bool, optional
        If enabled, use fixed number of audio samples. This improves speed when
        filtering with large delay. Default is False.
    multi : bool, optional
        Enable multichannels evaluation on gain. Default is False.
    zero_phase : bool, optional
        Enable zero phase mode by subtracting timestamp to compensate delay.
        Default is False.
    scale : str, optional
        Set scale used by gain. Acceptable values are:
            - 'linlin' : linear frequency, linear gain
            - 'linlog' : linear frequency, logarithmic (in dB) gain (default)
            - 'loglin' : logarithmic (in octave scale where 20 Hz is 0) frequency, linear gain
            - 'loglog' : logarithmic frequency, logarithmic gain
    dumpfile : str, optional
        Set file for dumping, suitable for gnuplot.
    dumpscale : str, optional
        Set scale for dumpfile. Acceptable values are same with scale option.
        Default is 'linlog'.
    fft2 : bool, optional
        Enable 2-channel convolution using complex FFT. This improves speed significantly.
        Default is False.
    min_phase : bool, optional
        Enable minimum phase impulse response. Default is False.

    Example usage:
    --------------
    stream.firequalizer(
        gain="cubic_interpolate(f)",
        delay=0.02,
        accuracy=2,
        wfunc="blackman",
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#firequalizer
    """
    return FilterNode(
        stream,
        firequalizer.__name__,
        kwargs={
            "gain": gain,
            "gain_entry": gain_entry,
            "delay": delay,
            "accuracy": accuracy,
            "wfunc": wfunc,
            "fixed": fixed,
            "multi": multi,
            "zero_phase": zero_phase,
            "scale": scale,
            "dumpfile": dumpfile,
            "dumpscale": dumpscale,
            "fft2": fft2,
            "min_phase": min_phase,
        },
    ).stream()
