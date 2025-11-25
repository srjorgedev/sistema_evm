scrollbar_style = """
QScrollArea { 
    border: none; 
    background-color: transparent; 
    border-radius: 8px;
}

QScrollBar:vertical {
    border: none;
    background: #2D2D2D;    
    width: 8px;            
    margin: 4px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background-color: #555555;   
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background-color: #777777;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
"""

scroll_widget_style = """
#scrollContent {
    background-color: #131e24;
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
}
"""

scroll_area_style = """
QScrollArea {
    border: none;
    background: transparent;
}

QScrollArea QWidget#tableWidget {
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    background-color: #131e24;
}

QScrollArea > QWidget {
    border: none;
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    background-color: #19272c;
}
"""