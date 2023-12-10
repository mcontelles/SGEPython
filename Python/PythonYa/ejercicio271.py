'''Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido.'''
fichero=open("datos.txt","r")
lines=fichero.readlines()
print('El archivo tiene', len(lines), 'líneas')
for line in lines:
    print(line)
fichero.close()