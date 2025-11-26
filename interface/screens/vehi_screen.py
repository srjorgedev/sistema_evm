from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea,QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTabWidget
from PyQt6.QtCore import Qt, pyqtSignal

import controllers.bitacora_controller as FBitacora
import controllers.user_controller as FUsuario
import controllers.vehiculo_controller as FVehiculo

from interface.components.bitacoras.bitacora_row import BitacoraRowWidget
from interface.components.bitacoras.bitacora_row_archive import BitacoraArchivedRowWidget
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.data_fetch import TaskRunner
from interface.components.modal import ModalWidget
from interface.components.bitacoras.salida_form import SalidaFormWidget
from interface.components.bitacoras.entrada_form import EntradaFormWidget
from interface.components.table import TableWidget
from interface.components.user_row import UserRowWidget
from interface.components.vehiculo_row import VehiculoCardWidget
from interface.components.nuevoVehiculoForm import NewCarWidget

from interface.components.styles.general import COLORS_LIST, COLORS
from interface.components.styles.table_style import tab_style

from interface.components.modificar_matricula import ModificarMatriculaWidget  # tu archivo nuevo
from interface.components.baja_vehicuo import BajaVehiculoWidget 
from utils.log import log

class VEHIScreenWidget(QWidget):
    btn_archivar = pyqtSignal()
    
    notificar = pyqtSignal(str,str,str)
        
    def __init__(self):
        super().__init__()
        
        table_headers = ["N° Serie", "Matricula", "Marca", "Acciones"]

    
        # Creacion de elementos
        self.main_layout = QVBoxLayout(self) 
        label_titulo = QLabel("VEHICULOS")
        button_layout = QHBoxLayout()
        label_subtitulo = QLabel("Panel de Control")
        label_buttons = QLabel("Acciones rapidas")
        
        # Las tablas ahora estarán dentro de las pestañas
        self.table = TableWidget(table_headers)
        self.archivadas = TableWidget(table_headers)
        
        # Creación del QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.table, "Vehiculos registrados")
        # self.tabs.addTab(self.archivadas, "Registros Archivados")

        # Instancia del objeto para realizar operaciones con la BD en segundo plano.
        self.runner = TaskRunner(self)
        
        # Elementos espaciadores
        v_spacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        h_spacer = QSpacerItem(128, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        
        # Botones
        self.button_agregar = ButtonWidget("add", "Registrar vehiculo", COLORS_LIST[COLORS.CREAR])
        self.button_modificar = ButtonWidget("modify", "Modificar", COLORS_LIST[COLORS.MODIFICAR])
        self.main_layout.addWidget(self.button_modificar)
        self.button_archivar = ButtonWidget("archive", "Eliminar", COLORS_LIST[COLORS.ARCHIVAR])
        self.main_layout.addWidget(self.button_archivar)
        self.button_recargar = SquareButtonWidget("reload", "#f1f1f1")
        
        # Asignacion de atributos 
        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)
        
        self.modal_salida = ModalWidget(self, NewCarWidget(), "Crear un nuevo registro de salida")
        self.modal_entrada = ModalWidget(self, EntradaFormWidget(), "Crear un nuevo registro de entrada")
        
        # Asignacion de eventos en los botones cuando se hace clic        
        self.button_agregar.clicked.connect(self.modal_salida.show_modal)
        # self.button_recargar.clicked.connect(self.handle_refresh)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet(f"font-size: 40px; font-weight: bold; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_buttons.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_subtitulo.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        
        # Alineamos la posicion de elementos 
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Espacios en otros elementos
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        
        # Agragamos los botones al contenedor de botones
        button_layout.addWidget(self.button_agregar)
        button_layout.addWidget(self.button_modificar)
        button_layout.addWidget(self.button_archivar)
        button_layout.addItem(h_spacer)
        button_layout.addWidget(self.button_recargar)

        self.main_layout.addWidget(label_subtitulo)
        self.main_layout.addWidget(label_titulo)
        self.main_layout.addSpacerItem(v_spacer)
        self.main_layout.addWidget(label_buttons)
        self.main_layout.addLayout(button_layout)
        self.main_layout.addSpacerItem(v_spacer)
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addSpacerItem(v_spacer)
        self.modal_modificar = ModificarMatriculaWidget(refrescar_tabla_callback=self.refrescar_tabla)
        self.button_modificar.clicked.connect(self.modal_modificar.show)
        self.modal_baja = BajaVehiculoWidget(refrescar_tabla_callback=self.refrescar_tabla)
        self.button_archivar.clicked.connect(self.modal_baja.show)

        # Aplicamos los estilos a las pestañas
        self.apply_tab_styles()

        # Llamamos a la funcion que pide los datos.
        self.fetch_vehiculos()


    def apply_tab_styles(self):
        self.tabs.setStyleSheet(tab_style)
        
    def refrescar_tabla(self):
        # Aquí refrescas tu tabla de vehículos
        print("Tabla de vehículos refrescada")
        
    # Funcion para pedir los datos 
    def fetch_vehiculos(self):
        log("[VEHICULOS]: Iniciando fetch general...")
        # Llamar al objeto para hacer peticiones en segundo plano.
        # Esta funcion nos pide...
        # La funcion a ejecutar: func
        # Lo que se debe hacer si todo sale bien: on_success
        # Lo que se debe hacer si hay un error: on_error
        # Aqui no se utiliza, pero tambien esta args, para cuando se le pasen tuplas
        # tampoco se utiliza, kwargs, para cuando se le pasen objetos o clave = valor
        self.runner.run(
            func=FVehiculo.obtener_lista, 
            on_success=lambda data: self.handle_data(data, self.table), 
            on_error=self.handle_error
        )
        
    def handle_data(self, data: list[tuple], parent: TableWidget):
        log(f"[VEHICULOS]: Datos recibidos -> {len(data)} VEHICULOS.")
        
        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay vehiculos para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setContentsMargins(0, 16, 0, 0)
            
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for bitacora in data:
                card = VehiculoCardWidget(bitacora) 
                card.btn_archivo.connect(lambda: print("HI"))
                parent.addRow(card)   
        
    def handle_error(self, error_message):
        log(f"[VEHICULOS]: Error al hacer fetch -> {error_message}")