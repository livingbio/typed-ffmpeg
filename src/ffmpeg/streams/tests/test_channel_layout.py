"""Tests for audio channel layout definitions."""

from ..channel_layout import CHANNEL_LAYOUT


def test_channel_layout_basic() -> None:
    """Test basic channel layout definitions."""
    assert CHANNEL_LAYOUT["mono"] == 1
    assert CHANNEL_LAYOUT["stereo"] == 2


def test_channel_layout_surround() -> None:
    """Test surround sound channel layouts."""
    assert CHANNEL_LAYOUT["5.1"] == 6
    assert CHANNEL_LAYOUT["7.1"] == 8


def test_channel_layout_complex() -> None:
    """Test complex channel layouts."""
    assert CHANNEL_LAYOUT["5.1.2"] == 8
    assert CHANNEL_LAYOUT["7.1.4"] == 12
    assert CHANNEL_LAYOUT["22.2"] == 24


def test_channel_layout_special() -> None:
    """Test special channel layouts."""
    assert CHANNEL_LAYOUT["quad"] == 4
    assert CHANNEL_LAYOUT["hexagonal"] == 6
    assert CHANNEL_LAYOUT["octagonal"] == 8
    assert CHANNEL_LAYOUT["hexadecagonal"] == 16


def test_channel_layout_downmix() -> None:
    """Test downmix channel layout."""
    assert CHANNEL_LAYOUT["downmix"] == 2


def test_channel_layout_all_defined() -> None:
    """Test that all channel layouts are defined with valid channel counts."""
    for layout, channels in CHANNEL_LAYOUT.items():
        assert isinstance(layout, str)
        assert isinstance(channels, int)
        assert channels > 0
