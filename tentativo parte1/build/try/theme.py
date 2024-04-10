"""
VLib Design System, Theme Tokens & Audio Synthesis
Centralized cyberpunk color palette, typography, geometry definitions, and sound effects.
"""

from typing import Tuple
import sys
import threading

# Color Palette (Cyberpunk Dark Aesthetics)
BG_PRIMARY = "#272932"       # Dark slate canvas baseline
BG_SECONDARY = "#200628"     # Deep neon violet container
ACCENT_NEON = "#FDF500"      # Cyberpunk high-contrast yellow
ACCENT_PURPLE = "#9370DB"    # Medium purple divider lines
ACCENT_CYAN = "#00F0FF"      # Secondary cyberpunk highlight
TEXT_LIGHT = "#FFFFFF"       # White foreground headers
TEXT_MUTED = "#8B949E"       # Muted subtitle text
SUCCESS_GREEN = "#00FF66"    # Active status green
DANGER_RED = "#FF003C"       # Error / warning red

# Window Dimensions & Grid
WINDOW_WIDTH = 1253
WINDOW_HEIGHT = 767
CANVAS_RELIEF = "ridge"
CANVAS_BD = 0

# Typography
FONT_NAME_BRAND = "RussoOne Regular"
FONT_NAME_UI = "Helvetica"


def font_brand(size: int = 20) -> Tuple[str, int]:
    return (FONT_NAME_BRAND, -abs(size))


def font_ui(size: int = 11, bold: bool = False) -> Tuple[str, int, str]:
    style = "bold" if bold else "normal"
    return (FONT_NAME_UI, abs(size), style)


def play_cyber_sound(sound_type: str = "click", enabled: bool = True):
    """
    Non-blocking synthesized audio effect for Cyberpunk UI interactions.
    Gracefully executes in a background thread without blocking Tkinter UI.
    """
    if not enabled or sys.platform != "win32":
        return

    def _play():
        try:
            import winsound
            if sound_type == "roll":
                for f in (440, 580, 720, 880):
                    winsound.Beep(f, 35)
            elif sound_type == "win":
                for f in (523, 659, 784, 1046):
                    winsound.Beep(f, 60)
