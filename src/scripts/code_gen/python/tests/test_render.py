from pathlib import Path

import pytest

from ..context import all_codecs

from ...schema import FFMpegOptionType
from ...render import render
from ..schema import PythonFFMpegCodec, PythonFFMpegOption, PythonFFMpegOptionChoice
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from syrupy.extensions.json import JSONSnapshotExtension
from tempfile import TemporaryDirectory
template_folder = Path(__file__).parent.parent / "templates/codecs"

def test_render(snapshot: SnapshotAssertion) -> None:
    fake_codec: list[PythonFFMpegCodec] = [PythonFFMpegCodec(
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
                )
            ),
        ),
        help="H.264 video codec for encoding/decoding",
        is_decoder=True,
        is_encoder=False,
    )]

    with TemporaryDirectory() as temp_dir:
        paths= render(
            template_folder=template_folder,
            outpath=Path(temp_dir) / "out",
            codecs=fake_codec
        )
        assert paths == [
            Path(temp_dir) / "out" / "decoders.py",
            Path(temp_dir) / "out" / "encoders.py",
        ]
        with open(paths[0], "rb") as f:
            assert f.read() == snapshot(name="decoders.py", extension_class=SingleFileSnapshotExtension)
        with open(paths[1], "rb") as f:
            assert f.read() == snapshot(name="encoders.py", extension_class=SingleFileSnapshotExtension)


@pytest.mark.dev_only
def test_gen_codecs(snapshot: SnapshotAssertion) -> None:
    codecs = all_codecs()

    with TemporaryDirectory() as temp_dir:
        paths = render(
            template_folder=template_folder,
            outpath=Path(temp_dir) / "out",
            codecs=codecs
        )
        assert paths == [
            Path(temp_dir) / "out" / "decoders.py",
            Path(temp_dir) / "out" / "encoders.py",
        ]
        with open(paths[0], "rb") as f:
            assert f.read() == snapshot(name="decoders.py", extension_class=SingleFileSnapshotExtension)
        with open(paths[1], "rb") as f:
            assert f.read() == snapshot(name="encoders.py", extension_class=SingleFileSnapshotExtension)