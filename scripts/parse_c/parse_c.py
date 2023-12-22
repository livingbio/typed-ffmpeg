import pathlib
import re

import jinja2

from .parse_option import extract_av_options
from .schema import AVFilter

template_path = pathlib.Path(__file__).parent / "templates"


def parse_c(path: pathlib.Path) -> list[AVFilter]:
    with path.open() as f:
        code = f.read()

    macro_pattern = r'WIN_FUNC_OPTION\("([^"]+)", ([^,]+), ([^,]+), ([^)]+)\)'

    def win_func_option(win_func_opt_name, win_func_offset, flag, default_window_func) -> str:
        with (template_path / "win_func_option.tmpl").open() as ifile:
            return jinja2.Template(ifile.read()).render(
                win_func_opt_name=win_func_opt_name,
                win_func_offset=win_func_offset,
                flag=flag,
                default_window_func=default_window_func,
            )

    # Function to perform the replacement
    def replace_macro(match):
        win_func_opt_name = match.group(1)
        win_func_offset = match.group(2)
        flag = match.group(3)
        default_window_func = match.group(4)
        return win_func_option(win_func_opt_name, win_func_offset, flag, default_window_func)

    # Replace the macro in the string
    code = re.sub(macro_pattern, replace_macro, code)
    return extract_av_options(code)


def parse_all_filter_names(path: pathlib.Path) -> list[tuple[str, str]]:
    with path.open() as f:
        code = f.read()

    output = []
    for name in re.findall(r"extern const AVFilter ([\w\_]+);", code):
        _, flag, name = name.split("_", 2)
        output.append((flag, name))

    return output
