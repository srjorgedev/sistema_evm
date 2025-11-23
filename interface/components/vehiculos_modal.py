# interface/components/vehiculos_modal.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QThread
from interface.components.data_fetch import TaskRunner
from interface.components.vehiculo_row import VehiculoCardWidget
from controllers import vehiculo_controller 

class VehiculosModal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.runner = TaskRunner(self)

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Cargando vehículos...")
        self.label.setStyleSheet("color: white; font-size: 16px;")
        self.layout.addWidget(self.label)

        self.fetch_data()

    def fetch_data(self):
        self.runner.run(vehiculo_controller.lista, self.handle_data, self.handle_error)

    def handle_data(self, data):
        self.label.hide()

        for vehiculo in data:
            card = VehiculoCardWidget(vehiculo)
            self.layout.addWidget(card)

        self.layout.addStretch()

    def handle_error(self, err):
        self.label.setText("ERROR al cargar los vehículos.")
