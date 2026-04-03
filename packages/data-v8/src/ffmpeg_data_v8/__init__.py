"""Cache data files for typed-ffmpeg-v8 (FFmpeg 8.x)."""

from pathlib import Path


def get_cache_path() -> Path:
    """Return the path to the cache data directory."""
    return Path(__file__).parent / "cache"
