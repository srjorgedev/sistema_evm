from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QFrame, QSizePolicy
from PyQt6.QtCore import Qt

from interface.components.table_head import TableHeadWidget
from interface.components.styles.table_style import scrollbar_style, scroll_widget_style, scroll_area_style

class TableWidget2(QFrame):
    def __init__(self, headers: list[str] = None):
        super().__init__()
        
        self._main_layout = QVBoxLayout(self)
        self.header_container = QFrame()
        self.header_layout = QHBoxLayout(self.header_container)
        
        # 🚨 SOLUCIÓN AL ATTRIBUTE ERROR: Asegurar que los atributos existan 🚨
        self.scroll_area = QScrollArea() 
        self.scroll_content_widget = QWidget()
        self.rows_layout = QVBoxLayout(self.scroll_content_widget)
        # -------------------------------------------------------------------
        
        self.header_container.setObjectName("headerContainer") 
        
        self._main_layout.setSpacing(0) 
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)
        self.rows_layout.setContentsMargins(0, 0, 0, 0)
        self.rows_layout.setSpacing(2)
        
        self.scroll_area.setWidgetResizable(True) 
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.rows_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_content_widget.setObjectName("scrollContent")
        self.scroll_content_widget.setStyleSheet(scroll_widget_style)
        self.scroll_area.setStyleSheet(scroll_area_style)
        self.scroll_area.setStyleSheet(scrollbar_style)
        self.scroll_content_widget.setStyleSheet(scroll_widget_style)
        self.header_container.setStyleSheet("""
            #headerContainer {
                background-color: #17272f; 
                border-top-left-radius: 0;
                border-top-right-radius: 8px;
                border-bottom: 1px solid #15313e; 
            }
        """)

        self.scroll_area.setWidget(self.scroll_content_widget)
        
        self._main_layout.addWidget(self.header_container)
        self._main_layout.addWidget(self.scroll_area)

        if headers:
            self.setHeaders(headers)

    def setHeaders(self, labels: list[str]):
        """
        Configura los encabezados con factores de estiramiento para alineación.
        """
        while self.header_layout.count():
            item = self.header_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        num_columns = len(labels)
        
        # Dentro de interface/components/table2.py -> setHeaders

# ...
        for i, text in enumerate(labels):
            widget = TableHeadWidget(text)
            
            # 🚨 CLAVE: Forzar la política de estiramiento antes de setFixedWidth
            # Esto asegura que el layout lo pueda estirar o comprimir.
            widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
            
            stretch_factor = 1 

            # --- Regla 1: Columna 'N°' (Fija) ---
            if i == 0 and text.upper() in ["N°", "ID", "CODIGO"]:
                widget.setFixedWidth(80) 
                stretch_factor = 0 
                    
                # --- Regla 2: Columna 'Acciones' (Fija) ---
            elif i == num_columns - 1 and text.upper() == "ACCIONES":
                ACCIONES_COLUMN_WIDTH = 100 
                widget.setFixedWidth(ACCIONES_COLUMN_WIDTH) 
                stretch_factor = 0
                
                # --- Regla 3: Columna de datos (Estiramiento) ---
            else:
                    # 🚨 Asegurar que las columnas de datos se estiren 
                widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
                stretch_factor = 1 
                
            self.header_layout.addWidget(widget, stretch_factor)
            # ...

        # Esencial: Un estiramiento final para empujar todo a la izquierda si el layout está incompleto
        self.header_layout.addStretch(1) 

    def addRow(self, row_widget: QWidget):
        self.rows_layout.addWidget(row_widget)
        
    def clearRows(self):
        while self.rows_layout.count():
            item = self.rows_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()