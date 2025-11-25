import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, 
    QScrollArea, QSpacerItem, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.button import ButtonWidget, ColorKeys
from interface.components.square_button import SquareButtonWidget

from controllers import vehiculo_controller as Fvehiculo

from utils.log import log


class NewCarWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.runner = TaskRunner(self)
        self.main_layout = QVBoxLayout(self)

        self.select_tipos = SelectWidget("Tipo de vehiculo*", "Seleccione un tipo...")
        self.num_serie = InputWidget("Número de serie")
        self.matricula = InputWidget("Matrícula")
        self.proposito = InputWidget("Propósito del vehículo*")
        self.fechaAd = InputWidget("Fecha de adquisición")
        self.disponibilidad = InputWidget("Disponibilidad*")
        self.marca = InputWidget("Marca*")
        self.modelo = InputWidget("Modelo*")
        self.licencia = InputWidget("Licencia requerida*")

        crear_boton = ButtonWidget(None, "Registrar Vehículo", ColorKeys.CREAR)
        crear_boton.clicked.connect(self.registrar)

        layout_apd = QHBoxLayout()
        layout_apd.addWidget(self.num_serie)
        layout_apd.addWidget(self.matricula)

        layout_cred = QHBoxLayout()
        layout_cred.addWidget(self.proposito)
        layout_cred.addWidget(self.fechaAd)

        self.main_layout.addLayout(layout_apd)
        self.main_layout.addLayout(layout_cred)
        self.main_layout.addWidget(self.marca)
        self.main_layout.addWidget(self.modelo)
        self.main_layout.addWidget(self.disponibilidad)
        self.main_layout.addWidget(self.licencia)
        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addStretch()
        self.main_layout.addWidget(crear_boton)
        self.main_layout.addStretch()

        self.fetch_tipos()


   
    def fetch_tipos(self):
        self.runner.run(
            func=Fvehiculo.obtener_lista,
            on_success=lambda r: self.agregar_tipos(r),
            on_error=lambda e: log(f"[NEW CAR FORM]: Error cargando tipos -> {e}")
        )

    def agregar_tipos(self, datos):
        items = []
        for tupla in datos:
            items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))

        self.agregar_combo(items, self.select_tipos)

    def agregar_combo(self, datos, combobox):
        log("[NEW CAR FORM]: Agregando los datos al combobox...")
        combobox.addItems(datos)
        log("[NEW CAR FORM]: Datos agregados.")


    # ============================
    # ---- REGISTRAR VEHÍCULO ----
    # ============================
    def registrar(self):

        num_serie = self.num_serie.text()
        matricula = self.matricula.text()
        marca = self.marca.text()
        modelo = self.modelo.text()
        tipo = self.select_tipos.getValue()
        proposito = self.proposito.text()

        ok, mensaje = Fvehiculo.registrar_vehiculo(
            num_serie, matricula, marca, modelo, tipo, proposito
        )

        msg = QMessageBox()
        msg.setWindowTitle("Registro de vehículo")

        if ok:
            msg.setIcon(QMessageBox.Icon.Information)
        else:
            msg.setIcon(QMessageBox.Icon.Warning)

        msg.setText(mensaje)
        msg.exec()
