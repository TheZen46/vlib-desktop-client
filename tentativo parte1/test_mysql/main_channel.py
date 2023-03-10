from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\partizione alessandro\programmi+\tentativo parte1\build\assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1253x767")
window.configure(bg = "#272932")


canvas = Canvas(
    window,
    bg = "#272932",
    height = 767,
    width = 1253,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    120.0,
    111.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg='#272932',
    activebackground='#272932',
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=124.0,
    y=547.0,
    width=61.07171630859375,
    height=21.08544921875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    bg='#272932',
    activebackground='#272932',
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1133.0,
    y=741.0,
    width=109.07171630859375,
    height=18.271484375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    bg='#272932',
    activebackground='#272932',
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=20.0,
    y=741.0,
    width=232.0,
    height=18.271484375
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    bg='#272932',
    activebackground='#272932',
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=114.0,
    y=441.0,
    width=82.0,
    height=22.1328125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    bg='#272932',
    activebackground='#272932',
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=84.0,
    y=338.0,
    width=142.10357666015625,
    height=19.37548828125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    bg='#272932',
    activebackground='#272932',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=92.0,
    y=234.0,
    width=142.0,
    height=22.0
)

canvas.create_rectangle(
    263.5,
    156.5,
    266.0,
    685.0,
    fill="#9370DB",
    outline="")

canvas.create_text(
    277.0,
    42.0,
    anchor="nw",
    text="Main Channel",
    fill="#FDF500",
    font=("ShareTechMono Regular", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    769.0,
    411.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    600.0,
    388.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1033.0,
    422.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    697.0,
    460.0,
    image=image_image_5
)

canvas.create_text(
    1105.0,
    96.0,
    anchor="nw",
    text="name_user",
    fill="#FDF500",
    font=("RussoOne Regular", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    769.0,
    231.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    506.0,
    387.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    880.0,
    421.0,
    image=image_image_8
)

canvas.create_text(
    648.0,
    449.0,
    anchor="nw",
    text="Amount",
    fill="#FDF500",
    font=("RussoOne Regular", 20 * -1)
)

canvas.create_text(
    551.0,
    377.0,
    anchor="nw",
    text="name",
    fill="#FDF500",
    font=("RussoOne Regular", 20 * -1)
)

canvas.create_text(
    984.0,
    411.0,
    anchor="nw",
    text="nomber",
    fill="#FDF500",
    font=("RussoOne Regular", 20 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    514.0,
    459.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1162.0,
    51.0,
    image=image_image_10
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    bg='#200628',
    activebackground='#200628',
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=674.0,
    y=585.0,
    width=237.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
