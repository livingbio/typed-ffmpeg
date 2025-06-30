import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import filter_multi_output, input
from ...common.schema import StreamType
from ...dag.schema import Stream
from ..compile_cli import (
    compile,
    compile_as_list,
    get_args,
    parse,
    parse_with_validation,
)
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


def test_get_args_custom_filter(snapshot: SnapshotAssertion) -> None:
    graph = filter_multi_output(
        input("input1.mp4"),
        name="custom_split",
        input_typings=(StreamType.video,),
        output_typings=(StreamType.video, StreamType.video),
    )
    assert snapshot == get_args(graph)


@pytest.mark.parametrize(
    "command",
    [
        pytest.param(
            "ffmpeg -y -nostdin -i input_video.mkv output_video.mp4",
            id="global_binary_option",
        ),
        pytest.param(
            "ffmpeg.exe -i input_video.mkv output_video.mp4",
            id="ffmpeg_exe",
        ),
        pytest.param(
            "ffmpeg -y -nostdin -i input_video.mkv -b:v 1000k output_video.mp4",
            id="output_option_with_stream_selector",
        ),
        pytest.param(
            "ffmpeg -y -nostdin -i input_video.mkv -shortest -b:v 1000k -b:a 128k output_video.mp4",
            id="output_option_with_boolean_option",
        ),
        pytest.param(
            '''ffmpeg.exe -nostdin -analyzeduration 100M -probesize 100M -i "input_video.mkv" -vf "scale=-1:-1:flags=lanczos,pad=1920:1080:-1:-1,subtitles='subtitles.srt':stream_index=0:force_style='Fontname=Gotham Rounded Medium,Fontsize=17,Alignment=2,PrimaryColour=&Hffffff&,MarginV=25'" -sn -map 0:a:0 -map 0:v:0 -c:a aac -b:a 192k -ac 2 -c:v libx264 -crf 18 -preset slow -tune film -aq-strength 1.8 -mbtree 0 -pix_fmt yuv420p -y -hide_banner -loglevel error -stats -map_metadata -1 -map_chapters -1 "output_video.mp4"''',
            id="complex_command",
        ),
        pytest.param(
            "ffmpeg -y -not-exist-global -nostdin -i input_video.mkv -not-exist-input -i input-2.mp4 -not-exist-output -b:v 1000k -b:a 128k output_video.mp4",
            id="ignore_not_exist_option",
        ),
        pytest.param(
            """ffmpeg -i input.mov -filter_complex "[0:v]drawtext=text='=\\\\;\\:':borderw=2:fontcolor=white:fontfile=resources/fonts/arial.ttf:fontsize=30:r=25/1:timecode=00\\:00\\:00\\:00:x=(W-tw)/2:y=text_h[out]" -map [out] output.mp4""",
            id="escaping",
        ),
        pytest.param(
            "ffmpeg -i input.mov -map 0:s output.mp4",
            id="stream_selector_with_subtitle",
        ),
    ],
)
def test_parse_ffmpeg_commands(snapshot: SnapshotAssertion, command: str) -> None:
    parsed = parse(command)
    assert snapshot(name="parse-ffmpeg-commands") == parsed
    assert snapshot(name="build-ffmpeg-commands") == compile(parsed)
    assert snapshot(name="parse-with-validation") == parse_with_validation(command)
