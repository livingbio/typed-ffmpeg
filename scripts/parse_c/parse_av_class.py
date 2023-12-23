import re

from .parse_c_structure import parse_c_structure
from .schema import AVClass


def parse_av_class(text: str) -> dict[str, AVClass]:
    output = {}
    for filter, filter_desc in re.findall(r"static const AVClass ([\w\_]+) = ({.*?});", text, re.DOTALL | re.MULTILINE):
        descs: list[str] = parse_c_structure(filter_desc)
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip(' "')

        output[filter] = AVClass(
            class_name=config[".class_name"],
            item_name=config[".item_name"],
            option=config[".option"],
            version=config.get(".version"),
            log_level_offset_offset=config.get(".log_level_offset_offset"),
            parent_log_context_offset=config.get(".parent_log_context_offset"),
            child_next=config.get(".child_next"),
            child_class_next=config.get(".child_class_next"),
            category=config.get(".category"),
        )
    return output
