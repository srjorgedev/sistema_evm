import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QColor, QPalette
from interface.ui.components.sidemenu_button import MenuButtonWidget

datos_menu = [
    ("Dashboard", "dashboard"),
    ("Bitacoras", "register"),
    ("Solicitudes", "request"),
    ("Empleados", "employees"),
    ("Vehiculos", "car"),
    ("Mantenimientos", "maintenance")
]

class SidemenuWidget(QWidget):
    
    current_page = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()

        self.setFixedWidth(256)
        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding
        )

        self.layout_vertical = QVBoxLayout(self)
        self.layout_vertical.setContentsMargins(0, 12, 0, 12)
        self.layout_vertical.setSpacing(8)

        self.botones_menu: list[MenuButtonWidget] = []

        for i, (texto, icono) in enumerate(datos_menu):
            boton = MenuButtonWidget(texto, icono)
            boton.clicked.connect(self.manejar_clic_menu)
            
            self.layout_vertical.addWidget(boton, 0, Qt.AlignmentFlag.AlignHCenter)
            self.botones_menu.append(boton)

        self.layout_vertical.addStretch()

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("#242424"))
        self.setPalette(paleta)
        
        if self.botones_menu:
            self.botones_menu[0].set_active(True)

    def manejar_clic_menu(self):
        boton_clickeado = self.sender()
        
        for i, boton in enumerate(self.botones_menu):
            is_active = (boton is boton_clickeado)
            boton.set_active(is_active)
            
            if is_active:
                self.current_page.emit(i)
