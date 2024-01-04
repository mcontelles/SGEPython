def factorial(num):
    if num == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado

# Ejemplo
resultado = factorial(5)
print(resultado)
