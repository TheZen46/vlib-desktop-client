import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Main Page")

        options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]
        button_image_path = "2Q.png"  # Replace with the path to your .png image

        self.dropdown = CustomDropdown(self, options, button_image_path)
        self.dropdown.pack(pady=20)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

class CustomDropdown(tk.Frame):
    def __init__(self, master, options, button_image_path):
        super().__init__(master)
        self.master = master
        self.options = options
        self.selected_option = tk.StringVar()

        image = Image.open(button_image_path)
        self.button_image = ImageTk.PhotoImage(image)
        
        self.canvas = tk.Canvas(self, width=image.width, height=image.height, bg="white", highlightthickness=1)
        self.canvas.pack()

        self.button = self.canvas.create_image(0, 0, anchor="nw", image=self.button_image)
        self.text = self.canvas.create_text(image.width + 10, image.height // 2, anchor="w", text="", fill="#fdf500")  # Set text color to yellow
        
        self.canvas.tag_bind(self.button, "<Button-1>", self.toggle_dropdown)
        self.canvas.tag_bind(self.button, "<Enter>", self.change_cursor_to_hand)
        self.canvas.tag_bind(self.button, "<Leave>", self.change_cursor_to_arrow)
        
        self.menu = None
    
    def toggle_dropdown(self, event):
        if self.menu is None:
            self.menu = tk.Menu(self.canvas, tearoff=0)

            x1, y1, x2, y2 = self.canvas.bbox(self.button)
            corner_radius = 10
            # Set the background color to green and text color to yellow
            self.draw_rounded_rectangle(x1, y2, x2, y2 + len(self.options) * 30, corner_radius, fill="green")
            
            for option in self.options:
                self.menu.add_command(label=option, command=lambda opt=option: self.select_option(opt))
            self.menu.post(self.canvas.winfo_rootx(), self.canvas.winfo_rooty() + self.button_image.height())
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
    
    def draw_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.ARC, **kwargs)
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.ARC, **kwargs)
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.ARC, **kwargs)
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.ARC, **kwargs)

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
