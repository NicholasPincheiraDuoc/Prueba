import random

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.danio_min = 10
        self.danio_max = 20

    def atacar(self, oponente):
        danio = random.randint(self.danio_min, self.danio_max)
        print(f"{self.nombre} ataca a {oponente.nombre} y causa {danio} puntos de daño.")
        oponente.recibir_danio(danio)

    def recibir_danio(self, danio):
        self.salud -= danio
        if self.salud < 0:
            self.salud = 0
        print(f"{self.nombre} recibe {danio} puntos de daño. Salud restante: {self.salud}")

# Crear a los guerreros
patrick = Guerrero("Patrick")
nicholas = Guerrero("Nicholas")

# Juego de espadas
turno = 1
while patrick.salud > 0 and nicholas.salud > 0:
    print(f"\nTurno {turno}")
    turno += 1

    if random.choice([True, False]):
        patrick.atacar(nicholas)
    else:
        nicholas.atacar(patrick)

    print(f"{patrick.nombre}: {patrick.salud} de salud")
    print(f"{nicholas.nombre}: {nicholas.salud} de salud")

# Mostrar el resultado
if patrick.salud <= 0:
    print(f"\n{patrick.nombre} ha sido derrotado. ¡{nicholas.nombre} gana la batalla!")
else:
    print(f"\n{nicholas.nombre} ha sido derrotado. ¡{patrick.nombre} gana la batalla!")