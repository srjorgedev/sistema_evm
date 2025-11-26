import domain.vehiculos.crudVehiculo as CRUD

def registrar_vehiculo(num_serie, matricula, marca, modelo, tipo, proposito):
    return CRUD.insertarVehiculo(num_serie, matricula, marca, modelo, tipo, proposito)

def obtener_lista():
    return CRUD.listarVehiculos()

def obtener_marcas():
    return CRUD.obtener_marcas()

def obtener_modelos():
    return CRUD.obtener_modelos()

def obtener_licencias():
    return CRUD.obtener_licencias()
