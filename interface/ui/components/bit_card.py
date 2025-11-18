from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy
from PyQt6.QtCore import Qt

from domain.bitacoras.ClaseBitacora import Bitacora

class BitacoraCardWidget(QFrame):
    def __init__(self, data: Bitacora):
        super().__init__()
        self.setFixedHeight(60) 
        self.setStyleSheet("""
            BitacoraRow {
                background-color: #2d2d2d;
                border-radius: 5px;
                border: 1px solid #3E4149;
            }
            QLabel {
                color: #e0e0e0;
                border: none;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        
        lbl_id = QLabel(f"#{data.get_numControl()}")
        lbl_id.setFixedWidth(40)
        lbl_id.setStyleSheet("color: #808080; font-weight: bold;")
        
        lbl_titulo = QLabel(data.get_asunto())
        lbl_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        lbl_entrada = QLabel("Si" if data.get_entradaBool() == 1 else "No")
        lbl_entrada.setStyleSheet("color: #808080; font-weight: normal;")
        
        lbl_salida = QLabel("Si" if data.get_salidaBool() == 1 else "No")
        lbl_salida.setStyleSheet("color: #808080; font-weight: normal;")
        
        lbl_destino = QLabel(data.get_destino())
        lbl_destino.setStyleSheet("color: #808080; font-weight: normal;")

        layout.addWidget(lbl_id)
        layout.addWidget(lbl_titulo, 1) 
        layout.addWidget(lbl_destino, 1)
        layout.addWidget(lbl_salida, 1)
        layout.addWidget(lbl_entrada, 1)