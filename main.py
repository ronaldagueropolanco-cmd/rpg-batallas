class Personaje:
    def __init__(self, nombre, vida, dano, habilidades):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano
        self.habilidades = habilidades

    def atacar(self, objetivo):
        objetivo - self.vida