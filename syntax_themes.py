# syntax_themes.py
from pygments.style import Style
from pygments.token import (
    Token,
    Comment,
    Keyword,
    Name,
    Literal,
    String,
    Number,
    Operator,
    Generic,
    Text,
)

# ----------------------------
# 1) Dracula-like (dark, slightly purple)
# ----------------------------
class DraculaLikeStyle(Style):
    background_color = "#282a36"
    default_style = "#f8f8f2"
    styles = {
        Comment: "italic #6272a4",
        Keyword: "bold #ff79c6",
        Keyword.Declaration: "bold #ff79c6",
        Name: "#f8f8f2",
        Name.Function: "#50fa7b",
        Name.Builtin: "#8be9fd",
        Name.Decorator: "#ff79c6",
        Name.Class: "#8be9fd",
        String: "#f1fa8c",
        Number: "#bd93f9",
        Operator: "#f8f8f2",
        Literal: "#ffb86c",
        Generic: "#9aa7c7",
        Token.LineNumber: "#5c6370",
        Token.LineNumber.Current: "bold #ff79c6",
        Text: "#f8f8f2",
    }

# ----------------------------
# 2) Monokai-like
# ----------------------------
class MonokaiLikeStyle(Style):
    background_color = "#272822"
    default_style = "#f8f8f2"
    styles = {
        Comment: "italic #75715e",
        Keyword: "bold #f92672",
        Keyword.Declaration: "bold #f92672",
        Name: "#f8f8f2",
        Name.Function: "#a6e22e",
        Name.Builtin: "#66d9ef",
        Name.Decorator: "#fd971f",
        Name.Class: "#66d9ef",
        String: "#e6db74",
        Number: "#ae81ff",
        Operator: "#f8f8f2",
        Literal: "#fd971f",
        Generic: "#b4b7b4",
        Token.LineNumber: "#66615a",
        Token.LineNumber.Current: "bold #f92672",
        Text: "#f8f8f2",
    }

# ----------------------------
# 3) One Dark-like
# ----------------------------
class OneDarkStyle(Style):
    background_color = "#282c34"
    default_style = "#abb2bf"
    styles = {
        Comment: "italic #5c6370",
        Keyword: "bold #c678dd",
        Keyword.Declaration: "bold #c678dd",
        Name: "#abb2bf",
        Name.Function: "#61afef",
        Name.Builtin: "#e5c07b",
        Name.Decorator: "#c678dd",
        Name.Class: "#e5c07b",
        String: "#98c379",
        Number: "#56b6c2",
        Operator: "#abb2bf",
        Literal: "#d19a66",
        Generic: "#9aa7b0",
        Token.LineNumber: "#4b5263",
        Token.LineNumber.Current: "bold #c678dd",
        Text: "#abb2bf",
    }

# ----------------------------
# 4) Solarized Light-like
# ----------------------------
class SolarizedLightStyle(Style):
    background_color = "#fdf6e3"
    default_style = "#657b83"
    styles = {
        Comment: "italic #93a1a1",
        Keyword: "bold #859900",
        Keyword.Declaration: "bold #859900",
        Name: "#657b83",
        Name.Function: "#268bd2",
        Name.Builtin: "#b58900",
        Name.Decorator: "#268bd2",
        Name.Class: "#b58900",
        String: "#2aa198",
        Number: "#d33682",
        Operator: "#657b83",
        Literal: "#cb4b16",
        Generic: "#586e75",
        Token.LineNumber: "#586e75",
        Token.LineNumber.Current: "bold #268bd2",
        Text: "#657b83",
    }

# ----------------------------
# 5) Solarized Dark-like
# ----------------------------
class SolarizedDarkStyle(Style):
    background_color = "#002b36"
    default_style = "#839496"
    styles = {
        Comment: "italic #586e75",
        Keyword: "bold #b58900",
        Keyword.Declaration: "bold #b58900",
        Name: "#839496",
        Name.Function: "#268bd2",
        Name.Builtin: "#2aa198",
        Name.Decorator: "#b58900",
        Name.Class: "#2aa198",
        String: "#859900",
        Number: "#d33682",
        Operator: "#839496",
        Literal: "#cb4b16",
        Generic: "#93a1a1",
        Token.LineNumber: "#073642",
        Token.LineNumber.Current: "bold #b58900",
        Text: "#839496",
    }

# ----------------------------
# 6) Pastel Light
# ----------------------------
class PastelLightStyle(Style):
    background_color = "#fbfbff"
    default_style = "#2e2e2e"
    styles = {
        Comment: "italic #9aa0a6",
        Keyword: "bold #5b7de0",
        Keyword.Declaration: "bold #5b7de0",
        Name: "#2e2e2e",
        Name.Function: "#8a63c9",
        Name.Builtin: "#b66d2f",
        Name.Decorator: "#8a63c9",
        Name.Class: "#b66d2f",
        String: "#2f9d71",
        Number: "#3a6f78",
        Operator: "#2e2e2e",
        Literal: "#b07a3b",
        Generic: "#7b7f8a",
        Token.LineNumber: "#a0a6ad",
        Token.LineNumber.Current: "bold #5b7de0",
        Text: "#2e2e2e",
    }

# ----------------------------
# 7) Muted Dim (minimal dark)
# ----------------------------
class MutedDimStyle(Style):
    background_color = "#1e1e1e"
    default_style = "#b0b0b0"
    styles = {
        Comment: "italic #6c6c6c",
        Keyword: "bold #8b9ab3",
        Keyword.Declaration: "bold #8b9ab3",
        Name: "#b0b0b0",
        Name.Function: "#a89ecf",
        Name.Builtin: "#9d8074",
        Name.Decorator: "#a89ecf",
        Name.Class: "#9d8074",
        String: "#7fae7f",
        Number: "#8f9e9f",
        Operator: "#5e5e5e",
        Literal: "#9e8f6f",
        Generic: "#9aa7b0",
        Token.LineNumber: "#5a5a5a",
        Token.LineNumber.Current: "bold #a89ecf",
        Text: "#b0b0b0",
    }

# ----------------------------
# 8) High Contrast (black bg, bright tokens)
# ----------------------------
class HighContrastStyle(Style):
    background_color = "#000000"
    default_style = "#ffffff"
    styles = {
        Comment: "italic #888888",
        Keyword: "bold #00ffff",
        Keyword.Declaration: "bold #00ffff",
        Name: "#ffffff",
        Name.Function: "#ff00ff",
        Name.Builtin: "#ffff00",
        Name.Decorator: "#00ffff",
        Name.Class: "#ffff00",
        String: "#00ff00",
        Number: "#00ffff",
        Operator: "#ffffff",
        Literal: "#ff9900",
        Generic: "#ffffff",
        Token.LineNumber: "#777777",
        Token.LineNumber.Current: "bold #00ffff",
        Text: "#ffffff",
    }

# ----------------------------
# 9) Gruvbox Dark
# ----------------------------
class GruvboxDarkStyle(Style):
    background_color = "#1b1d1a"
    default_style = "#ebdbb2"
    styles = {
        Comment: "italic #928374",
        Keyword: "bold #fb4934",
        Keyword.Declaration: "bold #fb4934",
        Name: "#ebdbb2",
        Name.Function: "#b8bb26",
        Name.Builtin: "#8ec07c",
        Name.Decorator: "#fb4934",
        Name.Class: "#8ec07c",
        String: "#b8bb26",
        Number: "#d3869b",
        Operator: "#ebdbb2",
        Literal: "#fabd2f",
        Generic: "#a89984",
        Token.LineNumber: "#7c6f64",
        Token.LineNumber.Current: "bold #fb4934",
        Text: "#ebdbb2",
    }

# ----------------------------
# 10) Gruvbox Light
# ----------------------------
class GruvboxLightStyle(Style):
    background_color = "#fbf1c7"
    default_style = "#3c3836"
    styles = {
        Comment: "italic #928374",
        Keyword: "bold #9d0006",
        Keyword.Declaration: "bold #9d0006",
        Name: "#3c3836",
        Name.Function: "#79740e",
        Name.Builtin: "#7c6f64",
        Name.Decorator: "#9d0006",
        Name.Class: "#7c6f64",
        String: "#79740e",
        Number: "#b57614",
        Operator: "#3c3836",
        Literal: "#b57614",
        Generic: "#7c6f64",
        Token.LineNumber: "#8f6f52",
        Token.LineNumber.Current: "bold #9d0006",
        Text: "#3c3836",
    }

# ----------------------------
# 11) Nord (cool blues)
# ----------------------------
class NordStyle(Style):
    background_color = "#2e3440"
    default_style = "#d8dee9"
    styles = {
        Comment: "italic #616e88",
        Keyword: "bold #81a1c1",
        Keyword.Declaration: "bold #81a1c1",
        Name: "#d8dee9",
        Name.Function: "#88c0d0",
        Name.Builtin: "#8fbcbb",
        Name.Decorator: "#81a1c1",
        Name.Class: "#8fbcbb",
        String: "#a3be8c",
        Number: "#b48ead",
        Operator: "#d8dee9",
        Literal: "#ebcb8b",
        Generic: "#94a3b8",
        Token.LineNumber: "#3b4252",
        Token.LineNumber.Current: "bold #81a1c1",
        Text: "#d8dee9",
    }

# ----------------------------
# 12) Ayu Dark
# ----------------------------
class AyuDarkStyle(Style):
    background_color = "#0f1419"
    default_style = "#d5d6db"
    styles = {
        Comment: "italic #6f747a",
        Keyword: "bold #ffb454",
        Keyword.Declaration: "bold #ffb454",
        Name: "#d5d6db",
        Name.Function: "#7ccfff",
        Name.Builtin: "#ffd580",
        Name.Decorator: "#ffb454",
        Name.Class: "#ffd580",
        String: "#b8f0a8",
        Number: "#ffb454",
        Operator: "#d5d6db",
        Literal: "#ffb454",
        Generic: "#b7bec6",
        Token.LineNumber: "#3a3f45",
        Token.LineNumber.Current: "bold #ffb454",
        Text: "#d5d6db",
    }

# ----------------------------
# 13) Ayu Light
# ----------------------------
class AyuLightStyle(Style):
    background_color = "#f7f7f9"
    default_style = "#3b3b3b"
    styles = {
        Comment: "italic #9aa0a6",
        Keyword: "bold #f76d47",
        Keyword.Declaration: "bold #f76d47",
        Name: "#3b3b3b",
        Name.Function: "#4a90e2",
        Name.Builtin: "#ffb454",
        Name.Decorator: "#f76d47",
        Name.Class: "#ffb454",
        String: "#18a058",
        Number: "#b85c7d",
        Operator: "#3b3b3b",
        Literal: "#c18c3e",
        Generic: "#6f6f6f",
        Token.LineNumber: "#9b9b9b",
        Token.LineNumber.Current: "bold #f76d47",
        Text: "#3b3b3b",
    }

# ----------------------------
# 14) Tomorrow Night
# ----------------------------
class TomorrowNightStyle(Style):
    background_color = "#002b36"
    default_style = "#c5c8c6"
    styles = {
        Comment: "italic #969896",
        Keyword: "bold #f5871f",
        Keyword.Declaration: "bold #f5871f",
        Name: "#c5c8c6",
        Name.Function: "#b294bb",
        Name.Builtin: "#b5bd68",
        Name.Decorator: "#f5871f",
        Name.Class: "#b5bd68",
        String: "#b5bd68",
        Number: "#de935f",
        Operator: "#c5c8c6",
        Literal: "#cc6666",
        Generic: "#9fb1c1",
        Token.LineNumber: "#3a3f44",
        Token.LineNumber.Current: "bold #f5871f",
        Text: "#c5c8c6",
    }

# ----------------------------
# 15) Zenburn (soft low-contrast)
# ----------------------------
class ZenburnStyle(Style):
    background_color = "#3f3f3f"
    default_style = "#dcdccc"
    styles = {
        Comment: "italic #7f9f7f",
        Keyword: "bold #f0dfaf",
        Keyword.Declaration: "bold #f0dfaf",
        Name: "#dcdccc",
        Name.Function: "#dfaf8f",
        Name.Builtin: "#dfdfbf",
        Name.Decorator: "#f0dfaf",
        Name.Class: "#dfdfbf",
        String: "#8fb28f",
        Number: "#dfaf8f",
        Operator: "#dcdccc",
        Literal: "#e0cf9f",
        Generic: "#bcbdb6",
        Token.LineNumber: "#7a7a7a",
        Token.LineNumber.Current: "bold #f0dfaf",
        Text: "#dcdccc",
    }

# ----------------------------
# 16) Material Dark (saturated, modern)
# ----------------------------
class MaterialDarkStyle(Style):
    background_color = "#263238"
    default_style = "#eceff1"
    styles = {
        Comment: "italic #90a4ae",
        Keyword: "bold #ff4081",
        Keyword.Declaration: "bold #ff4081",
        Name: "#eceff1",
        Name.Function: "#82b1ff",
        Name.Builtin: "#c5e1a5",
        Name.Decorator: "#ff4081",
        Name.Class: "#c5e1a5",
        String: "#c3e88d",
        Number: "#ffab91",
        Operator: "#eceff1",
        Literal: "#ffd180",
        Generic: "#b0bec5",
        Token.LineNumber: "#4a5964",
        Token.LineNumber.Current: "bold #ff4081",
        Text: "#eceff1",
    }

# ----------------------------
# 17) Oceanic Next
# ----------------------------
class OceanicNextStyle(Style):
    background_color = "#1b2b34"
    default_style = "#d8dee9"
    styles = {
        Comment: "italic #65737e",
        Keyword: "bold #c594c5",
        Keyword.Declaration: "bold #c594c5",
        Name: "#d8dee9",
        Name.Function: "#5fb3b3",
        Name.Builtin: "#c0c5ce",
        Name.Decorator: "#c594c5",
        Name.Class: "#c0c5ce",
        String: "#99c794",
        Number: "#f99157",
        Operator: "#d8dee9",
        Literal: "#fac863",
        Generic: "#89b5b5",
        Token.LineNumber: "#2e3b44",
        Token.LineNumber.Current: "bold #c594c5",
        Text: "#d8dee9",
    }

# ----------------------------
# 18) Tokyo Night
# ----------------------------
class TokyoNightStyle(Style):
    background_color = "#1a1b27"
    default_style = "#c0caf5"
    styles = {
        Comment: "italic #565f89",
        Keyword: "bold #ff9e64",
        Keyword.Declaration: "bold #ff9e64",
        Name: "#c0caf5",
        Name.Function: "#7aa2f7",
        Name.Builtin: "#7dcfff",
        Name.Decorator: "#ff9e64",
        Name.Class: "#7dcfff",
        String: "#9ece6a",
        Number: "#d6786e",
        Operator: "#c0caf5",
        Literal: "#e0af68",
        Generic: "#98c379",
        Token.LineNumber: "#2c2f44",
        Token.LineNumber.Current: "bold #7aa2f7",
        Text: "#c0caf5",
    }

# ----------------------------
# 19) Cyberpunk (neon eye-catching)
# ----------------------------
class CyberpunkStyle(Style):
    background_color = "#0b0f19"
    default_style = "#f8f8f2"
    styles = {
        Comment: "italic #6b6b6b",
        Keyword: "bold #ff3d81",
        Keyword.Declaration: "bold #ff3d81",
        Name: "#f8f8f2",
        Name.Function: "#7ef1ff",
        Name.Builtin: "#ffd55a",
        Name.Decorator: "#ff3d81",
        Name.Class: "#ffd55a",
        String: "#7ef17e",
        Number: "#ff7ac6",
        Operator: "#f8f8f2",
        Literal: "#ffb86c",
        Generic: "#9aa7c7",
        Token.LineNumber: "#444444",
        Token.LineNumber.Current: "bold #ff3d81",
        Text: "#f8f8f2",
    }

# ----------------------------
# 20) EyeCandy Pastel Neon (bright, eye-catching)
# ----------------------------
class EyeCandyStyle(Style):
    background_color = "#0f1020"
    default_style = "#f5f7ff"
    styles = {
        Comment: "italic #9aa0a6",
        Keyword: "bold #7ee787",
        Keyword.Declaration: "bold #7ee787",
        Name: "#f5f7ff",
        Name.Function: "#ff9ed8",
        Name.Builtin: "#ffd08a",
        Name.Decorator: "#7ee787",
        Name.Class: "#ffd08a",
        String: "#7ef1c7",
        Number: "#b39cff",
        Operator: "#f5f7ff",
        Literal: "#ffcf7e",
        Generic: "#9fb1c1",
        Token.LineNumber: "#2b2b44",
        Token.LineNumber.Current: "bold #7ee787",
        Text: "#f5f7ff",
    }

# ----------------------------
# THEME MAP
# ----------------------------
THEME_MAP = {
    "dracula": (DraculaLikeStyle, "#282a36"),
    "monokai": (MonokaiLikeStyle, "#272822"),
    "one_dark": (OneDarkStyle, "#282c34"),
    "solarized_light": (SolarizedLightStyle, "#fdf6e3"),
    "solarized_dark": (SolarizedDarkStyle, "#002b36"),
    "pastel_light": (PastelLightStyle, "#fbfbff"),
    "muted_dim": (MutedDimStyle, "#1e1e1e"),
    "high_contrast": (HighContrastStyle, "#000000"),
    "gruvbox_dark": (GruvboxDarkStyle, "#1b1d1a"),
    "gruvbox_light": (GruvboxLightStyle, "#fbf1c7"),
    "nord": (NordStyle, "#2e3440"),
    "ayu_dark": (AyuDarkStyle, "#0f1419"),
    "ayu_light": (AyuLightStyle, "#f7f7f9"),
    "tomorrow_night": (TomorrowNightStyle, "#002b36"),
    "zenburn": (ZenburnStyle, "#3f3f3f"),
    "material_dark": (MaterialDarkStyle, "#263238"),
    "oceanic_next": (OceanicNextStyle, "#1b2b34"),
    "tokyo_night": (TokyoNightStyle, "#1a1b27"),
    "cyberpunk": (CyberpunkStyle, "#0b0f19"),
    "eyecandy": (EyeCandyStyle, "#0f1020"),
}


def get_syntax_theme(name: str):
    """
    Return (PygmentsStyleClass, background_hex) for the given short name.
    Defaults to 'muted_dim' if name not found.

    Valid keys: dracula, monokai, one_dark, solarized_light, solarized_dark,
                pastel_light, muted_dim, high_contrast, gruvbox_dark,
                gruvbox_light, nord, ayu_dark, ayu_light, tomorrow_night,
                zenburn, material_dark, oceanic_next, tokyo_night,
                cyberpunk, eyecandy
    """
    return THEME_MAP.get(name, THEME_MAP["muted_dim"])