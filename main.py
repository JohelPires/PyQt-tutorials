import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


def botao1():
    label.setText('Você clicou no botão 1')
    label.adjustSize()


def botao2():
    label.setText('Você clicou no botão 2')
    label.adjustSize()


def botao3():
    texto = le.text()
    label.setText(texto)
    label.adjustSize()


app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800, 600)
janela.setWindowTitle('This is some title')

btn1 = QPushButton('Botão 1', janela)
btn1.setGeometry(100, 100, 100, 20)
btn1.clicked.connect(botao1)

btn2 = QPushButton('Botão 2', janela)
btn2.setGeometry(100, 130, 100, 20)
btn2.clicked.connect(botao2)

btn3 = QPushButton('Botão 3', janela)
btn3.setGeometry(100, 160, 100, 20)
btn3.clicked.connect(botao3)

label = QLabel('This is some label', janela)
label.setGeometry(100, 10, 200, 20)

le = QLineEdit('insert something', janela)
le.setGeometry(210, 160, 100, 20)
le.textChanged.connect(botao3)

janela.show()

app.exec()
