from db.connV import conn
from domain.vehiculos.ClaseVehiculo import Vehiculo



def listarVehiculos():
    miConn = conn()
    comando = "select id_vehiculo as ID, num_serie AS 'Num Serie', matricula as Matricula, marca as Marca, modelo as Modelo, color as Color , fecha_adquision as 'Fecha de adquision', tipo as 'Tipo de Vehiculo', tipo_licencia as 'Tipo Licencia', capacidad_pasajeros as 'Capcidad Pasajeros', utilidad as 'Utilidad del vehiculo', comentarios as Comentarios from vehiculos"
    lista = miConn.lista(comando)
    
    if not lista:
        print("No hay vehiculos registrados, para mostrar")
    else:
        if len(lista)>0:
            for fila in lista:
                print(fila)
                
def agregarVehiculo(nuevoVehiculo):
    objVehiculo=nuevoVehiculo
    miConn = conn()
    aux = "insert into vehiculos (num_serie, matricula, marca, modelo, color, fecha_adquision, tipo, tipo_licencia, capacidad_pasajeros, utilidad, comentarios) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, '{9}', '{10}')"
    comando = aux.format(objVehiculo.get_num_serie(), 
    objVehiculo.get_matricula(), objVehiculo.get_marca(), 
    objVehiculo.get_modelo(), objVehiculo.get_color(), 
    objVehiculo.get_fecha_adquision(), objVehiculo.get_tipo(), 
    objVehiculo.get_tipo_licencia(), objVehiculo.get_capacidad_pasajeros(), 
    objVehiculo.get_utilidad(), objVehiculo.get_comentarios())
    lastid = miConn.registrar(comando)
    return lastid

def borrarVehiculo(existeVehiculo):
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
        
        
def modificarVehiculo(existeVehiculo):
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