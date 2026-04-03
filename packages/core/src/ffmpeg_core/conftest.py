import shutil

import pytest

requires_ffmpeg = pytest.mark.skipif(
    shutil.which("ffmpeg") is None,
    reason="ffmpeg binary not found",
)
requires_ffprobe = pytest.mark.skipif(
    shutil.which("ffprobe") is None,
    reason="ffprobe binary not found",
)
