from pathlib import Path
from tempfile import TemporaryDirectory

from ..cli import generate


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
        assert "from ffmpeg." in filters_content, (
            "Versioned output should use absolute imports for shared core"
        )
