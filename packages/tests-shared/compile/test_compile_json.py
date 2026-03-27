import json

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ffmpeg.compile.compile_json import compile, parse
from ffmpeg.compile.validate import validate
from ffmpeg.dag.schema import Stream

from .cases import shared_cases


@pytest.mark.parametrize("graph", shared_cases)
def test_compile_json(graph: Stream, snapshot: SnapshotAssertion) -> None:
    r = compile(graph)
    assert snapshot(
        name="compile-json", extension_class=JSONSnapshotExtension
    ) == json.loads(r)

    assert parse(r) == validate(graph, auto_fix=True), (
        "parse result should be equal to the original graph"
    )
