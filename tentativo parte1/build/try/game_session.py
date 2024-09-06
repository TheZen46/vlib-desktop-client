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
