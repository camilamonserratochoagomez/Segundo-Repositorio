# CBATIS 89
# 3°B Programacion Matutino
# CAMILA MONSERRAT OCHOA GOMEZ
# Programa que hace un sistema de contraseñas
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Función para abrir la ventana principal tras login exitoso
def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("400x200")
    ventana_principal.configure(bg="#e0f7fa")

    mensaje = tk.Label(
        ventana_principal,
        text="¡Bienvenido al sistema!",
        font=("Helvetica", 16, "bold"),
        bg="#e0f7fa",
        fg="#00796B"
    )
    mensaje.pack(pady=60)

    ventana_principal.mainloop()

# Función para verificar la contraseña
def verificar_password():
    password = entrada_password.get()
    if password == "camy123":
        messagebox.showinfo("Acceso", "Acceso correcto")
        ventana.destroy()  # Cierra la ventana de login
        abrir_ventana_principal()  # Abre la nueva ventana
    else:
        messagebox.showerror("Acceso", "Acceso denegado")

# Crear ventana principal de login
ventana = tk.Tk()
ventana.title("Sistema de Acceso")
ventana.geometry("350x200")
ventana.configure(bg="#f0f4f8")  # fondo claro

# Fuentes personalizadas
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_normal = font.Font(family="Helvetica", size=10)

# Marco centrado
marco = tk.Frame(ventana, bg="#ffffff", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de título
titulo = tk.Label(marco, text="Ingrese su contraseña", font=fuente_titulo, bg="#ffffff")
titulo.pack(padx=20, pady=(15, 5))

# Campo de entrada
entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)

# Botón de verificación
boton_verificar = tk.Button(
    marco, text="Verificar acceso", command=verificar_password,
    bg="#4CAF50", fg="white", font=fuente_normal, padx=10, pady=5,
    activebackground="#45a049", relief="flat"
)
boton_verificar.pack(pady=(10, 15))

# Ejecutar la app
ventana.mainloop()