'''Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.'''
clave = input("Ingrese una clave: ")

if 10 <= len(clave) <= 20:
    print("Clave válida.")
else:
    print("Error: La clave debe tener entre 10 y 20 caracteres.")