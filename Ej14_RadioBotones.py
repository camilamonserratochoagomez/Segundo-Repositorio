# CBATIS 89
# 3°B Programacion
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa de radio botenes que haga un descuento

import tkinter as tk

#Crear ventana
ventana=tk.Tk()
ventana.title("Calcular Descuento")
ventana.geometry("400x300")

#ETIQUETA Y CAJA DE TEXTO
etiqueta_cantidad=tk.Label(ventana,text="Ingresa la cantidad: ")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad=tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

def ejecutar_radio():
    opcion=seleccion.get()

    if opcion==1:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.05
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 5%,el cual equivael a: ${descuento:.2f}")

    elif opcion==2:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.10
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento de 10%,el cual equivale a: ${descuento:.2f}")

    elif opcion==3:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.15
    
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento de 15%,el cual equivale a: ${descuento:.2f}")

seleccion=tk.IntVar()

#Crear los radio botones
radioB1=tk.Radiobutton(ventana,text="Descuento 5%",variable=seleccion,value=1,command=ejecutar_radio)
radioB2=tk.Radiobutton(ventana,text="Descuento 10%",variable=seleccion,value=2,command=ejecutar_radio)
radioB3=tk.Radiobutton(ventana,text="Descuento 15%",variable=seleccion,value=3,command=ejecutar_radio)

radioB1.pack(pady=5)
radioB2.pack(pady=5)
radioB3.pack(pady=5)


etiqueta_resultado=tk.Label(ventana,text="",wraplength=350,justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
