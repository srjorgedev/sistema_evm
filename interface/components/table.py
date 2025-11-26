from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt

from interface.components.table_head import TableHeadWidget

from interface.components.styles.table_style import scrollbar_style, scroll_widget_style, scroll_area_style

from interface.components.styles.general import COLORS, COLORS_LIST

class TableWidget(QFrame):
    def __init__(self, headers: list[str] = None):
        super().__init__()
        
        self._main_layout = QVBoxLayout(self)
        self.header_container = QFrame()
        self.header_layout = QHBoxLayout(self.header_container)
        self.scroll_area = QScrollArea()
        self.scroll_content_widget = QWidget()
        self.rows_layout = QVBoxLayout(self.scroll_content_widget)
        
        self.header_container.setObjectName("headerContainer") 
        
        self._main_layout.setSpacing(0) 
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)
        self.rows_layout.setContentsMargins(0, 0, 0, 0)
        self.rows_layout.setSpacing(0)
        
        self.scroll_area.setWidgetResizable(True) 
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.rows_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_content_widget.setObjectName("scrollContent")
        self.scroll_content_widget.setStyleSheet(scroll_widget_style)
        self.scroll_area.setStyleSheet(scroll_area_style)
        self.scroll_area.setStyleSheet(scrollbar_style)
        self.scroll_content_widget.setStyleSheet(scroll_widget_style)
        self.header_container.setStyleSheet(f"""
            #headerContainer {{
                background-color: {COLORS_LIST[COLORS.TABLA_CLARO]};  
                border-top-left-radius: 0;
                border-top-right-radius: 8px;
                border-bottom: 2px solid {COLORS_LIST[COLORS.BG_CLARO_1]}; 
            }}
        """)

        self.scroll_area.setWidget(self.scroll_content_widget)
        
        self._main_layout.addWidget(self.header_container)
        self._main_layout.addWidget(self.scroll_area)

        if headers:
            self.setHeaders(headers)

    def setHeaders(self, labels: list[str]):
        for i, text in enumerate(labels):
            widget = TableHeadWidget(text)
            
            if i == 0 and labels[i].upper() in ["CODIGO", "N°", "ID"]:
                widget.setFixedWidth(80) 
                self.header_layout.addWidget(widget, 0, Qt.AlignmentFlag.AlignCenter)
            else: 
                self.header_layout.addWidget(widget, 1)

    def addRow(self, row_widget: QWidget):
        self.rows_layout.addWidget(row_widget)
        
    def clearRows(self):
        while self.rows_layout.count():
            item = self.rows_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()