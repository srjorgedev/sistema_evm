from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QComboBox, QMessageBox, QDialog,
    QTabWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
import mysql.connector

# ----------------------------- CONEXIÓN -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="evm_db"
    )

# ----------------------------- ESTILOS -----------------------------
APP_BG = "#2E2E2E"
TABLE_HEADER_BG = "#1F4E78"
TABLE_HEADER_FG = "#FFFFFF"
BTN_BG = "#1F78C1"
BTN_FG = "#FFFFFF"
BTN_HOVER = "#145A86"
DIALOG_BG = "#3A3A3A"
LINEEDIT_BG = "#4A4A4A"
LINEEDIT_FG = "#FFFFFF"

def set_widget_style(widget):
    palette = widget.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(APP_BG))
    widget.setPalette(palette)
    widget.setStyleSheet(f"background-color: {APP_BG}; color: {LINEEDIT_FG};")

def style_table(table):
    table.setStyleSheet(f"""
        QHeaderView::section {{
            background-color: {TABLE_HEADER_BG};
            color: {TABLE_HEADER_FG};
            font-weight: bold;
        }}
        QTableWidget {{
            background-color: {APP_BG};
            color: {LINEEDIT_FG};
            gridline-color: #555555;
        }}
        QTableWidget::item:selected {{
            background-color: {BTN_HOVER};
        }}
    """)
    table.setAlternatingRowColors(True)

def style_button(btn):
    btn.setStyleSheet(f"""
        QPushButton {{
            background-color: {BTN_BG};
            color: {BTN_FG};
            border-radius: 5px;
            padding: 5px 10px;
        }}
        QPushButton:hover {{
            background-color: {BTN_HOVER};
        }}
    """)

def style_lineedit(le):
    le.setStyleSheet(f"background-color: {LINEEDIT_BG}; color: {LINEEDIT_FG}; padding: 3px; border-radius: 3px;")

def style_combobox(cb):
    cb.setStyleSheet(f"background-color: {LINEEDIT_BG}; color: {LINEEDIT_FG}; padding: 3px; border-radius: 3px;")

def style_dialog(dialog):
    dialog.setStyleSheet(f"background-color: {DIALOG_BG}; color: {LINEEDIT_FG}; border-radius: 5px;")

# ----------------------------- CRUD MANTENIMIENTO + CONSULTAS -----------------------------
class MantenimientoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mantenimientos")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        set_widget_style(self)

        # ---------------- Botones CRUD fijos arriba ----------------
        self.btn_layout = QHBoxLayout()
        for text, slot in [
            ("Agregar", self.add_mantenimiento),
            ("Editar", self.edit_mantenimiento),
            ("Eliminar", self.delete_mantenimiento),
            ("Actualizar", self.load_data)
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            style_button(btn)
            self.btn_layout.addWidget(btn)
        self.main_layout.addLayout(self.btn_layout)

        # ---------------- Tab Widget para CRUD y Consultas ----------------
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # ---------------- Pestaña CRUD ----------------
        self.crud_tab = QWidget()
        self.crud_layout = QVBoxLayout()
        self.crud_tab.setLayout(self.crud_layout)

        # Tabla CRUD
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Folio", "Razón", "Estatus", "Importancia",
            "Fecha Programada", "Tipo", "Vehículo", "Estado"
        ])
        style_table(self.table)
        self.crud_layout.addWidget(self.table)

        self.tabs.addTab(self.crud_tab, "Listado General")

        # ---------------- Pestañas de Consultas ----------------
        self.consulta1_tab = QWidget()
        self.consulta1_layout = QVBoxLayout()
        self.consulta1_tab.setLayout(self.consulta1_layout)
        self.consulta1_table = QTableWidget()
        style_table(self.consulta1_table)
        self.consulta1_layout.addWidget(self.consulta1_table)
        self.tabs.addTab(self.consulta1_tab, "Reporte de mantenimiento UN vehículo")

        self.consulta2_tab = QWidget()
        self.consulta2_layout = QVBoxLayout()
        self.consulta2_tab.setLayout(self.consulta2_layout)
        self.consulta2_table = QTableWidget()
        style_table(self.consulta2_table)
        self.consulta2_layout.addWidget(self.consulta2_table)
        self.tabs.addTab(self.consulta2_tab, "Estados de vehículos en mantenimiento")

        self.consulta3_tab = QWidget()
        self.consulta3_layout = QVBoxLayout()
        self.consulta3_tab.setLayout(self.consulta3_layout)
        self.consulta3_table = QTableWidget()
        style_table(self.consulta3_table)
        self.consulta3_layout.addWidget(self.consulta3_table)
        self.tabs.addTab(self.consulta3_tab, "Mantenimientos por vehículo")

        # Cargar datos iniciales
        self.load_data()
        self.load_consultas()

    # ---------------------- CRUD Funciones ----------------------
    def load_data(self):
        self.table.setRowCount(0)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.folio, m.razon, m.estatus, m.importancia, m.fechaProgramada,
                   t.comentario, m.vehiculo, e.descripcion
            FROM mantenimiento m
            JOIN tipoMantenimiento t ON m.tipoMantenimiento = t.numero
            JOIN estadoMantenimiento e ON m.estadoMantenimiento = e.numero
            ORDER BY m.folio
        """)
        for row_idx, row_data in enumerate(cursor.fetchall()):
            self.table.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        cursor.close()
        conn.close()

    def add_mantenimiento(self):
        dialog = MantenimientoDialog()
        if dialog.exec():
            self.load_data()
            self.load_consultas()

    def edit_mantenimiento(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione un mantenimiento")
            return
        folio = int(self.table.item(selected, 0).text())
        dialog = MantenimientoDialog(folio)
        if dialog.exec():
            self.load_data()
            self.load_consultas()

    def delete_mantenimiento(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione un mantenimiento")
            return
        folio = int(self.table.item(selected, 0).text())
        confirm = QMessageBox.question(self, "Confirmar", f"Eliminar mantenimiento {folio}?")
        if confirm == QMessageBox.StandardButton.Yes:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mantenimiento WHERE folio=%s", (folio,))
            conn.commit()
            cursor.close()
            conn.close()
            self.load_data()
            self.load_consultas()

    # ---------------------- Consultas ----------------------
    def load_consultas(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Consulta 1: Reporte de mantenimiento UN vehículo
        cursor.execute("""
            SELECT v.numSerie, ma.nombre, mo.nombre, m.fechaProgramada, m.razon,
                   m.comentarios, t.comentario, tobs.descripcion, e.descripcion
            FROM mantenimiento m
            JOIN vehiculo v ON m.vehiculo = v.numSerie
            JOIN marca ma ON v.marca = ma.codigo
            JOIN modelo mo ON v.modelo = mo.codigo
            JOIN tipoMantenimiento t ON m.tipoMantenimiento = t.numero
            LEFT JOIN observacion tobs ON tobs.bitacora = m.folio
            JOIN estadoMantenimiento e ON m.estadoMantenimiento = e.numero
            ORDER BY v.numSerie
        """)
        rows = cursor.fetchall()
        self.consulta1_table.setRowCount(len(rows))
        self.consulta1_table.setColumnCount(9)
        self.consulta1_table.setHorizontalHeaderLabels([
            "Matrícula", "Marca", "Modelo", "Fecha", "Razón",
            "Comentarios", "Tipo Mantenimiento", "Tipo Observación", "Estado Mantenimiento"
        ])
        for r_idx, row in enumerate(rows):
            for c_idx, val in enumerate(row):
                self.consulta1_table.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))

        # Consulta 2: Estados de los vehículos en mantenimiento
        cursor.execute("""
            SELECT m.folio, v.numSerie, ma.nombre, mo.nombre, m.fechaProgramada,
                   m.razon, t.comentario, e.descripcion
            FROM mantenimiento m
            JOIN vehiculo v ON m.vehiculo = v.numSerie
            JOIN marca ma ON v.marca = ma.codigo
            JOIN modelo mo ON v.modelo = mo.codigo
            JOIN tipoMantenimiento t ON m.tipoMantenimiento = t.numero
            JOIN estadoMantenimiento e ON m.estadoMantenimiento = e.numero
            ORDER BY m.folio
        """)
        rows2 = cursor.fetchall()
        self.consulta2_table.setRowCount(len(rows2))
        self.consulta2_table.setColumnCount(8)
        self.consulta2_table.setHorizontalHeaderLabels([
            "Folio", "Matrícula", "Marca", "Modelo", "Fecha",
            "Razón", "Tipo Mantenimiento", "Estado Mantenimiento"
        ])
        for r_idx, row in enumerate(rows2):
            for c_idx, val in enumerate(row):
                self.consulta2_table.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))

        # Consulta 3: Mantenimientos por vehículo
        cursor.execute("""
            SELECT v.numSerie, ma.nombre, mo.nombre, m.folio, m.fechaProgramada,
                   m.razon, t.comentario, tobs.descripcion
            FROM mantenimiento m
            JOIN vehiculo v ON m.vehiculo = v.numSerie
            JOIN marca ma ON v.marca = ma.codigo
            JOIN modelo mo ON v.modelo = mo.codigo
            JOIN tipoMantenimiento t ON m.tipoMantenimiento = t.numero
            LEFT JOIN observacion tobs ON tobs.bitacora = m.folio
            ORDER BY v.numSerie, m.folio
        """)
        rows3 = cursor.fetchall()
        self.consulta3_table.setRowCount(len(rows3))
        self.consulta3_table.setColumnCount(8)
        self.consulta3_table.setHorizontalHeaderLabels([
            "Matrícula", "Marca", "Modelo", "Folio", "Fecha",
            "Razón", "Tipo Mantenimiento", "Tipo Observación"
        ])
        for r_idx, row in enumerate(rows3):
            for c_idx, val in enumerate(row):
                self.consulta3_table.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))

        cursor.close()
        conn.close()

# ----------------------------- DIALOGO MANTENIMIENTO (CRUD) -----------------------------
class MantenimientoDialog(QDialog):
    def __init__(self, folio=None):
        super().__init__()
        self.setWindowTitle("Mantenimiento")
        self.folio = folio
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        style_dialog(self)

        # Campos
        self.razon = QLineEdit(); style_lineedit(self.razon)
        self.estatus = QLineEdit(); style_lineedit(self.estatus)
        self.importancia = QLineEdit(); style_lineedit(self.importancia)
        self.fecha = QLineEdit(); style_lineedit(self.fecha)
        self.tipo = QComboBox(); style_combobox(self.tipo)
        self.vehiculo = QComboBox(); style_combobox(self.vehiculo)
        self.estado = QComboBox(); style_combobox(self.estado)

        for label, widget in [
            ("Razón", self.razon),
            ("Estatus", self.estatus),
            ("Importancia", self.importancia),
            ("Fecha Programada (YYYY-MM-DD)", self.fecha),
            ("Tipo Mantenimiento", self.tipo),
            ("Vehículo", self.vehiculo),
            ("Estado Mantenimiento", self.estado)
        ]:
            self.layout.addWidget(QLabel(label))
            self.layout.addWidget(widget)

        self.btn_save = QPushButton("Guardar"); style_button(self.btn_save)
        self.btn_save.clicked.connect(self.save)
        self.layout.addWidget(self.btn_save)

        self.load_combos()
        if folio:
            self.load_data()

    def load_combos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT numero, comentario FROM tipoMantenimiento")
        self.tipo.addItems([f"{num} - {desc}" for num, desc in cursor.fetchall()])
        cursor.execute("SELECT numSerie FROM vehiculo")
        self.vehiculo.addItems([v[0] for v in cursor.fetchall()])
        cursor.execute("SELECT numero, descripcion FROM estadoMantenimiento")
        self.estado.addItems([f"{num} - {desc}" for num, desc in cursor.fetchall()])
        cursor.close()
        conn.close()

    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT razon, estatus, importancia, fechaProgramada, tipoMantenimiento, vehiculo, estadoMantenimiento FROM mantenimiento WHERE folio=%s", (self.folio,))
        row = cursor.fetchone()
        if row:
            self.razon.setText(row[0])
            self.estatus.setText(row[1])
            self.importancia.setText(row[2])
            self.fecha.setText(str(row[3]))
            self.tipo.setCurrentIndex(row[4]-1)
            self.vehiculo.setCurrentText(row[5])
            self.estado.setCurrentIndex(row[6]-1)
        cursor.close()
        conn.close()

    def save(self):
        tipo_id = int(self.tipo.currentText().split(" - ")[0])
        estado_id = int(self.estado.currentText().split(" - ")[0])
        conn = get_connection()
        cursor = conn.cursor()
        if self.folio:
            cursor.execute("""
                UPDATE mantenimiento SET razon=%s, estatus=%s, importancia=%s, fechaProgramada=%s,
                tipoMantenimiento=%s, vehiculo=%s, estadoMantenimiento=%s WHERE folio=%s
            """, (self.razon.text(), self.estatus.text(), self.importancia.text(), self.fecha.text(),
                  tipo_id, self.vehiculo.currentText(), estado_id, self.folio))
        else:
            cursor.execute("""
                INSERT INTO mantenimiento (razon, estatus, importancia, fechaProgramada, tipoMantenimiento, vehiculo, estadoMantenimiento)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (self.razon.text(), self.estatus.text(), self.importancia.text(), self.fecha.text(),
                  tipo_id, self.vehiculo.currentText(), estado_id))
        conn.commit()
        cursor.close()
        conn.close()
        self.accept()


# ----------------------------- CRUD OBSERVACIONES + CONSULTA -----------------------------
class ObservacionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Observaciones")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        set_widget_style(self)

        # ---------------- Botones CRUD fijos arriba ----------------
        self.btn_layout = QHBoxLayout()
        for text, slot in [
            ("Agregar", self.add_observacion),
            ("Editar", self.edit_observacion),
            ("Eliminar", self.delete_observacion),
            ("Actualizar", self.load_data)
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            style_button(btn)
            self.btn_layout.addWidget(btn)
        self.main_layout.addLayout(self.btn_layout)

        # ---------------- Tab Widget para CRUD y Consulta ----------------
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # Pestaña CRUD
        self.crud_tab = QWidget()
        self.crud_layout = QVBoxLayout()
        self.crud_tab.setLayout(self.crud_layout)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Número", "Descripción", "Tipo", "Bitácora"])
        style_table(self.table)
        self.crud_layout.addWidget(self.table)
        self.tabs.addTab(self.crud_tab, "Listado General")

        # Pestaña Consulta Observaciones por Bitácora
        self.consulta_tab = QWidget()
        self.consulta_layout = QVBoxLayout()
        self.consulta_tab.setLayout(self.consulta_layout)
        self.consulta_table = QTableWidget()
        style_table(self.consulta_table)
        self.consulta_layout.addWidget(self.consulta_table)
        self.tabs.addTab(self.consulta_tab, "Observaciones por Bitácora")

        self.load_data()
        self.load_consulta()

    # ---------------------- CRUD Funciones ----------------------
    def load_data(self):
        self.table.setRowCount(0)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.numero, o.descripcion, t.descripcion, b.vehiculo
            FROM observacion o
            JOIN tipoObservacion t ON o.tipoObservacion = t.numero
            JOIN bitacora b ON o.bitacora = b.numero
            ORDER BY o.numero
        """)
        for row_idx, row_data in enumerate(cursor.fetchall()):
            self.table.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        cursor.close()
        conn.close()

    def add_observacion(self):
        dialog = ObservacionDialog()
        if dialog.exec():
            self.load_data()
            self.load_consulta()

    def edit_observacion(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione una observación")
            return
        numero = int(self.table.item(selected, 0).text())
        dialog = ObservacionDialog(numero)
        if dialog.exec():
            self.load_data()
            self.load_consulta()

    def delete_observacion(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione una observación")
            return
        numero = int(self.table.item(selected, 0).text())
        confirm = QMessageBox.question(self, "Confirmar", f"Eliminar observación {numero}?")
        if confirm == QMessageBox.StandardButton.Yes:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM observacion WHERE numero=%s", (numero,))
            conn.commit()
            cursor.close()
            conn.close()
            self.load_data()
            self.load_consulta()

    # ---------------------- Consulta Observaciones por Bitácora ----------------------
    def load_consulta(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.numero, o.numero, o.descripcion
            FROM observacion o
            JOIN bitacora b ON o.bitacora = b.numero
            ORDER BY b.numero, o.numero
        """)
        rows = cursor.fetchall()
        self.consulta_table.setRowCount(len(rows))
        self.consulta_table.setColumnCount(3)
        self.consulta_table.setHorizontalHeaderLabels(["Número Bitácora", "Número Observación", "Descripción"])
        for r_idx, row in enumerate(rows):
            for c_idx, val in enumerate(row):
                self.consulta_table.setItem(r_idx, c_idx, QTableWidgetItem(str(val)))
        cursor.close()
        conn.close()


# ----------------------------- DIALOGO OBSERVACION (CRUD) -----------------------------
class ObservacionDialog(QDialog):
    def __init__(self, numero=None):
        super().__init__()
        self.setWindowTitle("Observación")
        self.numero = numero
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        style_dialog(self)

        self.descripcion = QLineEdit(); style_lineedit(self.descripcion)
        self.tipo = QComboBox(); style_combobox(self.tipo)
        self.bitacora = QComboBox(); style_combobox(self.bitacora)

        for label, widget in [
            ("Descripción", self.descripcion),
            ("Tipo Observación", self.tipo),
            ("Bitácora", self.bitacora)
        ]:
            self.layout.addWidget(QLabel(label))
            self.layout.addWidget(widget)

        self.btn_save = QPushButton("Guardar"); style_button(self.btn_save)
        self.btn_save.clicked.connect(self.save)
        self.layout.addWidget(self.btn_save)

        self.load_combos()
        if numero:
            self.load_data()

    def load_combos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT numero, descripcion FROM tipoObservacion")
        self.tipo.addItems([f"{num} - {desc}" for num, desc in cursor.fetchall()])
        cursor.execute("SELECT numero, vehiculo FROM bitacora")
        self.bitacora.addItems([f"{num} - {veh}" for num, veh in cursor.fetchall()])
        cursor.close()
        conn.close()

    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT descripcion, tipoObservacion, bitacora FROM observacion WHERE numero=%s", (self.numero,))
        row = cursor.fetchone()
        if row:
            self.descripcion.setText(row[0])
            tipo_id = int(row[1])
            bit_id = int(row[2])
            for i in range(self.tipo.count()):
                if int(self.tipo.itemText(i).split(" - ")[0]) == tipo_id:
                    self.tipo.setCurrentIndex(i)
                    break
            for i in range(self.bitacora.count()):
                if int(self.bitacora.itemText(i).split(" - ")[0]) == bit_id:
                    self.bitacora.setCurrentIndex(i)
                    break
        cursor.close()
        conn.close()

    def save(self):
        tipo_id = int(self.tipo.currentText().split(" - ")[0])
        bit_id = int(self.bitacora.currentText().split(" - ")[0])
        conn = get_connection()
        cursor = conn.cursor()
        if self.numero:
            cursor.execute("UPDATE observacion SET descripcion=%s, tipoObservacion=%s, bitacora=%s WHERE numero=%s",
                           (self.descripcion.text(), tipo_id, bit_id, self.numero))
        else:
            cursor.execute("INSERT INTO observacion (descripcion, tipoObservacion, bitacora) VALUES (%s,%s,%s)",
                           (self.descripcion.text(), tipo_id, bit_id))
        conn.commit()
        cursor.close()
        conn.close()
        self.accept()
