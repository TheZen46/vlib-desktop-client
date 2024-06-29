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
        self.channel.place(x=84.0, y=234.0, width=142.0, height=22.0)
        self.buttons_list.append(self.channel)

        # Action Buttons
        self.recharge_image = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.recharge_button = Button(
            self,
            image=self.recharge_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=self.on_recharge_clicked,
            relief="flat"
        )
        self.recharge_button.place(x=836.0, y=252.0, width=250.0, height=54.0)
        self.buttons_list.append(self.recharge_button)

        self.back_image = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.back_button = Button(
            self,
            image=self.back_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page('getVIP'),
            relief="flat"
        )
        self.back_button.place(x=896.0, y=476.0, width=135.0, height=33.39)
        self.buttons_list.append(self.back_button)

        # Decorative Images
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(482.0, 69.0, image=self.image_image_2)
        self.images_list.append(self.image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(769.0, 411.0, image=self.image_image_3)
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(581.0, 367.0, image=self.image_image_4)
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(771.0, 609.0, image=self.image_image_5)
        self.images_list.append(self.image_5)

        self.image_image_6 = PhotoImage(file=self.controller.get_changedimage())
        self.image_6 = self.canvas.create_image(1162.0, 51.0, image=self.image_image_6)
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(1067.0, 171.0, image=self.image_image_7)
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(476.0, 171.0, image=self.image_image_8)
        self.images_list.append(self.image_8)

        self.image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(905.0, 170.0, image=self.image_image_9)
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(651.0, 170.0, image=self.image_image_10)
        self.images_list.append(self.image_10)

        self.image_image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(962.0, 366.0, image=self.image_image_11)
        self.images_list.append(self.image_11)

        # Dynamic Texts
        self.name_rev = self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername(),
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)

        self.credit_label = self.canvas.create_text(
            1018.0,
            160.0,
            anchor="nw",
            text=self.controller.get_credits() if hasattr(self.controller, "get_credits") else "0 CR",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.credit_label)

    def on_recharge_clicked(self):
        print("[Billing Engine] Opening wallet recharge interface...")
        if hasattr(self.controller, 'add_credits'):
            self.controller.add_credits(500)
        try:
            from theme import play_cyber_sound
            play_cyber_sound("recharge", enabled=self.controller.is_sound_enabled())
        except Exception:
            pass
        bal = self.controller.get_credits() if hasattr(self.controller, 'get_credits') else "500 CR"
        messagebox.showinfo(
            "VLib Credits",
            f"Wallet recharge successful!\n+500 Las Purgas Credits added.\nCurrent balance: {bal}"
        )
        if hasattr(self, 'credit_label'):
            self.canvas.itemconfig(self.credit_label, text=bal)

    def destroy_stuff(self):
        for button in self.buttons_list:
            button.destroy()
        self.buttons_list = []

        for image in self.images_list:
            self.canvas.delete(image)
        self.images_list = []

        for rectangle in self.rectangle_list:
            self.canvas.delete(rectangle)
        self.rectangle_list = []

        for text in self.texts_list:
            self.canvas.delete(text)
        self.texts_list = []

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
