class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):
        return f"O carro {self.marca} {self.modelo} está em movimento."
    

carro1 = Carro("Toyota", "Corolla")
print(carro1.dirigir())