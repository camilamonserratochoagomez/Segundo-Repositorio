# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

Colores=""
ventana=tk.Tk()
ventana.title("Lista desplagable ComboBox")
ventana.geometry("300x200")

etiqueta=tk.Label(ventana,text="Elige una opcion")
etiqueta.pack(pady=10)

opciones=["Rojo","Verde","Azul","Amarrillo","Morado"]
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion= ComboColores.get()#Obtines la opcion seleccionada
    

    if seleccion =="Rojo":
        Colores.config(bg="red")
        Color="red"
    elif seleccion =="Verde":
        Colores.config(bg="green")
        Color="green"
    elif seleccion =="Azul":
        Colores.config(bg="blue")
        Color="blue"
    elif seleccion =="Amarrillo":
        Colores.config(bg="yellow")
        Color="yellow"
    else:
        Colores.config(bg="purple")
        Color="purple"
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}",fg=Color)
     
ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)
        
etiqueta_resultado=tk.Label(ventana,text="Selecciona el color")
etiqueta_resultado.pack(pady=20)

Colores=tk.Label(text="             ")
Colores.pack()


ventana.mainloop()

