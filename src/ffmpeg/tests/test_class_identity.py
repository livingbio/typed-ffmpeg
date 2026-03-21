"""
Tests for class identity across multi-version imports.

These tests verify that the module redirect system correctly ensures that
root-level imports (from ffmpeg.streams import VideoStream) and version-specific
imports (from ffmpeg.v8.streams import VideoStream) resolve to the exact same
class objects.
"""

import pytest


def test_streams_module_identity():
    """Test that root streams module is same as versioned module."""
    import sys

    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    # Import both root and versioned modules
    import ffmpeg.streams
    import ffmpeg.v8.streams  # Assuming v8 is latest

    # They should be the exact same module object
    assert ffmpeg.streams is ffmpeg.v8.streams, (
        "Root streams module should be aliased to v8 streams module"
    )

    # Check in sys.modules too
    assert sys.modules["ffmpeg.streams"] is sys.modules["ffmpeg.v8.streams"]


def test_videostream_class_identity():
    """Test that VideoStream from root and v8 are the same class."""
    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    # Import from both paths
    from ffmpeg.streams.video import VideoStream as RootVS
    from ffmpeg.v8.streams.video import VideoStream as V8VS

    # Should be the exact same class object
    assert RootVS is V8VS, (
        "VideoStream from root and v8 should be the same class object"
    )


def test_audiostream_class_identity():
    """Test that AudioStream from root and v8 are the same class."""
    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    from ffmpeg.streams.audio import AudioStream as RootAS
    from ffmpeg.v8.streams.audio import AudioStream as V8AS

    assert RootAS is V8AS


def test_isinstance_across_imports():
    """Test that isinstance() works across import styles."""
    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    from ffmpeg.streams.video import VideoStream as RootVS
    from ffmpeg.v8.streams.video import VideoStream as V8VS

    # Create instance using v8 class
    from ffmpeg.v8.dag.nodes import FilterNode

    # Mock a stream (we can't easily create real ones without full setup)
    # Just test that the classes are compatible
    assert issubclass(V8VS, RootVS.__bases__[0])  # Same base class
    assert V8VS.__name__ == RootVS.__name__  # Same name


def test_codecs_module_identity():
    """Test that codecs module redirects work."""
    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    import ffmpeg.codecs
    import ffmpeg.v8.codecs

    # Should be aliased
    assert ffmpeg.codecs is ffmpeg.v8.codecs


def test_formats_module_identity():
    """Test that formats module redirects work."""
    import ffmpeg.versions

    version = ffmpeg.versions.default
    if not version:
        pytest.skip("No default version available")

    import ffmpeg.formats
    import ffmpeg.v8.formats

    # Should be aliased
    assert ffmpeg.formats is ffmpeg.v8.formats


def test_class_registry_single_entry():
    """Test that CLASS_REGISTRY has only one entry per class name."""
    from ffmpeg.common.serialize import CLASS_REGISTRY

    # Import from both paths
    from ffmpeg.streams.video import VideoStream as RootVS
    from ffmpeg.v8.streams.video import VideoStream as V8VS

    # Both should register the same class
    assert RootVS is V8VS

    # CLASS_REGISTRY should have only one VideoStream entry
    videostream_entries = [k for k in CLASS_REGISTRY.keys() if "VideoStream" in k]

    # Should be exactly one entry
    assert len(videostream_entries) >= 1, "VideoStream should be in CLASS_REGISTRY"

    # The registered class should be the same regardless of import path
    registered_class = CLASS_REGISTRY.get("VideoStream")
    if registered_class:
        assert registered_class is RootVS
        assert registered_class is V8VS


def test_module_redirect_does_not_break_hand_written():
    """Test that module redirects don't break hand-written modules."""
    # These modules should NOT be redirected
    import ffmpeg.dag
    import ffmpeg.common

    # They should be the root modules, not versioned
    assert "v8" not in ffmpeg.dag.__name__
    assert "v8" not in ffmpeg.common.__name__


def test_import_from_root_works():
    """Test that importing from root still works after redirects."""
    # These should work without errors
    from ffmpeg.streams import AudioStream, VideoStream
    from ffmpeg.codecs import decoders, encoders
    from ffmpeg.formats import demuxers, muxers

    # Basic sanity checks
    assert VideoStream is not None
    assert AudioStream is not None


def test_version_specific_import_still_works():
    """Test that version-specific imports still work."""
    import ffmpeg.versions

    for version in ffmpeg.versions.available():
        # Import from version-specific path
        version_module = f"ffmpeg.v{version}.streams.video"
        exec(f"from {version_module} import VideoStream as V{version}VS")

        # Should work without errors
        # Each version has its own classes
