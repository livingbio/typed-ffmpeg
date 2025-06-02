from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..probe import probe

test_data = Path(__file__).parent / "test_probe"


def is_static_image(format_name: str) -> bool:
    """Check if the format is a static image format."""
    return format_name in {"jpeg_pipe", "png_pipe", "webp_pipe"}


@pytest.mark.parametrize("path", test_data.glob("**/*.*"), ids=lambda x: x.name)
def test_probe_default(path: Path, snapshot: SnapshotAssertion) -> None:
    info = probe(path)

    # Check basic structure
    assert isinstance(info, dict)
    assert "format" in info
    assert "streams" in info

    # Check format section
    format_info = info["format"]
    assert isinstance(format_info, dict)
    assert "format_name" in format_info

    # Duration is not available for static images
    if not is_static_image(format_info["format_name"]):
        assert "duration" in format_info
        assert "size" in format_info
        assert "bit_rate" in format_info

    # Check streams section
    streams = info["streams"]
    assert isinstance(streams, list)
    assert len(streams) > 0

    # Check each stream
    for stream in streams:
        assert isinstance(stream, dict)
        assert "codec_type" in stream
        assert "index" in stream

        # codec_name is not available for data streams
        if stream["codec_type"] != "data":
            assert "codec_name" in stream

    snapshot(
        extension_class=JSONSnapshotExtension
    ) == info  # NOTE: the result is not stable so, we just want to record the result


@pytest.mark.parametrize("path", test_data.glob("**/*.*"), ids=lambda x: x.name)
def test_probe_complete(path: Path, snapshot: SnapshotAssertion) -> None:
    info = probe(
        path,
        show_program_version=True,
        show_library_versions=True,
        show_pixel_formats=True,
        show_packets=True,
        show_frames=True,
        show_programs=True,
        show_streams=True,
        show_chapters=True,
        show_format=True,
        show_error=True,
    )

    # Check basic structure
    assert isinstance(info, dict)
    assert "format" in info
    assert "streams" in info

    # Check format section
    format_info = info["format"]
    assert isinstance(format_info, dict)
    assert "format_name" in format_info

    # Duration is not available for static images
    if not is_static_image(format_info["format_name"]):
        assert "duration" in format_info
        assert "size" in format_info
        assert "bit_rate" in format_info

    # Check streams section
    streams = info["streams"]
    assert isinstance(streams, list)
    assert len(streams) > 0

    # Check each stream
    for stream in streams:
        assert isinstance(stream, dict)
        assert "codec_type" in stream
        assert "index" in stream

        # codec_name is not available for data streams
        if stream["codec_type"] != "data":
            assert "codec_name" in stream

            # Additional checks for complete probe
            if stream["codec_type"] == "video":
                assert "width" in stream
                assert "height" in stream
                # pix_fmt is not available for some formats like WebP
                if stream.get("codec_name") not in {"webp"}:
                    assert "pix_fmt" in stream
            elif stream["codec_type"] == "audio":
                assert "sample_rate" in stream
                assert "channels" in stream

    snapshot(
        extension_class=JSONSnapshotExtension
    ) == info  # NOTE: the result is not stable so, we just want to record the result
