
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

class VehiculoCardWidget(QWidget):
    def __init__(self, vehiculo):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.addWidget(QLabel(f"Marca: {vehiculo.get_marca()}"))
        layout.addWidget(QLabel(f"Modelo: {vehiculo.get_modelo()}"))
        layout.addWidget(QLabel(f"Placa: {vehiculo.get_matricula()}"))


        self.setStyleSheet("""
            background-color: #2b2b2b;
            border-radius: 8px;
            padding: 10px;
            color: white;
        """)
