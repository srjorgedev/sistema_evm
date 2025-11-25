from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor

from domain.bitacoras.Clase import Bitacora
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget

class SolicitudRowWidget(QFrame):
    btn_aceptar = pyqtSignal(object)
    btn_rechazar = pyqtSignal(object)
    
    def __init__(self, data: tuple):
        super().__init__()
        self.data = data
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        layout = QHBoxLayout(self)
        lbl_1 = QLabel(f"#{self.data[0]}")
        lbl_2 = QLabel(self.data[1])
        lbl_4 = QLabel(self.data[3])
        lbl_3 = QLabel(self.data[2])
        lbl_5 = QLabel(self.data[4])
        lbl_6 = QLabel(self.data[5])
        acciones = QWidget()
        acciones_layout = QHBoxLayout(acciones)
        
        # Botones 
        aceptar = SquareButtonWidget("ok", "#1f4355", 32)
        rechazar = SquareButtonWidget("close", "#1f4355", 32)
        
        # Funciones de botones
        rechazar.clicked.connect(lambda: self.emitir(self.btn_rechazar))
        aceptar.clicked.connect(lambda: self.emitir(self.btn_aceptar))
        
        acciones_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedHeight(56) 
        self.setStyleSheet("SolicitudRowWidget {background-color: transparent;} SolicitudRowWidget:hover {background-color: #162229;}")
        
        lbl_strong_style = "font-size: 14px; color: #009AD3; font-weight: bold; background: transparent;"
        lbl_normal_style = "font-size: 14px; color: #f1f1f1; font-weight: normal; background: transparent;"
        
        lbl_1.setFixedWidth(80) 
        lbl_1.setStyleSheet(lbl_strong_style)
        lbl_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        lbl_2.setStyleSheet(lbl_normal_style)
        lbl_3.setStyleSheet(lbl_normal_style)
        lbl_4.setStyleSheet(lbl_normal_style)
        lbl_5.setStyleSheet(lbl_normal_style)
        lbl_6.setStyleSheet(lbl_normal_style)
        acciones.setStyleSheet("background: transparent;")
        
        acciones_layout.addWidget(aceptar)
        acciones_layout.addWidget(rechazar)

        layout.addWidget(lbl_1)
        layout.addWidget(lbl_2, 1) 
        layout.addWidget(lbl_3, 1)
        layout.addWidget(lbl_4, 1)
        layout.addWidget(lbl_5, 1)
        layout.addWidget(lbl_6, 1)
        layout.addWidget(acciones, 1)
    
    def emitir(self, boton):
        boton.emit(self.data[0])