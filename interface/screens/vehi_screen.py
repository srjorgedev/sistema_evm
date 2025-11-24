# VEHIScreenWidget.py

from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt
from interface.components.button import ButtonWidget, ColorKeys
from interface.components.modal import ModalWidget

from interface.components.vehiculos_modal import VehiculosModal


class VEHIScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QGridLayout(self)
        button_layout = QHBoxLayout()

        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)

        # TITULO
        label_titulo = QLabel("VEHÍCULOS")
        label_titulo.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")

        label_subtitulo = QLabel("Panel de Control")
        label_subtitulo.setStyleSheet("font-size: 18px; color: #aaaaaa;")
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft)

        label_buttons = QLabel("Acciones")
        label_buttons.setStyleSheet("font-size: 18px; color: #aaaaaa;")

        # BOTONES
        self.button_vehiculos = ButtonWidget("car", "Ver Vehículos", ColorKeys.CREAR)
        self.button_agregar = ButtonWidget("car", "Agregar vehículo", ColorKeys.CREAR)
        self.button_modificar = ButtonWidget("car", "Modificar matrícula", ColorKeys.MODIFICAR)
        self.button_baja = ButtonWidget("car", "Dar de baja", ColorKeys.ARCHIVAR)

        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        button_layout.addWidget(self.button_vehiculos)
        button_layout.addWidget(self.button_agregar)
        button_layout.addWidget(self.button_modificar)
        button_layout.addWidget(self.button_baja)

        spacer = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.main_layout.addWidget(label_subtitulo, 0, 0)
        self.main_layout.addWidget(label_titulo, 1, 0)
        self.main_layout.addItem(spacer, 2, 0)
        self.main_layout.addWidget(label_buttons, 3, 0)
        self.main_layout.addLayout(button_layout, 4, 0)

        # SCROLL AREA
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

        # MODAL PARA VER VEHÍCULOS
        self.vehiculos_modal = ModalWidget(self, VehiculosModal())
        self.button_vehiculos.clicked.connect(self.vehiculos_modal.show_modal)

        