secuencia = input("Introduce una secuencia de numeros separados por espacios: ")
numeros = secuencia.split(" ")
suma=0
for i in numeros :
    numero =  int(i)
    suma+= numero
print("la suma es: "+str(suma))