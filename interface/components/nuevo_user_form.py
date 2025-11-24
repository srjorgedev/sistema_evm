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

from utils.log import log

class NewUserFormWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.runner = TaskRunner(self)
        
        