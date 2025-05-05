import pytest
from syrupy.assertion import SnapshotAssertion

from ...dag.schema import Stream
from ..compile_cli import compile
from .cases import shared_cases


@pytest.mark.parametrize("graph", shared_cases)
def test_compile_cli(snapshot: SnapshotAssertion, graph: Stream) -> None:
    assert snapshot(name="compile-cli") == compile(graph)
