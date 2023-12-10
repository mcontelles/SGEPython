'''Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.'''
oracion = input("Ingrese una oración: ")
oracion_minusculas = oracion.lower()
cantidad_vocales = sum(1 for letra in oracion_minusculas if letra in 'aeiou')

print(f"Cantidad de vocales en la oración: {cantidad_vocales}")
