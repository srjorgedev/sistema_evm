from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from interface.components.button import ButtonWidget, ColorKeys

class ContactosRowWidget(QWidget):
    def __init__(self, data):
        """
        data: tupla (Numero, Nombre, Email, Telefono)
        """
        super().__init__()

        # --- ESTILOS ---
        # Fondo transparente para que se vea integrado en la tabla
        self.setStyleSheet("""
            QWidget { background-color: transparent; }
            QLabel { font-size: 14px; color: #FFFFFF; font-weight: 500; }
        """)

        layout = QHBoxLayout(self)
        # Ajustamos márgenes para que se vea limpio
        layout.setContentsMargins(16, 8, 16, 8) 
        layout.setSpacing(10)
        
        # Políticas de tamaño
        fixed_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        expanding_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        # --- 1. DATOS DE LA FILA ---
        # data[0]: Numero, data[1]: Nombre, data[2]: Email, data[3]: Telefono
        
        # Columna 1: N° (Fijo para alinearse con el header)
        lbl_num = QLabel(str(data[0]))
        lbl_num.setFixedWidth(80) 
        lbl_num.setSizePolicy(fixed_policy)
        lbl_num.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Columna 2: Nombre (Se expande)
        lbl_nombre = QLabel(str(data[1]))
        lbl_nombre.setSizePolicy(expanding_policy)
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Columna 3: Email (Se expande)
        lbl_email = QLabel(str(data[2]))
        lbl_email.setSizePolicy(expanding_policy)
        lbl_email.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Columna 4: Teléfono (Se expande y centra)
        lbl_tel = QLabel(str(data[3]))
        lbl_tel.setSizePolicy(expanding_policy)
        lbl_tel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregamos los textos al layout
        layout.addWidget(lbl_num)
        layout.addWidget(lbl_nombre)
        layout.addWidget(lbl_email)
        layout.addWidget(lbl_tel)

        # --- 2. BOTONES DE ACCIÓN (ESTILO VISUAL EXACTO) ---
        
        # Contenedor para los botones (Acciones)
        actions_layout = QHBoxLayout()
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(8) # Espacio entre el lápiz y la basura
        
        # Botón Modificar (Lápiz)
        # Pasamos texto vacio "" para activar el modo "solo ícono/delineado"
        self.btn_edit = ButtonWidget("pencil", "", ColorKeys.MODIFICAR)
        self.btn_edit.setFixedSize(30, 30) # Tamaño pequeño y cuadrado
        
        # Botón Eliminar (Basura)
        self.btn_delete = ButtonWidget("trash", "", ColorKeys.ARCHIVAR)
        self.btn_delete.setFixedSize(30, 30) # Tamaño pequeño y cuadrado

        # Añadimos los botones al layout de acciones
        actions_layout.addWidget(self.btn_edit)
        actions_layout.addWidget(self.btn_delete)
        
        # --- 3. ALINEACIÓN FINAL ---
        
        # Primero, añadimos el layout de acciones a la fila
        layout.addLayout(actions_layout)
        
        # CRUCIAL: Añadimos un 'stretch' al final.
        # Esto asegura que si la tabla es muy ancha, los botones se queden pegados
        # a la izquierda de su columna imaginaria o permite controlar su posición.
        # Si quieres que se peguen totalmente a la derecha, pon el stretch ANTES de actions_layout.
        # Para que se vean como en tu imagen (columna Acciones), lo dejamos así y 
        # confiamos en el ancho fijo del widget padre o header.
        
        # Para forzar que ocupen el espacio de la columna "Acciones" definida en TableWidget:
        # Simplemente con agregarlos al final es suficiente si los labels anteriores son Expanding.

        self.setLayout(layout)