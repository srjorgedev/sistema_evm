import sys
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
    def __init__(self):
        super().__init__()
        
        self.runner = TaskRunner(self)
        
        self.main_layout = QVBoxLayout(self)
        self.select_tipos = SelectWidget("Tipo de empleado *", "Seleccione un tipo...")
        nombre_input = InputWidget("Nombre(s) *")
        prim_apd = InputWidget("Primer apellido *")
        seg_apd = InputWidget("Segundo apellido")
        correo = InputWidget("Correo electronico *")
        contraseña = InputWidget("Contraseña *", None, True)
        crear_boton = ButtonWidget(None, "Registrar empleado", ColorKeys.CREAR)
        
        layout_apd = QHBoxLayout()
        layout_cred = QHBoxLayout()
        
        layout_apd.addWidget(prim_apd)
        layout_apd.addWidget(seg_apd)
        
        layout_cred.addWidget(correo)
        layout_cred.addWidget(contraseña)
        
        self.main_layout.addWidget(nombre_input)
        self.main_layout.addLayout(layout_apd)
        self.main_layout.addLayout(layout_cred)
        self.main_layout.addWidget(self.select_tipos)
        self.main_layout.addStretch()
        self.main_layout.addWidget(crear_boton)
        self.main_layout.addStretch()
        
        self.fetch_tipos_empleado()
        
    def fetch_tipos_empleado(self):
        self.runner.run(
            func=FUser.lista_tipos,
            on_success= lambda a: self.agregar_tipos(a),
            on_error=lambda e: log(f"[NEW USER FORM]: Error -> {e}")
            )
        
    def agregar_tipos(self, datos):
        items = []
        for tupla in datos:
            items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))
            
        self.agregar_combo(items, self.select_tipos)
            
    def agregar_combo(self, datos, combobox): 
        log("[NEW USER FORM]: Agregando los datos al combobox...")
        
        combobox.addItems(datos)
        
        log("[NEW USER FORM]: Datos agregados.")