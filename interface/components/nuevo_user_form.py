import sys
import hashlib
import os
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, QScrollArea, QSpacerItem, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.button import ButtonWidget
from interface.components.square_button import SquareButtonWidget

import controllers.bitacora_controller as FBitacora
import controllers.observaciones_controller as FObservaciones
import controllers.user_controller as FUser

from interface.components.styles.general import  COLORS, COLORS_LIST

from utils.log import log

class NewUserFormWidget(QWidget):
    registro_solicitado = pyqtSignal(dict) 
    
    def __init__(self):
        super().__init__()
        
        self.runner = TaskRunner(self)
        
        self.main_layout = QVBoxLayout(self)
        
        self.select_tipos = SelectWidget("Tipo de empleado *", "Seleccione un tipo...")
        self.nombre_input = InputWidget("Nombre(s) *")
        self.prim_apd = InputWidget("Primer apellido *")
        self.seg_apd = InputWidget("Segundo apellido")
        self.correo = InputWidget("Correo electronico *")
        self.contrasena = InputWidget("Contraseña *", None, True)
        self.crear_boton = ButtonWidget(None, "Registrar empleado", COLORS_LIST[COLORS.CREAR])
        
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
        
        self.crear_boton.clicked.connect(self.submit_registration)
        
        self.agregar_tipos_fijos()
        
    def agregar_tipos_fijos(self):
        log("[NEW USER FORM]: Cargando tipos de empleado fijos.")
        self.runner.run(
            func=FUser.lista_tipos,
            on_success= lambda a: self.handle_tipos(a),
            on_error=lambda e: log(f"[USUARIOS]: Error -> {e}")
            )
        
    def handle_tipos(self, data): 
        items = []
        for dato in data: 
            items.append((dato[0] + " - " + dato[1], dato[0]))
            
        self.select_tipos.addItems(items)

    def submit_registration(self):
        log("[NEW USER FORM]: Solicitud de registro iniciada.")
        
        nombre = self.nombre_input.get_text()
        apellido_paterno = self.prim_apd.get_text()
        apellido_materno = self.seg_apd.get_text()
        correo = self.correo.get_text()
        contrasena_plana = self.contrasena.get_text()
        
        tipo_empleado_codigo = self.select_tipos.obtenerID()
        
        if not nombre or not apellido_paterno or not correo or not contrasena_plana or not tipo_empleado_codigo:
            QMessageBox.warning(self, "Error", f"Debes llenar todos los campos")
            log("[NEW USER FORM]: Error de validación: Faltan campos obligatorios.")
            return
            
        salt = os.urandom(16).hex() 
        
        password_hash = self.generate_hash(contrasena_plana, salt) 
        
        user_data = {
            "nombrePila": nombre,
            "apdPaterno": apellido_paterno,
            "apdMaterno": apellido_materno,
            "email": correo, 
            "password_hash": password_hash,
            "tipo_empleado": tipo_empleado_codigo
        }
        
        print(user_data)
        self.registro_solicitado.emit(user_data)
        log("[NEW USER FORM]: Datos de registro emitidos correctamente (Contraseña hasheada).")

    def generate_hash(self, password, salt):
        salted_password = (password + salt).encode('utf-8')
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return f"{salt}:{hashed_password}" 