def main():
    try:
        numeros = input("Ingrese los 6 números de la lotería separados por espacios: ").split()
        numeros = [int(num) for num in numeros]
        
        if len(numeros) == 6 and all(1 <= num <= 49 for num in numeros) and len(set(numeros)) == 6:
            numeros.sort()
            print("Números válidos y ordenados:", numeros)
        else:
            print("Error: La lista de números no es válida.")
    
    except ValueError:
        print("Error: Ingrese 6 valores numéricos.")

main()