from interface.components.sidemenu import SidemenuWidget
import sys
from PyQt6.QtWidgets import (
    QApplication, QStackedWidget,
    QMainWindow, QWidget,
    QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from interface.screens.screen import ScreenWidget
from interface.screens.bitacora_screen import BITScreenWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enterprise Vehicle Manager")
        
        widget_central = QWidget()
        self.layout_principal = QHBoxLayout(widget_central)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        
        self.sidemenu = SidemenuWidget()
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #0f181f;")
        
        self.stack.addWidget(ScreenWidget("VISTA DASHBOARD", "#2c3e50"))
        self.stack.addWidget(BITScreenWidget())
        self.stack.addWidget(ScreenWidget("VISTA SOLICITUDES", "#8e44ad"))
        self.stack.addWidget(ScreenWidget("VISTA EMPLEADOS", "#16a085"))
        self.stack.addWidget(ScreenWidget("VISTA VEHICULOS", "#c0392b"))
        self.stack.addWidget(ScreenWidget("VISTA MANTENIMIENTOS", "#2980b9"))
        
        self.sidemenu.current_page.connect(self.stack.setCurrentIndex)

        self.layout_principal.addWidget(self.sidemenu)
        
        # contenido_principal = QLabel("Contenido Principal de la App")

        # contenido_principal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # contenido_principal.setStyleSheet("background-color: #FFFFFF; font-size: 20px;")
        
        self.layout_principal.addWidget(self.stack, 1) 

        self.setCentralWidget(widget_central)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.showMaximized()
    sys.exit(app.exec())