class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        return f"Au Au, meu nome é {self.nome} e eu tenho {self.idade} anos"

cachorro1 = Cachorro("Rex", 3)
print(cachorro1.apresentacao())