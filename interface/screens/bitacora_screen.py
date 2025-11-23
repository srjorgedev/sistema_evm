# NUEVO: Importaciones necesarias para el threading y los datos
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QFrame
from PyQt6.QtCore import Qt, QThread, pyqtSignal

import controllers.bitacora_controller as FBitacora
from domain.bitacoras.Clase import Bitacora

from interface.components.bitacora_row import BitacoraRowWidget
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ColorKeys
from interface.components.data_fetch import TaskRunner
from interface.components.table_head import TableHeadWidget
from interface.components.modal import ModalWidget
from interface.components.salida_form import SalidaFormWidget

from interface.components.styles.table_style import scrollbar_style
from utils.log import log

class BITScreenWidget(QWidget):
    btn_archivar = pyqtSignal()
    
    notificar = pyqtSignal(str,str,str)
    
    def __init__(self):
        super().__init__()
        
        # Creacion de elementos
        self.main_layout = QGridLayout(self)
        label_titulo = QLabel("BITACORAS")
        button_layout = QHBoxLayout()
        label_subtitulo = QLabel("Panel de Control")
        label_buttons = QLabel("Acciones rapidas")
        label_table_subtitulo = QLabel("Registros")
        self.table_head_widget = QFrame()
        table_head = QHBoxLayout(self.table_head_widget)
        table_scroll_area = QScrollArea()
        table_scroll_widget = QWidget() 
        self.table_scroll_layout = QVBoxLayout(table_scroll_widget) 
        
        # Instancia del objeto para realizar operaciones con la BD en segundo plano.
        self.runner = TaskRunner(self)
        
        # Elementos espaciadores
        v_spacer = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        h_spacer = QSpacerItem(128, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        
        # Botones
        self.button_salida = ButtonWidget("out", "Registrar salida", ColorKeys.CREAR)
        self.button_entrada = ButtonWidget("in", "Registrar entrada", ColorKeys.CREAR)
        self.button_modificar = ButtonWidget("modify", "Modificar", ColorKeys.MODIFICAR)
        self.button_archivar = ButtonWidget("archive", "Archivar", ColorKeys.ARCHIVAR)
        self.button_recargar = SquareButtonWidget("reload", "#f1f1f1")
        
        # Asignacion de atributos 

        # Asignamos espacios del layout principal
        # Margins es el espacios entre el contenedor padre y el layout
        # Spacing es el espacio entre elementos hijos del layout
        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)
        
        # La ventana popup que aparece:
        # Self es el elemento padre, este archivo.
        # SalidaFormWidget es lo que se muestra dentro de este popup.
        self.modal = ModalWidget(self, SalidaFormWidget())
        
        # Asignacion de eventos en los botones cuando se hace clic        
        self.button_salida.clicked.connect(self.modal.show_modal)
        self.button_recargar.clicked.connect(self.handle_refresh)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        label_buttons.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        label_subtitulo.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        label_table_subtitulo.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        
        # Alineamos la posicion de elementos 
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Espacios en otros elementos
        label_table_subtitulo.setContentsMargins(0, 0, 0, 8)
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        
        # Agragamos los botones al contenedor de botones
        button_layout.addWidget(self.button_salida)
        button_layout.addWidget(self.button_entrada)
        button_layout.addWidget(self.button_modificar)
        button_layout.addWidget(self.button_archivar)
        button_layout.addItem(h_spacer)
        button_layout.addWidget(self.button_recargar)
        
        self.table_head_widget.setObjectName("headerContainer")
        
        table_head.setContentsMargins(4, 8, 0, 8) 
        table_head.setSpacing(0)
        
        # Estilos a la tabla
        table_scroll_widget.setStyleSheet("""
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        """)
        
        self.table_head_widget.setStyleSheet("""
        #headerContainer {
            background-color: #17272f;  
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border-bottom: 1px solid #15313e; 
        }
        """)
        
        # Agregamos titulos a la tabla 
        table_head.addWidget(TableHeadWidget("N°"))
        table_head.addWidget(TableHeadWidget("Asunto"), 1)
        table_head.addWidget(TableHeadWidget("Destino"), 1)
        table_head.addWidget(TableHeadWidget("Salida registrada"), 1)
        table_head.addWidget(TableHeadWidget("Entrada registrada"), 1)
        table_head.addWidget(TableHeadWidget("Acciones"), 1)

        table_scroll_area.setWidgetResizable(True)
        table_scroll_area.setStyleSheet(scrollbar_style)

        self.table_scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.table_scroll_layout.setSpacing(0)
        
        table_scroll_area.setWidget(table_scroll_widget)

        self.main_layout.addWidget(label_subtitulo, 0, 0)
        self.main_layout.addWidget(label_titulo, 1, 0)
        self.main_layout.addItem(v_spacer, 2, 0)
        self.main_layout.addWidget(label_buttons, 3, 0)
        self.main_layout.addLayout(button_layout, 4, 0)
        self.main_layout.addItem(v_spacer, 5, 0)
        self.main_layout.addWidget(label_table_subtitulo, 6, 0)
        self.main_layout.addWidget(self.table_head_widget, 7, 0)
        self.main_layout.addWidget(table_scroll_area, 8, 0)

        # Llamamos a la funcion que pide los datos.
        self.fetch_bitacoras()
        
    # Funcion para pedir los datos 
    def fetch_bitacoras(self):
        log("[BITACORAS]: Iniciando fetch...")
        # Llamar al objeto para hacer peticiones en segundo plano.
        # Esta funcion nos pide...
        # La funcion a ejecutar: func
        # Lo que se debe hacer si todo sale bien: on_success
        # Lo que se debe hacer si hay un error: on_error
        # Aqui no se utiliza, pero tambien esta args, para cuando se le pasen tuplas
        # tampoco se utiliza, kwargs, para cuando se le pasen objetos o clave = valor
        self.runner.run(func=FBitacora.lista, on_success=self.handle_data, on_error=self.handle_error)

    def handle_data(self, data: list[tuple]):
        log(f"[BITACORAS]: Datos recibidos -> {len(data)} bitácoras.")
        
        while self.table_scroll_layout.count():
            child = self.table_scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not data:
            no_data_label = QLabel("No hay bitácoras para mostrar.")
            no_data_label.setStyleSheet("font-size: 16px; color: #888888;")
            no_data_label.setContentsMargins(0, 16, 0, 0)
            
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table_scroll_layout.addWidget(no_data_label)
        else:
            for bitacora in data:
                card = BitacoraRowWidget(bitacora) 
                card.btn_archivo.connect(self.handle_archivar)
                self.table_scroll_layout.addWidget(card)
        
        self.table_scroll_layout.addStretch()

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

    def on_archivado_finalizado(self, boton):
        self.notificar.emit("Archivado", "Bitacora archivada exitosamente", "#2ecc71") 
        
        if boton:
            boton.setEnabled(True)
            
        self.fetch_bitacoras()
        
    def handle_refresh(self):
        print("[BITACORAS]: Refrescando datos...")
        self.runner.run(
            func=FBitacora.lista_archivados,
            on_success=self.handle_data,
            on_error=self.handle_error
        )