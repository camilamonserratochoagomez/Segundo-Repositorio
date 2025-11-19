# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa que hace operaciones basicas
import tkinter as tk


def sumar():
   # Obtener valores y mostrar la suma. Cada operación tiene su propia función
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def resta():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      resultado_val = num1 - num2
      resultado.config(text=f"Resultado: {resultado_val}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def multiplicacion():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      resultado_val = num1 * num2
      resultado.config(text=f"Resultado: {resultado_val}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def division():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      if num2 == 0:
         resultado.config(text="Error: división por cero")
         return
      resultado_val = num1 / num2
      resultado.config(text=f"Resultado: {resultado_val}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")


   # TODO: Obtener los valores de las entradas, sumarlos y mostrar el resultado

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Operaciones basicas")
ventana.geometry("350x230")
# los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

#crear boton de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

# boton de resta
boton_resta = tk.Button(ventana, text="restar", command=resta)
boton_resta.pack(pady=5)

#boton de multiplicacion
boton_multiplicacion = tk.Button(ventana, text="multiplicar" , command=multiplicacion)
boton_multiplicacion.pack(pady=5)

# boton de division
boton_division = tk.Button(ventana, text="Dividir", command=division)
boton_division.pack(pady=5)


# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()