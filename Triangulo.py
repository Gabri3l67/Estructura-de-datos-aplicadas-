from figura import Figura
import math

class Triangulo(Figura):
    def __init__(self, lado_1, lado_2, lado_3):
        super().__init__("Triángulo")
        self.lado_a = lado_1
        self.lado_b = lado_2
        self.lado_c = lado_3

    def calcular_s(self):   
        return (self.lado_a + self.lado_b + self.lado_c) / 2

    def calcular_area(self):
        s = self.calcular_s()
        return math.sqrt(s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c))

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
