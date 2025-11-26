from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFrame, QLabel, QHBoxLayout,
                            QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QRect, pyqtSignal
from PyQt6.QtGui import QColor

from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget

from interface.components.styles.general import COLORS, COLORS_LIST

class ModalWidget(QWidget):
    close = pyqtSignal()
    save = pyqtSignal()
    
    def __init__(self, parent=None, widget_contenido=None, titulo="", boton = None):
        super().__init__(parent)
        
        self.porcentaje_ancho = 0.75
        self.porcentaje_alto = 0.80

        self.setVisible(False)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        
        self.contenedor = QFrame(self) 
        self.contenedor.setStyleSheet(f"""
            QFrame {{
                background-color: {COLORS_LIST[COLORS.BG_CLARO_3]}; 
                border-radius: 10px;
            }}
        """)
        
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(30)
        sombra.setYOffset(10)
        sombra.setColor(QColor(0, 0, 0, 150))
        self.contenedor.setGraphicsEffect(sombra)

        self.layout_tarjeta = QVBoxLayout(self.contenedor)
        self.layout_tarjeta.setContentsMargins(32, 32, 32, 32)
        self.layout_tarjeta.setSpacing(16)
        
        self.header = QHBoxLayout()
        
        title = QLabel(titulo)
        title.setStyleSheet(f"font-size: 24px; font-weight: bold; color:  {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        
        self.btn_cerrar = SquareButtonWidget("close", "#cc1c11", 36)
        self.btn_cerrar.clicked.connect(self.hide_modal)
        
        self.header.addWidget(title)
        self.header.addStretch()
        self.header.addWidget(self.btn_cerrar)
        
        self.layout_tarjeta.addLayout(self.header)

        if widget_contenido:
            self.layout_tarjeta.addWidget(widget_contenido)

        if parent:
            self.resize(parent.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        
        if not self.parent():
            return

        parent_size = self.parent().size()
        self.setGeometry(0, 0, parent_size.width(), parent_size.height())

        ancho_tarjeta = int(parent_size.width() * self.porcentaje_ancho)
        alto_tarjeta = int(parent_size.height() * self.porcentaje_alto)
        
        pos_x = int((parent_size.width() - ancho_tarjeta) / 2)
        pos_y = int((parent_size.height() - alto_tarjeta) / 2)
        
        self.contenedor.setGeometry(pos_x, pos_y, ancho_tarjeta, alto_tarjeta)

    def show_modal(self):
        self.resize(self.parent().size()) 
        self.raise_()
        self.setVisible(True)
    
    def hide_modal(self):
        self.setVisible(False)