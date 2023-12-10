cantidad_total_preguntas = int(input("Ingrese la cantidad total de preguntas: "))
cantidad_respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas: "))

porcentaje_correctas = (cantidad_respuestas_correctas / cantidad_total_preguntas) * 100

if porcentaje_correctas >= 70:
    nivel = "Aprobado"
elif 50 <= porcentaje_correctas < 70:
    nivel = "Regular"
else:
    nivel = "No Aprobado"

print(f"El postulante tiene un porcentaje de respuestas correctas del {porcentaje_correctas:.2f}%.")
print(f"Nivel del postulante: {nivel}")