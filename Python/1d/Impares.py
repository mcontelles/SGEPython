'''
Crea un programa llamado Impares.py que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número, separados por comas.
'''
num = int(input("Introduce un número: "))
print(f"Los numeros impares del 1 al {num} son:")
numeros = ""
for i in range(1, num):
    if i%2!=0 and i>=(num-2):
        numeros += str(i)
    elif i%2!=0:
        numeros += str(i)+", "
print(numeros)