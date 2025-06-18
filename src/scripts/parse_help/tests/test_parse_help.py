from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_help import extract


def test_extract_options_from_help(snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == extract()
