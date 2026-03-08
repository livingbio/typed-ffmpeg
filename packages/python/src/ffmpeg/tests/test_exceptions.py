"""Tests for FFmpeg exception classes."""

import pytest

from ..exceptions import (
    FFMpegError,
    FFMpegExecuteError,
    FFMpegTypeError,
    FFMpegValueError,
)


def test_ffmpeg_error_base() -> None:
    """Test base FFMpegError exception."""
    error = FFMpegError("Test error message")
    assert str(error) == "Test error message"
    assert isinstance(error, Exception)


def test_ffmpeg_type_error() -> None:
    """Test FFMpegTypeError exception."""
    error = FFMpegTypeError("Invalid type provided")
    assert str(error) == "Invalid type provided"
    assert isinstance(error, FFMpegError)
    assert isinstance(error, TypeError)


def test_ffmpeg_value_error() -> None:
    """Test FFMpegValueError exception."""
    error = FFMpegValueError("Invalid value provided")
    assert str(error) == "Invalid value provided"
    assert isinstance(error, FFMpegError)
    assert isinstance(error, ValueError)


def test_ffmpeg_execute_error() -> None:
    """Test FFMpegExecuteError exception."""
    cmd = "ffmpeg -i input.mp4 output.mp4"
    stdout = b"Output from ffmpeg"
    stderr = b"Error from ffmpeg"
    retcode = 1

    error = FFMpegExecuteError(retcode, cmd, stdout, stderr)

    assert error.retcode == retcode
    assert error.cmd == cmd
    assert error.stdout == stdout
    assert error.stderr == stderr
    assert isinstance(error, FFMpegError)


def test_ffmpeg_execute_error_message() -> None:
    """Test FFMpegExecuteError error message format."""
    cmd = "ffmpeg -i input.mp4"
    stdout = b""
    stderr = b"Invalid file format"
    retcode = 1

    error = FFMpegExecuteError(retcode, cmd, stdout, stderr)
    error_msg = str(error)

    assert cmd in error_msg
    assert "error" in error_msg.lower()
    assert "stderr" in error_msg.lower()


def test_ffmpeg_execute_error_with_none_retcode() -> None:
    """Test FFMpegExecuteError with None return code."""
    cmd = "ffmpeg -i input.mp4"
    stdout = b""
    stderr = b"Process terminated"
    retcode = None

    error = FFMpegExecuteError(retcode, cmd, stdout, stderr)

    assert error.retcode is None
    assert error.cmd == cmd


def test_ffmpeg_errors_can_be_raised() -> None:
    """Test that all FFmpeg exceptions can be raised and caught."""
    with pytest.raises(FFMpegError):
        raise FFMpegError("Test error")

    with pytest.raises(FFMpegTypeError):
        raise FFMpegTypeError("Test type error")

    with pytest.raises(FFMpegValueError):
        raise FFMpegValueError("Test value error")

    with pytest.raises(FFMpegExecuteError):
        raise FFMpegExecuteError(1, "cmd", b"", b"")


def test_ffmpeg_error_hierarchy() -> None:
    """Test the exception hierarchy."""
    # FFMpegTypeError is both FFMpegError and TypeError
    with pytest.raises(FFMpegError):
        raise FFMpegTypeError("Type error")

    with pytest.raises(TypeError):
        raise FFMpegTypeError("Type error")

    # FFMpegValueError is both FFMpegError and ValueError
    with pytest.raises(FFMpegError):
        raise FFMpegValueError("Value error")

    with pytest.raises(ValueError):
        raise FFMpegValueError("Value error")
