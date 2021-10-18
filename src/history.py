import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self, res):
        res.join("data de abertura: {}\n".format(self.data_abertura))
        res.join("transações: ")
        for i in self.transacoes:
            res.join(i,"\n")
        return res