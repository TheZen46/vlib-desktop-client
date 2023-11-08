from tkinter import Tk, Frame
class Application(Tk):
    def __init__(self, OUTPUT_PATH):
        Tk.__init__(self)
        self.title('VLib')
        self.geometry('1253x767')
        self.pages = {}
    def show_page(self, page_name):
        pass
