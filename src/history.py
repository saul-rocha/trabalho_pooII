import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self, res):
        res.append("data de abertura: {}\n".format(self.data_abertura))
        res.append("transações: \n")
        for i in self.transacoes:
            res.append(i)
        return "\n".join(res)