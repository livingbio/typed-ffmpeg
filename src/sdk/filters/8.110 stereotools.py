def stereotools(
    stream: Stream,
    level_in: float = 1.0,
    level_out: float = 1.0,
    balance_in: float = 0,
    balance_out: float = 0,
    softclip: bool = False,
    mutel: bool = False,
    muter: bool = False,
    phasel: bool = False,
    phaser: bool = False,
    mode: Literal[
        "lr>lr",
        "lr>ms",
        "ms>lr",
        "lr>ll",
        "lr>rr",
        "lr>l+r",
        "lr>rl",
        "ms>ll",
        "ms>rr",
        "ms>rl",
        "lr>l-r",
    ] = "lr>lr",
    slev: float = 1.0,
    sbal: float = 0,
    mlev: float = 1.0,
    mpan: float = 0,
    base: float = 0,
    delay: float = 0,
    sclevel: float = 1.0,
    phase: float = 0,
    bmode_in: Literal["balance", "amplitude", "power"] = "balance",
    bmode_out: Literal["balance", "amplitude", "power"] = "balance",
) -> Stream:
    """
    This filter has some handy utilities to manage stereo signals, for converting M/S stereo recordings to L/R signal while having control over the parameters or spreading the stereo image of master track.

    Parameters:
    ----------
    stream : Stream
        The input stream to filter.
    level_in : float, optional
        Set input level before filtering for both channels. Defaults is 1.
        Allowed range is from 0.015625 to 64.
    level_out : float, optional
        Set output level after filtering for both channels. Defaults is 1.
        Allowed range is from 0.015625 to 64.
    balance_in : float, optional
        Set input balance between both channels. Default is 0.
        Allowed range is from -1 to 1.
    balance_out : float, optional
        Set output balance between both channels. Default is 0.
        Allowed range is from -1 to 1.
    softclip : bool, optional
        Enable softclipping. Results in analog distortion instead of harsh digital 0dB
        clipping. Disabled by default.
    mutel : bool, optional
        Mute the left channel. Disabled by default.
    muter : bool, optional
        Mute the right channel. Disabled by default.
    phasel : bool, optional
        Change the phase of the left channel. Disabled by default.
    phaser : bool, optional
        Change the phase of the right channel. Disabled by default.
    mode : {'lr>lr', 'lr>ms', 'ms>lr', 'lr>ll', 'lr>rr', 'lr>l+r', 'lr>rl', 'ms>ll', 'ms>rr', 'ms>rl', 'lr>l-r'}, optional
        Set stereo mode. Available values are:
            'lr>lr' (default): Left/Right to Left/Right.
            'lr>ms': Left/Right to Mid/Side.
            'ms>lr': Mid/Side to Left/Right.
            'lr>ll': Left/Right to Left/Left.
            'lr>rr': Left/Right to Right/Right.
            'lr>l+r': Left/Right to Left + Right.
            'lr>rl': Left/Right to Right/Left.
            'ms>ll': Mid/Side to Left/Left.
            'ms>rr': Mid/Side to Right/Right.
            'ms>rl': Mid/Side to Right/Left.
            'lr>l-r': Left/Right to Left - Right.
    slev : float, optional
        Set level of the side signal. Default is 1.
        Allowed range is from 0.015625 to 64.
    sbal : float, optional
        Set balance of the side signal. Default is 0.
        Allowed range is from -1 to 1.
    mlev : float, optional
        Set level of the middle signal. Default is 1.
        Allowed range is from 0.015625 to 64.
    mpan : float, optional
        Set middle signal pan. Default is 0. Allowed range is from -1 to 1.
    base : float, optional
        Set stereo base between mono and inversed channels. Default is 0.
        Allowed range is from -1 to 1.
    delay : float, optional
        Set delay in milliseconds how much to delay left from right channel and
        vice versa. Default is 0. Allowed range is from -20 to 20.
    sclevel : float, optional
        Set S/C level. Default is 1. Allowed range is from 1 to 100.
    phase : float, optional
        Set the stereo phase in degrees. Default is 0. Allowed range is from 0 to 360.
    bmode_in : {'balance', 'amplitude', 'power'}, optional
        Set balance mode for balance_in option.
        Can be one of the following:
            'balance': Classic balance mode. Attenuate one channel at a time. Gain is raised up to 1.
            'amplitude': Similar as classic mode above but gain is raised up to 2.
            'power': Equal power distribution, from -6dB to +6dB range.
    bmode_out : {'balance', 'amplitude', 'power'}, optional
        Set balance mode for balance_out option.
        Can be one of the following:
            'balance': Classic balance mode. Attenuate one channel at a time. Gain is raised up to 1.
            'amplitude': Similar as classic mode above but gain is raised up to 2.
            'power': Equal power distribution, from -6dB to +6dB range.

    Example usage:
    --------------
    stream.stereotools(
        mode="lr>ms",
        sbal=0.5,
        sclevel=2,
    )

    Ref: https://ffmpeg.org/ffmpeg-filters.html#stereotools
    """
    return FilterNode(
        stream,
        stereotools.__name__,
        kwargs={
            "level_in": level_in,
            "level_out": level_out,
            "balance_in": balance_in,
            "balance_out": balance_out,
            "softclip": softclip,
            "mutel": mutel,
            "muter": muter,
            "phasel": phasel,
            "phaser": phaser,
            "mode": mode,
            "slev": slev,
            "sbal": sbal,
            "mlev": mlev,
            "mpan": mpan,
            "base": base,
            "delay": delay,
            "sclevel": sclevel,
            "phase": phase,
            "bmode_in": bmode_in,
            "bmode_out": bmode_out,
        },
    ).stream()
