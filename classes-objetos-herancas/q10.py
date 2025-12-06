'''10. Crie uma classe Artista com um método apresentar() que imprime "Sou artista". 
Crie uma classe Programador com um método apresentar() que imprime "Sou programador". 
Depois crie uma classe PessoaMultiTalento que herda de ambas e veja qual método é chamado.'''
class Artista:
    def apresentar(self):
        print("Sou artista")

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    pass

pessoa = PessoaMultiTalento()
pessoa.apresentar()  # Isso imprimirá "Sou artista" devido à ordem de herança (Artista vem antes de Programador)