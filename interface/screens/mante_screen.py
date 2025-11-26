# interface/screens/mante_screen.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from interface.screens.crud_widgets import MantenimientoWidget  # importamos del CRUD

class MANTEScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.mantenimiento_widget = MantenimientoWidget()
        self.layout.addWidget(self.mantenimiento_widget)
