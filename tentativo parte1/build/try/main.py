from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, Label
from main_channel_obj import Main_Channel
from new_features_2obj import New_Features
from options_obj import Options
from rules_obj import Rules
from howdoesitworks_obj import HowDoesItWorks
from contact_us_obj import ContactUs
from signin_obj import SignIn
from signup_obj import SignUp
from tryagain_obj import TryAgain_SignUp
from descriptionlang_obj import DescriptionLang
from contactus_tryagain_obj import ContactUs_TryAgain
from personalizeimage_obj import PersonalizeImage
from termsandconditions_obj import TermsAndConditions
from done_obj import Done
from modding_obj import Modding
from getVIP_obj import getVIP
from check4updates_obj import Check4updates
from modifyaccount_obj import Modifyaccount
from languagesettings_obj import Languagesettings
from roles_obj import Roles
from rulz_obj import Rulz
from forgotthepassword_obj import Forgotthepassword
import time
import math
import threading

BACKGROUND_COLOR = '#272932'
SPHERE_COLOR = '#FDF500'
SPHERE_POINTS = 100  # Increase the number of points for better quality
AMPLITUDE = 15  # Adjust the amplitude of the wave
FREQUENCY = 3.2  # Adjust the frequency of the wave


class LoadingPage(Toplevel):
    def __init__(self, parent, new_page= None):
        Toplevel.__init__(self, parent)
        self.new_page = new_page
        self.title('Loading')
        self.geometry('175x150')
        self.attributes('-topmost', True)
        self.configure(
            bg= '#272932'
        )


        self.create_loading_animation()

    def create_loading_animation(self):
        loading_frame = Frame(self, background=BACKGROUND_COLOR)
        loading_frame.pack()

        self.canvas = Canvas(loading_frame, width=100, height=50, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.canvas.pack(
            padx=5,
            pady=10
        )

        self.spheres = []
        self.running = True

        self.create_spheres()
        self.animate_spheres()

    def create_spheres(self):
        x = 20
        y = 25
        radius = 5
        distance = 15

        for _ in range(6):
            sphere = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=SPHERE_COLOR)
            self.spheres.append(sphere)
            x += distance

    def animate_spheres(self):
        delay = 50  # milliseconds
        start_time = time.time()

        while self.running:
            t = time.time() - start_time

            for i, sphere in enumerate(self.spheres):
                x = 20 + i * 15
                y = 25 + AMPLITUDE * math.sin(FREQUENCY * (2 * math.pi * (i / len(self.spheres)) - FREQUENCY * t))
                self.canvas.coords(sphere, x - 5, y - 5, x + 5, y + 5)

            self.update()
            time.sleep(delay / 9000)

    def on_closing(self):
        self.running = False
        self.destroy()
    
    def verify_situation(self):
        if self.new_page.get_actual_val() == self.new_page.get_total_loading_progress():
            self.on_closing()


OUTPUT_PATH = Path(__file__).parent


class Application(Tk):
    def __init__(self, OUTPUT_PATH):
        Tk.__init__(self)
        self.OUTPUT_PATH = OUTPUT_PATH
        self.title('VLib')

        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        self.geometry("1253x767")
        self.configure(bg='#272932')
        self.iconbitmap('las_purgas.ico')

        self.username = ''
        self.where_image = 'D:/partizione alessandro/programmi+/tentativo parte1/build/assets/frame4/button_9.png'

        self.pages = {}

        self.resizable(False, False)


        #temp data store
        self.temp_username= ''
        self.temp_enpasscode= ''
        self.temp_birthday= ''
        self.temp_description= ''
        self.temp_language= ''
        self.temp_filestor= ''
        self.temp_mail= ''
        #this datas will be deleted once the creation of a new account



        self.new_features = New_Features(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.main_channel = Main_Channel(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH, username_gave=self.username)
        self.options = Options(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.rules = Rules(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.howdoesitwork = HowDoesItWorks(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.contact_us = ContactUs(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.sign_in = SignIn(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.sign_up = SignUp(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.tryagain_signup = TryAgain_SignUp(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.description_lang = DescriptionLang(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.contactus_tryagain = ContactUs_TryAgain(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.personalizeimage = PersonalizeImage(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.termsandconditions = TermsAndConditions(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.done = Done(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.modding = Modding(self.container, self, OUTPUT_PATH= self.OUTPUT_PATH)
        self.getVIP = getVIP(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.check4updates = Check4updates(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.modifyaccount = Modifyaccount(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.languagesettings = Languagesettings(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.roles = Roles(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.rulz = Rulz(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.forgotthepassword = Forgotthepassword(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)

        self.pages['main_channel'] = self.main_channel
        self.pages['new_features'] = self.new_features
        self.pages['options'] = self.options
        self.pages['rules'] = self.rules
        self.pages['howdoesitwork'] = self.howdoesitwork
        self.pages['contact_us'] = self.contact_us
        self.pages['sign_in'] = self.sign_in
        self.pages['sign_up'] = self.sign_up
        self.pages['tryagain_signup'] = self.tryagain_signup
        self.pages['description_lang'] = self.description_lang
        self.pages['contactus_tryagain'] = self.contactus_tryagain
        self.pages['personalizeimage'] = self.personalizeimage
        self.pages['termsandconditions'] = self.termsandconditions
        self.pages['done'] = self.done
        self.pages['modding'] = self.modding
        self.pages['getVIP'] = self.getVIP
        self.pages['check4updates'] = self.check4updates
        self.pages['modifyaccount'] = self.modifyaccount
        self.pages['languagesettings'] = self.languagesettings
        self.pages['roles'] = self.roles
        self.pages['rulz'] = self.rulz
        self.pages['forgotthepassword'] = self.forgotthepassword

        #first_page_opening= 'sign_in'
        lex= self.sign_in.check_auth()

        self.show_page(lex)

    def show_page(self, page_name):

        if 'current' in self.pages:
            current_page = self.pages['current']
            current_page.pack_forget()
            current_page.destroy_stuff()

        new_page = self.pages[page_name]
        new_page.pack(fill='both', expand=True)



        new_page.create_stuff()
        self.pages['current'] = new_page

    def change_username(self, new_username):
        self.username = new_username

    def get_changedusername(self):
        return self.username

    def change_img(self, new_image):
        self.where_image = new_image

    def get_changedimage(self):
        return self.where_image


    #something that could come soon.....
    def page_selected_thread(self, page_name):
        page_name.thread_start()
        

    def loading_page_thread(self):
        self.loading_page.update_progress(0)
        self.loading_page.deincomify()
        self.update()

    def infinite_loop(self, new_page):
        caligrapyhy = True
        while caligrapyhy:
            if new_page.get_percentage() >= 100:
                self.loading_page.on_closing()
                caligrapyhy = False


    #the long part
    def temp_tool(self, what, where, how=None):
        if what== 'modify' or what=='mod':
            if where== 'username' or where=='user':
                self.temp_username= how
                print(f'DONE {how}')
            elif where== 'passcode' or where=='pass':
                self.temp_enpasscode= how
                print(f'DONE {how}')
            elif where== 'birthday' or where=='birth':
                self.temp_birthday= how
                print(f'DONE {how}')
            elif where== 'description' or where=='desc':
                self.temp_description= how
                print(f'DONE {how}')
            elif where== 'language' or where== 'lang':
                self.temp_language= how
                print(f'DONE {how}')
            elif where== 'filestorage' or where=='file':
                self.temp_filestor= how
                print(f'DONE {how}')
            elif where== 'email' or where=='mail':
                self.temp_mail= how
                print(f'DONE {how}')
            else:
                print(f'how ({how})  --->   UNEXISTENT')
        
        elif what== 'return' or what=='obt':
            if where== 'username' or where=='user':
                return self.temp_username
            elif where== 'passcode' or where=='pass':
                return self.temp_enpasscode
            elif where== 'birthday' or where=='birth':
                return self.temp_birthday
            elif where== 'description' or where=='desc':
                return self.temp_description
            elif where== 'language' or where=='lang':
                return self.temp_language
            elif where== 'filestorage' or where=='file':
                return self.temp_filestor
            elif where== 'email' or where=='mail':
                return self.temp_mail
            else:
                print(f'where ({where})  --->   UNEXISTENT')

        elif what== 'reload' or 'reld':
            print('reloading all...')
            self.temp_username = ''
            self.temp_enpasscode = ''
            self.temp_birthday = ''
            self.temp_description = ''
            self.temp_filestor = ''
            self.temp_mail
            print('DONE')

#late project to make it faster
'''    class Temp_tool():
        def __init__(self, temp_username, temp_passcode, temp_birthday, temp_description, temp_lang):
            self.data_us= temp_username
            self.data_pas= temp_passcode
            self.data_birth= temp_birthday
            self.data_descr= temp_description
            self.data_lang= temp_lang

        
        def update_tempobj(self, what, how):
            what == how

        def'''


if __name__ == '__main__':
    app = Application(OUTPUT_PATH=OUTPUT_PATH)

    def on_closing():
        print('bye bye cruel world')
        app.destroy()

    app.protocol('WM_DELETE_WINDOW', on_closing)
    app.mainloop()
   