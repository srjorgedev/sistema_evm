import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class Pantalla(QMainWindow):
   
    def __init__(self):
        super(Pantalla, self).__init__()
        uic.loadUi('interface/ui/main.ui',self)
       
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Pantalla()
    d.show()
    sys.exit(app.exec())