import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ffmpeg.dag.nodes import GlobalStream

from ...common.serialize import loads
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
    assert snapshot(
        name="compile-python", extension_class=JSONSnapshotExtension
    ) == r.split("\n")

    assert parse(r) == validate(graph, auto_fix=True), (
        "parse result should be equal to the original graph"
    )


def test_compile_python_simple_global_args(snapshot: SnapshotAssertion) -> None:
    node = loads(
        """{"inputs":[{"node":{"filename":"output.mp4","inputs":[{"node":{"filename":"input.mp4","inputs":[],"kwargs":{},"__class__":"InputNode"},"index":null,"__class__":"AVStream"}],"kwargs":{},"__class__":"OutputNode"},"index":null,"__class__":"OutputStream"}],"kwargs":{},"__class__":"GlobalNode"}"""
    )
    stream = GlobalStream(node=node)
    r = compile(stream, fluent=True)
    assert snapshot(
        name="compile-python", extension_class=JSONSnapshotExtension
    ) == r.split("\n")
