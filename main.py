
#Importamos librerias necesarias#
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
#Creamos la clase Calculator que hereda de QMainWindow#
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('calculator.ui', self)


        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(5)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Conectar botones a sus funciones correspondientes
        self.uno.clicked.connect(lambda: self.onButtonClick('1'))
        self.dos.clicked.connect(lambda: self.onButtonClick('2'))
        self.tres.clicked.connect(lambda: self.onButtonClick('3'))
        self.cuatro.clicked.connect(lambda: self.onButtonClick('4'))
        self.cinco.clicked.connect(lambda: self.onButtonClick('5'))
        self.seis.clicked.connect(lambda: self.onButtonClick('6'))
        self.siete.clicked.connect(lambda: self.onButtonClick('7'))
        self.ocho.clicked.connect(lambda: self.onButtonClick('8'))
        self.nueve.clicked.connect(lambda: self.onButtonClick('9'))
        self.cero.clicked.connect(lambda: self.onButtonClick('0'))
        self.sumar.clicked.connect(lambda: self.onButtonClick('+'))
        self.dividir.clicked.connect(lambda: self.onButtonClick('/'))
        self.restar.clicked.connect(lambda: self.onButtonClick('-'))
        self.multiplicar.clicked.connect(lambda: self.onButtonClick('*'))
        self.resultado.clicked.connect(self.calculateResult)
        self.vaciar.clicked.connect(self.clearDisplay)


#Funciones#
    def onButtonClick(self, text):
        current_text = self.mostrar.text()
        new_text = current_text + text
        self.mostrar.setText(new_text)

    def calculateResult(self):
        try:
            result = eval(self.mostrar.text())
            self.mostrar.setText(str(result))
        except Exception as e:
            self.mostrar.setText(' Error ')

    def clearDisplay(self):
        self.mostrar.clear()

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
