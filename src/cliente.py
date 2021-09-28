class Client:
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def imprimir(self):
        print("nome: ", self.nome)
        print("sobrenome: ", self.sobrenome)
        print("cpf: ", self.cpf)

