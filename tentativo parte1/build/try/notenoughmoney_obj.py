from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, messagebox


class NotEnoughMoney(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH

        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame21"

        self.canvas = Canvas(
            self,
            bg="#272932",
            height=767,
            width=1253,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Static logo
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            120.0,
            111.0,
            image=self.image_image_1
        )

        # Dividing line
        self.canvas.create_rectangle(
            263.5,
            156.5,
            266.0,
            685.0,
            fill="#9370DB",
            outline=""
        )

        self.buttons_list = []
        self.images_list = []
