import pytest

from ..exceptions import (
    FFMpegError,
    FFMpegExecuteError,
    FFMpegTypeError,
    FFMpegValueError,
)


def test_ffmpeg_error_hierarchy() -> None:
    assert issubclass(FFMpegTypeError, FFMpegError)
    assert issubclass(FFMpegTypeError, TypeError)
    assert issubclass(FFMpegValueError, FFMpegError)
    assert issubclass(FFMpegValueError, ValueError)
    assert issubclass(FFMpegExecuteError, FFMpegError)


def test_ffmpeg_execute_error() -> None:
    err = FFMpegExecuteError(
        retcode=1,
        cmd="ffmpeg -i input.mp4",
        stdout=b"output",
        stderr=b"error message",
    )
    assert err.retcode == 1
    assert err.cmd == "ffmpeg -i input.mp4"
    assert err.stdout == b"output"
    assert err.stderr == b"error message"
    assert "error message" in str(err)


def test_ffmpeg_execute_error_catchable_as_ffmpeg_error() -> None:
    with pytest.raises(FFMpegError):
        raise FFMpegExecuteError(retcode=1, cmd="ffmpeg", stdout=b"", stderr=b"fail")
