import sys
from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTabWidget
from PyQt6.QtCore import Qt, pyqtSignal

import controllers.bitacora_controller as FBitacora
import controllers.user_controller as FUsuario

from domain.usuarios.CRUD import registrar_empleado
from interface.components.bitacoras.bitacora_row import BitacoraRowWidget
from interface.components.bitacoras.bitacora_row_archive import BitacoraArchivedRowWidget
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget
from interface.components.data_fetch import TaskRunner
from interface.components.modal import ModalWidget
from interface.components.bitacoras.salida_form import SalidaFormWidget
from interface.components.bitacoras.entrada_form import EntradaFormWidget
from interface.components.table2 import TableWidget2
from interface.components.user_row import UserRowWidget
from interface.components.tipo_row import TypeRowWidget
from interface.components.nuevo_user_form import NewUserFormWidget
from interface.components.choferes_row import ChoferRowWidget
from interface.components.contacto_row import ContactosRowWidget
import controllers.user_controller as FUser

from interface.components.styles.table_style import tab_style
from interface.components.styles.general import COLORS, COLORS_LIST

from utils.log import log

class USERScreenWidget(QWidget):
    btn_archivar = pyqtSignal()
  
    
    notificar = pyqtSignal(str,str,str)
    
    def __init__(self):
        super().__init__()
        
        table_headers = ["N°", "Nombre", "Rol", "Acciones"]
        tipo_headers = ["Codigo", "Descripcion", "Acciones"]
        chofer_headers = ["N°", "Nombre", "Numero de Licencia", "Tipo de Licencia", "Fecha de Vencimiento", "Acciones"]
        contactos_headers = ["N°", "Nombre", "Correo Electrónico", "Teléfono", "Acciones"]
        
        # Creacion de elementos
        self.main_layout = QVBoxLayout(self)
        label_titulo = QLabel("EMPLEADOS")
        button_layout = QHBoxLayout()
        label_subtitulo = QLabel("Panel de Control")
        label_buttons = QLabel("Acciones rapidas")
        
        # Las tablas ahora estarán dentro de las pestañas
        self.table = TableWidget2(table_headers)
        self.tipos_table = TableWidget2(tipo_headers)
        self.choferes_table = TableWidget2(chofer_headers)
        self.contactos_table = TableWidget2(contactos_headers)
        # Creación del QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.table, "Empleados registrados")
        self.tabs.addTab(self.tipos_table, "Tipos de empleados")
        self.tabs.addTab(self.choferes_table, "Choferes")
        self.tabs.addTab(self.contactos_table, "Contactos")

        # Instancia del objeto para realizar operaciones con la BD en segundo plano.
        self.runner = TaskRunner(self)
        
        # Elementos espaciadores
        v_spacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        h_spacer = QSpacerItem(128, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        
        # ----------------------------------------------------
        # 🚨 SECCIÓN CORREGIDA: Creación de Botones (debe ir antes de la conexión)
        # Botones
        self.button_agregar = ButtonWidget("add", "Registrar empleados", COLORS_LIST[COLORS.CREAR])
        self.button_modificar = ButtonWidget("modify", "Modificar", COLORS_LIST[COLORS.CREAR])
        self.button_archivar = ButtonWidget("archive", "Eliminar", COLORS_LIST[COLORS.CREAR])
        self.button_recargar = SquareButtonWidget("reload", "#f1f1f1")
        # ----------------------------------------------------

        # ----------------------------------------------------
        # 🚨 SECCIÓN CORREGIDA: Creación y Conexión del Modal (sin duplicados)
        self.user_form = NewUserFormWidget()
        self.modal_salida = ModalWidget(self, self.user_form, "Registrar un nuevo usuario.")
        
        self.user_form.registro_solicitado.connect(self.register_new_user)
        
        # Asignacion de eventos en los botones cuando se hace clic
        self.button_agregar.clicked.connect(self.modal_salida.show_modal)
        
        # CONEXIÓN CLAVE: Conectar la señal de registro del formulario al método
        self.user_form.registro_solicitado.connect(self.register_new_user)
        # ----------------------------------------------------
        
        
        # Asignacion de atributos 
        self.main_layout.setContentsMargins(48, 52, 48, 0) 
        self.main_layout.setSpacing(0)
        
        # Asignacion de estilos
        label_titulo.setStyleSheet(f"font-size: 40px; font-weight: bold; color:{COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_buttons.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        label_subtitulo.setStyleSheet(f"font-size: 18px; color: {COLORS_LIST[COLORS.TEXTO_OSCURO]};")
        
        # Alineamos la posicion de elementos 
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Espacios en otros elementos
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(16)
        
        # Agragamos los botones al contenedor de botones
        button_layout.addWidget(self.button_agregar)
        button_layout.addWidget(self.button_modificar)
        button_layout.addWidget(self.button_archivar)
        button_layout.addItem(h_spacer)
        button_layout.addWidget(self.button_recargar)

        self.main_layout.addWidget(label_subtitulo)
        self.main_layout.addWidget(label_titulo)
        self.main_layout.addSpacerItem(v_spacer)
        self.main_layout.addWidget(label_buttons)
        self.main_layout.addLayout(button_layout)
        self.main_layout.addSpacerItem(v_spacer)
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addSpacerItem(v_spacer)

        self.apply_tab_styles()

        # Llamamos a la funcion que pide los datos.
        self.fetch_usuarios()
        self.fetch_tipos_empleado()
        self.fetch_choferes()
        self.fetch_contactos()

    def apply_tab_styles(self):
        self.tabs.setStyleSheet(tab_style)
        
    def fetch_tipos_empleado(self):
        log("[USUARIOS]: Iniciando fetch de tipos...")
        self.runner.run(
            func=FUser.lista_tipos,
            on_success= lambda a: self.handle_tipos(a, self.tipos_table),
            on_error=lambda e: log(f"[USUARIOS]: Error -> {e}")
            )
        
    # Funcion para pedir los datos 
    def fetch_usuarios(self):
        log("[USUARIOS]: Iniciando fetch general...")
        self.runner.run(
            func=FUsuario.lista_general, 
            on_success=lambda data: self.handle_data(data, self.table), 
            on_error=self.handle_error
        )
    
    def fetch_choferes(self):
        log("[USUARIOS]: Fetch de choferes...")
        self.runner.run(
            func=FUsuario.lista_choferes,
            on_success=lambda data: self.handle_choferes(data, self.choferes_table),
            on_error=lambda e: log(f"[USUARIOS]: Error choferes -> {e}")
        )

    def handle_data(self, data: list[tuple], parent: TableWidget2):
        log(f"[USUARIOS]: Datos recibidos -> {len(data)} bitácoras.")
        
        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay empleados para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setContentsMargins(0, 16, 0, 0)
            
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for bitacora in data:
                card = UserRowWidget(bitacora) 
                card.btn_archivo.connect(lambda: print("HI"))
                parent.addRow(card)
    
    def handle_tipos(self, data: list[tuple], parent: TableWidget2):
        log(f"[USUARIOS]: Datos recibidos -> {len(data)} bitácoras.")
        
        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay tipos para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setContentsMargins(0, 16, 0, 0)
            
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for bitacora in data:
                card = TypeRowWidget(bitacora) 
                card.btn_archivo.connect(lambda: print("HI"))
                parent.addRow(card)
    
    def handle_choferes(self, data: list[tuple], parent: TableWidget2):
        log(f"[USUARIOS]: Choferes recibidos -> {len(data)}")

        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay choferes para mostrar.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for chofer in data:
                card = ChoferRowWidget(chofer) 
                parent.addRow(card)

    # --- Métodos para el Registro de Nuevo Empleado ---
    def register_new_user(self, data: dict):
        try:
            registrar_empleado(data)
            self.handle_registration_success()
        except Exception as e:
            self.notificar.emit("Error", f"Error al registrar: {e}", "ARCHIVAR")



    def handle_registration_success(self):
        """
        Se ejecuta después de que FUsuario.registrar_general regresa sin error.
        """
        log("[USUARIOS]: Registro de empleado exitoso.")
        self.modal_salida.hide_modal() # Cierra el modal de registro
        
        # Notifica al usuario del éxito
        self.notificar.emit("Éxito", "Empleado registrado correctamente.", "CREAR")
        
        # Recarga la tabla para mostrar el nuevo empleado
        self.fetch_usuarios()
        
    def handle_error(self, error_message):
        log(f"[USUARIOS]: Error al hacer fetch -> {error_message}")
        
   # No olvides importar el nuevo componente

    # ... dentro de USERScreenWidget ...

    def fetch_contactos(self):
        log("[USUARIOS]: Fetch de contactos...")
        self.runner.run(
            func=FUser.lista_contactos, # Asegúrate de haber agregado esto en el controller
            on_success=lambda data: self.handle_contactos(data, self.contactos_table),
            on_error=lambda e: log(f"[USUARIOS]: Error contactos -> {e}")
        )

    def handle_contactos(self, data: list[tuple], parent: TableWidget2):
        log(f"[USUARIOS]: Contactos recibidos -> {len(data)}")
        
        parent.clearRows()

        if not data:
            no_data_label = QLabel("No hay información de contacto.")
            no_data_label.setStyleSheet("background-color: transparent; font-size: 16px; color: #888888;")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            parent.addRow(no_data_label)
        else:
            for contacto in data:
                # contacto es la tupla (Numero, Nombre, Email, Telefono)
                card = ContactosRowWidget(contacto)
                parent.addRow(card)
                

