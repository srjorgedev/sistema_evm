import sys
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLabel, QWidget, QMessageBox
)
from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.button import ButtonWidget, ColorKeys
from controllers import vehiculo_controller as Fvehiculo
from utils.log import log


class NewCarWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.runner = TaskRunner(self)

        # Layout principal
        self.main_layout = QVBoxLayout(self)

        # Widgets de entrada
        self.select_tipos = SelectWidget("Tipo de vehiculo*", "Seleccione un tipo...")
        self.num_serie = InputWidget("Número de serie")
        self.matricula = InputWidget("Matrícula")
        self.proposito = InputWidget("Propósito del vehículo")
        self.fechaAd = InputWidget("Fecha de adquisición")
        self.marca = SelectWidget("Marca*", "Marca del vehiculo:")
        self.modelo = SelectWidget("Modelo*", "Modelo:")
        self.licencia = SelectWidget("Licencia requerida*", "Licencia requerida..")

        # Botón
        crear_boton = ButtonWidget(None, "Registrar Vehículo", ColorKeys.CREAR)
        crear_boton.clicked.connect(self.registrar)

        # Layouts auxiliares
        layout_apd = QHBoxLayout()
        layout_apd.addWidget(self.num_serie)
        layout_apd.addWidget(self.matricula)

        layout_cred = QHBoxLayout()
        layout_cred.addWidget(self.proposito)
        layout_cred.addWidget(self.fechaAd)

        # Agregar al layout principal
        self.main_layout.addLayout(layout_apd)
        self.main_layout.addLayout(layout_cred)
        self.main_layout.addWidget(self.marca)
        self.main_layout.addWidget(self.modelo)
        self.main_layout.addWidget(self.licencia)
        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addStretch()
        self.main_layout.addWidget(crear_boton)
        self.main_layout.addStretch()

        # Ahora sí: cargar datos dinámicos
        self.fetch_tipos()
        self.fetch_marcas()
        self.fetch_modelos()
        self.fetch_licencias()

    # Métodos de carga de datos
    def fetch_marcas(self):
        self.runner.run(
            func=Fvehiculo.obtener_marcas,
            on_success=lambda r: self._cargar_combo(r, self.marca, "[MARCA]"),
            on_error=lambda e: log(f"[NEW CAR FORM]: Error cargando marcas -> {e}")
        )

    def fetch_modelos(self):
        self.runner.run(
            func=Fvehiculo.obtener_modelos,
            on_success=lambda r: self._cargar_combo(r, self.modelo, "[MODELO]"),
            on_error=lambda e: log(f"[NEW CAR FORM]: Error cargando modelos -> {e}")
        )

    def fetch_licencias(self):
        self.runner.run(
            func=Fvehiculo.obtener_licencias,
            on_success=lambda r: self._cargar_combo(r, self.licencia, "[LICENCIA]"),
            on_error=lambda e: log(f"[NEW CAR FORM]: Error cargando licencias -> {e}")
        )

    def _cargar_combo(self, datos, combobox, tag):
        items = []
        for tupla in datos:
            if isinstance(tupla, (list, tuple)) and len(tupla) >= 2:
                id_val, nombre = tupla[0], tupla[1]
                if isinstance(nombre, (int, float)) and isinstance(id_val, str):
                    id_val, nombre = nombre, id_val
                items.append((f"{id_val} - {nombre}", id_val))
            else:
                items.append((str(tupla), str(tupla)))

        log(f"{tag} Agregando {len(items)} elementos al combobox...")
        combobox.clear()
        combobox.addItems(items)
        log(f"{tag} Datos agregados.")

    def fetch_tipos(self):
        self.runner.run(
            func=Fvehiculo.obtener_lista,
            on_success=lambda r: self.agregar_tipos(r),
            on_error=lambda e: log(f"[NEW CAR FORM]: Error cargando tipos -> {e}")
        )

    def agregar_tipos(self, datos):
        items = [(f"{tupla[0]} - {tupla[1]}", tupla[0]) for tupla in datos]
        self.agregar_combo(items, self.select_tipos)

    def agregar_combo(self, datos, combobox):
        log("[NEW CAR FORM]: Agregando los datos al combobox...")
        combobox.addItems(datos)
        log("[NEW CAR FORM]: Datos agregados.")

    def registrar(self):
        num_serie = self.num_serie.get_text()
        matricula = self.matricula.get_text()
        marca = self.marca.get_text()
        modelo = self.modelo.get_text()
        tipo = self.select_tipos.getValue()
        proposito = self.proposito.get_text()

        ok, mensaje = Fvehiculo.registrar_vehiculo(
            num_serie, matricula, marca, modelo, tipo, proposito
        )

        msg = QMessageBox()
        msg.setWindowTitle("Registro de vehículo")
        msg.setIcon(QMessageBox.Icon.Information if ok else QMessageBox.Icon.Warning)
        msg.setText(mensaje)
        msg.exec()