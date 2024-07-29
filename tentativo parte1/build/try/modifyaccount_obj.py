# [2024-DEV Stage 1/2]: refactor(account): enhance modifyaccount_obj.py with username validation
from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

class Modifyaccount(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame18"

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

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=self.save_modifications,
            relief="flat"
        )
        self.button_7.place(
            x=693.0,
            y=617.0,
            width=151.0,
            height=47.0
        )
        self.buttons_list.append(self.button_7)

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.controller.show_page('options'),
            relief="flat"
        )
        self.button_9.place(
            x=408.0,
            y=640.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_9)


        #TEXT
        self.name_rev= self.canvas.create_text(
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
            458.0,
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
            769.0,
            229.0,
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

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            579.0,
            368.0,
            image=self.image_image_6
        )
        self.images_list.append(self.image_6)

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            973.0,
            368.0,
            image=self.image_image_7
        )
        self.images_list.append(self.image_7)

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            492.0,
            495.0,
            image=self.image_image_8
        )
        self.images_list.append(self.image_8)

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            768.0,
            495.0,
            image=self.image_image_9
        )
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            1100.0,
            670.0,
            image=self.image_image_10
        )
        self.images_list.append(self.image_10)

        self.image_image_11 = PhotoImage(
            file=self.relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            652.0,
            359.0,
            image=self.image_image_11
        )
        self.images_list.append(self.image_11)

        self.image_image_12 = PhotoImage(
            file=self.relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            916.0,
            359.0,
            image=self.image_image_12
        )
        self.images_list.append(self.image_12)

        self.image_image_13 = PhotoImage(
            file=self.relative_to_assets("image_13.png"))
        self.image_13 = self.canvas.create_image(
            1052.0,
            495.0,
            image=self.image_image_13
        )
        self.images_list.append(self.image_13)

        self.image_image_14 = PhotoImage(
            file=self.relative_to_assets("image_14.png"))
        self.image_14 = self.canvas.create_image(
            535.0,
            587.0,
            image=self.image_image_14
        )
        self.images_list.append(self.image_14)


        #ENTRY
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            627.5,
            410.5,
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
            x=524.0,
            y=388.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_1)
        
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            907.5,
            410.5,
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
            x=804.0,
            y=388.0,
            width=207.0,
            height=43.0
        )
        self.entry_place_list.append(self.entry_2)

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            535.280029296875,
            535.199951171875,
            image=self.entry_image_3
        )
        self.images_list.append(self.entry_bg_3)
        self.entry_3 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_3.place(
            x=444.19999980926514,
            y=515.39990234375,
            width=182.16005897521973,
            height=37.60009765625
        )
        self.entry_place_list.append(self.entry_3)

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            769.360107421875,
            535.199951171875,
            image=self.entry_image_4
        )
        self.images_list.append(self.entry_bg_4)
        self.entry_4 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_4.place(
            x=678.2800779342651,
            y=515.39990234375,
            width=182.16005897521973,
            height=37.60009765625
        )
        self.entry_place_list.append(self.entry_4)

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            1003.440185546875,
            535.199951171875,
            image=self.entry_image_5
        )
        self.images_list.append(self.entry_bg_5)
        self.entry_5 = Entry(
            bd=0,
            font=('Russo One', 14),
            bg="#272932",
            fg="#fdf500",
            highlightthickness=0
        )
        self.entry_5.place(
            x=912.3601560592651,
            y=515.39990234375,
            width=182.16005897521973,
            height=37.60009765625
        )
        self.entry_place_list.append(self.entry_5)





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



    def save_modifications(self):
        new_username = self.entry_1.get().strip() if hasattr(self, 'entry_1') else ''
        new_email = self.entry_2.get().strip() if hasattr(self, 'entry_2') else ''
        
        from tkinter import messagebox
        if new_username:
            print(f"[Modify Account] Updating username to '{new_username}'")
            self.controller.change_username(new_username)
            if hasattr(self, 'name_rev'):
                self.canvas.itemconfig(self.name_rev, text=new_username)
            messagebox.showinfo("Account Settings", f"Profile successfully updated! New username: {new_username}")
            self.controller.show_page('options')
            return True
        else:
            messagebox.showinfo("Account Settings", "Account parameters saved.")
            self.controller.show_page('options')
            return True

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)