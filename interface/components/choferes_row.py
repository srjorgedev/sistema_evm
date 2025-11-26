from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from interface.components.button import ButtonWidget

from interface.components.styles.general import COLORS, COLORS_LIST

class ChoferRowWidget(QWidget):
    def __init__(self, data):
        """
        data: tupla (N°, Nombre, N° Licencia, Tipo, Vencimiento)
        """
        super().__init__()
        
        # --- Estilos ---
        self.setStyleSheet("""
            QWidget { background-color: transparent; }
            QLabel { font-size: 14px; color: #FFFFFF; font-weight: 500; }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 16, 8) 
        layout.setSpacing(10)
        
        # Políticas de tamaño
        fixed_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        expanding_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        # --- 1. Campos de Datos (Labels) ---
        data_values = [
            (str(data[0]), Qt.AlignmentFlag.AlignLeft),      # 0: N°
            (str(data[1]), Qt.AlignmentFlag.AlignLeft),      # 1: Nombre
            (str(data[2]), Qt.AlignmentFlag.AlignCenter),    # 2: N° Licencia
            (str(data[3]), Qt.AlignmentFlag.AlignCenter),    # 3: Tipo Licencia
            (str(data[4]), Qt.AlignmentFlag.AlignCenter)     # 4: Fecha Vencimiento
        ]
        
        # Crear y configurar los Labels
        for i, (text, alignment) in enumerate(data_values):
            lbl = QLabel(text)
            
            # 🚨 CLAVE DE ALINEACIÓN 1: Columna N° (índice 0) debe ser FIJA (80px)
            if i == 0:
                lbl.setFixedWidth(80) 
                lbl.setSizePolicy(fixed_policy) 
            # Columnas de datos intermedias: se estiran (índices 1 a 4)
            else:
                lbl.setSizePolicy(expanding_policy)
            
            lbl.setAlignment(alignment | Qt.AlignmentFlag.AlignVCenter) 
            layout.addWidget(lbl)
            
        # --- 2. Botones de Acción (Fijos) ---
        
        self.btn_edit = ButtonWidget("pencil", "", COLORS_LIST[COLORS.MODIFICAR]) 
        self.btn_delete = ButtonWidget("trash", "", COLORS_LIST[COLORS.ARCHIVAR])
        
        # 🚨 CLAVE DE ALINEACIÓN 2: Fijar el tamaño del botón a 30x30
        BUTTON_SIZE = 30 
        self.btn_edit.setFixedSize(BUTTON_SIZE, BUTTON_SIZE) 
        self.btn_delete.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        
        # Aplicar política fija para que no se estiren
        self.btn_edit.setSizePolicy(fixed_policy)
        self.btn_delete.setSizePolicy(fixed_policy)

        # Contenedor para botones
        actions_layout = QHBoxLayout()
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(5) 

        actions_layout.addWidget(self.btn_edit)
        actions_layout.addWidget(self.btn_delete)
        
        # Agrega el contenedor de acciones
        layout.addLayout(actions_layout)

        # 🚨 CLAVE DE ALINEACIÓN 3: Agrega un estiramiento final
        # Esto empuja los botones de acción al borde de su columna (ancho 100)
        layout.addStretch() 

        self.setLayout(layout)