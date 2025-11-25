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
        
        if text in ["N°", "N", "ID"]:
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if text.upper() == "N° SERIE":
            label.setContentsMargins(16,0,0,0)
        
        label.setStyleSheet("font-size: 16px; font-weight: bold; color: #f1f1f1;")
        self.setStyleSheet("background-color: transparent;")
        
        self.main_layout.addWidget(label)