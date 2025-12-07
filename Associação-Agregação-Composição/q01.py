
class Carro:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.motor = self.Motor(potencia)

    class Motor:
        def __init__(self, potencia):
            self.potencia = potencia

# Exemplo de uso
meu_carro = Carro("Fusca", 150)
print(f"Modelo do carro: {meu_carro.modelo}, Potência do motor: {meu_carro.motor.potencia} HP")
