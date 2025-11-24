
from db.connV import conn
from domain.solicitudes.ClaseSolicitudes import Vehiculo as SolicitudVehiculo

def listarSolicitudes():
    miConn = conn()
    comando = "select numero as ID, asunto as Asunto, horaSolicitada as Hora, fechaSolicitada as Fecha, vehicul as Vehiculo, edo_solicitud as Estado_Solicitud , solicitante as Solicitante, autorizador as Autorizador, from solicitud"
    lista = miConn.lista(comando)
    
    if not lista:
        print("No hay solicitudes registradas, para mostrar")
    else:
        if len(lista)>0:
            for fila in lista:
                print(fila)
                
def agregarSolicitud(nuevaSolicitud):
    objSolicitud=nuevaSolicitud
    miConn = conn()
    aux = "insert into solicitud (asunto, horaSolicitada, fechaSolicitada, vehiculo, edo_solicitud, solicitante, autorizador) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, '{9}', '{10}')"
    comando = aux.format(objSolicitud.get_numero(), 
    objSolicitud.get_asunto(), objSolicitud.get_horaSolicitud(), 
    objSolicitud.get_fechaSolicitud(), objSolicitud.get_vehiculo(), 
    objSolicitud.get_edoSolicitud(), objSolicitud.get_solicitante(), 
    objSolicitud.get_autorizador())
    lastid = miConn.registrar(comando)
    return lastid

def estadoSolicitud(existeSolicitud):
    objSolicitud=existeSolicitud
    miConn = conn()
    aux = "update from solicitud where edo_solicitud='En Proceso'"
    comando = aux.format(objSolicitud.get_edoSolicitud())
    contador = miConn.actualizar(comando)
    if existeSolicitud is False:
        print("La solicitud no existe")
        
    if contador ==1:
        print("Estado de la solicitud modificado correctamente correctamente")
    elif contador ==0:
        print("Datos de la solicitud no encontrados")
    else:
        print("Error al cambiar el estado de la solicitud")
        
        
def modificarSolicitud(existeSolicitud):
    objSolicitud = existeSolicitud
    miConn = conn()
    aux = "UPDATE vehiculos SET matricula = '{0}' WHERE id_vehiculo = {1}"
    comando = aux.format(objSolicitud.get_matricula(), int(objSolicitud.get_id()))
    contador = miConn.actualizar(comando)
    if existeSolicitud is False:
        print("La solicitud no existe")
        
    if contador == 1:
        print("Vehículo modificado correctamente")
    elif contador == 0:
        print("Datos del vehículo no encontrados")
    else:
        print("Error al modificar el vehículo")