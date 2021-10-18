import sys
import os

from PyQt5 import QtCore, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication


from interfaces.tela_cadastrar import Cadastrar
from interfaces.tela_deposita import Deposita
from interfaces.tela_extrato import Extrato 
from interfaces.tela_login import Login
from interfaces.tela_main_menu import Principal
from interfaces.tela_saque import Saque
from interfaces.tela_transferencia import Transferencia 
from interfaces.tela_home import Home

from src.cadastro import Cadastro
from src.conta import Conta
from src.cliente import Client
from src.autentica import Autenticavel
from src.auth import SistemaInterno

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow() 
        self.stack2 = QtWidgets.QMainWindow() 
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.principal = Principal()
        self.principal.setupUi(self.stack0)

        self.login = Login()
        self.login.setupUi(self.stack1)

        self.cadastrar = Cadastrar()
        self.cadastrar.setupUi(self.stack2)

        self.deposita = Deposita()
        self.deposita.setupUi(self.stack3)

        self.extrato = Extrato()
        self.extrato.setupUi(self.stack4)

        self.saque = Saque()
        self.saque.setupUi(self.stack5)

        self.transferencia = Transferencia()
        self.transferencia.setupUi(self.stack6)

        self.home = Home()
        self.home.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.si = SistemaInterno()
        self.principal.pushButton.clicked.connect(self.abrirTelaLogin)
        self.principal.pushButton_2.clicked.connect(self.abrirTelaCadastro)

        self.login.pushButton.clicked.connect(self.botaoEntrar)
        self.login.pushButton_2.clicked.connect(self.botaoVoltar)

        self.cadastrar.pushButton.clicked.connect(self.botaoOk)
        self.cadastrar.pushButton_2.clicked.connect(self.botaoVoltar)

        self.home.pushButton_2.clicked.connect(self.abrirTelaHome)
        self.home.pushButton.clicked.connect(self.botaoSacar)
        self.home.pushButton_3.clicked.connect(self.botaoExtrato)
        self.home.pushButton_4.clicked.connect(self.botaoTransfere)
        

       
       

        self.saque.pushButton.clicked.connect(self.botaoSacar)
        self.saque.pushButton_2.clicked.connect(self.botaoVoltar)

        self.transferencia.pushButton.clicked.connect(self.botaoTransfere)
        self.transferencia.pushButton_2.clicked.connect(self.botaoVoltar)

        self.home.pushButton_5.clicked.connect(self.botaoVoltar)

        #self.extrato.pushButton.clicked.connect(self.botaoExtrato)
        #self.extrato.pushButton_2.clicked.connect(self.botaoVoltar)


    def botaoOk(self):
            nome = self.cadastrar.lineEdit.text()
            sobrenome = self.cadastrar.lineEdit_4.text()
            cpf = self.cadastrar.lineEdit_6.text()
            numero = self.cadastrar.lineEdit_7.text()
            limite = self.cadastrar.lineEdit_8.text()
            senha = self.cadastrar.lineEdit_9.text()

            if not(nome == '' or sobrenome == '' or cpf == '' or numero == '' or limite == '' or senha == ''):
                cliente = Client(nome,sobrenome,cpf)
                c = Conta(numero, cliente, 0.0, limite, senha)
                if(self.cad.cadastra(c)):
                    QMessageBox.information(None, 'GP Bank', 'Cadastro realizado com sucesso!')
                    self.cadastrar.lineEdit.setText('')
                    self.cadastrar.lineEdit_4.setText('')
                    self.cadastrar.lineEdit_6.setText('')
                    self.cadastrar.lineEdit_7.setText('')
                    self.cadastrar.lineEdit_8.setText('')
                    self.cadastrar.lineEdit_9.setText('')
                else:
                    QMessageBox.information(None, 'GP Bank', 'CPF informado já existe!')
            else:
                QMessageBox.information(None, 'GP Bank', 'Todas as informações devem ser preenchidas!')
    

    def botaoEntrar(self):
        cpf = self.login.lineEdit.text()
        senha = self.login.lineEdit_2.text()

        conta = self.cad.busca_cpf(cpf)
        if(conta != None):
            if(self.si.login(conta, cpf, senha) == True):
                self.QtStack.setCurrentIndex(7)
                self.home.lineEdit.setText(str(conta.saldo))
                self.home.lineEdit_2.setText(str(conta.limite))


            else:
                QMessageBox.information(None, 'GP Bank', 'Login incorreto!')
                self.cadastrar.lineEdit.setText('')
                self.cadastrar.lineEdit_4.setText('')
        else:
            QMessageBox.information(None, 'GP Bank', 'Nenhuma conta cadastrada neste CPF!') 
            self.cadastrar.lineEdit.setText('')
            self.cadastrar.lineEdit_4.setText('')

    def botaoDeposita(self, conta):
        valor = 0.0
        valor = float(self.deposita.lineEdit_2.text())

        res = conta.deposita(valor)
        if res == False:
            QMessageBox.information(None, 'GP Bank', 'Valor inválido!')
        else:
            QMessageBox.information(None, 'GP Bank', 'Depósito efetuado!')    


    
    def abrirTelaHome(self):
        self.QtStack.setCurrentIndex(7)        

    def botaoExtrato(self):
        numero = self.extrato.lineEdit.text()
        conta = self.cad.busca(numero)
        if (conta != None):
            #self.extrato.lineEdit_2.setText(conta.historico)    
            self.extrato.lineEdit_3.setText(conta.titular.nome)
            self.extrato.lineEdit_4.setText(conta.titular.cpf)
            self.extrato.lineEdit_5.setText(conta.saldo)
        else:
            QMessageBox.information(None, 'GP Bank', 'Conta não encontrada!')

        self.extrato.pushButton_2.clicked.connect(self.botaoVoltar)
        
    def botaoSacar(self):
        valor = 0
        numero = self.deposita.lineEdit.text()
        valor = int(self.deposita.lineEdit_2.text())
        cliente = self.cad.busca(numero)

        if(cliente != None):
            res = cliente.saca(valor)
            if res == False:
                QMessageBox.information(None, 'GP Bank', 'Valor inválido!')
            else:
                QMessageBox.information(None, 'GP Bank', 'Saque efetuado!')
        else:
            QMessageBox.information(None,'GP Bank', 'Conta não encontrada!')

        self.QtStack.setCurrentIndex(0)

    def botaoTransfere(self):
        numero = self.transferencia.lineEdit.text()
        numero_dest = self.transferencia.lineEdit_3.text()
        valor = int(self.transferencia.lineEdit_2.text())
        cliente1 = self.cad.busca(numero)
        cliente2 =self.cad.busca(numero_dest)

        if(cliente1 != None and cliente2 != None):
            res = cliente1.transferencia(cliente2, valor)
            if res == False:
                QMessageBox.information(None, 'GP Bank', 'Valor inválido!')
            else:
                QMessageBox.information(None, 'GP Bank', 'Tranferencia efetuada!')
        else:
            QMessageBox.information(None,'GP Bank', 'Conta não encontrada!')

        self.QtStack.setCurrentIndex(0)


    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaDeposita(self):
        self.QtStack.setCurrentIndex(3)
    
    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(4)
    
    def abrirTelaSacar(self):
        self.QtStack.setCurrentIndex(5)

    def abrirTelaTransferencia(self):
        self.QtStack.setCurrentIndex(6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())