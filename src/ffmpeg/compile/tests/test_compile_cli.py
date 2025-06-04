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


def test_parse_global_binary_option(snapshot: SnapshotAssertion) -> None:
    parsed = parse("ffmpeg -nostdin -i input_video.mkv -y output_video.mp4")
    assert (
        snapshot(
            name="parse-global-binary-option", extension_class=JSONSnapshotExtension
        )
        == parsed
    )


def test_parse_ffmpeg_exe(snapshot: SnapshotAssertion) -> None:
    parsed = parse("ffmpeg.exe -i input_video.mkv output_video.mp4")
    assert (
        snapshot(name="parse-ffmpeg-exe", extension_class=JSONSnapshotExtension)
        == parsed
    )


def test_parse_ffmpeg_with_stream_option(snapshot: SnapshotAssertion) -> None:
    parsed = parse("""ffmpeg -i input.mov -i resources/nfa-logo.png -filter_complex "[0:v]scale=flags=lanczos+accurate_rnd:h=720:w=-1[s0];[s0]lut3d=file=resources/rip_lut_pushup.cube[s1];[1]scale=height=720:width=-1[s2];[s1][s2]overlay=eof_action=repeat:x=(W/2-w/2):y=0[s3];[s3]drawtext=borderw=2:fontcolor=white:fontfile=resources/fonts/arial.ttf:fontsize=30:r=25/1:timecode=00\\:00\\:00\\:00:x=(W-tw)/2:y=text_h[s4];[s4][0:a]concat=a=1:n=1:v=1[s5]" -map [s5] -f mp4 -ac 2 -b:a 64k -bf 2 -c:a aac -c:v h264_nvenc -color_primaries bt709 -color_trc bt709 -colorspace bt709 -g 250 -map_metadata -1 -movflags +faststart+write_colr -pix_fmt yuv420p -preset slow -profile:v high -qp 28 -rc constqp -refs 4 -shortest -spatial-aq 1 -strict_gop 1 -timecode 00:00:00:00 output.mp4 -hide_banner -loglevel error""")
    assert (
        snapshot(
            name="parse-ffmpeg-with-stream-option",
            extension_class=JSONSnapshotExtension,
        )
        == parsed
    )