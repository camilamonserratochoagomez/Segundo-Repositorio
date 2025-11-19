import tkinter as tk


def sumar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
   # TODO: Obtener los valores de las entradas, sumarlos y mostrar el resultado
   pass
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("350x230")
# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botón de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()