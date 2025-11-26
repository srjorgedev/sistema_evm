from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTabWidget
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
from interface.components.bitacoras.bitacora_info import BitacoraInfoWidget

from interface.components.styles.general import COLORS, COLORS_LIST
from interface.components.styles.table_style import tab_style

from utils.log import log

class BITScreenWidget(QWidget):
    btn_archivar = pyqtSignal()
    
    row_click: int = 0
    
    notificar = pyqtSignal(str,str,str)
    
    def __init__(self):
        super().__init__()
        
        table_headers = ["N°", "Asunto", "Destino", "Salida", "Entrada", "Acciones"] # Los titulos que tendra la tabla
        
        # Creacion de elementos
        self.main_layout = QVBoxLayout(self)                    # Contenedor vertical
        label_titulo = QLabel("BITACORAS")                      # Texto
        button_layout = QHBoxLayout()                           # Layout horizontal
        label_subtitulo = QLabel("Panel de Control")            # Texto
        label_buttons = QLabel("Acciones rapidas")              # Texto
        
        # Las tablas ahora estarán dentro de las pestañas
        self.table = TableWidget(table_headers)              # Creamos una tabla y le pasamos los titulos
        self.archivadas = TableWidget(table_headers)         # Creamos una tabla y le pasamos los titulos
        
        # Creación del QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.table, "Registros Activos")
        self.tabs.addTab(self.archivadas, "Registros Archivados")

        # Instancia del objeto para realizar operaciones con la BD en segundo plano.
        self.runner = TaskRunner(self)
        
        # Elementos espaciadores
        v_spacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        h_spacer = QSpacerItem(128, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        
        # Botones genericos
        # En ButtonWidget
        # El primer parametro es el icono, es obligatorio, por ejemplo -> ""out"
        # El segundo parametro es el texto, es obligorio, por ejemplo -> "Registrar salida"
        # El tercer parametro es el color, es opcional, por ejemplo -> ColorKeys.ARCHIVAR
        self.button_salida = ButtonWidget("out", "Registrar salida", COLORS_LIST[COLORS.CREAR]) 
        self.button_entrada = ButtonWidget("in", "Registrar entrada", COLORS_LIST[COLORS.CREAR]) 
        self.button_modificar = ButtonWidget("modify", "Modificar", COLORS_LIST[COLORS.MODIFICAR]) 
        self.button_archivar = ButtonWidget("archive", "Archivar", COLORS_LIST[COLORS.ARCHIVAR])
        # En SquareButtonWidget
        # El primer parametro es el icono, es obligatorio.
        # El segundo parametro es el color, es obligatorio.  
        self.button_recargar = SquareButtonWidget("reload", "#f1f1f1") 
        
        # Asignacion de atributos 
        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)
        
        # Las ventanas modal o pop-up.
        # En ModalWidget
        # El primer parametro, es el elemento padre, self. Es obligatorio.
        # El segundo parametro, es lo que aparecera dentro de la modal. Es obligatorio.
        # El tercer parametro, es el titulo de la modal. Es opcional, aunque preferiblemente hay que ponerlo.
        # self.modal_salida = ModalWidget(self, SalidaFormWidget(), "Crear un nuevo registro de salida")
        self.modal_entrada = ModalWidget(self, EntradaFormWidget(), "Crear un nuevo registro de entrada")
        # self.modal_into = ModalWidget(self, BitacoraInfoWidget(self.row_click), "Ver datos de bitacora")
        
        # Asignacion de eventos en los botones cuando se hace clic      
        # Le asignamos funciones a los botones cuando se les hace clic.
        # TODOS los botones tienen .clicked.connect  
        self.button_salida.clicked.connect(lambda: self.abrir_modal(SalidaFormWidget, "Crear un nuevo registro de salida"))
        self.button_entrada.clicked.connect(self.modal_entrada.show_modal)
        self.button_recargar.clicked.connect(self.handle_refresh)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet(f"font-size: 40px; font-weight: bold; color:{COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_buttons.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_subtitulo.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        
        # Alineamos la posicion de elementos 
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Espacios en otros elementos
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        
        # Agragamos los botones al contenedor de botones
        button_layout.addWidget(self.button_salida)
        button_layout.addWidget(self.button_entrada)
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
        self.fetch_bitacoras()
        self.fetch_archivadas()

    def apply_tab_styles(self):
        
        self.tabs.setStyleSheet(tab_style)
        
    # Funcion para pedir los datos 
    def fetch_bitacoras(self):
        log("[BITACORAS]: Iniciando fetch general...")
        # Llamar al objeto para hacer peticiones en segundo plano.
        # Esta funcion nos pide...
        # La funcion a ejecutar: func
        # Lo que se debe hacer si todo sale bien: on_success
        # Lo que se debe hacer si hay un error: on_error
        # Aqui no se utiliza, pero tambien esta args, para cuando se le pasen tuplas
        # tampoco se utiliza, kwargs, para cuando se le pasen objetos o clave = valor
        self.runner.run(
            func=FBitacora.lista, 
            on_success=lambda data: self.handle_data(data, self.table), 
            on_error=self.handle_error
        )
        
    # Funcion para pedir los datos 
    def fetch_archivadas(self):
        log("[BITACORAS]: Iniciando fetch archivados...")
        self.runner.run(
            func=FBitacora.lista_archivados, 
            on_success=lambda data: self.handle_data(data, self.archivadas), 
            on_error=self.handle_error
        )

    def handle_data(self, data: list[tuple], parent: TableWidget):
        log(f"[BITACORAS]: Datos recibidos -> {len(data)} bitácoras.")
        
        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay bitácoras para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setContentsMargins(0, 16, 0, 0)
            
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for bitacora in data:
                if bitacora[5] == True:
                    card = BitacoraRowWidget(bitacora) 
                    card.clic_row.connect(lambda id: self.handle_clic_row(id))
                    card.btn_archivo.connect(self.handle_archivar)
                elif bitacora[5] == False:
                    card = BitacoraArchivedRowWidget(bitacora) 
                    card.btn_archivo.connect(self.handle_desarchivar)
                    card.clic_row.connect(lambda id: self.handle_clic_row(id))
                parent.addRow(card)

    def handle_error(self, error_message):
        log(f"[BITACORAS]: Error al hacer fetch -> {error_message}")
        
    def handle_archivar(self, data: int):
        log(f"[BITACORAS]: Iniciando proceso de archivado...")
        log(f"[BITACORAS]: DATOS -> {data}")
        
        activado_por = self.sender()
        if activado_por: 
            activado_por.setEnabled(False)
            
        self.runner.run(FBitacora.archivar, 
                        lambda c: self.on_archivado_finalizado(activado_por), 
                        lambda: activado_por.setEnabled(True) if activado_por else None,
                        data
                        )
        
    def handle_desarchivar(self, data: int):
        log(f"[BITACORAS]: Iniciando proceso de desarchivado...")
        log(f"[BITACORAS]: DATOS -> {data}")
        
        activado_por = self.sender()
        if activado_por: 
            activado_por.setEnabled(False)
            
        self.runner.run(FBitacora.desarchivar, 
                        lambda c: self.on_archivado_finalizado(activado_por), 
                        lambda: activado_por.setEnabled(True) if activado_por else None,
                        data
                        )

    def on_archivado_finalizado(self, boton):
        self.notificar.emit("Archivado", "Bitacora archivada exitosamente", "#2ecc71") 
        
        if boton:
            boton.setEnabled(True)
            
        self.fetch_bitacoras()
        self.fetch_archivadas()
        
    def handle_refresh(self):
        print("[BITACORAS]: Refrescando datos...")
        self.fetch_bitacoras()
        self.fetch_archivadas()
        
        self.notificar.emit("Recarga", "Datos recargados con exito", "#2ecc71") 
    
    def handle_clic_row(self, id):
        log(f"[BITACORAS]: Clicando row -> {id}")
        id_bitacora = int(id) 
        
        content_widget = BitacoraInfoWidget(id_bitacora)
        
        self.modal_info = ModalWidget(self, content_widget, "Ver datos de bitácora")
        self.modal_info.show_modal()

    def abrir_modal(self, formulario, titulo):
        form = formulario()
        
        modal = ModalWidget(self, form, titulo)
        
        modal.show_modal()