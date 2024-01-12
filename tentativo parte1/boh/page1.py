from pathlib import Path
import tkinter as tk




class Page1(tk.Frame):
    def __init__(self, parent, controller, OUTPUT_PATH):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.OUTPUT_PATH = OUTPUT_PATH

        self.ASSETS_PATH = Path(__file__).resolve().parent.parent / "build" / "assets" / "frame8"

        self.canvas = tk.Canvas(
            self,
            bg = "#272932",
            height=767,
            width=1253,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
        
        self.canvas.place(x = 0, y = 0)
        image_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            120.0,
            111.0,
            image=image_image_1
        )


        # Create widgets for Page 1


        self.button_image = tk.PhotoImage(
            file = self.relative_to_assets("button_1.png")
        )

        self.button = tk.Button(
            self, 
            image= self.button_image,
            borderwidth=0,
            bg='#272932',
            activebackground='#272932',
            command=lambda:  controller.show_page("Page2"),
            relief="flat"
            )

        self.button.place(
            x=124.0,
            y=547.0,
            width=61.07171630859375,
            height=21.08544921875
        )


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
