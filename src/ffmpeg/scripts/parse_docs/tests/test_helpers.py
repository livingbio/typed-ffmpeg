import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..helpers import convert_html_to_markdown

test_data = pathlib.Path(__file__).parent / "test_helpers"


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_convert_html_to_markdown(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    html_content = filepath.read_text()
    assert snapshot(extension_class=SingleFileSnapshotExtension) == convert_html_to_markdown(html_content).encode(
        "utf8"
    )
