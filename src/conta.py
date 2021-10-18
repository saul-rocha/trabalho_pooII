from src.history import Historico

class Conta:
    _qtd_contas = 0
    __slots__ = ["_numero", "_titular", "_saldo", "_limite", "_senha", "historico"]
    def __init__(self, numero, client, saldo, limite, senha):
        self._numero = numero
        self._titular = client
        self._saldo = saldo
        self._limite = limite
        self._senha = senha
        self.historico = Historico()
        Conta._qtd_contas += 1

    @property
    def numero(self):
        return self._numero

    @property
    def senha(self):
        return self._senha

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    '''@titular.setter
    def titular(self, cliente):
        self._client = cliente'''

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @limite.setter
    def limite(self, limite):
        self._limite = limite

##retorna True se foi efetuado e False caso não
    def deposita(self, valor):
        if valor <= 0:
            return False
        else:
            self.saldo = int(self.saldo)+int(valor)
            self.historico.transacoes.append("Deposito  de {}".format(valor))
            return True

    def saca(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            self.historico.transacoes.append("Saque  de {}".format(saque))
            return True
        else:
            return False

    def extrato(self):
        print("Numero da Conta:", self.numero)
        self.titular.imprimir()
        print("Saldo: ", self.saldo)
        print("Limite: ", self.limite)
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transferencia(self, destino, valor):
        if valor < 0:
            return False
        elif self.saldo >= valor:
            retira = self.saca(valor)
            if (retira == False):
                return False
            else:
                destino.deposita(valor)
                self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
                return True
        else:
            return False

    def autentica(self, cpf, senha):
        if cpf == self.titular.cpf and senha == self.senha:
            return True
        else:
            return False