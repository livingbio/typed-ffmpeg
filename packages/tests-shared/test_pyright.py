"""
Regression test for https://github.com/livingbio/typed-ffmpeg/issues/923

Verifies that Pyright can resolve .output() on AVStream / AudioStream / VideoStream.
In v4.0.x the method was injected dynamically via setattr(), which Pyright cannot see.
"""

import subprocess
import sys
import textwrap

import pytest

# Minimal reproduction from the issue report
_SAMPLE = textwrap.dedent("""
    import ffmpeg

    stream = ffmpeg.input("in.mp3")
    stream.output(filename="out.wav")

    ffmpeg.input("in.mp3").audio.output(filename="out.wav")
    ffmpeg.input("in.mp3").video.output(filename="out.mp4")
""")


@pytest.fixture(scope="module")
def sample_file(tmp_path_factory):
    p = tmp_path_factory.mktemp("pyright") / "issue_923.py"
    p.write_text(_SAMPLE)
    return p


def _run_pyright(sample_file):
    result = subprocess.run(
        [sys.executable, "-m", "pyright", str(sample_file)],
        capture_output=True,
        text=True,
    )
    return result


def test_pyright_available(sample_file):
    """Skip the type-check test if pyright is not installed."""
    result = subprocess.run(
        [sys.executable, "-m", "pyright", "--version"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.skip("pyright not installed")


def test_output_method_visible_to_pyright(sample_file):
    """
    .output() must be statically visible on AVStream / AudioStream / VideoStream.

    Regression: v4.0.x injected output() via setattr() at runtime, making it
    invisible to Pyright (reportAttributeAccessIssue).
    """
    result = subprocess.run(
        [sys.executable, "-m", "pyright", "--version"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.skip("pyright not installed")

    result = _run_pyright(sample_file)
    assert "0 errors" in result.stdout, (
        f"Pyright reported errors — .output() is not visible to the type checker.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
