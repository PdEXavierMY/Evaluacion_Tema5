from io import open
import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return f"{self.nombre}: {self.vida} de vida, {self.ataque} de ataque, {self.defensa} de defensa, {self.alcance} de alcance"


class Gestor:

    personajes = []
    def __init__(self):
        self.cargar()
        
    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()