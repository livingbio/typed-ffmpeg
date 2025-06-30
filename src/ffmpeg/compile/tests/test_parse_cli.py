"""Tests for the parse_cli function that parses CLI without option validation."""

from unittest.mock import patch

from ..compile_cli import compile, parse, parse_cli, parse_with_validation


def test_parse_cli_basic():
    """Test that parse_cli can parse basic commands."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    result = parse_cli(command)
    
    # Should return a Stream object
    assert result is not None
    
    # Should be compilable back to a command
    compiled = compile(result)
    assert isinstance(compiled, str)
    assert "ffmpeg" in compiled
    assert "input.mp4" in compiled
    assert "output.mp4" in compiled


def test_parse_cli_complex():
    """Test that parse_cli can parse complex commands with filters."""
    command = "ffmpeg -y -i input.mp4 -filter_complex '[0:v]scale=1280:720[v]' -map '[v]' output.mp4"
    result = parse_cli(command)
    
    # Should return a Stream object
    assert result is not None
    
    # Should be compilable back to a command
    compiled = compile(result)
    assert isinstance(compiled, str)


def test_parse_cli_no_dict_loading():
    """Test that parse_cli does not load option dictionaries."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    with patch('ffmpeg.compile.compile_cli.get_options_dict') as mock_options, \
         patch('ffmpeg.compile.compile_cli.get_filter_dict') as mock_filters:
        
        result = parse_cli(command)
        
        # Verify dictionaries were not loaded
        mock_options.assert_not_called()
        mock_filters.assert_not_called()
        
        # Should still work
        assert result is not None
        compiled = compile(result)
        assert isinstance(compiled, str)


def test_parse_with_validation_false():
    """Test parse_with_validation with validation disabled."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    with patch('ffmpeg.compile.compile_cli.get_options_dict') as mock_options, \
         patch('ffmpeg.compile.compile_cli.get_filter_dict') as mock_filters:
        
        result = parse_with_validation(command, validate_options=False)
        
        # Verify dictionaries were not loaded
        mock_options.assert_not_called()
        mock_filters.assert_not_called()
        
        # Should still work
        assert result is not None


def test_parse_with_validation_true():
    """Test parse_with_validation with validation enabled."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    with patch('ffmpeg.compile.compile_cli.get_options_dict') as mock_options, \
         patch('ffmpeg.compile.compile_cli.get_filter_dict') as mock_filters:
        
        # Configure mocks to return empty dicts to avoid loading issues
        mock_options.return_value = {}
        mock_filters.return_value = {}
        
        result = parse_with_validation(command, validate_options=True)
        
        # Verify dictionaries were loaded
        mock_options.assert_called_once()
        mock_filters.assert_called_once()
        
        # Should still work
        assert result is not None


def test_parse_backwards_compatibility():
    """Test that the original parse function behavior is preserved."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    with patch('ffmpeg.compile.compile_cli.get_options_dict') as mock_options, \
         patch('ffmpeg.compile.compile_cli.get_filter_dict') as mock_filters:
        
        # Configure mocks to return empty dicts
        mock_options.return_value = {}
        mock_filters.return_value = {}
        
        result = parse(command)
        
        # Original parse should still load dictionaries for validation
        mock_options.assert_called_once()
        mock_filters.assert_called_once()
        
        # Should still work
        assert result is not None


def test_parse_cli_vs_parse_result_types():
    """Test that parse_cli and parse return the same types."""
    command = "ffmpeg -y -i input.mp4 output.mp4"
    
    # Mock dictionaries for validation mode
    with patch('ffmpeg.compile.compile_cli.get_options_dict') as mock_options, \
         patch('ffmpeg.compile.compile_cli.get_filter_dict') as mock_filters:
        
        mock_options.return_value = {}
        mock_filters.return_value = {}
        
        result_cli = parse_cli(command)
        result_parse = parse(command)
        
        # Both should return Stream objects of the same type
        assert type(result_cli) == type(result_parse)
        
        # Both should be compilable
        compiled_cli = compile(result_cli)
        compiled_parse = compile(result_parse)
        
        assert isinstance(compiled_cli, str)
        assert isinstance(compiled_parse, str)