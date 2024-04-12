# [2024-DEV Stage 1/2]: refactor(image): implement pure Pillow rounded corners in personalizeimage_obj.py
from pathlib import Path
from tkinter import Pack, Label, filedialog, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, OptionMenu
from PIL import Image, ImageDraw, ImageOps
try:
    from colorama import Fore, Style
except ImportError:
    class _ColorDummy:
        def __getattr__(self, name): return ""
    Fore = _ColorDummy()
    Style = _ColorDummy()

try:
    import aggdraw
    AGGDRAW_AVAILABLE = True
except ImportError:
    aggdraw = None
    AGGDRAW_AVAILABLE = False

class PersonalizeImage(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH= OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame4"

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
        self.buttonclick = []



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
            command=lambda: self.reindernewpage(),
            relief="flat",
            state= 'disabled'
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
            command=lambda: self.controller.show_page("description_lang"),
            relief="flat"
        )
        self.button_8.place(
            x=687.0,
            y=618.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print('samurai1_png'),
            relief="flat"
        )
        self.button_9.place(
            x=420.0,
            y=258.0,
            width=52.28857421875,
            height=53.0
        )
        self.buttons_list.append(self.button_9)

        self.button_image_10 = PhotoImage(
            file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print('V1_png'),
            relief="flat"
        )
        self.button_10.place(
            x=562.0,
            y=259.0,
            width=52.0,
            height=51.0
        )
        self.buttons_list.append(self.button_10)

        self.button_image_11 = PhotoImage(
            file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print('CasualBG1_png'),
            relief="flat"
        )
        self.button_11.place(
            x=715.0,
            y=258.0,
            width=52.42919921875,
            height=52.288726806640625
        )
        self.buttons_list.append(self.button_11)

        self.button_image_12 = PhotoImage(
            file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print('LightVL1_png'),
            relief="flat"
        )
        self.button_12.place(
            x=854.57763671875,
            y=259.0,
            width=52.42236328125,
            height=52.45068359375
        )
        self.buttons_list.append(self.button_12)

        self.button_image_13 = PhotoImage(
            file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.open_filedialog(),
            relief="flat"
        )
        self.button_13.place(
            x=1066.0,
            y=397.5492858886719,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_13)

        self.button_image_14 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print(str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'), self.button_14),
            relief="flat"
        )
        self.button_14.place(
            x=515.71826171875,
            y=395.5492858886719,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_14)

        self.button_image_15 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print(str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'), self.button_15),
            relief="flat"
        )
        self.button_15.place(
            x=657.47900390625,
            y=396.7112731933594,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_15)

        self.button_image_16 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print(str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'), self.button_16),
            relief="flat"
        )
        self.button_16.place(
            x=810.859375,
            y=395.5492858886719,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_16)

        self.button_image_17 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print(str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'), self.button_17),
            relief="flat"
        )
        self.button_17.place(
            x=950.2958984375,
            y=396.7112731933594,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_17)

        self.button_image_18 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            bg='#200628',
            activebackground='#200628',
            highlightthickness=0,
            command=lambda: self.message_print(str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_9.png'), self.button_18),
            relief="flat"
        )
        self.button_18.place(
            x=1022.337890625,
            y=261.0,
            width=52.34521484375,
            height=53.450714111328125
        )
        self.buttons_list.append(self.button_18)



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

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            534.0,
            195.0,
            image=self.image_image_9
        )
        self.images_list.append(self.image_9)

        self.image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            704.0,
            528.0,
            image=self.image_image_10
        )
        self.images_list.append(self.image_10)


    def open_filedialog(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[('PNG Files', '*.png')],
        )

        print(self.file_path)

        image = Image.open(self.file_path)

        desired_height = 53.450714111328125
        desired_width = 52.34521484375

        aspect_ratio = image.width / image.height

        if aspect_ratio > 1:
            desired_height = round(desired_width / aspect_ratio)
        else:
            desired_width = round(desired_height * aspect_ratio)

        # Resize the image
        res_image = image.resize((int(desired_width), int(desired_height)), resample=Image.BILINEAR)

        # Desired corner radius (set to 17.43 pixels)
        corner_radius = 17.43

        # Apply rounded corners with a transparent background
        rounded_image = self.round_corner_jpg(res_image, corner_radius)

        # Save the modified image with rounded corners in isolated cache
        temp_dir = Path(__file__).resolve().parent.parent.parent / "local_temp_files"
        temp_dir.mkdir(parents=True, exist_ok=True)
        res_path = temp_dir / "res_image.png"
        rounded_image.save(str(res_path))

        new_img_12 = PhotoImage(
            file=str(res_path)
        )
        if len(self.buttonclick) == 0:
            print(f'{Fore.RED}no buttons clicked before{Style.RESET_ALL}')
        else:
            self.buttonclick[-1].configure(
                image=new_img_12
            )

        self.list_click.append(str(res_path))


    def round_corner_jpg(self, image, radius):
        """Generate an image with rounded corners and a transparent background."""
        width, height = image.size
        mask = Image.new('L', (width, height), 0)
        if AGGDRAW_AVAILABLE and aggdraw:
            try:
                draw = aggdraw.Draw(mask)
                brush = aggdraw.Brush('white')
                draw.pieslice((0, 0, radius * 2, radius * 2), 90, 180, None, brush)
                draw.pieslice((width - radius * 2, 0, width, radius * 2), 0, 90, None, brush)
                draw.pieslice((0, height - radius * 2, radius * 2, height), 180, 270, None, brush)
                draw.pieslice((width - radius * 2, height - radius * 2, width, height), 270, 360, None, brush)
                draw.rectangle((radius, radius, width - radius, height - radius), brush)
                draw.rectangle((radius, 0, width - radius, radius), brush)
                draw.rectangle((0, radius, radius, height - radius), brush)
                draw.rectangle((radius, height - radius, width - radius, height), brush)
                draw.rectangle((width - radius, radius, width, height - radius), brush)
                draw.flush()
            except Exception:
                draw = ImageDraw.Draw(mask)
                draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255)
        else:
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255)

        image = image.convert('RGBA')
        image.putalpha(mask)
        return image


    def saving_selectedimage(self):
        self.controller.change_img(self.list_click[-1])

    def reindernewpage(self):
        self.saving_selectedimage()
        self.set_temp_datas()
        self.controller.show_page('termsandconditions')

    def message_print(self, actual_button, button=None):
        print('button clicked')
        self.button_7.config(state= 'normal')
        self.list_click.append(actual_button)
        self.buttonclick.append(button)


    def set_temp_datas(self):
        self.controller.temp_tool(
            what= 'mod',
            where= 'file',
            how= self.list_click[-1]
        )

        

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



    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)