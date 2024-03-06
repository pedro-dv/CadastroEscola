import uuid


class Pessoa:
    def __init__(self, nome, idade):
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"({self.matricula}, {self.nome}, {self.idade})"


if __name__ == "__main__":
    print(Pessoa("Jonas", 23))