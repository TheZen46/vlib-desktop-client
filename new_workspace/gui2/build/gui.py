import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, font

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Page Navigation Example")

        # Create a container to hold the different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Create a dictionary to store the different pages
        self.pages = {}

        # Create and add the pages to the dictionary
        page1 = Page1(self.container, self)
        page2 = Page2(self.container, self)
        page3 = Page3(self.container, self)
        page4 = Page4(self.container, self)
        page5 = Page5(self.container, self)
        page6 = Page6(self.container, self)
        page7 = Page7(self.container, self)
        page8 = Page8(self.container, self)
        self.pages["Page 1"] = page1
        self.pages["Page 2"] = page2
        self.pages["Page 3"] = page3
        self.pages["Page 4"] = page4
        self.pages["Page 5"] = page5
        self.pages["Page 6"] = page6
        self.pages["Page 7"] = page7
        self.pages["Page 8"] = page8

        # Show the initial page
        self.show_page("Page 1")

    def show_page(self, page_name):
        # Hide the current page, if any
        current_page = self.pages.get("current")
        if current_page is not None:
            current_page.pack_forget()

        # Show the new page
        new_page = self.pages[page_name]
        new_page.pack(fill="both", expand=True)
        self.pages["current"] = new_page

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 1
        label = tk.Label(self, text="Page 1")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page("Page 2"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_page("Page 3"))
        button2.pack()

        button3 = tk.Button(self, text="Show Message", command=self.show_message)
        button3.pack()

    def show_message(self):
        messagebox.showinfo("Message", "This is page 1!")

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 2
        label = tk.Label(self, text="Page 2")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_page("Page 4"))
        button2.pack()

        button3 = tk.Button(self, text="Open File", command=self.open_file_dialog)
        button3.pack()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Selected File", f"You selected: {file_path}")

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 3
        label = tk.Label(self, text="Page 3")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        button2 = tk.Button(self, text="Show Message", command=self.show_message)
        button2.pack()

        button3 = tk.Button(self, text="Choose Color", command=self.choose_color)
        button3.pack()

    def show_message(self):
        messagebox.showinfo("Message", "This is page 3!")

    def choose_color(self):
        color = colorchooser.askcolor()
        if color:
            messagebox.showinfo("Selected Color", f"You selected: {color[1]}")

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 4
        label = tk.Label(self, text="Page 4")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page("Page 2"))
        button1.pack()

        scale = tk.Scale(self, from_=0, to=10, orient="horizontal")
        scale.pack()

        button2 = tk.Button(self, text="Get Scale Value", command=lambda: self.get_scale_value(scale))
        button2.pack()

    def get_scale_value(self, scale):
        value = scale.get()
        messagebox.showinfo("Scale Value", f"The scale value is: {value}")

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 5
        label = tk.Label(self, text="Page 5")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        button2 = tk.Button(self, text="Change Font", command=self.change_font)
        button2.pack()

    def change_font(self):
        font_info = font.Font(family="Helvetica", size=12, weight="bold")
        messagebox.showinfo("Font Info", f"Selected Font: {font_info.actual()}")

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 6
        label = tk.Label(self, text="Page 6")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        canvas = tk.Canvas(self, width=200, height=200)
        canvas.pack()

        canvas.create_oval(50, 50, 150, 150, fill="blue")
        canvas.create_line(50, 150, 150, 50, fill="red", width=2)

class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 7
        label = tk.Label(self, text="Page 7")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        label = tk.Label(self, text="Please select an option:")
        label.pack()

        var = tk.StringVar()
        var.set("Option 1")

        option_menu = tk.OptionMenu(self, var, "Option 1", "Option 2", "Option 3")
        option_menu.pack()

        button2 = tk.Button(self, text="Get Selected Option", command=lambda: self.get_selected_option(var))
        button2.pack()

    def get_selected_option(self, var):
        selected_option = var.get()
        messagebox.showinfo("Selected Option", f"The selected option is: {selected_option}")

class Page8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create widgets for Page 8
        label = tk.Label(self, text="Page 8")
        label.pack(pady=10)

        button1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack()

        listbox = tk.Listbox(self)
        listbox.pack()

        for i in range(1, 21):
            listbox.insert(tk.END, f"Item {i}")

        button2 = tk.Button(self, text="Get Selected Item", command=lambda: self.get_selected_item(listbox))
        button2.pack()

    def get_selected_item(self, listbox):
        selected_item = listbox.get(tk.ACTIVE)
        messagebox.showinfo("Selected Item", f"The selected item is: {selected_item}")

# Create an instance of the application
app = Application()

# Start the main event loop
app.mainloop()
