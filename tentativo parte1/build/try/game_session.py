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
            height=767,
            width=1253,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.current_wager = 50
        self.game_running = False
        self.mode = "dice"  # "dice" or "hack"
        self.selected_node = "NODE-ALPHA"

        self.buttons_list = []
        self.texts_list = []
        self.dynamic_items = []

    def create_stuff(self):
        self.canvas.delete("all")
        self.buttons_list.clear()
        self.texts_list.clear()
        self.dynamic_items.clear()

        # Outer Neon Border
        self.canvas.create_rectangle(
            40, 40, 1213, 727,
            outline=CYBER_ACCENT, width=2
        )

        # Header Title
        title_text = "LAS PURGAS // NEURAL CYBER-DICE" if self.mode == "dice" else "LAS PURGAS // NEURAL TERMINAL BREACH"
        self.title_id = self.canvas.create_text(
            626, 75,
            text=title_text,
            fill=NEON_YELLOW,
            font=(FONT_MONO, 26, "bold"),
            anchor="center"
        )
        self.texts_list.append(self.title_id)

        subtitle_text = "VIRTUAL PROBABILITY ENGINE" if self.mode == "dice" else "CORP MAINFRAME INTRUSION SANDBOX"
        sub = self.canvas.create_text(
            626, 108,
            text=f"{subtitle_text} // NO REAL CURRENCY",
            fill=CYBER_ACCENT,
            font=(FONT_MONO, 11),
            anchor="center"
        )
        self.texts_list.append(sub)

        # Mode Switch Button (Top Right)
        mode_btn_text = "MODE: [TERMINAL HACK]" if self.mode == "dice" else "MODE: [CYBER-DICE]"
        self.mode_toggle_btn = Button(
            self,
            text=mode_btn_text,
            font=(FONT_DISPLAY, 10, "bold"),
            bg=CYBER_PURPLE,
            fg="#00F0FF",
            activebackground=CYBER_ACCENT,
            activeforeground="#FFFFFF",
            relief="ridge",
            bd=1,
            cursor="hand2",
            command=self.toggle_mode
        )
        self.mode_toggle_btn.place(x=970, y=60, width=210, height=36)
        self.buttons_list.append(self.mode_toggle_btn)

        # Player Info Panel
        self.balance_text = self.canvas.create_text(
            100, 165,
            text=f"BALANCE: {self.controller.get_credits()}",
            fill=NEON_YELLOW,
            font=(FONT_DISPLAY, 15),
            anchor="w"
        )
        self.texts_list.append(self.balance_text)

        self.wager_text = self.canvas.create_text(
            100, 200,
            text=f"ACTIVE WAGER: {self.current_wager} CR",
            fill="#FFFFFF",
            font=(FONT_DISPLAY, 13),
            anchor="w"
        )
        self.texts_list.append(self.wager_text)

        # Wager Selection Buttons
        wagers = [25, 50, 100, 250, 500]
        for i, val in enumerate(wagers):
            btn = Button(
                self,
                text=f"{val} CR",
                font=(FONT_DISPLAY, 10),
                bg=CYBER_PURPLE,
                fg=NEON_YELLOW,
                activebackground=CYBER_ACCENT,
                activeforeground="#FFFFFF",
                bd=1,
                relief="flat",
                command=lambda v=val: self.set_wager(v)
            )
            btn.place(x=100 + i * 80, y=225, width=70, height=32)
            self.buttons_list.append(btn)

        # Navigation Buttons (Bottom)
        back_btn = Button(
            self,
            text="<< EXIT TO HUB",
            font=(FONT_DISPLAY, 11),
            bg=CYBER_PURPLE,
            fg=NEON_YELLOW,
            activebackground=CYBER_ACCENT,
            bd=1,
            relief="flat",
            cursor="hand2",
            command=lambda: self.controller.show_page("main_channel")
        )
