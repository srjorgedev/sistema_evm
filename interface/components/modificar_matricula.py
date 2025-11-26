import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox
from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.styles.general import COLORS, COLORS_LIST
from controllers import vehiculo_controller as Fvehiculo
from utils.log import log


class ModificarMatriculaWidget(QWidget):
    def __init__(self, refrescar_tabla_callback=None):
        super().__init__()
        self.setWindowTitle("Modificar Matrícula")
        
        # Hacer la ventana modal y estática (sin redimensionar)
        from PyQt6.QtCore import Qt
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowCloseButtonHint)
        self.setFixedSize(800, 400)
        
        # Color de fondo azul oscuro (usando paleta oficial del proyecto)
        bg_color = COLORS_LIST[COLORS.MODAL_1]  # #1e293b
        text_color = "#f1f1f1"
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {bg_color};
                color: {text_color};
            }}
        """)
        
        self.runner = TaskRunner(self)
        self.refrescar_tabla_callback = refrescar_tabla_callback

        # Layout principal
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(15)

        # Título grande
        titulo = QLabel("MODIFICAR MATRÍCULA")
        titulo_font = titulo.font()
        titulo_font.setPointSize(18)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #f1f1f1; font-weight: bold;")
        self.main_layout.addWidget(titulo)
        
        # Separador visual
        separador = QLabel()
        separador.setStyleSheet("background-color: #334155; border: none;")
        separador.setFixedHeight(1)
        self.main_layout.addWidget(separador)
        self.main_layout.addSpacing(10)

        # Select vehículo
        self.select_vehiculo = SelectWidget("Vehículo*", "Seleccione un vehículo...")
        self.select_vehiculo.setFixedWidth(700)
        self.select_vehiculo.setFixedHeight(60)

        # Input nueva matrícula
        self.input_matricula = InputWidget("Nueva Matrícula:")
        self.input_matricula.setFixedWidth(700)
        self.input_matricula.setFixedHeight(100)

        # Agregar widgets al layout (mismo orden que en NewCarWidget)
        self.main_layout.addWidget(self.select_vehiculo)
        self.main_layout.addWidget(self.input_matricula)
        self.main_layout.addStretch()

        # Botón estilizado (igual que NewCarWidget)
        btn_guardar = QPushButton("✓ Modificar Matrícula")
        btn_guardar.setStyleSheet('''
            QPushButton {
                background-color: #2D89EF;
                color: white;
                padding: 10px 15px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1E5FBB;
            }
            QPushButton:pressed {
                background-color: #164A94;
            }
        ''')
        btn_guardar.clicked.connect(self.modificar_matricula)

        # Botón cerrar (X)
        btn_cerrar = QPushButton("✕ Cerrar")
        btn_cerrar.setStyleSheet('''
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 10px 15px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        ''')
        btn_cerrar.clicked.connect(self.close)

        # Layout para botones
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_guardar)
        btn_layout.addWidget(btn_cerrar)
        btn_layout.addStretch()

        self.main_layout.addSpacing(10)
        self.main_layout.addLayout(btn_layout)

        # Cargar vehículos
        self.fetch_vehiculos()

    def _cargar_combo(self, datos, combobox):
        items = []
        for tupla in datos:
            if isinstance(tupla, (list, tuple)) and len(tupla) >= 2:
                id_val, nombre = tupla[0], tupla[1]
                items.append((f"{id_val} - {nombre}", id_val))
            else:
                items.append((str(tupla), str(tupla)))

        combobox.addItems(items)

    def fetch_vehiculos(self):
        self.runner.run(
            func=Fvehiculo.obtener_lista,
            on_success=lambda r: self._cargar_combo(r, self.select_vehiculo),
            on_error=lambda e: log(f"[MODIFICAR MATRICULA]: Error cargando vehículos -> {e}")
        )

    def modificar_matricula(self):
        vehiculo_id = self.select_vehiculo.obtenerID()
        nueva_matricula = self.input_matricula.get_text().strip()

        if not vehiculo_id or str(vehiculo_id) == "0" or not nueva_matricula:
            QMessageBox.warning(self, "Error", "Seleccione un vehículo y escriba la nueva matrícula.")
            return

        ok, mensaje = Fvehiculo.modificar_matricula(vehiculo_id, nueva_matricula)

        msg = QMessageBox()
        msg.setWindowTitle("Modificar Matrícula")
        msg.setIcon(QMessageBox.Icon.Information if ok else QMessageBox.Icon.Warning)
        msg.setText(mensaje)
        msg.exec()

        if ok and self.refrescar_tabla_callback:
            try:
                self.refrescar_tabla_callback()
            except Exception:
                pass