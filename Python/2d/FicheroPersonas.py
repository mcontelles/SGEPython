def leer_fichero(nombre_fichero):
    try:
        with open(nombre_fichero, 'r') as fichero:
            lineas = fichero.readlines()
        return lineas
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no fue encontrado.")
        return []

def procesar_datos(lineas):
    personas = []
    for linea in lineas:
        nombre, edad = linea.split()
        personas.append({'nombre': nombre, 'edad': int(edad)})
    return personas

def encontrar_persona_mas_joven_y_mas_vieja(personas):
    if not personas:
        return None, None

    persona_mas_joven = min(personas, key=lambda x: x['edad'])
    persona_mas_vieja = max(personas, key=lambda x: x['edad'])

    return persona_mas_joven, persona_mas_vieja

def main():
    nombre_fichero = input("Ingrese el nombre del fichero de personas: ")

    lineas = leer_fichero(nombre_fichero)
    if not lineas:
        return

    personas = procesar_datos(lineas)

    persona_mas_joven, persona_mas_vieja = encontrar_persona_mas_joven_y_mas_vieja(personas)

    if persona_mas_joven and persona_mas_vieja:
        print("\nDatos de la persona más joven:")
        print(f"Nombre: {persona_mas_joven['nombre']}")
        print(f"Edad: {persona_mas_joven['edad']}")

        print("\nDatos de la persona más vieja:")
        print(f"Nombre: {persona_mas_vieja['nombre']}")
        print(f"Edad: {persona_mas_vieja['edad']}")
    else:
        print("No se pudieron encontrar datos de personas en el fichero.")

if __name__ == "__main__":
    main()