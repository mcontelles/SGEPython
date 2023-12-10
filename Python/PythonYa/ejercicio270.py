'''Podemos recorrer el archivo leyendo línea a línea utilizando la estructura repetitiva for'''
fichero=open("datos.txt","r")
for line in fichero:
    print(line)
fichero.close()