import sys
import os

from PyQt5 import QtCore, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication


from interfaces.tela_cadastrar import 
from interfaces. import 
from interfaces. import 
from interfaces. import 
from interfaces. import 

from src.cadastro import Cadastro
from src.conta import Conta
from src.cliente import Client


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

        self.principal = Principal()
        self.principal.setupUi(self.stack0)

        self.deposita = Deposita()
        self.deposita.setupUi(self.stack1)

        self.extrato = Extrato()
        self.extrato.setupUi(self.stack2)

        self.saque = Saque()
        self.saque.setupUi(self.stack3)

        self.transferencia = Transferencia()
        self.transferencia.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.principal.pushButton_2.clicked.connect(self.abrirTelaDeposita)
        self.principal.pushButton_3.clicked.connect(self.abrirTelaSacar)
        self.principal.pushButton_4.clicked.connect(self.abrirTelaTransferencia)
        self.principal.pushButton_5.clicked.connect(self.abrirTelaExtrato)

        self.principal.pushButton.clicked.connect(self.botaoOk)
        self.deposita.pushButton.clicked.connect(self.botaoDeposita)
        self.saque.pushButton.clicked.connect(self.botaoSacar)
        self.transferencia.pushButton.clicked.connect(self.botaoTransfere)
        self.extrato.pushButton.clicked.connect(self.botaoExtrato)

    def botaoOk(self):
        nome = self.principal.lineEdit.text()
        sobrenome = self.principal.lineEdit_4.text()
        cpf = self.principal.lineEdit_6.text()
        numero = self.principal.lineEdit_7.text()
        limite = self.principal.lineEdit_8.text()

        if not(nome == '' or sobrenome == '' or cpf == '' or numero == '' or limite == ''):
            cliente = Client(nome,sobrenome,cpf)
            c = Conta(numero,cliente,0,limite)
            if(self.cad.cadastra(c)):
                QMessageBox.information(None, 'GP Bank', 'Cadastro realizado com sucesso!')
                self.principal.lineEdit.setText('')
                self.principal.lineEdit_4.setText('')
                self.principal.lineEdit_6.setText('')
                self.principal.lineEdit_7.setText('')
                self.principal.lineEdit_8.setText('')
            else:
                QMessageBox.information(None, 'GP Bank', 'CPF informado já existe!')
        else:
            QMessageBox.information(None, 'GP Bank', 'Todas as informações devem ser preenchidas!')
        

    def botaoDeposita(self):
        valor = 0
        numero = self.deposita.lineEdit.text()
        valor = int(self.deposita.lineEdit_2.text())
        cliente = self.cad.busca(numero)
        if(cliente != None):

            res = cliente.deposita(valor)
            if res == False:
                QMessageBox.information(None, 'GP Bank', 'Valor inválido!')
            else:
                QMessageBox.information(None, 'GP Bank', 'Depósito efetuado!')    

        else:
            QMessageBox.information(None,'GP Bank', 'Conta não encontrada!')

        self.QtStack.setCurrentIndex(0)
        #self.tela_buscar.pushButton_2.clicked.connect(self.botaoVoltar)

    #corrigir forma de mostrar extrato
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

        self.extrato.pushButton_2.clicked.conne ct(self.botaoVoltar)
        
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

    def abrirTelaDeposita(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(2)
    
    def abrirTelaSacar(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaTransferencia(self):
        self.QtStack.setCurrentIndex(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())