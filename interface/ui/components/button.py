from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy, 
                             QFrame, QVBoxLayout)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QCursor, QColor
from pathlib import Path
from enum import Enum

direction = Path(__file__)
folder = direction.parent.parent.parent.parent

class ColorKeys(Enum):
    CREAR = "crear"
    MODIFICAR = "mod"
    ARCHIVAR = "archivar"

colors = {
    ColorKeys.ARCHIVAR: "#EF4444",
    ColorKeys.CREAR: "#22C55E",
    ColorKeys.MODIFICAR: "#fbff85"
}

class ButtonWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, icono, texto, color: ColorKeys):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(64)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.button_frame = QFrame()
        self.button_frame.setObjectName("btnFrame") 
        
        self.inner_layout = QHBoxLayout(self.button_frame)
        self.inner_layout.setContentsMargins(24, 0, 16, 0)
        self.inner_layout.setSpacing(16)

        self.icon_widget = QSvgWidget()
        self.icon_widget.setFixedSize(24, 24) 
        
        icon_path = folder / "public" / "icons" / f"{icono}.svg"
        if icon_path.exists():
            self.icon_widget.load(str(icon_path))
        else:
            print(f"Warning: Icono no encontrado en {icon_path}")

        self.text_label = QLabel(texto)
        self.text_label.setObjectName("btnText")

        self.text_label.setStyleSheet("font-size: 18px; font-weight: 500; color: #C1C1C1; border: none;")

        self.inner_layout.addWidget(self.icon_widget)
        self.inner_layout.addWidget(self.text_label)
        self.inner_layout.addStretch() 

        self.main_layout.addWidget(self.button_frame)

        c = QColor(colors[color])
        r, g, b = c.red(), c.green(), c.blue()

        alpha_normal = 0.25  
        alpha_hover = 0.5  

        self.setStyleSheet(f"""
            #btnFrame {{ 
                border-radius: 8px;
                /* Usamos RGBA: El estándar universal para transparencias */
                background-color: rgba({r}, {g}, {b}, {alpha_normal});
                border: 1px solid rgba({r}, {g}, {b}, 0.75); /* Borde sólido del color original */
            }}

            #btnFrame:hover {{
                background-color: rgba({r}, {g}, {b}, {alpha_hover});
            }}

            /* Estilos de texto e iconos */
            QLabel {{
                background-color: transparent;
                border: none;
                color: #C1C1C1;
                font-size: 18px; 
                font-weight: 500;
            }}
            
            QSvgWidget {{
                background-color: transparent;
                border: none;
            }}
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit() 
            event.accept()
        else:
            super().mousePressEvent(event)