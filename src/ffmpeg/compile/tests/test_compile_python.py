import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...dag.schema import Stream
from ..compile_python import compile_python
from .cases import shared_cases


@pytest.mark.parametrize("fluent", [True, False])
@pytest.mark.parametrize("graph", shared_cases)
def test_compile_python(
    graph: Stream, fluent: bool, snapshot: SnapshotAssertion
) -> None:
    r = compile_python(graph, fluent=fluent)
    assert snapshot(name="compile-python", extension_class=JSONSnapshotExtension) == r

    # exec(r)
    # assert result == graph
