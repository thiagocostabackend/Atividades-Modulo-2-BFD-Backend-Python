'''7. Crie uma classe Pessoa com atributos nome e idade. Depois crie uma classe Estudante que herda de 
Pessoa e adiciona matricula e curso. '''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso