#5. Na classe Cachorro, adicione um método aniversario() que aumenta a idade em 1 e mostre o novo valor.
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        return f"Au Au, meu nome é {self.nome} e eu tenho {self.idade} anos"
    def aniversario(self):
        self.idade += 1
        return f"Próximo aniversário de {self.nome} será de {self.idade} anos."

cachorro1 = Cachorro("Rex", 3)
print(cachorro1.apresentacao())
print(cachorro1.aniversario())
