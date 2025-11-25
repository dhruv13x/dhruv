# tests/utils/test_banner.py
import unittest.mock as mock
from dhruv.utils.banner import lerp, blend, print_logo
import os

def test_lerp():
    """Test the linear interpolation function"""
    assert lerp(0, 10, 0.5) == 5
    assert lerp(10, 20, 0) == 10
    assert lerp(10, 20, 1) == 20

def test_blend():
    """Test the color blending function"""
    c1 = (0, 0, 0)
    c2 = (255, 255, 255)
    assert blend(c1, c2, 0) == "#000000"
    assert blend(c1, c2, 1) == "#ffffff"

@mock.patch('rich.console.Console')
def test_print_logo(MockConsole):
    """Test that the print_logo function calls console.print"""
    mock_console_instance = MockConsole.return_value
    print_logo()
    assert mock_console_instance.print.call_count > 1

@mock.patch('rich.console.Console')
@mock.patch.dict(os.environ, {"CREATE_DUMP_PALETTE": "1"})
def test_print_logo_with_valid_palette_env(MockConsole):
    """Test print_logo with a valid palette index from environment variable."""
    mock_console_instance = MockConsole.return_value
    print_logo()
    assert mock_console_instance.print.call_count > 1

@mock.patch('rich.console.Console')
@mock.patch.dict(os.environ, {"CREATE_DUMP_PALETTE": "invalid"})
def test_print_logo_with_invalid_palette_env(MockConsole):
    """Test print_logo with an invalid palette index from environment variable."""
    mock_console_instance = MockConsole.return_value
    print_logo()
    assert mock_console_instance.print.call_count > 1
