class SistemaInterno:
    def login(self, obj, login, senha):

        if (hasattr(obj, 'autentica') and obj.autentica(login, senha)):
            return True
        else:
            return False