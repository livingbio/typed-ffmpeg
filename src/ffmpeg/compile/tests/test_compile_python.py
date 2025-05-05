import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...dag.schema import Stream
from ..compile_python import compile, parse
from ..validate import validate
from .cases import shared_cases


@pytest.mark.parametrize("fluent", [True, False])
@pytest.mark.parametrize("graph", shared_cases)
def test_compile_python(
    graph: Stream, fluent: bool, snapshot: SnapshotAssertion
) -> None:
    r = compile(graph, fluent=fluent)
    assert snapshot(name="compile-python", extension_class=JSONSnapshotExtension) == r

    assert parse(r) == validate(graph, auto_fix=True), (
        "parse result should be equal to the original graph"
    )
