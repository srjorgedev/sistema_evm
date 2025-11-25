from db.connV import conn
from db.ConnB import Conn
from domain.vehiculos.ClaseVehiculo import Vehiculo
from utils.log import log

def listarVehiculos():
    log("[CRUD VEHICULO]: Funcion -> Listar vehiculos")
    miConn = Conn()
    
    # Campos que recuperamos
    # Num serie, matricula, marca
    comando = """
    SELECT v.numSerie, v.matricula, m.nombre
    FROM vehiculo AS v
    INNER JOIN marca AS m ON v.marca = m.codigo
    """
    
    log("[CRUD VEHICULO]: Obteniendo datos...")
    lista = miConn.lista(comando)
    log("[CRUD VEHICULO]: Datos obtenidos.")
    
    if not lista:
        log("[CRUD VEHICULO]: No hay vehiculos.")
        return []
    else:
        if len(lista)>0:
            log("[CRUD VEHICULO]: Si hay vehiculos.")
            datos = []
            for item in lista:
                datos.append(item)
                
            log("[CRUD VEHICULO]: Retornando datos...")
            return datos
                
                
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
                
def agregarVehiculo(objVehiculo):
    miConn = conn()

    comando = """
        INSERT INTO vehiculo
        (numSerie, matricula, proposito, fechaAdquisicion, disponibilidad,
         marca, modelo, licencia_requerida)
        VALUES ('{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}', '{7}')
    """.format(
        objVehiculo.get_num_serie(),
        objVehiculo.get_matricula(),
        objVehiculo.get_proposito(),
        objVehiculo.get_fecha_adquisicion(),
        objVehiculo.get_disponibilidad(),
        objVehiculo.get_marca(),
        objVehiculo.get_modelo(),
        objVehiculo.get_licencia_requerida()
    )

    return miConn.registrar(comando)


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