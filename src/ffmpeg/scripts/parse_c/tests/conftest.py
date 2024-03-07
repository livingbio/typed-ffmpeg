from pathlib import Path

import pytest


@pytest.fixture
def ffmpeg_path() -> Path:
    return Path(__file__).parent.parent / "ffmpeg"
