import re

from .parse_c_structure import parse_c_structure
from .schema import AVFilter, AVFilterFlags


def parse_av_filter_flags(text: str | None) -> int:
    if text is None:
        return 0

    text = text.replace("\n", "")

    def convert_avfilter_flag(match) -> str:
        return str(AVFilterFlags[match.group(1)].value)

    if "AVFILTER" in text:
        text = re.sub(r"(AVFILTER_FLAG_\w+)", convert_avfilter_flag, text)

    return eval(text)


def parse_av_filter(text: str) -> dict[str, AVFilter]:
    output = {}
    for filter, filter_desc in re.findall(r"const AVFilter ([\w\_]+)\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE):
        descs: list[str] = parse_c_structure(filter_desc)
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip('" ')

        output[filter] = AVFilter(
            name=config[".name"],
            description=config[".description"],
            priv_class=config.get(".priv_class"),
            flags=parse_av_filter_flags(config.get(".flags")),
            inputs=config.get(".inputs"),
            outputs=config.get(".outputs"),
        )
    return output
