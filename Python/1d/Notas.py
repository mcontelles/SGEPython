ningunaMayorQue4 = True
todasMayoresQue4 = True
misMatch = True
notas = []
media=0

for i in range(3):
    while misMatch:
        try:
            nota = int(input("Introduce una nota: "))
            if nota>=0 and nota<=10:
                notas.append(nota)
                misMatch=False
            else:
                print("Debes introducir un número entero entre 1 y 10.")
        except:
            print("Debes introducir un número entero entre 1 y 10.")
    misMatch=True

for i in range(3):
    if(notas[i]<4):
        todasMayoresQue4=False
    elif(notas[i]>4):
        ningunaMayorQue4=False
    if(i==0):
        media+=notas[i]*0.3
    elif(i==1):
        media+=notas[i]*0.2
    elif(i==2):
        media+=notas[i]*0.5

if(not ningunaMayorQue4 and not todasMayoresQue4):
    media=2

print(f"La nota media es: {media:.2f}")