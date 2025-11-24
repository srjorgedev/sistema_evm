import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.input import InputWidget
from interface.components.select import SelectWidget

class SalidaFormWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout_v = QVBoxLayout(self)
        self.select_ = SelectWidget("HI")
        layout_h = QHBoxLayout()
        desc = QLabel("Completa los detalles del nuevo registro. \nTodos los campos son obligatorios.")
        title = QLabel("Crear un nuevo registro de salida")
    
        self.layout_v.setContentsMargins(0, 0, 0, 0) 
        self.layout_v.setSpacing(8) 
        layout_h.setSpacing(16)
        
        title.setStyleSheet("font-size: 32px; font-weight: bold; color: white;")
        desc.setStyleSheet("font-size: 16px; font-weight: normal; color: #c1c1c1;")
        
        self.select_.addItems([("Opción A", 1), ("Opción B", 2), ("Opción C", 2)])
        self.select_.change.connect(lambda e: print(f"Cambió a: {e}"))
        
        layout_h.addWidget(InputWidget("Asunto", r"^[a-zA-z\s,.]{0,50}$"))
        layout_h.addWidget(InputWidget("Destino", r"^[a-zA-z\s,.]{0,50}$"))
        
        self.layout_v.addWidget(title)
        self.layout_v.addWidget(desc)
        self.layout_v.addLayout(layout_h)
        self.layout_v.addWidget(self.select_)
        
        self.layout_v.addStretch()