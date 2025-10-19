import Validar
from menus import (
    mAutorizar,
    mBitacoras,
    mMantenimiento,
    mObservaciones,
    mPrincipal,
    mSolicitudes,
    mUsuarios,
    mVehiculos,
)
from funciones import (
    fBitacora,
    fVehiculos,
    fMantenimiento,
    fObservaciones,
    fSolicitudes,
    fUsuarios,
    fAutorizar,
)

opc1 = 0
while opc1 != 8:
    opc1: int = Validar._SelectMenu("    Ingrese una opcion: ",
                                    mPrincipal._Principal, 1, 8)

    match opc1:
        case 1:  # -> Bitacoras
            opc11 = 0
            while opc11 != 4:
                opc11 = Validar._SelectMenu("\n    Ingrese una opcion: ",
                                            mBitacoras._Bitacoras, 1, 4)
                match opc11:
                    case 1:
                        opc112 = 0
                        while opc112 != 4:
                            opc112 = Validar._SelectMenu(
                                "\n    Ingrese una opcion: ",
                                mBitacoras._CrearBitacora,
                                1,
                                4,
                            )
                            match opc112:
                                case 1:
                                    fBitacora._Salida()
                                case 2:
                                    fBitacora._Entrada()
                                case 3:
                                    fBitacora._Generar()
                                case 4:
                                    print("Volver al menu de bitacora")
                    case 2:
                        fBitacora._Listado()
                    case 3:
                        fBitacora._Consulta()
                    case 4:
                        print("Volver al menu principal")
        case 2:  # -> Vehiculos
            opc12 = 0
            while opc12 != 6:
                opc12 = Validar._SelectMenu("    Ingrese una opcion: ",
                                            mVehiculos._Vehiculos, 1, 6)
                match opc12:
                    case 1:
                        fVehiculos._Listado()
                    case 2:
                        fVehiculos._Agregar()
                    case 3:
                        fVehiculos._Modificar()
                    case 4:
                        fVehiculos._Eliminar()
                    case 5:
                        fVehiculos._Suspender()
                    case 6:
                        print("Volver al menu principal")
                print()
        case 6:  # -> Mantenimiento
            opc13 = 0
            while opc13 != 6:
                opc13 = Validar._SelectMenu("Ingrese una opcion: ",
                                            mMantenimiento._Mantenimiento, 1,
                                            6)
                match opc13:
                    case 1:
                        fMantenimiento._Listado()
                    case 2:
                        fMantenimiento._Agregar()
                    case 6:
                        print("Volver al menu principal")
                print()
        case 7:  # -> Observaciones
            opc14 = 0
            while opc14 != 6:
                opc14 = Validar._SelectMenu("Ingrese una opcion: ",
                                            mObservaciones._Observaciones, 1,
                                            6)
                match opc14:
                    case 1:
                        fObservaciones._Listado()
                    case 2:
                        fObservaciones._Agregar()
                    case 6:
                        print("Volver al menu principal")
                print()
        case 4:  # -> Solicitudes
            opc15 = 0
            while opc15 != 6:
                opc15 = Validar._SelectMenu("    Ingrese una opcion: ",
                                            mSolicitudes._Solicitudes, 1, 6)
                match opc15:
                    case 1:
                        fSolicitudes._Listado()
                    case 2:
                        fSolicitudes._Levantar()
                    case 3:
                        fSolicitudes._Modificar()
                    case 4:
                        fSolicitudes._ConsultarEstado()
                    case 5:
                        fSolicitudes._Eliminar()
                    case 6:
                        print("Volver al menu principal")
                print()
        case 5:  # -> Ususarios
            opc16 = 0
            while opc16 != 6:
                opc16 = Validar._SelectMenu("    Ingrese una opcion: ",
                                            mUsuarios._Usuarios, 1, 6)
                match opc16:
                    case 1:
                        fUsuarios._Listado()
                    case 2:
                        fUsuarios._Registrar()
                    case 6:
                        print("    Volver al menu principal")
                print()
        case 3:  # -> Autorizar Solicitudes
            opc17 = 0
            while opc17 != 6:
                opc17 = Validar._SelectMenu("    Ingrese una opcion: ",
                                            mAutorizar._Autorizar, 1, 6)
                match opc17:
                    case 1:
                        fAutorizar._ListadoSolicitudes()
                    case 2:
                        fAutorizar._ListadoAutorizaciones()
                    case 6:
                        print("    Volver al menu principal")
                print()
        case 8:
            print("    Salio del sistema.")
            print()
