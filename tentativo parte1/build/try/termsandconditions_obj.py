# [2024-DEV Stage 1/2]: refactor(terms): load terms&conditions.txt into scrollable custom text box
from pathlib import Path
from tkinter import Pack, Checkbutton, BooleanVar, DISABLED, Scrollbar, IntVar, Label, filedialog, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, OptionMenu
from tkinter import ttk
from PIL import Image
from colorama import Fore, Style
import threading
from tkinter.constants import VERTICAL, LEFT, BOTH, NW
from sqlconn_basdata import Mycon_basdata
from dropboxconn import DropConn

class TermsAndConditions(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH
        
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame2"

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
        self.list_click = []
        self.checked_1 = IntVar()

        self.total_loading_progress = 14
        self.loading_progress = 0



    def create_stuff(self):
        self.boolean_dataz = False
        self.state = 'disabled'

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
        self.increment_loading_progress()

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
        self.increment_loading_progress()

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
        self.increment_loading_progress()

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
        self.increment_loading_progress()

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
        self.increment_loading_progress()

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
        self.increment_loading_progress()

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.change_page(),
            relief="flat",
            state= self.state
        )
        self.button_7.place(
            x=747.0,
            y=618.0,
            width=237.0,
            height=45.0
        )
        self.buttons_list.append(self.button_7)
        self.increment_loading_progress()

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page("personalizeimage"),
            relief="flat"
        )
        self.button_8.place(
            x=687.0,
            y=618.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)
        self.increment_loading_progress()



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
        self.increment_loading_progress()

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            769.0,
            411.0,
            image=self.image_image_3
        )
        self.images_list.append(self.image_3)
        self.increment_loading_progress()

        self.customtextbox = self.CustomTextBox(
            width=261,
            height=63,
            relative_to_assets= self.relative_to_assets,
            text_file= str(Path(__file__).resolve().parent.parent.parent / 'terms&conditions.txt'),
            font_size=7,
            font_style='Arial',
            bg_color='#200628',
            text_color='#fdf500',
            scrollbar_bg='#200628',
            scrollbar_trough='#fdf500'
        )
        self.customtextbox.place(
            x= 720.0,
            y= 300.0
        )
        self.buttons_list.append(self.customtextbox)
        self.increment_loading_progress()


        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            669.0,
            460.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)
        self.increment_loading_progress()

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            769.0,
            252.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)
        self.increment_loading_progress()


        #CHECK BUTTON
        self.checkbutton = self.CustomCheckbutton(
            width = 30,
            height= 30,
            relative_to_assets=self.relative_to_assets,
            on_callback= self.check_on,
            off_callback= self.check_off
        )
        self.checkbutton.place(
            x=595.0,
            y=444.0
        )
        self.buttons_list.append(self.checkbutton)
        self.increment_loading_progress()


    def thread_start(self):
        thread_st = threading.Thread(target= self.create_stuff)
        thread_st.start()

    def get_percentage(self):
        return ((self.loading_progress / self.total_loading_progress)*100)

    def get_acual_val(self):
        return self.loading_progress
        
    def get_total_loading_progress(self):
        return self.total_loading_progress

    def increment_loading_progress(self):
        self.loading_progress += 1
        self.update()


    def check_on(self):
        print('on')
        self.boolean_dataz = True
        self.state = 'active'  # Set the state of the button_7
        self.button_7.configure(state=self.state)  # Update the state of button_7


    def check_off(self):
        print('off')
        self.boolean_dataz = False
        self.state = 'disabled'  # Set the state of the button_7
        self.button_7.configure(state=self.state)  # Update the state of button_7


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

    def adj_database(self):
        s= self.controller.temp_tool(what= 'obt', where='file')
        if s== 'samurai1_png' or s== 'V1_png' or s== 'CasualBG1_png' or s== 'LightVL1_png':
            database_conn= Mycon_basdata(
                username= self.controller.temp_tool(what= 'obt', where='user'),
                password= self.controller.temp_tool(what= 'obt', where='pass'),
                birthday= self.controller.temp_tool(what= 'obt', where='birth'),
                language= self.controller.temp_tool(what= 'obt', where='lang'),
                description= self.controller.temp_tool(what= 'obt', where='desc'),
                filedat= self.controller.temp_tool(what= 'obt', where='file'),
                email= self.controller.temp_tool(what= 'obt', where='mail')
            )
            database_conn.write_and_modify()
            database_conn.close_all()
            self.controller.change_img(f'{s}.png')
        else:
            database_conn= Mycon_basdata(
                username= self.controller.temp_tool(what= 'obt', where='user'),
                password= self.controller.temp_tool(what= 'obt', where='pass'),
                birthday= self.controller.temp_tool(what= 'obt', where='birth'),
                language= self.controller.temp_tool(what= 'obt', where='lang'),
                description= self.controller.temp_tool(what= 'obt', where='desc'),
                filedat= self.controller.temp_tool(what= 'obt', where='user')+'_image',
                email= self.controller.temp_tool(what= 'obt', where='mail')
            )
            database_conn.write_and_modify()
            database_conn.close_all()
            Connection_drop= DropConn(
                image_transfer= self.controller.temp_tool(what= 'obt', where='file'),
                user= self.controller.temp_tool(what= 'obt', where='user')
            )
            Connection_drop.upload_image()
            get_box= DropConn()
            get_box.downlaod_onlyimage(name_file= (self.controller.temp_tool(what= 'obt', where='user')+'_image'))
            self.controller.change_img(new_image= 'local_downloaded_image.png')

    def change_page(self):
        self.adj_database()
        self.controller.show_page("done")

    class CustomCheckbutton(Canvas):
        def __init__(self, relative_to_assets, master=None, on_callback=None, off_callback=None, **kwargs):
            super().__init__(master, **kwargs)
            self.checked_image = PhotoImage(file=relative_to_assets('image_5_on.png'))
            self.unchecked_image = PhotoImage(file=relative_to_assets('image_5_off.png'))
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

    class CustomTextBox(Canvas):
        def __init__(self, master=None, text_file=None, relative_to_assets=None, width=200, height=100, font_size=12, font_style="", bg_color="white", text_color="black", scrollbar_bg="gray", scrollbar_trough="lightgray"):
            super().__init__(master, bg=bg_color, highlightthickness=0)
            self.width = width
            self.height = height

            # Create a text widget
            self.textbox = Text(self, font=(font_style, font_size), bg=bg_color, fg=text_color, wrap="word", borderwidth= 0)
            self.textbox.pack(fill="both", expand=True)

            self.textbox_image = PhotoImage(file=relative_to_assets('image_4.png'))
            self.create_image(0, 0, anchor="nw", image=self.textbox_image)
            self.create_rectangle(0, 0, self.width, self.height, outline="", fill=bg_color)

            if text_file:
                self.insert_text_from_file(text_file)

            self.bind("<Configure>", self.adjust_size)

        def adjust_size(self, event):
            bbox = self.bbox("all")
            if bbox:
                textbox_width = bbox[2] - bbox[0]
                textbox_height = bbox[3] - bbox[1]
                if textbox_width > self.width or textbox_height > self.height:
                    self.configure(scrollregion=self.bbox("all"))

        def insert_text_from_file(self, filename):
            try:
                with open(filename, "r", encoding="utf-8", errors="replace") as file:
                    text = file.read()
            except Exception:
                text = "Termini e Condizioni d'Uso: Accettazione dei Termini e Condizioni della piattaforma di gioco Las Purgas."
            self.textbox.delete("1.0", "end")
            self.textbox.insert("1.0", text)


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
#relative_to_assets('image_4.png')