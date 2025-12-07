
class Forma:
    def area(self):
        pass
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio * self.raio

def imprimir_areas(formas):
    for forma in formas:
        print(f'Área: {forma.area():.2f}')

# Exemplo de uso
formas = [Quadrado(4), Circulo(3)]
imprimir_areas(formas)