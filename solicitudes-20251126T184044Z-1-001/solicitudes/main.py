import fSolicitudes
import val
import menu

opc = 0
while opc != 5:
    opc = val.vOpciones("Ingrese una opción: ", 1, 5, menu.menuSolicitudes)
    match opc:
        case 1:
            fSolicitudes.listarSolicitudes()
        case 2:
            fSolicitudes.SolicitarDatos()
        case 3:
            fSolicitudes.modificarEstadoSolicitud()
        case 4:
            fSolicitudes.modificarAsuntoSolicitud()
        case 5:
            print("Saliendo...")

            

