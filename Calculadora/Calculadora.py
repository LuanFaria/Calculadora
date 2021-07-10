import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow, QBoxLayout
from PyQt5.QtWidgets import QLineEdit, QSizePolicy
import time


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 500)  # Serve para Fixar o tamanho (largura X altura)
        self.setWindowTitle('Calculadora (Luan)')
        self.centro = QWidget()
        self.grade = QGridLayout(self.centro)

        self.display = QLineEdit()  # Formatando o Display
        self.grade.addWidget(self.display, 0, 0, 1, 4)  # Posição do Display

        self.display.setDisabled(True)  # Tira a opção de editar o campo
        self.setStyleSheet(
            '* {background: #1E90FF; color:#000; font-size: 35px,}'  # Formatação em CSS
        )
        self.display.setStyleSheet(
            '* {background: #B0E0E6; color:#000; font-size: 35px,}'  # Formatação em CSS
        )

        # Expande o display para completar o resto da tela.
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.botao0 = QPushButton('0')
        self.botao1 = QPushButton('1')
        self.botao2 = QPushButton('2')
        self.botao3 = QPushButton('3')
        self.botao4 = QPushButton('4')
        self.botao5 = QPushButton('5')
        self.botao6 = QPushButton('6')
        self.botao7 = QPushButton('7')
        self.botao8 = QPushButton('8')
        self.botao9 = QPushButton('9')
        self.botaox = QPushButton('X')
        self.botao_barra = QPushButton('/')
        self.botao_soma = QPushButton('+')
        self.botao_sub = QPushButton('-')
        self.botao_igual = QPushButton('=')
        self.botao_limpa = QPushButton('CE')
        self.botao_ponto = QPushButton('.')
        self.botao_exp = QPushButton('EXP')
        self.botao_ap = QPushButton('DEL')
        self.botao_off = QPushButton('OFF')

        self.caixa = QBoxLayout

        self.botao_limpa.setStyleSheet(
            '* {background: #FF0000}'  # Formatação em CSS
        )
        self.botao_off.setStyleSheet(
            '* {background: #FF0000}'  # Formatação em CSS
        )
        self.botao_igual.setStyleSheet(
            '* {background: Darkblue}'  # Formatação em CSS
        )
        self.grade.addWidget(self.botao_limpa, 1, 0)
        self.grade.addWidget(self.botao0, 5, 0)
        self.grade.addWidget(self.botao1, 4, 0)
        self.grade.addWidget(self.botao2, 4, 1)
        self.grade.addWidget(self.botao3, 4, 2)
        self.grade.addWidget(self.botao4, 3, 0)
        self.grade.addWidget(self.botao5, 3, 1)
        self.grade.addWidget(self.botao6, 3, 2)
        self.grade.addWidget(self.botao7, 2, 0)
        self.grade.addWidget(self.botao8, 2, 1)
        self.grade.addWidget(self.botao9, 2, 2)
        self.grade.addWidget(self.botaox, 2, 3)
        self.grade.addWidget(self.botao_barra, 3, 3)
        self.grade.addWidget(self.botao_sub, 4, 3)
        self.grade.addWidget(self.botao_soma, 1, 3)
        self.grade.addWidget(self.botao_igual, 5, 3)
        self.grade.addWidget(self.botao_ponto, 5, 1)
        self.grade.addWidget(self.botao_exp, 5, 2)
        self.grade.addWidget(self.botao_ap, 1, 2)
        self.grade.addWidget(self.botao_off, 1, 1)

        self.setCentralWidget(self.centro)

        self.botao_limpa.clicked.connect(self.Limpar)
        self.botao_ap.clicked.connect(self.Apaga_um)
        self.botao0.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao0.text()))
        self.botao1.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao1.text()))
        self.botao2.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao2.text()))
        self.botao3.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao3.text()))
        self.botao4.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao4.text()))
        self.botao5.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao5.text()))
        self.botao6.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao6.text()))
        self.botao7.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao7.text()))
        self.botao8.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao8.text()))
        self.botao9.clicked.connect(lambda: self.display.setText(self.display.text() + self.botao9.text()))
        self.botao_exp.clicked.connect(lambda: self.display.setText(self.display.text() + '**'))
        self.botao_ponto.clicked.connect(lambda: self.display.setText(self.display.text() + '.'))
        self.botao_off.clicked.connect(self.Desligar)
        self.botaox.clicked.connect(self.Mult)
        self.botao_barra.clicked.connect(self.Div)
        self.botao_soma.clicked.connect(self.Soma)
        self.botao_sub.clicked.connect(self.Sub)
        self.botao_igual.clicked.connect(self.Resultado)

    ################################################################################

    def Soma(self):
        self.display.setText(self.display.text() + self.botao_soma.text())
        # self._resultado = valor_1 + valor_2

    def Sub(self):
        self.display.setText(self.display.text() + self.botao_sub.text())
        # self._resultado = valor_1 - valor_2

    def Mult(self):
        self.display.setText(self.display.text() + '*')
        # self._resultado = valor_1 * valor_2

    def Div(self):
        self.display.setText(self.display.text() + self.botao_barra.text())
        # self._resultado = valor_1 / valor_2

    def Limpar(self):
        self.display.setText('')

    def Resultado(self):
        # self.display.setText(self.display.text() + self.botao_igual.text())
        # Linha anterior mostra o simbolo " = " na tela, está dando ERROR!!
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except:
            self.display.setText('Conta inválida!!')

    def Apaga_um(self):
        self.display.setText(self.display.text()[:-1])  # Printa tudo na tela e depois remove o ultimo caracter.

    def Desligar(self):
        try:
            self.display.setText('Desligando')
            time.sleep(0.5)
        except NameError:
            print('ERROR:')
        finally:
            quit()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
