'''Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.'''
numeros = [int(input("Ingrese un entero: ")) for _ in range(5)]
numeros_filtrados = [num for num in numeros if num < 10]
print("Lista original:", numeros)
print("Lista con elementos menores a 10:", numeros_filtrados)