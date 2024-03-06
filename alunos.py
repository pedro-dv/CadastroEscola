from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, nota):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f"({super().__repr__()}, {self.curso}, {self.nota})"

if __name__ == "__main__":
    print(Aluno("Jonas", 23, "Python", 10))