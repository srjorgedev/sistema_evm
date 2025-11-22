from PyQt6.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
    def __init__(self, titulos, datos):
        super().__init__()
        self._datos = datos
        # Nombres de las columnas
        self._headers = titulos

    # Nos dice cuantas filas hay
    def rowCount(self, parent=None):
        return len(self._datos)

    # Nos dice cuantas columnas hay
    def columnCount(self, parent=None):
        return len(self._headers)

    # Lo que debe mostrar en cada celda
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            fila = index.row()
            columna = index.column()
            return self._datos[fila][columna]
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return None