cantidad = int(input("Cuántos números quieres introducir? "))
mayor = 0
menor = 0
for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    if i==0:
        menor = numero
    if numero>mayor:
        mayor=numero
    if menor>numero:
        menor=numero
print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")    