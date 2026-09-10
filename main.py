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

superman.atacar(zod)