'''1. Crie uma classe chamada Carro com os atributos marca e modelo. Depois crie dois objetos diferentes 
dessa classe e imprima os valores. '''
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
print(f"Carro 1: Marca: {carro1.marca}, Modelo: {carro1.modelo}")
print(f"Carro 2: Marca: {carro2.marca}, Modelo: {carro2.modelo}")