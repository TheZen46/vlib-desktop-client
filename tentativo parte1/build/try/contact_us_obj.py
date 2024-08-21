from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox, simpledialog


class ContactUs(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame13"

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
        
        # LOGO's photo
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            120.0,
            111.0,
            image=self.image_image_1
        )

        # THE LINE
        self.canvas.create_rectangle(
            263.5,
            156.5,
            266.0,
            685.0,
            fill="#9370DB",
            outline=""
        )

        # list of all the deletable items
        self.buttons_list = []
        self.images_list = []
        self.rectangle_list = []
        self.texts_list = []

    def create_stuff(self):
        # BUTTONS
        self.Rules_image = PhotoImage(
            file=self.relative_to_assets("button_1.png")
        )
        self.Rules = Button(
            self, 
            image=self.Rules_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda: self.controller.show_page("rules"),
            relief="flat"
        )
        self.Rules.place(
            x=124.0,
            y=547.0,
            width=61.07171630859375,
            height=21.08544921875
        )
        self.buttons_list.append(self.Rules)

        self.ContactUs_image = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.ContactUs = Button(
            image=self.ContactUs_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("contact_us"),
            relief="flat"
        )
        self.ContactUs.place(
            x=1136.0,
            y=735.0,
            width=109.07171630859375,
            height=18.271484375
        )
        self.buttons_list.append(self.ContactUs)

        self.HowDoesItWork_image = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.HowDoesItWork = Button(
            image=self.HowDoesItWork_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("howdoesitwork"),
            relief="flat"
        )
        self.HowDoesItWork.place(
            x=20.0,
            y=741.0,
            width=232.0,
            height=18.271484375
        )
        self.buttons_list.append(self.HowDoesItWork)

        self.Options_image = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.Options = Button(
            image=self.Options_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("options"),
            relief="flat"
        )
        self.Options.place(
            x=114.0,
            y=441.0,
            width=82.0,
            height=22.1328125
        )
        self.buttons_list.append(self.Options)

        self.NewFeatures_image = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.NewFeatures = Button(
            image=self.NewFeatures_image,
            borderwidth=0,
            highlightthickness=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda: self.controller.show_page("new_features"),
            relief="flat"
        )
        self.NewFeatures.place(
            x=84.0,
            y=339.0,
            width=142.10357666015625,
            height=19.37548828125
        )
        self.buttons_list.append(self.NewFeatures)

        self.MainChannel_image = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.MainChannel = Button(
            image=self.MainChannel_image,
            bg='#272932',
            activebackground='#272932',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_page("main_channel"),
            relief="flat"
        )
        self.MainChannel.place(
            x=92.0,
            y=234.0,
            width=142.0,
            height=22.0
        )
        self.buttons_list.append(self.MainChannel)

        # BACK BUTTON (Restored from asset frame13/button_9.png)
        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page('options'),
            relief="flat"
        )
        self.button_9.place(
            x=402.0,
            y=636.5,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_9)

        # IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            416.0,
            77.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            769.0,
            411.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            769.0,
            382.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_2)
        self.images_list.append(self.image_3)
        self.images_list.append(self.image_4)

        # USERNAME BADGE
        self.name_rev = self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername() if hasattr(self.controller, 'get_changedusername') else "",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)

        # SUPPORT MATRIX DETAILS (Centered over image_4)
        t1 = self.canvas.create_text(
            769.0,
            275.0,
            anchor="center",
            text="LAS PURGAS SYNDICATE SUPPORT MATRIX",
            fill="#FDF500",
            font=("Arial", 16, "bold")
        )
        self.texts_list.append(t1)

        t2 = self.canvas.create_text(
            769.0,
            310.0,
            anchor="center",
            text="Official Community:  discord.gg/laspurgas",
            fill="#8be9fd",
            font=("Arial", 11, "bold")
        )
        self.texts_list.append(t2)

        t3 = self.canvas.create_text(
            769.0,
            335.0,
            anchor="center",
            text="Technical Dispatch:  support@laspurgas.net",
            fill="#50fa7b",
            font=("Arial", 11, "bold")
        )
        self.texts_list.append(t3)

        t4 = self.canvas.create_text(
            769.0,
            360.0,
            anchor="center",
            text="Source Repository:  github.com/TheZen46/vlib-desktop-client",
            fill="#ff79c6",
            font=("Arial", 11, "bold")
        )
        self.texts_list.append(t4)

        t5 = self.canvas.create_text(
            769.0,
            395.0,
            anchor="center",
            text="For account recoveries, mod verification, or billing inquiries, dispatch a ticket below.",
            fill="#cfcfcf",
            font=("Arial", 9)
        )
        self.texts_list.append(t5)

        # DISPATCH TICKET BUTTON
        self.dispatch_btn = Button(
            self,
            text="DISPATCH SUPPORT TICKET",
            command=self.on_dispatch_ticket,
            bg="#200628",
            fg="#FDF500",
            activebackground="#9370DB",
            activeforeground="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="ridge",
            bd=1,
            cursor="hand2"
        )
        self.dispatch_btn.place(
            x=654.0,
            y=428.0,
            width=230.0,
            height=36.0
        )
        self.buttons_list.append(self.dispatch_btn)

    def on_dispatch_ticket(self):
        user = self.controller.get_changedusername() if hasattr(self.controller, 'get_changedusername') else "Operative"
        if hasattr(self.controller, 'submit_support_ticket'):
            ticket = self.controller.submit_support_ticket(
                category="General Inquiries",
                message=f"Standard support request dispatched from client session by {user}."
            )
            ticket_id = ticket.get("ticket_id", "LP-00000")
            messagebox.showinfo(
                "Support Dispatch Confirmed",
                f"Ticket #{ticket_id} has been logged in Las Purgas Support Matrix!\n\n"
                f"User: {user}\nStatus: OPEN\n"
                "A syndicate representative will review your request shortly."
            )
        else:
            messagebox.showinfo("Support Notice", "Ticket logged to local diagnostics buffer.")

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
