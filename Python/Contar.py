def main():
    try:
        inicio = int(input("Ingrese el primer número para el conteo: "))
        fin = int(input("Ingrese el segundo número para el conteo: "))
        
        for num in range(inicio, fin + 1):
            print(num, end=" ")
    
    except ValueError:
        print("Error: Ingrese dos valores numéricos.")

if __name__ == "__main__":
    main()