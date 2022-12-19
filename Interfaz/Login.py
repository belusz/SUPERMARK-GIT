from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from datetime import date
import sqlite3
from sqlite3 import Error

#from forms.form_usuario import UsuarioPanel
#from forms.form_usuario import UsuarioPanel
#from forms.form_admin import *

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from SupermarkBDD.insert_bdd_supermarket import *
from Consultas.update_supermark import *
from Consultas.consultas_supermark import *

usrId = 1         

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
    global usrId
    if len(rows) != 0:
        usrId = rows[0][0]                                           
    return True if len(rows) > 0 else False

#verifico si el email ya existe en la bdd
def check_user(email):
    database = r"Supermark.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    rows = cur.fetchall()
    return True if len(rows) > 0 else False

#verifico si el producto ya existe
def check_product(codigo):
    database = r"Supermark.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
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
        screen_width=parent.winfo_screenwidth()
        screen_height=parent.winfo_screenheight()
        window_width=1142
        window_height=766
        x=(screen_width / 2) - (window_width / 2)
        y=(screen_height / 2) - (window_height / 2)
        parent.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
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
            else:
                toplevel = tk.Toplevel(self.parent)
                Cliente(toplevel).grid()   
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

   
#class Cliente(ttk.Frame):
#    def __init__(self, parent):
#        super().__init__(parent, padding=(20))
#        parent.title("Ventana Cliente")
#        parent.geometry("350x100+180+100")
#        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
#        parent.columnconfigure(0, weight=1)
#        parent.rowconfigure(0, weight=1)
#        parent.resizable(False, False)
#        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()

class Cliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent                       
        parent.title("Ventana Cliente")
        icon = PhotoImage(file="Interfaz/assets/frame1/cliente.png")
        parent.iconphoto(False, icon)
        parent.geometry('1536x864')
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        # Etiqueta y Spinbox
        etiqueta_temp = ttk.Label(self,text="Cantidad:")
        etiqueta_temp.place(x=5, y=270, width=60)
        self.spin_temp = ttk.Spinbox(self, from_=1, to=30, increment=1)
        self.spin_temp.set("1")    
        self.spin_temp.place(x=68, y=270, width=70)
        # Boton Agregar
        ttk.Button(self, text="Agregar", command=lambda:self.AddCarrito()).place(x=160, y=268, width=100)
        ttk.Button(self, text="Quitar", command=lambda:self.DelCarrito()).place(x=290, y=268, width=100)
        ttk.Button(self, text="FINALIZAR COMPRA", command=lambda:self.FinCompra()).place(x=200, y=598, width=250, height=30)
        
        #spin_temp.bind("<<Increment>>", temp_incrementada)
        #spin_temp.bind("<<Decrement>>", temp_disminuida)
                                           

        # definimos las columnas
        ttk.Label(self,text="PRODUCTOS",font=('Times', 18)).grid(row=0, column=0)
        columns = ('productoId','codigo', 'nombre', 'precio', 'stock', 'tipo', 'marca')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # definimos los encabezados
        self.tree.heading('productoId', text='ProductoId')                           
        self.tree.heading('codigo', text='Codigo')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('precio', text='Precio')
        self.tree.heading('stock', text='Stock')
        self.tree.heading('tipo', text='Tipo')
        self.tree.heading('marca', text='Marca')

        con=create_connection('Supermark.db')
        productos=select_all_productos(con)
        
        # agregar datos al treeview
        for contact in productos:
            self.tree.insert('', tk.END, values=contact)

        # para ejecutar un callback cuando se haga click en un item
        self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado())

        # agregar barra de scroll
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))


        # 2 tabla - definimos las columnas
        #title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        #title.pack(expand=tk.YES,fill=tk.BOTH)

        ttk.Label(self,text="MI CARRITO",font=('Times', 18)).place(x=630, y=305, width=500)

        columns2 = ('productoId','codigo', 'nombre', 'precio', 'cantidad', 'tipo', 'marca')
        self.tree2 = ttk.Treeview(self, columns=columns2, show='headings')
        self.tree2.place(x=1, y=350, width=1400)

        # definimos los encabezados
        self.tree2.heading('productoId', text='ProductoId')                                                   
        self.tree2.heading('codigo', text='Codigo')
        self.tree2.heading('nombre', text='Nombre')
        self.tree2.heading('precio', text='Precio')
        self.tree2.heading('cantidad', text='Cantidad')
        self.tree2.heading('tipo', text='Tipo')
        self.tree2.heading('marca', text='Marca')

        
        # para ejecutar un callback cuando se haga click en un item
        self.tree2.bind('<<TreeviewSelect>>', self.item_seleccionado())

        # agregar barra de scroll
        scrollbar2 = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree2.configure(yscroll=scrollbar2.set)
        scrollbar2.grid(row=1, column=2, sticky=(tk.N, tk.S))
        scrollbar2.place(x=1401, y=350, width=20, height= 230 )
        etiqueta_total = ttk.Label(self,text="Total:")
        etiqueta_total.place(x=5, y=600, width=60)

        self.total = ttk.Entry(self, justify=tk.RIGHT) #state="readonly",state=tk.DISABLED
        self.total.place(x=60, y=600, width=100)
        self.totalxprod = 0
        self.total.insert(0,self.totalxprod)                                                    
    def AddCarrito(self):
        carritos = []
        carritos.append(self.tree.item(self.tree.selection())['values'][0],)
        carritos.append(self.tree.item(self.tree.selection())['values'][1],)
        carritos.append(self.tree.item(self.tree.selection())['values'][2],)
        carritos.append(self.tree.item(self.tree.selection())['values'][3],)
        carritos.append(self.spin_temp.get(),)
        carritos.append(self.tree.item(self.tree.selection())['values'][5],)
        carritos.append(self.tree.item(self.tree.selection())['values'][6],)
        self.tree2.insert('', tk.END, values=carritos)
        self.spin_temp.set("1")
        self.totalxprod = self.totalxprod + (float(carritos[4]) * float(carritos[3]))
        self.total.delete(0, tk.END)
        self.total.insert(0,self.totalxprod)
        #self.detalleprod.append(self.tree.item(self.tree.selection())['values'][1],)
    def DelCarrito(self):
        if len(self.tree2.selection()) != 0:
            a=(self.tree2.item(self.tree2.selection())['values'][3],)
            b=(self.tree2.item(self.tree2.selection())['values'][4],)
            #c=(self.tree2.item(self.tree2.selection())['values'][0])
            self.totalxprod = self.totalxprod - (float(a[0])*float(b[0]))
            self.tree2.delete(self.tree2.selection())
            self.total.delete(0, tk.END)
            self.total.insert(0,self.totalxprod)
            #self.detalleprod.remove(c)                     
    def item_seleccionado(self):
        item = self.tree.item(self.tree.selection())['text']
        item2 = self.tree.item(self.tree.selection())['values']
        print(item)
        print(item2)

    def FinCompra(self):
        con=create_connection('Supermark.db')
        tarjetas=select_all_tarjetas(con,(usrId,))
        if self.totalxprod == 0:
            tkinter.messagebox.showinfo("Error","Para finalizar la compra debe agregar al menos un producto al carrito.")
        else:
            if len(tarjetas) == 0:
                toplevel = tk.Toplevel(self.parent)
                Tarjeta(toplevel).grid()
            else:
                self.Generar_comprobante()              
                tkinter.messagebox.showinfo("Sistema Supermark","La compra se realizo correctamente. En las porximas 48 hs recibirá sus productos.")

    def Generar_comprobante(self):
        comprobante = ["B",date.today(),self.totalxprod,usrId,1]
        con=create_connection('Supermark.db')
        create_comprobantes(con,comprobante)
        comprobanteId = select_comprobanteId(con)
        
        #create_comprobantes(con,comprobante)

        #comprobantes=select_all_tarjetas(con,(usrId,))
        for i in range(len(self.tree2.get_children())):
            item_count = self.tree2.get_children()
            #self.totalprod.append(self.tree2.item(item_count[i])['values'][0],)
            #self.totalprod.append(self.tree2.item(item_count[i])['values'][3],)
            #self.totalprod.append(self.tree2.item(item_count[i])['values'][4],)
            #print(self.totalprod)
            dcantidad = self.tree2.item(item_count[i])['values'][4]
            dprecio = self.tree2.item(item_count[i])['values'][3]
            dproducto = self.tree2.item(item_count[i])['values'][0]
            detalle_compra = [int(dcantidad),float(dprecio),int(dproducto),int(comprobanteId[0][0])]
            create_detalles_compra(con, detalle_compra)  

            dstock = consulta_stock(con,str(dproducto))
            update_stock(con,int(dstock[0])-int(dcantidad),int(dproducto))
            #cantidad de registro
            #print(len(self.tree2.get_children()))
        #self.detalleprod                                         

class Administrador(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent=parent
        parent.title("Ventana Administrador")
        icon = PhotoImage(file="Interfaz/assets/frame1/admin.png")
        parent.iconphoto(False, icon)
        parent.geometry("800x600")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        ttk.Button(self, text="Nuevo Producto", command=lambda: self.abrirRegistroProducto()).grid()
        #ttk.Button(self, text="Modificar Producto", command=self.editProducto()).grid()
        ttk.Button(self, text="Listar Productos", command=self.verProductos).grid()
        ttk.Button(self, text="Listar Ventas", command=self.verVentas).grid()
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()

    def abrirRegistroProducto(self):
        toplevel = tk.Toplevel(self.parent)
        Producto(toplevel).grid()
        
    def verProductos(self):
        toplevel = tk.Toplevel(self.parent)
        ListaProducto(toplevel).grid()
    
    def verVentas(self):
        toplevel = tk.Toplevel(self.parent)
        ListaVentas(toplevel).grid()
        

class ListaProducto(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        #self.parent = parent                       
        parent.title("Listado de Productos")
        icon = PhotoImage(file="Interfaz/assets/frame1/cliente.png")
        parent.iconphoto(False, icon)
        parent.geometry('1536x864')
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        self.codigo = tk.StringVar()
        self.nombre = tk.StringVar()
        self.precio = tk.StringVar()
        self.stock = tk.StringVar()
        self.tipo = tk.StringVar()
        self.marca = tk.StringVar()
        ttk.Label(self, text="Código:").grid( pady=5, row=0, column=0)
        ttk.Label(self, text="Nombre:").grid( pady=5, row=1, column=0)
        ttk.Label(self, text="Precio:").grid( pady=5, row=2, column=0)
        ttk.Label(self, text="Stock:").grid( pady=5, row=3, column=0)
        ttk.Label(self, text="Marca:").grid( pady=5, row=4, column=0)
        ttk.Label(self, text="Tipo:").grid( pady=5, row=5, column=0)
         
        ttk.Entry(self, width=40, textvariable=self.codigo).grid(padx=5, row=0, column=1)
        ttk.Entry(self, width=40, textvariable=self.nombre).grid(padx=5, row=1, column=1)
        ttk.Entry(self, width=40, textvariable=self.precio).grid(padx=5, row=2, column=1)
        ttk.Entry(self, width=40, textvariable=self.stock).grid(padx=5, row=3, column=1)
        ttk.Entry(self, width=40, textvariable=self.marca).grid(padx=5, row=4, column=1)
        self.tipo = ttk.Combobox(parent,state="readonly",values=["Conservas","Harinas","Pastas y Salsas","Snacks","Arroz y Legumbres","Bebidas","Lácteos"])
        self.tipo.place(x=75, y=170, width=248 )
        
        # Boton Agregar
        ttk.Button(self, text="Editar", command=lambda:self.SelectProduct()).place(x=5, y=200, width=150, height=30)
        ttk.Button(self, text="Guardar", command=lambda:self.EditProduct()).place(x=160, y=200, width=150, height=30)
        
        # definimos las columnas
        columns = ('productoId','codigo', 'nombre', 'precio', 'stock', 'tipo', 'marca')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        #self.tree.grid(row=15, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.tree.place(x=1, y=280, width=1200)

        ## definimos los encabezados
        self.tree.heading('productoId', text='ProductoId')                           
        self.tree.heading('codigo', text='Codigo')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('precio', text='Precio')
        self.tree.heading('stock', text='Stock')
        self.tree.heading('tipo', text='Tipo')
        self.tree.heading('marca', text='Marca')

        con=create_connection('Supermark.db')
        productos=select_all_productos(con)
        
        # agregar datos al treeview
        for contact in productos:
            self.tree.insert('', tk.END, values=contact)

    def SelectProduct(self):
        print(self.tree.item(self.tree.selection())['values'][0])
        self.codigo.set(self.tree.item(self.tree.selection())['values'][1])
        self.nombre.set(self.tree.item(self.tree.selection())['values'][2])
        self.precio.set(self.tree.item(self.tree.selection())['values'][3])
        self.stock.set(self.tree.item(self.tree.selection())['values'][4])
        self.tipo.set(self.tree.item(self.tree.selection())['values'][5])
        self.marca.set(self.tree.item(self.tree.selection())['values'][6])

    def EditProduct(self):
        if self.codigo.get() == "" or self.nombre.get() == "" or self.precio.get() == "" or self.stock.get() == "" or self.tipo.get() == "" or self.marca.get() == "":
                tkinter.messagebox.showinfo("Error", "Debe completar todos los campos")
        else:
            code = self.tree.item(self.tree.selection())['values'][1]
            if ( (str(self.codigo.get()) != str(code )) and check_product(self.codigo.get())):
                    tkinter.messagebox.showinfo("Error", "El codigo ya existe, ingrese otro")
            else:
                con=create_connection('Supermark.db')
                id_num = self.tree.item(self.tree.selection())['values'][0]
                tipo=select_tipoid(con,(self.tipo.get(),))
                update_producto(con,self.codigo.get(),self.nombre.get(),self.precio.get(),self.stock.get(),tipo[0],self.marca.get(),id_num)
                tkinter.messagebox.showinfo("Éxito", "El Producto fue modificado.")
                self.codigo.set("")
                self.nombre.set("")
                self.precio.set("")
                self.stock.set("")
                self.tipo.set("")
                self.marca.set("")
                productos=select_all_productos(con)
                self.tree.delete(*self.tree.get_children())
                for contact in productos:
                    self.tree.insert('', tk.END, values=contact)
            

class Producto(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Registrar Producto")
        icono3 = PhotoImage(file="Interfaz/assets/frame1/registrar.png")
        parent.iconphoto(False, icono3)
        parent.geometry("1142x766")

        self.codigo = tk.StringVar()
        self.nombre = tk.StringVar()
        self.precio = tk.StringVar()
        self.stock = tk.StringVar()
        #self.tipo = tk.StringVar()
        self.marca = tk.StringVar()
        
        ttk.Label(self, text="Código:").grid(pady=5, row=0, column=0)
        ttk.Label(self, text="Nombre:").grid( pady=5, row=1, column=0)
        ttk.Label(self, text="Precio:").grid( pady=5, row=2, column=0)
        ttk.Label(self, text="Stock:").grid( pady=5, row=3, column=0)
        ttk.Label(self, text="Marca:").grid( pady=5, row=4, column=0)
        ttk.Label(self, text="Tipo:").grid( pady=5, row=5, column=0)
        
        ttk.Entry(self, width=40, textvariable=self.codigo).grid(padx=5, row=0, column=1)
        ttk.Entry(self, width=40, textvariable=self.nombre).grid(padx=5, row=1, column=1)
        ttk.Entry(self, width=40, textvariable=self.precio).grid(padx=5, row=2, column=1)
        ttk.Entry(self, width=40, textvariable=self.stock).grid(padx=5, row=3, column=1)
        ttk.Entry(self, width=40, textvariable=self.marca).grid(padx=5, row=4, column=1)
        self.tipo = ttk.Combobox(parent,state="readonly",values=["Conservas","Harinas","Pastas y Salsas","Snacks","Arroz y Legumbres","Bebidas","Lácteos"])
        self.tipo.place(x=111, y=170, width=248 )
        
        ttk.Button(self, text="Cancelar", command=parent.destroy).grid(padx=5, row=6, column=1)
        ttk.Button(self, text="Finalizar", command=lambda: self.add_producto()).grid(padx=5, row=6, column=0)
        
    def add_producto(self):
        if check_product(self.codigo.get()):
            tkinter.messagebox.showinfo("Error", "El producto ya existe, ingrese otro")
        else:
            if self.codigo.get() == "" or self.nombre.get() == "" or self.precio.get() == "" or self.stock.get() == "" or self.tipo.get() == "" or self.marca.get() == "" :
                tkinter.messagebox.showinfo("Error", "Debe completar todos los campos")
            else: 
                  con=create_connection('Supermark.db')
                  tipo=select_tipoid(con,(self.tipo.get(),))                    
                  producto=[self.codigo.get(),self.nombre.get(),self.precio.get(),self.stock.get(),tipo[0],self.marca.get()]
                  create_productos(con,producto)
                  tkinter.messagebox.showinfo("Éxito", "Producto agregado con éxito")
                      
            
                            

# Nueva interfaz registro cliente

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
            text="Fecha de Nacimiento (AAAA-MM-DD)\n",
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
        
        self.email = tk.StringVar()
        self.clave = tk.StringVar()
        self.clave2 = tk.StringVar()
        
        ttk.Label(self, text="Email:").grid(pady=5, row=0, column=0)
        ttk.Label(self, text="Ingrese nueva contraseña:").grid( pady=5, row=1, column=0)
        ttk.Label(self, text="Repetir nueva contraseña:").grid( pady=5, row=2, column=0)

        ttk.Entry(self, width=40, textvariable=self.email).grid(padx=5, row=0, column=1)
        ttk.Entry(self, width=40, textvariable=self.clave).grid(padx=5, row=1, column=1)
        ttk.Entry(self, width=40, textvariable=self.clave2).grid(padx=5, row=2, column=1)
        
        
        ttk.Button(self, text="Cancelar", command=parent.destroy).grid(padx=5, row=6, column=1)
        ttk.Button(self, text="OK", command=lambda: self.edit_password()).grid(padx=5, row=6, column=0)
        
        
        
    #chequear
    def edit_password(self):
        if self.email.get() == "" or self.clave.get() == "" or self.clave2.get() == "":
                tkinter.messagebox.showinfo("Error", "Debe completar todos los campos")
        else:
            if not check_user(self.email.get()):
                tkinter.messagebox.showinfo("Error", "E-mail no existente en la base de datos, ingrese otro")    
            else:
                if self.clave.get() == self.clave2.get():
                    con=create_connection('Supermark.db')
                    id_tupla=select_userid(con,(self.email.get(),))
                    id_num=id_tupla[0]
                    update_usuarios_clave(con,(self.clave.get(),id_num))
                    tkinter.messagebox.showinfo("Éxito", "Contraseña restablecida")
                else:
                    tkinter.messagebox.showinfo("Error", "Las contraseñas no coinciden")       
     
     

class Tarjeta(ttk.Frame):
    def __init__(self, parent):
        
        super().__init__(parent, padding=(20))
        parent.title("Agregar Tarjeta")
        icono2 = PhotoImage(file="Interfaz/assets/frame2/tarjeta.png")
        parent.iconphoto(False, icono2)
        parent.geometry("426x240")
        
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)  
        
        self.numero = tk.StringVar()
        self.banco = tk.StringVar()
        self.titular = tk.StringVar()
        self.fechaCaducidad = tk.StringVar()
        self.pin = tk.StringVar()
        
        
        ttk.Label(self, text="Numero:").grid(pady=5, row=0, column=0)
        ttk.Label(self, text="Banco:").grid( pady=5, row=1, column=0)
        ttk.Label(self, text="Titular:").grid( pady=5, row=2, column=0)
        ttk.Label(self, text="Fecha de Caducidad:").grid( pady=5, row=3, column=0)
        ttk.Label(self, text="Codigo de Seguridad:").grid( pady=5, row=4, column=0)

        ttk.Entry(self, width=40, textvariable=self.numero).grid(padx=5, row=0, column=1)
        ttk.Entry(self, width=40, textvariable=self.banco).grid(padx=5, row=1, column=1)
        ttk.Entry(self, width=40, textvariable=self.titular).grid(padx=5, row=2, column=1)
        ttk.Entry(self, width=40, textvariable=self.fechaCaducidad).grid(padx=5, row=3, column=1)
        ttk.Entry(self, width=40, textvariable=self.pin).grid(padx=5, row=4, column=1)
        
        
        ttk.Button(self, text="Cancelar", command=parent.destroy).grid(padx=5, row=6, column=1)
        ttk.Button(self, text="Finalizar", command=lambda: self.add_tarjeta()).grid(padx=5, row=6, column=0)

    def add_tarjeta(self):
        if self.numero.get() == "" or self.banco.get() == "" or self.titular.get() == "" or self.fechaCaducidad.get() == "" or self.pin.get() == "":
            tkinter.messagebox.showinfo("Error", "Debe completar todos los campos")
        else:
            tarjeta=[self.numero.get(),self.banco.get(),self.titular.get(),self.fechaCaducidad.get(),usrId]
            con=create_connection('Supermark.db')
            create_tarjetas(con,tarjeta)
            tkinter.messagebox.showinfo("Éxito", "Tarjeta registrada con éxito")                           
                              
class ListaVentas(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        #self.parent = parent                       
        parent.title("Listado de Ventas")
        icon = PhotoImage(file="Interfaz/assets/frame1/cliente.png")
        parent.iconphoto(False, icon)
        parent.geometry('1536x864')
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        
        # definimos las columnas
        columns = ('comprobante', 'fecha', 'usuario', 'producto', 'cantidad', 'precio','total')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH,expand=1)
        self.tree.column("comprobante",minwidth=0,width=60,anchor=CENTER) 
        self.tree.column("fecha",minwidth=0,width=60,anchor=CENTER) 
        self.tree.column("usuario",minwidth=0,width=200) 
        self.tree.column("cantidad",minwidth=0,width=60,anchor=CENTER) 
        self.tree.column("precio",minwidth=0,width=60, anchor="e") 
        self.tree.column("producto",minwidth=0,width=350) 
        self.tree.column("total",minwidth=0,width=60, anchor="e") 

        ## definimos los encabezados
        self.tree.heading('comprobante', text='Comprobante')                           
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('usuario', text='Usuario')
        self.tree.heading('producto', text='Producto')
        self.tree.heading('cantidad', text='Cantidad')
        self.tree.heading('precio', text='Precio')
        self.tree.heading('total', text='Total')
        
        con=create_connection('Supermark.db')
        ventas=select_all_comprobantes(con)
        
        # agregar datos al treeview
        for contact in ventas:
            self.tree.insert('', tk.END, values=contact)

root = tk.Tk()
root.resizable(False, False)
App(root)
root.mainloop()
