from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from interface.components.notification_item import NotificacionItemWidget

class NotificationContainerWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True) 
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 8, 8, 16)
        self.main_layout.setSpacing(8)
        
        self.main_layout.addStretch(1)

    def nueva_notificacion(self, titulo, mensaje, color):
        item = NotificacionItemWidget(titulo, mensaje, color, self)
        item.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        
        self.main_layout.addWidget(item)