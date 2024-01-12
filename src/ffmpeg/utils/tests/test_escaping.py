import pytest
from syrupy.assertion import SnapshotAssertion

from ..escaping import escape


@pytest.mark.parametrize(
    "text", ["this is a 'string': may contain one, or more, special characters", "this is a string[0]"]
)
def test_escaping(snapshot: SnapshotAssertion, text: str) -> None:
    assert snapshot == escape(text, "\\'[],;")
