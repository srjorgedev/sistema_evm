# FILE: interface/components/new_observation_form.py
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QComboBox
from PyQt6.QtCore import pyqtSignal
from interface.components.data_fetch import TaskRunner
import controllers.observacion_controller as FObservacion

class NewObservationFormWidget(QWidget):
    saved = pyqtSignal()

    def __init__(self, numero=None):
        super().__init__()
        self.numero = numero
        layout = QVBoxLayout(self)
        self.combo_tipo = QComboBox()
        # The types should mirror DB - simple labels for now
        self.combo_tipo.addItems(["General","Seguridad","Estetica"]) 
        self.input_descripcion = QTextEdit()
        self.input_bitacora = QLineEdit()
        save_btn = QPushButton("Guardar")
        save_btn.clicked.connect(self.save)

        layout.addWidget(QLabel("Tipo de Observación"))
        layout.addWidget(self.combo_tipo)
        layout.addWidget(QLabel("Descripción"))
        layout.addWidget(self.input_descripcion)
        layout.addWidget(QLabel("Bitácora (número)"))
        layout.addWidget(self.input_bitacora)
        layout.addWidget(save_btn)

        self.runner = TaskRunner(self)

        if numero:
            self.load(numero)

    def load(self, numero):
        from domain.observaciones import crudObservacion
        obj = crudObservacion.buscar(type('T', (), {'get_numero': lambda self: numero})())
        if obj:
            self.combo_tipo.setCurrentText(obj.get_tipoObservacion())
            self.input_descripcion.setPlainText(obj.get_descripcion())
            self.input_bitacora.setText(str(obj.get_bitacoraAsociada()))

    def save(self):
        data = {
            'tipoObservacion': self.combo_tipo.currentIndex() + 1,
            'descripcion': self.input_descripcion.toPlainText(),
            'bitacoraAsociada': int(self.input_bitacora.text()) if self.input_bitacora.text().isdigit() else None
        }
        if self.numero:
            self.runner.run(FObservacion.actualizar, lambda r: self.on_saved(), lambda e: print(e), (self.numero, data))
        else:
            self.runner.run(FObservacion.alta, lambda r: self.on_saved(), lambda e: print(e), data)

    def on_saved(self):
        self.saved.emit()