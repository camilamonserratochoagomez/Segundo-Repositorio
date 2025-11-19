# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa que solicite a un cliente de un evento
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Venta de Aplicaciones")

# Agregar un campo de texto para ingresar el nombre del cliente
etiqueta_cliente = tk.Label(ventana, text="Nombre del Cliente:")
etiqueta_cliente.pack()
entrada_cliente = tk.Entry(ventana)
entrada_cliente.pack()

# Agregar un botón para confirmar la venta
boton_confirmar = tk.Button(ventana, text="Confirmar Venta", command=lambda: print("Venta realizada"))
boton_confirmar.pack()

# Iniciar la ventana
ventana.mainloop()