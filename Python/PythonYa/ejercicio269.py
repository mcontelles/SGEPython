'''Leer el contenido del archivo de texto 'datos.txt' línea a línea.'''
fichero=open("datos.txt","r")
line=fichero.readline()
while line!='':
    print(line)
    line=fichero.readline()
fichero.close()