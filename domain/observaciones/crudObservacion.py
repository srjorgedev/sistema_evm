# crudObservacion.py
from db.conn import conn
from domain.observaciones.Observacion import Observacion

# CREATE
def alta(objObservacion):
    miConn = conn()
    aux = "INSERT INTO OBSERVACIONES(Descripcion, TipoObservacion, BitacoraAsociada) VALUES('{0}','{1}','{2}')"
    comando = aux.format(objObservacion.get_descripcion(), objObservacion.get_tipoObservacion(), objObservacion.get_bitacoraAsociada())
    miConn.registrar(comando)

# READ
def lista():
    miConn = conn()
    comando = "SELECT Numero, Descripcion, TipoObservacion, BitacoraAsociada FROM OBSERVACIONES"
    listado = miConn.lista(comando)
    
    if listado == 0:
        print("Error: No se puede mostrar el listado o la conexión falló.")
        return 0
    
    if len(listado) > 0:
        print("\n--- Listado de Observaciones ---")
        for fila in listado:
            objObservacion = Observacion(fila[1], fila[2], fila[3], fila[0])
            print(objObservacion)
        return True
    else:
        print("No hay observaciones registradas.")

# UPDATE
def actualizar(objObservacion):
    miConn = conn()
    aux = "UPDATE OBSERVACIONES SET Descripcion = '{0}', BitacoraAsociada = '{1}' WHERE Numero = {2}"
    comando = aux.format(objObservacion.get_descripcion(), objObservacion.get_bitacoraAsociada(), objObservacion.get_numero())
    contador = miConn.actualizar(comando)
    if contador == 1:
        print("Actualización de Observación realizada")
    else:
        print("Actualización no realizada o Folio no encontrado")

# DELETE
def borrar(objObservacion):
    miConn = conn()
    aux = "DELETE FROM OBSERVACIONES WHERE Numero = {0}"
    comando = aux.format(objObservacion.get_numero())
    contador = miConn.actualizar(comando)
    if contador == 1:
        print("Observación Eliminada correctamente.")
    elif contador == 0:
        print("El Folio de la observación no existe.")
    else:
        print("Eliminación no realizada por error de BD.")
        
def buscar(objObservacion):
    miConn = conn()
    comando = "SELECT Numero, Descripcion, TipoObservacion, BitacoraAsociada FROM OBSERVACIONES WHERE Numero = {0}"
    comando = comando.format(objObservacion.get_numero())
    listado = miConn.lista(comando)
    
    if listado != 0 and len(listado) == 1:
        fila = listado[0]
        objEncontrado = Observacion(fila[1], fila[2], fila[3], fila[0])
        print("Observación encontrada:")
        print(objEncontrado)
        return objEncontrado
    else:
        print("Folio de Observación no encontrado.")
        return False