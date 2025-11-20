# NUEVO: Importaciones necesarias para el threading y los datos
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt, QThread

import controllers.bitacora_controller as FBitacora
from domain.bitacoras.Clase import Bitacora

from interface.components.bitacora_row import BitacoraCardWidget
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ColorKeys
from interface.components.data_fetch import Fetch
from interface.components.table_head import TableHeadWidget
from interface.components.modal import ModalWidget
from interface.components.salida_form import SalidaFormWidget

class BITScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Creacion de elementos
        self.main_layout = QGridLayout(self)
        label_titulo = QLabel("BITACORAS")
        button_layout = QHBoxLayout()
        label_subtitulo = QLabel("Panel de Control")
        label_buttons = QLabel("Acciones rapidas")
        label_table_subtitulo = QLabel("Registros")
        table_head = QHBoxLayout()
        scroll_area = QScrollArea()
        scroll_widget = QWidget() 
        self.scroll_layout = QVBoxLayout(scroll_widget) 
        
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
        
        self.modal = ModalWidget(self, SalidaFormWidget())
        self.button_salida.clicked.connect(self.modal.show_modal)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        label_buttons.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        label_subtitulo.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        
        label_table_subtitulo.setContentsMargins(0, 0, 0, 8)
        label_table_subtitulo.setStyleSheet("font-size: 18px; color: #c1c1c1;")
        
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        button_layout.addWidget(self.button_salida)
        button_layout.addWidget(self.button_entrada)
        button_layout.addWidget(self.button_modificar)
        button_layout.addWidget(self.button_archivar)
        button_layout.addItem(h_spacer)
        button_layout.addWidget(self.button_recargar)
                
        table_head.addWidget(TableHeadWidget("N°"))
        table_head.addWidget(TableHeadWidget("Asunto"), 1)
        table_head.addWidget(TableHeadWidget("Destino"), 1)
        table_head.addWidget(TableHeadWidget("Salida registrada"), 1)
        table_head.addWidget(TableHeadWidget("Entrada registrada"), 1)
        table_head.addWidget(TableHeadWidget("Acciones"), 1)

        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setStyleSheet("""
            QScrollArea { 
                border: none; 
                background-color: transparent; 
                border-radius: 8px;
            }
            
            QScrollBar:vertical {
                border: none;
                background: #2D2D2D;    /* Fondo de la barra (gris oscuro) */
                width: 10px;            /* IMPORTANTE: Ancho, no altura */
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background-color: #555555;   /* Color del manejador */
                min-height: 20px;            /* Altura mínima */
                border-radius: 5px;          /* Bordes redondeados */
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #777777;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                height: 0px;
            }
            
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(0)
        
        scroll_area.setWidget(scroll_widget)

        self.main_layout.addWidget(label_subtitulo, 0, 0)
        self.main_layout.addWidget(label_titulo, 1, 0)
        self.main_layout.addItem(v_spacer, 2, 0)
        self.main_layout.addWidget(label_buttons, 3, 0)
        self.main_layout.addLayout(button_layout, 4, 0)
        self.main_layout.addItem(v_spacer, 5, 0)
        self.main_layout.addWidget(label_table_subtitulo, 6, 0)
        self.main_layout.addLayout(table_head, 7, 0)
        self.main_layout.addWidget(scroll_area, 8, 0)
        self.main_layout.setRowStretch(8, 1) 

        self.fetch_bitacoras()
        #self.buttons_actions()
        
    def cerrar_y_guardar(self):
        self.modal.hide_modal()
        
    def buttons_actions(self):
        self.button_salida.clicked.connect(self.form_salida)
        self.button_entrada.clicked.connect(self.form_salida)
        self.button_modificar.clicked.connect(self.form_salida)
        self.button_archivar.clicked.connect(self.form_salida)
        self.button_recargar.clicked.connect(self.form_salida)

    def fetch_bitacoras(self):
        self.thread = QThread()  
        self.worker = Fetch()    
        
        self.worker.moveToThread(self.thread) 

        self.thread.started.connect(lambda: self.worker.run(FBitacora.lista))
        
        self.worker.finished.connect(self.handle_data)
        self.worker.error.connect(self.handle_error)
        
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()
        print("Iniciando fetch de bitácoras...")

    def handle_data(self, data: list[Bitacora]):
        print(f"Datos recibidos: {len(data)} bitácoras.")
        
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not data:
            no_data_label = QLabel("No hay bitácoras para mostrar.")
            no_data_label.setStyleSheet("font-size: 16px; color: #888888;")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.scroll_layout.addWidget(no_data_label)
        else:
            for bitacora in data:
                card = BitacoraCardWidget(bitacora) 
                self.scroll_layout.addWidget(card)
        
        self.scroll_layout.addStretch()

    def handle_error(self, error_message):
        print(f"Error al hacer fetch: {error_message}")