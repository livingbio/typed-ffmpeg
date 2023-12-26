import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion

from ..tmp.code_gen import generate_class, generate_filter_to_method
from ..tmp.signature import Filter

test_data = pathlib.Path(__file__).parent / "data"


@pytest.mark.parametrize("filepath", test_data.glob("*.json"), ids=lambda x: x.name)
def test_generate_filter_to_method(filepath: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    filter = Filter.load(filepath)
    assert snapshot == generate_filter_to_method(filter)


def test_generate_class(snapshot: SnapshotAssertion) -> None:
    filters = [Filter.load(filepath) for filepath in test_data.glob("*.json")]
    assert snapshot == generate_class(filters)
