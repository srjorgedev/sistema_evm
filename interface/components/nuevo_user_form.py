import sys
import hashlib
import os
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, QScrollArea, QSpacerItem
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.button import ButtonWidget, ColorKeys
from interface.components.square_button import SquareButtonWidget

import controllers.bitacora_controller as FBitacora
import controllers.observaciones_controller as FObservaciones
import controllers.user_controller as FUser

from utils.log import log

class NewUserFormWidget(QWidget):
    # 🚨 1. SEÑAL: Emitirá los datos listos para el controlador (FUsuario.registrar_general)
    registro_solicitado = pyqtSignal(dict) 
    
    def __init__(self):
        super().__init__()
        
        self.runner = TaskRunner(self)
        
        self.main_layout = QVBoxLayout(self)
        
        # --- 2. ASIGNACIÓN CLAVE: Asignar inputs como atributos ---
        self.select_tipos = SelectWidget("Tipo de empleado *", "Seleccione un tipo...")
        self.nombre_input = InputWidget("Nombre(s) *")
        self.prim_apd = InputWidget("Primer apellido *")
        self.seg_apd = InputWidget("Segundo apellido")
        self.correo = InputWidget("Correo electronico *")
        self.contrasena = InputWidget("Contraseña *", None, True)
        self.crear_boton = ButtonWidget(None, "Registrar empleado", ColorKeys.CREAR)
        
        layout_apd = QHBoxLayout()
        layout_cred = QHBoxLayout()
        
        layout_apd.addWidget(self.prim_apd)
        layout_apd.addWidget(self.seg_apd)
        
        layout_cred.addWidget(self.correo)
        layout_cred.addWidget(self.contrasena)
        
        self.main_layout.addWidget(self.nombre_input)
        self.main_layout.addLayout(layout_apd)
        self.main_layout.addLayout(layout_cred)
        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.crear_boton)
        self.main_layout.addStretch()
        
        # 3. CONEXIÓN: Conectar el botón a la función de envío
        self.crear_boton.clicked.connect(self.submit_registration)
        
        # 🚨 CAMBIO 1: Eliminamos la llamada a la BD y usamos el nuevo método fijo
        self.agregar_tipos_fijos()
        
    # 🚨 CAMBIO 2: Nuevo método para cargar los tipos de forma estática 
    def agregar_tipos_fijos(self):
        log("[NEW USER FORM]: Cargando tipos de empleado fijos.")
        items_fijos = [
            # Formato: (Texto a mostrar, Valor a enviar a la BD)
            # Asegúrate de que los códigos (ADM, CHOF, etc.) coincidan con tu columna tipo_empleado
            ("Administrador", "ADM"),
            ("Chofer", "CHOF"),
            ("Vigilante", "VIG"),
            ("Empleado-Usuario", "USER")
        ]
        
        self.select_tipos.addItems(items_fijos)

    # 🚨 CÓDIGO ELIMINADO: Ya no se usa la BD para esta función
    # def fetch_tipos_empleado(self):
    #     self.runner.run(
    #         func=FUser.lista_tipos,
    #         on_success= lambda a: self.agregar_tipos(a),
    #         on_error=lambda e: log(f"[NEW USER FORM]: Error -> {e}")
    #         )
        
    # def agregar_tipos(self, datos):
    #     items = []
    #     for tupla in datos:
    #         items.append((f"{tupla[0]} - {tupla[1]}", tupla[0])) 
    #     self.select_tipos.addItems(items) 
        
    # --- FUNCIONALIDAD CLAVE DE ENVÍO ---
    # Dentro de la clase NewUserFormWidget
    def submit_registration(self):
        log("[NEW USER FORM]: Solicitud de registro iniciada.")
        
        # 1. Obtener datos
        nombre = self.nombre_input.get_text()
        apellido_paterno = self.prim_apd.get_text()
        apellido_materno = self.seg_apd.get_text()
        correo = self.correo.get_text()
        contrasena_plana = self.contrasena.get_text() # <-- Contraseña en texto plano
        
        # Obtiene el código corto (ADM, CHOF, etc.)
        tipo_empleado_codigo = self.select_tipos.obtenerID()
        
        # 2. Validación básica
        if not nombre or not apellido_paterno or not correo or not contrasena_plana or not tipo_empleado_codigo:
            log("[NEW USER FORM]: Error de validación: Faltan campos obligatorios.")
            # NOTA: Aquí puedes añadir una notificación de error si lo deseas.
            return
            
        # 3. 🚨 HASHING DE CONTRASEÑA 🚨
        
        # Generar un salt aleatorio (16 bytes = 32 caracteres hexadecimales)
        salt = os.urandom(16).hex() 
        
        # Aplicar el hashing
        password_hash = self.generate_hash(contrasena_plana, salt) 
        
        # 4. Preparar el diccionario
        user_data = {
            "nombrePila": nombre,
            "apdPaterno": apellido_paterno,
            "apdMaterno": apellido_materno,
            "correo": correo, 
            "contrasena": password_hash, # ⬅️ AHORA ENVIAMOS EL HASH (salt:hash)
            "tipo_empleado": tipo_empleado_codigo
        }
        
        # 5. Emitir la señal
        self.registro_solicitado.emit(user_data)
        log("[NEW USER FORM]: Datos de registro emitidos correctamente (Contraseña hasheada).")

    def generate_hash(self, password, salt):
        """Hashea la contraseña con el salt usando SHA-256."""
        # 1. Concatenar la contraseña y el salt y codificar a bytes
        salted_password = (password + salt).encode('utf-8')
        
        # 2. Crear el hash SHA-256
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        
        # 3. Devolver el salt combinado con el hash para su almacenamiento (salt:hash)
        return f"{salt}:{hashed_password}" 

    # --- FUNCIONALIDAD CLAVE DE ENVÍO (submit_registration) ---
# ...