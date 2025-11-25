from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QMouseEvent

from domain.bitacoras.Clase import Bitacora
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget
from interface.components.dot import DotWidget
from interface.components.styles.general import COLORS, COLORS_LIST

class BitacoraRowWidget(QFrame):
    btn_archivo = pyqtSignal(object)
    btn_modificar = pyqtSignal()
    btn_entrada = pyqtSignal()
    btn_salida = pyqtSignal()
    
    clic_row = pyqtSignal(object)
    
    def __init__(self, data: tuple):
        super().__init__()
        self.data = data
        
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        layout = QHBoxLayout(self)
        lbl_id = QLabel(f"#{self.data[0]}")
        lbl_titulo = QLabel(self.data[1])
        lbl_entrada = DotWidget("ok" if self.data[3] == 1 else "close", COLORS_LIST[COLORS.MAL])
        lbl_salida = DotWidget("ok" if self.data[4] == 1 else "close", COLORS_LIST[COLORS.MAL])
        lbl_destino = QLabel(self.data[2])
        acciones = QWidget()
        acciones_layout = QHBoxLayout(acciones)
        
        dot_widget_1 = QWidget()
        dot_widget_2 = QWidget()
        dot_layout_1 = QHBoxLayout(dot_widget_1)
        dot_layout_2 = QHBoxLayout(dot_widget_2)
        
        # Botones 
        modificar = SquareButtonWidget("modify", "#1f4355", 32)
        archivar = SquareButtonWidget("archive", "#1f4355", 32)
        
        # Funciones de botones
        archivar.clicked.connect(self.emit_archivar)
        
        acciones_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedHeight(56) 
        self.setStyleSheet("BitacoraRowWidget {background-color: transparent;} BitacoraRowWidget:hover {background-color: #162229;}")
        
        lbl_strong_style = "font-size: 14px; color: #009AD3; font-weight: bold; background: transparent;"
        lbl_normal_style = "font-size: 14px; color: #ebebeb; font-weight: normal; background: transparent;"
        
        dot_widget_1.setStyleSheet("background-color: transparent;")
        dot_widget_2.setStyleSheet("background-color: transparent;")
        
        dot_layout_1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        dot_layout_2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        lbl_id.setFixedWidth(80) 
        lbl_id.setStyleSheet(lbl_strong_style)
        lbl_id.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        lbl_titulo.setStyleSheet(lbl_normal_style)
        lbl_entrada.setStyleSheet(lbl_normal_style)
        lbl_salida.setStyleSheet(lbl_normal_style)
        lbl_destino.setStyleSheet(lbl_normal_style)
        acciones.setStyleSheet("background: transparent;")
        
        # lbl_entrada.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        # lbl_salida.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        acciones_layout.addWidget(modificar)
        acciones_layout.addWidget(archivar)
        
        dot_layout_1.addWidget(lbl_salida)
        dot_layout_2.addWidget(lbl_entrada)

        layout.addWidget(lbl_id)
        layout.addWidget(lbl_titulo, 1) 
        layout.addWidget(lbl_destino, 1)
        layout.addWidget(dot_widget_1, 1)
        layout.addWidget(dot_widget_2, 1)
        layout.addWidget(acciones, 1)
    
    def emit_archivar(self):
        self.btn_archivo.emit(self.data[0])
        
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clic_row.emit(self.data[0])