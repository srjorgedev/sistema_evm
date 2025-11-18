from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

class ScreenWidget(QWidget):
    def __init__(self, texto, color_fondo):
        super().__init__()
        self.setStyleSheet(f"background-color: {color_fondo};")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        label = QLabel(texto)
        label.setStyleSheet("font-size: 30px; font-weight: bold; color: white;")
        layout.addWidget(label)