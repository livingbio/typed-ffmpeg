"""Tests for the Texinfo parser module."""

import tempfile
from pathlib import Path

import pytest

from ..cli import extract_texi_docs, process_texi_docs
from ..parse_texi import (
    TexiFilterSection,
    _parse_options_table,
    clean_texi_markup,
    parse_texi_sections,
)
from ..schema import FilterDocument

# --- clean_texi_markup tests ---


def test_clean_texi_var() -> None:
    assert clean_texi_markup("@var{x}") == "x"


def test_clean_texi_code() -> None:
    assert clean_texi_markup("@code{foo}") == "foo"


def test_clean_texi_samp() -> None:
    assert clean_texi_markup("@samp{bar}") == "bar"


def test_clean_texi_option() -> None:
    assert clean_texi_markup("@option{baz}") == "baz"


def test_clean_texi_emph() -> None:
    assert clean_texi_markup("@emph{italic}") == "italic"


def test_clean_texi_command() -> None:
    assert clean_texi_markup("@command{ffmpeg}") == "ffmpeg"


def test_clean_texi_file() -> None:
    assert clean_texi_markup("@file{input.mp4}") == "input.mp4"


def test_clean_texi_ref() -> None:
    assert clean_texi_markup("@ref{node,,display,manual}") == "display"


def test_clean_texi_ref_no_display() -> None:
    assert clean_texi_markup("@ref{node}") == "node"


def test_clean_texi_pxref() -> None:
    assert clean_texi_markup("@pxref{node,,display}") == "display"


def test_clean_texi_xref() -> None:
    assert clean_texi_markup("@xref{node,,display}") == "display"


def test_clean_texi_url() -> None:
    assert clean_texi_markup("@url{http://example.com}") == "http://example.com"


def test_clean_texi_nested() -> None:
    assert clean_texi_markup("Use @code{@var{x}} here") == "Use x here"


def test_clean_texi_multiple() -> None:
    assert clean_texi_markup("Set @var{x} to @code{0}") == "Set x to 0"


def test_clean_texi_plain_text() -> None:
    assert clean_texi_markup("plain text") == "plain text"


def test_clean_texi_at_escape() -> None:
    assert clean_texi_markup("@@") == "@"


def test_clean_texi_math() -> None:
    assert clean_texi_markup("@math{x+1}") == "x+1"


# --- _parse_options_table tests ---


def test_parse_options_simple_table() -> None:
    body = """\
@table @option
@item duration, d
Specify the duration of the cross fade effect.

@item nb_samples, ns
Specify the number of samples.
@end table
"""
    result = _parse_options_table(body)
    assert "duration" in result
    assert "d" in result
    assert "nb_samples" in result
    assert "ns" in result
    assert (
        "duration" in result["duration"].lower()
        or "cross fade" in result["duration"].lower()
    )


def test_parse_options_single_name() -> None:
    body = """\
@table @option
@item gain
Set the gain.
@end table
"""
    result = _parse_options_table(body)
    assert "gain" in result
    assert "gain" in result["gain"].lower() or "set" in result["gain"].lower()


def test_parse_options_no_table() -> None:
    result = _parse_options_table("Just some text with no table.")
    assert result == {}


def test_parse_options_multiline_desc() -> None:
    body = """\
@table @option
@item mode
Set the mode.
This can be one of several values.
Default is auto.
@end table
"""
    result = _parse_options_table(body)
    assert "mode" in result
    assert "several values" in result["mode"]


def test_parse_options_nested_table() -> None:
    body = """\
@table @option
@item outer
Outer description.

@table @samp
@item inner_val
Inner value description.
@end table

@item second
Second option.
@end table
"""
    result = _parse_options_table(body)
    assert "outer" in result
    assert "second" in result


# --- parse_texi_sections tests ---

SAMPLE_TEXI = """\
@chapter Audio Filters

@section acrossfade

Apply cross fade from one input audio stream to another input audio stream.
The cross fade is applied for specified duration near the end of first stream.

@table @option
@item nb_samples, ns
Specify the number of samples for which the cross fade effect has to last.

@item duration, d
Specify the duration of the cross fade effect.
@end table

@subsection Examples

Some example here.

@section adelay

Delay one or more audio channels.

@table @option
@item delays
Set list of delays in milliseconds.
@end table
"""


def test_parse_sections_multiple() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    names = [s.filter_names for s in sections]
    assert ("acrossfade",) in names
    assert ("adelay",) in names


def test_parse_sections_description() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    acrossfade = [s for s in sections if "acrossfade" in s.filter_names][0]
    assert "cross fade" in acrossfade.description


def test_parse_sections_parameters() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    acrossfade = [s for s in sections if "acrossfade" in s.filter_names][0]
    assert "nb_samples" in acrossfade.parameter_descs
    assert "ns" in acrossfade.parameter_descs
    assert "duration" in acrossfade.parameter_descs
    assert "d" in acrossfade.parameter_descs


def test_parse_sections_multi_name() -> None:
    texi = """\
@chapter Filters

@section aderivative, aintegral

Compute the derivative or integral of the audio stream.
"""
    sections = parse_texi_sections(texi)
    assert len(sections) == 1
    assert sections[0].filter_names == ("aderivative", "aintegral")


def test_parse_sections_desc_stops_before_table() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    acrossfade = [s for s in sections if "acrossfade" in s.filter_names][0]
    assert "@table" not in acrossfade.description
    assert "nb_samples" not in acrossfade.description


def test_parse_sections_raw_body() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    acrossfade = [s for s in sections if "acrossfade" in s.filter_names][0]
    assert "@table @option" in acrossfade.raw_body


def test_parse_sections_ignores_subsection() -> None:
    sections = parse_texi_sections(SAMPLE_TEXI)
    names_flat = [n for s in sections for n in s.filter_names]
    assert "Examples" not in names_flat


# --- TexiFilterSection dataclass test ---


def test_texi_filter_section_fields() -> None:
    section = TexiFilterSection(
        filter_names=("test",),
        description="A test filter.",
        raw_body="raw body here",
        parameter_descs={"p": "desc"},
    )
    assert section.filter_names == ("test",)
    assert section.description == "A test filter."
    assert section.raw_body == "raw body here"
    assert section.parameter_descs == {"p": "desc"}


# --- FilterDocument texi field tests ---


def test_texi_description_overrides_html() -> None:
    doc = FilterDocument(
        section_index="",
        hash="test",
        title="test",
        body="<p>HTML description</p>",
        filter_names=("test",),
        _texi_description="Texi description",
    )
    assert doc.description == "Texi description"


def test_texi_parameter_descs_overrides_html() -> None:
    doc = FilterDocument(
        section_index="",
        hash="test",
        title="test",
        body="<dl><dt><samp>x</samp></dt><dd>HTML desc</dd></dl>",
        filter_names=("test",),
        _texi_parameter_descs={"x": "Texi param desc"},
    )
    assert doc.parameter_descs == {"x": "Texi param desc"}


def test_falls_back_to_html_when_texi_none() -> None:
    doc = FilterDocument(
        section_index="1.1",
        hash="test",
        title="1.1 test",
        body="<p>HTML description</p>",
        filter_names=("test",),
    )
    assert "HTML description" in doc.description


def test_texi_fields_default_none() -> None:
    doc = FilterDocument(
        section_index="",
        hash="test",
        title="test",
        body="",
        filter_names=("test",),
    )
    assert doc._texi_description is None
    assert doc._texi_parameter_descs is None


# --- process_texi_docs / extract_texi_docs tests ---

SAMPLE_TEXI_FILE = """\
@chapter Audio Filters

@section acrossfade

Apply cross fade from one input audio stream to another input audio stream.

@table @option
@item nb_samples, ns
Specify the number of samples.

@item duration, d
Specify the duration.
@end table

@section adelay

Delay one or more audio channels.

@table @option
@item delays
Set list of delays in milliseconds.
@end table
"""


def _write_texi_tempfile() -> Path:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".texi", delete=False)
    f.write(SAMPLE_TEXI_FILE)
    f.flush()
    f.close()
    return Path(f.name)


def test_process_texi_docs_returns_filter_documents() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    assert len(docs) == 2
    assert all(isinstance(d, FilterDocument) for d in docs)


def test_process_texi_docs_filter_names() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    names = [d.filter_names for d in docs]
    assert ("acrossfade",) in names
    assert ("adelay",) in names


def test_process_texi_docs_description() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    acrossfade = [d for d in docs if "acrossfade" in d.filter_names][0]
    assert "cross fade" in acrossfade.description


def test_process_texi_docs_hash() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    acrossfade = [d for d in docs if "acrossfade" in d.filter_names][0]
    assert acrossfade.hash == "acrossfade"


def test_process_texi_docs_section_index() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    assert all(d.section_index == "" for d in docs)


def test_process_texi_docs_body() -> None:
    docs = process_texi_docs(_write_texi_tempfile())
    acrossfade = [d for d in docs if "acrossfade" in d.filter_names][0]
    assert "@table @option" in acrossfade.body


def test_extract_texi_docs_finds_filter() -> None:
    doc = extract_texi_docs("acrossfade", _write_texi_tempfile())
    assert "acrossfade" in doc.filter_names


def test_extract_texi_docs_raises_for_unknown() -> None:
    with pytest.raises(ValueError, match="Unknown filter"):
        extract_texi_docs("nonexistent", _write_texi_tempfile())
