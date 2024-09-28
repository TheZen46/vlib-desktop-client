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
        back_btn.place(x=80, y=665, width=160, height=38)
        self.buttons_list.append(back_btn)

        rules_btn = Button(
            self,
            text="PAYOUT RULES",
            font=(FONT_DISPLAY, 11),
            bg=CYBER_PURPLE,
            fg=CYBER_ACCENT,
            activebackground=CYBER_ACCENT,
            activeforeground="#FFFFFF",
            bd=1,
            relief="flat",
            cursor="hand2",
            command=self.show_payout_rules
        )
        rules_btn.place(x=1010, y=665, width=160, height=38)
        self.buttons_list.append(rules_btn)

        # Render specific mode UI
        if self.mode == "dice":
            self._render_dice_mode()
        else:
            self._render_hack_mode()

    def toggle_mode(self):
        if self.game_running:
            return
        self.mode = "hack" if self.mode == "dice" else "dice"
        self.create_stuff()

    def set_wager(self, amount: int):
        self.current_wager = amount
        self.canvas.itemconfig(self.wager_text, text=f"ACTIVE WAGER: {self.current_wager} CR")

    # ==========================================
    # MODE 1: CYBER-DICE
    # ==========================================
    def _render_dice_mode(self):
        self.dice1_rect = self.canvas.create_rectangle(
            460, 310, 580, 430,
            fill=CYBER_PURPLE, outline=NEON_YELLOW, width=2
        )
        self.dice2_rect = self.canvas.create_rectangle(
            670, 310, 790, 430,
            fill=CYBER_PURPLE, outline=NEON_YELLOW, width=2
        )

        self.dice1_text = self.canvas.create_text(
            520, 370,
            text="?",
            fill=NEON_YELLOW,
            font=(FONT_DISPLAY, 40, "bold"),
            anchor="center"
        )
        self.texts_list.append(self.dice1_text)

        self.dice2_text = self.canvas.create_text(
            730, 370,
            text="?",
            fill=NEON_YELLOW,
            font=(FONT_DISPLAY, 40, "bold"),
            anchor="center"
        )
        self.texts_list.append(self.dice2_text)

        self.action_btn = Button(
            self,
            text="ROLL CYBER-DICE",
            font=(FONT_DISPLAY, 15, "bold"),
            bg="#9370DB",
            fg="#FFFFFF",
            activebackground=NEON_YELLOW,
            activeforeground=CYBER_PURPLE,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.roll_dice
        )
        self.action_btn.place(x=485, y=475, width=280, height=48)
        self.buttons_list.append(self.action_btn)

        self.result_text = self.canvas.create_text(
            626, 565,
            text="SELECT WAGER AND ROLL TO BEGIN",
            fill="#FFFFFF",
            font=(FONT_MONO, 13),
            anchor="center"
        )
        self.texts_list.append(self.result_text)

    def roll_dice(self):
        if self.game_running:
            return

        if not self.controller.spend_credits(self.current_wager):
            messagebox.showwarning(
                "Insufficient Balance",
                f"You need at least {self.current_wager} CR to roll!\nHead over to the recharge station."
            )
            self.controller.show_page("notenoughmoney")
            return

        self.game_running = True
        self.action_btn.config(state="disabled")
        play_cyber_sound("roll", enabled=self.controller.is_sound_enabled())
        self.canvas.itemconfig(self.balance_text, text=f"BALANCE: {self.controller.get_credits()}")
        self.canvas.itemconfig(self.result_text, text="ROLLING CYBER-DICE...", fill=CYBER_ACCENT)

        self._roll_animation(step=0)

    def _roll_animation(self, step: int):
        if step < 8:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            self.canvas.itemconfig(self.dice1_text, text=str(d1))
            self.canvas.itemconfig(self.dice2_text, text=str(d2))
            self.after(50, lambda: self._roll_animation(step + 1))
        else:
            self._finalize_roll()

    def _finalize_roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2

        self.canvas.itemconfig(self.dice1_text, text=str(d1))
        self.canvas.itemconfig(self.dice2_text, text=str(d2))

        if d1 == d2:
            won = int(self.current_wager * 3.0)
            self.controller.add_credits(won)
            msg = f"CRITICAL DOUBLE! Rolled ({d1}, {d2}) -> WON {won} CR (3x Payout)!"
            color = NEON_YELLOW
            play_cyber_sound("win", enabled=self.controller.is_sound_enabled())
        elif total in [7, 11]:
            won = int(self.current_wager * 2.0)
            self.controller.add_credits(won)
