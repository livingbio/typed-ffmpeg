from ..node import FilterNode
from ..stream import Stream


def surround(
    stream: Stream,
    chl_out: str = "5.1",
    chl_in: str = "stereo",
    level_in: float = 1,
    level_out: float = 1,
    lfe: bool = True,
    lfe_low: int = 128,
    lfe_high: int = 256,
    lfe_mode: str = "add",
    smooth: float = 0.0,
    angle: int = 90,
    focus: float = 0,
    fc_in: float = 1,
    fc_out: float = 1,
    fl_in: float = 1,
    fl_out: float = 1,
    fr_in: float = 1,
    fr_out: float = 1,
    sl_in: float = 1,
    sl_out: float = 1,
    sr_in: float = 1,
    sr_out: float = 1,
    bl_in: float = 1,
    bl_out: float = 1,
    br_in: float = 1,
    br_out: float = 1,
    bc_in: float = 1,
    bc_out: float = 1,
    lfe_in: float = 1,
    lfe_out: float = 1,
    allx: float = -1,
    ally: float = -1,
    fcx: float = 0.5,
    fcy: float = 0.5,
    flx: float = 0.5,
    fly: float = 0.5,
    frx: float = 0.5,
    fry: float = 0.5,
    slx: float = 0.5,
    sly: float = 0.5,
    srx: float = 0.5,
    sry: float = 0.5,
    blx: float = 0.5,
    bly: float = 0.5,
    brx: float = 0.5,
    bry: float = 0.5,
    bcx: float = 0.5,
    bcy: float = 0.5,
    win_size: int = 4096,
    win_func: str = "hann",
    overlap: float = 0.5,
) -> Stream:
    """
    Apply audio surround upmix filter.

    This filter allows producing multichannel output from an audio stream.

    The filter accepts the following options:

        Parameters:
        ----------
        stream : Stream
             The input stream to filter.
        chl_out : str, optional
             Set output channel layout. By default, this is '5.1'.
             See 'the Channel Layout section in the ffmpeg-utils(1) manual'
             for the required syntax.
        chl_in : str, optional
             Set input channel layout. By default, this is 'stereo'.
             See 'the Channel Layout section in the ffmpeg-utils(1) manual'
             for the required syntax.
        level_in : float, optional
             Set input volume level. By default, this is 1.
        level_out : float, optional
             Set output volume level. By default, this is 1.
        lfe : bool, optional
             Enable LFE channel output if the output channel layout has it.
             By default, this is enabled.
        lfe_low : int, optional
             Set the LFE low cutoff frequency. By default, this is 128 Hz.
        lfe_high : int, optional
             Set the LFE high cutoff frequency. By default, this is 256 Hz.
        lfe_mode : str, optional
             Set the LFE mode, can be 'add' or 'sub'. Default is 'add'.
             In 'add' mode, the LFE channel is created from the input audio and added to the output.
             In 'sub' mode, the LFE channel is created from the input audio and added to the output, but
             also all non-LFE output channels are subtracted with the output LFE channel.
        smooth : float, optional
             Set the temporal smoothness strength, used to gradually change factors when transforming
             stereo sound in time. Allowed range is from 0.0 to 1.0.
             Useful to improve output quality with 'focus' option values greater than 0.0.
             Default is 0.0. Only values inside this range and without edges are effective.
        angle : int, optional
             Set the angle of stereo surround transform. Allowed range is from 0 to 360.
             Default is 90.
        focus : float, optional
             Set the focus of stereo surround transform. Allowed range is from -1 to 1.
             Default is 0.
        fc_in : float, optional
             Set front center input volume. By default, this is 1.
        fc_out : float, optional
             Set front center output volume. By default, this is 1.
        fl_in : float, optional
             Set front left input volume. By default, this is 1.
        fl_out : float, optional
             Set front left output volume. By default, this is 1.
        fr_in : float, optional
             Set front right input volume. By default, this is 1.
        fr_out : float, optional
             Set front right output volume. By default, this is 1.
        sl_in : float, optional
             Set side left input volume. By default, this is 1.
        sl_out : float, optional
             Set side left output volume. By default, this is 1.
        sr_in : float, optional
             Set side right input volume. By default, this is 1.
        sr_out : float, optional
             Set side right output volume. By default, this is 1.
        bl_in : float, optional
             Set back left input volume. By default, this is 1.
        bl_out : float, optional
             Set back left output volume. By default, this is 1.
        br_in : float, optional
             Set back right input volume. By default, this is 1.
        br_out : float, optional
             Set back right output volume. By default, this is 1.
        bc_in : float, optional
             Set back center input volume. By default, this is 1.
        bc_out : float, optional
             Set back center output volume. By default, this is 1.
        lfe_in : float, optional
             Set LFE input volume. By default, this is 1.
        lfe_out : float, optional
             Set LFE output volume. By default, this is 1.
        allx : float, optional
             Set the spread usage of stereo image across the X axis for all channels.
             Allowed range is from -1 to 15. By default, this value is negative -1, and thus unused.
        ally : float, optional
             Set the spread usage of stereo image across the Y axis for all channels.
             Allowed range is from -1 to 15. By default, this value is negative -1, and thus unused.
        fcx, flx, frx, blx, brx, slx, srx, bcx : float, optional
             Set the spread usage of stereo image across the X axis for each channel.
             Allowed range is from 0.06 to 15.
             By default this value is 0.5.
        fcy, fly, fry, bly, bry, sly, sry, bcy : float, optional
             Set the spread usage of stereo image across the Y axis for each channel.
             Allowed range is from 0.06 to 15.
             By default this value is 0.5.
        win_size : int, optional
             Set the window size. Allowed range is from 1024 to 65536. Default size is 4096.
        win_func : str, optional
             Set the window function.
             It accepts the following values:
                 'rect'
                 'bartlett'
                 'hann, hanning'
                 'hamming'
                 'blackman'
                 'welch'
                 'flattop'
                 'bharris'
                 'bnuttall'
                 'bhann'
                 'sine'
                 'nuttall'
                 'lanczos'
                 'gauss'
                 'tukey'
                 'dolph'
                 'cauchy'
                 'parzen'
                 'poisson'
                 'bohman'
                 'kaiser'
             Default is 'hann'.
        overlap : float, optional
             Set the window overlap. If set to 1, the recommended overlap for the selected
             window function will be picked. Default is 0.5.

    Example usage:
    --------------
    stream.surround(
        chl_out="5.1",
        chl_in="stereo",
        level_in=1,
        level_out=1,
        lfe=True,
        lfe_low=128,
        lfe_high=256,
        lfe_mode="add",
        smooth=0.0,
        angle=90,
        focus=0,
        fc_in=1,
        fc_out=1,
        fl_in=1,
        fl_out=1,
        fr_in=1,
        fr_out=1,
        sl_in=1,
        sl_out=1,
        sr_in=1,
        sr_out=1,
        bl_in=1,
        bl_out=1,
        br_in=1,
        br_out=1,
        bc_in=1,
        bc_out=1,
        lfe_in=1,
        lfe_out=1,
        allx=-1,
        ally=-1,
        fcx=0.5,
        fcy=0.5,
        flx=0.5,
        fly=0.5,
        frx=0.5,
        fry=0.5,
        slx=0.5,
        sly=0.5,
        srx=0.5,
        sry=0.5,
        blx=0.5,
        bly=0.5,
        brx=0.5,
        bry=0.5,
        bcx=0.5,
        bcy=0.5,
        win_size=4096,
        win_func="hann",
        overlap=0.5,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#surround
    """
    return FilterNode(
        stream,
        surround.__name__,
        kwargs={
            "chl_out": chl_out,
            "chl_in": chl_in,
            "level_in": level_in,
            "level_out": level_out,
            "lfe": lfe,
            "lfe_low": lfe_low,
            "lfe_high": lfe_high,
            "lfe_mode": lfe_mode,
            "smooth": smooth,
            "angle": angle,
            "focus": focus,
            "fc_in": fc_in,
            "fc_out": fc_out,
            "fl_in": fl_in,
            "fl_out": fl_out,
            "fr_in": fr_in,
            "fr_out": fr_out,
            "sl_in": sl_in,
            "sl_out": sl_out,
            "sr_in": sr_in,
            "sr_out": sr_out,
            "bl_in": bl_in,
            "bl_out": bl_out,
            "br_in": br_in,
            "br_out": br_out,
            "bc_in": bc_in,
            "bc_out": bc_out,
            "lfe_in": lfe_in,
            "lfe_out": lfe_out,
            "allx": allx,
            "ally": ally,
            "fcx": fcx,
            "fcy": fcy,
            "flx": flx,
            "fly": fly,
            "frx": frx,
            "fry": fry,
            "slx": slx,
            "sly": sly,
            "srx": srx,
            "sry": sry,
            "blx": blx,
            "bly": bly,
            "brx": brx,
            "bry": bry,
            "bcx": bcx,
            "bcy": bcy,
            "win_size": win_size,
            "win_func": win_func,
            "overlap": overlap,
        },
    ).stream()
