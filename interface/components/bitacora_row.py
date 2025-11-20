from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

from domain.bitacoras.Clase import Bitacora
from interface.components.square_button import SquareButtonWidget

class BitacoraCardWidget(QFrame):
    def __init__(self, data: Bitacora):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        layout = QHBoxLayout(self)
        lbl_id = QLabel(f"#{data.get_numControl()}")
        lbl_titulo = QLabel(data.get_asunto())
        lbl_entrada = QLabel("Si" if data.get_entradaBool() == 1 else "No")
        lbl_salida = QLabel("Si" if data.get_salidaBool() == 1 else "No")
        lbl_destino = QLabel(data.get_destino())
        acciones = QWidget()
        acciones_layout = QHBoxLayout(acciones)
        
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedHeight(48) 
        self.setStyleSheet("BitacoraCardWidget {background-color: #131e24;} BitacoraCardWidget:hover {background-color: red;}")
        
        lbl_strong_style = "font-size: 18px; color: #009AD3; font-weight: bold; background: transparent;"
        lbl_normal_style = "font-size: 18px; color: #f1f1f1; font-weight: normal; background: transparent;"
        
        lbl_id.setFixedWidth(40)
        lbl_id.setStyleSheet(lbl_strong_style)
        lbl_id.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        lbl_titulo.setStyleSheet(lbl_normal_style)
        lbl_entrada.setStyleSheet(lbl_normal_style)
        lbl_salida.setStyleSheet(lbl_normal_style)
        lbl_destino.setStyleSheet(lbl_normal_style)
        acciones.setStyleSheet("background: transparent;")
        
        lbl_entrada.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        acciones_layout.addWidget(SquareButtonWidget("out", "#1f4355", 32))
        acciones_layout.addWidget(SquareButtonWidget("in", "#1f4355", 32))
        acciones_layout.addWidget(SquareButtonWidget("modify", "#1f4355", 32))
        acciones_layout.addWidget(SquareButtonWidget("archive", "#1f4355", 32))

        layout.addWidget(lbl_id)
        layout.addWidget(lbl_titulo, 1) 
        layout.addWidget(lbl_destino, 1)
        layout.addWidget(lbl_salida, 1)
        layout.addWidget(lbl_entrada, 1)
        layout.addWidget(acciones, 1)