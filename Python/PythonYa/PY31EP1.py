'''Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.'''
lista_enteros = [int(input("Ingrese un entero: ")) for _ in range(5)]
mayor, menor = max(lista_enteros), min(lista_enteros)
print("Lista de enteros:", lista_enteros)
print("Mayor valor:", mayor)
print("Menor valor:", menor)