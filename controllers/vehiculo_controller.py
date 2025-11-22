from domain.vehiculos.ClaseVehiculo import Vehiculo
from domain.vehiculos import crudVehiculo as crud

def lista():
    registros = crud.listarVehiculos()
    vehiculos = [Vehiculo(*fila) for fila in registros]  # cada fila debe tener los 12 campos
    return vehiculos