import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..parse import help_text


@pytest.mark.parametrize("filter_name", ["trim", "scale", "blend", "adeclip"])
def test_help_text(snapshot: SnapshotAssertion, filter_name: str) -> None:
    assert snapshot(extension_class=SingleFileSnapshotExtension) == help_text(filter_name=filter_name).encode("utf-8")
