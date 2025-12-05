"""
Tests for the GlobalRunable class.

This module tests the execution capabilities of FFmpeg filter graphs,
including compilation, running, and the new use_filter_complex_script feature.
"""

from unittest.mock import MagicMock, patch

import pytest

from ....base import input
from ....exceptions import FFMpegExecuteError


def test_use_filter_complex_script_parameter() -> None:
    """Test that use_filter_complex_script parameter works correctly."""
    # Create a simple filter graph
    stream = (
        input("test.mp4")
        .video.vfilter(name="scale", w=1280, h=720)
        .output(filename="output.mp4")
    )

    # Test normal compilation (should use -filter_complex)
    normal_args = stream.compile()
    assert "-filter_complex" in normal_args
    assert "-filter_complex_script" not in normal_args

    # Test with use_filter_complex_script=True (should use -filter_complex_script)
    script_args = stream.compile(use_filter_complex_script=True)
    assert "-filter_complex_script" in script_args
    assert "-filter_complex" not in script_args

    # Verify the script file is created and contains the filter content
    script_index = script_args.index("-filter_complex_script")
    script_filename = script_args[script_index + 1]

    # The script file should exist and contain the filter complex content
    with open(script_filename) as f:
        script_content = f.read()
        assert "scale=w=1280:h=720" in script_content


def test_use_filter_complex_script_with_run_method() -> None:
    """Test that use_filter_complex_script parameter works with the run method."""
    # Create a simple filter graph
    stream = (
        input("test.mp4")
        .video.vfilter(name="scale", w=1280, h=720)
        .output(filename="output.mp4")
    )

    # Test that the parameter is accepted by the run method
    # Note: We don't actually run the command, just test that it compiles correctly
    try:
        # This should not raise an error
        args = stream.compile(use_filter_complex_script=True)
        assert "-filter_complex_script" in args
    except Exception as e:
        pytest.fail(f"compile with use_filter_complex_script=True failed: {e}")


def test_use_filter_complex_script_with_compile_line() -> None:
    """Test that use_filter_complex_script parameter works with compile_line method."""
    # Create a simple filter graph
    stream = (
        input("test.mp4")
        .video.vfilter(name="scale", w=1280, h=720)
        .output(filename="output.mp4")
    )

    # Test normal compilation
    normal_line = stream.compile_line()
    assert "-filter_complex" in normal_line
    assert "-filter_complex_script" not in normal_line

    # Test with use_filter_complex_script=True
    script_line = stream.compile_line(use_filter_complex_script=True)
    assert "-filter_complex_script" in script_line
    # When using filter_complex_script, it should use the script file instead of inline filter
    # The command should contain the script filename
    assert ".txt" in script_line


def test_run_captures_stderr_on_error() -> None:
    """Test that stderr is captured in FFMpegExecuteError when FFmpeg fails."""
    stream = input("nonexistent.mp4").output(filename="output.mp4")

    # Mock subprocess.Popen to simulate FFmpeg failure with stderr output
    mock_process = MagicMock()
    mock_process.communicate.return_value = (None, b"Error: Input file not found")
    mock_process.poll.return_value = 1

    with patch("subprocess.Popen", return_value=mock_process):
        with pytest.raises(FFMpegExecuteError) as exc_info:
            stream.run()

        # Verify that stderr is captured in the exception
        assert exc_info.value.stderr == b"Error: Input file not found"
        assert exc_info.value.stdout == b""
        assert exc_info.value.retcode == 1


def test_run_returns_empty_bytes_when_not_capturing() -> None:
    """Test that run() returns empty bytes when not capturing stdout/stderr."""
    stream = input("test.mp4").output(filename="output.mp4")

    # Mock subprocess.Popen to simulate successful FFmpeg run
    mock_process = MagicMock()
    mock_process.communicate.return_value = (None, b"Some FFmpeg output")
    mock_process.poll.return_value = 0

    with patch("subprocess.Popen", return_value=mock_process):
        stdout, stderr = stream.run()

        # Even though stderr was captured internally, it should return b""
        # when capture_stderr=False (the default)
        assert stdout == b""
        assert stderr == b""


def test_run_returns_stderr_when_capturing() -> None:
    """Test that run() returns stderr when capture_stderr=True."""
    stream = input("test.mp4").output(filename="output.mp4")

    # Mock subprocess.Popen to simulate successful FFmpeg run
    mock_process = MagicMock()
    mock_process.communicate.return_value = (None, b"Some FFmpeg output")
    mock_process.poll.return_value = 0

    with patch("subprocess.Popen", return_value=mock_process):
        stdout, stderr = stream.run(capture_stderr=True)

        # When capture_stderr=True, stderr should be returned
        assert stdout == b""
        assert stderr == b"Some FFmpeg output"
