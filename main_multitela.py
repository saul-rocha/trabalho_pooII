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

        self.tela_main_menu = Principal()
        self.tela_main_menu.setupUi(self.stack0)

        self.tela_login = Login()
        self.tela_login.setupUi(self.stack1)

        self.tela_cadastrar = Cadastrar()
        self.tela_cadastrar.setupUi(self.stack2)

        self.tela_deposita = Deposita()
        self.tela_deposita.setupUi(self.stack3)

        self.tela_extrato = Extrato()
        self.tela_extrato.setupUi(self.stack4)

        self.tela_saque = Saque()
        self.tela_saque.setupUi(self.stack5)

        self.tela_transferencia = Transferencia()
        self.tela_transferencia.setupUi(self.stack6)

        self.tela_home = Home()
        self.tela_home.setupUi(self.stack7)

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

        self.tela_main_menu.pushButton.clicked.connect(self.abrirTelaLogin)
        self.tela_main_menu.pushButton_2.clicked.connect(self.abrirTelaCadastro)

        self.tela_login.pushButton.clicked.connect(self.botaoEntrar)
        self.tela_login.pushButton_2.clicked.connect(self.botaoVoltar)

        self.tela_cadastrar.pushButton.clicked.connect(self.botaoOk)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.botaoVoltar)

        self.tela_home.pushButton_2.clicked.connect(self.abrirTelaDeposita)
        self.tela_deposita.pushButton.clicked.connect(self.botaoDeposita)
        self.tela_deposita.pushButton_2.clicked.connect(self.abrirTelaHome)


        self.tela_home.pushButton.clicked.connect(self.botaoSacar)
        self.tela_home.pushButton_3.clicked.connect(self.botaoExtrato)
        self.tela_home.pushButton_4.clicked.connect(self.botaoTransfere)
        
       

        self.tela_saque.pushButton.clicked.connect(self.botaoSacar)
        self.tela_saque.pushButton_2.clicked.connect(self.botaoVoltar)

        self.tela_transferencia.pushButton.clicked.connect(self.botaoTransfere)
        self.tela_transferencia.pushButton_2.clicked.connect(self.botaoVoltar)

        self.tela_home.pushButton_5.clicked.connect(self.botaoVoltar)

        #self.tela_extrato.pushButton.clicked.connect(self.botaoExtrato)
        #self.tela_extrato.pushButton_2.clicked.connect(self.botaoVoltar)


    def botaoOk(self):
            nome = self.tela_cadastrar.lineEdit.text()
            sobrenome = self.tela_cadastrar.lineEdit_4.text()
            cpf = self.tela_cadastrar.lineEdit_6.text()
            numero = self.tela_cadastrar.lineEdit_7.text()
            limite = self.tela_cadastrar.lineEdit_8.text()
            senha = self.tela_cadastrar.lineEdit_9.text()

            if not(nome == '' or sobrenome == '' or cpf == '' or numero == '' or limite == '' or senha == ''):
                cliente = Client(nome,sobrenome,cpf)
                c = Conta(numero, cliente, 0.0, limite, senha)
                if(self.cad.cadastra(c)):
                    QMessageBox.information(None, 'GP Bank', 'Cadastro realizado com sucesso!')
                    self.tela_cadastrar.lineEdit.setText('')
                    self.tela_cadastrar.lineEdit_4.setText('')
                    self.tela_cadastrar.lineEdit_6.setText('')
                    self.tela_cadastrar.lineEdit_7.setText('')
                    self.tela_cadastrar.lineEdit_8.setText('')
                    self.tela_cadastrar.lineEdit_9.setText('')
                else:
                    QMessageBox.information(None, 'GP Bank', 'CPF informado já existe!')
            else:
                QMessageBox.information(None, 'GP Bank', 'Todas as informações devem ser preenchidas!')


    def botaoEntrar(self):
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        conta = self.cad.busca_cpf(cpf)
        if(conta != None):
            if(self.si.login(conta, cpf, senha) == True):
                self.QtStack.setCurrentIndex(7)
                self.tela_home.lineEdit.setText(str(conta.saldo))
                self.tela_home.lineEdit_2.setText(str(conta.limite))

            else:
                
                QMessageBox.information(None, 'GP Bank', 'Login incorreto!')
                
        else:
            QMessageBox.information(None, 'GP Bank', 'Nenhuma conta cadastrada neste CPF!') 

        #self.tela_login.lineEdit.setText('')
        #self.tela_login.lineEdit_2.setText('')

    def botaoDeposita(self):
        valor = 0.0
        valor = self.tela_deposita.lineEdit_2.text()

        cpf = self.tela_login.lineEdit.text()
        conta = self.cad.busca_cpf(cpf)
        res = conta.deposita(valor)

        if res == False:
            QMessageBox.information(None, 'GP Bank', 'Valor inválido!')
        else:
            QMessageBox.information(None, 'GP Bank', 'Depósito efetuado!')   

        self.tela_home.lineEdit.setText(str(conta.saldo))
        self.tela_home.lineEdit_2.setText(str(conta.limite)) 


    def botaoExtrato(self):
        numero = self.tela_extrato.lineEdit.text()
        conta = self.cad.busca(numero)
        if (conta != None):
            #self.tela_extrato.lineEdit_2.setText(conta.historico)    
            self.tela_extrato.lineEdit_3.setText(conta.titular.nome)
            self.tela_extrato.lineEdit_4.setText(conta.titular.cpf)
            self.tela_extrato.lineEdit_5.setText(conta.saldo)
        else:
            QMessageBox.information(None, 'GP Bank', 'Conta não encontrada!')

        self.tela_extrato.pushButton_2.clicked.connect(self.botaoVoltar)
        
    def botaoSacar(self):
        valor = 0
        numero = self.tela_deposita.lineEdit.text()
        valor = int(self.tela_deposita.lineEdit_2.text())
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
        numero = self.tela_transferencia.lineEdit.text()
        numero_dest = self.tela_transferencia.lineEdit_3.text()
        valor = int(self.tela_transferencia.lineEdit_2.text())
        cliente1 = self.cad.busca(numero)
        cliente2 =self.cad.busca(numero_dest)

        if(cliente1 != None and cliente2 != None):
            res = cliente1.tela_transferencia(cliente2, valor)
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

    def abrirTelaHome(self):
        self.QtStack.setCurrentIndex(7)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())