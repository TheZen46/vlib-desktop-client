from pathlib import Path
from tkinter import Pack, Label, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, OptionMenu
import hashlib
import re
import json
from datetime import datetime
from sqlconn_basdata import Mycon_basdata


class SignUp(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"D:\partizione alessandro\programmi+\tentativo parte1\build\assets\frame0")

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
        self.entry_var_1 = StringVar()
        self.entry_var_2 = StringVar()
        self.entry_var_3 = StringVar()
        self.entry_var_4 = StringVar()
        self.entry_var_5 = StringVar()
        self.entry_var_6 = StringVar()
        
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
            command=lambda: self.verificator_all(),
            relief="flat",
            state= 'disabled'
        )
        self.button_7.place(
            x=702.0,
            y=605.0,
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
            command=lambda: self.controller.show_page('sign_in'),
            relief="flat"
        )
        self.button_8.place(
            x=650.0,
            y=605.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)



        #TEXT
        self.Title = self.canvas.create_text(
            276.0,
            31.0,
            anchor="nw",
            text="Sign Up",
            fill="#FDF500",
            font=("ShareTechMono Regular", 50 * -1)
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
            474.0,
            168.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            474.0,
            295.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            765.0,
            343.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            765.0,
            471.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            457.0,
            421.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            859.0,
            173.0,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            872.0,
            215.0,
            image=self.image_image_9
        )
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            953.0,
            213.0,
            image=self.image_image_10
        )
        self.images_list.append(self.image_10)



        #ENTRY_PLACE
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            526.5,
            216.5,
            image=self.entry_image_1
        )
        self.images_list.append(self.entry_bg_1)
        self.entry_1 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate='key',
            textvariable=self.entry_var_1
        )
        self.entry_1['validatecommand'] = (self.entry_1.register(self.validate_input_spaces), '%P')
        self.entry_1.place(
            x=423.0,
            y=194.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_1)

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            526.5,
            343.5,
            image=self.entry_image_2
        )
        self.images_list.append(self.entry_bg_2)
        self.entry_2 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate='key',
            textvariable=self.entry_var_2
        )
        self.entry_2['validatecommand'] = (self.entry_2.register(self.validate_input_spaces), '%P')
        self.entry_2.place(
            x=423.0,
            y=321.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_2)

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            526.5,
            470.5,
            image=self.entry_image_3
        )
        self.images_list.append(self.entry_bg_3)
        self.entry_3 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate='key',
            textvariable=self.entry_var_3
        )
        self.entry_3['validatecommand'] = (self.entry_3.register(self.validate_input_spaces), '%P')
        self.entry_3.place(
            x=423.0,
            y=448.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_3)


        validation_year = self.register(self.validate_numeric_input_year)


        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            1013.0,
            216.5,
            image=self.entry_image_4
        )
        self.images_list.append(self.entry_bg_4)
        self.entry_4 = Entry(
            bd=0,
            font=('Russo One', 16),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate="key",
            validatecommand=(validation_year, "%P"),
            width=2,
            textvariable=self.entry_var_4
        )
        self.entry_4.place(
            x=978.0,
            y=194.0,
            width=70.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_4)


        validation_month = self.register(self.validate_numeric_input_month)


        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            910.5,
            216.5,
            image=self.entry_image_5
        )
        self.images_list.append(self.entry_bg_5)
        self.entry_5 = Entry(
            bd=0,
            font=('Russo One', 15),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate="key",
            validatecommand=(validation_month, "%P"),
            width=4,
            textvariable=self.entry_var_5
        )
        self.entry_5.place(
            x=897.0,
            y=194.0,
            width=27.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_5)


        validation_day = self.register(self.validate_numeric_input_day)

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(829.5, 216.5, image=self.entry_image_6)
        self.images_list.append(self.entry_bg_6)
        self.entry_6 = Entry(
            bd=0,
            font=('Russo One', 15),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            validate="key",
            validatecommand=(validation_day, "%P"),
            width=2,  # Set width to limit the number of characters,
            textvariable=self.entry_var_6
        )
        self.entry_6.place(x=816.0, y=194.0, width=27.0, height=43.0)
        self.entry_place_list.append(self.entry_6)

        self.entry_var_1.trace_add('write', self.check_entries)
        self.entry_var_2.trace_add('write', self.check_entries)
        self.entry_var_3.trace_add('write', self.check_entries)
        self.entry_var_4.trace_add('write', self.check_entries)
        self.entry_var_5.trace_add('write', self.check_entries)
        self.entry_var_6.trace_add('write', self.check_entries)
        
    def check_entries(self, *args):
        # Check if all entry widgets have content
        if (
            self.entry_var_1.get() and
            self.entry_var_2.get() and
            self.entry_var_3.get() and
            self.entry_var_4.get() and
            self.entry_var_5.get() and
            self.entry_var_6.get()
        ):
            # Enable button_7
            self.button_7.config(state='normal')
        else:
            # Disable button_7
            self.button_7.config(state='disabled')


    def validate_numeric_input_day(self, new_value):
        if new_value.isdigit() or new_value =='':
            if len(new_value) <= 2:
                if new_value == '' or 1 <= int(new_value) <= 31:
                    return True
        return False

    def validate_numeric_input_month(self, new_value):
        if new_value.isdigit() or new_value =='':
            if len(new_value) <= 2:
                if new_value == '' or int(new_value) <= 12 and int(new_value) >0:
                    return True
        return False

    def validate_numeric_input_year(self, new_value):
        if new_value.isdigit() or new_value =='':
            if len(new_value) <= 4:
                if new_value == '' or int(new_value) <= 2020 or int(new_value) == 2077:
                    return True
        return False

    def validate_input_spaces(self, text):
        if ' ' in text:
            return False
        return True



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



    def verify_passcode_1(self):
        if self.entry_2.get() == '':
            return False
        
        with open(self.relative_to_assets('all-words.txt'), 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip() == self.entry_2.get():
                    print('so..... you tried a password and that\'s too easy? TRY AGAIN!!')
                    return False
        print('YET, no matching password, congrats it\'s secure')
        return True

    def verify_passcode_2(self):
        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        special_chars_regex = r'[^A-Za-z0-9]'
        numbers_regex = r'\d'
        
        # Check if all requirements are met
        if re.search(uppercase_regex, self.entry_2.get()) and \
        re.search(lowercase_regex, self.entry_2.get()) and \
        re.search(special_chars_regex, self.entry_2.get()) and \
        re.search(numbers_regex, self.entry_2.get()):
            return True
        else:
            return False

    def verification_pass(self):
        if self.verify_passcode_1() == True:
            print('verification password list passed')
            if self.verify_passcode_2() == True:
                print('your password is perfect : \n ACCESS GUARATEED')
                return True
        print('The password is not enough secure')
        return False



    def verification_email(self):
        if self.entry_3.get() == '':
            return False
        
        nomber_at = 0
        
        for character in self.entry_3.get():
            if character == '@':
                nomber_at+=1
        
        if nomber_at == 1:
            print('the email seems correct')
            return True
        
        else:
            print('the email doesn\'t seems correct')
            return False


    def unique_username(self):
        #this function schould be changed when will be added the server connection. (CHANGED)
        sql_namever= Mycon_basdata(
            username= self.entry_1.get()
        )
        save_where= sql_namever.find_and_verify_name()
        
        if save_where== True:
            print('username unique')
            return True
        else:
            print('username already used')
            return False

    def usname_noworld(self):
        if self.entry_1.get() == '':
            return False
        return True

    def verification_usname(self):
        if self.unique_username() == True:
            if self.usname_noworld() == True:
                return True
        return False


    def verification_date(self):
        if self.entry_4.get() == '':
            return False
        
        age = int(datetime.now().year) - int(self.entry_4.get())
        print(age)
        
        if age >= 14:
            if 93 > age:
                return True
        
        return False

    def verificator_all(self):
        if self.verification_usname() == True:
            if self.verification_pass() == True:
                if self.verification_email() == True:
                    if self.verification_date() == True:
                        self.controller.change_username(self.entry_1.get())
                        self.set_temp_datas()
                        self.controller.show_page('description_lang')
                    else:
                        self.controller.show_page('tryagain_signup')
                else:
                    self.controller.show_page('tryagain_signup')
            else:
                self.controller.show_page('tryagain_signup')
        else:
            self.controller.show_page('tryagain_signup')


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    

    def calculate_sha256(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()

    def set_temp_datas(self):
        self.controller.temp_tool(
            what= 'mod',
            where= 'username',
            how= self.entry_1.get()
        )
        self.controller.temp_tool(
            what= 'mod',
            where= 'passcode',
            how= self.entry_2.get()
        )
        self.controller.temp_tool(
            what= 'mod',
            where= 'birth',
            how= f'{self.entry_4.get()}-{self.entry_5.get()}-{self.entry_6.get()}'
        )
        self.controller.temp_tool(
            what= 'mod',
            where= 'email',
            how= self.entry_3.get()
        )