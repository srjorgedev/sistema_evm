import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget
from pathlib import Path

direction = Path(__file__)
folder = direction.parent.parent

class MenuButtonWidget(QFrame):
    clicked = pyqtSignal()

    def __init__(self, texto, icono):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.setMinimumHeight(48) 
        
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.inner_frame = QFrame()
        self.inner_frame.setObjectName("InnerButton")
        self.inner_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.inner_frame.setFixedSize(240, 44) 
        
        self.layout_interno = QHBoxLayout(self.inner_frame)
        self.layout_interno.setContentsMargins(12, 0, 12, 0)
        self.layout_interno.setSpacing(8)
        
        self.icon = QSvgWidget()
        self.label_texto = QLabel(texto)
        
        icon_path = folder / "assets" / "icons" / f"{icono}.svg"
        self.icon.load(str(icon_path))
        
        self.icon.setFixedSize(24, 24) 
        self.icon.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

        self.layout_interno.addWidget(self.icon)
        self.layout_interno.addWidget(self.label_texto, 1) 
        
        self.layout_externo = QHBoxLayout(self)
        self.layout_externo.setContentsMargins(0, 0, 0, 0)
        self.layout_externo.addStretch()
        self.layout_externo.addWidget(self.inner_frame)
        self.layout_externo.addStretch()
        
        self._active = False
        self.setProperty("active", self._active)
        self.inner_frame.setProperty("active", self._active)

        self.setStyleSheet("""
            /* Widget Padre (256px) */
            MenuButtonWidget {
                background-color: transparent;
            }
            MenuButtonWidget[active="true"] {
                background-color: #C030C0; /* Fondo morado activo */
            }

            /* Widget Hijo (240px) */
            MenuButtonWidget #InnerButton {
                background-color: none;
                border: 1px solid #5A5F6B; /* Borde inactivo */
                border-radius: 2px;
            }
            MenuButtonWidget[active="true"] #InnerButton {
                border-color: transparent; /* Oculta el borde si está activo */
            }

            /* Reglas de Hover (SOLO para botones INACTIVOS) */
            MenuButtonWidget[active="false"]:hover {
                background-color: #009AD3; /* Fondo azul en hover */
            }
            MenuButtonWidget[active="false"]:hover #InnerButton {
                border-color: transparent; /* Oculta el borde en hover */
            }

            /* Reglas de Texto */
            MenuButtonWidget #InnerButton QLabel {
                color: #f1f1f1; /* Texto blanco (default e inactivo) */
            }
            
            /* Texto activo (blanco, como en tu imagen) */
            MenuButtonWidget[active="true"] #InnerButton QLabel {
                color: #f1f1f1;
            }
        """)

    def set_active(self, is_active):
        self._active = is_active
        self.setProperty("active", self._active)
        self.inner_frame.setProperty("active", is_active)
        
        self.style().polish(self)
        self.style().unpolish(self)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)