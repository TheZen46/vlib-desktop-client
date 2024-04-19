from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, BooleanVar
import hashlib
try:
    import mysql.connector
except ImportError:
    mysql = None
import json
from sqlconn_basdata import Mycon_basdata
from dropboxconn import DropConn

class SignIn(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame6"

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
        #self.check_auth()
        
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
            command=lambda: self.watcha_base(),
            relief="flat"
        )
        self.button_7.place(
            x=665.0,
            y=583.0,
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
            command=lambda: self.controller.show_page('forgotthepassword'),
            relief="flat"
        )
        self.button_8.place(
            x=809.0,
            y=651.0,
            width=183.0,
            height=21.0
        )
        self.buttons_list.append(self.button_8)


        self.checkbutton = self.CustomCheckbutton(
            width = 50,
            height= 50,
            relative_to_assets=self.relative_to_assets,
            on_callback= self.check_on,
            off_callback= self.check_off
        )
        self.checkbutton.place(
            x=892.0,
            y=412.0
        )
        self.buttons_list.append(self.checkbutton)

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page('sign_up'),
            relief="flat"
        )
        self.button_9.place(
            x=549.0,
            y=651.0,
            width=183.0,
            height=21.0
        )
        self.buttons_list.append(self.button_9)


        #TEXT
        self.Title = self.canvas.create_text(
            274.0,
            33.0,
            anchor="nw",
            text="Sign in",
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
            717.0,
            263.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            717.0,
            390.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        #ENTRY_PLACE
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            769.5,
            311.5,
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
            x=666.0,
            y=289.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_1)

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            769.5,
            438.5,
            image=self.entry_image_2
        )
        self.images_list.append(self.entry_bg_2)
        self.entry_2 = Entry(
            bd=0,
            font=('Russo One', 16),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0,
            show= '*'
        )
        self.entry_2.place(
            x=666.0,
            y=416.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_2)

    def check_on(self):
        print('on')
        self.entry_2["show"] = ""


    def check_off(self):
        print('off')
        self.entry_2["show"] = "*"

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

        return list_compilation



    def no_compilation(self):
        neutral_list = self.verify_compilated_areas()
        for boll in neutral_list:
            if boll == False:
                return False
        return True


    def watcha_base(self):
        username_entry = self.entry_1.get().strip() if hasattr(self, 'entry_1') else ''
        password_entry = self.entry_2.get().strip() if hasattr(self, 'entry_2') else ''
        if not username_entry or not password_entry:
            print("[SignIn] Username or password empty.")
            return

        try:
            get_sql = Mycon_basdata(username=username_entry, password=password_entry)
            if get_sql.find_and_verify():
                print(f"[SignIn] Verification successful for user '{username_entry}'")
                self.controller.change_username(new_username=username_entry)
                s = get_sql.get_imagepath()
                if s in ['samurai1_png', 'V1_png', 'CasualBG1_png', 'LightVL1_png']:
                    self.controller.change_img(new_image=f'{s}.png')
                else:
                    try:
                        get_box = DropConn()
                        get_box.downlaod_onlyimage(name_file=f'{s}')
                        self.controller.change_img(new_image='local_downloaded_image.png')
                    except Exception:
                        self.controller.change_img(new_image='samurai1_png.png')
                self.controller.show_page("main_channel")
                return
        except Exception as e:
            print(f"[SignIn] Remote/offline check error: {e}")

        for user_data in self.read_dicts_from_file():
            if user_data.get('username') == username_entry and user_data.get('password') == password_entry:
                self.controller.change_username(new_username=username_entry)
                img = user_data.get('icon_image', 'samurai1_png.png')
                self.controller.change_img(img)
                self.controller.show_page("main_channel")
                return

        print(f"[SignIn] Invalid credentials for user '{username_entry}'")

    def read_data(self, filename):
        search_paths = [
            Path(filename),
            Path(__file__).resolve().parent.parent.parent / filename,
            Path(__file__).resolve().parent / filename
        ]
        for p in search_paths:
            if p.exists():
                try:
                    with open(p, 'r', encoding='utf-8') as file:
                        return json.load(file)
                except Exception:
                    pass
        return {}

    def compilation_variation(self):
        if self.no_compilation() == True:
            for dictionaries in self.read_dicts_from_file():
                if dictionaries['username'] == self.entry_1.get():
                    if dictionaries['password'] == self.entry_2.get():
                        self.controller.change_username(dictionaries['username'])
                        self.controller.change_img(dictionaries['icon_image'])
                        self.controller.show_page('main_channel')

        else:
            print('check 1 not passed')


    def check_auth(self):
        getit= self.read_data("Onl_verification.json")
        print('hi')
        if getit.get('activity') == 'Active':
            get_sql= Mycon_basdata(
                username= getit['user'],
                password= getit['pass']
            )
            print('give em ball')
            if get_sql.find_and_verify_noenc() == True:
                print('halo calo')
                self.controller.change_username(new_username= getit['user'])
                s= get_sql.get_imagepath()
                print('ballerz')
                if s== 'samurai1_png' or s== 'V1_png' or s== 'CasualBG1_png' or s== 'LightVL1_png':
                    tupler= s
                    print(tupler)
                    self.controller.change_img(new_image= f'{s}.png')
                    #self.controller.show_page("main_channel")
                    return 'main_channel'
                else:
                    print(s)
                    get_box= DropConn()
                    get_box.downlaod_onlyimage(name_file= f'{s}')
                    self.controller.change_img(new_image= 'local_downloaded_image.png')
                    #self.controller.show_page("main_channel")
                    return 'main_channel'
            else:
                return 'sign_in'
        else:
            return 'sign_in'
        
        print('mushrooms')




    def read_dicts_from_file(self):
        user_dicts = []
        search_paths = [
            Path(__file__).resolve().parent.parent.parent / 'users.txt',
            Path(__file__).resolve().parent.parent / 'users.txt',
            Path(__file__).resolve().parent / 'users.txt',
            Path('users.txt')
        ]
        target_path = None
        for p in search_paths:
            if p.exists():
                target_path = p
                break

        if not target_path:
            return user_dicts

        try:
            with open(target_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                user_dict = {}
                for line in lines:
                    line = line.strip()
                    if not line:
                        if user_dict:
                            user_dicts.append(user_dict)
                            user_dict = {}
                    elif ': ' in line:
                        key, value = line.split(': ', 1)
                        user_dict[key] = value
                if user_dict:
                    user_dicts.append(user_dict)
        except Exception as e:
            print(f"[SignIn] Notice reading users file: {e}")
        return user_dicts

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    


    def calculate_sha256(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()
    
    class CustomCheckbutton(Canvas):
        def __init__(self, relative_to_assets, master=None, on_callback=None, off_callback=None, **kwargs):
            super().__init__(master, **kwargs)
            self.checked_image = PhotoImage(file=relative_to_assets('button_11.png'))
            self.unchecked_image = PhotoImage(file=relative_to_assets('button_10.png'))
            self.on_callback = on_callback
            self.off_callback = off_callback 
            self.checked = BooleanVar(value=False)
            self.bind("<Button-1>", self.toggle)
            self.draw()

        def toggle(self, event=None):
            self.checked.set(not self.checked.get())
            self.draw()
            if self.checked.get() and self.on_callback:
                self.on_callback()
                self.update()
            elif not self.checked.get() and self.off_callback:
                self.off_callback()
                self.update()

        def draw(self):
            self.delete("all")
            image = self.checked_image if self.checked.get() else self.unchecked_image
            self.create_image(0, 0, anchor="nw", image=image)
            self.configure(
                background='#200628',
                borderwidth=0,
                highlightthickness=0
            )