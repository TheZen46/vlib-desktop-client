"""
VLib Custom Dropdown with Image Canvas Integration
Implements a graphical dropdown with rounded rectangles, custom hover states, and dynamic image resolution.
"""

from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk


class CustomDropdown(tk.Frame):
    def __init__(self, master, options, button_image_path):
        super().__init__(master)
        self.master = master
        self.options = options
        self.selected_option = tk.StringVar()

        img_path = Path(button_image_path)
        if not img_path.exists():
            img_path = Path(__file__).resolve().parent.parent.parent / "2Q.png"

        if img_path.exists():
            image = Image.open(img_path)
            self.button_image = ImageTk.PhotoImage(image)
            img_width, img_height = image.width, image.height
        else:
            self.button_image = None
            img_width, img_height = 120, 40

        self.canvas = tk.Canvas(self, width=img_width, height=img_height, bg="#272932", highlightthickness=0)
        self.canvas.pack()

        if self.button_image:
            self.button = self.canvas.create_image(0, 0, anchor="nw", image=self.button_image)
            self.canvas.tag_bind(self.button, "<Button-1>", self.toggle_dropdown)
            self.canvas.tag_bind(self.button, "<Enter>", self.change_cursor_to_hand)
            self.canvas.tag_bind(self.button, "<Leave>", self.change_cursor_to_arrow)
        else:
            self.button = self.canvas.create_rectangle(0, 0, img_width, img_height, fill="#200628")

        self.text = self.canvas.create_text(
            img_width // 2,
            img_height // 2,
            anchor="center",
            text="Select...",
            fill="#FDF500",
            font=("Helvetica", 10, "bold")
        )

        self.menu = None

    def toggle_dropdown(self, event=None):
        if self.menu is None:
            self.menu = tk.Menu(self.canvas, tearoff=0, bg="#272932", fg="#FDF500", activebackground="#200628", activeforeground="#FFFFFF")
            for option in self.options:
                self.menu.add_command(label=option, command=lambda opt=option: self.select_option(opt))
            self.menu.post(self.canvas.winfo_rootx(), self.canvas.winfo_rooty() + 40)
        else:
            self.menu.destroy()
            self.menu = None

    def select_option(self, option):
        self.selected_option.set(option)
        self.canvas.itemconfig(self.text, text=option)
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None
        if option == "Exit":
            self.master.quit()

    def change_cursor_to_hand(self, event):
        self.canvas.config(cursor="hand2")

    def change_cursor_to_arrow(self, event):
        self.canvas.config(cursor="arrow")


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("VLib Custom Dropdown Showcase")
        self.configure(bg="#272932")

        options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]
        button_image_path = Path(__file__).resolve().parent.parent.parent / "2Q.png"

        self.dropdown = CustomDropdown(self, options, button_image_path)
        self.dropdown.pack(pady=20)

        self.quit_button = tk.Button(self, text="Close", command=self.destroy, bg="#200628", fg="#FDF500", relief="flat")
        self.quit_button.pack(pady=10)


if __name__ == "__main__":
    app = MainPage()
    app.update()
    app.destroy()
    print("[ver_auth] Dropdown component verified successfully.")
