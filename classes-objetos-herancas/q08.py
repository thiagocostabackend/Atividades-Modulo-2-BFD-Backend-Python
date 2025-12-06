class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def decimo_terceiro(self):
        return self.salario
    