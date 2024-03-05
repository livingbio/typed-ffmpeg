import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.filters import props

from ..schema import FilterDocument

test_data = pathlib.Path(__file__).parent / "test_schema"


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_parse_filter_document(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    filter_document = FilterDocument.load(filepath)
    assert snapshot(exclude=props("path", "refs"), extension_class=JSONSnapshotExtension) == filter_document.model_dump(
        mode="json"
    )
    assert snapshot(extension_class=JSONSnapshotExtension, name="parameters") == filter_document.parameter_descs
    assert snapshot(extension_class=JSONSnapshotExtension, name="properties") == {
        "description": filter_document.description,
        "url": filter_document.url,
    }
