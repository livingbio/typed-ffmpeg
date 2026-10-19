"""
Detect which filter options FFmpeg evaluates as expressions.

FFmpeg declares expression options (e.g. ``drawbox=x=(iw-w)/2``) as plain
``AV_OPT_TYPE_STRING``, so ``ffmpeg -h filter=...`` cannot tell them apart from
free-form text. The libavfilter source can: an option is an expression when the
struct field it is stored in is passed to ``av_expr_parse`` /
``av_expr_parse_and_eval`` (directly, through a helper function, or through a
token-pasting macro).
"""

import re
from collections import defaultdict
from pathlib import Path

EXPR_FUNCTIONS = frozenset({"av_expr_parse", "av_expr_parse_and_eval"})

_OPTION_RE = re.compile(
    r'\{\s*"(?P<name>[^"]+)"\s*,'  # option name
    r'\s*(?:(?:"(?:[^"\\]|\\.)*"\s*)+|NULL)\s*,'  # help text
    r"\s*(?:OFFSET\s*\(|offsetof\s*\(\s*\w+\s*,)\s*(?P<field>[^)]*?)\s*\)\s*,"  # field
    r"\s*AV_OPT_TYPE_STRING\b"
)
_FILTER_NAME_RE = re.compile(r'\.(?:p\.)?name\s*=\s*"(\w+)"')
_FUNCTION_RE = re.compile(
    r"^[A-Za-z_][\w\s\*]*?\b(\w+)\s*\([^;{}]*\)\s*\{", re.MULTILINE
)
_MACRO_RE = re.compile(r"^#\s*define\s+(\w+)\(([^)]*)\)(.*)$", re.MULTILINE)
_CALL_RE = re.compile(r"\b(\w+)\s*\(")
_PREFIX_RE = re.compile(r"^(?:vf|af|avf|vsrc|asrc|avsrc|vsink|asink|f|src|sink)_")


def _strip_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.DOTALL)
    text = re.sub(r"//[^\n]*", "", text)
    # join macro continuation lines so a #define is a single line
    return re.sub(r"\\\n", " ", text)


def _call_arguments(text: str, functions: set[str]) -> list[str]:
    """
    Collect the arguments of every call to one of ``functions``.

    Args:
        text: The C source code
        functions: The function (or macro) names to look for

    Returns:
        The raw text between the parentheses of each call

    """
    output = []
    for match in _CALL_RE.finditer(text):
        if match.group(1) not in functions:
            continue
        depth, start = 1, match.end()
        for index in range(start, len(text)):
            if text[index] == "(":
                depth += 1
            elif text[index] == ")":
                depth -= 1
                if depth == 0:
                    output.append(text[start:index])
                    break
    return output


def _functions_calling(text: str, callees: set[str]) -> set[str]:
    """
    Find the functions that call one of ``callees``.

    Args:
        text: The C source code
        callees: The function names to look for

    Returns:
        Names of functions defined in ``text`` whose body calls one of ``callees``

    """
    starts = [(m.start(), m.group(1)) for m in _FUNCTION_RE.finditer(text)]
    output = set()
    for index, (position, name) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else len(text)
        body = text[position:end]
        if any(re.search(rf"\b{callee}\s*\(", body) for callee in callees):
            output.add(name)
    return output


def _field_name(field: str) -> str:
    """
    Normalize an ``OFFSET(...)`` argument to a struct field name.

    Args:
        field: The argument, e.g. ``expr_str[Y]`` or ``opts.x``

    Returns:
        The field name, e.g. ``expr_str`` or ``x``

    """
    return re.sub(r"\[.*?\]", "", field).split(".")[-1].strip()


def _pasted_fields(text: str, expr_functions: set[str]) -> set[str]:
    """
    Fields reached through token-pasting macros.

    e.g. ``#define SET_SIZE_EXPR(name, opt) ... av_expr_parse_and_eval(&res,
    rot->name##_expr_str, ...)`` invoked as ``SET_SIZE_EXPR(outh, ...)`` parses
    the field ``outh_expr_str``.

    Args:
        text: The C source code
        expr_functions: Functions known to parse their arguments as expressions

    Returns:
        The struct field names parsed as expressions through such macros

    """
    fields = set()
    for match in _MACRO_RE.finditer(text):
        macro, params, body = match.groups()
        if not any(re.search(rf"\b{fn}\s*\(", body) for fn in expr_functions):
            continue
        params_list = [p.strip() for p in params.split(",")]
        pasted = re.findall(r"(?:->|\.)\s*(\w+)\s*##\s*(\w+)", body)
        if not pasted:
            continue
        for args in _call_arguments(text[match.end() :], {macro}):
            values = [a.strip() for a in args.split(",")]
            for param, suffix in pasted:
                if param in params_list and params_list.index(param) < len(values):
                    fields.add(values[params_list.index(param)] + suffix)
    return fields


def parse_expression_options(text: str) -> tuple[set[str], set[str]]:
    """
    Parse one libavfilter C file.

    Args:
        text: The C source code

    Returns:
        The filter names defined in the file and the names of its string
        options that are parsed as FFmpeg expressions.

    """
    text = _strip_comments(text)
    options = [
        (m.group("name"), _field_name(m.group("field")))
        for m in _OPTION_RE.finditer(text)
    ]
    if not options:
        return set(_FILTER_NAME_RE.findall(text)), set()

    expr_functions = set(EXPR_FUNCTIONS)
    # follow helpers (and helpers of helpers) that forward to av_expr_parse
    while True:
        callers = _functions_calling(text, expr_functions) - expr_functions
        if not callers:
            break
        expr_functions |= callers

    call_args = " ".join(_call_arguments(text, expr_functions))
    expr_fields = {
        field
        for _, field in options
        if re.search(rf"(?:->|\.)\s*{re.escape(field)}\b", call_args)
    }
    expr_fields |= _pasted_fields(text, expr_functions)

    return (
        set(_FILTER_NAME_RE.findall(text)),
        {name for name, field in options if field in expr_fields},
    )


def extract_expression_options(
    source_folder: Path, filter_names: set[str]
) -> dict[str, list[str]]:
    """
    Scan libavfilter for options evaluated as expressions.

    Args:
        source_folder: Root of an extracted FFmpeg source tree
        filter_names: Names of the filters reported by the ffmpeg binary; any
            other ``.name = "..."`` match (e.g. pad names) is ignored

    Returns:
        Mapping of filter name to the sorted names of its expression options

    """
    output: dict[str, set[str]] = defaultdict(set)
    for path in sorted((source_folder / "libavfilter").rglob("*.c")):
        names, options = parse_expression_options(path.read_text(errors="ignore"))
        if not options:
            continue
        names = (names | {_PREFIX_RE.sub("", path.stem)}) & filter_names
        for name in names:
            output[name] |= options
    return {name: sorted(output[name]) for name in sorted(output)}
