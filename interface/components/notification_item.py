from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPropertyAnimation, QTimer

class NotificacionItemWidget(QFrame):
    def __init__(self, titulo, mensaje, color = None, parent=None):
        super().__init__(parent)
        
        self.color = "#009AD3" if color == None else color 
        
        self.layout_principal = QHBoxLayout(self)
        self.layout_principal.setContentsMargins(0, 0, 0, 0) 
        self.layout_principal.setSpacing(8) 
        
        self.setFixedSize(320, 60)
        self.setObjectName("FondoNotificacion")
        
        self.setStyleSheet("""
            QFrame#FondoNotificacion {
                background-color: #2c3e50;
                border-radius: 8px;
            }
        """)

        self.franja = QFrame()
        self.franja.setFixedWidth(4) 
        self.franja.setStyleSheet(f"""
            background-color: {self.color};
            border-top-left-radius: 4px;    
            border-bottom-left-radius: 4px; 
        """)

        self.contenido_widget = QWidget()
        self.layout_contenido = QVBoxLayout(self.contenido_widget)
        self.layout_contenido.setContentsMargins(8, 4, 8, 8) 
        self.layout_contenido.setSpacing(4)
        
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("color: white; font-weight: bold; font-size: 18px; background: transparent;")
        
        lbl_mensaje = QLabel(mensaje)
        lbl_mensaje.setWordWrap(True)
        lbl_mensaje.setStyleSheet("color: #bdc3c7; font-size: 14px; background: transparent;")

        self.layout_contenido.addWidget(lbl_titulo)
        self.layout_contenido.addWidget(lbl_mensaje)
        
        self.layout_principal.addWidget(self.franja)
        self.layout_principal.addWidget(self.contenido_widget)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(24)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(shadow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cerrar_animado)
        self.timer.start(3000) 

    def cerrar_animado(self):
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        self.anim = QPropertyAnimation(self.effect, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.finished.connect(self.close) 
        self.anim.start()