from PIL import Image
import os

def escalar_imagen(nombre_original, ancho, alto):
    try:
        imagen = Image.open(nombre_original)
        nombre_base, extension = os.path.splitext(nombre_original)
        nuevo_nombre = f"{ancho}_{alto}_{nombre_base}{extension}"
        
        nueva_imagen = imagen.resize((ancho, alto))
        nueva_imagen.save(nuevo_nombre)
        
        print(f"Imagen escalada guardada como: {nuevo_nombre}")
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Error: {e}")


nombre_imagen = input("Ingrese el nombre de la imagen: ")

while True:
    try:
        ancho = int(input("Ingrese el ancho de la imagen (0 para salir): "))
        if ancho == 0:
            break
        alto = int(input("Ingrese el alto de la imagen (0 para salir): "))
        if alto == 0:
            break

        escalar_imagen(nombre_imagen, ancho, alto)
    except ValueError:
        print("Error: Ingrese valores numéricos para el ancho y alto.")
