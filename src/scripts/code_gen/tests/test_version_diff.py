"""Tests for version_diff module."""

from unittest.mock import patch

from ..version_diff import (
    VersionDelta,
    VersionMetadata,
    build_version_metadata,
    diff_versions,
    format_version_note,
)


class TestFormatVersionNote:
    """Tests for generating version availability notes."""

    def test_new_in_version(self) -> None:
        """Test that a filter first appearing in a later version is noted as new."""
        version_map = {"dnn_processing": {"7", "8"}, "overlay": {"5", "6", "7", "8"}}
        all_versions = ["5.0", "6.0", "7.0", "8.0"]
        result = format_version_note("dnn_processing", version_map, all_versions, "7")
        assert result == "New in FFmpeg 7.0."

    def test_removed_in_later_version(self) -> None:
        """Test that a filter absent from the latest version is noted as removed."""
        version_map = {"old_filter": {"5", "6", "7"}}
        all_versions = ["5.0", "6.0", "7.0", "8.0"]
        result = format_version_note("old_filter", version_map, all_versions, "7")
        assert result == "Removed in FFmpeg 8.0."

    def test_no_note_for_always_present(self) -> None:
        """Test that a filter present in all versions returns no note."""
        version_map = {"overlay": {"5", "6", "7", "8"}}
        all_versions = ["5.0", "6.0", "7.0", "8.0"]
        result = format_version_note("overlay", version_map, all_versions, "7")
        assert result is None

    def test_not_in_version_map(self) -> None:
        """Test that a filter not found in the version map returns no note."""
        version_map: dict[str, set[str]] = {}
        all_versions = ["5.0", "6.0"]
        result = format_version_note("unknown", version_map, all_versions, "6")
        assert result is None

    def test_no_longer_available(self) -> None:
        """Test that a filter missing from the target version is noted as unavailable."""
        version_map = {"legacy_filter": {"5", "6"}}
        all_versions = ["5.0", "6.0", "7.0"]
        result = format_version_note("legacy_filter", version_map, all_versions, "7")
        assert result == "No longer available in FFmpeg 7.0."

    def test_empty_versions(self) -> None:
        """Test that an empty all_versions list returns no note."""
        version_map = {"overlay": {"5"}}
        all_versions: list[str] = []
        result = format_version_note("overlay", version_map, all_versions, "5")
        assert result is None

    def test_new_in_earliest_version(self) -> None:
        """If present in earliest version, not 'new'."""
        version_map = {"overlay": {"5", "6", "7"}}
        all_versions = ["5.0", "6.0", "7.0"]
        result = format_version_note("overlay", version_map, all_versions, "5")
        assert result is None

    def test_present_only_in_current(self) -> None:
        """Present in current version only; earlier versions exist → new."""
        version_map = {"new_filter": {"7"}}
        all_versions = ["5.0", "6.0", "7.0"]
        result = format_version_note("new_filter", version_map, all_versions, "7")
        assert result == "New in FFmpeg 7.0."

    def test_gap_in_later_versions(self) -> None:
        """Filter removed in v7 but present in v8 → still notes removal at v7."""
        version_map = {"quirky": {"5", "6", "8"}}
        all_versions = ["5.0", "6.0", "7.0", "8.0"]
        result = format_version_note("quirky", version_map, all_versions, "6")
        assert result == "Removed in FFmpeg 7.0."


class TestVersionDelta:
    def test_dataclass_frozen(self) -> None:
        delta = VersionDelta(from_version="6.0", to_version="7.0")
        assert delta.filters_added == ()
        assert delta.codecs_removed == ()

    def test_dataclass_with_data(self) -> None:
        delta = VersionDelta(
            from_version="6.0",
            to_version="7.0",
            filters_added=("dnn_processing",),
            filters_removed=("old_filter",),
        )
        assert delta.filters_added == ("dnn_processing",)
        assert delta.filters_removed == ("old_filter",)


class TestDiffVersions:
    def test_with_missing_caches(self) -> None:
        """When cache files don't exist, returns empty tuples."""
        delta = diff_versions("99.0", "100.0")
        assert delta.filters_added == ()
        assert delta.filters_removed == ()
        assert delta.codecs_added == ()
        assert delta.formats_added == ()

    def test_with_mocked_caches(self) -> None:
        """Test diff_versions with mocked cache loading."""

        class FakeFilter:
            def __init__(self, name: str):
                self.name = name

        class FakeCodec:
            def __init__(self, name: str):
                self.name = name

        class FakeFormat:
            def __init__(self, name: str):
                self.name = name

        def mock_load_names(cache_prefix: str, version_key: str, cls: type) -> set[str] | None:
            data = {
                ("filters", "6_0"): {"overlay", "scale", "old_filter"},
                ("filters", "7_0"): {"overlay", "scale", "dnn_processing"},
                ("codecs", "6_0"): {"h264", "aac"},
                ("codecs", "7_0"): {"h264", "aac", "av1"},
                ("formats", "6_0"): {"mp4", "mkv"},
                ("formats", "7_0"): {"mp4", "mkv"},
            }
            return data.get((cache_prefix, version_key))

        with patch(
            "scripts.code_gen.version_diff._load_names_from_cache",
            side_effect=mock_load_names,
        ):
            delta = diff_versions("6.0", "7.0")

        assert delta.filters_added == ("dnn_processing",)
        assert delta.filters_removed == ("old_filter",)
        assert delta.codecs_added == ("av1",)
        assert delta.codecs_removed == ()
        assert delta.formats_added == ()
        assert delta.formats_removed == ()


class TestBuildVersionMetadata:
    def test_with_missing_caches(self) -> None:
        """When no caches exist, returns empty metadata."""
        metadata = build_version_metadata(["99.0", "100.0"])
        assert metadata.available_versions == ["100.0", "99.0"]
        assert metadata.filter_versions == {}
        assert metadata.codec_versions == {}
        assert metadata.format_versions == {}

    def test_with_mocked_caches(self) -> None:
        def mock_load_names(cache_prefix: str, version_key: str, cls: type) -> set[str] | None:
            data = {
                ("filters", "6_0"): {"overlay", "scale"},
                ("filters", "7_0"): {"overlay", "scale", "new_filter"},
                ("codecs", "6_0"): {"h264"},
                ("codecs", "7_0"): {"h264", "av1"},
                ("formats", "6_0"): {"mp4"},
                ("formats", "7_0"): {"mp4"},
            }
            return data.get((cache_prefix, version_key))

        with patch(
            "scripts.code_gen.version_diff._load_names_from_cache",
            side_effect=mock_load_names,
        ):
            metadata = build_version_metadata(["6.0", "7.0"])

        assert metadata.available_versions == ["6.0", "7.0"]
        assert metadata.filter_versions["overlay"] == {"6", "7"}
        assert metadata.filter_versions["new_filter"] == {"7"}
        assert metadata.codec_versions["av1"] == {"7"}
        assert metadata.format_versions["mp4"] == {"6", "7"}

    def test_version_metadata_defaults(self) -> None:
        m = VersionMetadata()
        assert m.filter_versions == {}
        assert m.codec_versions == {}
        assert m.format_versions == {}
        assert m.available_versions == []
