'''Leer el contenido del archivo de texto 'datos.txt'.'''
fichero=open("datos.txt","r")
print(fichero.read())
fichero.close()