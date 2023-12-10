'''Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code.'''
fichero=open("datos.txt","w", encoding="utf-8") 
fichero.write("Primer línea.\n") 
fichero.write("Segunda línea.\n") 
fichero.write("Tercer línea.\n")  
fichero.close() 