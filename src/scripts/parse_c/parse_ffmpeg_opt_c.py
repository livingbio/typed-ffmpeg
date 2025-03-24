#!/usr/bin/env python3
"""
Module for parsing FFmpeg options from C source code.

This module extracts FFmpeg command-line options by parsing the options array
in the ffmpeg_opt.c file. It identifies option names, types, flags, help text,
and other properties to build a structured representation of FFmpeg's CLI options.
"""

import re
from dataclasses import replace

from ffmpeg.common.schema import FFMpegOption, FFMpegOptionFlag

from .parse_c_structure import parse_c_structure


def parse_ffmpeg_opt_c(text: str) -> list[FFMpegOption]:
    """
    Parse the ffmpeg option from C code

    Args:
        text: The text to parse

    Returns:
        The parsed options
    """
    match = re.findall(
        r"const OptionDef options\[\] = (\{.*?\n\})", text, re.MULTILINE | re.DOTALL
    )
    data = parse_c_structure(match[0])

    output: dict[str, FFMpegOption] = {}

    for line in data:
        name = None
        type = None
        flags = None
        help = None
        arg_name = None
        canon = None

        if len(line) == 5:
            name, type, flags, _, help = line
        elif len(line) == 6:
            name, type, flags, _, help, arg_name = line
        elif len(line) == 7:
            name, type, flags, _, help, arg_name, canon = line
        elif len(line) == 1:
            continue
        else:  # pragma: no cover
            raise ValueError(line)

        name = name.strip('"')
        help = help.strip('"')
        arg_name = arg_name.strip('"') if arg_name else None
        flags = flags.replace("\n", "")
        flags = eval(flags)
        output[name] = FFMpegOption(
            name=name, type=type, flags=flags, help=help, argname=arg_name, canon=canon
        )

    # process canon
    for key, opt in output.items():
        if opt.flags & FFMpegOptionFlag.OPT_HAS_CANON:
            assert opt.canon
            ref = opt.canon.split("=")[1].strip().strip('"')
            output[key] = replace(opt, type=output[ref].type)

    return list(output.values())
