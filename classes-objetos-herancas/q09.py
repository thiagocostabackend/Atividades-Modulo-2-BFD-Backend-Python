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
    
class Professor(Funcionario):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade, salario)
        self.disciplina = disciplina
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e lessiono {self.disciplina}.")

professor1 = Professor("Ana", 35, 4000, "Matemática")
professor1.apresentar()