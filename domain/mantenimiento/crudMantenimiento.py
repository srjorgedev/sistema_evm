# crudMantenimiento.py
from db.conn import conn
from db.ConnB import Conn
from domain.mantenimiento.Mantenimiento import Mantenimiento

# CREATE
def alta(objMantenimiento):
    miConn = conn()
    cols = "Razon, Estatus, Importancia, FechaProgramada, Comentarios, TipoMantenimiento, Vehiculo, EstadoMantenimiento"
    
    aux = f"INSERT INTO MANTENIMIENTO ({cols}) VALUES('{objMantenimiento.get_razon()}', '{objMantenimiento.get_estatus()}', '{objMantenimiento.get_importancia()}', '{objMantenimiento.get_fechaProgramada()}', '{objMantenimiento.get_comentarios()}', '{objMantenimiento.get_tipoMantenimiento()}', '{objMantenimiento.get_vehiculo()}', '{objMantenimiento.get_estadoMantenimiento()}')"
    
    miConn.registrar(aux)

# READ
def lista():
    miConn = Conn()
    comando = """
        SELECT folio, razon, fechaProgramada, comentarios, tipo_mantenimiento, vehiculo, edo_mantenimiento
        FROM mantenimiento
    """
    
    listado = miConn.lista(comando)

    # Si la conexión falló o no hay datos, regresar lista vacía para evitar errores en PyQt
    if not listado:
        print("No hay mantenimientos registrados o la consulta falló.")
        return []

    objs = []

    for fila in listado:
        obj = Mantenimiento(
            razon=fila[1],
            fechaProgramada=str(fila[2]),
            comentarios=fila[3],
            tipoMantenimiento=fila[4],
            vehiculo=fila[5],
            edoMantenimiento=fila[6],
            folio=fila[0]
        )
        objs.append(obj)

    return objs

        
# UPDATE
def actualizar(objMantenimiento):
    miConn = conn()
    aux = "UPDATE MANTENIMIENTO SET Estatus = '{0}', Importancia = '{1}', FechaProgramada = '{2}', Comentarios = '{3}', EstadoMantenimiento = '{4}' WHERE Folio = {5}"
    comando = aux.format(objMantenimiento.get_estatus(), objMantenimiento.get_importancia(), objMantenimiento.get_fechaProgramada(), objMantenimiento.get_comentarios(), objMantenimiento.get_estadoMantenimiento(), objMantenimiento.get_folio())
    contador = miConn.actualizar(comando)
    if contador == 1:
        print("Actualización de Mantenimiento realizada")
    else:
        print("Actualización no realizada o Folio no encontrado")

# DELETE
def borrar(objMantenimiento):
    miConn = conn()
    aux = "DELETE FROM MANTENIMIENTO WHERE Folio = {0}"
    comando = aux.format(objMantenimiento.get_folio())
    contador = miConn.actualizar(comando)
    if contador == 1:
        print("Mantenimiento Eliminado correctamente.")
    elif contador == 0:
        print("El Folio del mantenimiento no existe.")
    else:
        print("Eliminación no realizada por error de BD.")
        
def buscar(objMantenimiento):
    miConn = conn()
    comando = "SELECT Folio, Razon, Estatus, Importancia, FechaProgramada, Comentarios, TipoMantenimiento, Vehiculo, EstadoMantenimiento FROM MANTENIMIENTO WHERE Folio = {0}"
    comando = comando.format(objMantenimiento.get_folio())
    listado = miConn.lista(comando)
    
    if listado != 0 and len(listado) == 1:
        fila = listado[0]
        objEncontrado = Mantenimiento(fila[1], fila[2], fila[3], str(fila[4]), fila[5], fila[6], fila[7], fila[8], fila[0])
        print("Mantenimiento encontrado:")
        print(objEncontrado)
        return objEncontrado
    else:
        print("Folio de Mantenimiento no encontrado.")
        return False