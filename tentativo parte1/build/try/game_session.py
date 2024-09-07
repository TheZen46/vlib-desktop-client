"""
VLib (Las Purgas) Cyberpunk Mini-Game Session
Dual-mode interactive casino arcade:
1. Neural Cyber-Dice (Dice physics & probability payout)
2. Neural Terminal Hack (Corporate mainframe breach simulation)
"""

from pathlib import Path
from tkinter import Frame, Canvas, Button, messagebox
import random

try:
    from theme import (
        BG_PRIMARY as DARK_SLATE,
        ACCENT_NEON as NEON_YELLOW,
        BG_SECONDARY as CYBER_PURPLE,
        ACCENT_PURPLE as CYBER_ACCENT,
        play_cyber_sound
    )
except ImportError:
    DARK_SLATE = "#272932"
    NEON_YELLOW = "#FDF500"
    CYBER_PURPLE = "#200628"
    CYBER_ACCENT = "#9370DB"
    def play_cyber_sound(snd, enabled=True): pass

FONT_DISPLAY = "RussoOne Regular"
FONT_MONO = "ShareTechMono Regular"


class GameSession(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        super().__init__(parent, bg=DARK_SLATE)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH

        self.canvas = Canvas(
            self,
            bg=DARK_SLATE,
