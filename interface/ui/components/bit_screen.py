# NUEVO: Importaciones necesarias para el threading y los datos
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt, QThread
import interface.bitacoras.fBitacora as FBitacora
from interface.ui.components.bit_card import BitacoraCardWidget
from domain.bitacoras.ClaseBitacora import Bitacora
from interface.ui.components.button import ButtonWidget
from interface.ui.components.button import ColorKeys
from interface.ui.components.data_fetch import Fetch

class BITScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QGridLayout(self)
        button_layout = QHBoxLayout()

        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)

        label_titulo = QLabel("BITACORAS")
        label_titulo.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        
        label_subtitulo = QLabel("Panel de Control")
        label_subtitulo.setStyleSheet("font-size: 18px; color: #aaaaaa;")
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        label_buttons = QLabel("Acciones")
        
        label_buttons.setStyleSheet("font-size: 18px; color: #aaaaaa;")
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        button_layout.addWidget(ButtonWidget("register", "Registrar salida", ColorKeys.CREAR))
        button_layout.addWidget(ButtonWidget("register", "Registrar entrada", ColorKeys.CREAR))
        button_layout.addWidget(ButtonWidget("register", "Modificar", ColorKeys.MODIFICAR))
        button_layout.addWidget(ButtonWidget("register", "Archivar", ColorKeys.ARCHIVAR))
        
        spacer = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.main_layout.addWidget(label_subtitulo, 0, 0)
        self.main_layout.addWidget(label_titulo, 1, 0)
        self.main_layout.addItem(spacer, 2, 0)
        self.main_layout.addWidget(label_buttons, 3, 0)
        self.main_layout.addLayout(button_layout, 4, 0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        self.scroll_widget = QWidget() 
        self.scroll_layout = QVBoxLayout(self.scroll_widget) 
        self.scroll_layout.setContentsMargins(0, 16, 0, 0)
        self.scroll_layout.setSpacing(16)
        
        self.scroll_area.setWidget(self.scroll_widget)
        
        self.main_layout.addWidget(self.scroll_area, 5, 0)
        self.main_layout.setRowStretch(5, 1) 

        self.fetch_bitacoras()

    def fetch_bitacoras(self):
        self.thread = QThread()  
        self.worker = Fetch()    
        
        self.worker.moveToThread(self.thread) 
        
        print("Callable?:", callable(FBitacora.lista))
        print("FBitacora.lista =", FBitacora.lista, type(FBitacora.lista))
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