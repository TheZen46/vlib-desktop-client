from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

class Options(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame10"

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
            highlightthickness=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda: self.controller.show_page("options"),
            relief="flat"
        )
        self.Options.place(
            x=122.0,
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

        self.KYS_image = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.KYSbutton = Button(
            image=self.KYS_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.logout(),
            relief="flat"
        )
        self.KYSbutton.place(
            x=905.0,
            y=589.0,
            width=125.0,
            height=45.0
        )
        self.buttons_list.append(self.KYSbutton)

        sound_on = self.controller.is_sound_enabled() if hasattr(self.controller, 'is_sound_enabled') else True
        btn_text = "🔊 AUDIO FX: ENABLED" if sound_on else "🔇 AUDIO FX: MUTED"
        btn_fg = "#50fa7b" if sound_on else "#888888"

        self.audio_toggle_btn = Button(
            self,
            text=btn_text,
            bg="#200628",
            fg=btn_fg,
            activebackground="#9370DB",
            activeforeground="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="ridge",
            bd=1,
            cursor="hand2",
            command=self.on_toggle_audio
        )
        self.audio_toggle_btn.place(
            x=448.0,
            y=589.0,
            width=210.0,
            height=45.0
        )
        self.buttons_list.append(self.audio_toggle_btn)

        self.Modding_image = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.Modding = Button(
            image=self.Modding_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("modding"),
            relief="flat"
        )
        self.Modding.place(
            x=448.0,
            y=197.0,
            width=151.0,
            height=47.0
        )
        self.buttons_list.append(self.Modding)

        self.GetVip_image = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.GetVip = Button(
            image=self.GetVip_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("getVIP"),
            relief="flat"
        )
        self.GetVip.place(
            x=448.0,
            y=324.0,
            width=151.0,
            height=47.0
        )
        self.buttons_list.append(self.GetVip)

        self.Check4Updates_image = PhotoImage(
            file=self.relative_to_assets("button_10.png"))
        self.Check4Updates = Button(
            image=self.Check4Updates_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("check4updates"),
            relief="flat"
        )
        self.Check4Updates.place(
            x=879.0,
            y=197.0,
            width=231.0,
            height=47.0
        )
        self.buttons_list.append(self.Check4Updates)

        self.ModifyAccount_image = PhotoImage(
            file=self.relative_to_assets("button_11.png"))
        self.ModifyAccount = Button(
            image=self.ModifyAccount_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("modifyaccount"),
            relief="flat"
        )
        self.ModifyAccount.place(
            x=879.0,
            y=324.0,
            width=231.0,
            height=47.0
        )
        self.buttons_list.append(self.ModifyAccount)

        self.LanguageSettings_image = PhotoImage(
            file=self.relative_to_assets("button_12.png"))
        self.LanguageSettings = Button(
            image=self.LanguageSettings_image,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("languagesettings"),
            relief="flat"
        )
        self.LanguageSettings.place(
            x=643.0,
            y=411.0,
            width=253.0,
            height=47.0
        )
        self.buttons_list.append(self.LanguageSettings)


        #TEXT
        self. name_rev= self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername(),
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)

        #IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            368.0,
            69.0,
            image=self.image_image_2
        )
        self.images_list.append(self.image_2)

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            769.0,
            411.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            665.0,
            615.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.controller.get_changedimage())
        self.image_5 = self.canvas.create_image(
            1162.0,
            51.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)



    def on_toggle_audio(self):
        from theme import play_cyber_sound
        if hasattr(self.controller, 'toggle_sound'):
            new_state = self.controller.toggle_sound()
            btn_text = "🔊 AUDIO FX: ENABLED" if new_state else "🔇 AUDIO FX: MUTED"
            btn_fg = "#50fa7b" if new_state else "#888888"
            self.audio_toggle_btn.config(text=btn_text, fg=btn_fg)
            if new_state:
                play_cyber_sound("claim", enabled=True)

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
    
