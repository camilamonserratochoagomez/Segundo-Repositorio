# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ
# Programar que muestre una ventana,en el cual 
# Progrma que hace descuento, IVA y Total

#Importamos la biblioteca tkinter,que permite crear interfaces graficas en Python
import tkinter as tk
from tkinter import messagebox # messagebox sirve para mostrar cuadros de dialogo(alerta,errores,etc)

#FUNCIONES PRINCIPALES

#Funcion para calcular el IVA (Impuesto al valor Agregado 16%)
def calcular_iva():
    try:
        # Obtenemos el valor que el usuario escribio en la caja de texto
        cantidad=float(entrada_cantidad.get()) #Convertimos el texto a numeros decimal

        #Calculamos el 16% de IVA
        iva=cantidad*0.16

        #Mostramos el resultado en la etiqueta de resultado
        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}")

    #Si el usuario no ingresa un munero, mostramos un mensaje de error
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida.")

#Funcion para calcular en 10% de descuento
def calcular_descuento():
    try:
        #Obtenemos el valor ingresado por el usuario
        cantidad=float(entrada_cantidad.get())

        #Calculamos el 10% de descuento
        descuento=cantidad*0.10

        #Mostramos el resultado en la etiqueta
        etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad valida.")

#Funcion para calcular el total a pagar (considerando IVA y descuento)
def calcular_total():
    try:
        cantidad=float(entrada_cantidad.get())

        #Calcular IVA y descuento
        iva = cantidad * 0.16
        descuento = cantidad * 0.10

        # Total = cantidad original + IVA - descuento
        total = cantidad + iva - descuento

        #Mostramos el total en pantalla
        etiqueta_resultado.config(text=f"total a pagar: ${total:.2f}")

    except ValueError:
        messagebox.showerror("Error","Porfavor ingresar una cantidad valida")

#INGRESAR GRAFICA DE LA VENTANA PRINCIPAL

#Creamos la ventana principal
ventana=tk.Tk() #Inicia la aplicacion grafica
ventana.title("Calcular IVA yDescuento")# Titulo de la ventana
ventana.geometry("300x250") #Tamaño (anchox alto)
ventana.resizable(False,False) #Evitar que el usuario cambie el tamaño de la ventana

#ETIQUETAS Y CAJA DE TEXTO

#Creamos una etiqueta que indica que dbe escribir el usuario
etiqueta_cantidad=tk.Label(ventana,text="ingresar la cantidad: ")
etiqueta_cantidad.pack(pady=10) # .pack() coloca el elemento y pady da un margen vertical

#Caja de texto donde se escribira la cantidad
entrada_cantidad=tk.Entry(ventana,justify="center") #justify centra el texto
entrada_cantidad.pack(pady=5)
#Botones para calcular IVA
boton_iva=tk.Button(ventana,text="Calcular IVA (16%)",command=calcular_iva,bg="#E2DCD6")
boton_iva.pack(pady=5)
#Boton para calcular descuento
boton_descuento=tk.Button(ventana,text="Calcular el descuento (10%)",command=calcular_descuento,bg="#E2DCD6")
boton_descuento.pack(pady=5)
#Boton para calcular el total
boton_total=tk.Button(ventana,text="Calcular total",command=calcular_total,bg="#E2DCD6")
boton_total.pack(pady=5)
#ETIQUETA PARA MOSTRAR RESULTADOS
etiqueta_cantidad=tk.Label(ventana,text="Resultado:")
etiqueta_cantidad.pack(pady=10)
etiqueta_resultado=tk.Label(ventana,text="")
etiqueta_resultado.pack()


ventana.mainloop()        
