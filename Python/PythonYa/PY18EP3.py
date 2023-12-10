'''Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.'''
numeros = [5, 2, 8, 1, 7]

numeros.sort()
print("Orden de menor a mayor:", numeros)

numeros.sort(reverse=True)
print("Orden de mayor a menor:", numeros)