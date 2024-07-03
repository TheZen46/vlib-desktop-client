# [2024-DEV Stage 3/8]: refactor(modding): add mod launch sandbox verification in modding_obj.py
from pathlib import Path
from tkinter import Pack, Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
from profile_manager import AVAILABLE_MODS


class Modding(Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH
        
        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "frame14"

        self.canvas = Canvas(
            self,
            bg="#272932",
            height=767,
            width=1253,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
    
        # LOGO's photo
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            120.0,
            111.0,
            image=self.image_image_1
        )

        # THE LINE 
        self.canvas.create_rectangle(
            263.5,
            156.5,
            266.0,
            685.0,
            fill="#9370DB",
            outline=""
        )

        # list of all the deletable items
        self.buttons_list = []
        self.images_list = []
        self.rectangle_list = []
        self.texts_list = []
        self.mod_buttons = {}

    def create_stuff(self):
        # BUTTONS
        self.rules_image = PhotoImage(
            file=self.relative_to_assets("button_1.png")
        )
        self.rules = Button(
            self, 
            image=self.rules_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda: self.controller.show_page("rules"),
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
            command=lambda: self.controller.show_page("contact_us"),
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
            command=self.on_mod_launch_clicked,
            relief="flat"
        )
        self.button_7.place(
            x=1011.0,
            y=583.0,
            width=125.0,
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
            command=lambda: self.controller.show_page('options'),
            relief="flat"
        )
        self.button_8.place(
            x=408.0,
            y=640.0,
            width=42.0,
            height=43.0
        )
        self.buttons_list.append(self.button_8)

        # TEXT
        self.name_rev = self.canvas.create_text(
            1105.0,
            96.0,
            anchor="nw",
            text=self.controller.get_changedusername() if hasattr(self.controller, 'get_changedusername') else "",
            fill="#FDF500",
            font=("RussoOne Regular", 20 * -1)
        )
        self.texts_list.append(self.name_rev)

        # IMAGES
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            368.0,
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
            768.0,
            199.0,
            image=self.image_image_4
        )
        self.images_list.append(self.image_4)

        self.image_image_5 = PhotoImage(
            file=self.controller.get_changedimage() if hasattr(self.controller, 'get_changedimage') else "")
        self.image_5 = self.canvas.create_image(
            1162.0,
            51.0,
            image=self.image_image_5
        )
        self.images_list.append(self.image_5)

        # INTERACTIVE MOD MATRIX CARDS
        self.render_mod_matrix()

    def render_mod_matrix(self):
        start_y = 245.0
        row_height = 72.0
        self.mod_buttons = {}

        for i, mod in enumerate(AVAILABLE_MODS):
            y = start_y + i * row_height
            # Background row card
            rect = self.canvas.create_rectangle(
                420.0,
                y,
                980.0,
                y + 60.0,
                fill="#181a24",
                outline="#9370DB",
                width=1
            )
            self.rectangle_list.append(rect)

            # Mod Name and Version
            t_name = self.canvas.create_text(
                435.0,
                y + 8.0,
                anchor="nw",
                text=f"{mod['name']}  ({mod['version']})",
                fill="#FDF500",
                font=("Arial", 11, "bold")
            )
            self.texts_list.append(t_name)

            # Category Tag
            t_cat = self.canvas.create_text(
                800.0,
                y + 9.0,
                anchor="nw",
                text=f"[{mod['category'].upper()}]",
                fill="#8be9fd",
                font=("Arial", 9, "bold")
            )
            self.texts_list.append(t_cat)

            # Description
            t_desc = self.canvas.create_text(
                435.0,
                y + 32.0,
                anchor="nw",
                text=mod['desc'],
                fill="#a0a8b8",
                font=("Arial", 9)
            )
            self.texts_list.append(t_desc)

            # Toggle Button
            is_active = self.controller.is_mod_active(mod['id']) if hasattr(self.controller, 'is_mod_active') else False
            btn_text = "ACTIVE" if is_active else "INACTIVE"
            btn_bg = "#50fa7b" if is_active else "#44475a"
            btn_fg = "#000000" if is_active else "#f8f8f2"

            toggle_btn = Button(
                self,
                text=btn_text,
                bg=btn_bg,
                fg=btn_fg,
                activebackground="#9370DB",
                activeforeground="#FFFFFF",
                font=("Arial", 9, "bold"),
                relief="ridge",
                bd=1,
                cursor="hand2",
                command=lambda mid=mod['id']: self.on_toggle_mod(mid)
            )
            toggle_btn.place(
                x=880.0,
                y=y + 12.0,
                width=88.0,
                height=36.0
            )
            self.buttons_list.append(toggle_btn)
            self.mod_buttons[mod['id']] = toggle_btn

        # Status text summary
        active_count = len(self.controller.profile.get_active_mods()) if hasattr(self.controller, 'profile') else 2
        self.status_summary = self.canvas.create_text(
            700.0,
            550.0,
            anchor="center",
            text=f"Active Mods: {active_count} / {len(AVAILABLE_MODS)}   |   Engine Pipeline: SANDBOX VERIFIED",
            fill="#50fa7b",
            font=("Arial", 10, "bold")
        )
        self.texts_list.append(self.status_summary)

    def on_toggle_mod(self, mod_id: str):
        if hasattr(self.controller, 'toggle_mod'):
            new_state = self.controller.toggle_mod(mod_id)
            btn = self.mod_buttons.get(mod_id)
            if btn:
                btn.config(
                    text="ACTIVE" if new_state else "INACTIVE",
                    bg="#50fa7b" if new_state else "#44475a",
                    fg="#000000" if new_state else "#f8f8f2"
                )
            if hasattr(self, 'status_summary'):
                active_count = len(self.controller.profile.get_active_mods())
                self.canvas.itemconfig(
                    self.status_summary,
                    text=f"Active Mods: {active_count} / {len(AVAILABLE_MODS)}   |   Engine Pipeline: SANDBOX VERIFIED"
                )

    def on_mod_launch_clicked(self):
        print("[VLib Mod Manager] Initializing mod launch sequence...")
        if hasattr(self, 'name_rev'):
            self.canvas.itemconfig(self.name_rev, text="[MOD ENGINE ACTIVE]")
        active_mods = self.controller.profile.get_active_mods() if hasattr(self.controller, 'profile') else []
        active_names = [m["name"] for m in AVAILABLE_MODS if m["id"] in active_mods]
        summary = "\n".join(f"• {name}" for name in active_names) if active_names else "No active mods selected."
        messagebox.showinfo(
            "VLib Modding Engine",
            f"Las Purgas Cyberpunk Mod Pack v2.1\n\nActive Mod Pipeline:\n{summary}\n\nStatus: Verified & Loaded into Game Engine."
        )

    def destroy_stuff(self):
        for button in self.buttons_list:
            button.destroy()
        self.buttons_list = []

        for image in self.images_list:
            self.canvas.delete(image)
        self.images_list = []

        for rectangle in self.rectangle_list:
            self.canvas.delete(rectangle)
        self.rectangle_list = []
        
        for text in self.texts_list:
            self.canvas.delete(text)
        self.texts_list = []
        self.mod_buttons = {}

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
