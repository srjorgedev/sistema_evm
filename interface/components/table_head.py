from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

class TableHeadWidget(QFrame):
    def __init__(self, text):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.setFixedHeight(48)
        
        self.main_layout = QHBoxLayout(self)
        label = QLabel(text)     
        
        label.setStyleSheet("font-size: 18px; font-weight: normal; color: #f1f1f1;")
        self.setStyleSheet("background-color: #17272f;")
        
        self.main_layout.addWidget(label)