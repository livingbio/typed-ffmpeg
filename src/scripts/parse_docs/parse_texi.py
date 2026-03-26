"""Texinfo (.texi) parser for extracting FFmpeg filter documentation sections."""

import re
from dataclasses import dataclass


def clean_texi_markup(text: str) -> str:
    """
    Strip Texinfo commands, leaving plain text.

    Handles commands like @var{x}, @code{x}, @ref{node,,display,manual}, etc.

    Args:
        text: Text containing Texinfo markup

    Returns:
        Plain text with markup stripped

    """
    # Replace @@ with a placeholder, then restore
    text = text.replace("@@", "\x00AT\x00")

    # Handle @ref/@pxref/@xref: extract display text (3rd arg) or node name (1st arg)
    def _ref_replace(m: re.Match[str]) -> str:
        args = m.group(2).split(",")
        # Display text is the 3rd argument if present and non-empty
        if len(args) >= 3 and args[2].strip():
            return args[2].strip()
        return args[0].strip()

    text = re.sub(r"@(ref|pxref|xref)\{([^}]*)\}", _ref_replace, text)

    # Handle simple @command{content} patterns — process innermost first (for nesting)
    # Repeat until no more nested commands remain
    simple_cmd = re.compile(
        r"@(?:var|code|samp|option|emph|command|file|url|math|strong|b|i|t|r|w|dfn|cite|acronym|env|kbd)\{([^{}]*)\}"
    )
    while simple_cmd.search(text):
        text = simple_cmd.sub(r"\1", text)

    # Restore @@ -> @
    text = text.replace("\x00AT\x00", "@")

    return text


@dataclass(frozen=True)
class TexiFilterSection:
    """A parsed filter section from a Texinfo file."""

    filter_names: tuple[str, ...]
    """Filter names (e.g. ('aderivative', 'aintegral'))."""

    description: str
    """Description text (before first @table/@subsection/@itemize), markup stripped."""

    raw_body: str
    """Raw Texinfo body of the section (between @section lines)."""

    parameter_descs: dict[str, str]
    """Option name -> description text mapping."""


def _parse_options_table(body: str) -> dict[str, str]:
    """
    Parse the first top-level @table @option block into option name -> description.

    Args:
        body: Texinfo body text that may contain @table @option blocks

    Returns:
        Dictionary mapping option names to their description text

    """
    # Find the first @table @option ... @end table block (top-level only)
    # We need to handle nested @table blocks by counting depth
    lines = body.split("\n")
    in_table = False
    depth = 0
    table_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("@table") and not in_table and depth == 0:
            if "@option" in stripped:
                in_table = True
                depth = 1
                continue
        elif in_table:
            if stripped.startswith("@table"):
                depth += 1
            elif stripped == "@end table":
                depth -= 1
                if depth == 0:
                    break
            if depth == 1:
                table_lines.append(line)

    if not table_lines:
        return {}

    # Parse @item entries at depth 1
    result: dict[str, str] = {}
    current_names: list[str] = []
    current_desc_lines: list[str] = []

    for line in table_lines:
        stripped = line.strip()
        if stripped.startswith("@item "):
            # Save previous item
            if current_names:
                desc = clean_texi_markup("\n".join(current_desc_lines).strip())
                for name in current_names:
                    result[name] = desc

            # Parse new item names
            names_str = stripped[len("@item ") :]
            current_names = [n.strip() for n in names_str.split(",") if n.strip()]
            current_desc_lines = []
        elif stripped.startswith("@table"):
            # Skip nested table content — collect it but don't parse items from it
            # We already handle depth tracking above, but items inside nested tables
            # won't appear here since we only keep depth==1 lines
            current_desc_lines.append(line)
        else:
            current_desc_lines.append(line)

    # Save last item
    if current_names:
        desc = clean_texi_markup("\n".join(current_desc_lines).strip())
        for name in current_names:
            result[name] = desc

    return result


def parse_texi_sections(texi_content: str) -> list[TexiFilterSection]:
    """
    Parse Texinfo content into filter sections.

    Splits on @section lines (not @subsection) and extracts description,
    raw body, and parameter options for each section.

    Args:
        texi_content: Full Texinfo file content

    Returns:
        List of TexiFilterSection objects

    """
    # Split on @section lines (but not @subsection)
    # Pattern: line starting with @section followed by the section name
    section_pattern = re.compile(r"^@section\s+(.+)$", re.MULTILINE)

    splits = list(section_pattern.finditer(texi_content))
    if not splits:
        return []

    sections: list[TexiFilterSection] = []

    for i, match in enumerate(splits):
        name_str = match.group(1).strip()
        filter_names = tuple(n.strip() for n in name_str.split(",") if n.strip())

        # Body is from end of @section line to start of next @section (or end of file)
        body_start = match.end()
        body_end = splits[i + 1].start() if i + 1 < len(splits) else len(texi_content)
        raw_body = texi_content[body_start:body_end].strip()

        # Extract description: text before first @table, @subsection, or @itemize
        desc_end_pattern = re.compile(r"^(@table|@subsection|@itemize)", re.MULTILINE)
        desc_match = desc_end_pattern.search(raw_body)
        if desc_match:
            desc_text = raw_body[: desc_match.start()].strip()
        else:
            desc_text = raw_body.strip()

        description = clean_texi_markup(desc_text)

        # Parse parameters
        parameter_descs = _parse_options_table(raw_body)

        sections.append(
            TexiFilterSection(
                filter_names=filter_names,
                description=description,
                raw_body=raw_body,
                parameter_descs=parameter_descs,
            )
        )

    return sections
