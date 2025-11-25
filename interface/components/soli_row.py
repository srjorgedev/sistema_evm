from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import pyqtSignal
from interface.components.button import ButtonWidget, ColorKeys

import domain.solicitudes.crudSolicitudes as CRUD
from domain.solicitudes.ClaseSolicitudes import Solicitud


class SolicitudRowWidget(QWidget):
    reload_table = pyqtSignal()  

    def __init__(self, datos):
        """
        datos = (numero, asunto, matricula, estado, solicitante, autorizador)
        """
        super().__init__()

        self.numero = datos[0]      
        self.asunto = datos[1]
        self.matricula = datos[2]
        self.estado = datos[3]
        self.solicitante = datos[4]
        self.autorizador = datos[5]

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)

        layout.addWidget(QLabel(str(self.numero)))
        layout.addWidget(QLabel(self.asunto))
        layout.addWidget(QLabel(self.matricula))
        layout.addWidget(QLabel(self.estado))
        layout.addWidget(QLabel(self.solicitante))
        layout.addWidget(QLabel(self.autorizador))

        # Botones
        btn_ok = ButtonWidget("done", "", ColorKeys.CREAR)
        btn_cancel = ButtonWidget("close", "", ColorKeys.ARCHIVAR)
        btn_delete = ButtonWidget("trash", "", ColorKeys.ARCHIVAR)

        layout.addWidget(btn_ok)
        layout.addWidget(btn_cancel)
        layout.addWidget(btn_delete)

        btn_ok.clicked.connect(self.aceptar)
        btn_cancel.clicked.connect(self.rechazar)
        btn_delete.clicked.connect(self.eliminar)

    def aceptar(self):
        """Cambia el estado a 2 (Aprobada)."""
        nueva = Solicitud(
            numero=self.numero,
            asunto=None,
            matricula=None,
            estado="2",
            solicitante=None,
            autorizador=None
        )
        CRUD.estadoSolicitud(nueva)
        self.reload_table.emit()

    def rechazar(self):
        """Cambia el estado a 3 (Rechazada)."""
        nueva = Solicitud(
            numero=self.numero,
            asunto=None,
            matricula=None,
            estado="3",
            solicitante=None,
            autorizador=None
        )
        CRUD.estadoSolicitud(nueva)
        self.reload_table.emit()

    def eliminar(self):
        """Elimina la solicitud por ID."""
        CRUD.eliminarSolicitud(self.numero)
        self.reload_table.emit()
