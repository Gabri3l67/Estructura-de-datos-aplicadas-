from figura import Figura


class Rectangulo(Figura):
    def __init__(self, altura, base):
        super().__init__("Rectángulo")
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

    def calcular_perimetro(self):
        return 2 * (self.altura + self.base)
