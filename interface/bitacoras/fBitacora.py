import domain.bitacoras.crudBitacora as CRUD
from domain.bitacoras.ClaseBitacora import Bitacora
import interface.bitacoras.Val as Val


def lista():
    print("   \n-- Lista de bitacoras --")
    print(
        f"{'N.Ctrl':<8}{'Asunto':<35}{'Destino':<15}{'Salida':<10}{'Entrada':<10}"
    )

    CRUD.listaGeneral()
    print()


def registrarSalida():
    print("   \n-- Registrar salida --")

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
        print("   No se pudo registrar.")
        return
    else:
        print("   Bitacora registrada.")
    print()

    bitacora.set_numControl(lastid)

    print(bitacora)


def registrarEntrada():
    print("   \n-- Registrar entrada --")

    print("   Bitacoras sin entrada:")
    bitacoras_sin_entrada = CRUD.bitacoraSinEntrada()
    print()

    if bitacoras_sin_entrada == 0:
        print("   No hay bitacoras.")
        return

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
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
        print("   No se pudo registrar la entrada.")
        return

    print(bitacora)


def eliminar():
    print("   \n-- Eliminar --")
    print("   Bitacoras:")
    bitacoras = CRUD.listaGeneral()
    print()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    elegir = Val.Decision("Borrar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.baja(bitacora)
        if rowcount == -1:
            print("   No se pudo eliminar la bitacora.")
            return

        print("   Bitacora eliminada.")
    else:
        print("   Eliminacion cancelada.")
    print()


def modificar():
    print("   \n-- Modificar destino --")
    bitacoras = CRUD.listaGeneral()
    print()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    nuevoDestino = Val.Str("Nuevo destino: ")

    bitacora.set_destino(nuevoDestino)

    elegir = Val.Decision("Modificar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.actualizarDestino(bitacora)
        if rowcount == -1:
            print("   No se pudo actualizar la bitacora.")
            return

        print("   Destino actualizado.")
    else:
        print("   Actualizacion cancelada.")
    print()


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
