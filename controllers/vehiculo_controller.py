import domain.vehiculos.crudVehiculo as CRUD

def registrar_vehiculo(num_serie, matricula, marca, modelo, tipo, proposito):
    return CRUD.insertarVehiculo(num_serie, matricula, marca, modelo, tipo, proposito)

def obtener_lista():
    return CRUD.listarVehiculos()
