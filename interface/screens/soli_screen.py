from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTabWidget
from PyQt6.QtCore import Qt, pyqtSignal

import controllers.solicitudes_controller as FSoli

from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ColorKeys
from interface.components.data_fetch import TaskRunner
from interface.components.modal import ModalWidget
from interface.components.bitacoras.salida_form import SalidaFormWidget
from interface.components.bitacoras.entrada_form import EntradaFormWidget
from interface.components.table import TableWidget
from interface.components.solicitud_row import SolicitudRowWidget
from interface.components.nuevaSoliForm import NuevaSoliForm

from utils.log import log

class SOLIScreenWidget(QWidget):
    btn_aceptar = pyqtSignal()
    btn_rechazar = pyqtSignal()
    
    notificar = pyqtSignal(str,str,str)
    
    def __init__(self):
        super().__init__()
        
        table_headers = ["N°", "Asunto", "Matricula", "Estado", "Solicitante", "Revisor", "Acciones"]
        
        # Creacion de elementos
        self.main_layout = QVBoxLayout(self) 
        label_titulo = QLabel("SOLICITUDES")
        button_layout = QHBoxLayout()
        label_subtitulo = QLabel("Panel de Control")
        label_buttons = QLabel("Acciones rapidas")
        
        # Las tablas ahora estarán dentro de las pestañas
        self.table = TableWidget(table_headers)
        self.archivadas = TableWidget(table_headers)
        
        # Creación del QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.table, "Todas las solicitudes")

        # Instancia del objeto para realizar operaciones con la BD en segundo plano.
        self.runner = TaskRunner(self)
        
        # Elementos espaciadores
        v_spacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        h_spacer = QSpacerItem(128, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        
        # Botones
        self.button_agregar = ButtonWidget("add", "Crear solicitud", ColorKeys.CREAR)
        self.button_modificar = ButtonWidget("modify", "Modificar", ColorKeys.MODIFICAR)
        self.button_archivar = ButtonWidget("archive", "Eliminar", ColorKeys.ARCHIVAR)
        self.button_recargar = SquareButtonWidget("reload", "#f1f1f1")
        
        # Asignacion de atributos 
        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)
        
        self.modal_salida = ModalWidget(self, NuevaSoliForm(), "Crear un nuevo registro de salida")
        self.modal_entrada = ModalWidget(self, EntradaFormWidget(), "Crear un nuevo registro de entrada")
        
        # Asignacion de eventos en los botones cuando se hace clic        
        self.button_agregar.clicked.connect(self.modal_salida.show_modal)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet("font-size: 40px; font-weight: bold; color: white;")
        label_buttons.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        label_subtitulo.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        
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

        # Aplicamos los estilos a las pestañas
        self.apply_tab_styles()

        # Llamamos a la funcion que pide los datos.
        self.fetch_data()

    def apply_tab_styles(self):
        style = """
            QTabWidget::pane {
                background-color: #f1f1f1;
            }
            QTabBar::tab {
                background: transparent;
                color: #f1f1f1;
                border: 2px solid #17272f;
                border-bottom: none;
                padding: 8px 24px;
                font-size: 14px;
                border-top-left-radius: 8px; /* Redondeado en la esquina superior izquierda */
                border-top-right-radius: 8px; /* Redondeado en la esquina superior derecha */
                margin-right: 4px; /* Pequeño espacio entre pestañas */
            }
            QTabBar::tab:selected {
                background: #17272f; /* Verde vibrante para la pestaña seleccionada */
                color: #f1f1f1;
                border-color: #17272f; /* Borde del mismo color para coherencia */
                border-bottom-color: #0f181f; /* Para que parezca un botón "flotante" */
            }
            QTabBar::tab:hover:!selected {
                background: #283a45; /* Un tono un poco más claro al pasar el ratón por encima */
                color: #c1c1c1;
            }
            QTabBar::tab:!selected {
                margin-top: 2px; /* Ligeramente más bajo que el seleccionado para el efecto flotante */
                color: #c1c1c1;
            }
        """
        self.tabs.setStyleSheet(style)
        
    # Funcion para pedir los datos 
    def fetch_data(self):
        log("[SOLICITUDES]: Iniciando fetch general...")
        # Llamar al objeto para hacer peticiones en segundo plano.
        # Esta funcion nos pide...
        # La funcion a ejecutar: func
        # Lo que se debe hacer si todo sale bien: on_success
        # Lo que se debe hacer si hay un error: on_error
        # Aqui no se utiliza, pero tambien esta args, para cuando se le pasen tuplas
        # tampoco se utiliza, kwargs, para cuando se le pasen objetos o clave = valor
        self.runner.run(
            func=FSoli.lista_general, 
            on_success=lambda data: self.handle_data(data, self.table), 
            on_error=self.handle_error
        )

    def handle_data(self, data: list[tuple], parent: TableWidget):
        log(f"[SOLICITUDES]: Datos recibidos -> {len(data)} solicitudes.")
    
        parent.clearRows()
    
        if not data:
            no_data_label = QLabel("No hay solicitudes para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
            return
    
        for d in data:
            numero = d[0]
            asunto = d[1]
            matricula = d[5]
            estado = d[7]
            solicitante = d[9]
            autorizador = d[11]
    
            fila = SolicitudRowWidget(
                (numero, asunto, matricula, estado, solicitante, autorizador)
            )
    
            parent.addRow(fila)
    
    
    def handle_error(self, error_message):
        log(f"[SOLICITUDES]: Error al hacer fetch -> {error_message}")