"""Tests for version_diff module."""

from ..version_diff import format_version_note


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
