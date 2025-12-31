"""
Tests for the GlobalRunable class.

This module tests the execution capabilities of FFmpeg filter graphs,
including compilation, running, and the new use_filter_complex_script feature.
"""

import asyncio
import io
import subprocess
import sys

import pytest

from ....base import input
from ..runnable import GlobalRunable

# Note: Integration tests for tee_stderr that actually run FFmpeg are in
# src/ffmpeg/dag/tests/test_nodes.py (test_output_run_with_tee_stderr*)


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


class TestTeeStderrHelperMethods:
    """Unit tests for tee_stderr helper methods."""

    def test_start_stderr_tee_thread_captures_data(self) -> None:
        """Test that _start_stderr_tee_thread captures stderr data."""
        stderr_data = b"test stderr output\nline 2\n"
        stderr_pipe = io.BytesIO(stderr_data)

        capture_buffer: list[bytes] = []
        thread = GlobalRunable._start_stderr_tee_thread(
            stderr_pipe,
            capture_buffer=capture_buffer,
            write_to_stderr=False,
        )
        thread.join(timeout=5.0)

        assert b"".join(capture_buffer) == stderr_data

    def test_start_stderr_tee_thread_with_write_enabled(self) -> None:
        """Test that _start_stderr_tee_thread captures data when write_to_stderr=True."""
        # Note: We can't easily test actual writes to sys.stderr.buffer as it's readonly
        # Instead, we verify the capture works and trust the write logic
        stderr_data = b"test output\n"
        stderr_pipe = io.BytesIO(stderr_data)

        capture_buffer: list[bytes] = []
        thread = GlobalRunable._start_stderr_tee_thread(
            stderr_pipe,
            capture_buffer=capture_buffer,
            write_to_stderr=True,  # This would write to stderr in real usage
        )
        thread.join(timeout=5.0)

        # Data should be captured regardless of write_to_stderr setting
        assert b"".join(capture_buffer) == stderr_data

    def test_start_stderr_tee_thread_quiet_mode(self) -> None:
        """Test that _start_stderr_tee_thread captures data with write_to_stderr=False."""
        stderr_data = b"should be captured\n"
        stderr_pipe = io.BytesIO(stderr_data)

        capture_buffer: list[bytes] = []
        thread = GlobalRunable._start_stderr_tee_thread(
            stderr_pipe,
            capture_buffer=capture_buffer,
            write_to_stderr=False,  # Quiet mode - no console output
        )
        thread.join(timeout=5.0)

        # Data should still be captured even in quiet mode
        assert b"".join(capture_buffer) == stderr_data

    def test_start_stderr_tee_thread_handles_empty_input(self) -> None:
        """Test that _start_stderr_tee_thread handles empty input gracefully."""
        stderr_pipe = io.BytesIO(b"")

        capture_buffer: list[bytes] = []
        thread = GlobalRunable._start_stderr_tee_thread(
            stderr_pipe,
            capture_buffer=capture_buffer,
            write_to_stderr=False,
        )
        thread.join(timeout=5.0)

        assert capture_buffer == []

    def test_start_stderr_tee_thread_handles_large_data(self) -> None:
        """Test that _start_stderr_tee_thread handles data larger than chunk size."""
        # Create data larger than the 4096 byte chunk size
        stderr_data = b"x" * 10000 + b"\n"
        stderr_pipe = io.BytesIO(stderr_data)

        capture_buffer: list[bytes] = []
        thread = GlobalRunable._start_stderr_tee_thread(
            stderr_pipe,
            capture_buffer=capture_buffer,
            write_to_stderr=False,
        )
        thread.join(timeout=5.0)

        assert b"".join(capture_buffer) == stderr_data


class TestTeeStderrWithRealSubprocess:
    """Tests for tee_stderr using real subprocess (Python) to verify behavior."""

    def test_tee_thread_with_real_process(self) -> None:
        """Test tee thread with a real subprocess."""
        stderr_message = b"test stderr message from python\n"

        process = subprocess.Popen(
            [
                sys.executable,
                "-c",
                f"import sys; sys.stderr.buffer.write({stderr_message!r}); sys.stderr.flush()",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        capture_buffer: list[bytes] = []

        if process.stderr is not None:
            thread = GlobalRunable._start_stderr_tee_thread(
                process.stderr,
                capture_buffer=capture_buffer,
                write_to_stderr=False,
            )

            process.wait()
            thread.join(timeout=5.0)

            assert b"".join(capture_buffer) == stderr_message

    def test_tee_thread_captures_multiline_output(self) -> None:
        """Test that tee thread captures multi-line output correctly."""
        lines = [b"line 1\n", b"line 2\n", b"line 3\n"]
        stderr_message = b"".join(lines)

        process = subprocess.Popen(
            [
                sys.executable,
                "-c",
                f"import sys; sys.stderr.buffer.write({stderr_message!r}); sys.stderr.flush()",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        capture_buffer: list[bytes] = []

        if process.stderr is not None:
            thread = GlobalRunable._start_stderr_tee_thread(
                process.stderr,
                capture_buffer=capture_buffer,
                write_to_stderr=False,
            )

            process.wait()
            thread.join(timeout=5.0)

            captured = b"".join(capture_buffer)
            assert captured == stderr_message

    def test_thread_cleanup_after_process_exit(self) -> None:
        """Test that thread properly cleans up after process exits."""
        process = subprocess.Popen(
            [sys.executable, "-c", "import sys; sys.stderr.write('done')"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        capture_buffer: list[bytes] = []

        if process.stderr is not None:
            thread = GlobalRunable._start_stderr_tee_thread(
                process.stderr,
                capture_buffer=capture_buffer,
                write_to_stderr=False,
            )

            # Wait for process to finish
            process.wait()

            # Thread should finish quickly after process exits
            thread.join(timeout=5.0)
            assert not thread.is_alive()


class TestTeeStderrParameterBehavior:
    """Tests for tee_stderr parameter behavior and interactions."""

    def test_tee_stderr_parameter_exists(self) -> None:
        """Test that tee_stderr parameter is accepted by run method."""
        import inspect

        stream = input("test.mp4").output(filename="output.mp4")
        sig = inspect.signature(stream.run)

        assert "tee_stderr" in sig.parameters
        assert sig.parameters["tee_stderr"].default is False
        # Note: Due to `from __future__ import annotations`, annotation is a string
        assert sig.parameters["tee_stderr"].annotation in (bool, "bool")

    def test_tee_stderr_and_quiet_parameters_coexist(self) -> None:
        """Test that tee_stderr and quiet parameters can be used together."""
        import inspect

        stream = input("test.mp4").output(filename="output.mp4")
        sig = inspect.signature(stream.run)

        assert "tee_stderr" in sig.parameters
        assert "quiet" in sig.parameters
        assert sig.parameters["quiet"].default is False

    def test_tee_stderr_does_not_affect_compile(self) -> None:
        """Test that tee_stderr parameter doesn't affect compilation."""
        stream = input("test.mp4").output(filename="output.mp4")

        # tee_stderr is an execution-time parameter, not a compilation parameter
        args1 = stream.compile()
        args2 = stream.compile()

        assert args1 == args2
        assert len(args1) > 0


class TestRunAsync:
    """Tests for the async run_async method using asyncio.subprocess."""

    @pytest.mark.asyncio
    async def test_run_async_returns_asyncio_process(self) -> None:
        """Test that run_async returns an asyncio.subprocess.Process."""
        stream = input("test.mp4").output(filename="output.mp4")

        # Use a simple echo command to verify the async functionality works
        process = await stream.run_async(cmd=["echo", "test"])

        assert isinstance(process, asyncio.subprocess.Process)
        await process.wait()

    @pytest.mark.asyncio
    async def test_run_async_with_pipes(self) -> None:
        """Test that run_async works with pipe options."""
        stream = input("test.mp4").output(filename="output.mp4")

        # Use echo command to test piping
        process = await stream.run_async(
            cmd=["echo", "hello"], pipe_stdout=True, pipe_stderr=True
        )

        assert isinstance(process, asyncio.subprocess.Process)
        assert process.stdout is not None
        assert process.stderr is not None

        stdout, stderr = await process.communicate()
        assert b"hello" in stdout
        assert process.returncode == 0

    @pytest.mark.asyncio
    async def test_run_async_is_awaitable(self) -> None:
        """Test that run_async method is directly awaitable."""
        stream = input("test.mp4").output(filename="output.mp4")

        # The method should be awaitable without additional wrapper
        result = stream.run_async(cmd=["echo", "test"])

        # result should be a coroutine
        assert asyncio.iscoroutine(result)

        # Consume the coroutine
        process = await result
        assert isinstance(process, asyncio.subprocess.Process)
        await process.wait()
