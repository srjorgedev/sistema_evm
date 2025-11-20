import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, QSpacerItem
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtSvgWidgets import QSvgWidget

from utils.load_resource import ruta_svg
from interface.components.sidemenu_button import MenuButtonWidget

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
        
        # Creación de elementos
        self.layout_vertical = QVBoxLayout(self)
        self.layout_horizontal = QHBoxLayout()
        img_logo = QLabel("EVM")
        sidebar_icon = QSvgWidget()
        
        self.botones_menu: list[MenuButtonWidget] = []
        for texto, icono in datos_menu:
            self.botones_menu.append(MenuButtonWidget(texto, icono))

        # Asignación de atributos
        self.setFixedWidth(256)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("#131e24"))
        self.setPalette(paleta)

        self.layout_vertical.setContentsMargins(0, 24, 0, 12)
        self.layout_vertical.setSpacing(8)

        self.layout_horizontal.setContentsMargins(24, 0, 24, 0)
        
        img_logo.setStyleSheet("font-size: 24px; font-weight: bold; color: #f1f1f1;")
        self.setStyleSheet("SideMenuWidget {border-left: 2px solid #11465b;}")
        
        sidebar_icon.setFixedSize(24, 24)
        icon_path = ruta_svg("sidebar")
        if icon_path.exists():
            sidebar_icon.load(str(icon_path))
        else:
            print(f"Advertencia: Icono no encontrado en {icon_path}")

        for i, boton in enumerate(self.botones_menu):
            boton.clicked.connect(self.manejar_clic_menu)

        if self.botones_menu:
            self.botones_menu[0].set_active(True)

        # Layout
        self.layout_horizontal.addWidget(img_logo)
        self.layout_horizontal.addWidget(sidebar_icon)
        
        self.layout_vertical.addLayout(self.layout_horizontal)
        self.layout_vertical.addItem(QSpacerItem(8, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))

        for boton in self.botones_menu:
            self.layout_vertical.addWidget(boton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.layout_vertical.addStretch()

    def manejar_clic_menu(self):
        boton_clickeado = self.sender()
        
        for i, boton in enumerate(self.botones_menu):
            is_active = (boton is boton_clickeado)
            boton.set_active(is_active)
            
            if is_active:
                self.current_page.emit(i)
