
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
    comando = aux.format(objSolicitud.get_num_serie(), 
    objSolicitud.get_matricula(), objSolicitud.get_marca(), 
    objSolicitud.get_modelo(), objSolicitud.get_color(), 
    objSolicitud.get_fecha_adquision(), objSolicitud.get_tipo(), 
    objSolicitud.get_tipo_licencia(), objSolicitud.get_capacidad_pasajeros(), 
    objSolicitud.get_utilidad(), objSolicitud.get_comentarios())
    lastid = miConn.registrar(comando)
    return lastid

def estadoSolicitud(existeVehiculo):
    objVehiculo=existeVehiculo
    miConn = conn()
    aux = "delete from vehiculos where id_vehiculo={0}"
    comando = aux.format(objVehiculo.get_id())
    contador = miConn.actualizar(comando)
    if existeVehiculo is False:
        print("El vehiculo no existe")
        
    if contador ==1:
        print("Vehiculo eliminado correctamente")
    elif contador ==0:
        print("Datos del vehiculo no encontrados")
    else:
        print("Error al eliminar el vehiculo")
        
        
def modificarSolicitud(existeVehiculo):
    objVehiculo = existeVehiculo
    miConn = conn()
    aux = "UPDATE vehiculos SET matricula = '{0}' WHERE id_vehiculo = {1}"
    comando = aux.format(objVehiculo.get_matricula(), int(objVehiculo.get_id()))
    contador = miConn.actualizar(comando)
    if existeVehiculo is False:
        print("El vehiculo no existe")
        
    if contador == 1:
        print("Vehículo modificado correctamente")
    elif contador == 0:
        print("Datos del vehículo no encontrados")
    else:
        print("Error al modificar el vehículo")