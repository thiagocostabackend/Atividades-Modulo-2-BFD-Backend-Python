
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []
    
    def cadastrar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if not self.notas: # o not verifica se a lista está vazia e retorna True se estiver vazia
            return 0
        return sum(self.notas) / len(self.notas)
    
    def exibir_dados(self):
        media = self.calcular_media() # interliga os métodos
        return f'Aluno: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Média: {media:.2f}'
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario
    
    def exibir_dados(self):
        return f'Professor: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}, Salário: R${self.salario:.2f}'
    
# objetos de Aluno e Professor
aluno1 = Aluno('Ana Silva', 20, '2023001')
aluno1.cadastrar_nota(8.5)
aluno1.cadastrar_nota(7.0)
aluno1.cadastrar_nota(9.0)
professor1 = Professor('Carlos Souza', 45, 'Matemática', 3500.00)
# Exibindo os dados formatados
print(aluno1.exibir_dados())
print(professor1.exibir_dados())