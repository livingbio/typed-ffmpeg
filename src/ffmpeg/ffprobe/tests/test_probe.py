import subprocess
import time
from dataclasses import asdict
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..probe import probe, probe_obj

test_data = Path(__file__).parent / "test_probe"


def is_static_image(format_name: str) -> bool:
    """
    Check if the format is a static image format.

    Args:
        format_name: The format name to check

    Returns:
        True if the format is a static image format, False otherwise

    """
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
        name="json", extension_class=JSONSnapshotExtension
    ) == info  # NOTE: the result is not stable so, we just want to record the result

    obj = probe_obj(path)
    assert obj is not None
    snapshot(name="obj", extension_class=JSONSnapshotExtension) == asdict(obj)


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
        name="json", extension_class=JSONSnapshotExtension
    ) == info  # NOTE: the result is not stable so, we just want to record the result

    obj = probe_obj(
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
    assert obj is not None
    snapshot(name="obj", extension_class=JSONSnapshotExtension) == asdict(obj)


def test_probe_timeout_cleanup() -> None:
    """
    Test that ffprobe subprocess is properly cleaned up when timeout occurs.

    This test verifies that when a TimeoutExpired exception is raised,
    the subprocess is terminated and pipes are closed, preventing memory leaks.
    """
    # Use unittest.mock to create a test scenario
    # Create a test file that exists
    import tempfile
    from unittest.mock import patch

    import psutil

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
        tmp_path = tmp.name
        # Write some minimal data so the file exists
        tmp.write(b"fake video data")

    try:
        # Mock a long-running process that will timeout
        original_popen = subprocess.Popen

        def mock_popen(*args, **kwargs):
            # Create a real subprocess that will take a long time
            # We'll use 'sleep' command instead of ffprobe
            if "ffprobe" in str(args[0]):
                # Replace ffprobe with a sleep command that takes longer than timeout
                new_args = ["sleep", "30"]
                proc = original_popen(new_args, **kwargs)
                return proc
            return original_popen(*args, **kwargs)

        with patch("subprocess.Popen", side_effect=mock_popen):
            # Get list of current sleep processes before the test
            sleep_pids_before = {
                p.pid for p in psutil.process_iter() if p.name() == "sleep"
            }

            # Try to probe with a very short timeout
            # This should raise TimeoutExpired
            with pytest.raises(subprocess.TimeoutExpired):
                probe(tmp_path, timeout=1)  # 1 second timeout

            # Give a moment for cleanup to complete
            time.sleep(0.5)

            # Get list of current sleep processes after the test
            sleep_pids_after = {
                p.pid for p in psutil.process_iter() if p.name() == "sleep"
            }

            # There should be no new sleep processes lingering
            # (all processes started should have been terminated)
            new_sleep_pids = sleep_pids_after - sleep_pids_before
            assert len(new_sleep_pids) == 0, (
                f"Expected no new sleep processes, but found {len(new_sleep_pids)} lingering: {new_sleep_pids}"
            )

    finally:
        # Clean up the temp file
        Path(tmp_path).unlink(missing_ok=True)
