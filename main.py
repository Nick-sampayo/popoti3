class Aluno:
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome 
        self.sexo = sexo 
        self.idade = idade

if __name__ == "__main__":
    aluno1 = Aluno("00002604","Nicolas","M","16")
    print(aluno1.matricula)
    print(aluno1.nome)
    print(aluno1.sexo)
    print(aluno1.idade)