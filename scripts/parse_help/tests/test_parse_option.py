from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_filter import parse_section_tree
from ..parse_option import help_full_text


def test_help_full_text(snapshot: SnapshotAssertion) -> None:
    assert snapshot(name="help-full-text", extension_class=JSONSnapshotExtension) == parse_section_tree(
        help_full_text()
    )
