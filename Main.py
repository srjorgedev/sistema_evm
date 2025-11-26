import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from PyQt6.QtCore import Qt, QThread, pyqtSignal

# Componentes y pantallas
from interface.components.sidemenu import SidemenuWidget
from interface.components.notifications import NotificationContainerWidget
from interface.components.styles.general import COLORS_LIST, COLORS

from interface.screens.bitacora_screen import BITScreenWidget
from interface.screens.vehi_screen import VEHIScreenWidget
from interface.screens.soli_screen import SOLIScreenWidget
from interface.screens.users_screen import USERScreenWidget
from interface.screens.mante_screen import MANTEScreenWidget
from interface.screens.obser_screen import OBSERScreenWidget

from db.conn import conn

# --- Hilo para probar conexión ---
class DBTest(QThread):
    finished = pyqtSignal(bool)
    notification = pyqtSignal(object)

    def run(self):
        try:
            miConn = conn()
            if miConn.conexion.is_connected():
                self.finished.emit(True)
            else:
                self.finished.emit(False)
        except:
            self.finished.emit(False)

# --- Ventana Principal ---
class VentanaPrincipal(QMainWindow):
    notification = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enterprise Vehicle Manager")

        # Layout central
        widget_central = QWidget()
        self.layout_principal = QHBoxLayout(widget_central)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setContentsMargins(0, 0, 0, 0)

        # SideMenu y Stack
        self.sidemenu = SidemenuWidget()
        self.stack = QStackedWidget()
        self.notification_container = NotificationContainerWidget(self)

        self.pantalla_bitacora.notificar.connect(self.notification_container.nueva_notificacion)
        
        self.stack.setStyleSheet(f"background-color: {COLORS_LIST[COLORS.BG_CLARO_1]};")
        
        # self.stack.addWidget(ScreenWidget("VISTA DASHBOARD", "#2c3e50"))
        self.stack.addWidget(self.pantalla_bitacora)
        self.stack.addWidget(SOLIScreenWidget())
        self.stack.addWidget(USERScreenWidget())
        self.stack.addWidget(VEHIScreenWidget())
        self.stack.addWidget(MANTEScreenWidget())   # Mantenimiento
        self.stack.addWidget(OBSERScreenWidget())   # Observaciones

        # Conectar side menu con stack
        self.sidemenu.current_page.connect(self.stack.setCurrentIndex)

        # Layout principal
        self.layout_principal.addWidget(self.sidemenu)
        self.layout_principal.addWidget(self.stack, 1)
        self.setCentralWidget(widget_central)

        # Notificaciones
        self.notification_container.raise_()

        # Test DB
        self.test_db_connection()

    def test_db_connection(self):
        self.worker = DBTest()
        self.worker.finished.connect(self.handle_db_result)
        self.worker.start()

    def handle_db_result(self, status):
        if not status:
            self.notification_container.nueva_notificacion(
                "Error", "No se pudo conectar a la base de datos.", "#c0392b"
            )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        container_width = 340
        x = self.width() - container_width
        y = 0
        h = self.height()
        self.notification_container.setGeometry(x, y, container_width, h)

# --- Main ---
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.showMaximized()
    sys.exit(app.exec())
