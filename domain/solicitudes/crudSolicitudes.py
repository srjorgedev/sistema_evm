from db.connV import conn
from db.ConnB import Conn

from utils.log import log

def listarSolicitudes():
    log("[CRUD SOLICITUDES]: Funcion -> Listar")
    miConn = Conn()
    # 0, 1, 5, 7, 9, 11
    comando = """
    SELECT 
        s.numero AS ID, 
        s.asunto AS Asunto, 
        s.horaSolicitada AS Hora, 
        s.fechaSolicitada AS Fecha,
        s.vehiculo AS Vehiculo, 
        ve.matricula,
        es.numero AS eso_solicitud_codigo,
        es.descripcion AS edo_solicitud,
        s.solicitante AS Solicitante, 
        eso.nombrePila,
        s.autorizador AS Autorizador,
        ea.nombrePila
        FROM solicitud AS s
        INNER JOIN edo_solicitud AS es ON s.edo_solicitud = es.numero
        INNER JOIN empleado AS eso ON s.solicitante = eso.numero
        INNER JOIN empleado AS ea ON s.autorizador = ea.numero
        INNER JOIN vehiculo AS ve ON s.vehiculo = ve.numSerie
        ORDER BY ID
    """
    log("[CRUD SOLICITUDES]: Obteniendo datos")
    lista = miConn.lista(comando)
    log("[CRUD SOLICITUDES]: Datos obtenidos")
    if not lista:
        log("[CRUD SOLICITUDES]: Error")
        return []
    else:
        if len(lista)>0:
            for fila in lista:
                datos = []
                for item in lista:
                    datos.append(item)

                return datos

def agregarSolicitud(nuevaSolicitud):
    objSolicitud=nuevaSolicitud
    miConn = conn()
    aux = "insert into solicitud (asunto, horaSolicitada, fechaSolicitada, vehiculo, edo_solicitud, solicitante, autorizador) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')"
    comando = aux.format(
    objSolicitud.get_asunto(),
    objSolicitud.get_horaSolicitud(),
    objSolicitud.get_fechaSolicitud(),
    objSolicitud.get_vehiculo(),
    objSolicitud.get_edoSolicitud(),
    objSolicitud.get_solicitante(),
    objSolicitud.get_autorizador())
    lastid = miConn.registrar(comando)
    return lastid

def estadoSolicitud(existeSolicitud):
    objSolicitud=existeSolicitud
    miConn = conn()
    aux = "UPDATE solicitud SET edo_solicitud = '{0}' WHERE numero = {1}"
    comando=aux.format(objSolicitud.get_edoSolicitud(),objSolicitud.get_numero() ) 
    contador=miConn.actualizar(comando)
    if existeSolicitud is False:
        print("La solicitud no existe")

    if contador == 1:
        print("Estado de la solicitud modificado correctamente")
    elif contador == 0:
        print("Datos de la solicitud no encontrados")
    else:
        print("Error al modificar estado de la solicitud")

        
def modificarSolicitud(solicitud):
    objSolicitud=solicitud 
    miConn = conn() 
    aux = " UPDATE solicitud SET asunto = '{0}'WHERE numero = {1}"
    comando=aux.format(solicitud.get_asunto(),solicitud.get_numero())
    contador = miConn.actualizar(comando)
    if solicitud is False:
        print("La solicitud no existe")
    if contador == 1:
        print("Solicitud modificada correctamente")
    elif contador == 0:
        print("Datos de la solicitud no encontrados")
    else:
        print("Error al modificar solicitud")
