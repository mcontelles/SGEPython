datos = str(input("Introduce datos separados por comas: ")).split(",")
datos.reverse()
for dato in datos :
    print(dato, end=" ")