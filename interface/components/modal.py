from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFrame, QPushButton,
                             QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QRect, pyqtSignal
from PyQt6.QtGui import QColor, QCursor

from interface.components.square_button import SquareButtonWidget

class ModalWidget(QWidget):
    close = pyqtSignal()
    save = pyqtSignal()
    
    def __init__(self, parent=None, widget_contenido=None):
        super().__init__(parent)
        
        self.porcentaje_ancho = 0.75
        self.porcentaje_alto = 0.75

        self.setVisible(False)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        
        self.contenedor = QFrame(self) 
        self.contenedor.setStyleSheet("""
            QFrame {
                background-color: #1e293b; 
            }
            QLabel { background: transparent; color: white; }
        """)
        
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(30)
        sombra.setYOffset(10)
        sombra.setColor(QColor(0, 0, 0, 150))
        self.contenedor.setGraphicsEffect(sombra)

        self.layout_tarjeta = QVBoxLayout(self.contenedor)
        self.layout_tarjeta.setContentsMargins(48, 48, 48, 48)
        
        if widget_contenido:
            self.layout_tarjeta.addWidget(widget_contenido)
            
        self.btn_cerrar = SquareButtonWidget("close", "#cc1c11", 36)
        self.btn_cerrar.setParent(self.contenedor)
        self.btn_cerrar.clicked.connect(self.hide_modal)
        self.btn_cerrar.raise_()

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
        
        margen_x = 48
        margen_y = 48
        btn_x = ancho_tarjeta - self.btn_cerrar.width() - margen_x
        btn_y = margen_y
        
        self.btn_cerrar.move(btn_x, btn_y)

    def show_modal(self):
        self.resize(self.parent().size()) 
        self.raise_()
        self.setVisible(True)
    
    def hide_modal(self):
        self.setVisible(False)

    # def mousePressEvent(self, event):
    #     if not self.contenedor.geometry().contains(event.pos()):
    #         self.hide_modal()