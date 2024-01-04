def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

resultado_mcd = mcd(20, 12)
print(f"Máximo común divisor de 20 y 12: {resultado_mcd}")

print("Números primos del 1 al 50:")
for i in range(1, 51):
    if esPrimo(i):
        print(i, end=" ")
