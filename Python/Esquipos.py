class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None
    
    def mostrar(self):
        if self.equipo:
            print(f"{self.dorsal}. {self.nombre} - Equipo: {self.equipo.nombre}")
        else:
            print(f"{self.dorsal}. {self.nombre} - Sin equipo")

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre

equipo1 = Equipo("Los Lakers")
jugador1 = Jugador(16, "Pau Gasol")
jugador1.equipo = equipo1

jugador1.mostrar()
