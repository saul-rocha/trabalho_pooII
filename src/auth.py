class SistemaInterno:
    def login(self, obj, login, senha):

        if (hasattr(obj, 'autentica') and obj.autentica(login, senha)):
            print("{} AUTENTICADO!".format(obj.__class__.__name__))
            return True
            # chama método autentica
        else:
            print("{} NÃO AUTENTICADO!".format(obj.__class__.__name__))
            return False
            # imprime mensagem de ação inválida