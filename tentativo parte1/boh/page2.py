import tkinter as tk

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 2
        label = tk.Label(self, text="Page 2")
        label.pack(pady=10)

        self.button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page1"))
        self.button.pack()
