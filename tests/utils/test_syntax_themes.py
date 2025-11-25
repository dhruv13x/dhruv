# tests/utils/test_syntax_themes.py
from dhruv.utils.syntax_themes import (
    get_syntax_theme,
    hsl_to_rgb,
    rgb_to_hex,
    hsl_to_hex,
    relative_luminance,
    contrast_ratio,
    generate_random_theme,
    THEME_MAP,
    OneDarkStyle,
)
from pygments.style import Style

def test_get_syntax_theme_known():
    """Test getting a known theme."""
    style_class, bg_hex = get_syntax_theme("dracula")
    assert issubclass(style_class, Style)
    assert bg_hex == "#282a36"

def test_get_syntax_theme_fallback():
    """Test the fallback to one_dark for an unknown theme."""
    style_class, bg_hex = get_syntax_theme("unknown_theme")
    assert style_class == OneDarkStyle
    assert bg_hex == OneDarkStyle.background_color

def test_get_syntax_theme_case_insensitive():
    """Test that theme lookup is case-insensitive."""
    style_class, bg_hex = get_syntax_theme("DrAcUlA")
    assert issubclass(style_class, Style)
    assert bg_hex == "#282a36"

def test_get_syntax_theme_random():
    """Test getting a random theme."""
    style_class1, bg_hex1 = get_syntax_theme("random")
    style_class2, bg_hex2 = get_syntax_theme("random")
    assert issubclass(style_class1, Style)
    assert issubclass(style_class2, Style)
    assert (style_class1, bg_hex1) != (style_class2, bg_hex2)

def test_get_syntax_theme_random_seeded():
    """Test getting a deterministic random theme with a seed."""
    style_class1, bg_hex1 = get_syntax_theme("random:123")
    style_class2, bg_hex2 = get_syntax_theme("random:123")
    assert issubclass(style_class1, Style)
    assert issubclass(style_class2, Style)
    assert bg_hex1 == bg_hex2

def test_hsl_to_rgb():
    """Test HSL to RGB conversion."""
    assert hsl_to_rgb(0, 1, 0.5) == (255, 0, 0)
    assert hsl_to_rgb(120, 1, 0.5) == (0, 255, 0)

def test_rgb_to_hex():
    """Test RGB to hex conversion."""
    assert rgb_to_hex((255, 0, 0)) == "#ff0000"

def test_hsl_to_hex():
    """Test HSL to hex conversion."""
    assert hsl_to_hex(0, 1, 0.5) == "#ff0000"

def test_relative_luminance():
    """Test relative luminance calculation."""
    assert relative_luminance("#000000") == 0
    assert relative_luminance("#ffffff") == 1

def test_contrast_ratio():
    """Test contrast ratio calculation."""
    assert round(contrast_ratio("#ffffff", "#000000")) == 21

def test_generate_random_theme():
    """Test random theme generation."""
    style_class, bg_hex = generate_random_theme(seed=42)
    assert issubclass(style_class, Style)
    assert isinstance(bg_hex, str)
    assert bg_hex.startswith("#")
