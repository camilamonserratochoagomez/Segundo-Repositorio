# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# Progrma que ejecute tu nombre y apellido
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Nombre Completo")
ventana.geometry("300x200")

# Etiqueta y cuadro de texto para el nombre
tk.Label(ventana, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

# Etiqueta y cuadro de texto para el apellido
tk.Label(ventana, text="Apellido:").pack(pady=5)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack(pady=5)

# Función que muestra el nombre completo
def mostrar_nombre():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    nombre_completo = f"{nombre} {apellido}"
    messagebox.showinfo("Nombre Completo", f"Tu nombre completo es: {nombre_completo}")

# Botón para mostrar el nombre
tk.Button(ventana, text="Mostrar el Nombre", command=mostrar_nombre).pack(pady=10)

# Iniciar el programa
ventana.mainloop()