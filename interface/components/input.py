import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, QLineEdit
)
from PyQt6.QtCore import Qt, pyqtSignal, QRegularExpression
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor, QRegularExpressionValidator
from PyQt6.QtSvgWidgets import QSvgWidget

class InputWidget(QWidget):
    def __init__(self, text, pattern=None, password=False):
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        label = QLabel(text)
        self.input_field = QLineEdit()
        
        self.input_field.setFixedHeight(40) 
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(5) 
        
        label.setStyleSheet("color: #f1f1f1; font-size: 16px;")
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #0f172a; 
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 8px;
                color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3b82f6;
            }
        """)
        
        if password: 
            self.input_field.setEchoMode(QLineEdit.EchoMode.Password)
        
        if pattern: 
            regex = QRegularExpressionValidator(QRegularExpression(pattern), self)
            self.input_field.setValidator(regex)
        
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(self.input_field)
        
    def get_text(self):
        return self.input_field.text()
        
    def set_text(self, text):
        self.input_field.setText(text)