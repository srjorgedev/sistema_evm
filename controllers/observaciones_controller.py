import domain.observaciones.CRUD as CRUD 
from utils.log import log

def lista_tipos():
    log("[CTRL OBS]: Funcion -> LISTA GENERAL")
    try:
        log("[CTRL OBS]: Obteniendo datos del CRUD")
        resultado = CRUD.lista_tipos_observacion()
        log("[CTRL OBS]: Datos obtenidos, retornando...")
        return resultado
    except Exception as e:
        log("[CTRL OBS]: Ocurrió un error, retornando...")
        raise