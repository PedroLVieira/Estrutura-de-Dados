from PyQt5 import QtCore, QtGui, QtWidgets, uic
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 385)
        MainWindow.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entrar_inicial = QtWidgets.QPushButton(self.centralwidget)
        self.entrar_inicial.setGeometry(QtCore.QRect(210, 270, 121, 51))
        self.entrar_inicial.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"font: sans-serif;")
        self.entrar_inicial.setObjectName("entrar_inicial")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.senha_inicial = QtWidgets.QLineEdit(self.centralwidget)
        self.senha_inicial.setGeometry(QtCore.QRect(200, 170, 151, 31))
        self.senha_inicial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.senha_inicial.setObjectName("senha_inicial")
        self.login_inicial = QtWidgets.QLineEdit(self.centralwidget)
        self.login_inicial.setGeometry(QtCore.QRect(200, 90, 151, 31))
        self.login_inicial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.login_inicial.setObjectName("login_inicial")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.login_erro = QtWidgets.QLabel(self.centralwidget)
        self.login_erro.setGeometry(QtCore.QRect(190, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_erro.setFont(font)
        self.login_erro.setText("")
        self.login_erro.setObjectName("login_erro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.login_inicial, self.senha_inicial)
        MainWindow.setTabOrder(self.senha_inicial, self.entrar_inicial)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.entrar_inicial.setText(_translate("MainWindow", "Entrar"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.label_3.setText(_translate("MainWindow", "Login"))


config = {
    'user': 'root',
    'password': 'pedro12510',
    'host': '127.0.0.1',
    'port':'3306',
    'database': 'agenda'
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def checklogin():
    tela_inicial.login_erro.setText("")
    user = tela_inicial.login_inicial.text()
    password = tela_inicial.senha_inicial.text()
    cursor.execute("""
                   
                   SELECT * FROM admin;
                   
                   """)

    try:
        for linha in cursor.fetchall():
            if linha[1] == user and linha[2] == password:
                tipo = "admin"
            else:
                cursor.execute("""
                               
                    SELECT * FROM user;
                    
                    """)
                if linha[2] == user and linha[3] == password:
                    tipo = "user"
        if tipo == "admin":
            tela_inicial.hide()
            tabela.show()
        elif tipo == "user":
            tela_inicial.hide()
            tabela.show()
    except:
        tela_inicial.login_erro.setText("Login ou Senha Incorretos")

app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi("tela_inicial.ui")
tabela=uic.loadUi("tabela.ui")
tela_inicial.entrar_inicial.clicked.connect(checklogin)
tela_inicial.senha_inicial.setEchoMode(QtWidgets.QLineEdit.Password)
tela_inicial.show()
app.exec()