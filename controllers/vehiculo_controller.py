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

def modificar_matricula(num_serie, nueva_matricula):
    """Wrapper de controlador para actualizar la matrícula por número de serie.
    Devuelve una tupla (ok: bool, mensaje: str).
    """
    try:
        contador = CRUD.actualizar_matricula_por_serie(num_serie, nueva_matricula)
        if contador and int(contador) > 0:
            return True, "Matrícula actualizada correctamente."
        else:
            return False, "No se encontró el vehículo o no se realizó ningún cambio."
    except Exception as e:
        return False, f"Error al actualizar matrícula: {e}"

def borrar_vehiculo(num_serie, motivo=None):
    """Envuelve la operación CRUD de borrado de vehículo por número de serie.

    Devuelve (True, mensaje) si se eliminaron filas, (False, mensaje) en caso contrario.
    """
    try:
        filas = CRUD.borrar_por_num_serie(num_serie)
        if filas > 0:
            msg = "Vehículo eliminado correctamente."
            if motivo:
                msg += f" Motivo: {motivo}"
            return True, msg
        else:
            return False, "No se encontró el vehículo con ese número de serie."
    except Exception as e:
        return False, str(e)
