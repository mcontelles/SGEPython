'''Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):'''
n = int(input("Ingrese la cantidad de números a cargar: "))
pares = 0
impares = 0

for _ in range(n):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Se ingresaron {pares} números pares y {impares} números impares.")
