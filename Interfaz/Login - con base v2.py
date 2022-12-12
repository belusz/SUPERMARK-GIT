
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import tkinter.messagebox


def create_connection(db_file):
    """ create a database connection to the SQLite database
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
    database = r'Supermark.db'
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email = ? AND clave = ?", (email, clave))
    rows = cur.fetchall()
    return True if len(rows) > 0 else False


def validate_tipo_user(email):
    database = r'Supermark.db'
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT tipo FROM usuarios WHERE email = ?",(email,))
    
    rows = cur.fetchall()
    
    return rows[0][0]


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent    # guardamos una referencia de la ventana ppal
        parent.title("Bienvenido a Supermark - Login")
        parent.geometry("400x200+100+100")
        self.parent.iconbitmap("Interfaz/carro.ico")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(True, True)
        
        self.email = tk.StringVar()
        self.clave = tk.StringVar()
        
        ttk.Label(self, text="Inicie Sesion").grid()
        ttk.Label(self, text="Nombre Usuario: ").grid()
        ttk.Entry(self, textvariable=self.email).grid()
        ttk.Label(self, text="Contraseña: ").grid()
        ttk.Entry(self, textvariable=self.clave).grid() # show="*"
        ttk.Button(self, text="Ingresar", command=lambda: self.abrir_ventana()).grid()
        # ttk.Button(self, text="Ingresar", command=lambda: print(
        #     validate_user())).grid()
        ttk.Button(self, text="Registrarse", command=lambda: self.abrir_registro()).grid()
    
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