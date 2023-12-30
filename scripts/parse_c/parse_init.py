import re


def parse_init(text: str) -> dict[str, str] | None:
    match = re.findall(
        r"(static __attribute__\(\(cold\)\) int ([\w_]+?)\(AVFilterContext.*?\n})", text, re.DOTALL | re.MULTILINE
    )
    if match:
        return {name: func for func, name in match}
    return None
