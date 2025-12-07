'''2.  Crie uma classe Professor e uma classe Universidade. 
○  A Universidade pode ter vários professores. 
○  Mas os Professores também podem existir sem a Universidade.'''
class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def __str__(self):
        return f'Professor: {self.nome}, Disciplina: {self.disciplina}'

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        for professor in self.professores:
            print(professor)

# Exemplo de uso
prof1 = Professor("Dr. Silva", "Matemática")
prof2 = Professor("Dra. Souza", "Física")
uni = Universidade("Universidade Federal")
uni.adicionar_professor(prof1)
uni.adicionar_professor(prof2)
uni.listar_professores()