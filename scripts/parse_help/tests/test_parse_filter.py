import pytest
from parse_c.helper import dump
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..parse_filter import extract_avfilter_info_from_help, help_full_text, help_text, parse_section_tree


def test_help_full_text(snapshot: SnapshotAssertion) -> None:
    assert snapshot(name="help-full-text", extension_class=JSONSnapshotExtension) == parse_section_tree(
        help_full_text()
    )


@pytest.mark.parametrize(
    "filter_name",
    [
        "bitplanenoise",
        "anlmf",
        "negate",
        "abuffersink",
        "abuffer",
        "afade",
        "trim",
        "scale",
        "blend",
        "adeclip",
        "concat",
        "scale2ref",
    ],
)
def test_help_text(snapshot: SnapshotAssertion, filter_name: str) -> None:
    assert snapshot(name="help-text", extension_class=SingleFileSnapshotExtension) == help_text(
        filter_name=filter_name
    ).encode("utf-8")
    assert snapshot(name="extract-help-text", extension_class=JSONSnapshotExtension) == dump(
        extract_avfilter_info_from_help(filter_name=filter_name)
    )
    assert snapshot(name="parse-section-tree", extension_class=JSONSnapshotExtension) == parse_section_tree(
        text=help_text(filter_name=filter_name)
    )
