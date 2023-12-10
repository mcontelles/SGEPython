usuarios={}
for i in range(4):
    dni = int(input("Introduce el DNI: "))
    calle = str(input("Calle: "))
    numero = int(input("Número de puerta: "))
    piso = int(input("Piso: "))
    usuarios[dni] = (dni, calle, numero, piso)

dni = int(input("Busca datos por DNI (introduce un DNI): "))
if dni in usuarios:
    print("El usuario con DNI",usuarios[dni][0],"vive en la calle",usuarios[dni][1],", Nº", usuarios[dni][2],", piso:" ,usuarios[dni][3])
else:
    print("El DNI no se encuentra almacenado")