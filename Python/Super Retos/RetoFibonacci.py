def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num + 1):
            a, b = b, a + b
        return b

#Prueba
resultado = fibonacci(10)
print(resultado)