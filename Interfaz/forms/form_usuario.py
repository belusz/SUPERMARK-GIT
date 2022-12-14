import tkinter as tk
from tkinter.font import BOLD
import math
import forms.generic as utl

class UsuarioPanel:
        
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Sistema Supermark - Usuario')
        
        #  Obtenemos el largo y  ancho de la pantalla
        wtotal = math.trunc(self.ventana.winfo_screenwidth()/1.5)
        htotal = math.trunc(self.ventana.winfo_screenheight()/1.5)     
        size = str(wtotal) + "x" + str(htotal)
        self.ventana.geometry(size)
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,wtotal,htotal)
        logo =utl.leer_imagen("./Interfaz/assets/frame0/image_3.png", (math.trunc(wtotal/1.5), math.trunc(htotal/1.5)))

        # # frame_logo
        # #frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='black')
        # frame_logo = tk.Frame(self.ventana, bd=0, width=math.trunc(wtotal/2), relief=tk.SOLID, padx=10, pady=10,bg='wiith')
        # frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        # label = tk.Label( frame_logo, image=logo,bg='wiith' )
        # label.place(x=0,y=0,relwidth=1, relheight=1)
        # 
        # #frame_form
        # frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        # frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        # #frame_form
        # 
        # #frame_form_top
        # frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='wiith')
        # frame_form_top.pack(side="top",fill=tk.X)
        # title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        # title.pack(expand=tk.YES,fill=tk.BOTH)
        # #end frame_form_top

        self.ventana.mainloop()
