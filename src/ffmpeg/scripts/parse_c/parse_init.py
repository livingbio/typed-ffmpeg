import re


def parse_init(text: str, function_name) -> str | None:
    match = re.findall(r"(^static [^\n]*?%s\(AVFilterContext.*?\n})" % function_name, text, re.DOTALL | re.MULTILINE)
    if match:
        return match[0]

    return None
