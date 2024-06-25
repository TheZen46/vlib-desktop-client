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
        self.rectangle_list = []
        self.texts_list = []

    def create_stuff(self):
        # Sidebar Navigation Buttons
        self.rules_image = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.rules = Button(
            self,
            image=self.rules_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("rules"),
            relief="flat"
        )
        self.rules.place(x=124.0, y=547.0, width=61.07, height=21.08)
        self.buttons_list.append(self.rules)

        self.contact_image = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.contact = Button(
            self,
            image=self.contact_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("contact_us"),
            relief="flat"
        )
        self.contact.place(x=1133.0, y=741.0, width=109.07, height=18.27)
        self.buttons_list.append(self.contact)

        self.how_image = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.how = Button(
            self,
            image=self.how_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("howdoesitwork"),
            relief="flat"
        )
        self.how.place(x=20.0, y=741.0, width=232.0, height=18.27)
        self.buttons_list.append(self.how)

        self.options_image = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.options = Button(
            self,
            image=self.options_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("options"),
            relief="flat"
        )
        self.options.place(x=114.0, y=441.0, width=82.0, height=22.13)
        self.buttons_list.append(self.options)

        self.features_image = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.features = Button(
            self,
            image=self.features_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("new_features"),
            relief="flat"
        )
        self.features.place(x=84.0, y=339.0, width=142.1, height=19.38)
        self.buttons_list.append(self.features)

        self.channel_image = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.channel = Button(
            self,
            image=self.channel_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("main_channel"),
            relief="flat"
        )
