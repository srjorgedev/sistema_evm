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

    
        lbl_asunto = QLabel("Asunto:")
        self.txt_asunto = QLineEdit()

    
        lbl_fecha = QLabel("Fecha:")

        self.comboDia = QComboBox()
        self.comboDia.addItems([str(d) for d in range(1, 32)])
        self.comboDia.setFixedSize(100, 40)

        self.comboMes = QComboBox()
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.comboMes.addItems(meses)
        self.comboMes.setFixedSize(100, 40)

        self.comboAnio = QComboBox()
        self.comboAnio.addItems([str(a) for a in range(2025, 2035)])
        self.comboAnio.setFixedSize(100, 40)

        fecha_layout = QHBoxLayout()
        fecha_layout.setSpacing(8)
        fecha_layout.addWidget(self.comboDia)
        fecha_layout.addWidget(self.comboMes)
        fecha_layout.addWidget(self.comboAnio)

    
        lbl_hora = QLabel("Hora:")

        self.comboHora = QComboBox()
        self.comboHora.addItems([f"{h:02d}" for h in range(0, 24)])
        self.comboHora.setFixedWidth(55)

        self.comboMin = QComboBox()
        self.comboMin.addItems([f"{m:02d}" for m in range(0, 60)])
        self.comboMin.setFixedWidth(55)

        hora_layout = QHBoxLayout()
        hora_layout.setSpacing(8)
        hora_layout.addWidget(self.comboHora)
        hora_layout.addWidget(self.comboMin)

        
        self.select_tipos = SelectWidget("Vehiculo*", "Seleccione un Vehiculo...")
        self.select_solicitante = SelectWidget("Empleados*:", "Seleccione al solicitante")

        btn_guardar = QPushButton("Guardar Solicitud")
        btn_guardar.clicked.connect(self.guardar)

    
        self.main_layout.addWidget(lbl_asunto)
        self.main_layout.addWidget(self.txt_asunto)

        self.main_layout.addWidget(lbl_fecha)
        self.main_layout.addLayout(fecha_layout)

        self.main_layout.addWidget(lbl_hora)
        self.main_layout.addLayout(hora_layout)

        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addWidget(self.select_solicitante)

        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(btn_guardar)
        
        self.fetch_datoscars()
        self.fetch_datosuser()


    def guardar(self):
        asunto = self.txt_asunto.text()
        solicitante = self.select_solicitante.obtenerID()
        tipo = self.select_tipos.obtenerID()
        

        # Validaciones
        if asunto.strip() == "" or len(asunto) < 3:
            QMessageBox.warning(self, "Error", "El asunto debe tener al menos 3 caracteres.")
            return

       
        dia = int(self.comboDia.currentText())
        mes = self.comboMes.currentIndex() + 1
        anio = int(self.comboAnio.currentText())

        fecha = f"{anio}-{mes:02d}-{dia:02d}"

        hora = self.comboHora.currentText()
        minuto = self.comboMin.currentText()
        hora_completa = f"{hora}:{minuto}:00"

        try:
            solicitante_id = int(solicitante)
        except ValueError:
            QMessageBox.warning(self, "Error", "IDs deben ser numéricos.")
            return


        nueva = Solicitud(
            "",                   # numero
            asunto,               # asunto
            hora_completa,        # horaSolicitud
            fecha,                # fechaSolicitud
            tipo if tipo else "", # vehiculo
            solicitante_id        # solicitante
        )

        CRUD.agregarSolicitud(nueva)

        QMessageBox.information(self, "Éxito", "Solicitud creada correctamente.")

        self.txt_asunto.clear()
        self.select_solicitante.clear()

        self.solicitud_creada.emit()

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