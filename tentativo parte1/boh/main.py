from pathlib import Path
import tkinter as tk
from page1 import Page1
from page2 import Page2

OUTPUT_PATH = Path(__file__).parent


class Application(tk.Tk):
    def __init__(self, OUTPUT_PATH):
        tk.Tk.__init__(self)
        self.OUTPUT_PATH = OUTPUT_PATH

        self.title("Page Navigation Example")
        self.geometry("1253x767")
        # Create a container to hold the different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Create a dictionary to store the different pages
        self.pages = {}
        
        self.resizable(False, False)

        # Create and add the pages to the dictionary
        page1 = Page1(self.container, self, OUTPUT_PATH= self.OUTPUT_PATH)
        page2 = Page2(self.container, self)
        self.pages["Page1"] = page1
        self.pages["Page2"] = page2

        # Show the initial page
        self.show_page("Page1")


    def show_page(self, page_name):
        # Hide the current page, if any
        current_page = self.pages.get("current")
        if current_page is not None:
            current_page.pack_forget()

        # Show the new page
        new_page = self.pages[page_name]
        new_page.pack(fill="both", expand=True)
        self.pages["current"] = new_page

# Create an instance of the application
app = Application(OUTPUT_PATH= OUTPUT_PATH)

# Start the main event loop
app.mainloop()
