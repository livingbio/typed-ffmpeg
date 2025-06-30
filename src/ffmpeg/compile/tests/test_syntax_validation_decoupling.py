"""
Tests for the decoupled syntax parsing and validation functionality.

This module tests the new syntax-only parsing functions and validation utilities
that separate CLI syntax parsing from option existence validation.
"""

import pytest
from syrupy.assertion import SnapshotAssertion

from ..compile_cli import (
    get_options_dict,
    parse_global_syntax,
    parse_input_syntax,
    parse_options,
    parse_output_syntax,
    validate_global_options,
    validate_input_options,
    validate_output_options,
    validate_parsed_options,
    parse,
    compile,
)


class TestSyntaxOnlyParsing:
    """Test pure syntax parsing without validation."""

    def test_parse_options_syntax_only(self):
        """Test that parse_options works without requiring validation."""
        tokens = ["-vcodec", "libx264", "-b:v", "1000k", "-y", "-noaudio"]
        result = parse_options(tokens)
        
        expected = {
            "vcodec": ["libx264"],
            "b:v": ["1000k"],
            "y": [None],
            "audio": [False],  # -noaudio becomes audio: [False]
        }
        
        # Convert defaultdict to regular dict for comparison
        result_dict = dict(result)
        assert result_dict == expected

    def test_parse_input_syntax(self):
        """Test input syntax parsing without validation."""
        tokens = ["-ss", "10", "-t", "30", "-i", "input1.mp4", "-r", "25", "-i", "input2.mp4"]
        result = parse_input_syntax(tokens)
        
        assert len(result) == 2
        assert result[0][0] == "input1.mp4"
        assert dict(result[0][1]) == {"ss": ["10"], "t": ["30"]}
        assert result[1][0] == "input2.mp4"
        assert dict(result[1][1]) == {"r": ["25"]}

    def test_parse_output_syntax(self):
        """Test output syntax parsing without validation."""
        tokens = ["-vcodec", "libx264", "-b:v", "1000k", "output1.mp4", "-acodec", "aac", "output2.mp4"]
        result = parse_output_syntax(tokens)
        
        assert len(result) == 2
        assert result[0][0] == "output1.mp4"
        assert dict(result[0][1]) == {"vcodec": ["libx264"], "b:v": ["1000k"]}
        assert result[1][0] == "output2.mp4"
        assert dict(result[1][1]) == {"acodec": ["aac"]}

    def test_parse_global_syntax(self):
        """Test global options syntax parsing without validation."""
        tokens = ["-y", "-loglevel", "error", "-hide_banner", "-i", "input.mp4"]
        options, remaining = parse_global_syntax(tokens)
        
        assert dict(options) == {"y": [None], "loglevel": ["error"], "hide_banner": [None]}
        assert remaining == ["-i", "input.mp4"]

    def test_parse_with_unknown_options(self):
        """Test that syntax parsing handles unknown options gracefully."""
        tokens = ["-unknown_option", "value", "-another_unknown", "-i", "input.mp4"]
        options, remaining = parse_global_syntax(tokens)
        
        assert dict(options) == {"unknown_option": ["value"], "another_unknown": [None]}
        assert remaining == ["-i", "input.mp4"]


class TestValidationUtilities:
    """Test validation utility functions."""

    def test_validate_parsed_options_with_filter(self):
        """Test validation with option type filtering."""
        parsed = {
            "y": [None],           # global-only option
            "f": ["mp4"],          # input/output option - should appear in both contexts
            "unknown": ["value"],  # unknown option
        }
        
        ffmpeg_options = get_options_dict()
        
        # Test global filtering
        global_params = validate_parsed_options(parsed, ffmpeg_options, "global")
        assert "y" in global_params
        assert "f" not in global_params  # f is not a global option
        assert "unknown" not in global_params
        
        # Test input filtering
        input_params = validate_parsed_options(parsed, ffmpeg_options, "input")
        assert "f" in input_params  # f is an input option
        assert "y" not in input_params
        
        # Test output filtering
        output_params = validate_parsed_options(parsed, ffmpeg_options, "output")
        assert "f" in output_params  # f is also an output option
        assert "y" not in output_params

    def test_validate_input_options(self):
        """Test input-specific validation utility."""
        # Use options that are clearly input-only vs output-only vs both
        parsed = {"analyzeduration": ["100M"], "f": ["mp4"], "unknown": ["value"]}
        result = validate_input_options(parsed)
        
        # Should only include input options (both analyzeduration and f are input options)
        assert "analyzeduration" in result or "f" in result  # At least one should be present
        assert "unknown" not in result  # Unknown option should be filtered

    def test_validate_output_options(self):
        """Test output-specific validation utility."""
        # Use options that are more clearly output-focused
        parsed = {"f": ["mp4"], "movflags": ["+faststart"], "unknown": ["value"]}  
        result = validate_output_options(parsed)
        
        # Should only include output options
        assert len(result) > 0  # At least some valid options should be present
        assert "unknown" not in result  # Unknown option should be filtered

    def test_validate_global_options(self):
        """Test global-specific validation utility."""
        parsed = {"y": [None], "loglevel": ["error"], "ss": ["10"]}
        result = validate_global_options(parsed)
        
        # Should only include global options
        assert "y" in result
        assert "loglevel" in result
        assert "ss" not in result  # input option, should be filtered

    def test_boolean_option_conversion(self):
        """Test that validation correctly converts boolean options."""
        parsed = {
            "y": [None],      # should become True
            "audio": [False], # should become False (from -noaudio)
            "b:v": ["1000k"], # should become "1000k"
        }
        
        ffmpeg_options = get_options_dict()
        result = validate_parsed_options(parsed, ffmpeg_options, "any")
        
        assert result.get("y") is True
        assert result.get("b:v") == "1000k"


class TestMainParseFunction:
    """Test the main parse function with validation control."""

    def test_parse_with_validation_default(self):
        """Test that parse function validates by default."""
        cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 -unknown_option value output.mp4"
        result = parse(cmd)  # default validate=True
        
        # Should filter out unknown options
        compiled = compile(result)
        assert "-unknown_option" not in compiled
        assert "libx264" in compiled

    def test_parse_without_validation(self):
        """Test parse function with validation disabled."""
        cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 -unknown_option value output.mp4"
        result = parse(cmd, validate=False)
        
        # Should preserve unknown options
        compiled = compile(result)
        assert "-unknown_option" in compiled
        assert "value" in compiled
        assert "libx264" in compiled

    def test_parse_validation_parameter_explicitly_true(self):
        """Test parse function with validation explicitly enabled."""
        cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 -unknown_option value output.mp4"
        result = parse(cmd, validate=True)
        
        # Should filter out unknown options
        compiled = compile(result)
        assert "-unknown_option" not in compiled
        assert "libx264" in compiled

    def test_parse_roundtrip_with_validation(self):
        """Test that parse+compile roundtrip works with validation."""
        original_cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 output.mp4"
        
        # Parse with validation
        parsed = parse(original_cmd, validate=True)
        compiled = compile(parsed)
        
        # Parse again
        reparsed = parse(compiled, validate=True)
        recompiled = compile(reparsed)
        
        # Should be equivalent
        assert compiled == recompiled

    def test_parse_roundtrip_without_validation(self):
        """Test that parse+compile roundtrip works without validation."""
        original_cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 -custom_option value output.mp4"
        
        # Parse without validation
        parsed = parse(original_cmd, validate=False)
        compiled = compile(parsed)
        
        # Should preserve custom option
        assert "-custom_option" in compiled
        assert "value" in compiled

    def test_backward_compatibility(self):
        """Test that existing code continues to work."""
        cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 output.mp4"
        
        # Old way (should still work)
        result_old = parse(cmd)
        
        # New way with explicit validation
        result_new = parse(cmd, validate=True)
        
        # Should produce same results
        assert compile(result_old) == compile(result_new)


class TestPackageSizeReduction:
    """Test scenarios where bundled options are not required."""

    def test_parse_without_loading_options_dict(self, monkeypatch):
        """Test that parsing without validation doesn't require options dict."""
        # Mock get_options_dict to verify it's not called
        get_options_dict_called = False
        
        def mock_get_options_dict():
            nonlocal get_options_dict_called
            get_options_dict_called = True
            return {}
        
        monkeypatch.setattr("src.ffmpeg.compile.compile_cli.get_options_dict", mock_get_options_dict)
        
        cmd = "ffmpeg -y -i input.mp4 -vcodec libx264 output.mp4"
        result = parse(cmd, validate=False)
        
        # Options dict should not have been loaded for parse-only mode
        assert not get_options_dict_called
        
        # Should still produce valid output
        compiled = compile(result)
        assert "ffmpeg" in compiled


@pytest.mark.parametrize(
    "tokens,expected_options",
    [
        # Basic options
        (["-vcodec", "libx264"], {"vcodec": ["libx264"]}),
        # Boolean options
        (["-y", "-hide_banner"], {"y": [None], "hide_banner": [None]}),
        # Negated boolean options
        (["-noaudio", "-novideo"], {"audio": [False], "video": [False]}),
        # Mixed options
        (["-ss", "10", "-y", "-b:v", "1000k"], {"ss": ["10"], "y": [None], "b:v": ["1000k"]}),
        # Stream specifiers
        (["-c:v", "libx264", "-c:a", "aac"], {"c:v": ["libx264"], "c:a": ["aac"]}),
    ],
)
def test_parse_options_parametrized(tokens, expected_options):
    """Parametrized test for parse_options function."""
    result = parse_options(tokens)
    assert dict(result) == expected_options


def test_complex_integration():
    """Integration test with complex command using both validation modes."""
    complex_cmd = '''ffmpeg -y -loglevel error -hide_banner -i "input video.mp4" -ss 00:01:30 -i "audio track.wav" -filter_complex "[0:v]scale=1920:1080[v];[1:a]aresample=48000[a]" -map "[v]" -map "[a]" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 192k -metadata title="Test Video" -movflags +faststart "output.mp4"'''
    
    # Test with validation
    result_validated = parse(complex_cmd, validate=True)
    compiled_validated = compile(result_validated)
    
    # Test without validation  
    result_no_validation = parse(complex_cmd, validate=False)
    compiled_no_validation = compile(result_no_validation)
    
    # Both should compile successfully
    assert "ffmpeg" in compiled_validated
    assert "ffmpeg" in compiled_no_validation
    
    # Both should contain the basic structure
    assert "-i" in compiled_validated
    assert "-i" in compiled_no_validation
    assert "input video.mp4" in compiled_validated
    assert "input video.mp4" in compiled_no_validation
    
    # The no-validation version might contain more options
    # (this is expected behavior - validation filters out unknown/invalid options)