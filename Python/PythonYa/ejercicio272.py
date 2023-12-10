'''Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.'''
fichero=open("datos.txt","a")
fichero.write("nueva línea 1\n")
fichero.write("nueva línea 2\n")
fichero.close()
fichero=open("datos.txt","r")
text=fichero.read()
print(text)
fichero.close()