class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
    
    def mostrar(self):
        print(f"{self.dorsal}. {self.nombre}")


jugador1 = Jugador(16, "Pau Gasol")
jugador2 = Jugador(6, "LeBron James")

jugador1.mostrar()
jugador2.mostrar()
