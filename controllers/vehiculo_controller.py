from domain.vehiculos.ClaseVehiculo import Vehiculo
from domain.vehiculos import crudVehiculo as crud
import db


def lista():
    lista= crud.listarVehiculos  ("SELECT matricula FROM vehiculo")
    return [Vehiculo(*lista) for lista in lista]