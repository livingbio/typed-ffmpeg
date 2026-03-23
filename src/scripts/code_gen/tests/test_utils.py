import pytest

from ..utils import get_relative_import, get_relative_path


@pytest.mark.parametrize(
    "import_path, template_path, expected",
    [
        ("types", "options/framesync.py.jinja", "..types"),
        ("types", "dag/global_runnable/global_args.py.jinja", "...types"),
        ("streams.audio", "streams/audio.py.jinja", None),
        ("streams.video", "streams/audio.py.jinja", ".video"),
        ("dag.nodes", "filters.py.jinja", ".dag.nodes"),
        ("dag.nodes", "streams/audio.py.jinja", "..dag.nodes"),
        ("types", "streams/audio.py.jinja", "..types"),
        ("filters", "streams/audio.py.jinja", "..filters"),
        ("dag.nodes", "dag/io/_input.py.jinja", "..nodes"),
        ("codecs.schema", "codecs/encoders.py.jinja", ".schema"),
        ("formats.schema", "formats/muxers.py.jinja", ".schema"),
    ],
)
def test_get_relative_path(
    import_path: str, template_path: str, expected: str | None
) -> None:
    assert get_relative_path(import_path, template_path) == expected


def test_get_relative_import() -> None:
    # Test normal import
    result = get_relative_import(
        "types", "options/framesync.py.jinja", "Binary, Boolean"
    )
    assert result == "from ..types import Binary, Boolean"

    # Test same file import (should return empty string)
    result = get_relative_import(
        "streams.audio", "streams/audio.py.jinja", "AudioStream"
    )
    assert result == ""

    # Test nested import
    result = get_relative_import("dag.nodes", "streams/audio.py.jinja", "FilterNode")
    assert result == "from ..dag.nodes import FilterNode"


# --- Versioned import resolution tests ---

# Set of modules that are generated (have corresponding templates).
# All others are hand-written shared core.
GENERATED_MODULES = {
    "filters",
    "sources",
    "streams.video",
    "streams.audio",
    "codecs.encoders",
    "codecs.decoders",
    "formats.muxers",
    "formats.demuxers",
    "options.codec",
    "options.format",
    "dag.io._input",
    "dag.io._output",
    "dag.io.output_args",
    "dag.global_runnable.global_args",
}


class TestVersionedImportResolution:
    """
    Tests for get_relative_import with version_prefix parameter.

    When version_prefix is set (e.g., "v6"), generated files live in
    src/ffmpeg/v6/ instead of src/ffmpeg/. Imports between generated files
    use relative paths (both in v6/), but imports to shared hand-written
    core use absolute paths (from ffmpeg.{module}).
    """

    def test_generated_to_shared_types(self) -> None:
        """Types is hand-written → absolute import from ffmpeg.types."""
        result = get_relative_import(
            "types",
            "filters.py.jinja",
            "Int, String",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.types import Int, String"

    def test_generated_to_shared_dag_factory(self) -> None:
        """dag.factory is hand-written → absolute import."""
        result = get_relative_import(
            "dag.factory",
            "filters.py.jinja",
            "filter_node_factory",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.dag.factory import filter_node_factory"

    def test_generated_to_shared_dag_nodes(self) -> None:
        """dag.nodes is hand-written → absolute import."""
        result = get_relative_import(
            "dag.nodes",
            "filters.py.jinja",
            "FilterableStream, FilterNode",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.dag.nodes import FilterableStream, FilterNode"

    def test_generated_to_shared_schema(self) -> None:
        """Test that schema is treated as hand-written and uses an absolute import."""
        result = get_relative_import(
            "schema",
            "filters.py.jinja",
            "Default, StreamType",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.schema import Default, StreamType"

    def test_generated_to_shared_common_schema(self) -> None:
        """Test that common.schema is treated as hand-written and uses an absolute import."""
        result = get_relative_import(
            "common.schema",
            "filters.py.jinja",
            "FFMpegFilterDef",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.common.schema import FFMpegFilterDef"

    def test_generated_to_shared_options_framesync(self) -> None:
        """options.framesync is hand-written → absolute import."""
        result = get_relative_import(
            "options.framesync",
            "filters.py.jinja",
            "FFMpegFrameSyncOption",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.options.framesync import FFMpegFrameSyncOption"

    def test_generated_to_shared_utils(self) -> None:
        """Test that utils.frozendict is treated as hand-written and uses an absolute import."""
        result = get_relative_import(
            "utils.frozendict",
            "filters.py.jinja",
            "FrozenDict, merge",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.utils.frozendict import FrozenDict, merge"

    def test_generated_to_shared_from_nested(self) -> None:
        """Importing shared core from deeply nested generated file."""
        result = get_relative_import(
            "dag.nodes",
            "dag/io/_input.py.jinja",
            "FilterNode",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.dag.nodes import FilterNode"

    def test_generated_to_generated_sibling(self) -> None:
        """Both are generated → relative import."""
        result = get_relative_import(
            "streams.video",
            "filters.py.jinja",
            "VideoStream",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from .streams.video import VideoStream"

    def test_generated_to_generated_same_subdir(self) -> None:
        """Both generated, same subdirectory → relative import."""
        result = get_relative_import(
            "streams.video",
            "streams/audio.py.jinja",
            "VideoStream",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from .video import VideoStream"

    def test_generated_to_generated_options(self) -> None:
        """options.codec is generated → relative import."""
        result = get_relative_import(
            "options.codec",
            "filters.py.jinja",
            "FFMpegAVCodecContextEncoderOption",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from .options.codec import FFMpegAVCodecContextEncoderOption"

    def test_generated_dag_io_to_generated_codecs(self) -> None:
        """Both generated, different subdirs → relative import."""
        result = get_relative_import(
            "codecs.encoders",
            "dag/io/_output.py.jinja",
            "SomeEncoder",
            version_prefix="v7",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ...codecs.encoders import SomeEncoder"

    def test_self_import_returns_empty(self) -> None:
        """Self-import skip works with version_prefix."""
        result = get_relative_import(
            "filters",
            "filters.py.jinja",
            "something",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == ""

    def test_no_version_prefix_unchanged(self) -> None:
        """Without version_prefix, behavior is identical to before."""
        result = get_relative_import("types", "filters.py.jinja", "Int, String")
        assert result == "from .types import Int, String"

    def test_version_prefix_without_generated_modules(self) -> None:
        """
        Test that omitting generated_modules forces all imports to be absolute.

        If version_prefix is set but generated_modules is None,
        all imports become absolute (safe fallback for shared core).
        """
        result = get_relative_import(
            "types",
            "filters.py.jinja",
            "Int, String",
            version_prefix="v6",
            generated_modules=None,
        )
        assert result == "from ffmpeg.types import Int, String"

    def test_shared_codecs_schema(self) -> None:
        """codecs.schema is hand-written → absolute import."""
        result = get_relative_import(
            "codecs.schema",
            "dag/io/_output.py.jinja",
            "FFMpegEncoderOption",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.codecs.schema import FFMpegEncoderOption"

    def test_shared_streams_av(self) -> None:
        """streams.av is hand-written → absolute import."""
        result = get_relative_import(
            "streams.av",
            "streams/video.py.jinja",
            "AVStream",
            version_prefix="v6",
            generated_modules=GENERATED_MODULES,
        )
        assert result == "from ffmpeg.streams.av import AVStream"
