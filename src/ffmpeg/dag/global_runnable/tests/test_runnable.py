"""
Tests for the GlobalRunable class.

This module tests the execution capabilities of FFmpeg filter graphs,
including compilation, running, and the new use_filter_complex_script feature.
"""

import pytest

from ....base import input


def test_use_filter_complex_script_parameter():
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


def test_use_filter_complex_script_with_run_method():
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


def test_use_filter_complex_script_with_compile_line():
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
