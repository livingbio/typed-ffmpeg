import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion

from ..signature import generate_json_schema, parse_filter_document, parse_schema

test_data = pathlib.Path(__file__).parent / "data"


@pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path", "query", "body"])
@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_parse_schema(filepath: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    info = parse_filter_document(filepath.read_text())
    assert snapshot == [k.model_dump(mode="json") for k in parse_schema(info)]


@pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path", "query", "body"])
@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_generate_json_schema(filepath: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    info = parse_filter_document(filepath.read_text())
    assert snapshot == generate_json_schema(info)
