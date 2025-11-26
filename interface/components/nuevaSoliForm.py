from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QComboBox, QHBoxLayout
)
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QDate

from domain.solicitudes.ClaseSolicitudes import Solicitud
import domain.solicitudes.crudSolicitudes as CRUD
from interface.components.data_fetch import TaskRunner 
import controllers.vehiculo_controller as Fvehiculos
import controllers.user_controller as Fempleados

from interface.components.input import InputWidget
from interface.components.select import SelectWidget



class NuevaSoliForm(QWidget):

    solicitud_creada = pyqtSignal()
    

    def __init__(self):
        super().__init__()
        self.datos = TaskRunner(self)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.setWindowTitle("Nueva Solicitud")

    
        self.txtasunto = InputWidget("Asunto:")
        self.main_layout.addWidget(self.txtasunto)

        lbl_fecha = QLabel("Fecha y hora:")
        self.main_layout.addWidget(lbl_fecha)
        fecha_hora_layout = QHBoxLayout()

        self.comboDia = QComboBox()
        self.comboDia.addItems([str(d) for d in range(1, 32)])

        self.comboMes = QComboBox()
        self.comboMes.addItems([
            "Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
        ])

        self.comboAnio = QComboBox()
        self.comboAnio.addItems(["2025", "2026", "2027"])

        fecha_hora_layout.addWidget(self.comboDia)
        fecha_hora_layout.addSpacing(5)
        fecha_hora_layout.addWidget(self.comboMes)
        fecha_hora_layout.addSpacing(5)
        fecha_hora_layout.addWidget(self.comboAnio)

        fecha_hora_layout.addSpacing(25)

        self.comboHora = QComboBox()
        self.comboHora.addItems([f"{h:02d}" for h in range(0, 24)])

        self.comboMin = QComboBox()
        self.comboMin.addItems([f"{m:02d}" for m in range(0, 60)])

        fecha_hora_layout.addWidget(self.comboHora)
        fecha_hora_layout.addSpacing(5)
        fecha_hora_layout.addWidget(self.comboMin)

        self.main_layout.addLayout(fecha_hora_layout)

        self.select_tipos = SelectWidget("Vehiculo:", "Seleccione un Vehiculo...")
        self.select_solicitante = SelectWidget("Empleados:", "Seleccione al solicitante")

        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addWidget(self.select_solicitante)
        
        btn_guardar = QPushButton("Generar Solicitud")
        btn_guardar.setStyleSheet("""
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
        """)
        btn_guardar.clicked.connect(self.guardar)  
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(btn_guardar)




        self.fetch_datoscars()
        self.fetch_datosuser()


    def guardar(self):
        asunto = self.txtasunto.get_text()
        solicitante = self.select_solicitante.obtenerID()
        tipo = self.select_tipos.obtenerID()

        # Validaciones
        if not asunto or len(asunto) < 3:
            QMessageBox.warning(self, "Error", "El asunto debe tener al menos 3 caracteres.")
            return

        if solicitante is None or tipo is None:
            QMessageBox.warning(self, "Error", "Debe seleccionar vehículo y solicitante.")
            return

        try:
            solicitante_id = int(solicitante)
        except (ValueError, TypeError):
            QMessageBox.warning(self, "Error", "El ID del solicitante debe ser numérico.")
            return

        # Construir fecha y hora
        dia = int(self.comboDia.currentText())
        mes = self.comboMes.currentIndex() + 1
        anio = int(self.comboAnio.currentText())
        fecha = f"{anio}-{mes:02d}-{dia:02d}"

        hora = self.comboHora.currentText()
        minuto = self.comboMin.currentText()
        hora_completa = f"{hora}:{minuto}:00"

        # Crear objeto Solicitud con los 8 parámetros requeridos
        # Orden: numero, asunto, horaSolicitud, fechaSolicitud, vehiculo, edoSolicitud, solicitante, autorizador
        nueva = Solicitud(
            "",                   # numero (se asigna en BD)
            asunto,               # asunto
            hora_completa,        # horaSolicitud
            fecha,                # fechaSolicitud
            tipo if tipo else "", # vehiculo
            "1",                  # edoSolicitud (1 = Pendiente por defecto)
            solicitante_id,       # solicitante
            ""                    # autorizador (puede dejarse vacío por ahora)
        )

        try:
            CRUD.agregarSolicitud(nueva)
            QMessageBox.information(self, "Éxito", "Solicitud creada correctamente.")

            self.txtasunto.clear()
            self.select_solicitante.clear()
            self.solicitud_creada.emit()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo crear la solicitud: {str(e)}")

    def fetch_datoscars(self):
        self.datos.run(
            func=Fvehiculos.obtener_lista,
            on_error=lambda e: print(f"[SOLI FORM]: Ocurrio un error -> {e}"),
            on_success=lambda e: self.datoscar(e)
        )
    def datoscar(self, datos):
        items = []
        for tupla in datos:
            items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))
        
        self.tipos_obs = items
        
        self.agregar_combo(items, self.select_tipos)
        
    def agregar_combo(self, datos, combobox): 
        print("[SOLI FORM]: Agregando los datos al combobox...")
        
        combobox.addItems(datos)
        
        print("[SOLI FORM]: Datos agregados.")
        
    def fetch_datosuser(self):
        self.datos.run(
            func=Fempleados.lista_general,
            on_error=lambda e: print(f"[SOLI USER FORM]: Ocurrio un error -> {e}"),
            on_success=lambda e: self.datosuser(e)
        )
    def datosuser(self, datos):
        items = []
        for tupla in datos:
            items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))
        
        self.tipos_obs = items
        
        self.agregar_combo(items, self.select_solicitante)
        
    def agregar_combo(self, datos, combobox): 
        print("[SOLI  USER FORM]: Agregando los datos al combobox...")
        
        combobox.addItems(datos)
        
        print("[SOLI FORM]: Datos agregados.")
        
class ModificarSoliForm(QWidget):

    solicitud_modificada = pyqtSignal()  # Señal para actualizar la tabla después de modificar

    def __init__(self, solicitud: Solicitud):
        super().__init__()
        self.setWindowTitle("Modificar")

        self.setWindowTitle(f"Modificar Solicitud #{solicitud.numero}")
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        lbl_fecha = QLabel("Fecha y hora:")
        self.main_layout.addWidget(lbl_fecha)

        fecha_layout = QHBoxLayout()
        self.comboDia = QComboBox()
        self.comboDia.addItems([str(d) for d in range(1, 32)])

        self.comboMes = QComboBox()
        self.comboMes.addItems([
            "Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
        ])

        self.comboAnio = QComboBox()
        self.comboAnio.addItems(["2025", "2026", "2027"])

        fecha_layout.addWidget(self.comboDia)
        fecha_layout.addWidget(self.comboMes)
        fecha_layout.addWidget(self.comboAnio)

        self.main_layout.addLayout(fecha_layout)

        # Botón Guardar
        btn_guardar = QPushButton("Guardar Fecha")
        btn_guardar.setStyleSheet("""
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
        """)
        btn_guardar.clicked.connect(self.guardar_fecha)
        self.main_layout.addWidget(btn_guardar)

        self.cargar_fecha_actual()

    def cargar_fecha_actual(self):
        """Cargar la fecha actual de la solicitud en los combos"""
        fecha = self.solicitud.fechaSolicitud  # Formato: 'YYYY-MM-DD'
        anio, mes, dia = map(int, fecha.split('-'))
        self.comboDia.setCurrentText(str(dia))
        self.comboMes.setCurrentIndex(mes - 1)
        self.comboAnio.setCurrentText(str(anio))

    def guardar_fecha(self):
        """Actualizar la fecha de la solicitud"""
        dia = int(self.comboDia.currentText())
        mes = self.comboMes.currentIndex() + 1
        anio = int(self.comboAnio.currentText())
        nueva_fecha = f"{anio}-{mes:02d}-{dia:02d}"

        # Actualizamos solo la fecha
        self.solicitud.fechaSolicitud = nueva_fecha
        try:
            CRUD.actualizarSolicitud(self.solicitud)  # Método que actualiza en BD
            QMessageBox.information(self, "Éxito", "Fecha actualizada correctamente.")
            self.solicitud_modificada.emit()
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo actualizar la fecha: {e}")