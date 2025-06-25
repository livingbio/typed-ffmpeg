from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ...render import render
from ..context import all_codecs, all_formats
from ..schema import (
    PythonFFMpegCodec,
    PythonFFMpegFormat,
    PythonFFMpegOption,
    PythonFFMpegOptionChoice,
)

template_folder = Path(__file__).parent.parent / "templates"


def test_render_codecs(snapshot: SnapshotAssertion) -> None:
    fake_codec: list[PythonFFMpegCodec] = [
        PythonFFMpegCodec(
            name="h264",
            options=(
                PythonFFMpegOption(
                    name="profile",
                    type="string",
                    default=None,
                    help="Set H.264 profile (baseline, main, high)",
                    choices=(
                        PythonFFMpegOptionChoice(
                            name="baseline",
                            help="Baseline profile for compatibility",
                            flags="baseline",
                            value="baseline",
                        ),
                    ),
                ),
            ),
            help="H.264 video codec for encoding/decoding",
            is_decoder=True,
            is_encoder=False,
        )
    ]

    with TemporaryDirectory() as temp_dir:
        paths = render(
            template_folder=template_folder / "codecs",
            outpath=Path(temp_dir) / "out",
            codecs=fake_codec,
        )

        for path in paths:
            assert path.exists()
            assert path.is_file()
            assert path.suffix == ".py"

            with open(path, "rb") as f:
                assert f.read() == snapshot(
                    name=path.name, extension_class=SingleFileSnapshotExtension
                )


def test_render_formats(snapshot: SnapshotAssertion) -> None:
    fake_format: list[PythonFFMpegFormat] = [
        PythonFFMpegFormat(
            name="mp4",
            options=(
                PythonFFMpegOption(
                    name="profile",
                    type="string",
                    default=None,
                    help="Set MP4 profile (baseline, main, high)",
                    choices=(
                        PythonFFMpegOptionChoice(
                            name="baseline",
                            help="Baseline profile for compatibility",
                            flags="baseline",
                            value="baseline",
                        ),
                    ),
                ),
            ),
            help="MP4 container format",
            is_muxer=True,
            is_demuxer=False,
        )
    ]

    with TemporaryDirectory() as temp_dir:
        paths = render(
            template_folder=template_folder / "formats",
            outpath=Path(temp_dir) / "out",
            formats=fake_format,
        )

        for path in paths:
            assert path.exists()
            assert path.is_file()
            assert path.suffix == ".py"

            with open(path, "rb") as f:
                assert f.read() == snapshot(
                    name=path.name, extension_class=SingleFileSnapshotExtension
                )


@pytest.mark.dev_only
def test_gen_codecs() -> None:
    codecs = all_codecs()

    outpath = Path("out") / "test_gen_codecs"
    render(template_folder=template_folder / "codecs", outpath=outpath, codecs=codecs)


@pytest.mark.dev_only
def test_gen_formats() -> None:
    formats = all_formats()

    outpath = Path("out") / "test_gen_formats"
    render(
        template_folder=template_folder / "formats", outpath=outpath, formats=formats
    )
