from interface.components.styles.general import COLORS, COLORS_LIST

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

scroll_widget_style = f"""
#scrollContent {{
    background-color: {COLORS_LIST[COLORS.SIDE_CLARO_1]};
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
}}
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

tab_style = f"""
    QTabWidget::pane {{
        background-color: #f1f1f1;
    }}
    QTabBar::tab {{
        background: transparent;
        color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};
        border: 2px solid {COLORS_LIST[COLORS.TABLA_CLARO]};
        border-bottom: none;
        padding: 8px 24px;
        font-size: 14px;
        border-top-left-radius: 8px; 
        border-top-right-radius: 8px;
        margin-right: 4px; /* Pequeño espacio entre pestañas */
    }}
    QTabBar::tab:selected {{
        background: {COLORS_LIST[COLORS.TABLA_CLARO]}; 
        color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};
        border-color: {COLORS_LIST[COLORS.TABLA_CLARO]};
        border-bottom-color: {COLORS_LIST[COLORS.BG_CLARO_1]};
    }}
    QTabBar::tab:hover:!selected {{
        background: {COLORS_LIST[COLORS.BG_CLARO_2]}; 
        color: {COLORS_LIST[COLORS.BG_CLARO_4]};
    }}
    QTabBar::tab:!selected {{
        margin-top: 2px; 
        color: {COLORS_LIST[COLORS.BG_CLARO_4]};
    }}
"""