from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

ventana = Tk()

class AdminPanel:

    def imagen():
        filename = askopenfilename()
        img = Image.open(filename)
        new_img = img.resize((300,200))
        render = ImageTk.PhotoImage(new_img)
        img1 = Label(ventana, image=render)
        img1.image = render
        img1.place(x=200, y=230)

    def mensaje():
        salir = messagebox.askquestion("Salir","¿Desea salir del sistema?")
        if salir == 'yes':
            ventana.quit()
            ventana.destroy()

    def about():
        messagebox.showinfo("Acerca del Sistema Supermark","Este programa fue desarrollado por Belu y Gus, cualquier otra información ingresar a http://plataforma.milprogramadores.com.ar/index.php")

    ventana.title("Sistema Supermark - Administrador")
    ventana.geometry('800x600')
    ventana.iconbitmap('./Interfaz/assets/frame2/carrito.ico')
    fondo = PhotoImage(file='./Interfaz/assets/frame2/super.gif')
    fondo1 = Label(ventana, image=fondo).place(x=0, y=0, relwidth=1,relheight=1 )
    menu1 = Menu(ventana)
    ventana.config(menu=menu1)

    usuario = Menu(menu1, tearoff=0)
    usuario.add_command(label="Nuevo Usuario ...", command=imagen)
    usuario.add_command(label="Modificar Usuario")
    usuario.add_command(label="Listar Usuarios")
    usuario.add_separator()
    usuario.add_command(label="Salir del sistema", command=mensaje)

    producto = Menu(menu1, tearoff=0)
    producto.add_command(label="Nuevo Producto ...")
    producto.add_command(label="Modificar Productos")
    producto.add_command(label="Listar Productos")

    venta = Menu(menu1, tearoff=0)
    venta.add_command(label="Listar Ventas")

    ayuda = Menu(menu1, tearoff=0)
    ayuda.add_command(label="Acerca de",command=about)

    menu1.add_cascade(label="Usuario",menu=usuario)
    menu1.add_cascade(label="Producto",menu=producto)
    menu1.add_cascade(label="Venta",menu=venta)
    menu1.add_cascade(label="Ayuda",menu=ayuda)

    ventana.mainloop()
