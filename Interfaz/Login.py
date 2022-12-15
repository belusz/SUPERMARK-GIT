from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

import sqlite3
from sqlite3 import Error

from forms.form_usuario import UsuarioPanel
from forms.form_usuario import UsuarioPanel
from forms.form_admin import *

#no funciona
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from SupermarkBDD.insert_bdd_supermarket import *



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

#verifico si el email ya existe en la bdd
def check_user(email):
    database = r"Supermark.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
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
        self.parent = parent
        parent.title("Bienvenido a Supermark")
        parent.geometry("1142x766")
        icono = PhotoImage(file="Interfaz/assets/carro.png")
        parent.iconphoto(False, icono)
        parent.resizable(False, False)

        self.email = tk.StringVar()
        self.clave = tk.StringVar()
        
        self.canvas = Canvas(
            parent,
            bg="#FFFFFF",
            height=766,
            width=1142,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file="Interfaz/assets/frame0/image_1.png")
        self.image_1 = self.canvas.create_image(572.0, 383.0, image=self.image_image_1)
        self.image_image_2 = PhotoImage(file="Interfaz/assets/frame0/image_2.png")
        self.image_2 = self.canvas.create_image(868.0, 384.0, image=self.image_image_2)
        self.canvas.create_text(
            190.0,
            170.0,
            anchor="nw",
            text="BIENVENIDO A ",
            fill="#FFFFFF",
            font=("Lato Regular", 32 * -1),
        )
        self.entry_image_1 = PhotoImage(file="Interfaz/assets/frame0/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            849.0, 102.0, image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.email,
        )
        self.entry_1.place(x=713.0, y=85.0, width=272.0, height=32.0)
        self.canvas.create_text(
            714.0,
            48.0,
            anchor="nw",
            text="Usuario (E-mail)",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )
        self.entry_image_2 = PhotoImage(file="Interfaz/assets/frame0/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            847.0, 184.0, image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.clave,
        )
        self.entry_2.place(x=711.0, y=167.0, width=272.0, height=32.0)
        self.entry_2.config(show="*")

        self.canvas.create_text(
            715.5568237304688,
            133.5064697265625,
            anchor="nw",
            text="Contraseña",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.button_image_1 = PhotoImage(file="Interfaz/assets/frame0/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_recuperacion(),
            relief="flat",
        )
        self.button_1.place(x=898.0, y=242.0, width=178.0, height=54.0)
        self.canvas.create_text(
            635.0,
            254.0,
            anchor="nw",
            text="¿Olvidó su contraseña?",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )
        self.button_image_2 = PhotoImage(file="Interfaz/assets/frame0/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_ventana(),
            relief="flat",
        )
        self.button_2.place(x=705.0, y=334.0, width=283.0, height=55.687255859375)
        self.button_image_3 = PhotoImage(file="Interfaz/assets/frame0/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_registro(),
            relief="flat",
        )
        self.button_3.place(x=699.0, y=504.0, width=283.0, height=55.68719482421875)
        self.canvas.create_text(
            772.0,
            429.0,
            anchor="nw",
            text="¿No tiene cuenta?",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )
        self.image_image_3 = PhotoImage(file="Interfaz/assets/frame0/image_3.png")
        self.image_3 = self.canvas.create_image(305.0, 394.0, image=self.image_image_3)
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
                # AdminPanel()
            else:
                toplevel = tk.Toplevel(self.parent)
                Cliente(toplevel).grid()
                # toplevel = tk.Toplevel(self.parent)
                # Cliente(toplevel).grid()
                UsuarioPanel()
        else:
            if self.email.get() == "" or self.clave.get() == "":
                tkinter.messagebox.showinfo("Error", "Usuario o Contraseña vacíos")
            else:
                tkinter.messagebox.showinfo(
                    "Error", "Usuario o Contraseña incorrecto", icon="error"
                )

    def abrir_recuperacion(self):
        toplevel = tk.Toplevel(self.parent)
        Recuperacion(toplevel).grid()

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


# Nueva interfaz registro

class Registro(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Registrarse")
        icono3 = PhotoImage(file="Interfaz/assets/frame1/registrar.png")
        parent.iconphoto(False, icono3)
        parent.geometry("1142x766")

        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.email = tk.StringVar()
        self.dni = tk.StringVar()
        self.fechanac = tk.StringVar()
        self.clave = tk.StringVar()
        self.clavecheck= tk.StringVar()
        self.direccion = tk.StringVar()
        self.tipo = tk.StringVar()

        self.canvas_registro = Canvas(
            parent,
            bg="#FFFFFF",
            height=766,
            width=1142,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas_registro.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file="Interfaz/assets/frame1/image_1.png")
        self.image_1 = self.canvas_registro.create_image(
            578.0, 383.0, image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(file="Interfaz/assets/frame1/entry_1.png")
        self.entry_bg_1 = self.canvas_registro.create_image(
            289.5, 154.0, image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , textvariable=self.nombre
        )
        self.entry_1.place(x=19.0, y=140.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            15.0,
            111.0,
            anchor="nw",
            text="Nombre\n",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_2 = PhotoImage(file="Interfaz/assets/frame1/entry_2.png")
        self.entry_bg_2 = self.canvas_registro.create_image(
            288.5, 226.0, image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , textvariable=self.apellido
        )
        self.entry_2.place(x=18.0, y=212.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            18.0,
            178.0,
            anchor="nw",
            text="Apellido",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_3 = PhotoImage(file="Interfaz/assets/frame1/entry_3.png")
        self.entry_bg_3 = self.canvas_registro.create_image(
            288.5, 291.0, image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.email
        )
        self.entry_3.place(x=18.0, y=277.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            17.0,
            248.0,
            anchor="nw",
            text="E-mail",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_4 = PhotoImage(file="Interfaz/assets/frame1/entry_4.png")
        self.entry_bg_4 = self.canvas_registro.create_image(
            290.5, 363.0, image=self.entry_image_4
        )
        self.entry_4 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.dni
        )
        self.entry_4.place(x=20.0, y=349.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            19.0,
            317.0,
            anchor="nw",
            text="DNI (Sólo números)",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_5 = PhotoImage(file="Interfaz/assets/frame1/entry_5.png")
        self.entry_bg_5 = self.canvas_registro.create_image(
            290.5, 438.0, image=self.entry_image_5
        )
        self.entry_5 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.fechanac
        )
        self.entry_5.place(x=20.0, y=424.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            17.0,
            391.0,
            anchor="nw",
            text="Fecha de Nacimiento (dd-mm-aa)\n",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_6 = PhotoImage(file="Interfaz/assets/frame1/entry_6.png")
        self.entry_bg_6 = self.canvas_registro.create_image(
            291.5, 510.0, image=self.entry_image_6
        )
        self.entry_6 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.direccion
        )
        self.entry_6.place(x=21.0, y=496.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            18.0,
            467.0,
            anchor="nw",
            text="Dirección",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_7 = PhotoImage(file="Interfaz/assets/frame1/entry_7.png")
        self.entry_bg_7 = self.canvas_registro.create_image(
            290.5, 575.0, image=self.entry_image_7
        )
        self.entry_7 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.tipo
        )
        self.entry_7.place(x=20.0, y=561.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            16.0,
            536.0,
            anchor="nw",
            text="Tipo de usuario (admin / cliente)",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_8 = PhotoImage(file="Interfaz/assets/frame1/entry_8.png")
        self.entry_bg_8 = self.canvas_registro.create_image(
            288.5, 647.0, image=self.entry_image_8
        )
        self.entry_8 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.clave
        )
        self.entry_8.place(x=18.0, y=633.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            13.0,
            604.0,
            anchor="nw",
            text="Clave",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.entry_image_9 = PhotoImage(file="Interfaz/assets/frame1/entry_9.png")
        self.entry_bg_9 = self.canvas_registro.create_image(
            853.5, 647.0, image=self.entry_image_9
        )
        self.entry_9 = Entry(
            self.canvas_registro, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=self.clavecheck
        )
        self.entry_9.place(x=583.0, y=633.0, width=541.0, height=26.0)

        self.canvas_registro.create_text(
            580.0,
            604.0,
            anchor="nw",
            text="Repetir Clave",
            fill="#000000",
            font=("Nokora Bold", 20 * -1),
        )

        self.button_image_1 = PhotoImage(file="Interfaz/assets/frame1/button_1.png")
        self.button_1 = Button(
            self.canvas_registro,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=parent.destroy,
            relief="flat",
        )
        self.button_1.place(x=687.0, y=686.0, width=283.0, height=55.68719482421875)

        self.button_image_2 = PhotoImage(file="Interfaz/assets/frame1/button_2.png")
        self.button_2 = Button(
            self.canvas_registro,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: add_user(self),
            relief="flat",
        )
        self.button_2.place(x=179.0, y=686.0, width=283.0, height=55.68719482421875)

        self.canvas_registro.create_rectangle(
            0.0, 20.0, 932.0, 86.0, fill="#AF0A08", outline=""
        )

        self.canvas_registro.create_text(
            15.0,
            35.0,
            anchor="nw",
            text="Por favor complete todos los campos para registrarse:",
            fill="#FFFFFF",
            font=("Nokora Black", 32 * -1),
        )
        
        #metodo para agregar usuario a la bdd
        def add_user(self):
            if check_user(self.email.get()):
                tkinter.messagebox.showinfo("Error", "E-mail ya asociado a un cliente, ingrese otro")
            else:
                if self.email.get() == "" or self.clave.get() == "" or self.nombre.get() == "" or self.apellido.get() == "" or self.dni.get() == "" or self.direccion.get() == "" or self.dni.get() == "" or self.fechanac.get() == "":
                    tkinter.messagebox.showinfo("Error", "Debe completar todos los campos")
                else:
                   if self.clave.get() == self.clavecheck.get():
                       #corregir este
                        usuario=[self.nombre.get(),self.apellido.get(),self.email.get(),self.dni.get(),self.fechanac.get(),self.clave.get(),self.direccion.get(),self.tipo.get()]
                        con=create_connection('Supermark.db')
                        create_usuarios(con,usuario)
                        tkinter.messagebox.showinfo("Éxito", "Registrado con éxito")
                   else:
                        tkinter.messagebox.showinfo("Error", "Las contraseñas no coinciden")
                    
        

        self.mainloop


    
        

class Recuperacion(ttk.Frame):
    def __init__(self, parent):
        
        super().__init__(parent, padding=(20))
        parent.title("Recuperacion de Contraseña")
        icono2 = PhotoImage(file="Interfaz/assets/frame1/recuperar.png")
        parent.iconphoto(False, icono2)
        parent.geometry("426x240")
        
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)  
        
        ttk.Label(self, text="Email:").grid(pady=5, row=0, column=0)
        ttk.Label(self, text="Ingrese nueva contraseña:").grid( pady=5, row=1, column=0)
        ttk.Label(self, text="Repetir nueva contraseña:").grid( pady=5, row=2, column=0)

        ttk.Entry(self, width=40).grid(padx=5, row=0, column=1)
        ttk.Entry(self, width=40).grid(padx=5, row=1, column=1)
        ttk.Entry(self, width=40).grid(padx=5, row=2, column=1)
        
        
        ttk.Button(self, text="Cancelar", command=parent.destroy).grid(padx=5, row=6, column=1)
        ttk.Button(self, text="OK", command=parent.destroy).grid(padx=5, row=6, column=0)
        
        def edit_password(self):
            pass
        
        

root = tk.Tk()
root.resizable(False, False)
App(root)
root.mainloop()
