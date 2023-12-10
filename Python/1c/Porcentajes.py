excepcion = True
while excepcion:
    try:
        chicos= int(input("Cuántos chicos hay en clase?"))
        excepcion = False
    except:
        print("Debes introducir un número entero.")
excepcion = True
while excepcion:
    try:
        chicas= int(input("Cuántas chicas hay en clase?"))
        excepcion = False
    except:
        print("Debes introducir un número entero.")
total = int(chicos+chicas)
chicosPer = float((chicos/total)*100)
chicasPer = float((chicas/total)*100)
print(f"{chicosPer:.3f}% de chicos.")
print(f"{chicasPer:.3f}% de chicas.")