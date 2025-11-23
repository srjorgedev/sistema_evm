from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt

from interface.components.table_head import TableHeadWidget

from interface.components.styles.table_style import scrollbar_style, scroll_widget_style, scroll_area_style

class BITTableWidget(QFrame):
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
        for i, text in enumerate(labels):
            widget = TableHeadWidget(text)
            
            if i == 0:
                widget.setFixedWidth(60) 
            
            self.header_layout.addWidget(widget)

    def addRow(self, row_widget: QWidget):
        self.rows_layout.addWidget(row_widget)
        
    def clearRows(self):
        while self.rows_layout.count():
            item = self.rows_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()