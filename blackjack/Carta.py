class Carta:
    def __init__(self, valor, palo, nombre):
        self.valor = valor
        self.palo = palo
        self.nombre = nombre

    def __repr__(self):
        return f"{self.nombre}"