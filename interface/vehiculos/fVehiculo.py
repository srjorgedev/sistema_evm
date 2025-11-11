import domain.vehiculos.crudVehiculo as crudVehiculo
from domain.vehiculos.ClaseVehiculo import Vehiculo
import interface.vehiculos.val as val
from datetime import datetime


def listarVehiculos():
    print("   - - - Listado de Vehiculos - - -")
    crudVehiculo.listarVehiculos()


def SolicitarDatos():
    print("    - - - Agregar Vehiculo - - - ")
    num_serie = val.vNumSerie("Ingresa el numero de serie del vehiculo: ")
    matricula = val.vMatricula("Ingresa la matricula del vehiculo: ")
    marca = val.vDatos("Ingresa la marca del vehiculo: ")
    modelo = val.vDatos("Ingresa el modelo del vehiculo: ")
    color = val.vDatos("Ingresa el color del vehiculo: ")
    fecha_adquision = val.vFecha()
    tipo = val.vDatos("Ingresa el tipo de vehiculo: ")
    tipo_licencia = val.vTipoLicencia("Tipo de licencia requerida: ")
    capacidad_pasajeros = val.vCapacidad("Capacidad de pasajeros:")
    utilidad = val.vDatos("Utilidad del vehiculo: ")
    comentarios = val.vDatos("comentarios adicionales: ")
    nuevoVehiculo = Vehiculo("", num_serie, matricula, marca, modelo, color,
                             fecha_adquision, tipo, tipo_licencia,
                             capacidad_pasajeros, utilidad, comentarios)
    crudVehiculo.agregarVehiculo(nuevoVehiculo)


def borrarVehiculo():
    print("    - - - Eliminar Vehiculo - - - ")
    print(
        "   ADVERTENCIA: Esta acción es irreversible y puede afectar otros datos"
    )
    id_vehiculo = input("   Ingresa el ID del vehiculo a eliminar: ")
    existeVehiculo = Vehiculo(id_vehiculo, "", "", "", "", "", "", "", "", "",
                              "", "")
    crudVehiculo.borrarVehiculo(existeVehiculo)


def modificarMatricula():
    print("    - - - Modificar Matricula del Vehiculo - - - ")
    id_vehiculo = input("   Ingresa el ID del vehiculo a modificar: ")
    nueva_matricula = val.vMatricula("Ingresa la nueva matricula: ")
    existeVehiculo = Vehiculo(id_vehiculo, "", "", "", "", "", "", "", "", "",
                              "", "")
    existeVehiculo.set_matricula(nueva_matricula)
    crudVehiculo.modificarVehiculo(existeVehiculo)
