import re

from .parse_c_structure import parse_c_structure
from .schema import AVFilterPad


def parse_av_filter_pad(text: str) -> dict[str, list[AVFilterPad]]:
    output = {}
    for filter_pad, filter_pad_desc in re.findall(
        r"static const AVFilterPad ([\w\_]+)\[\]\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        key_values: list[str]
        item = []
        for key_values in parse_c_structure(filter_pad_desc):
            config = {}
            for key_value in key_values:
                if "=" not in key_value:
                    continue

                var, value = key_value.split("=", 1)
                config[var.strip()] = value.strip('" ')

            item.append(
                AVFilterPad(
                    name=config[".name"],
                    type=config[".type"],
                )
            )

        output[filter_pad] = item
    return output
