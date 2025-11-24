from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor

from domain.bitacoras.Clase import Bitacora
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget

class UserRowWidget(QFrame):
    btn_archivo = pyqtSignal(object)
    btn_modificar = pyqtSignal()
    btn_entrada = pyqtSignal()
    btn_salida = pyqtSignal()
    
    def __init__(self, data: tuple):
        super().__init__()
        self.data = data
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        layout = QHBoxLayout(self)
        lbl_id = QLabel(f"#{self.data[0]}")
        lbl_titulo = QLabel(self.data[1])
        lbl_rol = QLabel(self.data[2])
        acciones = QWidget()
        acciones_layout = QHBoxLayout(acciones)
        
        # Botones 
        modificar = SquareButtonWidget("modify", "#1f4355", 32)
        archivar = SquareButtonWidget("archive", "#1f4355", 32)
        
        # Funciones de botones
        archivar.clicked.connect(self.emit_archivar)
        
        acciones_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.setContentsMargins(8, 0, 8, 0)
        
        self.setFixedHeight(56) 
        self.setStyleSheet("BitacoraRowWidget {background-color: transparent;} BitacoraRowWidget:hover {background-color: #162229;}")
        
        lbl_strong_style = "font-size: 18px; color: #009AD3; font-weight: bold; background: transparent;"
        lbl_normal_style = "font-size: 18px; color: #f1f1f1; font-weight: normal; background: transparent;"
        
        lbl_id.setFixedWidth(40)
        lbl_id.setStyleSheet(lbl_strong_style)
        lbl_id.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        lbl_titulo.setStyleSheet(lbl_normal_style)
        lbl_rol.setStyleSheet(lbl_normal_style)
        acciones.setStyleSheet("background: transparent;")
        
        acciones_layout.addWidget(modificar)
        acciones_layout.addWidget(archivar)

        layout.addWidget(lbl_id)
        layout.addWidget(lbl_titulo, 1) 
        layout.addWidget(lbl_rol, 1)
        layout.addWidget(acciones, 1)
    
    def emit_archivar(self):
        self.btn_archivo.emit(self.data[0])