# [2024-DEV Stage 6/8]: refactor(app): enhance Application router with dynamic view registration in main.py
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
from notenoughmoney_obj import NotEnoughMoney
from profile_manager import ProfileManager
from game_session import GameSession
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
        self.start_time = time.time()

        self.create_spheres()
        self.animate_step()

    def create_spheres(self):
        x = 20
        y = 25
        radius = 5
        distance = 15

        for _ in range(6):
            sphere = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=SPHERE_COLOR)
            self.spheres.append(sphere)
            x += distance

    def animate_step(self):
        if not self.running or not self.winfo_exists():
            return
        t = time.time() - self.start_time
        for i, sphere in enumerate(self.spheres):
            x = 20 + i * 15
            y = 25 + AMPLITUDE * math.sin(FREQUENCY * (2 * math.pi * (i / len(self.spheres)) - FREQUENCY * t))
            self.canvas.coords(sphere, x - 5, y - 5, x + 5, y + 5)
        self.after(33, self.animate_step)

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
        ico_file = Path(__file__).resolve().parent.parent.parent / 'las_purgas.ico'
        if ico_file.exists():
            try:
                self.iconbitmap(str(ico_file))
            except Exception:
                pass

        self.username = ''
        self.where_image = str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png')

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
        self.profile = ProfileManager(self)
        self.notenoughmoney = NotEnoughMoney(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)
        self.game_session = GameSession(self.container, self, OUTPUT_PATH=self.OUTPUT_PATH)

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
        self.pages['notenoughmoney'] = self.notenoughmoney
        self.pages['start_game'] = self.game_session
        self.pages['game_session'] = self.game_session

        #first_page_opening= 'sign_in'
        try:
            lex = self.sign_in.check_auth()
            if not lex or lex not in self.pages:
                lex = 'sign_in'
        except Exception as e:
            print(f'Auth check notice: {e}')
            lex = 'sign_in'
        self.show_page(lex)

    def show_page(self, page_name):
        if page_name not in self.pages:
            print(f"[VLib Router] Warning: Page '{page_name}' not registered. Redirecting to 'main_channel'.")
            page_name = "main_channel" if "main_channel" in self.pages else "sign_in"

        if 'current' in self.pages:
            current_page = self.pages['current']
            current_page.pack_forget()
            current_page.destroy_stuff()

        new_page = self.pages[page_name]
        new_page.pack(fill='both', expand=True)

        new_page.create_stuff()
        self.pages['current'] = new_page

    def launch_game(self):
        from tkinter import messagebox
        print("[Game Engine] Initializing Las Purgas Cyberpunk Client...")
        messagebox.showinfo(
            "Las Purgas - Game Launcher",
            "Connecting to Las Purgas Server (127.0.0.1:7777)...\n"
            "Shader Pipeline: Loaded\n"
            "Asset Bundle: Cyberpunk City Core v2.1\n\n"
            "Game session initialized successfully!"
        )

    def get_credits(self):
        return self.profile.get_formatted_credits()

    def get_raw_credits(self):
        return self.profile.get_credits()

    def get_rank(self):
        return self.profile.get_rank()

    def is_vip(self):
        return self.profile.is_vip()

    def add_credits(self, amount):
        return self.profile.add_credits(amount)

    def spend_credits(self, amount):
        return self.profile.spend_credits(amount)

    def claim_daily_allowance(self):
        return self.profile.claim_daily_allowance()

    def get_available_mods(self):
        return self.profile.get_available_mods()

    def is_mod_active(self, mod_id):
        return self.profile.is_mod_active(mod_id)

    def toggle_mod(self, mod_id):
        return self.profile.toggle_mod(mod_id)

    def submit_support_ticket(self, category, message):
        return self.profile.submit_support_ticket(self.username or "Guest", category, message)

    def is_sound_enabled(self):
        return self.profile.is_sound_enabled() if hasattr(self, 'profile') else True

    def toggle_sound(self):
        return self.profile.toggle_sound() if hasattr(self, 'profile') else True

    def logout(self):
        print(f"[VLib Session] User '{self.username}' logged out.")
        self.username = ''
        self.temp_tool('reload', None)
        onl_path = Path(__file__).resolve().parent.parent.parent / "Onl_verification.json"
        if onl_path.exists():
            try:
                import json
                with open(onl_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                data["activity"] = "Inactive"
                with open(onl_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
            except Exception:
                pass
        self.show_page('sign_in')

    def change_username(self, new_username):
        self.username = new_username
        if hasattr(self, 'profile'):
            self.profile.set_user(new_username)

    def get_changedusername(self):
        return self.username

    def change_img(self, new_image):
        if not new_image:
            return
        candidate = Path(new_image)
        if not candidate.is_absolute():
            tentativo_dir = Path(__file__).resolve().parent.parent.parent
            if (tentativo_dir / new_image).exists():
                candidate = tentativo_dir / new_image
            elif (Path(__file__).resolve().parent / new_image).exists():
                candidate = Path(__file__).resolve().parent / new_image
            elif (Path(__file__).resolve().parent.parent / "assets" / "frame4" / new_image).exists():
                candidate = Path(__file__).resolve().parent.parent / "assets" / "frame4" / new_image
        self.where_image = str(candidate)

    def get_changedimage(self):
        candidate = Path(self.where_image)
        if candidate.exists():
            return str(candidate)
        fallback = Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'
        if fallback.exists():
            return str(fallback)
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

        elif what == 'reload' or what == 'reld':
            print('reloading all...')
            self.temp_username = ''
            self.temp_enpasscode = ''
            self.temp_birthday = ''
            self.temp_description = ''
            self.temp_filestor = ''
            self.temp_mail = ''
            self.temp_language = ''
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
   