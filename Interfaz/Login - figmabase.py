from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import tkinter.messagebox
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\abelu\Documents\Python - Mil programadores salteños\PROYECTO SUPERMARK\SUPERMARK GIT\Interfaz\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def validate_user(email, clave):
    database = r"Supermark.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email = ? AND clave = ?", (email, clave))
    rows = cur.fetchall()
    return True if len(rows) > 0 else False


def validate_tipo_user(email):
    database = r"Supermark.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT tipo FROM usuarios WHERE email = ?", (email,))

    rows = cur.fetchall()

    return rows[0][0]


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent  # guardamos una referencia de la ventana ppal
        parent.title("Ventana Login")
        parent.geometry("400x200+100+100")
        icono=PhotoImage(file="Interfaz/assets/carro.png")
        self.parent.iconphoto(False,icono)
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(True, True)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=766,
            width=1142,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(572.0, 383.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(868.0, 384.0, image=image_image_2)

        self.canvas.create_text(
            190.0,
            170.0,
            anchor="nw",
            text="BIENVENIDO A ",
            fill="#FFFFFF",
            font=("Lato Regular", 32 * -1),
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(849.0, 102.0, image=entry_image_1)
        entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry_1.place(x=713.0, y=85.0, width=272.0, height=32.0)

        self.canvas.create_text(
            714.0,
            48.0,
            anchor="nw",
            text="Usuario",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(847.0, 184.0, image=entry_image_2)
        entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry_2.place(x=711.0, y=167.0, width=272.0, height=32.0)

        self.canvas.create_text(
            715.5568237304688,
            133.5064697265625,
            anchor="nw",
            text="Contraseña",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
        )
        button_1.place(x=898.0, y=242.0, width=178.0, height=54.0)

        self.canvas.create_text(
            635.0,
            254.0,
            anchor="nw",
            text="¿Olvidó su contraseña?",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
        )
        button_2.place(x=705.0, y=334.0, width=283.0, height=55.687255859375)

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
        )
        button_3.place(x=699.0, y=504.0, width=283.0, height=55.68719482421875)

        self.canvas.create_text(
            772.0,
            429.0,
            anchor="nw",
            text="¿No tiene cuenta?",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(305.0, 394.0, image=image_image_3)

        self.canvas.create_rectangle(
            140.0, 298.0, 240.0, 398.0, fill="#000000", outline=""
        )

    def validate_login(self):
        return validate_user(self.email.get(), self.clave.get())

    def abrir_ventana(self):
        # creamos la ventana secundaria
        # como padre indicamos la ventana principal (no usamos grid)
        if self.validate_login():
            if validate_tipo_user(self.email.get()) == "admin":
                toplevel = tk.Toplevel(self.parent)
                Administrador(toplevel).grid()
            else:
                toplevel = tk.Toplevel(self.parent)
                Cliente(toplevel).grid()
        else:
            tkinter.messagebox.showinfo("Error", "Usuario o Contraseña Incorrecta")

    def abrir_registro(self):
        toplevel = tk.Toplevel(self.parent)
        Registro(toplevel).grid()


class Cliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Ventana Cliente")
        parent.geometry("350x100+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()


class Administrador(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Ventana Administrador")
        parent.geometry("350x100+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()


class Registro(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Ventana Registro")
        parent.geometry("350x100+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()


root = tk.Tk()
App(root).grid()
root.mainloop()
