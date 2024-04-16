from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, BooleanVar
import json
import hashlib

#NOTA:
#NECCESSITà DI MIGLIORARE LE PRESTAZIONI DI CARICAMENTO, SERVE TROPPO 
# TEMPO PER CARICARE L'IMMAGINE


class Done(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame3"

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

        self.total_loading_progress = 9
        self.loading_progress = 0

    def create_stuff(self):
        self.boolean_var= False
        
        
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
            command=lambda: print('button clicked'),
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
            command=lambda: self.variation(),
            relief="flat"
        )
        self.button_7.place(
            x=747.0,
            y=618.0,
            width=237.0,
            height=45.0
        )
        self.buttons_list.append(self.button_7)
        #TEXT


        #IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            359.0,
            61.0,
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
            769.0,
            175.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            712.0,
            358.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            545.0,
            510.0,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)


        self.checkbutton = self.CustomCheckbutton(
            width = 50,
            height= 50,
            relative_to_assets=self.relative_to_assets,
            on_callback= self.check_on,
            off_callback= self.check_off
        )
        self.checkbutton.place(
            x=610.0,
            y=490.0
        )
        self.buttons_list.append(self.checkbutton)

    def write_data(self, filename, data):
        destinations = [
            Path(filename),
            Path(__file__).resolve().parent.parent.parent / filename
        ]
        for dest in destinations:
            try:
                with open(dest, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)
            except Exception:
                pass

    def calculate_sha256(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()

    def variation(self):
        username = self.controller.temp_tool(what='obt', where='user')
        if username:
            self.controller.change_username(username)
        if self.boolean_var == True:
            activity = 'Active'
            raw_pass = self.controller.temp_tool(what='obt', where='pass') or ''
            passcode = self.calculate_sha256(raw_pass)
            data = {"user": username, "pass": passcode, 'activity': activity}
            self.write_data("Onl_verification.json", data)
            print('data written')
            self.controller.show_page("main_channel")
        else:
            activity = 'Ghost'
            data = {"user": None, "pass": None, 'activity': activity}
            self.write_data("Onl_verification.json", data)
            print('data written')
            self.controller.show_page("main_channel")

    def check_on(self):
        print('on')
        self.boolean_var= True

    def check_off(self):
        print('off')
        self.boolean_var= False

    def get_total_loading_progress(self):
        return self.total_loading_progress

    def increment_loading_progress(self):
        self.loading_progress += 1
        #self.prorgess_percentege = (self.current_loading_progress / self.total_loading_progress) * 100


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