from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
import hashlib


class Forgotthepassword(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"D:\partizione alessandro\programmi+\tentativo parte1\build\assets\frame7")

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
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=723.0,
            y=581.0,
            width=203.0,
            height=43.0
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
            command=lambda: self.controller.show_page('sign_in'),
            relief="flat"
        )
        self.button_8.place(
            x=654.0,
            y=581.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)


        #TEXT
        self.Title = self.canvas.create_text(
            277.0,
            42.0,
            anchor="nw",
            text="Forgot the password?",
            fill="#FDF500",
            font=("ShareTechMono Regular", 40 * -1)
        )
        self.texts_list.append(self.Title)


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
            528.0,
            207.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            928.0,
            345.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            514.0,
            369.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)


        #ENTRY_PLACE
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            580.5,
            255.5,
            image=self.entry_image_1
        )
        self.images_list.append(self.entry_bg_1)
        self.entry_1 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_1.place(
            x=477.0,
            y=233.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_1)

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            580.5,
            419.0,
            image=self.entry_image_2
        )
        self.images_list.append(self.entry_bg_2)
        self.entry_2 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_2.place(
            x=477.0,
            y=397.0,
            width=207.0,
            height=42.0
        )
        self.entry_place_list.append(self.entry_2)



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



    def value_of_boxes(self):
        list_values = []
        list_values.append(self.entry_1.get())
        list_values.append(self.entry_2.get())
        print(list_values)
        return list_values 



    def verify_compilated_areas(self):
        list_compilation = []
        list_answer = [self.entry_1.get(), self.entry_2.get()]
        
        if self.entry_1.get() == '' or self.entry_1.get()== ' ':
            list_compilation.append(False)
        else:
            list_compilation.append(True)
        
        if self.entry_2.get() == '' or self.entry_2.get() == ' ':
            list_compilation.append(False)
        else:
            list_compilation.append(True)
        
        print(list_compilation)
        print(list_answer)

        self.dictionario = {}


        self.read_dict_from_file(self.dictionario)

        return list_compilation



    def no_compilation(self):
        neutral_list = self.verify_compilated_areas()
        for boll in neutral_list:
            if boll == False:
                return False
        return True



    def compilation_variation(self):
        if self.no_compilation() == True:
            if self.dictionario['username'] == self.entry_1.get():
                if self.dictionario['password'] == self.entry_2.get():
                    print('check 1 passed')
                    print(f'the sha256 hash of the passcode is : \n {self.calculate_sha256(self.entry_2.get())}')

        else:
            print('check 1 not passed')
            

    def read_dict_from_file(self, dictionary):
        dictionary = {}

        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(': ')
                dictionary[key] = value
        self.dictionario = dictionary



    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    


    def calculate_sha256(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()