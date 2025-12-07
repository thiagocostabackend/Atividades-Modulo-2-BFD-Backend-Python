'''4. Crie uma classe Veiculo com o método mover(). 
 Depois crie: 
●  Carro, que imprime "Dirigindo...". 
 
●  Bicicleta, que imprime "Pedalando...". 
 
●  Avião, que imprime "Voando...". 
 
●  Faça um programa que receba uma lista de veículos e use um loop para chamar o método mover() 
de cada um. '''
class Veiculo:
    def mover(self):
        pass
class Carro(Veiculo):
    def mover(self):
        print("Dirigindo...")  

class Bicicleta(Veiculo):
    def mover(self):
        print("Pedalando...")  

class Aviao(Veiculo):
    def mover(self):
        print("Voando...")

# Criando uma lista com veículos diferentes
veiculos = [Carro(), Bicicleta(), Aviao()]
for veiculo in veiculos:
    veiculo.mover()