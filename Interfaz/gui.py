
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abelu\Documents\Python - Mil programadores salteños\PROYECTO SUPERMARK\SUPERMARK GIT\Interfaz\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

#Cambiar ícono y nombre de la ventana

#Con archivo .ico
#window.iconbitmap(r"C:\Users\abelu\Documents\Python - Mil programadores salteños\PROYECTO SUPERMARK\SUPERMARK GIT\Interfaz\supermark.ico")

icono=PhotoImage(file="Interfaz/carro.png")
window.iconphoto(False,icono)


window.title("Supermark")

window.geometry("1142x766")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 766,
    width = 1142,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    572.0,
    383.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    851.0,
    384.0,
    image=image_image_2
)

canvas.create_text(
    160.0,
    170.0,
    anchor="nw",
    text="BIENVENIDO A ",
    fill="#FFFFFF",
    font=("Lato Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    849.0,
    102.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=713.0,
    y=85.0,
    width=272.0,
    height=32.0
)

canvas.create_text(
    714.0,
    48.0,
    anchor="nw",
    text="Usuario",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    847.0,
    184.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=711.0,
    y=167.0,
    width=272.0,
    height=32.0
)

canvas.create_text(
    715.5568237304688,
    133.5064697265625,
    anchor="nw",
    text="Contraseña",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=898.0,
    y=242.0,
    width=178.0,
    height=54.0
)

canvas.create_text(
    635.0,
    254.0,
    anchor="nw",
    text="¿Olvidó su contraseña?",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=705.0,
    y=334.0,
    width=283.0,
    height=55.687255859375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=699.0,
    y=504.0,
    width=283.0,
    height=55.68719482421875
)

canvas.create_text(
    772.0,
    429.0,
    anchor="nw",
    text="¿No tiene cuenta?",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    276.0,
    434.0,
    image=image_image_3
)

canvas.create_rectangle(
    140.0,
    298.0,
    240.0,
    398.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
