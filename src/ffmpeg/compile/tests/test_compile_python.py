import pytest
from syrupy.assertion import SnapshotAssertion

from ...dag.schema import Stream
from ..compile_python import compile_python
from .cases import shared_cases


@pytest.mark.parametrize("graph", shared_cases)
def test_compile_python(graph: Stream, snapshot: SnapshotAssertion) -> None:
    assert snapshot(name="compile-python") == compile_python(graph)
