from domain.vehiculos.ClaseVehiculo import Vehiculo
from domain.vehiculos import crudVehiculo as crud

def lista():
    lista= crud.listarVehiculos()
    return [Vehiculo(*lista) for lista in lista]
