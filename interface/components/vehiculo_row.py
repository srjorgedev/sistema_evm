from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor

from domain.bitacoras.Clase import Bitacora
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget

class VehiculoCardWidget(QFrame):
    btn_archivo = pyqtSignal(object)
    btn_modificar = pyqtSignal()
    
    def __init__(self, data: tuple):
        super().__init__()
        self.data = data  # (id, serie, matricula, marca)
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        layout = QHBoxLayout(self)

        lbl_id = QLabel(f"#{self.data[0]}")
        lbl_serie = QLabel(self.data[1])       # serie
        lbl_matricula = QLabel(self.data[2])   # matrícula
        lbl_marca = QLabel(self.data[3])       # marca
        
        acciones = QWidget()
        acciones_layout = QHBoxLayout(acciones)

        # Botones
        modificar = SquareButtonWidget("modify", "#1f4355", 32)
        archivar = SquareButtonWidget("archive", "#1f4355", 32)

        archivar.clicked.connect(self.emit_archivar)

        acciones_layout.addWidget(modificar)
        acciones_layout.addWidget(archivar)
        acciones_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Estilos
        lbl_style = "font-size: 18px; color: #f1f1f1; background: transparent;"
        lbl_strong = "font-size: 18px; color: #009AD3; font-weight: bold; background: transparent;"

        lbl_id.setStyleSheet(lbl_strong)
        lbl_serie.setStyleSheet(lbl_style)
        lbl_matricula.setStyleSheet(lbl_style)
        lbl_marca.setStyleSheet(lbl_style)
        
        lbl_id.setFixedWidth(40)
        lbl_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedHeight(56)

        # Armado final
        layout.addWidget(lbl_id)
        layout.addWidget(lbl_serie, 1)
        layout.addWidget(lbl_matricula, 1)
        layout.addWidget(lbl_marca, 1)
        layout.addWidget(acciones, 1)

    def emit_archivar(self):
        self.btn_archivo.emit(self.data[0])
