from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from ..cli import _generate_for_version, _get_version_metadata, generate


def test_generate() -> None:
    outpath = Path(TemporaryDirectory().name)
    generate(outpath)


def test_generate_version_dir() -> None:
    """Test code generation with --version-dir flag using cached data."""
    with TemporaryDirectory() as tmpdir:
        outpath = Path(tmpdir)
        generate(outpath, version_dir=True)

        from scripts.parse_help.utils import get_ffmpeg_version

        version = get_ffmpeg_version("ffmpeg")
        major = version.split(".")[0]
        version_dir = outpath / f"v{major}"

        # Version directory should exist
        assert version_dir.is_dir(), f"Expected {version_dir} to exist"

        # Should have key generated files
        assert (version_dir / "__init__.py").exists()
        assert (version_dir / "py.typed").exists()
        assert (version_dir / "filters.py").exists()
        assert (version_dir / "sources.py").exists()

        # Subdirectories should exist
        assert (version_dir / "streams").is_dir()
        assert (version_dir / "codecs").is_dir()
        assert (version_dir / "formats").is_dir()

        # Verify generated files contain absolute imports for shared core
        filters_content = (version_dir / "filters.py").read_text()
        assert (
            "from ffmpeg_core." in filters_content or "from ffmpeg." in filters_content
        ), (
            "Versioned output should use absolute imports for shared core (ffmpeg or ffmpeg_core)"
        )


def test_generate_from_cache() -> None:
    """Test code generation from cache using --version flag (no FFmpeg binary needed)."""
    with TemporaryDirectory() as tmpdir:
        outpath = Path(tmpdir)
        metadata = _get_version_metadata()

        _generate_for_version(
            version="8.1",
            outpath=outpath,
            rebuild=False,
            ffmpeg_binary="ffmpeg",
            version_dir=False,
            version_metadata=metadata,
        )

        assert (outpath / "filters.py").exists()
        assert (outpath / "sources.py").exists()
        assert (outpath / "streams" / "video.py").exists()

        # Should have deprecation hints
        filters_content = (outpath / "filters.py").read_text()
        streams_video = (outpath / "streams" / "video.py").read_text()
        combined = filters_content + streams_video
        assert "New in FFmpeg" in combined or "Removed in FFmpeg" in combined


def test_committed_version_bindings_import() -> None:
    """Test that committed version bindings for v5-v8 all import correctly."""
    try:
        import ffmpeg.versions
    except ImportError:
        pytest.skip("ffmpeg.versions not available (monorepo uses separate packages)")

    available = ffmpeg.versions.available()
    assert len(available) >= 4, f"Expected at least 4 versions, got {available}"

    for ver in available:
        mod = f"ffmpeg.v{ver}"
        # Test core submodule imports
        exec(f"from {mod} import filters, sources")
        exec(f"from {mod}.codecs import encoders, decoders")
        exec(f"from {mod}.formats import muxers, demuxers")
        exec(f"from {mod}.streams import audio, video")


def test_version_diff() -> None:
    """Test cross-version diff command produces meaningful output."""
    from ..version_diff import diff_versions

    delta = diff_versions("5.1", "8.0")
    total = (
        len(delta.filters_added)
        + len(delta.filters_removed)
        + len(delta.codecs_added)
        + len(delta.codecs_removed)
        + len(delta.formats_added)
        + len(delta.formats_removed)
    )
    assert total > 0, "Expected some differences between FFmpeg 5.1 and 8.0"


@pytest.mark.parametrize("version", ["5", "6", "7", "8"])
def test_version_deprecation_hints(version: str) -> None:
    """Test that version bindings contain deprecation hints in docstrings."""
    # Monorepo: packages/vN/src/ffmpeg; legacy: src/ffmpeg/vN
    repo_root = Path(__file__).resolve().parents[4]
    monorepo_dir = repo_root / "packages" / f"v{version}" / "src" / "ffmpeg"
    legacy_dir = repo_root / "src" / "ffmpeg" / f"v{version}"
    version_dir = monorepo_dir if monorepo_dir.exists() else legacy_dir
    if not version_dir.exists():
        pytest.skip(f"v{version} bindings not generated")

    # At least some version should have "New in FFmpeg" or "Removed in FFmpeg" notes
    filters_content = (version_dir / "filters.py").read_text()
    streams_video = (version_dir / "streams" / "video.py").read_text()
    combined = filters_content + streams_video

    has_notes = "New in FFmpeg" in combined or "Removed in FFmpeg" in combined
    # v5 is the earliest, so it won't have "New in" notes; v8 is latest so no "Removed in"
    # But intermediate versions should have both
    if version in ("6", "7"):
        assert has_notes, f"v{version} should have version notes in docstrings"
