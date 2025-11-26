from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTabWidget, QFrame
from PyQt6.QtCore import Qt, pyqtSignal

import controllers.bitacora_controller as FBitacora

from interface.components.bitacoras.bitacora_row import BitacoraRowWidget
from interface.components.bitacoras.bitacora_row_archive import BitacoraArchivedRowWidget
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.data_fetch import TaskRunner
from interface.components.modal import ModalWidget
from interface.components.bitacoras.salida_form import SalidaFormWidget
from interface.components.bitacoras.entrada_form import EntradaFormWidget
from interface.components.table import TableWidget

from interface.components.styles.general import COLORS, COLORS_LIST

from utils.log import log

class BitacoraInfoWidget(QWidget):
    def __init__(self, id):
        super().__init__()
        
        self.runner = TaskRunner(self)
        
        self.main_layout = QVBoxLayout(self)
        
        self.main_layout.setContentsMargins(0,0,0,0)
        
        self.fetch_data(id)
        
    def fetch_data(self, id):
        log("[BITACORA INFO]: Obteniendo datos...")
        self.runner.run(
            func= lambda: FBitacora.buscar(id),
            on_success= lambda data: self.handle_data(data),
            on_error= lambda: log("[BiTACORA INFO]: Todo mal"),
        )
        
    def handle_data(self, data):
        salida_gas = data["salida"]["gas"]
        salida_km = data["salida"]["km"]
        salida_datos = [
            ("Fecha", data["salida"]["fecha"]),
            ("Hora", data["salida"]["hora"]),
            ("Combustible", str(salida_gas)),
            ("Kilometraje", str(salida_km)),
        ]
        
        entrada_gas = data["entrada"]["gas"]
        entrada_km = data["entrada"]["km"]
        entrada_datos = [
            ("Fecha", data["entrada"]["fecha"]),
            ("Hora", data["entrada"]["hora"]),
            ("Combustible", str(entrada_gas)),
            ("Kilometraje", str(entrada_km)),
        ]
        
        layout_x = QHBoxLayout()
        layout_x2 = QHBoxLayout()
        solicitante = InfoWidget("Solicitante", data["solicitante"])
        autorizador = InfoWidget("Autorizado por", data["autorizador"])
        destino = InfoWidget("Destino", data["destino"])
        asunto = InfoWidget("Asunto", data["asunto"])
        salida = RegistroWidget("Salida", salida_datos)
        entrada = RegistroWidget("Entrada", entrada_datos)
        
        layout_x.setSpacing(12)
        self.main_layout.setSpacing(12)
        
        layout_x.addWidget(solicitante)
        layout_x.addWidget(autorizador)
        
        layout_x2.addWidget(salida)
        layout_x2.addWidget(entrada)
        
        
        self.main_layout.addLayout(layout_x)
        self.main_layout.addWidget(destino)
        self.main_layout.addWidget(asunto)
        self.main_layout.addLayout(layout_x2)
        self.main_layout.addStretch()
        
        
class InfoWidget(QFrame):
    def __init__(self, titulo, texto):
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        self.titulo = QLabel(titulo)
        self.contenido = QLabel(texto)
        
        self.main_layout.setSpacing(4)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        
        self.setStyleSheet(f"""
            InfoWidget {{
                background-color: {COLORS_LIST[COLORS.MODAL_CARD]};
                border: 1px solid {COLORS_LIST[COLORS.MODAL_CARD_BORDER]};
            }}
        """)
        
        self.titulo.setStyleSheet("font-size: 12px; color:#c1c1c1; background-color: transparent;")
        self.contenido.setStyleSheet("font-size: 14px; color:#f1f1f1; background-color: transparent;")
        
        self.main_layout.addWidget(self.titulo)
        self.main_layout.addWidget(self.contenido)
        
class RegistroWidget(QFrame):
    def __init__(self, titulo, datos: list[tuple[str, any]]):
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        self.titulo = QLabel(titulo)
        
        self.main_layout.setSpacing(4)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        
        self.setStyleSheet(f"""
            RegistroWidget {{
                background-color: {COLORS_LIST[COLORS.MODAL_CARD]};
                border: 1px solid {COLORS_LIST[COLORS.MODAL_CARD_BORDER]};
            }}
        """)
        
        self.titulo.setStyleSheet("font-size: 12px; color:#c1c1c1; background-color: transparent;")
        
        self.main_layout.addWidget(self.titulo)

        self.setContent(datos)
    
    def setContent(self, datos):
        for dato in datos:
            contenido_layout = QHBoxLayout()
            titulo_contenido = QLabel(dato[0])
            print(dato[1])
            contenido = QLabel(dato[1] if dato[1] not in [None, "None"] else "Pendiente...")
            
            titulo_contenido.setStyleSheet("font-size: 14px; color:#f1f1f1; background-color: transparent;")
            contenido.setStyleSheet("font-size: 14px; color:#f1f1f1; background-color: transparent;")
            
            contenido_layout.addWidget(titulo_contenido)
            contenido_layout.addStretch()
            contenido_layout.addWidget(contenido)
            
            self.main_layout.addLayout(contenido_layout)