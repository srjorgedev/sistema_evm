# crudMantenimiento.py
from db.conn import conn
from db.ConnB import Conn
from domain.mantenimiento.Mantenimiento import Mantenimiento

# ----- CREATE -----
def alta(objMantenimiento):
    miConn = conn()
    comando = """
        INSERT INTO mantenimiento 
        (Razon, Estatus, Importancia, FechaProgramada, Comentarios, TipoMantenimiento, Vehiculo, EstadoMantenimiento)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        objMantenimiento.get_razon(),
        objMantenimiento.get_estatus(),
        objMantenimiento.get_importancia(),
        objMantenimiento.get_fechaProgramada(),
        objMantenimiento.get_comentarios(),
        objMantenimiento.get_tipoMantenimiento(),
        objMantenimiento.get_vehiculo(),
        objMantenimiento.get_estadoMantenimiento()
    )
    try:
        cursor = miConn.conexion.cursor()
        cursor.execute(comando, valores)
        miConn.conexion.commit()
        print("Mantenimiento registrado correctamente.")
    except Exception as e:
        print("Error en el registro:")
        print(e)


# ----- READ -----
def lista():
    miConn = Conn()
    
    try:
        comando = "SELECT folio, razon, fechaProgramada, comentarios, tipo_mantenimiento, vehiculo, edo_mantenimiento FROM MANTENIMIENTO"
        listado = miConn.lista(comando)
        lista = []
        for fila in listado:
            m = Mantenimiento(
                fila[1],  # Razon
                0,  # Estatus
                0,  # Importancia
                str(fila[2]),  # FechaProgramada
                fila[3],  # Comentarios
                fila[4],  # TipoMantenimiento (ID)
                fila[5],  # Vehiculo
                fila[6],  # EstadoMantenimiento (ID)
                fila[0]   # Folio
            )
            lista.append(m)
        return lista
    except Exception as e:
        print("Error al listar:")
        print(e)
        return []


# ----- UPDATE -----
def actualizar(objMantenimiento):
    miConn = conn()
    comando = """
        UPDATE mantenimiento SET
        Estatus=%s,
        Importancia=%s,
        FechaProgramada=%s,
        Comentarios=%s,
        TipoMantenimiento=%s,
        EstadoMantenimiento=%s
        WHERE Folio=%s
    """
    valores = (
        objMantenimiento.get_estatus(),
        objMantenimiento.get_importancia(),
        objMantenimiento.get_fechaProgramada(),
        objMantenimiento.get_comentarios(),
        objMantenimiento.get_tipoMantenimiento(),
        objMantenimiento.get_estadoMantenimiento(),
        objMantenimiento.get_folio()
    )
    try:
        cursor = miConn.conexion.cursor()
        cursor.execute(comando, valores)
        miConn.conexion.commit()
        if cursor.rowcount == 1:
            print("Actualización de mantenimiento realizada.")
        else:
            print("Actualización no realizada o folio no encontrado.")
    except Exception as e:
        print("Error en conexión o actualización:")
        print(e)


# ----- DELETE -----
def borrar(objMantenimiento):
    miConn = conn()
    comando = "DELETE FROM mantenimiento WHERE Folio=%s"
    valores = (objMantenimiento.get_folio(),)
    try:
        cursor = miConn.conexion.cursor()
        cursor.execute(comando, valores)
        miConn.conexion.commit()
        if cursor.rowcount == 1:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("El folio del mantenimiento no existe.")
    except Exception as e:
        print("Error al eliminar mantenimiento:")
        print(e)


# ----- BUSCAR POR FOLIO -----
def buscar(objMantenimiento):
    miConn = conn()
    comando = "SELECT Folio, Razon, Estatus, Importancia, FechaProgramada, Comentarios, TipoMantenimiento, Vehiculo, EstadoMantenimiento FROM mantenimiento WHERE Folio=%s"
    valores = (objMantenimiento.get_folio(),)
    try:
        cursor = miConn.conexion.cursor()
        cursor.execute(comando, valores)
        fila = cursor.fetchone()
        if fila:
            m = Mantenimiento(
                fila[1],
                fila[2],
                fila[3],
                str(fila[4]),
                fila[5],
                fila[6],
                fila[7],
                fila[8],
                fila[0]
            )
            return m
        else:
            print("Folio de mantenimiento no encontrado.")
            return False
    except Exception as e:
        print("Error al buscar mantenimiento:")
        print(e)
        return False
