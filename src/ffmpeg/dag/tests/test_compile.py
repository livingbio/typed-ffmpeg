import pytest
from syrupy.assertion import SnapshotAssertion

from ...base import input
from ..compile import compile, compile_to_python, is_simple_graph
from ..schema import Stream


@pytest.mark.parametrize(
    "stream",
    [
        input("input.mp4").output(filename="output.mp4"),
        input("input.mp4").video.output(filename="output.mp4"),
        input("input.mp4").audio.output(filename="output.mp4"),
        input("input.mp4", f="mp4", ss=1).output(filename="output.mp4"),
        input("input.mp4").output(filename="output.mp4").global_args(y=True),
        input("input.mp4")
        .output(filename="output.mp4")
        .global_args(y=True)
        .merge_outputs(input("input2.mp4").output(filename="output2.mp4")),
    ],
)
def test_compile(stream: Stream, snapshot: SnapshotAssertion) -> None:
    assert snapshot(name="compile") == compile(stream)
    assert snapshot(name="compile_to_python") == compile_to_python(stream)
    assert snapshot(name="is_simple_graph") == is_simple_graph(stream)
