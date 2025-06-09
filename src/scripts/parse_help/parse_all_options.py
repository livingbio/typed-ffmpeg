import re
import subprocess

from .schema import FFMpegAVOption, FFMpegOptionChoice


def parse_all_options(help_text: str) -> list[FFMpegAVOption]:
    output: list[FFMpegAVOption] = []
    section = None
    last_option: FFMpegAVOption | None = None
    choices: list[FFMpegOptionChoice] = []

    re_option_pattern = re.compile(
        r"(?P<short_name>[\w\-]+)\s+\<(?P<type>[\w]+)\>\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )
    re_choice_pattern = re.compile(
        r"(?P<short_name>[\w\-\s]+)\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )
    re_value_pattern = re.compile(
        r"(?P<short_name>[\w\-\s]+)\s+(?P<value>[\w\-]+)\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )

    for line in help_text.split("\n"):
        # Empty line
        if not line.strip():
            if last_option:
                output.append(
                    FFMpegAVOption(
                        section=last_option.section,
                        name=last_option.name.strip().strip("-"),
                        type=last_option.type,
                        flags=last_option.flags,
                        help=last_option.help,
                        choices=tuple(choices),
                    )
                )
                last_option = None
                choices = []
            continue

        # AVOptions section
        if re.findall(r"^[\w]+[\s]+AVOptions:", line):
            section = line
            continue

        if not section:
            continue

        # Choice line
        if line.startswith("     "):
            assert last_option
            if last_option.type == "flags":
                choice = re_choice_pattern.findall(line)
                assert choice, f"No choice found in line: {line}"
                name, flags, help = choice[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        help=help,
                        value=name.strip(),
                    )
                )
            elif last_option.type == "string":
                choice = re_choice_pattern.findall(line)
                assert choice, f"No choice found in line: {line}"
                name, flags, help = choice[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        help=help,
                        value=name.strip(),
                    )
                )
            else:
                v = re_value_pattern.findall(line)
                assert v, f"No value found in line: {line}"
                name, value, flags, help = v[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        value=value,
                        help=help,
                    )
                )

            continue

        # Option line
        if line.startswith("  "):
            if last_option:
                output.append(
                    FFMpegAVOption(
                        section=last_option.section,
                        name=last_option.name.strip().strip("-"),
                        type=last_option.type,
                        flags=last_option.flags,
                        help=last_option.help,
                        choices=tuple(choices),
                    )
                )
            last_option = None
            choices = []

            p = re_option_pattern.findall(line)
            assert p, f"No option found in line: {line}"

            last_option = FFMpegAVOption(
                section=section,
                name=p[0][0].strip(),
                type=p[0][1],
                flags=p[0][2],
                help=p[0][3],
            )

    return output


def extract_options_help_text() -> str:
    """
    Get the help text for a filter.

    Returns:
        The help text.
    """

    result = subprocess.run(
        ["ffmpeg", "-h", "full", "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def extract_avoption_info_from_help() -> list[FFMpegAVOption]:
    text = extract_options_help_text()
    return parse_all_options(text)
