from interface.components.sidemenu import SidemenuWidget
import sys
from PyQt6.QtWidgets import (
    QApplication, QStackedWidget,
    QMainWindow, QWidget,
    QHBoxLayout
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal

from interface.screens.screen import ScreenWidget
from interface.screens.bitacora_screen import BITScreenWidget
from interface.screens.vehi_screen import VEHIScreenWidget
from interface.screens.soli_screen import SOLIScreenWidget
from interface.components.notifications import NotificationContainerWidget
from interface.screens.users_screen import USERScreenWidget
from interface.screens.mante_screen import MANTEScreenWidget

from interface.components.styles.general import COLORS_LIST, COLORS

from db.ConnB import Conn

class DBTest(QThread):
    finished = pyqtSignal(bool)
    notification = pyqtSignal(object)

    def run(self):
        status = Conn().comprobarConexion()
        self.finished.emit(status)

class VentanaPrincipal(QMainWindow):
    notification = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enterprise Vehicle Manager")

        widget_central = QWidget()
        self.layout_principal = QHBoxLayout(widget_central)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        
        self.pantalla_bitacora = BITScreenWidget()
        
        self.sidemenu = SidemenuWidget()
        self.stack = QStackedWidget()
        self.notification_container = NotificationContainerWidget(self)
        
        self.pantalla_bitacora.notificar.connect(self.notification_container.nueva_notificacion)
        
        self.stack.setStyleSheet(f"background-color: {COLORS_LIST[COLORS.BG_OSCURO_1]};")
        
        # self.stack.addWidget(ScreenWidget("VISTA DASHBOARD", "#2c3e50"))
        self.stack.addWidget(self.pantalla_bitacora)
        self.stack.addWidget(SOLIScreenWidget())
        self.stack.addWidget(USERScreenWidget())
        self.stack.addWidget(VEHIScreenWidget())
        self.stack.addWidget(MANTEScreenWidget())
        
        self.sidemenu.current_page.connect(self.stack.setCurrentIndex)

        self.layout_principal.addWidget(self.sidemenu)
        self.layout_principal.addWidget(self.stack, 1) 

        self.setCentralWidget(widget_central)
        
        self.notification_container.raise_()
        
        self.test_db_connection()
        
    def test_db_connection(self):
        self.worker = DBTest()
        self.worker.finished.connect(self.handle_db_result)
        self.worker.start()

    def handle_db_result(self, status):
        if not status:
            self.notification_container.nueva_notificacion("Error", "No se pudo conectar a la base de datos.", "#c0392b")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        
        container_width = 340 
        
        x = self.width() - container_width
        y = 0
        h = self.height()
        
        self.notification_container.setGeometry(x, y, container_width, h)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.showMaximized()
    sys.exit(app.exec())