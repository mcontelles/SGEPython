class PersonalHospital:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def mostrar(self):
        print(f"DNI: {self.dni}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}")


class Medico(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad

    def mostrar(self):
        super().mostrar()
        print(f"Especialidad: {self.especialidad}")


class Enfermero(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta

    def mostrar(self):
        super().mostrar()
        print(f"Planta: {self.planta}")


class PruebaConsulta:
    def __init__(self, fecha, medico):
        self.fecha = fecha
        self.medico = medico

    def mostrar(self):
        print(f"Fecha de la prueba/consulta: {self.fecha}")
        print("Médico que atendió:")
        self.medico.mostrar()


class Paciente:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial = []

    def agregar_prueba_consulta(self, prueba_consulta):
        self.historial.append(prueba_consulta)

    def mostrar(self):
        print(f"DNI: {self.dni}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}")
        print("Historial de pruebas y consultas:")
        for prueba_consulta in self.historial:
            prueba_consulta.mostrar()


medico1 = Medico("12345678A", "Dr. López", "Calle A", "123456789", "Cardiología")
enfermero1 = Enfermero("87654321B", "Enfermero Pérez", "Calle B", "987654321", "Planta 3")

paciente1 = Paciente("11111111X", "Juan Pérez", "Calle C", "555555555")

prueba1 = PruebaConsulta("01/01/2023", medico1)
paciente1.agregar_prueba_consulta(prueba1)

prueba2 = PruebaConsulta("02/01/2023", medico1)
paciente1.agregar_prueba_consulta(prueba2)

paciente1.mostrar()
