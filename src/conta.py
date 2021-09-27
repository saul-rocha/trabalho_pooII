import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data de abertura: {}".format(self.data_abertura))
        print("transações: ")
        for i in self.transacoes:
            print("-", i)

class Client:

    __slots__ = ['_nome','_sobrenome', '_cpf']
    
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


class Conta:
    _qtd_contas = 0
    __slots__ = ["_numero", "_titular", "_saldo", "_limite", "historico"]
    def __init__(self, numero, client, saldo = 0, limite = 100):
        self._numero = numero
        self._titular = client
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()
        Conta._qtd_contas += 1

    @property
    def numero(self):
        return self._numero

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

    @titular.setter
    def titular(self, cliente):
        self._client = cliente

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @limite.setter
    def limite(self, limite):
        self._limite = limite

##retorna True se foi efetuado e False caso não
    def deposita(self, valor):
        if valor < 0:
            return False
        else:
            self.saldo += valor
            self.historico.transacoes.append("Deposito  de {}".format(valor))
            return True

    def saca(self, saque):
        if self.saldo > saque:
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
        self.historico.imprime()
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