print("******Introduce números, uno a uno, para acabar, introduce '0'.******")
numero = int(input("Introduce un número: "))
numeros = []
while numero!=0:
    numeros.append(numero)
    numero = int(input("Introduce un número: "))
posiciones = []
numeroBuscado = int(input("Introduce el número que quieras buscar: "))
print()
for i in range(len(numeros)):
    try:
        posiciones.append(numeros.index(numeroBuscado, i))
    except:
        break
posicionesSet = set(posiciones)
print("El número se halló en las siguientes posiciones:")
for posicion in posicionesSet:
    print(posicion, end=" ")