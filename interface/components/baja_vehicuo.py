import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.styles.general import COLORS, COLORS_LIST
from controllers import vehiculo_controller as Fvehiculo
from utils.log import log


class BajaVehiculoWidget(QWidget):
    """Formulario para dar de baja un vehículo con estilo consistente.

    - Ventana modal estática
    - Título grande y separador
    - Fondo con color de paleta del proyecto
    - Carga vehículos con TaskRunner
    - Muestra confirmación antes de 'dar de baja' (aún no ejecuta borrado en BD)
    """

    def __init__(self, refrescar_tabla_callback=None):
        super().__init__()
        self.refrescar_tabla_callback = refrescar_tabla_callback

        self.setWindowTitle("Dar de baja vehículo")
        # Modal estático sin redimensionar, solo botón cerrar
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowCloseButtonHint)
        self.setFixedSize(800, 380)

        # Paleta de colores
        bg = COLORS_LIST[COLORS.MODAL_1]
        text_color = "#f1f1f1"
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
                color: {text_color};
            }}
        """)

        # Task runner
        self.runner = TaskRunner(self)

        # Layout principal
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(12)

        # Título
        titulo = QLabel("DAR DE BAJA VEHÍCULO")
        f = titulo.font()
        f.setPointSize(16)
        f.setBold(True)
        titulo.setFont(f)
        titulo.setStyleSheet("color: #f1f1f1; font-weight: bold;")
        self.main_layout.addWidget(titulo)

        # Separador
        sep = QLabel()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background-color: #334155; border: none;")
        self.main_layout.addWidget(sep)

        # Campos
        self.select_vehiculo = SelectWidget("Vehículo*", "Seleccione un vehículo...")
        self.select_vehiculo.setFixedWidth(700)
        self.select_vehiculo.setFixedHeight(60)

        self.input_motivo = InputWidget("Motivo de baja:")
        self.input_motivo.setFixedWidth(700)
        self.input_motivo.setFixedHeight(60)

        self.main_layout.addWidget(self.select_vehiculo)
        self.main_layout.addWidget(self.input_motivo)

        # Botones
        self.btn_baja = QPushButton("✓ Dar de baja")
        self.btn_baja.setFixedHeight(46)
        self.btn_baja.setStyleSheet(f'''
            QPushButton {{
                background-color: {COLORS_LIST[COLORS.ARCHIVAR]};
                color: white;
                padding: 10px 18px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #c0392b;
            }}
            QPushButton:pressed {{
                background-color: #a93226;
            }}
        ''')

        self.btn_cancel = QPushButton("✕ Cerrar")
        self.btn_cancel.setFixedHeight(46)
        self.btn_cancel.setStyleSheet('''
            QPushButton {
                background-color: #6b7280;
                color: white;
                padding: 10px 18px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4b5563;
            }
        ''')
        self.btn_cancel.clicked.connect(self.close)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(self.btn_baja)
        btn_row.addWidget(self.btn_cancel)
        btn_row.addStretch()

        self.main_layout.addSpacing(8)
        self.main_layout.addLayout(btn_row)

        # Cargar datos
        self.fetch_vehiculos()

        # Conectar acción
        self.btn_baja.clicked.connect(self.confirmar_baja)

    def _cargar_combo(self, datos, combobox):
        items = []
        for tupla in datos:
            if isinstance(tupla, (list, tuple)) and len(tupla) >= 2:
                items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))
            else:
                items.append((str(tupla), str(tupla)))

        combobox.addItems(items)

    def fetch_vehiculos(self):
        self.runner.run(
            func=Fvehiculo.obtener_lista,
            on_success=lambda r: self._cargar_combo(r, self.select_vehiculo),
            on_error=lambda e: log(f"[BAJA VEHICULO]: Error cargando vehículos -> {e}")
        )

    def confirmar_baja(self):
        vehiculo_id = self.select_vehiculo.obtenerID()
        motivo = self.input_motivo.get_text().strip()

        if not vehiculo_id:
            QMessageBox.warning(self, "Error", "Selecciona un vehículo para dar de baja.")
            return

        if not motivo:
            QMessageBox.warning(self, "Error", "Ingresa el motivo de la baja.")
            return

        respuesta = QMessageBox.question(self, "Confirmar baja",
                                         f"¿Deseas dar de baja el vehículo {vehiculo_id}?\nMotivo: {motivo}",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if respuesta == QMessageBox.StandardButton.Yes:
            # Llamar al controlador en segundo plano para no bloquear la UI
            def _borrar():
                return Fvehiculo.borrar_vehiculo(vehiculo_id, motivo)

            def _ok(resultado):
                try:
                    ok, msg = resultado
                    if ok:
                        QMessageBox.information(self, "Baja", msg)
                        if self.refrescar_tabla_callback:
                            try:
                                self.refrescar_tabla_callback()
                            except Exception:
                                pass
                        self.close()
                    else:
                        QMessageBox.warning(self, "Error", msg)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Respuesta inesperada: {e}")

            def _err(e):
                QMessageBox.critical(self, "Error", f"Error al intentar borrar: {e}")

            self.runner.run(func=_borrar, on_success=_ok, on_error=_err)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BajaVehiculoWidget()
    w.show()
    sys.exit(app.exec())
