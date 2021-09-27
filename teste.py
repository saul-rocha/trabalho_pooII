from src.conta import Conta, Client # importa a classe do diretorio src

cc = Client("Saul", "Rocha", "1111")
c1c = Client("Romuere", "Silva", "2222")
c = Conta("123", cc, 300)
c1 = Conta("321", c1c, 1000)


res = True
res = c1.saca(10)

if res == True:
    print("OK!\n\n\n")
else:
    print("Não realizado!\n\n\n")

res = c.transferencia(c1, 200)
if res == True:
    print("OK!\n\n\n")
else:
    print("Nao realizado!\n\n\n")

res = c1.deposita(100)
if res == True:
    print("OK!\n\n\n")
else:
    print("Nao realizado!\n\n\n")

c.extrato()
print("\n")
c1.extrato()

res = c1.saca(10000)
if res == True:
    print("OK!\n\n\n")
else:
    print("Nao realizado!\n\n\n")