# FILE: interface/components/observation_row_archive.py
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal

class ObservacionArchivedRowWidget(QWidget):
    btn_desarchivar = pyqtSignal(int)
    clic_row = pyqtSignal(int)

    def __init__(self, data_tuple):
        super().__init__()
        numero = data_tuple[0]
        descripcion = data_tuple[1]
        tipo = data_tuple[2]
        bitacora = data_tuple[3]

        layout = QHBoxLayout(self)
        lbl = QLabel(f"{numero} | {tipo} | {descripcion[:50]} | Bit: {bitacora}")
        btn_des = QPushButton("Reactivar")
        btn_des.clicked.connect(lambda: self.btn_desarchivar.emit(numero))
        lbl.mousePressEvent = lambda e: self.clic_row.emit(numero)
        layout.addWidget(lbl)
        layout.addWidget(btn_des)