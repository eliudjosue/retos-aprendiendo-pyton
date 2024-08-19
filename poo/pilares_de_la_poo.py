class Personajes:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(f".Fuerza {self.fuerza}")
        print(f".Inteligencia {self.inteligencia}")
        print(f".Defensa: {self.defensa}")
        print(f".Vida: {self.vida}")
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia +inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre}, ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre}, ha realizado, {daño}, puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
        else: 
            enemigo.morir()



# mi_personaje = Personajes("Naruto", 10, 1, 5, 100)
# mi_enemigo = Personajes("Sasuke", 8, 5, 3, 100)
# mi_personaje.atacar(mi_enemigo)

# Herencia
class Guerrero(Personajes):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero valiryo, daño 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Nu,ero incorrecto")
        
    def atributos(self):
            super().atributos()
            print(f".Espada: {self.espada}")
        
    def daño(self, enemigo):
            return self.fuerza*self.espada - enemigo.defensa

rocklee = Guerrero("rocklee", 20, 10, 10, 100, 5)

class Mago(Personajes):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f".Libro: {self.libro}")

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    

# goku = Personajes("Goku", 20, 15, 10, 100)

# naruto = Guerrero("Naruto", 20, 15, 10, 100, 5)

# gandalf = Mago("Gandalf", 20, 15, 10, 100, 5)


# goku.atributos()
# naruto.atributos()
# gandalf.atributos()

# goku.atacar(naruto)
# naruto.atacar(gandalf)
# gandalf.atacar(goku)

# goku.atributos()
# naruto.atributos()
# gandalf.atributos()

# POLIMORFISMO

personaje_1 = Guerrero("Orochimaru", 20, 10, 4, 100, 4)
personaje_2 = Mago("Sarutobi", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("/nTurno", turno)
        print(">>> Accion de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("/nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("/nHa ganado", jugador_2.nombre)
    else:
        print("/nEmpate")

combate(personaje_1, personaje_2)

