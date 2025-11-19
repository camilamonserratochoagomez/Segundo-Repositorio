# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ
# Caluclar el precio, subtotal y el IVA

import tkinter as tk
from tkinter import messagebox

def calcular_iva():
        cantidad=float(entrada_cantidad.get())
        precio=float(entrada_precio.get())
        iva=(cantidad*precio) *0.16
        etiqueta_resultado.config(text=f"IVA : ${iva:.2f}")

def calcular_subtotal():
        cantidad=float(entrada_cantidad.get())
        precio=float(entrada_precio.get())
        subtotal=cantidad*precio
        etiqueta_resultado.config(text=f"subtotal: ${subtotal:.2f}")

def calcular_total():
        cantidad=float(entrada_cantidad.get())
        precio=float(entrada_precio.get())
        iva=(cantidad*precio)*0.16
        total= iva+(cantidad*precio)

ventana=tk.Tk()
ventana.title("Calculo de ventas")
ventana.geometry("400x350")
ventana.resizable(False,False)

#ETIQUETAS Y CAJA DE TEXTO
etiqueta_cantidad=tk.Label(ventana,text="Cantidad de articulos")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad=tk.Entry(ventana,justify="center")
entrada_cantidad.pack(pady=5)

etiqueta_precio=tk.Label(ventana,text="Precio por articulo")
etiqueta_precio.pack(pady=5)

entrada_precio=tk.Entry(ventana,justify="center")
entrada_precio.pack(pady=10)

#BOTON DEL SUBTOTAL
boton_subtotal=tk.Button(ventana,text="Calcular subtotal ",command=calcular_subtotal,bg="#E2DCD6")
boton_subtotal.pack(pady=5)
#BOTON DEL IVA
boton_iva=tk.Button(ventana,text="IVA (16%)",command=calcular_iva,bg="#E2DCD6")
boton_iva.pack(pady=5)
#BOTON DE TOTAL DE LA COMPRA
boton_Total=tk.Button(ventana,text="Total de la compra",command=calcular_total,bg="#E2DCD6")
boton_Total.pack(pady=5)

#ETIQUETA PARA MOSTRAR RESULTADOS
etiqueta_cantidad=tk.Label(ventana,text="Resultado:")
etiqueta_cantidad.pack(pady=10)
etiqueta_resultado=tk.Label(ventana,text="")
etiqueta_resultado.pack()

ventana.mainloop()