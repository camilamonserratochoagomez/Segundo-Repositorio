# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ
# Progrmas que hace tipo de cambios en dinero
import tkinter as tk
from tkinter import messagebox

def calcular_dolares():
    try:
        cantidad=float(entrada_cantidad.get())
        dolares=cantidad / 18.00
        etiqueta_resultado.config(text=f"Dolares: ${dolares:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresar su cantidad valida")

def calcular_Euros():
    try:
        cantidad=float(entrada_cantidad.get())
        euros=cantidad / 19.50
        etiqueta_resultado.config(text=f"euros: ${euros:.2f}")

    except ValueError:
        messagebox.showerror ("Error","Por favor ingresar su cantidad valida")

def calcular_Libras():
    try:
        cantidad=float(entrada_cantidad.get())
        libras=cantidad / 22.30
        etiqueta_resultado.config(text=f"libras: ${libras:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor iingresar su cantidad valida")

def calcular_Yenes():
    try:
        cantidad=float(entrada_cantidad.get())
        Yenes=cantidad / 0.12
        etiqueta_resultado.config(text=f"yenes: ${Yenes:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresar su cantidad valida")


#Creamos una ventana
ventana=tk.Tk()
ventana.title("Divisas")
ventana.geometry("400x350")
ventana.resizable(False,False)

#ETIQUETAS Y CAJAS DE TEXTO

#Etiquetas
etiqueta_cantidad=tk.Label(ventana,text="Cantidad")
etiqueta_cantidad.pack(pady=10)

#Caja de texto

entrada_cantidad=tk.Entry(ventana,justify="center")
entrada_cantidad.pack(pady=5)

#Boton de dolares

boton_Dolares=tk.Button(ventana,text="Dolares",command=calcular_dolares,bg="#E2DCD6")
boton_Dolares.pack(pady=5)

#Boton de euros
boton_euros=tk.Button(ventana,text="Euros",command=calcular_Euros,bg="#E2DCD6")
boton_euros.pack(pady=5)

#Boton de libras
boton_libras=tk.Button(ventana,text="Libras",command=calcular_Libras,bg="#E2DCD6")
boton_libras.pack(pady=5)

#Boton de yenes
boton_Yenes=tk.Button(ventana,text="Yenes",command=calcular_Yenes,bg="#E2DCD6")
boton_Yenes.pack(pady=5)

#ETIQUETA PARA MOSTRAR RESULTADOS
etiqueta_cantida=tk.Label(ventana,text="Resultado:")
etiqueta_cantida.pack(pady=10)
etiqueta_resultado=tk.Label(ventana,text="")
etiqueta_resultado.pack()

ventana.mainloop()