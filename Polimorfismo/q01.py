
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

# Criando uma lista com vários animais
animais = [Cachorro(), Gato()]

# Percorrendo a lista e chamando o método falar() de cada animal
for animal in animais:
    animal.falar()