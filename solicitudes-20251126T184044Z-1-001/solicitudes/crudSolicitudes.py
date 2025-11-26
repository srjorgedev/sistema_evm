from BD.conn import conn

def listarSolicitudes():
    miConn = conn()
    comando = "SELECT numero AS ID, asunto AS Asunto, horaSolicitada AS Hora, fechaSolicitada AS Fecha, vehiculo AS Vehiculo, edo_solicitud AS Estado_Solicitud, solicitante AS Solicitante, autorizador AS Autorizador FROM solicitud"
    
    lista = miConn.lista(comando)
    
    if not lista:
        print("No hay solicitudes registradas para mostrar")
    else:
        if len(lista)>0:
            for fila in lista:
                print(fila)
                
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
