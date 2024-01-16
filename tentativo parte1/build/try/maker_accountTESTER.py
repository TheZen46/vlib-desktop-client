"""
VLib Cyberpunk Custom Dropdown Component
A themed Tkinter OptionMenu matching the VLib dark slate and neon yellow aesthetic.
"""

import tkinter as tk
from typing import List, Callable, Optional


class CustomDropdown(tk.Frame):
    def __init__(
        self,
        parent: tk.Widget,
        options: List[str],
        default: Optional[str] = None,
        callback: Optional[Callable[[str], None]] = None,
        bg: str = "#272932",
        fg: str = "#FDF500"
    ):
        super().__init__(parent, bg=bg)
        self.options = options
        self.callback = callback
        initial_val = default if default in options else (options[0] if options else "")

        self.var = tk.StringVar(value=initial_val)
        self.option_menu = tk.OptionMenu(self, self.var, *self.options, command=self.handle_selection)
        self.option_menu.config(
            bg=bg,
            activebackground=bg,
            borderwidth=0,
            foreground=fg,
            activeforeground="#FFFFFF",
            highlightthickness=0,
            relief="flat",
            padx=10,
            pady=4
        )
        self.option_menu["menu"].config(
            background=bg,
            border=0,
            borderwidth=0,
            foreground=fg,
            activebackground="#200628",
            activeforeground="#FFFFFF"
        )
        self.option_menu.pack(fill="x", expand=True)

    def handle_selection(self, option: str):
        if self.callback is not None:
            self.callback(option)

    def get(self) -> str:
        return self.var.get()

    def set(self, value: str):
        if value in self.options:
            self.var.set(value)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("VLib Custom Dropdown Test")
    root.configure(bg="#272932")
    root.geometry("300x150")

    def on_change(val):
        print(f"[Dropdown Event] Selected: {val}")

    opts = ["English (EN)", "Italiano (IT)", "Deutsch (DE)", "Español (ES)"]
    dd = CustomDropdown(root, opts, default="English (EN)", callback=on_change)
    dd.pack(pady=40, padx=20)

    root.update()
    root.destroy()
    print("CustomDropdown test passed successfully.")
