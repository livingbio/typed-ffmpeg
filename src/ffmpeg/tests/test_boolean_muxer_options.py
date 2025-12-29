"""
Test cases for boolean muxer options that require explicit 1/0 values.

FFmpeg expects certain boolean options like strftime and reset_timestamps
to be passed as -option 1 or -option 0, not just -option.
"""

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from .. import formats
from ..base import input


def test_hls_muxer_strftime_boolean_option(snapshot: SnapshotAssertion) -> None:
    """
    Test that strftime=True for HLS muxer outputs -strftime 1, not -strftime.

    FFmpeg expects -strftime 1 or -strftime 0, not just -strftime without a value.
    """
    input1 = input("input1.mp4")
    out = input1.output(
        filename="out.m3u8", f="hls", muxer_options=formats.muxers.hls(strftime=True)
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())


def test_hls_muxer_strftime_false_boolean_option(snapshot: SnapshotAssertion) -> None:
    """Test that strftime=False for HLS muxer outputs -strftime 0."""
    input1 = input("input1.mp4")
    out = input1.output(
        filename="out.m3u8", f="hls", muxer_options=formats.muxers.hls(strftime=False)
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())


def test_segment_muxer_reset_timestamps_boolean_option(
    snapshot: SnapshotAssertion,
) -> None:
    """
    Test that reset_timestamps=True for segment muxer outputs -reset_timestamps 1.

    FFmpeg expects -reset_timestamps 1 or -reset_timestamps 0, not just -reset_timestamps without a value.
    """
    input1 = input("input1.mp4")
    out = input1.output(
        filename="out%03d.mp4",
        f="segment",
        muxer_options=formats.muxers.segment(reset_timestamps=True),
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())


def test_hls_muxer_strftime_mkdir_boolean_option(snapshot: SnapshotAssertion) -> None:
    """Test that strftime_mkdir=True for HLS muxer outputs -strftime_mkdir 1."""
    input1 = input("input1.mp4")
    out = input1.output(
        filename="out.m3u8",
        f="hls",
        muxer_options=formats.muxers.hls(strftime_mkdir=True),
    )
    assert snapshot(extension_class=JSONSnapshotExtension) == (out.compile())
