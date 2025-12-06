
'''11.Use super() em todas as classes do exercício anterior para que os métodos sejam chamados em cadeia, 
seguindo a MRO.'''


class Artista:
    def apresentar(self):
        print("Sou artista")
        super().apresentar()


class Programador:
    def apresentar(self):
        print("Sou programador")
        # Programador é o último, então não chama super()


class PessoaMultiTalento(Artista, Programador):
    def apresentar(self):
        print("Sou uma pessoa multi-talentosa")
        super().apresentar()


pessoa = PessoaMultiTalento()
pessoa.apresentar()  # Isso imprimirá a cadeia de chamadas seguindo a MRO
