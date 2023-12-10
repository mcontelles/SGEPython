'''En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.'''
nombres = []
notas = []

for _ in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    
    nombres.append(nombre)
    notas.append(nota)

print("Listado de alumnos:")
for i in range(4):
    nombre = nombres[i]
    nota = notas[i]
    
    if nota >= 8:
        condicion = "Muy Bueno"
    elif 4 <= nota <= 7:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    
    print(f"Nombre: {nombre}, Nota: {nota}, Condición: {condicion}")

cantidad_muy_bueno = sum(1 for nota in notas if nota >= 8)
print(f"Cantidad de alumnos con la leyenda 'Muy Bueno': {cantidad_muy_bueno}")