# Camila Monserrat Ochoa Gomez
# Programacion 3°B
# medio punto en el examen de la segunda unidad
# 10/11/2025


import tkinter as tk
from tkinter import messagebox

def calcular_sueldo():
    try:
        nombre = entry_nombre.get()
        sueldo_mensual = float(entry_sueldo.get())
        meses_trabajados = int(entry_meses.get())

        if meses_trabajados < 0 or meses_trabajados > 12:
            messagebox.showerror("Error", "Los meses trabajados deben estar entre 0 y 12.")
            return

        # Calcular sueldo por meses
        sueldo_por_meses = sueldo_mensual * meses_trabajados

        # Calcular aguinaldo (solo si trabajó más de 3 meses)
        aguinaldo = sueldo_mensual / 2 if meses_trabajados > 3 else 0

        # Subtotal
        subtotal = sueldo_por_meses + aguinaldo

        # Determinar tipo de bono
        tipo = bono_var.get()
        if tipo == 1:  # Completo
            bono_anual = subtotal * 0.10
        elif tipo == 2:  # Parcial
            bono_anual = subtotal * 0.05
        else:  # Sin bono
            bono_anual = 0

        # Sueldo total anual
        sueldo_total = subtotal + bono_anual

        # Mostrar resultados
        resultado.set(f"Trabajador: {nombre}\n"
                      f"Sueldo por meses: ${sueldo_por_meses:.2f}\n"
                      f"Aguinaldo: ${aguinaldo:.2f}\n"
                      f"Subtotal: ${subtotal:.2f}\n"
                      f"Bono anual: ${bono_anual:.2f}\n"
                      f"Sueldo TOTAL anual: ${sueldo_total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")


# Ventana principal
ventana = tk.Tk()
ventana.title("Camila Monserrat Ochoa Gomez")
ventana.geometry("400x450")

# Entradas
tk.Label(ventana, text="Nombre del trabajador:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Sueldo mensual:").pack()
entry_sueldo = tk.Entry(ventana)
entry_sueldo.pack()

tk.Label(ventana, text="Meses trabajados (0 a 12):").pack()
entry_meses = tk.Entry(ventana)
entry_meses.pack()

# Tipo de bono (radio buttons)
tk.Label(ventana, text="Tipo de bono anual:").pack()
bono_var = tk.IntVar()
tk.Radiobutton(ventana, text="Completo (10%)", variable=bono_var, value=1).pack()
tk.Radiobutton(ventana, text="Parcial (5%)", variable=bono_var, value=2).pack()
tk.Radiobutton(ventana, text="Sin bono (0%)", variable=bono_var, value=3).pack()


# Botón para calcular
tk.Button(ventana, text="Calcular Sueldo Total", command=calcular_sueldo).pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", font=("Arial", 10, "bold")).pack(pady=10)

ventana.mainloop()
