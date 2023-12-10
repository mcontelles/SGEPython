'''Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.'''
edades_manana = [int(input("Ingrese la edad del estudiante (turno mañana): ")) for _ in range(5)]
edades_tarde = [int(input("Ingrese la edad del estudiante (turno tarde): ")) for _ in range(6)]
edades_noche = [int(input("Ingrese la edad del estudiante (turno noche): ")) for _ in range(11)]

promedio_manana = sum(edades_manana) / len(edades_manana)
promedio_tarde = sum(edades_tarde) / len(edades_tarde)
promedio_noche = sum(edades_noche) / len(edades_noche)

print(f"Promedio de edades (turno mañana): {promedio_manana}")
print(f"Promedio de edades (turno tarde): {promedio_tarde}")
print(f"Promedio de edades (turno noche): {promedio_noche}")

if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene un promedio de edades mayor.")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene un promedio de edades mayor.")
else:
    print("El turno noche tiene un promedio de edades mayor.")
