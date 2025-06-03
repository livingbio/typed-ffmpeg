import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...dag.schema import Stream
from ..compile_cli import compile, compile_as_list, parse
from .cases import shared_cases


@pytest.mark.parametrize("graph", shared_cases)
def test_compile_cli(snapshot: SnapshotAssertion, graph: Stream) -> None:
    assert snapshot(
        name="compile-cli", extension_class=JSONSnapshotExtension
    ) == compile_as_list(graph)


@pytest.mark.parametrize("graph", shared_cases)
def test_parse_compile(snapshot: SnapshotAssertion, graph: Stream) -> None:
    compiled = compile(graph)
    parsed = parse(compiled)
    compiled_again = compile(parsed)
    assert snapshot(name="parse-compile", extension_class=JSONSnapshotExtension) == (
        compiled,
        compiled_again,
    )


def test_parse_ffmpeg_exe(snapshot: SnapshotAssertion) -> None:
    parsed = parse("ffmpeg.exe -i input_video.mkv output_video.mp4")
    assert (
        snapshot(name="parse-ffmpeg-exe", extension_class=JSONSnapshotExtension)
        == parsed
    )
