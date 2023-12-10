def pedir_entero_mensaje(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def pedir_tamano_tabla():
    N = pedir_entero_mensaje("Ingrese el tamaño de la tabla (N): ")
    return N

def llenar_tabla(N):
    tabla = []
    for i in range(N):
        fila = []
        for j in range(N):
            valor = pedir_entero_mensaje(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): ")
            fila.append(valor)
        tabla.append(fila)
    return tabla

def es_matriz_identidad(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if i == j and tabla[i][j] != 1:
                return False
            elif i != j and tabla[i][j] != 0:
                return False
    return True

def main():
    N = pedir_tamano_tabla()
    tabla = llenar_tabla(N)

    print("\nTabla ingresada:")
    for fila in tabla:
        print(fila)

    if es_matriz_identidad(tabla):
        print("\nLa tabla es una matriz identidad.")
    else:
        print("\nLa tabla NO es una matriz identidad.")

if __name__ == "__main__":
    main()