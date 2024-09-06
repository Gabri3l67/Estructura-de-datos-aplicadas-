import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_resultados(self, area, perimetro):
        return f"Resultados de {self.nombre}:\nÁrea: {round(area, 2)}\nPerímetro: {round(perimetro, 2)}"

