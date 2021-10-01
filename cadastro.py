class Cadastro:

    __slots__ = ['_lista_Contas']

    def __init__(self):
        self._lista_Contas = []

    def cadastra(self, conta):
        existe = self.busca(conta.numero)
        if(existe==None):
            self._lista_Contas.append(conta)
            return True
        else:
            return False

    def busca(self, numero):
        res = None
        for lp in self._lista_Contas:
            if lp.numero == numero:
                res = lp
        return res