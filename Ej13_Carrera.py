# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa Nombre de las carreras

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
ventana=tk.Tk()
ventana.title("Lista desplagable con botones")
ventana.geometry("350x250")

etiqueta=tk.Label(ventana,text="Elige una opcion")
etiqueta.pack(pady=10)

opciones=[
    "ARH",
    "Arquitectura",
    "Comercio electronico",
    "Comercio internacional",
    "Construccion",
    "Mecatrononica",
    "Programacion"
]
ComboCarreras=ttk.Combobox(ventana, values=opciones, state="readonly")
ComboCarreras.pack(pady=5)

def mostrar_seleccion():
    seleccion= ComboCarreras.get()
    etiqueta_resultado.config(text=f"Seleccionesta: {seleccion}")

    ComboCarreras.bind("<<ComboboxSelected>>",mostrar_seleccion)
    etiqueta_resultado=tk.Label(ventana,text="Selecciona una carrera")
    etiqueta_resultado.pack(pady=20)

ventana.mainloop()