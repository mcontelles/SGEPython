def ask_num():
    misMatch = True
    while misMatch:
        try:
            num = int(input("Introduce un número: "))
            misMatch=False
        except:
            print("Debes introducir un número.")
    return num

def mcd(num1, num2):
    found = False

    while not found:
        num1Mayor = num1>num2
        if(num1Mayor):
            if(num1%num2==0):
                found = True
                return num2
            else:
                num1=num1%num2
        else:
            if(num2%num1==0):
                found = True
                return num1
            else:
                num2=num2%num1


def main():
    num1 = ask_num()
    num2 = ask_num()
    print(f"El MCD de {num1} y {num2} es: {mcd(num1, num2)}")

main()