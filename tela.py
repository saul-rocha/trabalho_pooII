# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from src.cadastro import Cadastro
from src.cliente import Client
from src.conta import Conta
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 50, 232, 58))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Depósito"))
        self.pushButton.setText(_translate("Form", "Depositar"))
        self.label.setText(_translate("Form", "Nº da Conta"))
        self.label_2.setText(_translate("Form", "Valor"))

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(790, 480)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 20))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 280, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Frame)
        self.widget.setGeometry(QtCore.QRect(170, 360, 447, 61))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(Frame)
        self.widget1.setGeometry(QtCore.QRect(230, 60, 331, 209))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nome = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        self.nome.setFont(font)
        self.nome.setAlignment(QtCore.Qt.AlignCenter)
        self.nome.setObjectName("nome")
        self.gridLayout_3.addWidget(self.nome, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 4, 1, 1, 1)
        self.limite = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        self.limite.setFont(font)
        self.limite.setObjectName("limite")
        self.gridLayout_3.addWidget(self.limite, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.sobrenome = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        self.sobrenome.setFont(font)
        self.sobrenome.setObjectName("sobrenome")
        self.gridLayout_3.addWidget(self.sobrenome, 1, 0, 1, 1)
        self.numero = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        self.numero.setFont(font)
        self.numero.setObjectName("numero")
        self.gridLayout_3.addWidget(self.numero, 3, 0, 1, 1)
        self.cpf = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        self.cpf.setFont(font)
        self.cpf.setAlignment(QtCore.Qt.AlignCenter)
        self.cpf.setObjectName("cpf")
        self.gridLayout_3.addWidget(self.cpf, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)


        '''modifics'''
        self.cad = Cadastro()
        self.pushButton.clicked.connect(self.botaoCadastra)

    def botaoCadastra(self):
        nome = self.lineEdit.text()
        sobrenome = self.lineEdit_4.text()
        cpf = self.lineEdit_6.text()
        numero = self.lineEdit_7.text()
        limite = self.lineEdit_8.text()
       
        if not(nome == '' or sobrenome == '' or cpf == '' or numero == ''or limite == ''):
            p = Client(nome, sobrenome, cpf)
            c = Conta(numero, p,0,limite)
            if(self.cad.cadastra(c)):
                QMessageBox.information(None, 'POOII', 'Conta criada com sucesso!')
                self.lineEdit.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_6.setText('')
                self.lineEdit_7.setText('')
                self.lineEdit_8.setText('')
            else:
                QMessageBox.information(None, 'POOII', 'Conta informada já existe!')
        else:
            QMessageBox.information(None, 'POOII', 'Todas as informações devem ser preenchidas!')
        


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "GP Bank"))
        self.label.setText(_translate("Frame", "Abrir Conta"))
        self.pushButton.setText(_translate("Frame", "OK"))
        self.pushButton_2.setText(_translate("Frame", "Depositar"))
        self.pushButton_3.setText(_translate("Frame", "Sacar"))
        self.pushButton_5.setText(_translate("Frame", "Extrato"))
        self.pushButton_4.setText(_translate("Frame", "Transferência"))
        self.nome.setText(_translate("Frame", "Nome"))
        self.limite.setText(_translate("Frame", "Limite"))
        self.sobrenome.setText(_translate("Frame", "Sobrenome"))
        self.numero.setText(_translate("Frame", "Número"))
        self.cpf.setText(_translate("Frame", "CPF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())