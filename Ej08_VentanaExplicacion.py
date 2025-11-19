# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa que muestra una ventana con una etiqueta y un boton

#Importamos la libreia Tkinter y le damos un alias "tk"
import tkinter as tk

#Crear una ventana principal
ventana=tk.Tk() #Instalancia de la aplicacion

#Configurar el titulo de la ventana
ventana.title("Ventana de saludos")

#Definir el tamaño de la ventana(ancho x alto)
ventana.geometry("400x300")

#Agregar un texto(etiqueta)
etiqueta=tk.Label(ventana,text="hola, buenos dias",font=("Arial",16))
etiqueta.pack(pady=20)#"pack" es para que se muestra en la ventana y "pady" es para que se separe del borde superior

#Agregar un boton
def saludar():
    etiqueta.config(text="¡Que tal!, ¿como va tu dia?")

boton=tk.Button(ventana,text="saludar",command=saludar)
boton.pack(pady=10)

#Ejecutar el bucle principal de la aplicacion
ventana.mainloop()