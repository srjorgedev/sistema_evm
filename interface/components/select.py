from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QComboBox)
from PyQt6.QtCore import pyqtSignal

from interface.components.styles.general import COLORS, COLORS_LIST

class SelectWidget(QWidget):
    change = pyqtSignal(object)
    
    def __init__(self, text, placeholder = None):
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        self.label = QLabel(text)
        self.combobox = QComboBox()
        
        if placeholder: self.combobox.setPlaceholderText(placeholder)
        self.main_layout.setContentsMargins(0,0,0,0)
        
        self.label.setStyleSheet(f"color: {COLORS_LIST[COLORS.TEXTO_OSCURO]}; font-size: 16px;")
        self.combobox.setStyleSheet(f"""
            QComboBox {{
                background-color: #0f172a; 
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 8px;
                color: white;
                font-size: 14px;
                padding-right: 30px;
            }}
            QComboBox:focus {{
                border: 1px solid #3b82f6;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px; /* Un poco más ancho para centrar mejor */
                border: none;
                background: transparent;
            }}
            QComboBox::down-arrow {{
                image: none; 
                width: 0px; 
                height: 0px; 

                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid #ffffff;

                subcontrol-position: center;
                margin-right: 5px;
            }}
            QComboBox QAbstractItemView {{
                background-color: #2b2b2b; 
                color: #c1c1c1;           
                selection-background-color: #3b82f6; 
                selection-color: #f1f1f1;  
                outline: 0px;          
            }}
        """)
        
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.combobox)
        
        self.combobox.currentIndexChanged.connect(self.emit_data)
        
    def addItems(self, data: list[tuple[str, any]]):
        self.combobox.clear() 
        
        for item in data: 
            self.combobox.addItem(str(item[0]), str(item[1]))
            
    def addItem(self, data: tuple[str, any]):
        self.combobox.addItem(str(data[0]), data[1])
            
    def emit_data(self):
        id_seleccionado = self.combobox.currentData()
        self.change.emit(id_seleccionado)

    def obtenerID(self):
        return self.combobox.currentData()

    def obtenerTexto(self):
        return self.combobox.currentText()