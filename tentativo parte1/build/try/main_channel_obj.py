# [2024-DEV Stage 3/7]: refactor(channel): update active username badge on main_channel canvas
from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

class Main_Channel(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH, username_gave):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        self.username_gave = username_gave
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame8"

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
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda: self.controller.show_page("new_features"),
            relief="flat"
        )
        self.NewFeatures.place(
            x=84.0,
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
            command=self.refresh_channel_view,
            relief="flat"
        )
        self.MainChannel.place(
            x=92.0,
            y=234.0,
            width=142.0,
            height=22.0
        )
        self.buttons_list.append(self.MainChannel)

        self.START_image = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.STARTgame = Button(
            image=self.START_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("start_game"),
            relief="flat"
        )
        self.STARTgame.place(
            x=674.0,
            y=585.0,
            width=237.0,
            height=45.0
        )
        self.buttons_list.append(self.STARTgame)

        self.daily_bonus_btn = Button(
            self,
            text="CLAIM DAILY CR",
            bg="#200628",
            fg="#FDF500",
            activebackground="#9370DB",
            activeforeground="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="ridge",
            bd=1,
            cursor="hand2",
            command=self.on_claim_daily_clicked
        )
        self.daily_bonus_btn.place(
            x=925.0,
            y=585.0,
            width=155.0,
            height=45.0
        )
        self.buttons_list.append(self.daily_bonus_btn)


        #IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            769.0,
            411.0,
            image=self.image_image_2
        )
        self.images_list.append(self.image_2)

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            600.0,
            388.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            1033.0,
            422.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            697.0,
            460.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            769.0,
            231.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            506.0,
            387.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            880.0,
            421.0,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            514.0,
            459.0,
            image=self.image_image_9
        )
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(
            file=self.controller.get_changedimage())
        self.image_10 = self.canvas.create_image(
            1162.0,
            51.0,
            image=self.image_image_10
        )
        self.images_list.append(self.image_10)


        #TEXT
        self.Title = self.canvas.create_text(
            277.0,
            42.0,
            anchor="nw",
            text="Main Channel",
            fill="#FDF500",
            font=("ShareTechMono Regular", 40 * -1)
        )
        self.texts_list.append(self.Title)

        self.Amount = self.canvas.create_text(
            648.0,
            449.0,
            anchor="nw",
            text=self.controller.get_credits() if hasattr(self.controller, 'get_credits') else "2,500 CR",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.Amount)

        self.name= self.canvas.create_text(
            551.0,
            377.0,
            anchor="nw",
            text=self.controller.get_changedusername(),
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name)

        self.nomber = self.canvas.create_text(
            984.0,
            411.0,
            anchor="nw",
            text=self.controller.get_rank() if hasattr(self.controller, 'get_rank') else "LVL 5",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.nomber)

        self. name_rev= self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername(),
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)





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



    def on_claim_daily_clicked(self):
        from tkinter import messagebox
        if hasattr(self.controller, 'claim_daily_allowance'):
            success, reward, balance, msg = self.controller.claim_daily_allowance()
            if hasattr(self, 'Amount'):
                self.canvas.itemconfig(self.Amount, text=self.controller.get_credits())
            try:
                from theme import play_cyber_sound
                if success:
                    play_cyber_sound("claim", enabled=self.controller.is_sound_enabled())
            except Exception:
                pass
            messagebox.showinfo("Syndicate Dividend", msg)
        else:
            messagebox.showinfo("Syndicate Dividend", "Daily allowance service unavailable.")

    def refresh_channel_view(self):
        if hasattr(self, 'Amount') and hasattr(self.controller, 'get_credits'):
            self.canvas.itemconfig(self.Amount, text=self.controller.get_credits())
        if hasattr(self, 'nomber') and hasattr(self.controller, 'get_rank'):
            self.canvas.itemconfig(self.nomber, text=self.controller.get_rank())
        if hasattr(self, 'name') and hasattr(self.controller, 'get_changedusername'):
            self.canvas.itemconfig(self.name, text=self.controller.get_changedusername())
        if hasattr(self, 'name_rev') and hasattr(self.controller, 'get_changedusername'):
            self.canvas.itemconfig(self.name_rev, text=self.controller.get_changedusername())

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
