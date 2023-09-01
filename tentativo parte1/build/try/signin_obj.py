from tkinter import Frame, Canvas
class SignIn(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH
