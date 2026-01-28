from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...compile.compile_cli import get_args, get_stream_label
from ...compile.context import DAGContext
from ...exceptions import FFMpegExecuteError
from ...filters import concat
from ...schema import StreamType
from ...utils.frozendict import FrozenDict
from ...utils.snapshot import DAGSnapshotExtension
from ..nodes import (
    FilterNode,
    GlobalNode,
    GlobalStream,
    InputNode,
    OutputNode,
    OutputStream,
)
from ..schema import Node


@pytest.mark.parametrize(
    "node, expected_type",
    [
        pytest.param(
            InputNode(
                filename="test.mp4",
                kwargs=FrozenDict(
                    {"f": "mp4"},
                ),
            ),
            InputNode,
            id="input-node",
        ),
        pytest.param(
            OutputNode(
                filename="test.mp4",
                kwargs=FrozenDict(
                    {"bufsize": "64k"},
                ),
                inputs=(),
            ),
            OutputNode,
            id="output-node",
        ),
        pytest.param(
            FilterNode(
                name="scale",
                kwargs=FrozenDict({
                    "w": "1920",
                    "h": "1080",
                    "true": True,
                    "false": False,
                }),
            ),
            FilterNode,
            id="filter-node",
        ),
        pytest.param(
            input(filename="tmp.mp4")
            .output(filename="temp")
            .global_args(y=True, extra_options={"no": False, "speed": 1})
            .node,
            GlobalNode,
            id="global-node",
        ),
        pytest.param(
            input(filename="tmp1.mp4")
            .output(filename="out1.mp4")
            .merge_outputs(input(filename="tmp2.mp4").output(filename="out2.mp4"))
            .node,
            GlobalNode,
            id="merge-output-node",
        ),
    ],
)
def test_node_prop(
    node: Node, expected_type: type[Node], snapshot: SnapshotAssertion
) -> None:
    assert snapshot(name="f.repr") == node.repr()
    assert snapshot(name="__repr__") == repr(node)
    assert snapshot(name="get_args") == get_args(node)
    assert type(node) is expected_type
    assert snapshot(extension_class=DAGSnapshotExtension, name="graph") == node


def base_stream() -> OutputStream:
    input1 = input("tmp1.mp4")
    input2 = input("tmp2.mp4")

    f = concat(input1.video, input2.video)
    return f.video(0).output(filename="output.mp4")


@pytest.mark.parametrize(
    "stream,expected_overwrite",
    [
        pytest.param(base_stream(), None, id="not config"),
        pytest.param(
            base_stream().global_args(y=True), True, id="set y is True with global args"
        ),
        pytest.param(
            base_stream().global_args(y=False),
            None,
            id="set y is True with global args",
        ),
        pytest.param(
            base_stream().global_args(n=True),
            False,
            id="set n is True with global args",
        ),
        pytest.param(
            base_stream().global_args(n=False),
            None,
            id="set n is False with global args",
        ),
        pytest.param(
            base_stream().overwrite_output(), True, id="set y with overwrite_output"
        ),
        pytest.param(base_stream().global_args(), None, id="not set with global args"),
    ],
)
def test_global_node_with_args_overwrite(
    snapshot: SnapshotAssertion,
    stream: OutputStream | GlobalStream,
    expected_overwrite: bool | None,
) -> None:
    context = DAGContext.build(stream.node)

    if expected_overwrite is True:
        assert "-y" in stream.compile()
    elif expected_overwrite is False:
        assert "-n" in stream.compile()
    else:
        assert "-y" not in stream.compile()
        assert "-n" not in stream.compile()

    assert snapshot(name="get-args", extension_class=JSONSnapshotExtension) == get_args(
        stream.node, context
    )
    assert (
        snapshot(name="compile", extension_class=JSONSnapshotExtension)
        == stream.compile()
    )
    assert snapshot(
        name="compile with overwrite", extension_class=JSONSnapshotExtension
    ) == stream.compile(overwrite_output=True)
    assert snapshot(
        name="compile without overwrite", extension_class=JSONSnapshotExtension
    ) == stream.compile(overwrite_output=False)
    assert (
        snapshot(name="compile-line", extension_class=JSONSnapshotExtension)
        == stream.compile_line()
    )
    assert snapshot(extension_class=DAGSnapshotExtension, name="graph") == stream.node


def test_nostdin(snapshot: SnapshotAssertion) -> None:
    input1 = input("tmp1.mp4")
    stream = input1.output(filename="output.mp4").global_args(stdin=False)
    assert stream.compile() == snapshot


def test_filter_node_with_outputs(snapshot: SnapshotAssertion) -> None:
    input1 = input("tmp1.mp4")
    input2 = input("tmp2.mp4")

    f = concat(input1.video, input2.video)
    stream = f.video(0).output(filename="output.mp4")
    context = DAGContext.build(stream.node)
    assert snapshot(extension_class=JSONSnapshotExtension) == get_args(f, context)


def test_output_run(datadir: Path) -> None:
    input1 = input(datadir / "input.mp4")
    output = input1.output(filename="output.mp4")
    output.run(overwrite_output=True)

    with pytest.raises(FFMpegExecuteError):
        input_not_exists = input(datadir / "not-exists.mp4")
        output = input_not_exists.output(filename="output.mp4")
        output.run()


def test_output_run_with_tee_stderr(datadir: Path) -> None:
    """Test that tee_stderr captures stderr while running FFmpeg."""
    input1 = input(datadir / "input.mp4")
    output = input1.output(filename="output.mp4")

    # Run with tee_stderr=True - should capture stderr
    _stdout, stderr = output.run(tee_stderr=True, overwrite_output=True)

    # FFmpeg always writes something to stderr (version info, progress, etc.)
    assert isinstance(stderr, bytes)
    assert len(stderr) > 0

    # Should contain FFmpeg-related output


def test_output_run_with_tee_stderr_quiet(datadir: Path) -> None:
    """Test that tee_stderr with quiet=True captures but doesn't display stderr."""
    input1 = input(datadir / "input.mp4")
    output = input1.output(filename="output.mp4")

    # Run with tee_stderr=True and quiet=True
    _stdout, stderr = output.run(tee_stderr=True, quiet=True, overwrite_output=True)

    # Stderr should still be captured
    assert isinstance(stderr, bytes)
    assert len(stderr) > 0


def test_output_run_with_tee_stderr_error(datadir: Path) -> None:
    """Test that tee_stderr captures stderr on error."""
    input_not_exists = input(datadir / "not-exists.mp4")
    output = input_not_exists.output(filename="output.mp4")

    with pytest.raises(FFMpegExecuteError) as exc_info:
        output.run(tee_stderr=True)

    # Error should contain captured stderr
    err = exc_info.value
    assert isinstance(err, FFMpegExecuteError)
    assert err.stderr is not None
    assert len(err.stderr) > 0


def test_output_run_with_tee_stderr_and_capture_stdout(datadir: Path) -> None:
    """Test that tee_stderr works correctly with capture_stdout=True."""
    input1 = input(datadir / "input.mp4")
    # Output to pipe to capture stdout
    output = input1.output(filename="pipe:1", f="null")

    # Run with both tee_stderr and capture_stdout
    stdout, stderr = output.run(
        tee_stderr=True, capture_stdout=True, overwrite_output=True
    )

    # Both should be captured
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, bytes)
    assert len(stderr) > 0  # FFmpeg always outputs to stderr


def test_output_run_with_tee_stderr_without_capture_stdout(datadir: Path) -> None:
    """Test that tee_stderr works correctly with capture_stdout=False."""
    input1 = input(datadir / "input.mp4")
    output = input1.output(filename="output.mp4")

    # Run with tee_stderr but without capture_stdout
    stdout, stderr = output.run(
        tee_stderr=True, capture_stdout=False, overwrite_output=True
    )

    # stdout should be empty, stderr should be captured
    assert stdout == b""
    assert isinstance(stderr, bytes)
    assert len(stderr) > 0


def test_output_run_tee_stderr_ignores_capture_stderr(datadir: Path) -> None:
    """Test that capture_stderr is ignored when tee_stderr=True."""
    input1 = input(datadir / "input.mp4")
    output = input1.output(filename="output.mp4")

    # Even with capture_stderr=False, tee_stderr=True should capture stderr
    _stdout, stderr = output.run(
        tee_stderr=True, capture_stderr=False, overwrite_output=True
    )

    # stderr should still be captured because tee_stderr=True
    assert isinstance(stderr, bytes)
    assert len(stderr) > 0


def test_filter_node_output_typings() -> None:
    f = FilterNode(
        name="scale",
        kwargs=FrozenDict({
            "w": "1920",
            "h": "1080",
        }),
        output_typings=(StreamType.video, StreamType.audio),
    )
    assert f.video(0).index == 0
    assert f.audio(0).index == 1

    f = FilterNode(
        name="scale",
        kwargs=FrozenDict({"w": "1920", "h": "1080"}),
        output_typings=(StreamType.audio,),
    )

    with pytest.raises(ValueError):
        f.video(0)

    with pytest.raises(ValueError):
        f.audio(1)


def test_filter_node_with_inputs(snapshot: SnapshotAssertion) -> None:
    in_file = input("test.mp4")

    assert snapshot(extension_class=JSONSnapshotExtension) == FilterNode(
        name="scale",
        kwargs=FrozenDict({"w": "1920", "h": "1080"}),
        inputs=(in_file.video, in_file.audio),
        input_typings=(StreamType.video, StreamType.audio),
    )

    with pytest.raises(ValueError):
        FilterNode(
            name="scale",
            inputs=(in_file.video,),
            input_typings=(StreamType.audio, StreamType.video),
        )

    with pytest.raises(TypeError) as te:
        FilterNode(
            name="scale",
            kwargs=FrozenDict({"w": "1920", "h": "1080"}),
            inputs=(in_file.video,),
            input_typings=(StreamType.audio,),
        )

    assert snapshot == te

    with pytest.raises(TypeError) as te:
        FilterNode(
            name="scale",
            kwargs=FrozenDict({"w": "1920", "h": "1080"}),
            inputs=(in_file.audio,),
            input_typings=(StreamType.video,),
        )

    assert snapshot == te


def test_custom_filter(snapshot: SnapshotAssertion) -> None:
    in_file = input("test.mp4")

    assert snapshot == get_args(in_file.audio.afilter(name="volume", v=0.5, a=0.3).node)
    assert snapshot == get_args(
        in_file.video.vfilter(name="rotate", angle=90, xx=30).node
    )


def test_input_selector(snapshot: SnapshotAssertion) -> None:
    node = InputNode(filename="test.mp4", kwargs=FrozenDict({"f": "mp4"}))

    assert snapshot(extension_class=JSONSnapshotExtension) == get_args(
        node.audio.areverse().node
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == get_args(
        node.video.reverse().node
    )


def test_filterable_stream(snapshot: SnapshotAssertion) -> None:
    input1 = input("tmp1.mp4")
    input2 = input("tmp2.mp4")

    out = concat(input1, input2).video(0).output(filename="output.mp4")

    assert snapshot == get_stream_label(input2, DAGContext.build(out.node))
    assert snapshot == get_stream_label(input2)

    assert snapshot == get_stream_label(input1.split().video(0))
