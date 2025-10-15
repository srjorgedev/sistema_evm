import Menu, Validar, FunBitacora
from FunMenu import _Limpiar

_Limpiar()

opc1 = 0
while opc1 != 9:
    opc1: int = Validar._SelectMenu("Ingrese una opcion: ", Menu._Principal, 1, 8)

    match opc1:
        case 1: # -> Bitacoras
            opc11 = 0
            while opc11 != 5:
                opc11 = Validar._SelectMenu("\n    Ingrese una opcion: ", Menu._Bitacoras, 1, 6)
                match opc11:
                    case 1:
                        FunBitacora._Listado()
                        _Limpiar()
                    case 2:
                        opc112 = 0
                        while opc112 != 4:
                            opc112 = Validar._SelectMenu("\n    Ingrese una opcion: ", Menu._CrearBitacora, 1, 4)
                    case 3:
                        print("Editar bitacora")
                        print("En construccion...")
                    case 4:
                        print("Consultar bitacora")
                        print("En construccion...")
                    case 5:
                        print("Volver al menu principal")
        case 2: # -> Vehiculos
            opc12 = 0
            while opc12 != 6:
                opc12 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Vehiculos, 1, 6)
                match opc12:
                    case 1:
                        print("Listado de vehiculos")
                        print("En construccion...")
                    case 2:
                        print("Agregar vehiculo")
                        print("En construccion...")
                    case 3:
                        print("Modificar informacion de vehiculo")
                        print("En construccion...")
                    case 4:
                        print("Eliminar vehiculo")
                        print("En construccion...")
                    case 5:
                        print("Suspender vehiculo")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 3: # -> Mantenimiento
            opc13 = 0
            while opc13 != 6:
                opc13 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Mantenimiento, 1, 6)
                match opc13:
                    case 1:
                        print("Listado de mantenimientos")
                        print("En construccion...")
                    case 2:
                        print("Solicitar mantenimiento")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 4: # -> Observaciones
            opc14 = 0
            while opc14 != 6:
                opc14 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Observaciones, 1, 6)
                match opc14:
                    case 1:
                        print("Listado de observaciones")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 5: # -> Solicitudes
            opc15 = 0
            while opc15 != 6:
                opc15 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Solicitudes, 1, 6)
                match opc15:
                    case 1:
                        print("Listado de solicitudes")
                        print("En construccion...")
                    case 2:
                        print("Levantar solicitud")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 6: # -> Ususarios
            opc16 = 0
            while opc16 != 6:
                opc16 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Usuarios, 1, 6)
                match opc16:
                    case 1:
                        print("Listado de usuarios")
                        print("En construccion...")
                    case 2:
                        print>("Registrar usuario")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 7: # -> Autorizar Solicitudes
            opc17 = 0
            while opc17 != 6:
                opc17 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Autorizar, 1, 6)
                match opc17:
                    case 1:
                        print("Listado de Solicitudes")
                    case 2:
                        print("Listado de autorizaciones")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 8:
            print("Salio del sistema.")
            print()
