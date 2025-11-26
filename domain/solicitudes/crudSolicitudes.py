from db.connV import conn
from db.ConnB import Conn
from utils.log import log


def listarSolicitudes():
    log("[CRUD SOLICITUDES]: Función -> Listar")
    miConn = Conn()

    comando = """
    SELECT 
        s.numero AS ID, 
        s.asunto AS Asunto, 
        s.horaSolicitada AS Hora, 
        s.fechaSolicitada AS Fecha,
        s.vehiculo AS Vehiculo, 
        ve.matricula,
        es.numero AS edo_solicitud_codigo,
        es.descripcion AS edo_solicitud,
        s.solicitante AS Solicitante, 
        eso.nombrePila AS nombre_solicitante,
        s.autorizador AS Autorizador,
        ea.nombrePila AS nombre_autorizador
    FROM solicitud AS s
    INNER JOIN edo_solicitud AS es ON s.edo_solicitud = es.numero
    INNER JOIN empleado AS eso ON s.solicitante = eso.numero
    INNER JOIN empleado AS ea ON s.autorizador = ea.numero
    INNER JOIN vehiculo AS ve ON s.vehiculo = ve.numSerie
    ORDER BY ID;
    """

    log("[CRUD SOLICITUDES]: Obteniendo datos...")
    lista = miConn.lista(comando)
    log("[CRUD SOLICITUDES]: Datos obtenidos.")

    if not lista:
        log("[CRUD SOLICITUDES]: No hay solicitudes.")
        return []

    return lista

def agregarSolicitud(nuevaSolicitud):
    obj = nuevaSolicitud
    miConn = conn()

    comando = f"""
    INSERT INTO solicitud 
    (asunto, fechaSolicitada, horaSolicitada, vehiculo, solicitante)
    VALUES (
        '{obj.get_asunto()}',
        '{obj.get_fechaSolicitud()}',
        '{obj.get_horaSolicitud()}',
        '{obj.get_vehiculo()}',
        '{obj.get_solicitante()}',
    )
    """

    lastid = miConn.registrar(comando)
    log(f"[CRUD SOLICITUDES]: Solicitud agregada ID -> {lastid}")

    return lastid

def estadoSolicitud(existeSolicitud):
    obj = existeSolicitud
    miConn = conn()

    comando = f"""
    UPDATE solicitud 
    SET edo_solicitud = '{obj.get_edoSolicitud()}'
    WHERE numero = {obj.get_numero()};
    """

    contador = miConn.actualizar(comando)

    if contador == 1:
        log("[CRUD SOLICITUDES]: Estado actualizado correctamente.")
    elif contador == 0:
        log("[CRUD SOLICITUDES]: Solicitud no encontrada.")
    else:
        log("[CRUD SOLICITUDES]: Error modificando estado.")


def actualizar_matricula(id_vehiculo, nueva_matricula):
    print(f"[CRUD] Actualizando id={id_vehiculo} con matrícula={nueva_matricula}")
    #db.execute("UPDATE vehiculos SET matricula=? WHERE id=?", (nueva_matricula, id_vehiculo))
        
def eliminarSolicitud(numero):
    comando = f"DELETE FROM solicitud WHERE numero = {numero};"
    from db.connV import conn
    miConn = conn()
    miConn.actualizar(comando)

