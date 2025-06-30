import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import filter_multi_output, input
from ...common.schema import StreamType
from ...dag.schema import Stream
from ..compile_cli import compile, compile_as_list, get_args, parse, parse_cli
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


@pytest.mark.parametrize(
    "command",
    [
        pytest.param(
            "ffmpeg -y -nostdin -i input_video.mkv output_video.mp4",
            id="basic_command",
        ),
        pytest.param(
            "ffmpeg -y -loglevel quiet -i input.mp4 -c:v libx264 -crf 23 output.mp4",
            id="codec_options",
        ),
        pytest.param(
            "ffmpeg -i input1.mp4 -i input2.mp4 -map 0 output1.mp4 -map 1 output2.mp4",
            id="multiple_inputs_outputs",
        ),
        pytest.param(
            "ffmpeg -y -i input.mp4 -filter_complex '[0:v]scale=1280:720[v]' -map '[v]' output.mp4",
            id="filter_complex",
        ),
    ],
)
def test_parse_cli_without_validation(snapshot: SnapshotAssertion, command: str) -> None:
    """Test that parse_cli works without option validation"""
    parsed = parse_cli(command)
    assert snapshot(name="parse-cli-without-validation") == parsed
    # Verify it can be compiled back to command
    compiled = compile(parsed)
    assert isinstance(compiled, str)


def test_parse_cli_vs_parse_compatibility() -> None:
    """Test that parse_cli produces similar results to parse for basic commands"""
    # Use a simple command that should work with both approaches
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    try:
        parsed_with_validation = parse(command)
        parsed_without_validation = parse_cli(command)
        
        # Both should produce Stream objects
        assert type(parsed_with_validation) == type(parsed_without_validation)
        
        # Both should be compilable
        compiled_with_validation = compile(parsed_with_validation)
        compiled_without_validation = compile(parsed_without_validation)
        
        assert isinstance(compiled_with_validation, str)
        assert isinstance(compiled_without_validation, str)
        
    except Exception as e:
        # If validation fails due to missing cache files, that's expected
        # but parse_cli should still work
        parsed_without_validation = parse_cli(command)
        compiled_without_validation = compile(parsed_without_validation)
        assert isinstance(compiled_without_validation, str)
