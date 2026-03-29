"""Cache data files for typed-ffmpeg-v5 (FFmpeg 5.x)."""

from pathlib import Path


def get_cache_path() -> Path:
    """Return the path to the cache data directory.

    Returns:
        Path to the cache data directory.

    """
    return Path(__file__).parent / "cache"
