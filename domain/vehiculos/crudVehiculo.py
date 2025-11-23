from db.connV import conn
from db.ConnB import Conn
from domain.vehiculos.ClaseVehiculo import Vehiculo

def listarVehiculos():
    miConn = Conn()
    comando = "select * from vehiculo"
    lista = miConn.lista(comando)
    
    if not lista:
        print("No hay vehiculos registrados, para mostrar")
    else:
        if len(lista)>0:
            return lista
                
def listaCorta():
    miConn = conn()
    comando = """
    SELECT 
        v.numSerie, 
        ma.nombre as marca,
        mo.nombre as modelo,
        v.disponibilidad 
    FROM vehiculo AS v
    INNER JOIN marca AS ma ON v.marca = ma.codigo
    INNER JOIN modelo AS mo ON v.modelo = mo.codigo
    WHERE v.disponibilidad = TRUE  
    """
    
    lista = miConn.lista(comando)
    vehiculos: list[Vehiculo] = []
    if not lista:
        print("No hay vehiculos registrados, para mostrar")
    else:
        if len(lista)>0:
            for fila in lista:
                vehiculos.append(Vehiculo(0, fila[0], 0, fila[1], fila[2], 0, 0, 0, 0, 0, 0, 0))
    
    return lista
                
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