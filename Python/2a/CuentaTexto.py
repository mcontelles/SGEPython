texto = str(input("Introduce un texto: "))

cont = 0
while texto.find('Python')>=0:
    texto = texto[texto.find('Python')+6:]
    cont+=1
print(texto)
print("La palabra Python aparece "+str(cont)+" veces.")