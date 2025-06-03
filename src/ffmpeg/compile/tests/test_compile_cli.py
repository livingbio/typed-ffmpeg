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


def test_parse_filter_chain(snapshot: SnapshotAssertion) -> None:
    parsed = parse(
        """ffmpeg.exe -nostdin -analyzeduration 100M -probesize 100M -i "input_video.mkv" -vf "scale=-1:-1:flags=lanczos,pad=1920:1080:-1:-1,subtitles='subtitles.srt':stream_index=0:force_style='Fontname=Gotham Rounded Medium,Fontsize=17,Alignment=2,PrimaryColour=&Hffffff&,MarginV=25'" -sn -map 0:a:0 -map 0:v:0 -c:a aac -b:a 192k -ac 2 -c:v libx264 -crf 18 -preset slow -tune film -aq-strength 1.8 -mbtree 0 -pix_fmt yuv420p -y -hide_banner -loglevel error -stats -map_metadata -1 -map_chapters -1 "output_video.mp4" """
    )
