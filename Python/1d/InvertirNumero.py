numero = int(input("Introduce un número: "))
while numero!=0:
    digito = int(numero%10)
    print(digito, end="")
    numero=(numero-digito)/10