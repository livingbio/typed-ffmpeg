import pathlib
from dataclasses import asdict

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from syrupy.filters import props

from ..helpers import convert_html_to_markdown, parse_filter_document

test_data = pathlib.Path(__file__).parent / "test_helpers"


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_convert_html_to_markdown(
    snapshot: SnapshotAssertion, filepath: pathlib.Path
) -> None:
    html_content = filepath.read_text()
    assert snapshot(
        extension_class=SingleFileSnapshotExtension
    ) == convert_html_to_markdown(html_content).encode("utf8")


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_parse_filter_document(
    snapshot: SnapshotAssertion, filepath: pathlib.Path
) -> None:
    html_content = filepath.read_text()
    filter_document = parse_filter_document(html_content)

    assert snapshot(
        exclude=props("path", "refs"), extension_class=JSONSnapshotExtension
    ) == asdict(filter_document)
    assert (
        snapshot(extension_class=JSONSnapshotExtension, name="parameters")
        == filter_document.parameter_descs
    )
    assert snapshot(extension_class=JSONSnapshotExtension, name="properties") == {
        "description": filter_document.description,
        "url": filter_document.url,
    }
