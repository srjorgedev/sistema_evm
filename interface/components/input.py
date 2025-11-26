import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, QLineEdit
)
from PyQt6.QtCore import Qt, pyqtSignal, QRegularExpression
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor, QRegularExpressionValidator
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.styles.general import COLORS, COLORS_LIST

class InputWidget(QWidget):
    def __init__(self, text, pattern=None, password=False):
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        label = QLabel(text)
        self.input_field = QLineEdit()
        
        self.input_field.setFixedHeight(40) 
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(5) 
        
        label.setStyleSheet(f"color:  {COLORS_LIST[COLORS.TEXTO_OSCURO]}; font-size: 16px;")
        self.input_field.setStyleSheet(f"""
            QLineEdit {{
                background-color:  {COLORS_LIST[COLORS.BG_CLARO_2]}; 
                border: 1px solid {COLORS_LIST[COLORS.BG_OSCURO_2]};
                border-radius: 4px;
                padding: 8px;
                color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};
                font-size: 14px;
            }}
            QLineEdit:focus {{
                border: 1px solid #3b82f6;
            }}
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