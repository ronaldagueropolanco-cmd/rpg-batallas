import random

class Personaje:
    def __init__(self, nombre, vida, dano, habilidades):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano
        self.habilidades = habilidades
        self.inventario = {}

    def atacar(self, objetivo):
        dano_real = random.randint(self.dano - 20, self.dano + 20)
        objetivo.vida -= dano_real

    def agregar_objeto(self, objeto):
        self.inventario[objeto.nombre] = objeto

    def usar_objeto(self, nombre_objeto):
        if nombre_objeto not in self.inventario:
            return "No tienes ese objeto"
        else:
            self.vida += self.inventario[nombre_objeto].curacion
            self.inventario[nombre_objeto].cantidad -= 1

            if self.inventario[nombre_objeto].cantidad == 0:
                del self.inventario[nombre_objeto]

class Heroe(Personaje):
    def __init__(self, nombre, vida, dano, habilidades, superpoder):
        super().__init__(nombre, vida, dano, habilidades)
        self.superpoder = superpoder

class Enemigo(Personaje):
    def __init__(self, nombre, vida, dano, habilidades, arma_poderosa):
        super().__init__(nombre, vida, dano, habilidades)
        self.arma_poderosa = arma_poderosa

class Objeto:
    def __init__(self, nombre, curacion, cantidad):
        self.nombre = nombre
        self.curacion = curacion
        self.cantidad = cantidad

superman = Heroe("SuperMan", 300, 150, ["Volar", "Super Fuerza"], "super_fuerza")
zod = Enemigo("Zod", 250, 125, ["Fuerza", "Resistencia"], "Pistola")

objeto_superman = Objeto("Pocion de vida", 45, 3)
objeto_zod = Objeto("Pocion de vida", 45, 3)

superman.agregar_objeto(objeto_superman)
zod.agregar_objeto(objeto_zod)

while True:
    accion = input(f"{superman.nombre}, ¿qué haces? (escribe 'atacar' o 'curar'): ").lower()
    
    while accion != 'atacar' and accion != 'curar':
        print("Comando no reconocido")
        accion = input(f"{superman.nombre}, ¿qué haces? (escribe 'atacar' o 'curar'): ").lower()

    if accion == 'curar':
        superman.usar_objeto("Pocion de vida")
        print(f"{superman.nombre} se esta curando, vida actual {superman.vida}")
        superman.atacar(zod)
        if zod.vida >= 0:
            print(f"{superman.nombre} ataca a {zod.nombre}. {zod.nombre}  le queda con {zod.vida} de vida")
        else:
            print(f"{zod.nombre} fue derrotado. Ganador {superman.nombre}")
            break
    elif accion == 'atacar':
        superman.atacar(zod)
        if zod.vida >= 0:
            print(f"{superman.nombre} ataca a {zod.nombre}. {zod.nombre}  le queda con {zod.vida} de vida")
        else:
            print(f"{zod.nombre} fue derrotado. Ganador {superman.nombre}")
            break

    if zod.vida <= 50:
        zod.usar_objeto("Pocion de vida")
        print(f"{zod.nombre} se esta curando, vida actual {zod.vida}")
        zod.atacar(superman)
        if superman.vida >= 0:
            print(f"{zod.nombre} ataca a {superman.nombre}. {superman.nombre}  le queda con {superman.vida} de vida \n")
        else:
            print(f"{superman.nombre} fue derrotado. Ganador {zod.nombre}")
            break
    else:
        zod.atacar(superman)
        if superman.vida >= 0:
            print(f"{zod.nombre} ataca a {superman.nombre}. {superman.nombre}  le queda con {superman.vida} de vida \n")
        else:
            print(f"{superman.nombre} fue derrotado. Ganador {zod.nombre}")
            break