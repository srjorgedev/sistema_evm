from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy, 
                             QFrame, QVBoxLayout)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QCursor, QColor
from pathlib import Path
from enum import Enum

direction = Path(__file__)
folder = direction.parent.parent

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
        
        # Asignacion de atributos
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Atributo: FONDO TRANSPARENTE
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)            # Atributo: HOVER 
        
        # Asignacion de dimensiones
        # Reglas de las dimensiones. Anchura - Preferred: se expande si hay espacio. Altura - Fixed: No se expande
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed) 
        self.setMinimumHeight(64) # Minimo de altura de 64 unidades
        
        # Cambia el cursor 
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) # Cursor del puntero
        
        # Creacion de elementos hijos
        self.main_layout = QVBoxLayout(self)                        # Layout vertical
        self.button_frame = QFrame()                                # Un contenedor     
        self.inner_layout = QHBoxLayout(self.button_frame)          # layout horizontal
        self.icon_widget = QSvgWidget()                             # SVG para iconos
        self.text_label = QLabel(texto)                             # Texto
        
        # Propiedadess y atributos                      
        self.main_layout.setContentsMargins(0, 0, 0, 0)             # Margenes entre el borde y los hijos en 0
        self.main_layout.setSpacing(0)                              # Espaciado entre los elementos hijos en 0

        self.button_frame.setObjectName("btnFrame")                 # Nombre para los estilos
        
        self.inner_layout.setContentsMargins(24, 0, 16, 0)          # Margenes entre el borde y los hijos
        self.inner_layout.setSpacing(16)                            # Espaciado entre los elementos hijos en 16

        self.icon_widget.setFixedSize(24, 24)                       # Tamaño inmutable para el icono
        
        # Estilos
        self.text_label.setStyleSheet("font-size: 18px; font-weight: 500; color: #C1C1C1; border: none;")
        
        icon_path = folder / "assets" / "icons" / f"{icono}.svg"    # Ruta del svg
        if icon_path.exists():
            self.icon_widget.load(str(icon_path))
        else:
            print(f"Warning: Icono no encontrado en {icon_path}")

        # Acomodar los elementos en el layout horizontal
        self.inner_layout.addWidget(self.icon_widget)
        self.inner_layout.addWidget(self.text_label)
        self.inner_layout.addStretch() 

        # Acomodar el layout horizontal en el layout vertical
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