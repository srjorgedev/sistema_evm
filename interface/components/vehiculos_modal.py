# interface/components/vehiculos_modal.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QThread
from interface.components.data_fetch import Fetch
from interface.components.vehiculo_row import VehiculoCardWidget
from controllers import vehiculo_controller 

class VehiculosModal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Cargando vehículos...")
        self.label.setStyleSheet("color: white; font-size: 16px;")
        self.layout.addWidget(self.label)

        self.fetch_data()

    def fetch_data(self):
        self.thread = QThread()
        self.worker = Fetch(vehiculo_controller.lista)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.handle_data)
        self.worker.error.connect(self.handle_error)

        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()

    def handle_data(self, data):
        self.label.hide()

        for vehiculo in data:
            card = VehiculoCardWidget(vehiculo)
            self.layout.addWidget(card)

        self.layout.addStretch()

    def handle_error(self, err):
        self.label.setText("ERROR al cargar los vehículos.")
