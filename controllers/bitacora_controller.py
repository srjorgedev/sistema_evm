import domain.bitacoras.CRUD as CRUD
from domain.bitacoras.Clase import Bitacora
import interface.bitacoras.Val as Val
from utils.log import log

def lista():
    log("[CTRL BIT]: Funcion -> LISTA GENERAL")
    try:
        log("[CTRL BIT]: Obteniendo datos del CRUD")
        resultado = CRUD.listaGeneral()
        log("[CTRL BIT]: Datos obtenidos, retornando...")
        return resultado
    except Exception as e:
        log("[CTRL BIT]: Ocurrió un error, retornando...")
        raise
    
def lista_archivados():
    log("[CTRL BIT]: Funcion -> LISTA ARCHIVADOS")
    # log("Entré a FBitacora.lista")
    try:
        # log("Ejecutando CRUD.listaGeneral...")
        resultado = CRUD.listaArchivados()
        # log("Resultado:", resultado)
        return resultado
    except Exception as e:
        # log("ERROR dentro de lista():", e)
        raise
        

# Logica similar al de eliminar
def archivar(data: int):
    log("[CTRL BIT]: Funcion -> ARCHIVAR")
    try: 
        log("[CTRL BIT]: Iniciando...")
        r = CRUD.archivar(data)
        log("[CTRL BIT]: Terminado.")
        log(f"[CTRL BIT]: Retorno -> {r}")
    except Exception as e:
        log("[CTRL BIT]: Error ->")
        log(e)
    

def registrarSalida():
    log("   \n-- Registrar salida --")

    asunto = Val.Str("Asunto: ")
    destino = Val.Str("Destino: ")
    kilometraje = Val.Float("Kilometraje: ")
    gasolina = Val.Float("Gasolina: ")

    bitacora = Bitacora()
    bitacora.set_asunto(asunto)
    bitacora.set_destino(destino)
    bitacora.registrar_salida(kilometraje, gasolina)

    lastid = CRUD.crearSalida(bitacora)

    if (lastid == -1):
        log("   No se pudo registrar.")
        return
    else:
        log("   Bitacora registrada.")
    log()

    bitacora.set_numControl(lastid)

    log(bitacora)


def registrarEntrada():
    log("   \n-- Registrar entrada --")

    log("   Bitacoras sin entrada:")
    bitacoras_sin_entrada = CRUD.bitacoraSinEntrada()
    log()

    if bitacoras_sin_entrada == 0:
        log("   No hay bitacoras.")
        return

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        log(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    bitacora = completar_objeto(bitacora, existe[0])

    kilometraje = Val.KMEntrada("Kilometraje: ",
                                bitacora.get_salida().get_kilometraje())
    gasolina = Val.GasEntrada("Gasolina: ",
                              bitacora.get_salida().get_gasolina())

    bitacora.registrar_entrada(kilometraje, gasolina)
    bitacora.calcular_gasolinaConsumida()
    bitacora.calcular_kilometrajeTotal()
    bitacora.calcular_gasolinaRendimiento()

    rowcount = CRUD.crearEntrada(bitacora)
    if rowcount == -1:
        log("   No se pudo registrar la entrada.")
        return

    log(bitacora)


def eliminar():
    log("   \n-- Eliminar --")
    log("   Bitacoras:")
    bitacoras = CRUD.listaGeneral()
    log()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        log(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    elegir = Val.Decision("Borrar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.baja(bitacora)
        if rowcount == -1:
            log("   No se pudo eliminar la bitacora.")
            return

        log("   Bitacora eliminada.")
    else:
        log("   Eliminacion cancelada.")
    log()


def modificar():
    log("   \n-- Modificar destino --")
    bitacoras = CRUD.listaGeneral()
    log()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        log(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    nuevoDestino = Val.Str("Nuevo destino: ")

    bitacora.set_destino(nuevoDestino)

    elegir = Val.Decision("Modificar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.actualizarDestino(bitacora)
        if rowcount == -1:
            log("   No se pudo actualizar la bitacora.")
            return

        log("   Destino actualizado.")
    else:
        log("   Actualizacion cancelada.")
    log()


def completar_objeto(bitacora: Bitacora, tupla):
    bitacora.set_asunto(tupla[0])
    bitacora.set_destino(tupla[1])
    bitacora.set_responsable(tupla[2])
    bitacora.set_autorizador(tupla[3])
    bitacora.set_vehiculo(tupla[4])
    bitacora.registrar_salida(tupla[5], tupla[6])
    bitacora.get_salida().set_fecha(tupla[7])
    bitacora.get_salida().set_hora(tupla[7])

    return bitacora
