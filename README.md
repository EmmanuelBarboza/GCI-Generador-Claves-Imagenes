# GCI-Generador-Claves-Imagenes

## Descripción

GCI-Generador-Claves-Imagenes es una aplicación que permite generar contraseñas seguras a partir de imágenes. La aplicación utiliza el hash SHA-256 de la imagen seleccionada para generar una contraseña única y segura de 16 caracteres. La interfaz gráfica está construida con Tkinter y permite seleccionar una imagen desde el sistema, generar la contraseña y copiarla al portapapeles para su uso.

## Características

- Generación de contraseñas seguras a partir de imágenes utilizando el hash SHA-256.
- Interfaz gráfica sencilla con Tkinter para facilitar la interacción.
- Redimensionamiento y visualización de la imagen seleccionada.
- Opción para copiar la contraseña generada al portapapeles.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `hashlib` (incluida en Python)
  - `tkinter` (incluida en Python)
  - `Pillow` (para manejo de imágenes)
  - `numpy` (para convertir imágenes en datos)
  - `pyperclip` (para copiar al portapapeles)

Puedes instalar las bibliotecas necesarias con el siguiente comando:

```bash
pip install pillow numpy pyperclip
