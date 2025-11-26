# interface/screens/obser_screen.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from interface.screens.crud_widgets import ObservacionWidget  # importamos del CRUD

class OBSERScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.observacion_widget = ObservacionWidget()
        self.layout.addWidget(self.observacion_widget)
