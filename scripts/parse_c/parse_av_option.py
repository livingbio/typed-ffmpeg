import re

from .parse_c_structure import parse_c_structure
from .schema import AVOption


def _p(string: str, assert_key: str = None) -> str:
    if not "=" in string or not string.startswith("."):
        return string

    key, value = string.split("=", 1)
    key = key.strip()[1:]
    if assert_key:
        assert assert_key == key.strip(), string

    return string


def _aligns(values: list[str]) -> dict[str, str]:
    vars = ["name", "help", "offset", "type", "default", "min", "max", "flags", "unit"]
    output = {}

    assert len(values) <= len(vars), values
    j = 0

    for i, var in enumerate(vars):
        if j < len(values):
            try:
                v = _p(values[j], var)
                output[var] = v
                j += 1
            except AssertionError:
                output[var] = None
        else:
            output[var] = None

    assert j == len(values), values
    return output


def _parse_av_option(text: str) -> list[AVOption]:
    # the meaning of option_str please see libavutil/opt.h::AVOption
    option_lines = parse_c_structure(text)

    output: list[AVOption] = []

    def _eval_avoption(
        _name: str,
        _help: str,
        _offset: str,
        _type: str,
        _default: str = None,
        _min: str = None,
        _max: str = None,
        _flags: str = None,
        _unit: str = None,
    ) -> AVOption:
        return AVOption(
            name=_name.strip('"'),
            help=_help.strip('"'),
            offset=_offset,
            type=_type,
            default=_default,
            min=_min,
            max=_max,
            flags=_flags,
            unit=_unit and _unit.strip('"'),
        )

    for option_line in option_lines:
        if isinstance(option_line, str):
            continue

        # NOTE: convert all to string (otherwise default will be list)
        option_line = [str(k) for k in option_line]

        if len(option_line) < 4:
            continue

        kwargs = _aligns(option_line)
        output.append(_eval_avoption(**{"_" + k: v for k, v in kwargs.items()}))

    return output


def parse_av_option(text: str) -> dict[str, list[AVOption]]:
    text += """

static const AVOption ff_yadif_options[] = {
    { "mode", "specify the interlacing mode", __builtin_offsetof(YADIFContext, mode), AV_OPT_TYPE_INT, {.i64=YADIF_MODE_SEND_FRAME}, 0, 3, 16|(1<<16), "mode"},
    { "send_frame", "send one frame for each frame", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_MODE_SEND_FRAME}, (-2147483647 -1), 2147483647, 16|(1<<16), "mode" },
    { "send_field", "send one frame for each field", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_MODE_SEND_FIELD}, (-2147483647 -1), 2147483647, 16|(1<<16), "mode" },
    { "send_frame_nospatial", "send one frame for each frame, but skip spatial interlacing check", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_MODE_SEND_FRAME_NOSPATIAL}, (-2147483647 -1), 2147483647, 16|(1<<16), "mode" },
    { "send_field_nospatial", "send one frame for each field, but skip spatial interlacing check", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_MODE_SEND_FIELD_NOSPATIAL}, (-2147483647 -1), 2147483647, 16|(1<<16), "mode" },

    { "parity", "specify the assumed picture field parity", __builtin_offsetof(YADIFContext, parity), AV_OPT_TYPE_INT, {.i64=YADIF_PARITY_AUTO}, -1, 1, 16|(1<<16), "parity" },
    { "tff", "assume top field first", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_PARITY_TFF}, (-2147483647 -1), 2147483647, 16|(1<<16), "parity" },
    { "bff", "assume bottom field first", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_PARITY_BFF}, (-2147483647 -1), 2147483647, 16|(1<<16), "parity" },
    { "auto", "auto detect parity", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_PARITY_AUTO}, (-2147483647 -1), 2147483647, 16|(1<<16), "parity" },

    { "deint", "specify which frames to deinterlace", __builtin_offsetof(YADIFContext, deint), AV_OPT_TYPE_INT, {.i64=YADIF_DEINT_ALL}, 0, 1, 16|(1<<16), "deint" },
    { "all", "deinterlace all frames", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_DEINT_ALL}, (-2147483647 -1), 2147483647, 16|(1<<16), "deint" },
    { "interlaced", "only deinterlace frames marked as interlaced", 0, AV_OPT_TYPE_CONST, {.i64=YADIF_DEINT_INTERLACED}, (-2147483647 -1), 2147483647, 16|(1<<16), "deint" },

    { ((void*)0) }
};
"""

    output = {}
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)\[\]\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        output[filter] = _parse_av_option(option_str)
    return output
