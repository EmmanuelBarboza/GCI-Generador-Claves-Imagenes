import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import pyperclip

def image_to_password(image_path):
    """Convierte una imagen en una contraseña basada en su hash."""
    try:
        img = Image.open(image_path)
        img_data = np.array(img).tobytes()
        hash_obj = hashlib.sha256(img_data)
        return hash_obj.hexdigest()[:16]  # Tomar los primeros 16 caracteres
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar la imagen: {e}")
        return None

def select_image():
    """Abre un cuadro de diálogo para seleccionar una imagen y genera la contraseña."""
    file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        password = image_to_password(file_path)
        if password:
            password_var.set(password)
            display_image(file_path)

def copy_to_clipboard():
    """Copia la contraseña generada al portapapeles."""
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")

def display_image(image_path):
    """Carga y muestra la imagen seleccionada en la interfaz."""
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Redimensionar la imagen
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Contraseñas por Imagen")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=20)

title_label = tk.Label(frame, text="Generador de Contraseñas", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack()

btn_select = tk.Button(frame, text="Seleccionar Imagen", command=select_image, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
btn_select.pack(pady=10)

image_label = tk.Label(frame, bg="#f4f4f4")
image_label.pack()

password_var = tk.StringVar()
entry_password = tk.Entry(frame, textvariable=password_var, width=30, font=("Arial", 12), state='readonly', justify='center')
entry_password.pack(pady=10)

btn_copy = tk.Button(frame, text="Copiar Contraseña", command=copy_to_clipboard, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5)
btn_copy.pack()

root.mainloop()
