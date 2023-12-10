'''Abrir un archivo de texto con el parámetro "r+", imprimir su text actual y agregar luego dos líneas al final.'''
fichero=open("datos.txt","r+") 
text=fichero.read()
print(text)
fichero.write("1\n")
fichero.write("2\n")
fichero.close()