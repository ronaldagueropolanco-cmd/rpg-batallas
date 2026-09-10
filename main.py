class Personaje:
    def __init__(self, nombre, vida, dano, habilidades):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano
        self.habilidades = habilidades

    def atacar(self, objetivo):
        objetivo.vida -= self.dano

class Heroe(Personaje):
    def __init__(self, nombre, vida, dano, habilidades, superpoder):
        super().__init__(nombre, vida, dano, habilidades)
        self.superpoder = superpoder

class Enemigo(Personaje):
    def __init__(self, nombre, vida, dano, habilidades, arma_poderosa):
        super().__init__(nombre, vida, dano, habilidades)
        self.arma_poderosa = arma_poderosa

superman = Heroe("SuperMan", 300, 150, ["Volar", "Super Fuerza"], "super_fuerza")

zod = Enemigo("Zod", 250, 125, ["Fuerza", "Resistencia"], "Pistola")

while True:
    superman.atacar(zod)
    if zod.vida >= 0:
        print(f"{superman.nombre} ataca a {zod.nombre}. {zod.nombre}  le queda con {zod.vida} de vida")
    else:
        print(f"{zod.nombre} fue derrotado. Ganador {superman.nombre}")
        break

    zod.atacar(superman)
    if superman.vida >= 0:
        print(f"{zod.nombre} ataca a {superman.nombre}. {superman.nombre}  le queda con {superman.vida} de vida \n")
    else:
        print(f"{superman.nombre} fue derrotado. Ganador {zod.nombre}")
        break