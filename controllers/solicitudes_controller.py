import domain.solicitudes.crudSolicitudes as CRUD 
import domain.vehiculos.crudVehiculo as CRUD_Vehiculo
from db.conn import conn

def lista_general():
    return CRUD.listarSolicitudes()

def lista_aceptadas():
    return CRUD.listarSolicitudes()

def lista_rechazadas():
    return CRUD.listarSolicitudes()

def obtener_vehiculos():
    """Obtiene lista de vehículos disponibles (id, matricula)"""
    return CRUD_Vehiculo.listarVehiculos()

def obtener_estados_solicitud():
    """Obtiene lista de estados de solicitud"""
    try:
        miConn = conn()
        comando = "SELECT numero, descripcion FROM edo_solicitud;"
        return miConn.lista(comando)
    except Exception as e:
        print(f"Error obteniendo estados: {e}")
        return []

