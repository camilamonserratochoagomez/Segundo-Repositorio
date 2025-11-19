# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# dos ventanas que aparescan tu nombre y apellido
import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

# Función para abrir una ventana hija
def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Hija")
    ventana_hija.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija, text="Esta es una ventana hija", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

# Botón en la ventana principal para abrir la ventana hija
boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana Hija", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

# Iniciar el loop principal
ventana_principal.mainloop()