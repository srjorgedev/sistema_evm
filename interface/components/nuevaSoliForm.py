from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QComboBox
)
from PyQt6.QtCore import pyqtSignal

from domain.solicitudes.ClaseSolicitudes import Solicitud
import domain.solicitudes.crudSolicitudes as CRUD


class NuevaSoliForm(QWidget):

    solicitud_creada = pyqtSignal()   
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nueva Solicitud")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        lbl_asunto = QLabel("Asunto:")
        self.txt_asunto = QLineEdit()

        lbl_mat = QLabel("Matrícula del vehículo:")
        self.txt_matricula = QLineEdit()


        lbl_estado = QLabel("Estado:")
        self.cmb_estado = QComboBox()
        self.cmb_estado.addItems(["1"])   # Siempre inicia en 1 (Pendiente)

        lbl_sol = QLabel("Solicitante (ID empleado):")
        self.txt_solicitante = QLineEdit()

  
        lbl_auto = QLabel("Autorizador (ID empleado):")
        self.txt_autorizador = QLineEdit()

        btn_guardar = QPushButton("Guardar Solicitud")
        btn_guardar.clicked.connect(self.guardar)

       
        layout.addWidget(lbl_asunto)
        layout.addWidget(self.txt_asunto)

        layout.addWidget(lbl_mat)
        layout.addWidget(self.txt_matricula)

        layout.addWidget(lbl_estado)
        layout.addWidget(self.cmb_estado)

        layout.addWidget(lbl_sol)
        layout.addWidget(self.txt_solicitante)

        layout.addWidget(lbl_auto)
        layout.addWidget(self.txt_autorizador)

        layout.addSpacing(10)
        layout.addWidget(btn_guardar)



    def guardar(self):
        asunto = self.txt_asunto.text()
        matricula = self.txt_matricula.text()
        estado = self.cmb_estado.currentText()
        solicitante = self.txt_solicitante.text()
        autorizador = self.txt_autorizador.text()


        if asunto.strip() == "" or len(asunto) < 3:
            QMessageBox.warning(self, "Error", "El asunto debe tener al menos 3 caracteres.")
            return

        if len(matricula) == 0:
            QMessageBox.warning(self, "Error", "Debes ingresar una matrícula.")
            return

        if not solicitante.isdigit():
            QMessageBox.warning(self, "Error", "El ID del solicitante debe ser numérico.")
            return

        if not autorizador.isdigit():
            QMessageBox.warning(self, "Error", "El ID del autorizador debe ser numérico.")
            return

        
        nueva = Solicitud(
            asunto=asunto,
            matricula=matricula,
            estado=estado,
            solicitante=solicitante,
            autorizador=autorizador
        )

        
        CRUD.crearSolicitud(nueva)

        QMessageBox.information(self, "Éxito", "Solicitud creada correctamente.")

        self.txt_asunto.clear()
        self.txt_matricula.clear()
        self.txt_solicitante.clear()
        self.txt_autorizador.clear()

        self.solicitud_creada.emit()

      
        self.close()
