import tkinter as tk
import time

class CustomDropdown(tk.Frame):
    def __init__(self, parent, options, callback=None):
        super().__init__(parent)
        self.options = options
        self.callback = callback

        self.var = tk.StringVar(value=options[0])
        self.option_menu = tk.OptionMenu(self, self.var, *self.options, command=self.handle_selection)
        self.option_menu.config(
            bg='#272932',
            activebackground='#272932',
            borderwidth=0,
            foreground='#FDF500',
            activeforeground='#FDF590',
            highlightthickness= 0
        )
        self.option_menu["menu"].config(
            background='#272932',
            border=0,
            borderwidth=0,
            foreground='#FDF500'
        )
        self.option_menu.pack()

    def handle_selection(self, option):
        # Implement this method to handle the selected option
        if self.callback is not None:
            self.callback(option)

# Example usage:
def option_selected(option):
    print(f"Selected option: {option}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Dropdown")

    options = ["Eng", 'None', '...']

    dropdown = CustomDropdown(root, options, callback=option_selected)
    dropdown.pack()
    

    root.mainloop()