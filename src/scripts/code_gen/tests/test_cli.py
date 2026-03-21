import tempfile
import urllib.request
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from ..cli import _convert_av_options, generate, reexport
from ..schema import FFMpegAVOption, FFMpegOptionChoice


def _has_network() -> bool:
    """Check if network access is available."""
    try:
        urllib.request.urlopen("https://ffmpeg.org", timeout=3)
        return True
    except Exception:
        return False


# --- _convert_av_options ---


class TestConvertAVOptions:
    def test_empty_list(self) -> None:
        result = _convert_av_options([])
        assert result == ()

    def test_single_option(self) -> None:
        from scripts.parse_help.schema import FFMpegAVOption as ParseHelpAVOption
        from scripts.parse_help.schema import FFMpegOptionChoice as ParseHelpChoice

        choices = (ParseHelpChoice(name="fast", help="fast mode", flags="", value="1"),)
        src = ParseHelpAVOption(
            section="AVCodecContext",
            name="preset",
            type="string",
            flags="E..V.......",
            help="encoding preset",
            min="0",
            max="100",
            default="medium",
            choices=choices,
        )
        result = _convert_av_options([src])
        assert len(result) == 1
        assert isinstance(result[0], FFMpegAVOption)
        assert result[0].name == "preset"
        assert result[0].section == "AVCodecContext"
        assert result[0].default == "medium"
        assert len(result[0].choices) == 1
        assert isinstance(result[0].choices[0], FFMpegOptionChoice)
        assert result[0].choices[0].name == "fast"

    def test_multiple_options(self) -> None:
        from scripts.parse_help.schema import FFMpegAVOption as ParseHelpAVOption

        opts = [
            ParseHelpAVOption(
                section="s", name="a", type="int", flags="", help="h1"
            ),
            ParseHelpAVOption(
                section="s", name="b", type="string", flags="", help="h2"
            ),
        ]
        result = _convert_av_options(opts)
        assert len(result) == 2
        assert result[0].name == "a"
        assert result[1].name == "b"


# --- generate ---


@pytest.mark.skipif(
    not _has_network(),
    reason="Requires network access to download filter docs",
)
def test_generate() -> None:
    outpath = Path(TemporaryDirectory().name)
    generate(outpath)


def test_generate_unsupported_version() -> None:
    """generate raises BadParameter for old FFmpeg versions."""
    import typer
    from unittest.mock import patch

    with patch(
        "scripts.parse_help.utils.get_ffmpeg_version", return_value="4.4"
    ):
        with pytest.raises(typer.BadParameter, match="not supported"):
            generate(Path("/tmp/test_out"), ffmpeg_binary="ffmpeg")


# --- reexport ---


def test_reexport_no_version_dirs() -> None:
    """reexport exits with error when no version dirs exist."""
    from click.exceptions import Exit

    with tempfile.TemporaryDirectory() as outpath:
        with pytest.raises(Exit):
            reexport(outpath=Path(outpath))


def test_reexport_with_version_dir() -> None:
    """reexport generates re-export modules for existing version dir."""
    with tempfile.TemporaryDirectory() as outpath:
        out = Path(outpath)
        vdir = out / "v7"
        vdir.mkdir()

        # Create a minimal filters.py in the version dir
        filters_content = '''\
# NOTE: this file is auto-generated, do not modify
def overlay() -> None:
    """Apply overlay filter."""
    pass


def scale() -> None:
    """Scale video."""
    pass


def _private() -> None:
    pass
'''
        (vdir / "filters.py").write_text(filters_content)
        (vdir / "sources.py").write_text(
            "# NOTE: this file is auto-generated\n"
            "def sine() -> None:\n    pass\n"
        )

        reexport(outpath=out, version="7")

        # Check that re-export file was created
        reexport_file = out / "filters.py"
        assert reexport_file.exists()
        content = reexport_file.read_text()
        assert "from ffmpeg.v7.filters import" in content
        assert "overlay" in content
        assert "scale" in content
        # Private functions should not be re-exported
        assert "_private" not in content

        # Check sources re-export
        sources_file = out / "sources.py"
        assert sources_file.exists()
        assert "sine" in sources_file.read_text()


def test_reexport_nonexistent_version() -> None:
    """reexport exits when specified version dir doesn't exist."""
    from click.exceptions import Exit

    with tempfile.TemporaryDirectory() as outpath:
        with pytest.raises(Exit):
            reexport(outpath=Path(outpath), version="99")
