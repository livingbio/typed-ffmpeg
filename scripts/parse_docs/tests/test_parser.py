import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.filters import props

from ..parser import FilterDocument

test_data = pathlib.Path(__file__).parent / "data"


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_parse_filter_document(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    filter_document = FilterDocument.load(filepath)
    assert snapshot(exclude=props("path", "refs"), extension_class=JSONSnapshotExtension) == filter_document.model_dump(
        mode="json"
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == filter_document.parameters
