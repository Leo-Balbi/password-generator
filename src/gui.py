import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import pyperclip  # Librería para copiar al portapapeles
from utils import generate_password, save_password

# Función para generar y mostrar la contraseña
def generate():
    length = int(entry_length.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    save_password(password)
    
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")
    
    messagebox.showinfo("Contraseña Generada", "¡Tu contraseña ha sido guardada en passwords.txt!")

# Función para copiar la contraseña al portapapeles
def copy_password():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copiado", "¡Contraseña copiada al portapapeles!")

# Crear ventana con tema moderno
root = ThemedTk(theme="arc")
root.title("🔐 Generador de Contraseñas Seguras")
root.geometry("400x300")

# Estilos personalizados
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

# Etiqueta de título
ttk.Label(root, text="Generador de Contraseñas", font=("Arial", 16, "bold")).pack(pady=10)

# Longitud de la contraseña
ttk.Label(root, text="Longitud de la contraseña:", font=("Arial", 12)).pack()
entry_length = ttk.Entry(root)
entry_length.pack()

# Complejidad de la contraseña
ttk.Label(root, text="Nivel de seguridad:", font=("Arial", 12)).pack()
complexity_var = tk.StringVar(value="medium")
ttk.OptionMenu(root, complexity_var, "low", "medium", "high").pack()

# Campo de contraseña generada
password_entry = ttk.Entry(root, state="readonly", font=("Arial", 12))
password_entry.pack(pady=5)

# Botones
ttk.Button(root, text="Generar Contraseña", command=generate).pack(pady=5)
ttk.Button(root, text="Copiar Contraseña", command=copy_password).pack(pady=5)

# Ejecutar la aplicación
root.mainloop()