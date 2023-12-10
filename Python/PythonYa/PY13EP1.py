'''Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""'''
oracion = input("Ingrese una oración: ")
espacios_en_blanco = oracion.count(" ")

print(f"Cantidad de espacios en blanco en la oración: {espacios_en_blanco}")