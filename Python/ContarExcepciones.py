def main():
    try:
        numeros = input("Ingrese dos números enteros separados por espacio: ").split()
        a, b = map(int, numeros)
        
        for num in range(a, b + 1):
            print(num, end=" ")

    except ValueError:
        print("Datos incorrectos")


main()
