from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

class New_Features(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame9"

        self.canvas = Canvas(
            self,
            bg = "#272932",
            height=767,
            width=1253,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
        
        self.canvas.place(x = 0, y = 0)
        
        #LOGO's photo
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            120.0,
            111.0,
            image=self.image_image_1
        )

        #THE LINE
        self.canvas.create_rectangle(
            263.5,
            156.5,
            266.0,
            685.0,
            fill="#9370DB",
            outline="")

        #list of all the deletable items
        self.buttons_list = []
        self.images_list = []
        self.rectangle_list = []
        self.texts_list = []





    def create_stuff(self):
        #BUTTONS
        self.rules_image = PhotoImage(
            file = self.relative_to_assets("button_1.png")
        )
        self.rules = Button(
            self, 
            image= self.rules_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda:  self.controller.show_page("rules"),
            relief="flat"
            )
        self.rules.place(
            x=124.0,
            y=547.0,
            width=61.07171630859375,
            height=21.08544921875
        )
        self.buttons_list.append(self.rules)

        self.ContactUs_image = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.ContactUs = Button(
            self,
            image=self.ContactUs_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda:  self.controller.show_page("contact_us"),
            relief="flat"
        )
        self.ContactUs.place(
            x=1133.0,
            y=741.0,
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
            x=95.0,
            y=338.0,
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


        #TEXT
        self.Title = self.canvas.create_text(
            277.0,
            42.0,
          anchor="nw",
           text="New Features",
           fill="#FDF500",
            font=("ShareTechMono Regular", 40 * -1)
        )
        self.texts_list.append(self.Title)

        self.name_rev = self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername(),
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)

        self.text_info = self.canvas.create_text(
            430.0,
            418.0,
            anchor="nw",
            text="PATCH HIGHLIGHTS & RELEASE NOTES",
            fill="#FDF500",
            font=("Arial", 11, "bold")
        )
        self.texts_list.append(self.text_info)

        features = [
            ("⚡ CYBER DICE & TERMINAL HACK", "Playable in-app casino game with animated dice roll physics, terminal hack, and multi-tier chip betting."),
            ("💰 VIRTUAL ECONOMY ENGINE", "Persistent credit wallets, VIP status multipliers, daily syndicate allowance (+250 / +500 CR), and audit logs."),
            ("🛠️ MODULAR MODDING MATRIX", "Live sandbox manager supporting real-time toggling of post-processing shaders, audio decks, and tools."),
            ("🎫 SYNDICATE SUPPORT MATRIX", "Restored back navigation, automated ticket dispatching (LP-XXXXX), and local diagnostic buffers."),
            ("🔒 OFFLINE RESILIENCE & PILLOW AVATARS", "High-DPI alpha-mask rounded corners, SHA-256 session encryption, and seamless MySQL offline fallback.")
        ]
        start_y = 445.0
        for i, (title, desc) in enumerate(features):
            y = start_y + i * 44.0
            t_head = self.canvas.create_text(
                435.0, y,
                anchor="nw",
                text=title,
                fill="#FDF500",
                font=("Arial", 9, "bold")
            )
            self.texts_list.append(t_head)

            t_desc = self.canvas.create_text(
                435.0, y + 16.0,
                anchor="nw",
                text=desc,
                fill="#bdc3c7",
                font=("Arial", 8)
            )
            self.texts_list.append(t_desc)

        self.vlib_patch= self.canvas.create_text(
            955.0,
            175.0,
            anchor="nw",
            text="1.0.0",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.vlib_patch)

        self.launcher_patch= self.canvas.create_text(
            984.0,
            236.0,
            anchor="nw",
            text="1.0.0",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.launcher_patch)

        self.last_update= self.canvas.create_text(
            955.0,
            297.0,
            anchor="nw",
            text="2023-12-16",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.last_update)


        #IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.purpleBG = self.canvas.create_image(
            769.0,
            411.0,
            image=self.image_image_2
        )
        self.images_list.append(self.purpleBG)

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            1004.0,
            186.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            1033.0,
            247.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            1004.0,
            308.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            779.0,
            541.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            565.0,
            246.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            850.0,
            185.0,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            873.0,
            246.0,
            image=self.image_image_9
        )
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            857.0,
            307.0,
            image=self.image_image_10
        )
        self.images_list.append(self.image_10)

        self.image_image_11 = PhotoImage(
            file=self.relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            769.0,
            368.0,
            image=self.image_image_11
        )
        self.images_list.append(self.image_11)

        self.image_image_12 = PhotoImage(
            file=self.controller.get_changedimage())
        self.image_12 = self.canvas.create_image(
            1162.0,
            51.0,
            image=self.image_image_12
        )
        self.images_list.append(self.image_12)



    def destroy_stuff(self):
        #DESTROY BUTTONS
        for button in self.buttons_list:
            button.destroy()
        self.buttons_list = []

        #DESTROY IMAGES
        for image in self.images_list:
            self.canvas.delete(image)
        self.images_list = []

        #DESTROY RECTANGLES
        for rectangle in self.rectangle_list:
            self.canvas.delete(rectangle)
        self.rectangle_list = []
        
        #DESTROY TEXTS
        for text in self.texts_list:
            self.canvas.delete(text)
        self.texts_list = []



    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
