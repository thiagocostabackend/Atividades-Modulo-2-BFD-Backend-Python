'''2. Crie uma classe Pessoa com os atributos: 
●  nome (público) 
●  _anoNasceu (protegido) 
 
Instancie um objeto e mostre que é possível acessar _idade, mas que não é recomendado.'''
class Pessoa:
    def __init__(self, nome, anoNasceu):
        self.nome = nome
        self._anoNasceu = anoNasceu

# Exemplo de uso:
pessoa = Pessoa("João", 1990)
print(pessoa.nome)         # Acesso público
print(pessoa._anoNasceu)   # Acesso protegido (não recomendado)