# tests/utils/test_ascii_banners.py
import unittest.mock as mock
from dhruv.utils.ascii_banners import banner, main_callback

@mock.patch('dhruv.utils.ascii_banners.console')
def test_banner(mock_console):
    """Test that the banner function calls console.print"""
    banner()
    mock_console.print.assert_called_once()

@mock.patch('dhruv.utils.ascii_banners.console')
@mock.patch('dhruv.utils.ascii_banners.banner')
def test_main_callback_no_subcommand(mock_banner, mock_console):
    """Test the main_callback function when no subcommand is invoked"""
    ctx = mock.Mock()
    ctx.invoked_subcommand = None
    main_callback(ctx)
    mock_banner.assert_called_once()
    assert mock_console.print.call_count == 1

@mock.patch('dhruv.utils.ascii_banners.console')
@mock.patch('dhruv.utils.ascii_banners.banner')
def test_main_callback_with_subcommand(mock_banner, mock_console):
    """Test the main_callback function when a subcommand is invoked"""
    ctx = mock.Mock()
    ctx.invoked_subcommand = "some_command"
    main_callback(ctx)
    mock_banner.assert_called_once()
    mock_console.print.assert_not_called()
