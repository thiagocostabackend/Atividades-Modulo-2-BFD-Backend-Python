'''Crie uma classe Autor e uma classe Livro. 
○  Um autor pode escrever vários livros. 
○  Um livro tem apenas um autor. 
○  Os objetos devem ser capazes de interagir sem dependência total (um Autor pode existir sem 
Livro e vice-versa).'''
class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro) # Associação

    def listar_livros(self):
        return [livro.titulo for livro in self.livros]
    
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        autor.adicionar_livro(self) # Associação

# Exemplo de uso
autor1 = Autor("J.K. Rowling")
livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1)
livro2 = Livro("Harry Potter e a Câmara Secreta", autor1)

print(f"Autor: {autor1.nome}")
print("Livros escritos:")
for titulo in autor1.listar_livros():
    print(f"- {titulo}")

