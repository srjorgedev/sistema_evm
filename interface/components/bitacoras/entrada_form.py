import sys
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QWidget, QSpacerItem,
    QScrollArea
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QResizeEvent, QColor, QPalette, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget

from interface.components.input import InputWidget
from interface.components.select import SelectWidget
from interface.components.data_fetch import TaskRunner
from interface.components.square_button import SquareButtonWidget
from interface.components.button import ButtonWidget

from interface.components.button import ColorKeys

import controllers.bitacora_controller as FBitacora
import controllers.observaciones_controller as FObservaciones

from utils.log import log

class EntradaFormWidget(QWidget):
    observaciones_widgets = []
    def __init__(self):
        super().__init__()
        
        self.tipos_obs = []
        self.runner = TaskRunner(self)
        
        self.main_layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea()
        self.content_widget = QWidget()
        self.layout_v = QVBoxLayout(self.content_widget)
        self.select_ = SelectWidget("La entrada pertenece a la bitacora *", "Seleccione una bitacora...")
        self.observaciones = QVBoxLayout()
        self.btn_add_obs = ButtonWidget("add", "Agregar Observación", ColorKeys.BASE)
        layout_h = QHBoxLayout()
        desc = QLabel("Completa los detalles del nuevo registro. \n* campo es obligatorio.")
        km_entrada = InputWidget("Kilometraje al entrar *", r"^[0-9]+.?[0-9]*$")
        gas_entrada = InputWidget("Litros de gasolina al entrar *", r"^[0-9]+.?[0-9]*$")
        v_spacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        observaciones_label = QLabel("Registrar observaciones (opcional)")
        crear_button = ButtonWidget("ok", "Continuar", ColorKeys.CREAR)
    
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
    
        layout_h.setSpacing(8)
        
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.layout_v.setContentsMargins(0, 0, 10, 24)
        self.layout_v.setSpacing(0) 
        self.main_layout.setSpacing(0)
        
        self.scroll_area.setStyleSheet("background-color: transparent;")
        self.content_widget.setStyleSheet("background-color: transparent;")
        desc.setStyleSheet("font-size: 16px; font-weight: normal; color: #c1c1c1;")
        observaciones_label.setStyleSheet("font-size: 16px; font-weight: normal; color: #f1f1f1;")
        
        self.select_.change.connect(lambda e: log(f"[ENTRADA FORM]: Bitacora -> {e}"))
        self.btn_add_obs.clicked.connect(self.agregar_observacion)
        
        self.observaciones.setSpacing(8)
        
        layout_h.addWidget(km_entrada)
        layout_h.addWidget(gas_entrada)
        
        self.layout_v.addWidget(desc)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addWidget(self.select_)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addLayout(layout_h)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addWidget(observaciones_label)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addWidget(self.btn_add_obs)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addLayout(self.observaciones)
        self.layout_v.addItem(v_spacer)
        self.layout_v.addWidget(crear_button)
        
        self.layout_v.addStretch()
        
        self.scroll_area.setWidget(self.content_widget)
        self.main_layout.addWidget(self.scroll_area)
        
        self.agregar_observacion()
        
        self.fetch_bitacoras_no_entrada()
        self.fetch_tipos_observaciones()
        
    def agregar_observacion(self):
        row_widget = QWidget()
        observaciones_layout = QHBoxLayout(row_widget)
        observaciones_input = InputWidget(f"Observacion #{len(self.observaciones_widgets) + 1}", r"^[a-zA-z\s,.]{0,50}$")
        nuevo_select = SelectWidget("Tipo de observacion", "Seleccione un tipo de observacion...")
        observaciones_close = SquareButtonWidget("close", "#ef4444", 36)
        
        observaciones_layout.setContentsMargins(0, 0, 0, 0)
        observaciones_layout.setSpacing(8)
        
        row_widget.setStyleSheet("background-color: transparent;")
        
        observaciones_close.clicked.connect(lambda: self.eliminar_observacion(row_widget))
        
        if self.tipos_obs:
            self.agregar_combo(self.tipos_obs, nuevo_select)

        row_widget.select_interno = nuevo_select
        
        observaciones_layout.addWidget(observaciones_input, 3)
        observaciones_layout.addWidget(nuevo_select, 2)        
        observaciones_layout.addWidget(observaciones_close, 0, Qt.AlignmentFlag.AlignBottom) 
        
        self.observaciones_widgets.append(row_widget)
        self.observaciones.addWidget(row_widget)
    
    def eliminar_observacion(self, widget_fila: QWidget):
        if widget_fila in self.observaciones_widgets:
            self.observaciones_widgets.remove(widget_fila)
        self.observaciones.removeWidget(widget_fila)
        widget_fila.deleteLater()
    
    def fetch_bitacoras_no_entrada(self):
        log("[ENTRADA FORM]: Obteniendo bitacoras sin entrada...")
        self.runner.run(
            func=FBitacora.lista_sin_entrada,
            on_error=lambda e: log("[ENTRADA FORM]: Ocurrio un error."),
            on_success=lambda e: self.agregar_bitacoras_sin_entrada(e)
        )
    def fetch_tipos_observaciones(self):
        log("[ENTRADA FORM]: Obteniendo tipos de observaciones...")
        self.runner.run(
            func=FObservaciones.lista_tipos,
            on_error=lambda e: log(f"[ENTRADA FORM]: Ocurrio un error -> {e}"),
            on_success=lambda e: self.agregar_tipos_observacion(e)
        )
    
    def agregar_bitacoras_sin_entrada(self, datos):
        items = []
        for tupla in datos:
            items.append((f"#{tupla[0]} - {tupla[1]}, {tupla[2]}", tupla[0]))
        
        self.agregar_combo(items, self.select_)

    def agregar_tipos_observacion(self, datos): 
        items = []
        for tupla in datos:
            items.append((f"{tupla[0]} - {tupla[1]}", tupla[0]))
        
        self.tipos_obs = items
        
        for row in self.observaciones_widgets:
            self.agregar_combo(items, row.select_interno)
        
    def agregar_combo(self, datos, combobox): 
        log("[ENTRADA FORM]: Agregando los datos al combobox...")
        
        combobox.addItems(datos)
        
        log("[ENTRADA FORM]: Datos agregados.")