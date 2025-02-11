import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..base import input, merge_outputs, output, vfilter
from ..filters import concat, join
from ..schema import StreamType
from ..streams.video import VideoStream


def test_output_node(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1")

    value = {"str": "x", "int": 1, "float": 0.1}
    # due to https://github.com/python/mypy/issues/11583
    # out = input1.output(filename="out.mp4", **value)  # type: ignore[arg-type]
    # assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())

    out = input1.output(filename="out.mp4", extra_options=value)
    assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1")
    input2 = input("input2")
    input3 = input("input3")

    # with pytest.raises(ValueError) as e:
    concat(*(input1, input2, input2))  # will auto correct n's value now
    # assert snapshot == e

    concat(*(input1, input2, input3), n=3)
    assert isinstance(concat(*(input1, input2, input3), n=3).video(0), VideoStream)

    concat(*(input1, input2.video, input3.video), n=3)

    with pytest.raises(TypeError) as te:
        concat(*(input1, input2.audio, input3.audio), n=3)
    assert snapshot == te


def test_compile(snapshot: SnapshotAssertion) -> None:
    # ['ffmpeg', '-i', 'input.mp4', '-i', 'overlay.png', '-filter_complex', '[0]trim=end_frame=20:start_frame=10[s0];[0]trim=end_frame=40:start_frame=30[s1];[s0][s1]concat=n=2[s2];[1]hflip[s3];[s2][s3]overlay=eof_action=repeat[s4];[s4]drawbox=50:50:120:120:red:t=5[s5]', '-map', '[s5]', 'out.mp4']
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


def test_generate_thumbnail_for_video(snapshot: SnapshotAssertion) -> None:
    # ["ffmpeg", "-ss", "10", "-i", "input.mp4", "-filter_complex", "[0]scale=800:-1[s0]", "-map", "[s0]", "-vframes", "1", "output.mp4"]
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input("input.mp4", ss=10)
        .scale(w="800", h="-1")
        .output(filename="output.mp4", vframes=1)
        .compile()
    )


def test_assemble_video_from_sequence_of_frames(snapshot: SnapshotAssertion) -> None:
    # ["ffmpeg", "-framerate", "25", "-pattern_type", "glob", "-i", "/path/to/jpegs/*.jpg", "movie.mp4""]
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input(
            "/path/to/jpegs/*.jpg",
            extra_options={"framerate": 25, "pattern_type": "glob"},
        )
        .output(filename="movie.mp4")
        .compile()
    )


def test_assemble_video_from_sequence_of_frames_with_additional_filtering(
    snapshot: SnapshotAssertion,
) -> None:
    # ["ffmpeg", "-framerate", "25", "-pattern_type", "glob", "-i", "/path/to/jpegs/*.jpg", "-filter_complex", "[0]deflicker=mode=pm:size=10[s0];[s0]scale=force_original_aspect_ratio=increase:size=hd1080[s1]", "-map", "[s1]", "-crf", "20", "-movflags", "faststart", "-pix_fmt", "yuv420p", "-preset", "slower", "movie.mp4"]
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input(
            "/path/to/jpegs/*.jpg",
            extra_options={"framerate": 25, "pattern_type": "glob"},
        )
        .deflicker(mode="pm", size=10)
        # FIXME: scale's w,h options should be optional
        .scale(force_original_aspect_ratio="increase", extra_options={"size": "hd1080"})
        .output(
            filename="movie.mp4",
            pix_fmt="yuv420p",
            extra_options={"crf": 20, "movflags": "faststart", "preset": "slower"},
        )
        .compile()
    )


def test_audio_video_pipeline(snapshot: SnapshotAssertion) -> None:
    # ["ffmpeg", "-i", "input.mp4", "-i", "input.mp3", "-filter_complex", "[0:v]scale=1280:-1[s0];[1]volume=0.5[s1];[s0][s1]concat=n=2:v=0:a=1[s2]", "-map", "[s2]", "output.mp4"]
    in1 = input("in1.mp4")
    in2 = input("in2.mp4")
    v1 = in1.video.hflip()
    a1 = in1.audio
    v2 = in2.video.reverse().hue(s="0")
    a2 = in2.audio.areverse().aphaser()
    joined = concat(v1, a1, v2, a2, v=1, a=1)
    v3 = joined.video(0)
    a3 = joined.audio(0).volume(volume="0.8")
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == output(v3, a3, filename="out.mp4").compile()
    )


def test_mono_to_stereo_with_offsets_and_video(snapshot: SnapshotAssertion) -> None:
    # ["ffmpeg", "-i", "audio-left.wav", "-i", "audio-right.wav", "-i", "input-video.mp4", "-filter_complex", "[0]atrim=start=5[s0];[s0]asetpts=PTS-STARTPTS[s1];[1]atrim=start=10[s2];[s2]asetpts=PTS-STARTPTS[s3];[s1][s3]join=channel_layout=stereo:inputs=2[s4]", "-map", "[s4]", "-map", "2:v", "-shortest", "-vcodec", "copy", "output-video.mp4", "-y"]
    audio_left = input("audio-left.wav").atrim(start=5).asetpts(expr="PTS-STARTPTS")
    audio_right = input("audio-right.wav").atrim(start=10).asetpts(expr="PTS-STARTPTS")
    input_video = input("input-video.mp4")
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        join(audio_left, audio_right, inputs=2, channel_layout="stereo")
        .output(
            input_video.video, filename="output-video.mp4", shortest=True, vcodec="copy"
        )
        .overwrite_output()
        .compile()
    )


def test_drawtext_escaping(snapshot: SnapshotAssertion) -> None:
    # ["ffmpeg", "-i", "input.mp4", "-filter_complex", "[0]drawtext=text='this is a \\'string\\'': may contain one, or more, special characters':fontfile=/path/to/font.ttf[s0]", "-map", "[s0]", "output.mp4"]
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input("input.mp4")
        .drawtext(
            text="this is a 'string': may contain one, or more, special characters",
            fontfile="/path/to/font.ttf",
        )
        .output(filename="output.mp4")
        .compile()
    )


def test_compile_bool_option(snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input("input.mp4")
        .drawtext(text="hello", extra_options={"escape_text": False})
        .output(filename="output.mp4")
        .compile()
    )

    assert snapshot(extension_class=JSONSnapshotExtension) == (
        input("input.mp4")
        .drawtext(text="hello", extra_options={"escape_text": True})
        .output(filename="output.mp4")
        .compile()
    )


def test_compile_merge_outputs(snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == (
        merge_outputs(
            output(input("input1.mp4"), filename="output1.mp4"),
            output(input("input2.mp4"), filename="output2.mp4"),
        ).compile()
    )


def test_compile_merge_outputs_with_filter_complex(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    input2 = input("input2.mp4")

    joined = concat(input1, input2, n=2)
    splitted = joined.video(0).split()
    output1 = output(splitted.video(0), filename="output1.mp4")
    output2 = output(splitted.video(1), filename="output2.mp4")

    assert snapshot(extension_class=JSONSnapshotExtension) == (
        merge_outputs(output1, output2).compile()
    )


def test_concat_dumuxer(snapshot: SnapshotAssertion) -> None:
    stream = input(
        "files.txt",
        f="concat",
        extra_options={
            "safe": 0,
            "protocol_whitelist": "file,http,https,tcp,tls",
        },
    )

    assert snapshot(extension_class=JSONSnapshotExtension) == (
        stream.output(filename="output.mp4").compile()
    )


def test_customize_vfilter(snapshot: SnapshotAssertion) -> None:
    in_file = input("input.mp4")

    gltransition = vfilter(
        in_file,
        in_file,
        name="gltransition",
        duration=1,
        offset=0.5,
        direction="left",
        input_typings=(StreamType.video, StreamType.video),
    )

    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == gltransition.output(filename="output.mp4").compile()
    )
