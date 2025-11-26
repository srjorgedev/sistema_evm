# FILE: interface/components/observation_row.py
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal

class ObservacionRowWidget(QWidget):
    btn_eliminar = pyqtSignal(int)
    btn_editar = pyqtSignal(int)
    clic_row = pyqtSignal(int)

    def __init__(self, data_tuple):
        super().__init__()
        # data_tuple: (numero, descripcion, TipoTexto, bitacora)
        numero = data_tuple[0]
        descripcion = data_tuple[1]
        tipo = data_tuple[2]
        bitacora = data_tuple[3]

        layout = QHBoxLayout(self)
        lbl = QLabel(f"{numero} | {tipo} | {descripcion[:50]} | Bit: {bitacora}")
        btn_edit = QPushButton("Editar")
        btn_del = QPushButton("Eliminar")
        btn_edit.clicked.connect(lambda: self.btn_editar.emit(numero))
        btn_del.clicked.connect(lambda: self.btn_eliminar.emit(numero))
        lbl.mousePressEvent = lambda e: self.clic_row.emit(numero)
        layout.addWidget(lbl)
        layout.addWidget(btn_edit)
        layout.addWidget(btn_del)