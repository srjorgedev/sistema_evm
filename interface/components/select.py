from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy, 
                             QFrame, QVBoxLayout, QListWidget)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QCursor, QColor


class SelectWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main