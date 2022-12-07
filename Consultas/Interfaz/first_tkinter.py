# hola_mundo_imp.py

import tkinter as tk
from tkinter import ttk


root = tk.Tk() # Objeto Tkinter
frame = ttk.Frame(root).grid() # 
ttk.Button(frame, text="Hola", command= lambda: print("Hola")).grid()
root.mainloop()