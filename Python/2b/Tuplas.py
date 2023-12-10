calle = str(input("Calle: "))
numero = int(input("Número de puerta: "))
piso = int(input("Piso: "))
direccion = calle, numero, piso
print(f"Usted vive en la Calle {direccion[0]}, Nº {direccion[1]}, Piso {direccion[2]}")