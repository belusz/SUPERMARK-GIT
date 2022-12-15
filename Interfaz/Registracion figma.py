from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abelu\Documents\Python - Mil programadores salteños\PROYECTO SUPERMARK\SUPERMARK GIT\Interfaz\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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
    578.0,
    383.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    289.5,
    154.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=19.0,
    y=140.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    15.0,
    111.0,
    anchor="nw",
    text="Nombre\n",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    288.5,
    226.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=18.0,
    y=212.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    18.0,
    178.0,
    anchor="nw",
    text="Apellido",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    288.5,
    291.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=18.0,
    y=277.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    17.0,
    248.0,
    anchor="nw",
    text="E-mail",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    290.5,
    363.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=20.0,
    y=349.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    19.0,
    317.0,
    anchor="nw",
    text="DNI (Sólo números)",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    290.5,
    438.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=20.0,
    y=424.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    17.0,
    391.0,
    anchor="nw",
    text="Fecha de Nacimiento (dd-mm-aa)\n",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    291.5,
    510.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=21.0,
    y=496.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    18.0,
    467.0,
    anchor="nw",
    text="Dirección",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    290.5,
    575.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=20.0,
    y=561.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    16.0,
    536.0,
    anchor="nw",
    text="Tipo de usuario (admin / cliente)",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    288.5,
    647.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=18.0,
    y=633.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    13.0,
    604.0,
    anchor="nw",
    text="Clave",
    fill="#000000",
    font=("Nokora Bold", 20 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    853.5,
    647.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=583.0,
    y=633.0,
    width=541.0,
    height=26.0
)

canvas.create_text(
    580.0,
    604.0,
    anchor="nw",
    text="Repetir Clave",
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
    x=687.0,
    y=686.0,
    width=283.0,
    height=55.68719482421875
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
    x=179.0,
    y=686.0,
    width=283.0,
    height=55.68719482421875
)

canvas.create_rectangle(
    0.0,
    20.0,
    932.0,
    86.0,
    fill="#AF0A08",
    outline="")

canvas.create_text(
    15.0,
    35.0,
    anchor="nw",
    text="Por favor complete todos los campos para registrarse:",
    fill="#FFFFFF",
    font=("Nokora Black", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
