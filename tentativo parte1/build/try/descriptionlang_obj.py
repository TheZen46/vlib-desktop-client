from pathlib import Path
from tkinter import Pack, Label, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, OptionMenu


class DescriptionLang(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        self.char_count = StringVar()
        self.char_count.set("You have no description, so sad...")

        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame1"

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
        self.entry_place_list = []



    def create_stuff(self):
        #BUTTONS
        self.Rules_image = PhotoImage(
            file = self.relative_to_assets("button_1.png")
        )
        self.Rules = Button(
            self, 
            image= self.Rules_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda:  self.controller.show_page("rules"),
            relief="flat",
            state= "disabled"
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
            self,
            image=self.ContactUs_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            highlightthickness=0,
            command=lambda:  self.controller.show_page("contact_us"),
            relief="flat",
            state= "disabled"
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
            relief="flat",
            state= "disabled"
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
            relief="flat",
            state= "disabled"
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
            relief="flat",
            state= "disabled"
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
            relief="flat",
            state= "disabled"
        )
        self.MainChannel.place(
            x=92.0,
            y=234.0,
            width=142.0,
            height=22.0
        )
        self.buttons_list.append(self.MainChannel)

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.change_pag(),
            relief="flat"
        )
        self.button_7.place(
            x=747.0,
            y=618.0,
            width=237.0,
            height=45.0
        )
        self.buttons_list.append(self.button_7)

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page('sign_up'),
            relief="flat"
        )
        self.button_8.place(
            x=687.0,
            y=618.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)


        #TEXT



        #IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            408.0,
            60.0,
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
            485.0,
            208.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            492.0,
            354.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            947.0,
            444.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            876.0,
            266.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.image_8 = self.canvas.create_image(
            510.0,
            251.5,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)

        #DROPDOWN_LIST
        self.valdrop = ''
        
        language_codes = [
            "AFR", "AKA", "ALB", "AMH", "ARA", "ARM", "ASM", "AZE", "BAK", "BEL",
            "BEN", "BHO", "BIS", "BOD", "BOS", "BUL", "BUR", "CAT", "CEB", "CHE",
            "CHI", "CHT", "CHU", "CHV", "COS", "CRE", "CRO", "CZE", "DAG", "DAN",
            "DAR", "DEU", "DUT", "ENG", "EPO", "EST", "EUS", "FAO", "FAS", "FIN",
            "FRA", "FRY", "FUR", "GAE", "GEO", "GID", "GLE", "GLG", "GLV", "GOT",
            "GRC", "GRN", "GUA", "GUJ", "HAT", "HAU", "HAW", "HEB", "HER", "HIN",
            "HMO", "HRV", "HUN", "IBO", "IDO", "ILE", "INA", "IND", "ISL", "ITA",
            "JAV", "JPN", "KAN", "KAT", "KAZ", "KHM", "KIK", "KIR", "KOM", "KON",
            "KOR", "KUA", "KUR", "LAO", "LAT", "LAV", "LIT", "LUG", "LIM", "LIN",
            "LIN", "LIT", "LTV", "LUB", "LUG", "LUO", "MAC", "MAH", "MAL", "MAR",
            "MGL", "MLG", "MLT", "MYA", "NEP", "NLD", "NOR", "NYA", "NYN", "OCI",
            "OJI", "ORI", "ORM", "OSS", "PAH", "PAN", "PES", "PLI", "POL", "POR",
            "QUE", "RON", "RUN", "RUS", "SAG", "SAN", "SCN", "SCO", "SEL", "SIN",
            "SLA", "SLK", "SLV", "SME", "SMO", "SND", "SND", "SOM", "SON", "SPA",
            "SQI", "SRB", "SSW", "SUN", "SWA", "SWE", "TAH", "TAM", "TAT", "TEL",
            "TGK", "TGL", "THA", "TIB", "TIR", "TON", "TPI", "TSN", "TUR", "TUK",
            "TWI", "UDM", "UIG", "UKR", "URD", "UZB", "VEN", "VIE", "VOL", "WEL",
            "WOL", "XHO", "YID", "YOR", "ZHA", "ZUL"
        ]

        self.dropdown_list = CustomDropdown(self, options= language_codes, callback=self.change_valdrop)
        self.dropdown_list.configure(
            borderwidth=0,
            highlightthickness=0,
            background='#272932'
        )
        self.dropdown_list.place(
            x=483,
            y=240,
            width=55
        )
        self.buttons_list.append(self.dropdown_list)


        #ENTRY_PLACE
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            583.5,
            436.0,
            image=self.entry_image_1
        )
        self.images_list.append(self.entry_bg_1)
        self.entry_1 = Text(
            bd=0,
            font=('Russo One', 12),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_1.place(
            x=448.0,
            y=380.0,
            width=271.0,
            height=110.0
        )
        self.entry_1.bind('<KeyRelease>', self.validate_input)
        self.entry_place_list.append(self.entry_1)


        self.char_count_label = Label(
            self, 
            textvariable=self.char_count,
            bg="#200628",
            fg="#fdf500",
            font=('Lexend', 10)
        )
        self.char_count_label.place(
            x=436.0,
            y=500.0
        )


    def validate_input(self, event=None):
        text_content = self.entry_1.get("1.0", "end-1c")
        
        # Truncate the text to 200 characters if it exceeds the limit
        if len(text_content) > 400:
            text_content = text_content[:400]
            self.entry_1.delete("1.0", "end-1c")
            self.entry_1.insert("1.0", text_content)

        char_count = len(text_content)
        self.char_count.set(f"You've written {char_count} of 400 characters available")

        if char_count >= 400:
            self.char_count_label.config(fg="red")
            self.char_count.set(f"You've reached the maximum amount of characters")
        elif char_count == 0:
            self.char_count.set("You have no description, so sad...")
        elif char_count == 69 or char_count== 104:
            self.char_count.set(f"Character limit exceeded: {char_count}/400. Please shorten your description.")
        else:
            self.char_count_label.config(fg="#fdf500")
            self.char_count.set(f"You've written {char_count} of 400 characters available")


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

        #DESTROY ENTRY_PLACE
        for entry_place in self.entry_place_list:
            entry_place.destroy()
        self.entry_place_list = []

    def set_temp_datas(self):
        self.controller.temp_tool(
            what= 'mod',
            where= 'description',
            how= self.entry_1.get("1.0", "end-1c")
        )
        self.controller.temp_tool(
            what= 'mod',
            where= 'lang',
            how= self.dropdown_list.get_selected_option()
        )

    def change_pag(self):
        self.set_temp_datas()
        self.controller.show_page('personalizeimage')

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def change_valdrop(self, option):
        self.valdrop = option

class CustomDropdown(Frame):
    def __init__(self, parent, options, callback=None):
        super().__init__(parent)
        self.options = options
        self.callback = callback

        self.var = StringVar(value=options[0])
        self.option_menu = OptionMenu(self, self.var, *self.options, command=self.handle_selection)
        self.option_menu.config(
            bg='#272932',
            activebackground='#272932',
            borderwidth=0,
            highlightcolor='#272932',
            foreground='#FDF500',
            activeforeground='#FDF590',
            highlightthickness= 0
        )
        self.option_menu["menu"].config(
            background='#272932',
            border=0,
            borderwidth=0,
            foreground='#FDF500'
        )
        self.option_menu.pack()

    def handle_selection(self, option):
        # Implement this method to handle the selected option
        if self.callback is not None:
            self.callback(option)

    def get_selected_option(self):
        return self.var.get()