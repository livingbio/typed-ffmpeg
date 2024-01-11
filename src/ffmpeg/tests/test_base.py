import pytest
from pydantic import ValidationError
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..base import input
from ..filters import concat
from ..streams.video import VideoStream


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1")
    input2 = input("input2")
    input3 = input("input3")

    with pytest.raises(ValidationError) as e:
        concat(*(input1, input2, input2))
    assert snapshot == e

    concat(*(input1, input2, input3), n=3)
    assert isinstance(concat(*(input1, input2, input3), n=3).stream(0), VideoStream)

    concat(*(input1, input2.video, input3.video), n=3)

    with pytest.raises(ValidationError) as e:
        concat(*(input1, input2.audio, input3.audio), n=3)
    assert snapshot == e


def test_compile(snapshot: SnapshotAssertion) -> None:
    in_file = input("input.mp4")
    overlay_file = input("overlay.png")
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        concat(
            in_file.trim(start_frame=10, end_frame=20),
            in_file.trim(start_frame=30, end_frame=40),
        )
        .video(0)
        .overlay(overlay_file.hflip())
        .drawbox(x="50", y="50", width="120", height="120", color="red", thickness="5")
        .output(filename="out.mp4")
        .compile()
    )
    # ['ffmpeg', '-i', 'input.mp4', '-i', 'overlay.png', '-filter_complex', '[0]trim=end_frame=20:start_frame=10[s0];[0]trim=end_frame=40:start_frame=30[s1];[s0][s1]concat=n=2[s2];[1]hflip[s3];[s2][s3]overlay=eof_action=repeat[s4];[s4]drawbox=50:50:120:120:red:t=5[s5]', '-map', '[s5]', 'out.mp4']


def test_generate_thumbnail_for_video(snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input("input.mp4", ss=10).scale(w="800", h="-1").output(filename="output.mp4", vframes=1).compile()
    )


#  ['ffmpeg',
#  '-ss',
#  '10',
#  '-i',
#  'input.mp4',
#  '-filter_complex',
#  '[0]scale=800:-1[s0]',
#  '-map',
#  '[s0]',
#  '-vframes',
#  '1',
#  'output.mp4']
